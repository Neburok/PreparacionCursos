---
layout: page
title: Cursos
<<<<<<< HEAD
permalink: /cursos/
nav_order: 2
has_children: false
---

# Cursos Disponibles
{: .no_toc }

Esta página contiene información sobre los cursos que imparto en la Universidad Tecnológica de Querétaro.

## Tabla de contenidos
{: .no_toc .text-delta }

1. TOC
{:toc}

## Carreras de Ingeniería

{% assign sorted_cursos = site.cursos | sort: 'title' %}
<div class="cursos-list">
  {% for curso in sorted_cursos %}
  <div class="curso-item">
    <h3><a href="{{ curso.url | relative_url }}">{{ curso.title }}</a></h3>
    <p>{{ curso.description }}</p>
    <p><strong>Código:</strong> {{ curso.codigo }} | <strong>Periodo:</strong> {{ curso.periodo }}</p>
    <p><strong>Créditos:</strong> {{ curso.creditos }} | <strong>Horas:</strong> {{ curso.horas }}</p>
    <a href="{{ curso.url | relative_url }}" class="btn">Ver detalles del curso</a>
  </div>
  {% endfor %}
</div>

## Calendario Académico

Los cursos siguen el calendario académico oficial de la Universidad Tecnológica de Querétaro. Los horarios específicos de cada curso se encuentran en la página del curso correspondiente.

## Metodología General

Los cursos utilizan un enfoque de enseñanza-aprendizaje que combina:

- Clases presenciales con apoyo de tecnología
- Prácticas y laboratorios
- Uso de herramientas computacionales y de inteligencia artificial
- Evaluación continua por competencias

## Recursos Compartidos

Algunos recursos son comunes a varios cursos y se encuentran disponibles en la sección de [Materiales](/materiales). 
=======
nav_order: 2
has_children: true
permalink: /cursos/
---


{: .no_toc }

Cursos disponibles en el repositorio de materiales didácticos.
{: .fs-6 .fw-300 }

## Ingeniería de Materiales

Asignatura fundamental que proporciona las competencias necesarias para seleccionar y utilizar materiales de acuerdo con especificaciones de diseño, considerando aspectos técnicos, económicos y ambientales.

[Ver detalles](/cursos/ingenieria-materiales){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Syllabus](/IngenieriaMateriales/syllabus){: .btn .fs-5 .mb-4 .mb-md-0 }

### Contenido Principal

- Propiedades físicas, químicas y tecnológicas de materiales
- Métodos de selección y evaluación de materiales
- Análisis de casos industriales
- Proyecto integrador de selección de materiales

---

## Física Moderna

Curso que introduce los fundamentos de la mecánica cuántica y sus aplicaciones, enfatizando la comprensión de fenómenos a nivel atómico y el uso de herramientas computacionales.

[Ver detalles](/_cursos/FisicaModerna/fisica-moderna.md){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Syllabus](/FisicaModerna/syllabus){: .btn .fs-5 .mb-4 .mb-md-0 }

### Contenido Principal

- Fundamentos de teoría cuántica
- Dualidad onda-partícula
- Ecuación de Schrödinger
- Simulaciones interactivas de fenómenos cuánticos
>>>>>>> ac32365c89f8a3a1911f608dc2d04e5784f7ac05
