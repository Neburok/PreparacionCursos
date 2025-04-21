# Sitio Web de Cursos en Jekyll

Este repositorio contiene un sitio web desarrollado con Jekyll para organizar y presentar materiales de cursos de ingeniería.

## Requisitos previos

Para ejecutar este sitio localmente, necesitarás tener instalados:

1. Ruby (versión 2.5.0 o superior)
2. RubyGems
3. GCC y Make (para sistemas que necesiten compilar extensiones nativas)

## Instalación

1. Clona este repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   cd PreparacionCursos
   ```

2. Instala Jekyll y las dependencias:
   ```
   gem install bundler
   bundle install
   ```

## Ejecutar el sitio localmente

Para iniciar el servidor de desarrollo:

```
bundle exec jekyll serve
```

Ahora puedes acceder al sitio en tu navegador en `http://localhost:4000`.

Para habilitar la recarga automática cuando haces cambios:

```
bundle exec jekyll serve --livereload
```

## Estructura del sitio

- `_config.yml`: Configuración principal de Jekyll
- `_layouts/`: Plantillas para diferentes tipos de páginas
- `_includes/`: Componentes HTML reutilizables
- `_sass/`: Archivos SCSS para estilos
- `assets/`: Archivos estáticos (CSS, imágenes, etc.)
- `_cursos/`: Colección de páginas para cada curso
- `_materiales/`: Colección de materiales didácticos

## Añadir un nuevo curso

1. Crea un nuevo archivo en la carpeta `_cursos/` con extensión `.md`
2. Añade el frontmatter con el formato:
   ```yaml
   ---
   layout: curso
   title: Título del Curso
   codigo: CÓDIGO-101
   periodo: Periodo académico
   imagen: /assets/images/nombre-imagen.jpg
   creditos: 5
   horas: 60
   description: "Descripción breve del curso."
   ---
   ```
3. Añade el contenido del curso en formato Markdown

## Publicación

Para publicar el sitio:

1. Construye el sitio:
   ```
   bundle exec jekyll build
   ```
2. Los archivos generados estarán en la carpeta `_site/`

Para publicar en GitHub Pages:

1. Configura `_config.yml` con tu información de GitHub Pages
2. Sube los cambios a la rama principal
3. Configura GitHub Pages para publicar desde la rama principal o la carpeta `docs/`

## Licencia

Este material se comparte bajo licencia [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/) 