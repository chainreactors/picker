---
title: Diagrams versus Models (Threat Model Thursday)
url: https://shostack.org/blog/diagrams-versus-models/
source: Shostack & Friends Blog
date: 2026-09-24
fetch_date: 2026-09-25T06:52:25.484106
---

# Diagrams versus Models (Threat Model Thursday)

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
3. Diagrams versus Models (Threat Model Thursday)

Shostack + Friends Blog

# Diagrams versus Models (Threat Model Thursday)

What does the new book tell us about the difference between diagrams and models?
![A hand-sketched threat model diagram dissolves into a glowing indigo, lime, and orange 3D wireframe cube as abstraction transforms into precise structure.](/images/blog/img/2026/diagrams-or-models-767w.jpeg)

Diagrams are the most recognizable tools and deliverables of threat
modeling. (Both functions are important: the working tool of a
diagram which helps us ask what can go wrong and the deliverable
or record which we keep.)

In the first edition, I used the terms “diagram” and “model” nearly
interchangeably. In the second, I get more specific about the
differences. The dotted line in a diagram is *showing* a boundary,
or the controls, or where there are different principals. And
that’s what it is: A bunch of pixels which show the information. In a
model, those properties can be specified and acted on. Or even
derived: If each element in a model has an attribute about what
account it runs with, then you can *locate* boundaries
automatically. You may even be able to infer things about what
enforces the boundary. (Unix kernels, AWS IAM, hope, etc.)

In the second edition, I use the term *model* in two distinct ways: the first is ‘any
representation,’ while the second is a formalized construct with
technical properties.

Diagrams are easy, fast, and customizable. You can put any shape
you want in, you can break rules such as “no data sinks,” you can
slap a boundary through the middle of a process, and ain’t no
tooling gonna stop you. Models are harder to
build: There are questions about the properties that you’re going
to compute on later. You can’t fudge as easily. If you want
traceability from model to code (or vice versa), you need to spend
time connecting the two, and then maintain those connections. If
your model breaks the rules, a model checker can warn you, the
same way a compiler can (with the same pros and cons).

This dichotomy of “is it worth it” is a theme of the book, because
it’s a theme of threat modeling. How do we improve return on
investment? The first step is to know where you’re investing. If
your diagram tool requires a lot of
clicking, then you have to deal with the lots of clicks. And if you need a Visio license
before you can start, then there’s both the cash cost and the
administrative overhead of getting Visio. Neither adds materially
to the quality of a threat model, and so, with investment being
higher, the return must be increased as well.

A question I hear all the time is “do we need a diagram if we’re
asking an LLM to threat model for us?” The obvious answer is “no.”
The LLM will “threat model” (whatever that means) without a
diagram, or create one if its token stream stumbles on the idea it
needs one. A better question is “how do we get the LLM to do a
good job threat modeling?” The answer depends on how you engage
with its output. Is a diagram a useful checkpoint? Does it help
keep the LLM on task? Does it help the humans review the plan or
output? (I know, those things aren’t as fashionable as turning
dollars into tokens and burning them.)

LLMs can drive down the costs of diagramming or modeling. Above, I
wrote about the work to build models, and that really is
changing. The change is unevenly distributed, and its impact is
hard to see right now, but overarchingly, I think we’re going to
move from diagrams to models as the cost of those models drops,
enabling deeper, model-centered system analysis. But we won’t stop
there. There’s already work in model-driven system construction,
and it’s not limited
to security. It offers a route to generally better code, because it offers
us ways to specify and build systems with a larger number of more
predictable properties.

That model-centered development won’t eliminate the use of
exploratory or explanatory diagrams that I discussed in the post
on [diagrams and clarity](/blog/clarity-in-diagrams-threat-model-thursday/), but it will replace
people creating diagrams with design, as-built, and as-operated
diagrams being created on the fly from the system models.

Image by midjourney: "Split-composition illustration, left half a hand-drawn pencil sketch on graph paper of a threat model data-flow diagram with boxes, arrows, trust boundaries drawn as dashed lines, and a small stick-figure attacker icon, right half the same diagram morphing into a precise 3D CAD wireframe model floating in space with clean glowing wireframe edges and dimension annotations, the transition rendered as the pencil lines dissolving into glowing wireframe edges, dramatic side lighting, dark neutral background, palette of indigo purple, lime green, bright orange and red-orange, technical and precise on the right, loose and human on the left, no legible text"

Originally published by Adam on 24 Sep 2026

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

[![A hand-sketched threat model diagram dissolves into a glowing indigo, lime, and orange 3D wireframe cube as abstraction transforms into precise structure.](/images/blog/img/2026/diagrams-or-models-175w.jpeg)](/blog/diagrams-versus-models/)

### [Diagrams versus Models (Threat Model Thursday)](/blog/diagrams-versus-models/)

24 Sep 2026

What does the new book tell us about the difference between diagrams and models?

[![A watercolor image of a robot and human at a San Francisco rooftop pool during a conference. The robot is about to dive in.](/images/blog/img/2026/owasp-pool-robot-175w.jpeg)](/blog/our-plans-for-owasp-and-threatmodcon-26/)

### [Heading to San Francisco and ready to party for OWASP's 25th](/blog/our-plans-for-owasp-and-threatmodcon-26/)

22 Sep 2026

If by party, you mean obs...