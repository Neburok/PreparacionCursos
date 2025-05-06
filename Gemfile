source "https://rubygems.org"

# Gema principal de Jekyll
gem "jekyll", "~> 4.3.2"

# Tema Just The Docs
gem "just-the-docs"

# Si estás usando GitHub Pages, descomenta la siguiente línea
# gem "github-pages", group: :jekyll_plugins

# Plugins de Jekyll
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
  gem "jekyll-seo-tag", "~> 2.1"
  gem "jekyll-sitemap"
end

# Windows y JRuby no incluyen zoneinfo files, así que incluye las gemas de tzinfo
# y otras dependencias que tu sistema puede necesitar
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Rendimiento - activa la auto-recarga integrada
gem "webrick", "~> 1.8" 