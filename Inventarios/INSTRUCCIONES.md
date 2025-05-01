# Plan para Control de Inventario con Códigos QR
## Universidad Tecnológica de Querétaro - División Industrial

---

## 1. Diagnóstico inicial con códigos QR

- **Generación de formatos**
  - Ejecutar `generar_formato.py` para crear Excel de diagnóstico
  - Ejecutar `generar_qr.py` para crear códigos QR para cada bien
  - Imprimir el Excel y etiquetas QR para el recorrido físico

- **Verificación física**
  - Localizar cada bien según los registros oficiales
  - Documentar su estado actual con fotografías
  - Colocar etiquetas QR en lugar visible pero protegido
  - Registrar ubicación exacta de la etiqueta QR
  - Actualizar el Excel con todos los datos recopilados

- **Procesamiento de resultados**
  - Identificar bienes no localizados para investigación
  - Detectar bienes que requieren mantenimiento o baja
  - Completar el resumen estadístico en el Excel

---

## 2. Sistema de información digital

- **Base de datos centralizada**
  - Importar datos del Excel de diagnóstico
  - Vincular cada registro con su código QR único
  - Establecer relaciones entre bienes, ubicaciones y responsables

- **Aplicación de gestión**
  - Implementar sistema para escanear códigos QR
  - Permitir actualización en tiempo real del estado y ubicación
  - Automatizar generación de reportes y alertas

- **Respaldo y seguridad**
  - Configurar respaldos automáticos
  - Establecer niveles de acceso para diferentes usuarios
  - Implementar registro de movimientos y cambios

---

## 3. Control y seguimiento continuo

- **Inventarios periódicos**
  - Establecer calendario de verificaciones físicas (trimestrales/semestrales)
  - Utilizar la aplicación con códigos QR para agilizar el proceso
  - Comparar resultados con inventarios anteriores

- **Gestión de cambios**
  - Procedimiento para solicitar movimientos de bienes
  - Registro de transferencias entre ubicaciones o responsables
  - Actualización automática en la base de datos

- **Mantenimiento preventivo**
  - Programar revisiones según tipo de bien
  - Registrar historial de mantenimientos realizados
  - Generar alertas para próximos mantenimientos

---

## 4. Procedimientos administrativos

- **Solicitud de bajas**
  - Formato electrónico vinculado al sistema QR
  - Documentación fotográfica del estado actual
  - Seguimiento del proceso con la Subdirección de Inventarios

- **Adquisiciones**
  - Proceso para integrar nuevos bienes al sistema
  - Generación automática de códigos QR para nuevas adquisiciones
  - Actualización del inventario general

- **Reportes periódicos**
  - Dashboard con estado general del inventario
  - Informes para dirección y administración
  - Estadísticas de uso, movimientos y estado

---

## 5. Infraestructura necesaria

- **Dispositivos**
  - Smartphones o tablets para escaneo de códigos QR
  - Impresora de etiquetas para códigos QR (preferiblemente resistentes)
  - Servidor o nube para alojamiento de la base de datos

- **Software**
  - Aplicación móvil para escaneo y gestión
  - Sistema web para administración centralizada
  - Interfaz con sistemas institucionales existentes

- **Materiales**
  - Etiquetas adhesivas resistentes para códigos QR
  - Protectores para etiquetas (en casos de exposición a condiciones adversas)
  - Archivadores para documentación física de respaldo

---

## Cronograma de implementación

1. **Fase Inmediata (1-2 semanas)**
   - Generación de formatos Excel
   - Creación de códigos QR para todo el inventario
   - Impresión de materiales para diagnóstico

2. **Fase 1: Diagnóstico (3-4 semanas)**
   - Verificación física de todos los bienes
   - Colocación de etiquetas QR
   - Documentación fotográfica completa

3. **Fase 2: Digitalización (4-6 semanas)**
   - Desarrollo/implementación de sistema de gestión
   - Migración de datos del Excel a la base de datos
   - Pruebas de funcionamiento

4. **Fase 3: Capacitación (2 semanas)**
   - Formación al personal en uso del sistema
   - Documentación de procedimientos
   - Ajustes según retroalimentación

5. **Fase 4: Operación completa (permanente)**
   - Uso rutinario del sistema
   - Mejora continua
   - Evaluación periódica de resultados

---

## Instrucciones para ejecutar los scripts

```bash
# Paso 1: Generar el Excel para diagnóstico
python generar_formato.py

# Paso 2: Generar códigos QR para cada bien
python generar_qr.py

# Paso 3: Revisar los archivos generados
# - Formato_Diagnostico_Inventario.xlsx
# - Carpeta codigos_qr/ con todas las etiquetas
```

---

**Documento preparado para:**  
**Prof. Rubén Velázquez Hernández**  
**Dirección de la División Industrial**  
**Universidad Tecnológica de Querétaro**
