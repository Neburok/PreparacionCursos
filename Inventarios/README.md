# Control de Inventario de Bienes y Enseres Menores

Este proyecto permite gestionar el inventario de bienes muebles y enseres menores a través de una hoja de cálculo estructurada con validaciones de datos.

## Características

- Extracción automática de datos desde archivos PDF de resguardo
- Generación de archivo CSV con todos los datos extraídos
- Creación de archivo Excel con:
  - Estructura de columnas estandarizada
  - Validación de datos en campos clave
  - Formato adecuado para fechas y campos numéricos

## Estructura de Columnas

| Columna | Tipo | Descripción | Validación |
|---------|------|-------------|------------|
| ID_Inventario | Texto | Identificador único (No.Act. o EM) | Campo obligatorio y único |
| Tipo_Bien | Texto | Tipo de bien | Lista desplegable: 'Bien Mueble', 'Enser Menor' |
| Descripcion | Texto | Descripción detallada | - |
| Marca | Texto | Marca del bien | - |
| Modelo | Texto | Modelo del bien | - |
| No_Serie | Texto | Número de serie | - |
| Edificio | Texto | Edificio donde se ubica | Lista desplegable: NANO, PIDET, CIC1, etc. |
| Planta | Texto | Nivel donde se ubica | Lista desplegable: BAJA, ALTA, PRIMERA, etc. |
| Area_Especifica | Texto | Ubicación detallada | - |
| Estado_Actual | Texto | Estado del bien | Lista desplegable: Bueno, Regular, Malo, etc. |
| Fecha_Ultima_Revision | Fecha | Fecha de última verificación física | Formato de fecha |
| Observaciones | Texto | Notas adicionales | - |
| Fecha_Resguardo_Original | Fecha | Fecha de asignación original | Formato de fecha, Opcional |

## Requisitos

- Python 3.6+
- Bibliotecas requeridas:
  - pandas
  - PyPDF2
  - openpyxl

## Instalación

```bash
pip install pandas PyPDF2 openpyxl
```

## Uso

1. Coloca los archivos PDF de resguardo en el mismo directorio que el script
2. Ejecuta el script:

```bash
python inventario.py
```

3. Se generarán dos archivos:
   - `Control_Inventario.csv`: Datos en formato CSV
   - `Control_Inventario.xlsx`: Archivo Excel con validaciones

## Mantenimiento

- Puedes editar directamente el archivo Excel generado
- Para agregar nuevos bienes, simplemente añade nuevas filas siguiendo el formato
- Las validaciones están configuradas para funcionar con filas adicionales

## Notas

- Si necesitas actualizar los datos, vuelve a ejecutar el script para regenerar los archivos
- El campo `Fecha_Ultima_Revision` se completa automáticamente con la fecha actual al ejecutar el script
- Los campos `Observaciones` y `Fecha_Resguardo_Original` se dejan en blanco para llenado manual
