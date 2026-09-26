---
title: Why I Build Gori
url: https://www.hahwul.com/posts/2026/why-i-build-gori/
source: HAHWUL
date: 2026-09-25
fetch_date: 2026-09-26T06:51:03.661574
---

# Why I Build Gori

[Skip to content](#main-content)

[HAHWUL](https://www.hahwul.com/)

[Posts](/posts/)
[Notes](/notes/)
[Projects](/projects/)
[About](/about/)

⌘K

# Why I Build Gori

SEPTEMBER 25, 2026

EN

[KO](/ko/posts/2026/why-i-build-gori/ "Why I Build Gori")

Why I'm building it, and what comes next

![gori](images/01-hero.webp)

Since June this year, I've been building and using [Gori](https://github.com/hahwul/gori), a TUI tool (a proxy like Burp Suite). It's now approaching v0.8, and a few people have started using it, so I thought it would be good to write down why I made it and what I plan to build next.

## Why Reinvent the Wheel?

I keep something like a project bucket list in my head. Not things built purely out of need or to solve a problem, but just... honestly, just things I wanted to build. Most of them were big projects, so I never found it easy to get started.

I'm one of the beneficiaries of the AI era. The faster development speed and environment that AI brought gave me a huge boost in productivity, and I've been able to take those projects out of my head one by one.

The first was [Hwaro](https://github.com/hahwul/hwaro) (화로, "brazier"), a static site generator (SSG), and the second is Gori (고리, "ring"), a proxy tool.

Even setting personal goals aside, building a tool is a chance to learn the many technologies and choices woven into it. And building a proxy tool is definitely not an easy road.

## Three Goals of Gori

The goals I want to reach with Gori boil down to three. They come from the pain points I've had using proxy tools like Burp Suite, ZAP, and Caido, and from my own personal vision.

### 1. TUI and Muscle Memory

I really love TUIs. Compared to a CLI, a TUI has to express a lot within a limited space, which makes it quite tricky, but that very constraint tends to produce intuitive UI/UX. And when you use well-known TUI tools like Vim or Helix for a while, you build muscle memory that stays in your hands for life.
(You still know how to quit Vim even after years away from it, right?)

![Gori's command menu, one Space away](images/02-tui-space-menu.webp)

Gori aims to build that same kind of muscle memory. I'd love to see lots of people get used to it and enjoy security testing with quick, fluid moves.

### 2. Speed and Comfort

Gori is written in Crystal, and since it's a TUI, it's inherently much faster and lighter than the JVM-based Burp Suite and ZAP, or Caido, which is Rust-based but runs a TS layer on top. (It usually takes only about 20-50MB of memory.)

![Still 28MB of memory while capturing traffic in the History tab](images/03-speed-memory.webp)

Long-time Burp Suite users will know the feeling. The longer an engagement goes on, the slower it gets, until it's eating most of your PC's memory. ZAP and Caido can't escape this either, because the GUI itself consumes so much.

Speed and comfort matter a lot. That's why I made comfort one of Gori's core goals.

### 3. AI and Automation

As AI has advanced, vulnerability analysis and hacking have changed a lot too. If people used to analyze everything by hand, I think today's picture is AI agents taking the lead, or AI and humans analyzing together.

I wanted Gori to sit right in the middle. Humans can analyze quickly in the TUI with muscle memory, but I also wanted it to be a Swiss Army knife for AI, and I hoped it could be used for automation too. That's how Gori ended up with three main interfaces (TUI x MCP x CLI).

![TUI x MCP x CLI, one engine](images/04-tui-mcp-cli.webp)

I'm picturing humans, AI, and scripts all flowing through a single tool.

## Thoughts So Far

I expected it, but proxies are really hard. Because it's a security testing tool, it's hard to just use well-known libraries as they are, and there are so many parts I have to implement myself. (Gori carries its own transport stack, HTTP included. That's what lets it send malformed requests.)

So there's a lot to learn. At least I won't get bored as long as I keep working on this project. I don't know what it will have become in five or ten years, but I think it'll still be the project I love most, just like now.

## What's Next

I don't have any grand plans. My top priority is simply the three goals above, in other words, delivering an experience optimized for both humans and AI, and I plan to build in as much of what security testing needs as possible. (That's also why I haven't built a plugin system yet. On this front, I've been heavily influenced by Helix's philosophy that the defaults should be enough.)

By the time v1 comes around, I think it'll probably be... a proxy with an even simpler, cleaner TUI than it has now.

## Wrapping Up

Now that the ceiling on human capability has been broken, I think it's time to act, one by one, on the goals you've been keeping in your heart. Believe in yourself, don't stop, and keep running forward. We are burning flames.

[gori](https://www.hahwul.com/tags/gori/)
[proxy](https://www.hahwul.com/tags/proxy/)
[tui](https://www.hahwul.com/tags/tui/)
[security-testing](https://www.hahwul.com/tags/security-testing/)

[← Previous
I've joined the Kemal Core Team!](/posts/2026/i-ve-joined-the-kemal-core-team/)

* [Why Reinvent the Wheel?](#why-reinvent-the-wheel)
* [Three Goals of Gori](#three-goals-of-gori)
  + [1. TUI and Muscle Memory](#1-tui-and-muscle-memory)
  + [2. Speed and Comfort](#2-speed-and-comfort)
  + [3. AI and Automation](#3-ai-and-automation)
* [Thoughts So Far](#thoughts-so-far)
* [What's Next](#whats-next)
* [Wrapping Up](#wrapping-up)

[TAGS](/tags/)
[USES](/about/uses/)
[CONTACT](/contact/)
[SPONSOR](/sponsor/)
[FEEDS](/feeds/)
[PRIVACY](/privacy/)

Developed and Designed by Me
2026 HAHWUL.

Esc

All
Posts
Notes
Projects
Archive
Pages

All
EN
KO

Type to search posts, notes, projects and the archive.