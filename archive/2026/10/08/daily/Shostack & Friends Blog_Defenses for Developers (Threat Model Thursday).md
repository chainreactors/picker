---
title: Defenses for Developers (Threat Model Thursday)
url: https://shostack.org/blog/threat-model-thursday-defenses-developers/
source: Shostack & Friends Blog
date: 2026-10-08
fetch_date: 2026-10-09T08:10:59.978570
---

# Defenses for Developers (Threat Model Thursday)

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
3. Defenses for Developers (Threat Model Thursday)

Shostack + Friends Blog

# Defenses for Developers (Threat Model Thursday)

Defenses are often confusing, and developers make the security choices that are hard to reverse. But if you can handle git, you can handle threat modeling.
![A watercolor painting of a silhouetted figure stands at a fork where several glowing trails wind away under an indigo sky, each trail marked by a signpost.](/images/blog/img/2026/defenses-developers-tmt-1000w.jpeg)

Every developer ought to know as much about threat modeling as they
know about git, because developers are the ones making the
decisions about security, and making choices that are hard to
reverse. And so they ought to have tools to consider what can go
wrong in security, and what to do about it.

One of the challenges they face is that defenses are... hard to
understand. From the language we use (“controls”? “solutions?” Why
doesn’t the product do what it needs to be safe out of the box?)
to the multitude of types of defenses, we could productively focus
more on thinking clearly, considering their needs, and and working
to communicate well.

One of the major drivers for the second edition ([Threat
Modeling: Designing for Security in an AI World](https://amzn.to/4urxcBJ)) has been to
address developers’ needs in ways that complement  [Threats](https://amzn.to/3Pu8axg). And
so, in this edition, I’ve focused a lot of my work rebuilding
the way that I present defenses. The first edition had a set
of chapters:

7. Processing and Managing Threats
8. Defensive Tactics and Technologies
9. Trade-Oﬀs When Addressing Threats
10. Validating That Threats Are Addressed

In retrospect, that’s not organized great. “Trade-Offs” is a
chapter which is largely about risk management, with a
sideline into prioritization, and doesn’t really talk about
tradeoffs we might make, such as usability or performance. So
I rebuilt that. It’s now:

9. Technical Defenses
10. Defense Project Management
11. Risk Manage What Remains

That starts from the concrete, “what can I do about this?”
That’s shaped by the sort of thing we’re working on. If I’m
building a Windows app, I have different choices to make than
if I’m building on Android or AWS. It continues to how well
developed a product or feature are: the more people who’ve
taken dependencies on something, the harder it is to
change.

The answers are frequently singular, and perhaps “obvious” to those
with technical skill in security. And as we teach, we routinely
see people tying... strange defenses to the threats. (We rarely
correct it very aggressively: we’re defending hypothetical systems, and
we hope that those building real defenses will do a bit more
dilligence.) But people are often faced with complex choices and
they need to integrate those many choices into complex software
projects, and that requires project management, including much of
what was previously in the chapter on processing and managing threats.

The new edition also includes an appendix on Defense Technologies,
which tries to act as a guide to the many catalogs of defenses.

With that, let me loop around to my opening line: As much as git? Is
that a good thing? Most engineers don’t understand git very well,
and use it with a small cookbook of techniques (and support from
an LLM). Is that an aspirational endgoal for threat modeling?
Frankly, no. But it is an aspirational *milestone*. Threat
modeling is simper than git. The complexities of branches, staging
areas, commits, and more are nearly inescapable, giving git a very
steep learning curve. (Much steeper than competing version control
systems, to enable its decentralized nature.) So I believe that
much of the work of the past decades to democratize and make
threat modeling accessible makes it reasonable to say “if you can
handle git, you can handle threat modeling.”

Image by midjourney: "A watercolor painting of a person standing at a fork in a winding path, with several trails branching ahead, each marked by a simple signpost in a different shape. One trail is lit more brightly than the others. Soft bleeding washes, visible paper texture, loose edges, deep indigo purple background, lime green and bright orange accents, red-orange highlights."

Originally published by Adam on 08 Oct 2026

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

[![A watercolor painting of a silhouetted figure stands at a fork where several glowing trails wind away under an indigo sky, each trail marked by a signpost.](/images/blog/img/2026/defenses-developers-tmt-175w.jpeg)](/blog/threat-model-thursday-defenses-developers/)

### [Defenses for Developers (Threat Model Thursday)](/blog/threat-model-thursday-defenses-developers/)

08 Oct 2026

Defenses are often confusing, and developers make the security choices that are hard to reverse. But if you can handle git, you can handle threat modeling.

[![A robot observes a threat through one lens while other lenses available to assess the threat hover nearby.](/images/blog/img/2026/lenses-for-threats-175w.jpeg)](/blog/threats-to-llms/)

### [Threats and LLMs (Threat Model Thursday)](/blog/threats-to-llms/)

01 Oct 2026

There are many ways to ask what can go wrong, and the useful skill is knowing which one matches what you're building.

[![A hand-sketched threat model diagram dissolves into a glowing indigo, lime, and orange 3D wireframe cube as abstraction transforms into precise structure.](/images/blog/img/2026/diagrams-or-models-175w.jpeg)](/blog/diagrams-versus-models/)

### [Diagrams versus Models (Threat Model Thursday)](/blog/diagrams-versus-models/)

24 Sep 2026

What does the new book tell us about the difference between diagrams and models?

[![A watercolor image of a robot and human at a San Francisco rooftop pool during a c...