import pandas as pd
import os

# Definir rutas de archivos
em_path = "/Users/nebur/ProyectosIA/Inventarios/RESGARDO_EM_VHR.csv"
bm_path = "/Users/nebur/ProyectosIA/Inventarios/RESGUARDO_BM_VHR.csv"
output_path = "/Users/nebur/ProyectosIA/Inventarios/Formato_Diagnostico_Inventario.xlsx"

# Leer CSV de enseres menores
em_df = pd.read_csv(em_path)
print(f"Enseres menores cargados: {len(em_df)} registros")

# Leer CSV de bienes muebles
bm_df = pd.read_csv(bm_path)
print(f"Bienes muebles cargados: {len(bm_df)} registros")

# Renombrar columnas para unificar (si es necesario)
if 'No.Act' in bm_df.columns:
    bm_df = bm_df.rename(columns={'No.Act': 'NoAct', 'Descripción': 'Descripcion', 'No. serie': 'NoSerie'})

# Función para extraer información de ubicación del comentario
def extraer_info(comentario):
    """Extrae información de ubicación y estado del comentario."""
    edificio = "No especificado"
    planta = "No especificado"
    area = "No especificado"
    estado = "No especificado"
    
    if isinstance(comentario, str):
        # Extraer edificio
        if "EDIFICIO:" in comentario:
            partes = comentario.split("EDIFICIO:")
            if len(partes) > 1:
                info_resto = partes[1].strip()
                
                # Extraer edificio
                if "PLANTA:" in info_resto:
                    edificio = info_resto.split("PLANTA:")[0].strip()
                
                # Extraer planta
                if "PLANTA:" in info_resto:
                    planta_info = info_resto.split("PLANTA:")[1]
                    if "CUBÍCULO" in planta_info:
                        planta = planta_info.split("CUBÍCULO")[0].strip()
                    elif "LABORATORIO" in planta_info:
                        planta = planta_info.split("LABORATORIO")[0].strip()
                    elif "ÁREA:" in planta_info:
                        planta = planta_info.split("ÁREA:")[0].strip()
                
                # Extraer área/cubículo/laboratorio
                if "ÁREA:" in info_resto:
                    area_info = info_resto.split("ÁREA:")[1]
                    if "EDO.DEL BIEN:" in area_info:
                        area = area_info.split("EDO.DEL BIEN:")[0].strip()
                    elif "ESTADO DEL BIEN:" in area_info:
                        area = area_info.split("ESTADO DEL BIEN:")[0].strip()
                    else:
                        area = area_info.strip()
                elif "CUBÍCULO" in info_resto:
                    area_info = "CUBÍCULO " + info_resto.split("CUBÍCULO")[1]
                    if "EDO.DEL BIEN:" in area_info:
                        area = area_info.split("EDO.DEL BIEN:")[0].strip()
                    elif "ESTADO DEL BIEN:" in area_info:
                        area = area_info.split("ESTADO DEL BIEN:")[0].strip()
                    else:
                        area = area_info.strip()
                elif "LABORATORIO" in info_resto:
                    area_info = "LABORATORIO " + info_resto.split("LABORATORIO")[1]
                    if "EDO.DEL BIEN:" in area_info:
                        area = area_info.split("EDO.DEL BIEN:")[0].strip()
                    elif "ESTADO DEL BIEN:" in area_info:
                        area = area_info.split("ESTADO DEL BIEN:")[0].strip()
                    else:
                        area = area_info.strip()
                
                # Extraer estado
                if "EDO.DEL BIEN:" in info_resto:
                    estado = info_resto.split("EDO.DEL BIEN:")[1].strip()
                elif "ESTADO DEL BIEN:" in info_resto:
                    estado = info_resto.split("ESTADO DEL BIEN:")[1].strip()
    
    return edificio, planta, area, estado

# Aplicar extracción de información
print("Procesando datos de ubicación para enseres menores...")
em_info = [extraer_info(comentario) for comentario in em_df['Comentarios']]
em_df['Edificio'] = [info[0] for info in em_info]
em_df['Planta'] = [info[1] for info in em_info]
em_df['Area'] = [info[2] for info in em_info]
em_df['Estado_Original'] = [info[3] for info in em_info]

