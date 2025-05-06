---
layout: page
title: Cursos
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