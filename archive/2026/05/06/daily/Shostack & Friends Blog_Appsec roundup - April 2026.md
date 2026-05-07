---
title: Appsec roundup - April 2026
url: https://shostack.org/blog/appsec-roundup-april-2026/
source: Shostack & Friends Blog
date: 2026-05-06
fetch_date: 2026-05-07T05:34:13.786057
---

# Appsec roundup - April 2026

[Skip to main content](#main-content)

[![Shostack and Associates logo, click for Homepage](/img/Shostack-logo-white.png)](/)

* [About](/about)
  + [Shostack + Associates](/about)
  + [Adam Shostack](/about/adam)
  + [Our Partners](/partners)
* [Services](/training)
  + [Training](/training)
  + [Accelerator](/secure-design-accelerator)
  + [Expert Witness](/expert-witness)
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
2. [Blog](/blog/)
3. Appsec roundup - April 2026

Shostack + Friends Blog

# Appsec roundup - April 2026

The importance of slow time in work is a theme for April, along with how Claude optimized away its own security rules. Also fun games collected at RSA!
![a photograph of a robot, sitting in a library, working on a jigsaw puzzle. The robot holds up the jigsaw puzzle](/images/blog/img/2025/appsec-roundup-feb-25-1000w.png)

This month leads off with [Buying Back Our Slack](https://www.seeingthesystem.com/p/buying-back-our-slack) and [Which Way Is Downhill?](https://www.seeingthesystem.com/p/which-way-is-downhill), both by
Ryan Moser. The first considers the impact on AI on work, the
second how people work in large systems. (I would argue slightly
with the framing of the first: work like
building a deck or writing tests are not “cognitive rest” but a
chance to reflect on our work and “sensemake.”)

Both have a great deal to say about application security, if you
take time and think about them. But if you don’t want to do that,
articles by Stephen de Vries, the Cloudflare sandbox, and Robert
Hansen’s Thoughts on PQC are all thoughtful bits. On the other
hand, NIST doesn’t have time to stop and think about
all the vulnerabilities anymore.

### Threat Modeling

* Andrew Nesbitt has a pair of posts: [Package
  Security Problems for AI Agents](https://nesbitt.io/2026/04/08/package-security-problems-for-ai-agents.html), and [Package
  Security Defenses for AI Agents](https://nesbitt.io/2026/04/09/package-security-defenses-for-ai-agents.html), with separate advice for
  those using AI coding platforms, and those designing them. Nice!
* Stephen de Vries at ThreatModeler makes a case worth reading in [Calm in the Chaos: Why Threat Modeling Matters More as AI Speeds
  Up the Build-Exploit-Patch Cycle:](https://threatmodeler.com/blog/calm-in-the-chaos-why-threat-modeling-matters-more-as-ai-speeds-up-the-build-exploit-patch-cycle/) AI is accelerating code generation, vulnerability discovery,
  and exploit development, but speed isn't the same as progress. The build-exploit-patch cycle is faster now, not better.
  Threat modeling, grounded in architectural design before the code is written, is how you break that cycle.

### Appsec

* Kenton Varda, Sunil Pai, and Ketan Gupta write on the Cloudflare
  blog about
  [Sandboxing AI agents, 100x
  faster](https://blog.cloudflare.com/dynamic-workers/), offering Javascript in that sandbox with a virtualized
  mini filesystem. Neat!
* [Vulnerability Research Is Cooked](https://sockpuppet.org/blog/2026/03/30/vulnerability-research-is-cooked/) amplifies what I said in
  February, about a [Vulnerability Finding
  Inflection Point](https://shostack.org/blog/vuln-finding-inflection/).

### AI

* Adversa.ai writes about how [Claude Code vulnerability: Deny
  rules silently bypassed because security checks cost too many
  tokens](https://adversa.ai/claude-code-security-bypass-deny-rules-disabled/). Oops!
* See above “Vuln finding inflection point” for my February
  comments about Glasswing and Mythos.

### Regulation

* NIST has announced that they're going to [enrich a smaller subset of CVEs with NVD data](https://www.nist.gov/news-events/news/2026/04/nist-updates-nvd-operations-address-record-cve-growth).

### Quantum 🔥

* Robert J. Hansen has [Thoughts
  on PQC](https://lists.gnupg.org/pipermail/gnupg-users/2026-April/068253.html) (Post Quantum Cryptography). He is not kind to people
  who have gone beyond earning skepticism to earning scorn.

![Secure By Design Story cards, Magic cards from Cribl, and Pentest Blitz](/images/blog/img/2026/appsec-roundup-games-april-2026-400w.jpeg)

### Games Received

* Finite State’s [Pentest Blitz](https://finitestate.io/events/defcon-33).
* [Bob Lord](https://infosec.exchange/%40boblord)’s Secure By Design Storycards.
* A set of Magic: The Gathering cards which I believe are from [Cribl](https://cribl.io/),
  but they’re very minimally branded and I can’t find anything about
  them online.

---

### Shostack + Associates News

* We’re getting ready for [Threat Modeling AI Systems](https://courses.shostack.org/courses/Threat-Modeling-AI-Systems-225), delivered
  by the awesome team of Michael Novack and Shoshana Cox in
  Washington DC, May 19+20. You can read Mike’s blog post [announcing
  the course](https://shostack.org/blog/threat-modeling-ai-systems-course-announce/).
* We rebranded for April 1. You can see the [Star Trek version of our homepage](https://shostack.org/lcars-index).
* Adam will be presenting “Threat Modeling in the Age of AI” at
  [Vancouver’s VanSecSIG](https://us06web.zoom.us/meeting/register/GdEq-c4lT-6zq3DAT7tkNg) on
  May 8.
* Adam and Erik will be delivering our classic [Threat Modeling Intensive](https://owasp.glueup.com/event/162243/register/)
  at OWASP Appsec EU in Vienna, June 23-24.
* Adam and team will be delivering [Threat
  Modeling Intensive with
  Complete AI](https://blackhat.com/us-26/training/schedule/#adam-shostacks-threat-modeling-intensive-with-complete-ai-51473) at Blackhat
  August 1-4.
* The Global Encryption Coalition released [Open Letter on
  [Canada’s] Bill C-22, An act respecting
  lawful access](https://www.globalencryption.org/2026/04/open-letter-on-bill-c-22-an-act-respecting-lawful-access/). Adam was
  honored to sign.
* A research team including Ruhr University Bochum,
  Ludwig-Maximilians-Universität
  München, and the University
  of Washington is doing a
  research project on how
  security decisions are made
  in complex software projects,
  and we’re recruiting for
  participants. Please see our
  [Linkedin](https://www.linkedin.com/posts/shostack_when-software-decisions-get-complex-how-share-7454976652746334208-Y4W9/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAABXB8Bi8nzcKtYJy26uPQJtELAN8sgDB4)
  post for more details and to
  sign up.

---

Image by midjourney: ”a photograph of a robot, sitting in a library, working on a jigsaw puzzle. The robot is spotlighted by light streaming in through a small window"

Originally published by Adam on 06 May 2026

Categories:
  [application security](/blog/category/application-security)
  [software engineering](/blog/category/software-engineering)
  [security](/blog/category/security)

## Our Favorite Content

[General threat modeling posts](/blog/category/threat-modeling)

[The Security Principles of Saltzer and Schroeder, illustrated with Star Wars](/blog/the-security-principles-of-saltzer-and-schroeder)

[Other Star Wars blog posts](/blog/category/star-wars)

[Modeling attackers and their motives](/blog/modeling-attackers-and-their-motives)

[Doing science with near misses](/blog/doing-science-with-near-misses)

[Posts about Adam’s “Threats” book](/blog/category/threats-book)

[Posts about Adam’s “Threat Modeling” book](/blog/category/threat-modeling-book)

[Posts about “The New School of Information Security” book](/blog/category/the-new-school)

[About this blog](/blog/about)

## Subscribe (RSS/Mail)

RSS/ATOM: The RSS [feed is here](https://shostack.org/feed.xml). We recommend RSS as the best way to follow this blog, and think generally RSS is the best way to take control of the information you ...