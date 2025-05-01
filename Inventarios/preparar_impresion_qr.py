import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import math
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import traceback

def crear_plantilla_etiquetas(directorio_qr, archivo_salida, etiquetas_por_fila=3, filas_por_pagina=8, 
                             margen_mm=10, espaciado_mm=5, ancho_etiqueta_mm=25, alto_etiqueta_mm=25):
    """
    Crea un PDF con múltiples códigos QR organizados en forma de etiquetas para imprimir
    
    Parámetros:
    - directorio_qr: Ruta a la carpeta con los archivos PNG de códigos QR
    - archivo_salida: Nombre del archivo PDF a generar
    - etiquetas_por_fila: Número de etiquetas por fila
    - filas_por_pagina: Número de filas por página
    - margen_mm: Margen de la página en milímetros
    - espaciado_mm: Espacio entre etiquetas en milímetros
    - ancho_etiqueta_mm: Ancho de cada etiqueta en milímetros
    - alto_etiqueta_mm: Alto de cada etiqueta en milímetros
    """
    try:
        print(f"Procesando etiquetas en {directorio_qr}...")
        # Convertir mm a puntos (1 punto = 0.352778 mm)
        mm_a_puntos = 2.83465
        
        margen = margen_mm * mm_a_puntos
        espaciado = espaciado_mm * mm_a_puntos
        ancho_etiqueta = ancho_etiqueta_mm * mm_a_puntos
        alto_etiqueta = alto_etiqueta_mm * mm_a_puntos
        
        # Obtener lista de archivos de códigos QR
        print("Listando archivos de códigos QR...")
        archivos_qr = [f for f in os.listdir(directorio_qr) if f.endswith('.png') and f != 'registro_qr.xlsx']
        print(f"Se encontraron {len(archivos_qr)} archivos QR")
        
        # Si existe un registro de QR, ordenar los archivos según los números de activo
        registro_qr_path = os.path.join(directorio_qr, 'registro_qr.xlsx')
        if os.path.exists(registro_qr_path):
            try:
                print("Ordenando archivos según registro...")
                df_registro = pd.read_excel(registro_qr_path)
                # Ordenar archivos según NoAct
                archivos_ordenados = []
                for _, row in df_registro.iterrows():
                    nombre_archivo = row['Nombre_Archivo']
                    if nombre_archivo in archivos_qr:
                        archivos_ordenados.append(nombre_archivo)
                        archivos_qr.remove(nombre_archivo)
                # Añadir cualquier archivo que no esté en el registro al final
                archivos_ordenados.extend(archivos_qr)
                archivos_qr = archivos_ordenados
                print(f"Se ordenaron {len(archivos_ordenados)} archivos")
            except Exception as e:
                print(f"Error al leer el registro de QR: {e}")
                print("Se utilizará el orden alfabético de los archivos.")
        
        # Crear el PDF
        print(f"Creando PDF en {archivo_salida}...")
        c = canvas.Canvas(archivo_salida, pagesize=letter)
        ancho_pagina, alto_pagina = letter
        
        # Calcular etiquetas por página
        etiquetas_por_pagina = etiquetas_por_fila * filas_por_pagina
        
        # Calcular número de páginas necesarias
        num_paginas = math.ceil(len(archivos_qr) / etiquetas_por_pagina)
        print(f"Se generarán {num_paginas} páginas")
        
        for pagina in range(num_paginas):
            print(f"Procesando página {pagina+1}/{num_paginas}...")
            # Índice inicial para esta página
            idx_inicial = pagina * etiquetas_por_pagina
            
            for i in range(etiquetas_por_pagina):
                if idx_inicial + i >= len(archivos_qr):
                    break
                    
                # Calcular posición de la etiqueta
                fila = i // etiquetas_por_fila
                columna = i % etiquetas_por_fila
                
                # Calcular coordenadas x, y (desde la esquina inferior izquierda)
                x = margen + columna * (ancho_etiqueta + espaciado)
                y = alto_pagina - margen - (fila + 1) * (alto_etiqueta + espaciado)
                
                # Abrir imagen del código QR
                ruta_qr = os.path.join(directorio_qr, archivos_qr[idx_inicial + i])
                print(f"Procesando imagen: {ruta_qr}")
                img = Image.open(ruta_qr)
                
                # Crear archivo temporal para esta imagen
                temp_path = f"temp_qr_{i}.png"
                img.save(temp_path)
                
                # Insertar imagen en el PDF
                c.drawImage(temp_path, x, y, width=ancho_etiqueta, height=alto_etiqueta)
                
                # Extraer No. Activo del nombre del archivo
                no_act = archivos_qr[idx_inicial + i].replace('.png', '')
                
                # Dibujar texto del No. Activo debajo del QR
                c.setFont("Helvetica", 6)
                c.drawCentredString(x + ancho_etiqueta/2, y - 8, no_act)
                
                # Eliminar archivo temporal
                os.remove(temp_path)
            
            # Agregar nueva página si no es la última
            if pagina < num_paginas - 1:
                c.showPage()
        
        # Guardar el PDF
        c.save()
        print(f"PDF de etiquetas creado: {archivo_salida}")
        print(f"Configuración: {etiquetas_por_fila}x{filas_por_pagina} etiquetas")
        print(f"Tamaño de etiqueta: {ancho_etiqueta_mm}x{alto_etiqueta_mm} mm")

    except Exception as e:
        print(f"Error en crear_plantilla_etiquetas: {e}")
        traceback.print_exc()

