---
layout: page
title: Componentes UI
nav_order: 3
has_children: true
permalink: /docs/ui-components/
---

# Componentes UI
{: .no_toc }

Aquí encontrarás información sobre los componentes de interfaz de usuario disponibles en este tema y cómo utilizarlos.

## Tabla de contenidos
{: .no_toc .text-delta }

1. TOC
{:toc}

## Botones

Los botones son elementos interactivos que pueden usarse para dirigir a los usuarios a otras páginas o para acciones específicas.

```markdown
[Link de texto normal](#url){: .btn }
[Link primario](#url){: .btn .btn-primary }
[Link con Outline](#url){: .btn .btn-outline }
```

## Tarjetas

Las tarjetas son contenedores con estilo que pueden usarse para destacar contenido específico:

```html
<div class="curso-item">
  <h3><a href="{{ url }}">Título del curso</a></h3>
  <p>Descripción del curso.</p>
  <p><strong>Código:</strong> XXX | <strong>Periodo:</strong> YYY</p>
</div>
```

## Etiquetas y Badges

Puedes usar etiquetas para destacar texto específico o estado:

```markdown
Texto normal
{: .label }

Advertencia
{: .label .label-yellow }

Nota importante
{: .label .label-blue }
```

## Tablas

Las tablas pueden utilizarse para presentar datos de manera organizada:

```markdown
| Encabezado1 | Encabezado2 | Encabezado3 |
|:------------|:------------|:------------|
| Fila1, Col1 | Fila1, Col2 | Fila1, Col3 |
| Fila2, Col1 | Fila2, Col2 | Fila2, Col3 |
``` 