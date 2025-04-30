import re
import pandas as pd
from io import StringIO

# Simulación del contenido extraído de los PDFs (reemplazar con la salida real de content_fetcher si es necesario)
# Nota: Se asume que la variable 'content_output' contiene la salida del tool_code anterior.
# En un entorno real, se usaría directamente la salida de content_fetcher.fetch.
# Para demostración, usamos un string multilinea simulando la salida.

content_output_simulado = """
{
type: uploaded file
fileName: RESGUARDO_BM_VELAZQUEZ HERNANDEZ_124881 (1).pdf
fullText:
--- PAGE 1 ---
... (Contenido simulado del PDF de Bienes Muebles) ...
"No.Act. ","Descripción ",,"No. serie ","Marca ","Modelo ","Comentarios "
"UTQ33 ","MESA CENTRO MESA REMPE 4005 ",,"SIN NUMERO ","SIN MARCA ","CENTRO MESA REMPE 4005 ","EDIFICIO: ""NANO"", PLANTA: BAJA, LABORATORIO 5, EDO.DEL BIEN: BUENO "
"UTQ1425 ","ESCRITORIO MADERA 4 CAJONES ",,"SIN NUMERO ","SIN MARCA ","MADERA 4 CAJONES ","EDIFICIO: ""CIC1"" 4.0, PLANTA: BAJA, ÓPTICA, EDO.DEL BIEN: BUENO "
"UTQ13775 ","PROYECTOR VIEWSONIC PJD5122 ","RYT102301002 ","VIEWSONIC ","PJD5122 ","EDIFICIO: ""O"" NANO, PLANTA: BAJA, CUBÍCULO 3, EDO.DEL BIEN: BUENO "
"UTQ17747 ","SISTEMA DE FISISORCION ","545 ","MICROMERITICS ","GEMINI VII ","EDIFICIO: ""O"" NANO, PLANTA: BAJA, LABORATORIO 5, EDO.DEL BIEN: BUENO "
... (Más datos simulados) ...
--- PAGE 5 ---
Total de bienes: 68
}
{
type: uploaded file
fileName: RESGUARDO_EM_VELAZQUEZ HERNANDEZ_124881 (1).pdf
fullText:
--- PAGE 1 ---
... (Contenido simulado del PDF de Enseres Menores) ...
"No.Act. ","Descripción ",,"No. serie ","Marca ","Modelo ","Comentarios "
"EM05673 ","GAVETA ","SIN NUMERO ","SIN MARCA ","SIN MODELO ","EDIFICIO: NANOTECNOLOGÍA PLANTA: BAJA CUBÍCULO 3 ESTADO DEL BIEN: BUENO "
"EM01030 ","SILLA ","SIN NUMERO ","SECRETARIAL ","BASE DE ESTRELLA DE 5 PUNTAS ","EDIFICIO: NANOTECNOLOGÍA PLANTA: BAJA CUBÍCULO 3 ESTADO DEL BIEN: BUENO "
"EM05860 ","Banco de taller s/n respaldo altura 24"" ","SIN NUMERO ","CATRES TUBULARES ","BANCO 05 ","EDIFICIO: PIDET PLANTA: BAJA LABORATORIO DE ÓPTICA ESTADO DEL BIEN: BUENO "
... (Más datos simulados) ...
--- PAGE 3 ---
Total de bienes: 33
}
"""

