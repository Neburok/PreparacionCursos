import pandas as pd
import qrcode
import os
from datetime import datetime

# Carpeta para guardar los códigos QR
carpeta_qr = "/Users/nebur/ProyectosIA/Inventarios/codigos_qr"
if not os.path.exists(carpeta_qr):
    os.makedirs(carpeta_qr)
    print(f"Carpeta creada: {carpeta_qr}")

# Ruta al archivo Excel generado por el script anterior
excel_path = "/Users/nebur/ProyectosIA/Inventarios/Formato_Diagnostico_Inventario.xlsx"

# Verificar si el archivo existe
if not os.path.exists(excel_path):
    print(f"El archivo {excel_path} no existe.")
    print("Ejecute primero 'generar_formato.py' para crear el archivo Excel.")
    exit(1)

# Cargar datos del Excel
print(f"Cargando datos desde {excel_path}...")
df = pd.read_excel(excel_path)
print(f"Se cargaron {len(df)} registros.")

# Crear un DataFrame para almacenar información de los códigos QR
qr_info = pd.DataFrame(columns=["NoAct", "Tipo", "Nombre_Archivo", "Fecha_Generacion"])

# Contador para seguimiento del progreso
total = len(df)
contador = 0

# Generar código QR para cada bien
print("Generando códigos QR...")
for index, row in df.iterrows():
    contador += 1
    if contador % 10 == 0 or contador == total:
        print(f"Progreso: {contador}/{total} ({int(contador/total*100)}%)")
    
    # Obtener información del bien
    no_act = row["NoAct"]
    tipo = row["Tipo"]
    descripcion = row["Descripcion"]
    ubicacion = f"{row['Edificio']} - {row['Planta']} - {row['Area']}"
    
    # Información a incluir en el código QR
    qr_data = f"""No. Activo: {no_act}
Tipo: {tipo}
Descripción: {descripcion}
Ubicación registrada: {ubicacion}
Responsable: Rubén Velázquez Hernández
División: Industrial
Fecha de verificación: __/__/____
Estado: ____________
Observaciones: __________________________
________________________________________
"""
    
    # Crear el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    # Crear imagen del código QR
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Nombre del archivo (usando el número de activo)
    nombre_archivo = f"{no_act}.png"
    ruta_completa = os.path.join(carpeta_qr, nombre_archivo)
    
    # Guardar imagen
    img.save(ruta_completa)
    
    # Registrar información
    qr_info.loc[len(qr_info)] = {
        "NoAct": no_act,
        "Tipo": tipo,
        "Nombre_Archivo": nombre_archivo,
        "Fecha_Generacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# Guardar el registro de códigos QR generados
registro_path = os.path.join(carpeta_qr, "registro_qr.xlsx")
qr_info.to_excel(registro_path, index=False)

print(f"\nSe han generado {len(qr_info)} códigos QR.")
print(f"Los códigos QR se encuentran en: {carpeta_qr}")
print(f"El registro de códigos QR generados está en: {registro_path}")

print("\nRecomendaciones para la impresión de códigos QR:")
print("1. Imprima los códigos QR en etiquetas adhesivas resistentes")
print("2. Tamaño recomendado: 2.5 cm x 2.5 cm")
print("3. Use impresión láser para mayor durabilidad")
print("4. Proteja las etiquetas con cinta transparente si estarán expuestas")
print("   a condiciones adversas (humedad, polvo, manipulación frecuente)")
