---
title: Beginner’s Guide: Creating Your First Ruby Project
url: https://www.hahwul.com/dev/ruby/noob-beginners-guide-in-ruby/
source: HAHWUL
date: 2025-09-22
fetch_date: 2025-10-02T20:30:02.988579
---

# Beginner’s Guide: Creating Your First Ruby Project

[ ]

[![HAHWUL Logo](/images/logo.png)](/)

[ ]

- [WHO](/about/)
- [BLOG](/blog/)
- [SEC](/sec/)
- [DEV](/dev/)
- [PROJECTS](/projects/)

* ENGLISH
* [한국어](https://www.hahwul.com/ko/dev/ruby/noob-beginners-guide-in-ruby/)

`⌘``K`

[ENGLISH](https://www.hahwul.com/dev/ruby/noob-beginners-guide-in-ruby/)

[한국어](https://www.hahwul.com/ko/dev/ruby/noob-beginners-guide-in-ruby/)

SEPTEMBER 21, 2025

# Beginner’s Guide: Creating Your First Ruby Project

A step-by-step tutorial to install Ruby and create, run, test, and build your first gem project.

Getting started with Ruby is quick if you follow a few simple steps. In this guide, you’ll install Ruby, scaffold a new gem project, write a tiny program, run tests, and produce a gem build.

I’ll keep it minimal and practical so you can get productive fast.

## 1) Install Ruby

* Using RVM (Ruby Version Manager, macOS/Linux):

```
curl -sSL https://get.rvm.io | bash -s stable
source ~/.rvm/scripts/rvm
```

* Install Ruby:

```
rvm install ruby --latest
rvm use ruby --default
```

* Verify:

```
ruby --version
gem --version
bundler --version
```

## 2) Create a new project

Ruby uses `bundler` for dependency management and project scaffolding.

* Gem library:

```
bundle gem my_gem
cd my_gem
```

This creates a basic structure:

```
my_gem/
├─ Gemfile
├─ lib/
│   └─ my_gem.rb
├─ my_gem.gemspec
└─ spec/
    └─ my_gem_spec.rb
```

## 3) Write your first program

Open `lib/my_gem.rb` and define a simple module:

```
module MyGem
  def self.greet(name = "Ruby")
    "Hello, #{name}!"
  end
end
```

Run it:

```
ruby -e "require_relative 'lib/my_gem.rb'; puts MyGem.greet"
```

## 4) Manage dependencies

If you add dependencies to `Gemfile`, install them:

```
bundle install
```

You generally won’t need this for the very first “hello world,” but it’s essential once you pull in libraries like HTTP clients or web frameworks.

## 5) Format your code

Install and use RuboCop:

```
gem install rubocop
```

* Lint:

```
rubocop
```

* Auto-fix:

```
rubocop -a
```

## 6) Add a simple test (RSpec)

Edit `spec/my_gem_spec.rb`:

```
require "my_gem"

RSpec.describe MyGem do
  it "greets with default name" do
    expect(MyGem.greet).to eq "Hello, Ruby!"
  end

  it "greets a custom name" do
    expect(MyGem.greet("World")).to eq "Hello, World!"
  end
end
```

Run tests:

```
bundle exec rspec
# or verbose:
bundle exec rspec -v
```

## 7) Build a gem

Build your gem:

```
gem build my_gem.gemspec
```

Test install:

```
gem install ./my_gem-0.1.0.gem
```

## 8) Check dependencies graph (nice debugging tool)

```
bundle viz
```

## 9) Optional: Lint with RuboCop

As mentioned, for more config:

```
rubocop --auto-gen-config
```

## Visual overview

Here’s a simple flow of your first project:

```
 flowchart LR
  A[Install Ruby] --> B[bundle gem my_gem]
  B --> C[Edit lib/my_gem.rb]
  C --> D[ruby run]
  D --> E[bundle exec rspec]
  E --> F[rubocop]
  F --> G[gem build]
  G --> H[gem install]
```

## What’s next?

* Explore popular gems:
  + Web frameworks: Sinatra, Rails
  + Testing: RSpec
  + HTTP client: Faraday
* Build a gem, a CLI tool, or a Rails app and publish it on RubyGems.

You’ve just created, tested, and built your first Ruby gem. Keep it small, iterate quickly, and enjoy the flexibility of Ruby.

[#ruby](https://www.hahwul.com/tags/ruby/)
[#dev](https://www.hahwul.com/tags/dev/)
[#beginner](https://www.hahwul.com/tags/beginner/)
[#tutorial](https://www.hahwul.com/tags/tutorial/)

* Scroll to Top
* Copy URL
* Comments
* Table of Contents
* [Share on X](https://twitter.com/intent/tweet?url=https%3A//www.hahwul.com/dev/ruby/noob-beginners-guide-in-ruby/&text=Beginner%E2%80%99s%20Guide%3A%20Creating%20Your%20First%20Ruby%20Project)

[ ]

[ ]

### Table of Contents

[1) Install Ruby](https://www.hahwul.com/dev/ruby/noob-beginners-guide-in-ruby/#1-install-ruby)

[2) Create a new project](https://www.hahwul.com/dev/ruby/noob-beginners-guide-in-ruby/#2-create-a-new-project)

[3) Write your first program](https://www.hahwul.com/dev/ruby/noob-beginners-guide-in-ruby/#3-write-your-first-program)

[4) Manage dependencies](https://www.hahwul.com/dev/ruby/noob-beginners-guide-in-ruby/#4-manage-dependencies)

[5) Format your code](https://www.hahwul.com/dev/ruby/noob-beginners-guide-in-ruby/#5-format-your-code)

[6) Add a simple test (RSpec)](https://www.hahwul.com/dev/ruby/noob-beginners-guide-in-ruby/#6-add-a-simple-test-rspec)

[7) Build a gem](https://www.hahwul.com/dev/ruby/noob-beginners-guide-in-ruby/#7-build-a-gem)

[8) Check dependencies graph (nice debugging tool)](https://www.hahwul.com/dev/ruby/noob-beginners-guide-in-ruby/#8-check-dependencies-graph-nice-debugging-tool)

[9) Optional: Lint with RuboCop](https://www.hahwul.com/dev/ruby/noob-beginners-guide-in-ruby/#9-optional-lint-with-rubocop)

[Visual overview](https://www.hahwul.com/dev/ruby/noob-beginners-guide-in-ruby/#visual-overview)

[What’s next?](https://www.hahwul.com/dev/ruby/noob-beginners-guide-in-ruby/#what-s-next)

[Next

Ruby Cheatsheet](https://www.hahwul.com/dev/ruby/ruby-cheatsheet/)

[Contact](/contact)
[Thanks](/thanks)
[Sitemap](/sitemap.xml)
Random
[Feeds](/feeds)

© 2025 HAHWUL
Developed and Designed by Me

* [WHO](/about/)
* [BLOG](/blog/)
* [SEC](/sec/)
* [DEV](/dev/)
* [PROJECTS](/projects/)

---

* Language
  + [ENGLISH](https://www.hahwul.com/dev/ruby/noob-beginners-guide-in-ruby/)
  + [한국어](https://www.hahwul.com/ko/dev/ruby/noob-beginners-guide-in-ruby/)