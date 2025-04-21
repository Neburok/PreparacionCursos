---
layout: page
title: Diseño
nav_order: 5
has_children: true
permalink: /docs/layout/
---

# Diseño
{: .no_toc }

Aquí encontrarás información sobre las opciones de diseño disponibles en este tema.

## Tabla de contenidos
{: .no_toc .text-delta }

1. TOC
{:toc}

## Anchura del contenido

Puedes controlar la anchura del contenido usando las siguientes clases:

```markdown
Contenido estándar (por defecto)

Contenido de ancho completo
{: .w-100 }

Contenido estrecho
{: .w-50 }
```

## Tablas

Las tablas pueden configurarse con diferentes estilos:

```markdown
| Tabla estándar | Descripción |
|:---------------|:------------|
| Fila 1         | Datos 1     |
| Fila 2         | Datos 2     |
{: .w-75 }
```

## Imágenes

Puedes configurar el tamaño y alineación de las imágenes:

```markdown
![Imagen centrada](/ruta/a/imagen.jpg)
{: .mx-auto .d-block }

![Imagen redimensionada](/ruta/a/imagen.jpg)
{: .w-50 }
```

## Divisores

Puedes usar divisores para separar secciones de contenido:

```markdown
---

Contenido separado por un divisor.
``` 