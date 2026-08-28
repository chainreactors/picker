---
title: Boundaries, Not Trust Boundaries (Threat Model Thursday)
url: https://shostack.org/blog/boundaries-threat-model-thursday/
source: Shostack & Friends Blog
date: 2026-08-27
fetch_date: 2026-08-28T13:37:04.039585
---

# Boundaries, Not Trust Boundaries (Threat Model Thursday)

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
3. Boundaries, Not Trust Boundaries (Threat Model Thursday)

Shostack + Friends Blog

# Boundaries, Not Trust Boundaries (Threat Model Thursday)

Boundaries are a crucial topic in the new threat modeling book
![Two houses, one with a fence and a clean yard](/images/blog/img/2026/boundaries-1000w.png)

Having [announced the new edition of Threat Modeling: Designing for
Security in an AI world](/blog/threat-modeling-2nd-edition/), I want to talk about some of the changes,
and the first change I want to cover is a whole new chapter on
“Trust and Boundaries,” and that “and” is important.

A key part of the new edition is that I’ve learned from those we
nominally teach, and this is the first lesson that I want to share from those learning
with us. The term “trust boundary” stymied some of them. They got
hung up and stayed hung up on the meaning of trust, and it didn’t
serve them.

So in the new edition, I’m simplifying by shortening that to “boundary.” The
concept of boundary is widely understood amongst developers,
operators and most everyone else. But even so, there’s
nuance. Informally, we use “boundary” to refer to the conceptual location, the policy
it’s expected to enforce, and the technical system that’s doing
so.

## Why boundaries matter

Failure to understand and enforce boundaries
is endemic. OpenAI’s failures that lead to their models hacking Huggingface were (in part)
a failure to consider how to make their boundaries work. Lack of
“non-human identity” is a boundary issue.

Another example was the Codecov incident, where an uploader script
[was able to initiate connections to random
hosts](https://about.codecov.io/security-update/) and also read secrets in the pipeline. Each of those
could be prevented with better boundaries. The first, don't allow
outbound connections from your pipeline, is pretty simple; the
second may be harder.

So the chapter goes through common technical boundaries like the
user-kernel boundary, firewalls, hardware, web servers and more
before diving deeply into isolation and policy, two important
concepts that are important tools in a toolbox.

The next major section is on coding defensively at a boundary,
including “Handle Input Like It’s Radioactive,” the relationship
between sanitization and validation, handling security before
business logic, how to handle input problems, and
attenuation. These are usually concepts that “security people” have often
picked up “along the way,” and need to be made concrete and
accessible to all engineers. Attenuation, by the way, is making
something less powerful. For example, we pass messages back and
forth, rather than shell scripts, because a shell script would
obviously give too much power to the caller.

The chapter then discusses the costs and side effects of
boundaries: speed, flexibility, and their relationship to existing
code. It closes out with organizational facets, like leveraging
domain driven design or team topologies to strengthen boundaries,
and an explicit discussion of terminology.

## Engineers at the center

A theme of this book is that you can’t bolt quality on, and
attempts to bolt security onto systems has failed. Expensively and consistently
for a long time. If we’re going to have more engineers build
security in, we’re going to need them to understand the things
that many security engineers understand. Or more, we’re going to
need them to understand the things which senior security engineers
understand. We don’t need them to be as facile or as capable as
someone who’s experienced (and a book won’t get them there
anyway). But we do need to start enumerating the concepts that we
expect people to know and apply, and we need to introduce those
concepts gently and well.

## Engineers work in organizations

The last concept here is another through-line for the book: That
engineering is done by people in organizations, and that good
threat modeling complements and improves how the organization
works. For example, if you use team topology concepts, boundaries help the teams ensure
that they remain loosely coupled, while also helping
security. Similarly, if you’re engineering with domain-driven
design, your objects become boundaries, enforcing domain rules as
they create and manage objects.

There’s a lot more to say, and next time I expect to talk about the
diagrams chapter.

Originally published by Adam on 27 Aug 2026

Categories:
  [books](/blog/category/books)
  [security](/blog/category/security)
  [threat modeling](/blog/category/threat-modeling)
  [threat model thursday](/blog/category/threat-model-thursday)
  [threat modeling 2nd edition](/blog/category/threat-modeling-2nd-edition)

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

[![Two houses, one with a fence and a clean yard](/images/blog/img/2026/boundaries-175w.png)](/blog/boundaries-threat-model-thursday/)

### [Boundaries, Not Trust Boundaries (Threat Model Thursday)](/blog/boundaries-threat-model-thursday/)

27 Aug 2026

Boundaries are a crucial topic in the new threat modeling book

[![An image of a man and robot working late into the night to ask what can go wrong](/images/blog/img/2026/survive-ai-disruption-175w.jpeg)](/blog/threat-modeling-technique-survives-AI-disruption/)

### [Why threat modeling is the technique that survives AI disruption](/blog/threat-modeling-technique-survives-AI-disruption/)

25 Aug 2026

AI is disrupting software security, but traditional threat modeling remains the ultimate survival skill.

[![An amazon blurb mentions a 2nd edition](/images/blog/img/2026/threat-modeling-2nd-ed-fancy-175w.png)](/blog/threat-modeling-2nd-edition/)

### [Threat Modeling: A Second Edition](/blog/threat-modeling-2nd-edition/)

20 Aug 2026

The long-awaited second edition of Threat Modeling...

[![Adam on stage at Black Hat 2026. The slide reads: All models are wrong, some models are useful](/images/blog/img/2026/bh26-talk-175w.jpeg)](/blog/phantom-b-talk-summary/)

### [Threat Modeling LLMs: Adam’s talk at Black Hat USA](/blog/p...