---
layout: page
title: Navegación
nav_order: 6
has_children: true
permalink: /docs/navigation/
---

# Navegación
{: .no_toc }

Aquí encontrarás información sobre cómo configurar la navegación en este tema.

## Tabla de contenidos
{: .no_toc .text-delta }

1. TOC
{:toc}

## Estructura de navegación

Just the Docs organiza la navegación mediante frontmatter en archivos Markdown:

```yaml
---
layout: page
title: Mi Página
nav_order: 2
has_children: true
permalink: /mi-seccion/
---
```

## Orden de navegación

Puedes controlar el orden de los elementos de navegación usando `nav_order`:

```yaml
---
nav_order: 1  # Aparece primero
---
```

## Páginas hijas

Para crear una jerarquía de navegación, utiliza `has_children` y `parent`:

```yaml
# En la página padre
---
has_children: true
---

# En la página hija
---
parent: Título de la página padre
---
```

## Enlaces externos

Puedes añadir enlaces externos a la navegación en `_config.yml`:

```yaml
aux_links:
  "Universidad Tecnológica de Querétaro":
    - "https://www.uteq.edu.mx/"
``` 