---
title: Focus on high priority threats(?)
url: https://shostack.org/blog/focus-on-high-priority-problems/
source: Shostack & Friends Blog
date: 2026-05-28
fetch_date: 2026-05-29T06:04:55.657547
---

# Focus on high priority threats(?)

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
3. Focus on high priority threats(?)

Shostack + Friends Blog

# Focus on high priority threats(?)

It’s easy to think prioritization is an easy problem, but it’s one deserving careful consideration.
![a photograph of an army of robots attacking and someone trying to prioritize](/images/blog/img/2026/high-priority-threats-1000w.png)

**“We need to focus on high priority threats!”**

We hear this all the time. In fact, it was practically a refrain at a
recent National Academies Forum on Cyber Resilience meeting on [Securing
AI systems](https://www.nationalacademies.org/units/DEPS-CSTB-13-03/event/46521). And it’s obvious. Given the challenges and the
practical speed at which companies are deploying AI systems, we
need to move quickly. Oh, and I also think it’s... worrisome, and quite possibly dangerous.

It’s worrisome because we might encounter one or more of:

* The threats prioritized are those that come to mind first.
* The search is stopped when a few apparently
  high-priority items have been found, or the “fix budget”
  seems full.
* Threats are implicitly prioritized, and likelihood or
  impact is mis-understood. Ignored threats are never
  revisited.

One of the advantages to modern threat modeling (compared to
brainstorming, abuse cases or even attack trees†) is that tools let us be
structured in our analyses. We’re not relying on a glance and an
instinctual claim of “these are the issues,” we’re walking through
(for example) a DFD and using STRIDE to perform an analysis, and
we can expect a certain number of issues to emerge. There are also
deeper analysis methods like STPASec or using the [Berryville Institute’s LLM ARA](https://berryvilleiml.com/docs/BIML-LLM24.pdf).

If we separate the questions of “what can go wrong” and “what are
we going to do about it,” then we can include a prioritization
step within “what are we going to do about it.”

Structuring our approach let us be confident we’re really
getting the high priority threats. What’s more, it’s important to specify and understand the prioritization scheme that’s in use. A great
deal of academic work on LLM-security focused on model theft,
a priority threat to those creating models, but perhaps less important
than [helping plan mass
shootings](https://www.npr.org/2026/04/23/nx-s1-5794016/openai-is-under-scrutiny-after-two-mass-shooters-used-chatgpt-to-plan-attacks). There are at least questions of ‘who’s hurt’ and
‘how the various harms relate to the motivations of AI tool creators.’

We should evaluate our prioritization approaches. This can be
tricky, because the issues which we prioritize may be prevented by
defenses we build. But in a research setting, we can evaluate aspects like intra-rater
consistency, and even same-rater consistency (how self-consistent
people are over time).

We can also evaluate threat discovery techniques. We can ask:

* Does this tool give consistent answers?
* How long does this tool take to use?
* What skills are needed to use this tool?

Research questions that I believe a National Academies Panel
should consider include:

1. What are the threat discovery techniques and what are
   their properties?
2. How do “fast and cheap” methods relate to more structured
   methods? What is the “effort” to “do more” and what does that
   “more” get us? For example, STRIDE is very general and may not provide
   LLM-specific analytic capabilities any better than brainstorming
   about LLMs. In contrast, the Berryville LLM ARA should provide
   both more specific threats. (This question is about threats, in
   contrast to the next, which is about defenses.)
3. What’s the relationship of specific analysis structures to
   defenses? Do the more specific threats lead to more specific
   defenses, or is the current set of defenses small enough that
   there’s limited benefit?
4. What are the prioritization schemes in use, how consistent
   are they and what
   biases might they encode?
5. How can we measure the reliability of prioritization
   methods?

† Some might be surprised by the claim about attack trees. To be more
specific, by themselves, trees provide a way to record an analysis, but no
guidance that leads to discovering
“there’s another way to achieve this goal.” Attack trees are
frequently used in conjunction with other techniques that provide
more structure.

Image Credit: Midjourney, “a photograph of an army of robots attacking and someone trying to prioritize”

Originally published by Adam on 28 May 2026

Categories:
  [security](/blog/category/security)
  [threat modeling](/blog/category/threat-modeling)

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

[![a photograph of an army of robots attacking and someone trying to prioritize](/images/blog/img/2026/high-priority-threats-175w.png)](/blog/focus-on-high-priority-problems/)

### [Focus on high priority threats(?)](/blog/focus-on-high-priority-problems/)

28 May 2026

It’s easy to think prioritization is an easy problem, but it’s one deserving careful consideration.

[![A diagram going from 23,019 finds to 88 advisories](/images/blog/img/2026/glasswing-fixes-175w.png)](/blog/vuln-finding-two-inflection-points/)

### [Vulnerability Finding: Two Inflection Points](/blog/vuln-finding-two-inflection-points/)

26 May 2026

Understanding the numbers from Anthropic and the system that surrounds Glasswing gives us new possibilities for effective defense.

[![Peter Neumann](/images/blog/img/2026/peter-neumann-175w.png)](/blog/remembering-peter-neumann/)

### [Remembering Peter Neumann](/blog/remembering-peter-neumann/)

23 May 2026

Peter Neumann helped define the field, and my career. He'll be missed terribly.

[![a robot viewing symbols on a whiteboard](/images/blog/img/2026/phantom-b-bh-175w.png)](/blog/blackhat-phantom-b/)

### [PHANTOM-B goes to Black Hat](/blog/blackhat-phantom-b/)

21 May 2026

A busy Black Hat: A new talk, a new practical tool, and a deadline you should know about

## Popular Blog Topics

[Threat Model Thursday](/blog/cat...