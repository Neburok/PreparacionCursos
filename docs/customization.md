---
layout: page
title: Personalización
nav_order: 7
permalink: /docs/customization/
---

# Personalización
{: .no_toc }

Aquí encontrarás información sobre cómo personalizar el aspecto y funcionamiento del tema.

## Tabla de contenidos
{: .no_toc .text-delta }

1. TOC
{:toc}

## Esquemas de color

Just the Docs incluye varios esquemas de color predefinidos. Puedes configurarlo en `_config.yml`:

```yaml
color_scheme: light  # Opciones: light, dark, purple, blue, green, red
```

## Estilos personalizados

Puedes añadir tus propios estilos en el archivo `_sass/custom/custom.scss`:

```scss
// Tu CSS personalizado aquí
.mi-clase-personalizada {
  color: blue;
  font-weight: bold;
}
```

## JavaScript personalizado

Para añadir JavaScript personalizado, crea un archivo en `_includes/head_custom.html`:

```html
<script>
  // Tu JavaScript personalizado aquí
  console.log('¡Hola mundo!');
</script>
```

## Logo personalizado

Puedes configurar un logo personalizado en `_config.yml`:

```yaml
logo: "/assets/images/mi-logo.png"
```

Asegúrate de ajustar el tamaño y posición en `_sass/custom/custom.scss`:

```scss
.site-logo {
  max-height: 30px;
  max-width: 100%;
}
``` 