def parse_pdf_content(text_content):
    """
    Analiza el texto extraído de un PDF de resguardo y extrae los datos de los bienes.
    Intenta manejar el formato específico de los PDFs proporcionados.
    """
    records = []
    # Expresión regular mejorada para capturar las líneas de datos
    # Busca líneas que empiezan con "UTQ" o "EM" seguido de números, luego campos entre comillas.
    # Es flexible con espacios y saltos de línea dentro de los campos.
    # Captura: ID, Descripcion, NoSerie, Marca, Modelo, Comentarios
    regex = re.compile(
        r'"((?:UTQ|EM)\d+)"\s*,'        # 1: ID_Inventario (UTQxxxx o EMxxxx)
        r'\s*"(.*?)"\s*,'               # 2: Descripcion
        r'(?:\s*,"(.*?)"\s*,|\s*,,)'    # 3: No_Serie (opcional, puede estar vacío)
        r'\s*"(.*?)"\s*,'               # 4: Marca
        r'\s*"(.*?)"\s*,'               # 5: Modelo
        r'\s*"(.*?)"\s*'                # 6: Comentarios (captura hasta la última comilla)
        , re.DOTALL | re.IGNORECASE     # DOTALL para que '.' incluya saltos de línea, IGNORECASE por si acaso
    )

    # Limpia un poco el texto antes de procesar
    clean_text = re.sub(r'""', '"', text_content) # Reemplaza comillas dobles escapadas
    clean_text = re.sub(r'\s*\n\s*', ' ', clean_text) # Une líneas rotas dentro de campos

    # Itera sobre las páginas simuladas o secciones
    # (En el caso real, se iteraría sobre la estructura JSON de la respuesta)
    # Aquí simulamos buscando las líneas relevantes
    lines = clean_text.split('\n')
    current_record_text = ""
    in_record_section = False

    for line in lines:
      # Detecta el inicio de la sección de datos (aproximado)
      if '"No.Act.' in line:
          in_record_section = True
          continue
      # Detecta el fin de la sección de datos (aproximado)
      if 'Total de bienes:' in line or '--- PAGE' in line and '--- PAGE 1 ---' not in line:
          in_record_section = False
          if current_record_text:
              # Procesa el último registro acumulado si existe
              match = regex.search(current_record_text)
              if match:
                  records.append(match.groups())
              current_record_text = ""
          continue

      if in_record_section:
          # Intenta encontrar una coincidencia en la línea actual
          match = regex.search(line)
          if match:
              # Si se encontró un registro completo, añadirlo y limpiar el acumulador
              if current_record_text: # Procesa el acumulado anterior si existía
                  prev_match = regex.search(current_record_text)
                  if prev_match:
                      records.append(prev_match.groups())
              records.append(match.groups())
              current_record_text = ""
          else:
              # Si no es un registro completo, acumular la línea (podría ser parte de un campo multilínea)
              # Añadir comillas al principio y final si no las tiene para intentar que coincida el regex
              # current_record_text += ' ' + line.strip()
              # Simplificación: Asumimos que cada línea con datos relevantes empieza con "UTQ" o "EM"
              # Si no coincide, probablemente es texto residual o encabezado/pie de página.
              # Esta parte es la más heurística y propensa a errores con formatos complejos.
               pass # Ignorar líneas que no coinciden directamente por ahora

    # Intento de procesar el último acumulado si quedó algo
    if current_record_text:
        match = regex.search(current_record_text)
        if match:
            records.append(match.groups())


    # Procesamiento de los comentarios para extraer ubicación y estado
    processed_data = []
    for record in records:
        id_inv, desc, n_serie, marca, modelo, comentarios = record

        # Limpieza básica de campos
        id_inv = id_inv.strip() if id_inv else 'N/A'
        desc = desc.strip().replace('\n', ' ') if desc else 'N/A'
        n_serie = n_serie.strip() if n_serie else 'SIN NUMERO'
        marca = marca.strip() if marca else 'SIN MARCA'
        modelo = modelo.strip() if modelo else 'SIN MODELO'
        comentarios = comentarios.strip().replace('\n', ' ') if comentarios else ''

        # Extracción de datos de los comentarios usando regex
        edificio = re.search(r'EDIFICIO:\s*"?([^,""]+)"?', comentarios, re.IGNORECASE)
        planta = re.search(r'PLANTA:\s*(\w+)', comentarios, re.IGNORECASE)
        # Area específica es más variable, intentamos capturar lo que sigue a planta/edificio
        area = re.search(r'(?:LABORATORIO|CUB[ÍI]CULO|ÁREA)[:\s]*([^,]+)', comentarios, re.IGNORECASE)
        estado = re.search(r'(?:EDO\.DEL BIEN|ESTADO(?: DEL BIEN)?):\s*(\w+)', comentarios, re.IGNORECASE)

        edificio_val = edificio.group(1).strip().upper() if edificio else 'N/D'
        # Corrección para nombres de edificios comunes
        if 'NANO' in edificio_val: edificio_val = 'NANO'
        if 'PIDET' in edificio_val: edificio_val = 'PIDET'
        if 'CIC1' in edificio_val: edificio_val = 'CIC1'


        planta_val = planta.group(1).strip().upper() if planta else 'N/D'
        area_val = area.group(1).strip() if area else 'N/D'
        estado_val = estado.group(1).strip().upper() if estado else 'N/D'

        # Determinar Tipo_Bien basado en el prefijo del ID
        tipo_bien = 'Bien Mueble' if id_inv.startswith('UTQ') else 'Enser Menor' if id_inv.startswith('EM') else 'N/D'

        processed_data.append({
            'ID_Inventario': id_inv,
            'Tipo_Bien': tipo_bien,
            'Descripcion': desc,
            'Marca': marca,
            'Modelo': modelo,
            'No_Serie': n_serie,
            'Edificio': edificio_val,
            'Planta': planta_val,
            'Area_Especifica': area_val,
            'Estado_Actual': estado_val,
            'Fecha_Ultima_Revision': '', # Dejar vacío para llenarlo manualmente
            'Observaciones': comentarios, # Guardar comentarios originales por si algo no se parseó bien
             'Fecha_Resguardo_Original': '' # Dejar vacío
        })

    return processed_data

# --- Ejecución Principal ---
all_data = []

# Simular la estructura de la respuesta de content_fetcher
# En un caso real, iterarías sobre la lista de resultados de fetch()
simulated_files = [
    content_output_simulado[content_output_simulado.find("fileName: RESGUARDO_BM"):content_output_simulado.find("fileName: RESGUARDO_EM")],
    content_output_simulado[content_output_simulado.find("fileName: RESGUARDO_EM"):]
]

for file_content in simulated_files:
    # Extraer el fullText simulado
    match_text = re.search(r'fullText:(.*)', file_content, re.DOTALL)
    if match_text:
        text = match_text.group(1)
        # Eliminar marcadores de página y limpiar
        text = re.sub(r'--- PAGE \d+ ---', '', text)
        parsed = parse_pdf_content(text)
        all_data.extend(parsed)

# Crear DataFrame de Pandas
df = pd.DataFrame(all_data)

# Reordenar columnas según la propuesta
column_order = [
    'ID_Inventario', 'Tipo_Bien', 'Descripcion', 'Marca', 'Modelo',
    'No_Serie', 'Edificio', 'Planta', 'Area_Especifica', 'Estado_Actual',
    'Fecha_Ultima_Revision', 'Observaciones', 'Fecha_Resguardo_Original'
]
df = df[column_order]

# Generar el archivo CSV
csv_output = df.to_csv(index=False, quoting=1) # quoting=1 envuelve todo en comillas

# Imprimir el CSV (en un entorno real, podrías guardarlo a un archivo)
print(csv_output)

# Guardar a un archivo CSV llamado 'inventario_inicial.csv'
# df.to_csv('inventario_inicial.csv', index=False, encoding='utf-8-sig')
# print("\nArchivo 'inventario_inicial.csv' generado exitosamente.")


