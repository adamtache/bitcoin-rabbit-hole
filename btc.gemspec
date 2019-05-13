# coding: utf-8

Gem::Specification.new do |spec|
  spec.name          = "btc"
  spec.version       = "1.0.0"
  spec.authors       = ["Adam Tache"]
  spec.email         = ["adamtache@gmail.com.com"]

  spec.summary       = %q{BTC theme.}
  spec.description   = "A BTC theme."
  spec.homepage      = "https://btc.slack.com"
  spec.license       = "MIT"

  spec.metadata["plugin_type"] = "theme"

  spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r{^(assets|_layouts|_includes|_sass|LICENSE|README|sw)}i) }

  spec.add_runtime_dependency "jekyll", "~> 3.6"
  spec.add_runtime_dependency "jekyll-sitemap", "~> 0.13"
  spec.add_runtime_dependency "jekyll-mentions", "~> 1.2"
  spec.add_runtime_dependency "jekyll-paginate", "~> 1.1"
  spec.add_runtime_dependency "jekyll-seo-tag", "~> 2.3"
  spec.add_runtime_dependency "jekyll-redirect-from", "~> 0.12"
  spec.add_runtime_dependency "jekyll-default-layout", "~> 0.1"
  spec.add_runtime_dependency "jekyll-feed", "~> 0.9"
  spec.add_runtime_dependency "jemoji", "~> 0.9"
  spec.add_runtime_dependency "jekyll-postfiles", "~> 3.0.0"

  spec.add_development_dependency "bundler", "~> 2.0.1"
  spec.add_development_dependency "rake", "~> 12.0"
  spec.add_development_dependency "rubocop", "~> 0.55.0"
end
