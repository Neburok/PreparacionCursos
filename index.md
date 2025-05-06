---
layout: home
title: Inicio
nav_order: 1
permalink: /
---

# Portal de Cursos de Ingeniería
{: .fs-9 }

Recursos didácticos para las asignaturas de Ingeniería en la Universidad Tecnológica de Querétaro.
{: .fs-6 .fw-300 }

[Ver Cursos](#cursos){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 } [Materiales Didácticos](#materiales){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## Bienvenido

Este sitio contiene recursos didácticos para las asignaturas que imparto en la Universidad Tecnológica de Querétaro. Ha sido diseñado para facilitar el acceso a materiales de clase, guías de estudio, y recursos complementarios que apoyarán tu aprendizaje.

## Cursos disponibles
{: #cursos }

{% assign sorted_cursos = site.cursos | sort: 'title' %}
<div class="cursos-list">
  {% for curso in sorted_cursos %}
  <div class="curso-item">
    <h3><a href="{{ curso.url | relative_url }}">{{ curso.title }}</a></h3>
    <p>{{ curso.description }}</p>
    <p><strong>Código:</strong> {{ curso.codigo }} | <strong>Periodo:</strong> {{ curso.periodo }}</p>
  </div>
  {% endfor %}
</div>

## Recursos generales
{: #materiales }

Estos recursos compartidos pueden ser útiles para diversos cursos:

- [Guías y manuales](/materiales/guias)
- [Políticas institucionales](/materiales/politicas)

## Sobre este sitio

Este repositorio tiene como propósito organizar, desarrollar y compartir material didáctico para la enseñanza de diversas asignaturas de Ingeniería a nivel universitario. Está diseñado tanto para estudiantes como para otros docentes interesados en estos temas. 