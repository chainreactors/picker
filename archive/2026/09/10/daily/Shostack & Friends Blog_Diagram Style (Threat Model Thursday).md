---
title: Diagram Style (Threat Model Thursday)
url: https://shostack.org/blog/diagram-style-threat-model-thursday/
source: Shostack & Friends Blog
date: 2026-09-10
fetch_date: 2026-09-11T06:52:13.652689
---

# Diagram Style (Threat Model Thursday)

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
3. Diagram Style (Threat Model Thursday)

Shostack + Friends Blog

# Diagram Style (Threat Model Thursday)

What makes a diagram good or useful?
![a very confused whiteboard diagram](/images/blog/img/2026/diagram-style-1000w.jpeg)

What makes for a beautiful and useful diagram? That’s an important
question, and one that we often touch on in training, as some
folks create diagrams that are beautiful, and others create ones
that are... hard to read. And beauty isn’t the only quality we
want, and perhaps isn’t even the best name. Beauty is a function
of readability and style, and good diagrams go beyond readability
and style by following some rules about what they incorporate and
how they show it.

Specific and actionable advice for how to make a diagram readable
and usable are an important addition to the new edition. The full
discussion spans several pages, and below are
excerpts from the lists in Chapter 3 of the [new edition of Threat
Modeling](/blog/threat-modeling-2nd-edition/):

## Readability

* Align with how we read. In many places, people write from left to right
  and top to bottom, so draw the same way to align with Western reading
  norms. (Adjust as needed if you work with other cultures.)
* Limit use of off-diagram references such as “A1” or “T3” that lead to head
  swiveling or page flipping.
* Label the unusual. If most connections are encrypted, specify that and
  mark the ones that are not.
* Keep lines short. Short lines are easier to follow.

## Style

* Fan in, fan out. Often, a central element of a diagram (“the system” or a
  dispatcher/queue manager) has many clients or connects out to many
  places. These fan in or fan out, and putting an element in the center, with
  clients on the left and the servers it talks to on the right, makes sense.
* Calmness is valuable and hard to achieve. A calm diagram carries a subtext of “We worked on this for you.”
* Diagram elements of the same size, on a grid, are calmer.
* Straight lines are calm, and they become less calm with each bend.
* Lines that cross are less calm. Swapping the placement of elements is a
  good technique for reducing line crossings.

## Rules

* Use unique labels. If you have three elements labeled “server” in a diagram, the label should be more specific. If you have several identical
  servers, you can use offset stacking.* Boundaries are explicitly shown for (at least) data centers, cloud providers,
    client devices, and other zones of administrative control.
  * Only data flows cross boundaries.

Using a diagram entails *understanding* it and then *using
it* to either ask or answer questions about the represented
system. The harder the diagram is to understand, the more work is
needed to get any value.

Diagram effort includes creating, refining, redrawing and
interpreting a diagram.

Return on effort is a major theme of the book. Thinking about the
work we put into either creating or using a diagram lets us ask “is
this next increment worthwhile?” “To whom is it valuable?” and “why
would it be valuable?”

As I [talked about in last week’s post](/blog/clarity-in-diagrams-threat-model-thursday/), the effort involved increases as you go from an
exploratory diagram to a diagram of record.

A diagram that’s pleasing to the eye is one with a clear purpose,
and that’s easy to use as we implicitly or explicitly trace how a system
works. A diagram where someone has shown care in
making it readable communicates that this is important enough to
do well. That effort pays off
for the users of the diagram mainly because they work faster, but
also because you’re showing respect by having made their work easier.

Image by Gemini, iterated prompts starting from
“Draw me a diagram that violates many of these rules.”

Originally published by Adam on 10 Sep 2026

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

[![a very confused whiteboard diagram](/images/blog/img/2026/diagram-style-175w.jpeg)](/blog/diagram-style-threat-model-thursday/)

### [Diagram Style (Threat Model Thursday)](/blog/diagram-style-threat-model-thursday/)

10 Sep 2026

What makes a diagram good or useful?

[![A promotional image for Threat Modeling, the bible of threat modeling, available for pre-order now!](/images/blog/img/2026/B&N-preorder-175w.jpeg)](/blog/barnes-and-noble-preorder-sale/)

### [Save on Threat Modeling 2nd Edition](/blog/barnes-and-noble-preorder-sale/)

09 Sep 2026

Barnes & Noble is having a preorder sale. Save on Adam's new book, coming February 2027!

[![a photograph of a robot, sitting in a library, working on a jigsaw puzzle. The robot holds up the jigsaw puzzle, and snow is falling inside the library](/images/blog/img/2025/appsec-roundup-aug-2025-175w.png)](/blog/appsec-roundup-july-aug-2026/)

### [Appsec roundup - July + August 2026](/blog/appsec-roundup-july-aug-2026/)

09 Sep 2026

The CRA, how AI is showing up in security requirements, threat modeling, bug fixing and inventing biases in its spare time. Also, a lot of cool books by other authors.

[![A diagram showing exploration and explanation feeding into design, into as-built and as-operated](/images/blog/img/2026/boundaries-in-threat-modeling-175w.jpeg)](/blog/clarity-in-diagrams-threat-model-thursday/)

### [Diagrams and Clarity (Threat Model Thursday)](/blog/clarity-in-diagrams-threat-model-thursday/)

03 Sep 2026

Diagrams serve needs, and surprisingly, form follows function

## Popular Blog Topics

[Threat Model Thursday](/blog/category/threat-model-thursday),
exploring specific published threat models

[Threat Modeling](/blog/category/threat-modeling) (general topic)

[Application Security](/blog/category/application-security)

[Software Engineering](/blog/category/software-engineering)

[Cloud Security](/blog/category/cloud-security)

[Compliance](/blog/catego...