---
title: Threats and LLMs (Threat Model Thursday)
url: https://shostack.org/blog/threats-to-llms/
source: Shostack & Friends Blog
date: 2026-10-01
fetch_date: 2026-10-02T07:49:17.367427
---

# Threats and LLMs (Threat Model Thursday)

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
3. Threats and LLMs (Threat Model Thursday)

Shostack + Friends Blog

# Threats and LLMs (Threat Model Thursday)

There are many ways to ask what can go wrong, and the useful skill is knowing which one matches what you're building.
![A robot observes a threat through one lens while other lenses available to assess the threat hover nearby.](/images/blog/img/2026/lenses-for-threats-1000w.jpeg)

Here, the [series on the second edition of
threat modeling](https://shostack.org/blog/category/threat-modeling-2nd-edition) takes a leap forward to Part III, which has
four chapters on what can go wrong.
Chapter 5, on STRIDE, is revised. Chapter 6 is largely
new, and focuses on attack lifecycle models, mainly
the Lockheed Kill Chain and ATT&CK, but also
touches on ATLAS, FiGHT, a “Threat Matrix for
Kubernetes”, SPARTA and VATT&CK. It also covers the relationship
between chains and trees, and the widely varied
language we use.

But the chapter that might be most exciting in this part is the one
that led to PHANTOM-B, because the research that went
into this chapter was pretty intense, and included
reading probably a few thousand pages of LLM, ML and
AI security, risk, threat, and governance documents
and making sense of it in a way that’s helpful to
readers.

The chapter kicks off with a simple model of “calling,” “running,”
or “training” an LLM, because those are so
influential on the threats you can do something
about, and so that flavor of the question “what are
we working on” permeates the chapter.

From there it covers a set of sets of what can go wrong with LLMs:

* PHANTOM-B
* MITRE ATLAS
* The Berryville Institute’s ARAs
* An image-specific taxonomy by Charlotte Bird
* Google’s SAIF
* NIST’s AIML (which is not their AIRMF)
* PROMISE TO MAP

Each is covered in depth. The chapter continues with a cornucopia of other ways to consider
what can go wrong:

* Google’s empirical misuse list
* Meta’s Rule of Two for AI (and why it’s misnamed)
* Several approaches to AI red teaming
* Scholarly concerns including adversarial perturbation,
  gradient climbing and model theft

The chapter’s last technical element is a set of concerns that span
outside of security: hallucination, bias or unfairness, and
reliability, and especially the crucial relationship of security
to reliability.

All of that does two things for you, the reader. First, it
organizes the many approaches you might use, letting you select
one that's appropriate to your situation. Second, each is
presented as a scope: when it makes sense to consider it. For
example, Bird’s taxonomy is useful for images. More generally, the
question of “what can go wrong with an LLM” isn’t limited to
prompt injection, and the different nature of the system may call
for different threat modeling.

Image by midjourney: "A clean flat editorial illustration of a friendly, simple robot standing at a table, holding up a round glass lens to examine a single glowing orb. Three more lenses of different sizes float in front of the orb, each showing it a little differently. Simple shapes, soft gradients, subtle shadows, deep indigo purple background, lime green and bright orange accents, red-orange highlights. Curious, thoughtful mood, plenty of negative space. No text, no padlocks"

Originally published by Adam on 01 Oct 2026

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

[Posts about Adam’s “Threats” book](/blog/category/threats-book)

[Posts about Adam’s “Threat Modeling” book](/blog/category/threat-modeling-book)

[Posts about “The New School of Information Security” book](/blog/category/the-new-school)

[About this blog](/blog/about)

## Subscribe (RSS/Mail)

RSS/ATOM: The RSS [feed is here](https://shostack.org/feed.xml). We recommend RSS as the best way to follow this blog, and think generally RSS is the best way to take control of the information you take in. You can [read our thinking here](https://shostack.org/blog/take-control-of-what-you-read).

Email: If you’d like a lower volume set of updates on what Adam is doing, [Adam’s New Thing](/contact) gets only a few messages a year, guaranteed. We include a subset of posts in each.

## Recent posts

[![A robot observes a threat through one lens while other lenses available to assess the threat hover nearby.](/images/blog/img/2026/lenses-for-threats-175w.jpeg)](/blog/threats-to-llms/)

### [Threats and LLMs (Threat Model Thursday)](/blog/threats-to-llms/)

01 Oct 2026

There are many ways to ask what can go wrong, and the useful skill is knowing which one matches what you're building.

[![A hand-sketched threat model diagram dissolves into a glowing indigo, lime, and orange 3D wireframe cube as abstraction transforms into precise structure.](/images/blog/img/2026/diagrams-or-models-175w.jpeg)](/blog/diagrams-versus-models/)

### [Diagrams versus Models (Threat Model Thursday)](/blog/diagrams-versus-models/)

24 Sep 2026

What does the new book tell us about the difference between diagrams and models?

[![A watercolor image of a robot and human at a San Francisco rooftop pool during a conference. The robot is about to dive in.](/images/blog/img/2026/owasp-pool-robot-175w.jpeg)](/blog/our-plans-for-owasp-and-threatmodcon-26/)

### [Heading to San Francisco and ready to party for OWASP's 25th](/blog/our-plans-for-owasp-and-threatmodcon-26/)

22 Sep 2026

If by party, you mean obsess over European bureaucracy, train people in the ways of the Force.. umm, threat modeling, and talk about the book until our voices give out.

[![an ai image of an ai ship](/images/blog/img/2026/pentagon-ai-175w.jpeg)](/blog/the-pentagon-china-ai-and-phantom-b/)

### [The Pentagon, China, AI and PHANTOM-B](/blog/the-pentagon-china-ai-and-phantom-b/)

21 Sep 2026

Could PHANTOM-B have stopped this close call?

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

[Book Reviews](/blog/category/book-reviews)

[News](/blog/category/news)

[Podcasts](/blog/category/podcasts), [Videos](/blog/category/videos) + [Webinars](/blog/category/webinars)
...