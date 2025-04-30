# Instrucciones para el Control de Inventario

Este proyecto incluye varias herramientas para ayudar a crear y mantener un control detallado de bienes muebles y enseres menores. A continuación se explica cada herramienta y cómo utilizarla.

## Herramientas disponibles

1. **inventario_template.py**: Genera una plantilla Excel con la estructura solicitada, validaciones y ejemplos.
2. **extraer_pdf_txt.py**: Extrae el texto de los PDFs de resguardo y lo guarda en archivos de texto para facilitar la migración manual.
3. **inventario.py**: Intenta extraer automáticamente los datos de los PDFs y crear un archivo Excel (puede no funcionar con todos los formatos de PDF).

## Recomendación de uso

Para obtener mejores resultados, recomendamos seguir este proceso:

### 1. Crear la plantilla Excel

```bash
python inventario_template.py
```

Este comando generará un archivo llamado `Plantilla_Inventario.xlsx` con:
- La estructura de columnas requerida
- Validaciones de datos para campos clave (Tipo_Bien, Edificio, Planta, Estado_Actual)
- Ejemplos de cómo completar los datos
- Una hoja de instrucciones detalladas

### 2. Extraer el texto de los PDFs

```bash
python extraer_pdf_txt.py
```

Este comando extraerá el texto de todos los PDFs en el directorio actual y los guardará en archivos de texto dentro de la carpeta `pdf_extracted_text/`. Estos archivos te permitirán:
- Ver el contenido textual de los PDFs
- Localizar y copiar los datos relevantes manualmente
- Entender la estructura de los documentos originales

### 3. Completar la plantilla Excel

1. Abre el archivo `Plantilla_Inventario.xlsx`
2. Revisa la hoja "Instrucciones" para entender el formato
3. Abre los archivos TXT extraídos de los PDFs
4. Transfiere manualmente los datos a la plantilla Excel, aprovechando las validaciones para mantener consistencia

## Características de la plantilla Excel

- **ID_Inventario**: Identificador único (No.Act. o EM)
- **Tipo_Bien**: Lista desplegable ('Bien Mueble', 'Enser Menor')
- **Descripcion**: Descripción detallada del bien
- **Marca**: Marca del bien (o "SIN MARCA")
- **Modelo**: Modelo del bien (o "SIN MODELO")
- **No_Serie**: Número de serie (o "SIN NUMERO")
- **Edificio**: Lista desplegable (NANO, PIDET, CIC1, CIC2)
- **Planta**: Lista desplegable (BAJA, ALTA, PRIMERA, etc.)
- **Area_Especifica**: Ubicación detallada
- **Estado_Actual**: Lista desplegable (Bueno, Regular, Malo, En Reparación, Dado de Baja)
- **Fecha_Ultima_Revision**: Fecha con formato adecuado
- **Observaciones**: Campo libre para notas adicionales
- **Fecha_Resguardo_Original**: Fecha opcional

## Personalización

Si necesitas personalizar las listas desplegables en Excel (por ejemplo, para añadir más opciones):

1. Selecciona la columna que quieres modificar
2. Ve a la pestaña "Datos" en Excel
3. Haz clic en "Validación de datos"
4. Modifica la lista de valores en "Origen"

## Requisitos

Para ejecutar los scripts, necesitas:

```bash
pip install pandas openpyxl pdfminer.six
```

## Actualizaciones futuras

Si en el futuro necesitas actualizar la estructura o agregar nuevos campos:

1. Modifica el script `inventario_template.py`
2. Ejecuta nuevamente el script para generar una nueva plantilla
3. Transfiere tus datos al nuevo formato

## Soporte

Si encuentras problemas o necesitas ayuda, revisa los mensajes de error que aparecen en la consola al ejecutar los scripts, ya que pueden proporcionar información útil sobre qué está fallando. 