def crear_plantillas_multiformato():
    """
    Crea múltiples plantillas de etiquetas con diferentes formatos
    """
    try:
        # Usar rutas relativas en lugar de absolutas
        directorio_qr = "codigos_qr"
        
        # Verificar si existe la carpeta de códigos QR
        if not os.path.exists(directorio_qr):
            print(f"Error: El directorio {directorio_qr} no existe.")
            print("Ejecute primero 'generar_qr.py' para crear los códigos QR.")
            return
        
        # Verificar si hay códigos QR en la carpeta
        archivos_qr = [f for f in os.listdir(directorio_qr) if f.endswith('.png') and f != 'registro_qr.xlsx']
        if not archivos_qr:
            print(f"Error: No se encontraron códigos QR en {directorio_qr}.")
            print("Ejecute primero 'generar_qr.py' para crear los códigos QR.")
            return
        
        # Crear carpeta para los PDF si no existe
        directorio_pdf = "plantillas_impresion"
        if not os.path.exists(directorio_pdf):
            os.makedirs(directorio_pdf)
            print(f"Carpeta creada: {directorio_pdf}")
        
        # Crear plantillas con diferentes configuraciones
        
        # 1. Plantilla estándar 3x8 (24 etiquetas por página)
        print("\n1. Generando plantilla estándar 3x8...")
        archivo_salida = os.path.join(directorio_pdf, "etiquetas_estandar_3x8.pdf")
        crear_plantilla_etiquetas(
            directorio_qr, 
            archivo_salida, 
            etiquetas_por_fila=3, 
            filas_por_pagina=8,
            ancho_etiqueta_mm=25, 
            alto_etiqueta_mm=25
        )
        
        # 2. Plantilla compacta 4x10 (40 etiquetas por página)
        print("\n2. Generando plantilla compacta 4x10...")
        archivo_salida = os.path.join(directorio_pdf, "etiquetas_compactas_4x10.pdf")
        crear_plantilla_etiquetas(
            directorio_qr, 
            archivo_salida, 
            etiquetas_por_fila=4, 
            filas_por_pagina=10,
            ancho_etiqueta_mm=20, 
            alto_etiqueta_mm=20,
            margen_mm=8,
            espaciado_mm=3
        )
        
        # 3. Plantilla grande 2x5 (10 etiquetas por página)
        print("\n3. Generando plantilla grande 2x5...")
        archivo_salida = os.path.join(directorio_pdf, "etiquetas_grandes_2x5.pdf")
        crear_plantilla_etiquetas(
            directorio_qr, 
            archivo_salida, 
            etiquetas_por_fila=2, 
            filas_por_pagina=5,
            ancho_etiqueta_mm=40, 
            alto_etiqueta_mm=40,
            margen_mm=15,
            espaciado_mm=10
        )
        
        # 4. Plantilla para hoja Avery estándar 3x10 (30 etiquetas por página)
        print("\n4. Generando plantilla Avery 3x10...")
        archivo_salida = os.path.join(directorio_pdf, "etiquetas_avery_3x10.pdf")
        crear_plantilla_etiquetas(
            directorio_qr, 
            archivo_salida, 
            etiquetas_por_fila=3, 
            filas_por_pagina=10,
            ancho_etiqueta_mm=25.4, 
            alto_etiqueta_mm=23.5,
            margen_mm=8.5,
            espaciado_mm=2.5
        )
        
        print("\nInstrucciones para imprimir:")
        print("1. Abra los archivos PDF generados en la carpeta 'plantillas_impresion'")
        print("2. Al imprimir, asegúrese de seleccionar 'Tamaño real' o 'Sin ajuste de escala'")
        print("3. Haga una prueba con una hoja normal antes de usar las etiquetas adhesivas")
        print("4. Elija el formato que mejor se adapte a sus hojas de etiquetas")
    
    except Exception as e:
        print(f"Error en crear_plantillas_multiformato: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    crear_plantillas_multiformato()
