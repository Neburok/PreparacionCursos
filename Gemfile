source "https://rubygems.org"

# Usar GitHub Pages
gem "github-pages", group: :jekyll_plugins

# Tema Just The Docs
gem "just-the-docs"

# Plugins de Jekyll
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
  gem "jekyll-seo-tag", "~> 2.1"
  gem "jekyll-sitemap"
end

# Windows y JRuby no incluyen zoneinfo files
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Rendimiento - activa la auto-recarga integrada
gem "webrick", "~> 1.8"

