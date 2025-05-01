# Sistema de Control de Inventario con Códigos QR

Este documento explica cómo implementar y utilizar el sistema de códigos QR para el control de inventario de la Universidad Tecnológica de Querétaro.

## Archivos del sistema

- `generar_formato.py`: Genera el archivo Excel para el diagnóstico inicial del inventario
- `generar_qr.py`: Crea códigos QR para cada bien en el inventario
- `codigos_qr/`: Carpeta donde se almacenan los códigos QR generados

## Proceso de implementación

### 1. Generación del formato de diagnóstico

```bash
python generar_formato.py
```

Este comando crea el archivo `Formato_Diagnostico_Inventario.xlsx` que contiene todos los bienes de su inventario con los campos necesarios para el diagnóstico.

### 2. Generación de códigos QR

```bash
python generar_qr.py
```

Este comando genera un código QR para cada bien en su inventario y los guarda en la carpeta `codigos_qr/`.

### 3. Impresión de códigos QR

- Imprima los códigos QR en etiquetas adhesivas resistentes
- Tamaño recomendado: 2.5 cm x 2.5 cm
- Use impresión láser para mayor durabilidad
- Considere proteger las etiquetas con cinta transparente para mayor durabilidad

## Proceso de diagnóstico inicial con códigos QR

### Preparación

1. Imprima el archivo Excel o llévelo en un dispositivo móvil
2. Prepare las etiquetas con códigos QR
3. Lleve un dispositivo para escanear los códigos QR (smartphone o tableta)
4. Lleve una cámara o smartphone para documentación fotográfica

### Durante la verificación física

1. Para cada bien:
   - Localice el bien físicamente
   - Verifique que corresponda con los datos del inventario
   - Evalúe su estado
   - Adhiera la etiqueta QR en un lugar visible pero protegido
   - Escanee el código QR para verificar que funcione correctamente
   - Tome una fotografía que muestre el bien y su etiqueta QR
   - Actualice la información en el Excel:
     * Marque como "Verificado" = "SI"
     * Actualice el estado y ubicación actual
     * En "Foto_ID", registre el nombre del archivo de la foto
     * En "Observaciones", indique la ubicación de la etiqueta QR en el bien

2. Para bienes no localizados:
   - Marque como "Estado_Actual" = "NO LOCALIZADO"
   - Guarde la etiqueta QR para cuando el bien sea encontrado

## Ventajas de utilizar códigos QR desde el inicio

1. **Eficiencia en verificaciones futuras**:
   - Escanear el código QR dará acceso inmediato a la información del bien
   - Facilita el seguimiento de movimientos y cambios de estado

2. **Documentación precisa**:
   - Cada bien queda identificado de manera única e inequívoca
   - Reduce errores de transcripción o identificación incorrecta

3. **Base para sistema de gestión avanzado**:
   - Los códigos QR son la base para un sistema digital de gestión
   - Permite implementar aplicaciones de seguimiento en tiempo real

## Para el seguimiento posterior

Con los códigos QR implementados, podrá:

1. Realizar inventarios periódicos de manera más eficiente
2. Registrar movimientos de bienes entre ubicaciones
3. Actualizar el estado de los bienes de manera sencilla
4. Mantener un historial de verificaciones y mantenimientos
5. Implementar un sistema digital completo basado en los códigos QR

## Recomendaciones para la colocación de etiquetas QR

- **Ubicación**: Coloque la etiqueta en un lugar visible pero que no interfiera con el uso del bien
- **Protección**: Evite áreas expuestas a fricción constante o condiciones ambientales extremas
- **Consistencia**: Establezca criterios uniformes para la colocación (por ejemplo, esquina superior derecha)
- **Documentación**: Fotografíe el bien mostrando claramente dónde se colocó la etiqueta

## Próximos pasos después del diagnóstico inicial

1. Desarrollar una aplicación móvil para escanear los códigos QR
2. Implementar un sistema de base de datos centralizado
3. Establecer protocolos para el mantenimiento y actualización de etiquetas
4. Capacitar al personal en el uso del sistema de códigos QR