print("Procesando datos de ubicación para bienes muebles...")
bm_info = [extraer_info(comentario) for comentario in bm_df['Comentarios']]
bm_df['Edificio'] = [info[0] for info in bm_info]
bm_df['Planta'] = [info[1] for info in bm_info]
bm_df['Area'] = [info[2] for info in bm_info]
bm_df['Estado_Original'] = [info[3] for info in bm_info]

# Agregar tipo de bien
em_df['Tipo'] = 'Enser Menor'
bm_df['Tipo'] = 'Bien Mueble'

# Unificar dataframes
print("Unificando dataframes...")
# Asegurar que ambos dataframes tengan las mismas columnas
columnas_comunes = ['NoAct', 'Descripcion', 'NoSerie', 'Marca', 'Modelo', 
                    'Comentarios', 'Edificio', 'Planta', 'Area', 
                    'Estado_Original', 'Tipo']

em_df_unificado = em_df[columnas_comunes]
bm_df_unificado = bm_df[columnas_comunes]

# Concatenar dataframes
df_unificado = pd.concat([em_df_unificado, bm_df_unificado], ignore_index=True)

# Agregar columnas para el diagnóstico
df_unificado['Verificado'] = 'NO'
df_unificado['Estado_Actual'] = ''
df_unificado['Ubicacion_Actual'] = ''
df_unificado['Requiere_Accion'] = ''
df_unificado['Tipo_Accion'] = ''
df_unificado['Responsable_Uso'] = ''
df_unificado['Fecha_Verificacion'] = ''
df_unificado['Foto_ID'] = ''
df_unificado['Observaciones'] = ''

# Reordenar columnas para mejor presentación
columnas_orden = [
    'Verificado', 
    'NoAct', 
    'Tipo', 
    'Descripcion', 
    'Marca', 
    'Modelo', 
    'NoSerie',
    'Edificio', 
    'Planta', 
    'Area', 
    'Estado_Original',
    'Estado_Actual', 
    'Ubicacion_Actual',
    'Requiere_Accion', 
    'Tipo_Accion', 
    'Responsable_Uso', 
    'Fecha_Verificacion',
    'Foto_ID', 
    'Observaciones', 
    'Comentarios'
]

df_final = df_unificado[columnas_orden]

# Crear el archivo Excel
print(f"Creando archivo Excel en: {output_path}")
writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
df_final.to_excel(writer, sheet_name='Inventario', index=False)

# Aplicar formato al archivo Excel
workbook = writer.book
worksheet = writer.sheets['Inventario']

# Definir formatos
header_format = workbook.add_format({
    'bold': True,
    'bg_color': '#D7E4BC',
    'border': 1,
    'text_wrap': True,
    'align': 'center',
    'valign': 'vcenter'
})

verificado_format = workbook.add_format({
    'bg_color': '#FFEB9C',
    'border': 1
})

estado_format = workbook.add_format({
    'bg_color': '#C4D79B',
    'border': 1
})

accion_format = workbook.add_format({
    'bg_color': '#FFC7CE',
    'border': 1
})

border_format = workbook.add_format({
    'border': 1
})

# Aplicar formatos al encabezado
for col_num, value in enumerate(df_final.columns.values):
    worksheet.write(0, col_num, value, header_format)

# Configurar ancho de columnas
anchos_columnas = {
    'A': 10,  # Verificado
    'B': 15,  # NoAct
    'C': 12,  # Tipo
    'D': 40,  # Descripcion
    'E': 15,  # Marca
    'F': 20,  # Modelo
    'G': 20,  # NoSerie
    'H': 15,  # Edificio
    'I': 10,  # Planta
    'J': 20,  # Area
    'K': 15,  # Estado_Original
    'L': 15,  # Estado_Actual
    'M': 20,  # Ubicacion_Actual
    'N': 15,  # Requiere_Accion
    'O': 15,  # Tipo_Accion
    'P': 20,  # Responsable_Uso
    'Q': 15,  # Fecha_Verificacion
    'R': 10,  # Foto_ID
    'S': 30,  # Observaciones
    'T': 40,  # Comentarios
}

for col_letter, ancho in anchos_columnas.items():
    col_num = ord(col_letter) - ord('A')
    worksheet.set_column(col_num, col_num, ancho)

