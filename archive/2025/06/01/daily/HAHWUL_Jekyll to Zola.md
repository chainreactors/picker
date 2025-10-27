---
title: Jekyll to Zola
url: https://www.hahwul.com/blog/2025/jekyll-to-zola/
source: HAHWUL
date: 2025-06-01
fetch_date: 2025-10-06T22:52:30.404804
---

# Jekyll to Zola

[ ]

[![HAHWUL Logo](/images/logo.png)](/)

[ ]

- [WHO](/about/)
- [BLOG](/blog/)
- [SEC](/sec/)
- [DEV](/dev/)
- [PROJECTS](/projects/)

* ENGLISH
* [한국어](https://www.hahwul.com/ko/blog/2025/jekyll-to-zola/)

`⌘``K`

[ENGLISH](https://www.hahwul.com/blog/2025/jekyll-to-zola/)

[한국어](https://www.hahwul.com/ko/blog/2025/jekyll-to-zola/)

MAY 31, 2025

# Jekyll to Zola

My journey migrating from Jekyll to Zola, a Rust-based SSG.

It's been nearly three years since I switched back from [Hugo to Jekyll](/blog/2022/hugo-to-jekyll/) in August 2022 (see that post here), and now I'm making another move – this time to a tool called Zola. I wanted to share this journey in a post. While Zola isn't as mainstream or as large a project as Hugo or Jekyll, it has its own unique charm. I'll briefly introduce Zola and explain why I decided to make the switch.

## What is Zola?

[Zola](https://github.com/getzola/zola) is a Static Site Generator (SSG) built with Rust. It uses its own template engine, Tera, and much like Hugo, it's distributed as a single binary. This means it's incredibly fast and doesn't require installing a bunch of separate dependencies. Furthermore, it comes with many convenient built-in features like Sass/SCSS compilation, syntax highlighting, table of contents generation, shortcodes, and internationalization (i18n) support, all without needing extra plugins, which makes for excellent usability.

## Why Zola?

Over the past few years, my development toolkit has increasingly filled up with Rust-based tools like [Caido](https://caido.io/), [Helix](https://helix-editor.com/), [Zed](https://zed.dev/). Starting this year, Rust has also become my primary programming language, and I've been diving deep into it. Naturally, this trend led me to explore other tools within the Rust ecosystem, and Zola was one of the appealing projects I discovered this way.

> This tool and its template engine tera were born from an intense dislike of the (insane) Golang template engine and therefore of Hugo that I was using before for 6+ sites.
> Vincent Prouillet

One of the main reasons I switched back from Hugo to Jekyll in the past was the complexity and, frankly, the awkwardness of Go's template engine. It seems Vincent Prouillet, Zola's developer, felt similarly. This shared sentiment about development philosophy played a significant role in my decision to choose Zola.

Of course, its technical appeal was a big factor too. After considering various factors, I decided to migrate to Zola, and I'm currently very satisfied with it. Especially compared to Jekyll, where build times could be a bit disappointing and its characteristic live reloading was often slow, Zola's live reloading is incredibly fast, which has significantly improved my writing experience. Additionally, the ability to handle internationalization (i18n) easily without complex configurations was another major factor in choosing Zola.

## Design

Migrating to Zola, I kept the core design philosophy of my existing Jekyll theme but rewrote the code to make it cleaner and more polished overall. Zola's template engine, Tera, is conceptually similar to Jekyll's Liquid but also resembles Jinja2 or Django templates, offering a more intuitive syntax. This made migrating and improving the existing logic relatively straightforward. A key difference I noticed is that with Jekyll, frequent page referencing can significantly impact build times. Zola doesn't seem to suffer from this to the same extent, which allowed me to enhance template reusability with macros without a noticeable performance penalty. Thanks to this, I managed to shorten the migration period considerably, more so than I initially anticipated.

Visually, I stuck with the existing black-based (`#000000`) theme but made the white accent points a bit more eye-catching. Good examples are the interactive elements on the main page and the 404 page.

![HAHWUL Main](https://github.com/user-attachments/assets/632a5603-34bf-41c1-9cb3-19fceca82002)
*<https://www.instagram.com/p/DJUO-64xTSC/>*

This sort of feel and the way it's expressed is something I came up with after getting inspired by a scene from the drama Loki season 2.

![Loki season 2's ending](https://github.com/user-attachments/assets/5ce4abb4-e870-4797-a287-9ec297c113b0)
*Loki season 2's ending scene*

## Conclusion

Changing the underlying tool of a blog can sometimes be arduous and lead to unexpected challenges, but it has always given me the opportunity to learn new technologies and create better outcomes. This migration to Zola was no different.

Of course, who knows, a few years down the line, another whim might lead me to seek out a new tool. But for now, I'm extremely satisfied with Zola's simplicity, speed, and the sense of stability and development philosophy that comes from it being Rust-based. Looking ahead, I plan to continue cultivating my blog while also contributing, even in small ways, to the Zola project, hoping to help this wonderful tool continue to evolve.

[#zola](https://www.hahwul.com/tags/zola/)
[#ssg](https://www.hahwul.com/tags/ssg/)
[#rust](https://www.hahwul.com/tags/rust/)

[ ]

[ ]

### Table of Contents

[What is Zola?](https://www.hahwul.com/blog/2025/jekyll-to-zola/#what-is-zola)

[Why Zola?](https://www.hahwul.com/blog/2025/jekyll-to-zola/#why-zola)

[Design](https://www.hahwul.com/blog/2025/jekyll-to-zola/#design)

[Conclusion](https://www.hahwul.com/blog/2025/jekyll-to-zola/#conclusion)

[Previous

Jwt-Hack: Reborn in Rust](https://www.hahwul.com/blog/2025/jwt-hack-v2/)

[Next

Hello Urx 👋🏼](https://www.hahwul.com/blog/2025/hello-urx/)

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
  + [ENGLISH](https://www.hahwul.com/blog/2025/jekyll-to-zola/)
  + [한국어](https://www.hahwul.com/ko/blog/2025/jekyll-to-zola/)