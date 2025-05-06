---
layout: home
title: Inicio
nav_order: 1
<<<<<<< HEAD
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
=======
description: "Repositorio de materiales didácticos para cursos de ingeniería de la UTEQ"
permalink: /
---

## Materiales Didácticos UTEQ
{: .fs-9 }

Repositorio de materiales didácticos para las asignaturas de Ingeniería de la Universidad Tecnológica de Querétaro.
{: .fs-6 .fw-300 }

[Ver Cursos](#cursos){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Ver Materiales](#materiales){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## Cursos

Actualmente el repositorio incluye los siguientes cursos:

- [Física Moderna](/cursos/fisica-moderna)
  - Fundamentos de la mecánica cuántica y sus aplicaciones
  - Fenómenos cuánticos y comportamiento de la materia a nivel atómico
  - Uso de simulaciones y herramientas computacionales

- [Ingeniería de Materiales](/cursos/ingenieria-materiales)
  - Propiedades y comportamiento de materiales en ingeniería
  - Selección de materiales para aplicaciones industriales
  - Análisis de casos y proyectos integrados

## Materiales

El repositorio contiene diversos recursos didácticos:

- Programas analíticos y syllabus
- Presentaciones y material teórico
- Guías de ejercicios y problemas
- Recursos multimedia y simulaciones
- Instrumentos de evaluación
- Proyectos integradores

## Uso

Este material está diseñado para:

- Docentes de las asignaturas
- Estudiantes como apoyo al aprendizaje
- Pares académicos interesados en colaborar
- Profesionales del área como referencia

## Licencia

Este material se comparte bajo licencia [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/), permitiendo su uso no comercial con atribución.
>>>>>>> ac32365c89f8a3a1911f608dc2d04e5784f7ac05
