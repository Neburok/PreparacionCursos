import os
import pandas as pd
import qrcode
import datetime
from tkinter import Tk, Label, Button, Entry, Text, Scrollbar, Frame, StringVar, messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

class VerificadorInventario:
    def __init__(self, root):
        self.root = root
        self.root.title("Verificador de Inventario")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Variables
        self.inventario_file = None
        self.df_inventario = None
        self.items_verificados = []
        self.codigo_var = StringVar()
        
        # Interfaz
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Frame superior para cargar el inventario
        frame_top = Frame(self.root, padx=10, pady=10)
        frame_top.pack(fill='x')
        
        Label(frame_top, text="Archivo de Inventario:").grid(row=0, column=0, sticky='w')
        self.lbl_archivo = Label(frame_top, text="No seleccionado", fg="red")
        self.lbl_archivo.grid(row=0, column=1, sticky='w')
        
        Button(frame_top, text="Seleccionar Archivo", command=self.cargar_inventario).grid(row=0, column=2, padx=5)
        
        # Frame para escaneo/entrada de códigos
        frame_scan = Frame(self.root, padx=10, pady=10)
        frame_scan.pack(fill='x')
        
        Label(frame_scan, text="Ingrese/Escanee Código:").grid(row=0, column=0, sticky='w')
        self.entry_codigo = Entry(frame_scan, textvariable=self.codigo_var, width=20)
        self.entry_codigo.grid(row=0, column=1, padx=5)
        self.entry_codigo.bind('<Return>', self.verificar_item)
        
        Button(frame_scan, text="Verificar", command=self.verificar_item).grid(row=0, column=2, padx=5)
        
        # Frame para mostrar resultados
        frame_results = Frame(self.root, padx=10, pady=10)
        frame_results.pack(fill='both', expand=True)
        
        # Área de texto para mostrar los resultados
        Label(frame_results, text="Items Verificados:").pack(anchor='w')
        
        text_frame = Frame(frame_results)
        text_frame.pack(fill='both', expand=True)
        
        self.text_resultados = Text(text_frame, height=15, width=70)
        self.text_resultados.pack(side='left', fill='both', expand=True)
        
        scrollbar = Scrollbar(text_frame, command=self.text_resultados.yview)
        scrollbar.pack(side='right', fill='y')
        
        self.text_resultados.config(yscrollcommand=scrollbar.set)
        
        # Botones de acción
        frame_buttons = Frame(self.root, padx=10, pady=10)
        frame_buttons.pack(fill='x')
        
        Button(frame_buttons, text="Exportar Reporte", command=self.exportar_reporte).pack(side='left', padx=5)
        Button(frame_buttons, text="Nueva Verificación", command=self.nueva_verificacion).pack(side='left', padx=5)
        
        # Mostrar información inicial
        self.text_resultados.insert('end', "Instrucciones:\n")
        self.text_resultados.insert('end', "1. Seleccione el archivo de inventario (Excel)\n")
        self.text_resultados.insert('end', "2. Escanee o ingrese manualmente el código de cada ítem\n")
        self.text_resultados.insert('end', "3. Presione Enter o el botón 'Verificar'\n")
        self.text_resultados.insert('end', "4. Al finalizar, exporte el reporte de verificación\n\n")
        self.text_resultados.config(state='disabled')
    
    def cargar_inventario(self):
        # Abrir diálogo para seleccionar archivo
        filename = askopenfilename(
            title="Seleccionar archivo de inventario",
            filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*"))
        )
        
        if not filename:
            return
        
        try:
            # Cargar el archivo Excel
            self.df_inventario = pd.read_excel(filename, sheet_name="Inventario")
            self.inventario_file = filename
            
            # Verificar estructura
            if 'ID_Inventario' not in self.df_inventario.columns:
                messagebox.showerror("Error", "El archivo no contiene la columna 'ID_Inventario'")
                self.df_inventario = None
                self.inventario_file = None
                return
            
            # Actualizar interfaz
            self.lbl_archivo.config(text=os.path.basename(filename), fg="green")
            
            # Habilitar área de texto y limpiarla
            self.text_resultados.config(state='normal')
            self.text_resultados.delete(1.0, 'end')
            self.text_resultados.insert('end', f"Inventario cargado: {os.path.basename(filename)}\n")
            self.text_resultados.insert('end', f"Total de items: {len(self.df_inventario)}\n\n")
            self.text_resultados.insert('end', "Comience a escanear o ingresar los códigos de inventario.\n\n")
            self.text_resultados.config(state='disabled')
            
            # Limpiar lista de verificados
            self.items_verificados = []
            
            # Enfocar en el campo de entrada
            self.entry_codigo.focus()
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {str(e)}")
    
    def verificar_item(self, event=None):
        # Verificar que se haya cargado el inventario
        if self.df_inventario is None:
            messagebox.showwarning("Advertencia", "Primero debe cargar un archivo de inventario.")
            return
        
        # Obtener el código ingresado
        codigo = self.codigo_var.get().strip()
        if not codigo:
            return
        
        # Buscar en el DataFrame
        encontrado = False
        item_info = {}
        
        # Primero buscar coincidencia exacta con ID_Inventario
        if codigo in self.df_inventario['ID_Inventario'].values:
            encontrado = True
            item = self.df_inventario[self.df_inventario['ID_Inventario'] == codigo].iloc[0]
            item_info = {
                'ID_Inventario': item['ID_Inventario'],
                'Descripcion': item['Descripcion'],
                'Ubicacion': f"{item['Edificio']} - {item['Planta']} - {item['Area_Especifica']}",
                'Estado': item['Estado_Actual'],
                'Fecha_Verificacion': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        
        # Actualizar interfaz
        self.text_resultados.config(state='normal')
        if encontrado:
            # Verificar si ya se verificó este ítem
            ya_verificado = False
            for item in self.items_verificados:
                if item['ID_Inventario'] == codigo:
                    ya_verificado = True
                    break
            
            if ya_verificado:
                self.text_resultados.insert('end', f"[{item_info['Fecha_Verificacion']}] DUPLICADO: {codigo} - {item_info['Descripcion']}\n")
            else:
                self.text_resultados.insert('end', f"[{item_info['Fecha_Verificacion']}] VERIFICADO: {codigo} - {item_info['Descripcion']}\n")
                self.items_verificados.append(item_info)
        else:
            self.text_resultados.insert('end', f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] NO ENCONTRADO: {codigo}\n")
        
        self.text_resultados.see('end')
        self.text_resultados.config(state='disabled')
        
        # Limpiar y enfocar el campo de entrada
        self.codigo_var.set("")
        self.entry_codigo.focus()
    
    def exportar_reporte(self):
        if not self.items_verificados:
            messagebox.showwarning("Advertencia", "No hay datos para exportar.")
            return
        
        try:
            # Crear DataFrame con los items verificados
            df_reporte = pd.DataFrame(self.items_verificados)
            
            # Calcular estadísticas
            if self.df_inventario is not None:
                total_items = len(self.df_inventario)
                items_verificados = len(self.items_verificados)
                porcentaje = round(items_verificados / total_items * 100, 2)
                
                # Crear DataFrame con el resumen
                df_resumen = pd.DataFrame([{
                    'Fecha_Verificacion': datetime.datetime.now().strftime('%Y-%m-%d'),
                    'Total_Items': total_items,
                    'Items_Verificados': items_verificados,
                    'Porcentaje': f"{porcentaje}%",
                    'Verificado_Por': os.getlogin()
                }])
            
            # Generar nombre del archivo con la fecha actual
            fecha_str = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            export_file = f"Verificacion_Inventario_{fecha_str}.xlsx"
            
            # Crear el archivo Excel con dos hojas
            with pd.ExcelWriter(export_file) as writer:
                df_reporte.to_excel(writer, sheet_name='Items_Verificados', index=False)
                if self.df_inventario is not None:
                    df_resumen.to_excel(writer, sheet_name='Resumen', index=False)
            
            messagebox.showinfo("Éxito", f"Reporte exportado a {export_file}")
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo exportar el reporte: {str(e)}")
    
    def nueva_verificacion(self):
        # Reiniciar estado
        self.items_verificados = []
        
        # Actualizar interfaz
        self.text_resultados.config(state='normal')
        self.text_resultados.delete(1.0, 'end')
        
        if self.df_inventario is not None:
            self.text_resultados.insert('end', f"Inventario cargado: {os.path.basename(self.inventario_file)}\n")
            self.text_resultados.insert('end', f"Total de items: {len(self.df_inventario)}\n\n")
            self.text_resultados.insert('end', "Nueva verificación iniciada. Comience a escanear.\n\n")
        else:
            self.text_resultados.insert('end', "Instrucciones:\n")
            self.text_resultados.insert('end', "1. Seleccione el archivo de inventario (Excel)\n")
            self.text_resultados.insert('end', "2. Escanee o ingrese manualmente el código de cada ítem\n")
            self.text_resultados.insert('end', "3. Presione Enter o el botón 'Verificar'\n")
            self.text_resultados.insert('end', "4. Al finalizar, exporte el reporte de verificación\n\n")
            
        self.text_resultados.config(state='disabled')
        self.codigo_var.set("")
        self.entry_codigo.focus()

def main():
    """Función principal para iniciar la aplicación"""
    root = Tk()
    app = VerificadorInventario(root)
    root.mainloop()

if __name__ == "__main__":
    main() 