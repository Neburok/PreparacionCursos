---
layout: page
title: Estructura de Navegación
parent: Navegación
nav_order: 1
permalink: /docs/navigation/estructura/
---

# Estructura de Navegación
{: .no_toc }

Just the Docs utiliza una estructura jerárquica para organizar la navegación en el sitio.

## Tabla de contenidos
{: .no_toc .text-delta }

1. TOC
{:toc}

## Organización de archivos

Los archivos Markdown se organizan jerárquicamente:

```
docs/
├── index.md               # Página de inicio
├── configuracion.md       # Página padre
├── configuracion/         # Carpeta con páginas hijas
│   ├── basica.md
│   └── avanzada.md
└── ui-components.md       # Otra página padre
    └── ui-components/     # Carpeta con páginas hijas
        ├── botones.md
        └── etiquetas.md
```

## Metadata de navegación

La navegación se controla a través del frontmatter en cada archivo Markdown:

```yaml
---
layout: page
title: Mi Página        # Nombre que aparece en la navegación
nav_order: 2            # Orden en la navegación (menor primero)
has_children: true      # Indica que tiene subpáginas
parent: Título Padre    # Indica la página padre (para subpáginas)
permalink: /mi-ruta/    # URL personalizada
---
```

## Niveles de navegación

Just the Docs permite varios niveles de navegación:

- Nivel principal: sin `parent`
- Segundo nivel: `parent: Título Padre`
- Tercer nivel: `parent: Título Padre` y `grand_parent: Título Abuelo` 