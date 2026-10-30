---
title: Appsec roundup - September/October 2026
url: https://shostack.org/blog/appsec-roundup-oct-2026/
source: Shostack & Friends Blog
date: 2026-10-29
fetch_date: 2026-10-30T07:55:12.859747
---

# Appsec roundup - September/October 2026

[Skip to main content](#main-content)

[![Shostack and Associates logo, click for Homepage](/img/Shostack-logo-white.png)](/)

* [About](/about)
  + [Shostack + Associates](/about)
  + [Adam Shostack](/about/adam)
  + [Our Partners](/partners)
* [Services](/training)
  + [Training](/training)
  + [Accelerator](/secure-design-accelerator)
  + [Speaking Requests](/speaking)
  + [Consulting](/consulting)
* [Resources](/resources)
  + [Overview](/resources)
  + [Threat Modeling](/resources/threat-modeling)
  + [Books](/books)
  + [Games](/tm-games)
  + [Cyber Public Health](/resources/cyber-public-health)
  + [Lessons Learned](/resources/lessons)
  + [Videos](/resources/videos)
  + [Whitepapers](/resources/whitepapers)
* [Blog](/blog)
* [Contact](/contact)

1. [Shostack + Associates](/)
2. [Blog](/blog)
3. Appsec roundup - September/October 2026

Shostack + Friends Blog

# Appsec roundup - September/October 2026

Adam Shostack, Shostack + Associates

New threat model tools, a PHP bug, chain-of-thought isn’t, and ... we’re not playing games here, or are we?
![a photograph of a robot, sitting in a library, working on a jigsaw puzzle.](/images/blog/img/2024/appsec-roundup-oct-2024-1000w.png)

There’s been a lot going on at Shostack + Associates, so we’re
combining the September and October roundups. This month leads off
with two articles from an online symposium on the LawBlog
Balkanization. Each presents an important insight into AI. The
first is
[Professional AI’s Dual Trust Problem](http://balkin.blogspot.com/2026/09/professional-ais-dual-trust-problem.html), by
Claudia E. Haupt and the second is Ignacio Cofone’s [Public Institutions Can’t Outsource
Their Reasoning](https://balkin.blogspot.com/2026/08/public-institutions-cant-outsource.html), about how a mix of over-reliance and
non-explainability led to 26,000 families being accused of tax
fraud, and leading to the resignation of an entire Dutch
government.

The second is a horrific example of what I called
over-reliance in PHANTOM-B:
> everything that is supposed to make a system like this
> accountable was in place. There was an approved algorithm and a
> procurement process behind it. Civil servants reviewed every
> flagged case. Procedures, escalation paths, and appeal rights
> existed on paper. None of those gave the institution the ability
> to answer for the outcome.

Trust is a system property, hard-won and easily lost. With that,
on to the ways to preserve it!

### Threat Modeling

* In [Security Review at the Speed of Agents](https://robinhood.com/us/en/careers/blog/security-review-at-the-speed-of-agents/) Vikram Ashtaputre talks about a system for review he built at
  RobinHood. Some interesting lessons.
* In [TALA is open-source](https://d2lang.com/blog/tala-is-open-source/), Alexander Wang releases TALA
  (Terrastruct's AutoLayout Algorithm):
  > TALA is a novel autolayout algorithm designed with software
  > architecture diagrams in mind. This means it's primarily an
  > orthogonal layout engine, which more closely matches what you
  > might find on whiteboards, rather than the DAG-based ones that
  > grow in one direction.

  TALA example #2 is a secure-enclave SoC, and note that the colors are
  not explicitly boundaries, which fooled me for a second.

### Appsec

* There was a well-publicized bug in PHP and in [We can now find
  flaws faster than anyone can fix
  them](https://tolmo.com/blog/faster-than-anyone-can-fix-them/), Mihail Kirov writes
  about how an OSTIF-funded audit
  found the issue two years
  ago. (I’m an advisor to OSTIF.) There’s bitter, angry controversy over ChainGuard’s choice
  to release the patch early,
  either violating an embargo or
  responding to reports of
  exploitation. I’m not going to
  wade into that fight. What I
  will say is the fight exposes a
  lack of institutions who can
  provide authoritative
  information to inform ending an
  embargo, or even offer a call
  that will be respected.
* Dan Luu’s [No reason for software to be slow](https://danluu.com/no-slow/) starts: “...performance work that used to require... a rare set of skills can be done by anyone who can type a few sentences, which means that you can do all sorts of optimizations that used to be too expensive to be worthwhile”
* In [Dear Open Source Developers: It's OK not to
  embargo](https://opensourcesecurity.io/2026/10-embargo/), Josh Bressers writes about Curl’s decision to treat
  low and medium severity security issues the same way Curl
  treats other bugs: without secrecy. He makes great points
  about the cost of that secrecy.

### AI

* In [Reasoning Models Don't Say What they
  Think](https://www.anthropic.com/research/reasoning-models-dont-say-think), a team from Anthropic demonstrates that “chain of
  thought” is not an accurate reflection of model calculations. (It’s nearly impossible
  to describe this without falling into anthropomorphization.) This
  finding is mirrored in METR’s [Brief
  independent investigation of agents’ behavior, reasoning and
  collaboration in the OpenAI / Hugging Face hacking incident](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)
  (“Brief” at 31000 words!) about which I hope to have more to say.
* In [Agent Security is a Systems Problem](https://arxiv.org/html/2605.18991v2), a long list
  of authors make a case for the titular claim, show that there's a set
  of tools that address agents, and discuss some of the challenges of
  doing so.

### Cryptography

* In [There’s a new way to break RSA that’s faster than anything we’ve
  seen before](https://arstechnica.com/security/2026/09/theres-a-new-way-to-break-rsa-thats-faster-than-anything-weve-seen-before/), Dan Goodin reports on [new
  work](https://eprint.iacr.org/2026/2131.pdf) by Nadia Heninger\*
  and colleagues. Reduces attack complexity to 265 for RSA
  1024, and 290 for 2024 against textbook RSA, but not
  PKCS or PSS. (Goodin describes Heninger as lead author; the preprint
  puts her in the middle.)

### Games Received

Christmas came early with a box of goodies from [Cybersec Games](https://cybersecgames.com/).

![A set of games](/images/blog/img/2026/games-oct-2026-600w.jpeg)

* [Context & Cringe](https://cybersecgames.com/products/context-cringe)
* [OWASP Cornucopia Web App Companion Set - 25ᵗʰ Anniversary Edition](https://cybersecgames.com/products/owasp-cornucopia-web-app-with-companion-edition)
* [OWASP Cumulus for Cloud architectures](https://cybersecgames.com/products/owasp-cumulus-threat-modeling-the-clouds)
* [Elevation of Autonomy for Threat Modelling AI Systems](https://cybersecgames.com/products/elevation-of-autonomy)
* [Insider Threat Kill Chain](https://cybersecgames.com/products/insider-threat-kill-chain-card-game)
* [Security Architects](https://cybersecgames.com/products/security-architects-a-fast-paced-threat-modeling-game?_pos=1&_sid=319a3a84c&_ss=r)
* [Elevation of Privilege threat modeling workshop
  kit](https://cybersecgames.com/products/elevation-of-privilege-play-to-learn-kit) including EoP, three instruction sets (the method, an
  architecture and a facilitator’s guide), threat cards, a log, and
  a scorekeeping booklet.

---

### Shostack + Associates News

We have lots of [OWASP and ThreatModCon
Plans](https://shostack.org/blog/updated-plans-for-owasp-and-threatmodcon-in-san-francisco/), including a few seats remaining in our three-day
Intensive Using AI covered in an extended blog post.

Image by midjourney, repeated from Oct, 2024

Originally published by Adam on 29 Oct 2026

Categories:
  [ai](/blog/category/ai)
  [application security](/blog/category/application-security)
  [software engineering](/blog/category/software-engineering)
  [security](/blog/category/security)

## Our Favorite Content

[General threat modeling posts](/blog/category/threat-modeling)

[The Security Principles of Saltzer and Schroeder, illustrated with Star Wars](/blog/the-security-principles-of-saltzer-and-schroeder)

[Other Star Wars blog posts]...