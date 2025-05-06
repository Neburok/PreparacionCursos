---
layout: page
title: Configuración Básica
parent: Configuración
nav_order: 1
permalink: /docs/configuracion/basica/
---

# Configuración Básica
{: .no_toc }

Esta página describe la configuración básica del sitio utilizando el tema Just the Docs.

## Tabla de contenidos
{: .no_toc .text-delta }

1. TOC
{:toc}

## Archivo _config.yml

El archivo `_config.yml` es el archivo principal de configuración de Jekyll. Aquí puedes definir:

- Título del sitio
- Descripción
- URL base
- Tema (Just the Docs)
- Configuración específica del tema

## Ejemplo de configuración

```yaml
# Configuración básica
title: "Cursos de Ingeniería"
author: "Prof. Rubén Velázquez Hernández"
description: "Recursos didácticos para cursos universitarios de Ingeniería"
baseurl: ""
url: ""

# Tema
theme: just-the-docs

# Configuración específica de Just The Docs
color_scheme: light
search_enabled: true
heading_anchors: true
```

## Cambios en la configuración

Para aplicar cambios en la configuración, necesitas reconstruir el sitio:

```bash
bundle exec jekyll serve
```

Los cambios en el archivo `_config.yml` requieren reiniciar el servidor para que surtan efecto. 