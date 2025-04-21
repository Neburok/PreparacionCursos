---
layout: page
title: Búsqueda
nav_order: 8
permalink: /docs/search/
---

# Búsqueda
{: .no_toc }

Just the Docs incluye funcionalidad de búsqueda incorporada que puedes configurar según tus necesidades.

## Tabla de contenidos
{: .no_toc .text-delta }

1. TOC
{:toc}

## Habilitar la búsqueda

La búsqueda está habilitada por defecto en Just the Docs. Puedes controlarla en `_config.yml`:

```yaml
search_enabled: true
```

## Configuración de búsqueda

Just the Docs ofrece varias opciones para personalizar el comportamiento de la búsqueda:

```yaml
# Excluir páginas de los resultados de búsqueda
search_exclude:
  - /docs/excluida.html
  
# Configurar el texto del botón de búsqueda
search:
  button_text: "Buscar"
  placeholder_text: "Buscar en el sitio"
  heading_level: 2
```

## Búsqueda en la página

La caja de búsqueda aparece en la parte superior de la página y buscará a través de todo el contenido del sitio.

## Resultados de búsqueda

Los resultados de búsqueda aparecen en tiempo real debajo de la caja de búsqueda, mostrando títulos y fragmentos de contenido relevante. 