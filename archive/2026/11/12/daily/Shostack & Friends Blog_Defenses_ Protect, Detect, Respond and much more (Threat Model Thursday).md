---
title: Defenses: Protect, Detect, Respond and much more (Threat Model Thursday)
url: https://shostack.org/blog/modeling-and-analyzing-defenses/
source: Shostack & Friends Blog
date: 2026-11-12
fetch_date: 2026-11-13T09:06:18.207181
---

# Defenses: Protect, Detect, Respond and much more (Threat Model Thursday)

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
3. Defenses: Protect, Detect, Respond and much more (Threat Model Thursday)

Shostack + Friends Blog

# Defenses: Protect, Detect, Respond and much more (Threat Model Thursday)

Adam Shostack, Shostack + Associates

How do you choose defenses when you can’t cover everything and useability is something you shouldn't trade away?
![A robot sits beside a small carry-on suitcase while contemplating what to pack from the mountain of choices beside it.](/images/blog/img/2026/defenses-tradeoffs-1000w.jpeg)

A major theme of the [new edition of Threat
Modeling](https://amzn.to/4urxcBJ) is that security is subject to
engineering tradeoffs. Those
tradeoffs happen both at a macro level
(“How much security do we need?”) and at a
micro-level (“how should we address this
threat?”).

Security purists may wish this were not the case, but engineering
always has the iron triangle of “fast,
cheap, good: pick any two.” Not engaging
with that means security gets bolted on,
poorly. This also informs the frequently
invoked “we can’t fix everything”
objection. The rest of engineering knows
that tradeoffs will be made. One of the
primary ways to manage that is “wait and
see,” which requires a way to see, and
imposes observability requirements.

Engineers know they’re always making tradeoffs, and Chapter 9 covers a set
of important technical properties for the defenses
we’re incorporating into our delivery. The
list comes after discussions of
customer-appropriateness and security
versus compliance, and includes:

* Goal: protect, detect, respond
* Goal: reduce likelihood or impact
* Simple to complex
* Reliable or probabilistic
* Strong or weak (passwords vs. auth apps)
* Chess move or checkmate
* Proven or innovative (and of course, disproven)
* Fail open or closed
* Build or buy
* One or many
* Automated or manual
* Effort to design, implement, maintain, or operate

This list evolved as I worked on the book, and I’ve noticed that
the choices associated with
LLM defenses are informative. LLM
guardrails are typically probalistic, weak,
chess moves, “innovative” in the sense of
unproven, fail-open, and high effort to
maintain and operate.

While the list wasn’t focused on LLMs, the description that emerges
of guardrails is useful, and captures much
of the discomfort that I hear people
talking about.

Being able to characterize emergent systems is useful in a list
like this, and while this edition is going
to the printer soon, all models are wrong,
and some are useful. How can we make this
list more useful?

Note that usability is not a property we
~~can~~ should trade
off. An unusable system is an invitation
for people to stop using it, go elsewhere,
or work around it. (Which is why the book
continues to have an entire chapter on
Human Factors and Usability, even as other
chapters were retired to the website.)

Image by midjourney: A watercolour painting of a friendly, simple robot kneeling beside open carryon luggage, with an overly large pile of items that won't all fit. The robot holds an iteme in one hand and rests the other hand on its chin, deciding what to pack. Use deep indigo purple, lime green, bright orange, and red-orange. Calm, thoughtful mood.

Originally published by Adam on 12 Nov 2026

Categories:
  [books](/blog/category/books)
  [security](/blog/category/security)
  [threat modeling](/blog/category/threat-modeling)
  [threat model thursday](/blog/category/threat-model-thursday)

## Our Favorite Content

[General threat modeling posts](/blog/category/threat-modeling)

[The Security Principles of Saltzer and Schroeder, illustrated with Star Wars](/blog/the-security-principles-of-saltzer-and-schroeder)

[Other Star Wars blog posts](/blog/category/star-wars)

[Modeling attackers and their motives](/blog/modeling-attackers-and-their-motives)

[Doing science with near misses](/blog/doing-science-with-near-misses)

[Posts about “Threat Modeling 2nd Edition”](/blog/category/threat-modeling-2nd-edition)

[Posts about Adam’s “Threats” book](/blog/category/threats-book)

[Posts about Adam’s “Threat Modeling” book](/blog/category/threat-modeling-book)

[Posts about “The New School of Information Security” book](/blog/category/the-new-school)

[About this blog](/blog/about)

## Subscribe (RSS/Mail)

RSS/ATOM: The RSS [feed is here](https://shostack.org/feed.xml). We recommend RSS as the best way to follow this blog, and think generally RSS is the best way to take control of the information you take in. You can [read our thinking here](https://shostack.org/blog/take-control-of-what-you-read).

Email: If you’d like a lower volume set of updates on what Adam is doing, [Adam’s New Thing](/contact) gets only a few messages a year, guaranteed. We include a subset of posts in each.

## Recent posts

[![A robot sits beside a small carry-on suitcase while contemplating what to pack from the mountain of choices beside it.](/images/blog/img/2026/defenses-tradeoffs-175w.jpeg)](/blog/modeling-and-analyzing-defenses/)

### [Defenses: Protect, Detect, Respond and much more (Threat Model Thursday)](/blog/modeling-and-analyzing-defenses/)

12 Nov 2026

How do you choose defenses when you can’t cover everything and useability is something you shouldn't trade away?

[![A banner from the Software Safety Initiative with their logo stating that Software runs the world; it should be safe.](/images/blog/img/2026/software-safety-initiative-ssi-175w.png)](/blog/Welcome-to-the-Software-Safety-Initiative/)

### [A warm welcome to the Software Safety Institute](/blog/Welcome-to-the-Software-Safety-Initiative/)

09 Nov 2026

A significant new voice for software safety has joined the field, and Adam is proud to lend his support.

[![A header image for conferences with a full audience ready for a threat modeling talk on the right and space for talk names and venues on the left.](/images/blog/img/2026/OWASP-and-TMC-slide-header-175w.png)](/blog/OWASP-and-ThreatModCon-SF-slides/)

### [SF talks: CRA changes + the state of threat modeling in 2026](/blog/OWASP-and-ThreatModCon-SF-slides/)

05 Nov 2026

Adam is speaking at both OWASP and ThreatModCon this week. Download the slides here.

[![a photograph of a robot, sitting in a library, working on a jigsaw puzzle.](/images/blog/img/2024/appsec-roundup-oct-2024-175w.png)](/blog/appsec-roundup-oct-2026/)

### [Appsec roundup - September/October 2026](/blog/appsec-roundup-oct-2026/)

29 Oct 2026

New threat model tools, a PHP bug, chain-of-thought isn’t, and ... we’re not playing games here, or are we?

## Popular Blog Topics

[Threat Model Thursday](/blog/category/threat-model-thursday),
exploring specific published threat models

[Threat Modeling](/blog/category/threat-modeling) (general topic)

[Application Security](/blog/category/application-security)

[Software Engineering](/blog/category/software-engineering)

[Cloud Security](/blog/category/cloud-security)

[Compliance](/blog/category/compliance)

[AI](/blog/category/ai) + [ChatGPT](/blog/category/chatgpt)

[Privacy](/blog/category/privacy) + [Personal Security](/blog/category/personal-security)

[Research](/blog/category/research-papers) + [Reports](/blog/category/reports-and-data)

[Book Reviews](/blog/c...