# Aplicar formatos condicionales a ciertas columnas
for row in range(1, len(df_final) + 1):
    worksheet.write(row, 0, df_final.iloc[row-1]['Verificado'], verificado_format)  # Verificado
    worksheet.write(row, 10, df_final.iloc[row-1]['Estado_Original'], estado_format)  # Estado_Original
    worksheet.write(row, 11, df_final.iloc[row-1]['Estado_Actual'], estado_format)  # Estado_Actual
    worksheet.write(row, 13, df_final.iloc[row-1]['Requiere_Accion'], accion_format)  # Requiere_Accion
    worksheet.write(row, 14, df_final.iloc[row-1]['Tipo_Accion'], accion_format)  # Tipo_Accion

# Añadir validación de datos
# Columna Verificado
worksheet.data_validation('A2:A1000', {
    'validate': 'list',
    'source': ['SI', 'NO', 'PARCIAL']
})

# Columna Estado_Actual
worksheet.data_validation('L2:L1000', {
    'validate': 'list',
    'source': ['BUENO', 'REGULAR', 'MALO', 'INSERVIBLE', 'NO LOCALIZADO']
})

# Columna Requiere_Accion
worksheet.data_validation('N2:N1000', {
    'validate': 'list',
    'source': ['SI', 'NO']
})

# Columna Tipo_Accion
worksheet.data_validation('O2:O1000', {
    'validate': 'list',
    'source': ['MANTENIMIENTO', 'REPARACIÓN', 'BAJA', 'TRANSFERENCIA', 'REUBICACIÓN', 'OTRO']
})

# Congelar paneles para facilitar navegación
worksheet.freeze_panes(1, 3)  # Fijar primera fila y primeras 3 columnas

# Crear una segunda hoja para resumen de inventario
worksheet_resumen = workbook.add_worksheet('Resumen')

# Encabezados para la hoja de resumen
encabezados_resumen = [
    'Categoría', 'Cantidad', 'Porcentaje'
]

# Aplicar formato a encabezados de resumen
for col_num, value in enumerate(encabezados_resumen):
    worksheet_resumen.write(0, col_num, value, header_format)

# Configurar anchos de columnas en hoja de resumen
worksheet_resumen.set_column(0, 0, 25)  # Categoría
worksheet_resumen.set_column(1, 1, 15)  # Cantidad
worksheet_resumen.set_column(2, 2, 15)  # Porcentaje

# Añadir secciones en el resumen
secciones = [
    "DISTRIBUCIÓN POR TIPO DE BIEN",
    "DISTRIBUCIÓN POR EDIFICIO",
    "DISTRIBUCIÓN POR ESTADO",
    "DISTRIBUCIÓN POR UBICACIÓN"
]

row_actual = 2
for seccion in secciones:
    seccion_format = workbook.add_format({
        'bold': True,
        'bg_color': '#9BC2E6',
        'border': 1,
        'align': 'center'
    })
    worksheet_resumen.merge_range(f'A{row_actual}:C{row_actual}', seccion, seccion_format)
    row_actual += 2  # Espacio para los datos
    row_actual += 2  # Espacio entre secciones

# Guardar el archivo
writer.close()

print(f"Archivo Excel creado exitosamente en: {output_path}")
print("Este archivo contiene dos hojas:")
print("1. 'Inventario': Lista completa de bienes para diagnóstico")
print("2. 'Resumen': Plantilla para estadísticas y visualización de inventario")
print("\nSugerencias para completar la hoja de Resumen:")
print("- Use fórmulas COUNTIF para contar bienes por categoría")
print("- Calcule porcentajes dividiendo cantidades entre el total de bienes")
print("- Considere añadir gráficos para visualizar la distribución")

# Imprimir estadísticas generales del inventario
total_bienes = len(df_final)
total_enseres = len(df_final[df_final['Tipo'] == 'Enser Menor'])
total_muebles = len(df_final[df_final['Tipo'] == 'Bien Mueble'])

print(f"\nEstadísticas generales del inventario:")
print(f"Total de bienes: {total_bienes}")
print(f"Total de enseres menores: {total_enseres}")
print(f"Total de bienes muebles: {total_muebles}")

# Distribucion por edificio
print("\nDistribución por edificio:")
por_edificio = df_final['Edificio'].value_counts()
for edificio, cantidad in por_edificio.items():
    print(f"- {edificio}: {cantidad} bienes")

# Los 5 tipos de bienes más comunes
print("\nTipos de bienes más comunes:")
por_descripcion = df_final['Descripcion'].value_counts().head(5)
for descripcion, cantidad in por_descripcion.items():
    print(f"- {descripcion}: {cantidad} unidades")