---
layout: page
title: Tablas
parent: Diseño
nav_order: 1
permalink: /docs/layout/tablas/
---

# Tablas
{: .no_toc }

Just the Docs proporciona varios estilos y opciones para trabajar con tablas.

## Tabla de contenidos
{: .no_toc .text-delta }

1. TOC
{:toc}

## Tabla básica

Una tabla básica en Markdown:

| Encabezado 1 | Encabezado 2 | Encabezado 3 |
|:-------------|:-------------|:-------------|
| Fila 1, Col 1 | Fila 1, Col 2 | Fila 1, Col 3 |
| Fila 2, Col 1 | Fila 2, Col 2 | Fila 2, Col 3 |
| Fila 3, Col 1 | Fila 3, Col 2 | Fila 3, Col 3 |

```markdown
| Encabezado 1 | Encabezado 2 | Encabezado 3 |
|:-------------|:-------------|:-------------|
| Fila 1, Col 1 | Fila 1, Col 2 | Fila 1, Col 3 |
| Fila 2, Col 1 | Fila 2, Col 2 | Fila 2, Col 3 |
| Fila 3, Col 1 | Fila 3, Col 2 | Fila 3, Col 3 |
```

## Alineación de tabla

Puedes controlar la alineación de las columnas:

| Alineado izquierda | Alineado centro | Alineado derecha |
|:-------------------|:---------------:|----------------:|
| Texto | Texto | Texto |
| Texto | Texto | Texto |

```markdown
| Alineado izquierda | Alineado centro | Alineado derecha |
|:-------------------|:---------------:|----------------:|
| Texto | Texto | Texto |
| Texto | Texto | Texto |
```

## Tamaño de tabla

Puedes controlar el ancho de la tabla con clases de utilidad:

| Nombre | Rol | Departamento |
|:-------|:----|:-------------|
| Ana García | Instructor | Ingeniería |
| Carlos López | Coordinador | Ciencias |
{: .w-75 }

```markdown
| Nombre | Rol | Departamento |
|:-------|:----|:-------------|
| Ana García | Instructor | Ingeniería |
| Carlos López | Coordinador | Ciencias |
{: .w-75 }
``` 