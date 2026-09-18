---
title: Diagrams and Common Elements (Threat Model Thursday)
url: https://shostack.org/blog/diagram-common-elements-threat-model-thursday/
source: Shostack & Friends Blog
date: 2026-09-17
fetch_date: 2026-09-18T06:52:46.878549
---

# Diagrams and Common Elements (Threat Model Thursday)

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
3. Diagrams and Common Elements (Threat Model Thursday)

Shostack + Friends Blog

# Diagrams and Common Elements (Threat Model Thursday)

All diagrams should have common elements, and using them consistently is a mark of skill and maturity
![A combined title block and legend from the new book](/images/blog/img/2026/title-blocks-and-legends-1684w.png)

Diagrams have a form, such as DFD, swim lane or C4, which is the
case even if they deviate from that form’s conventions. They have
style (or lack it). But regardless of the form or style of the
diagram, they should have a title block and a key (also called a legend). They can also have a convention of how to represent
what’s being worked on, and there’s one other common element you
should use and I’m not going
to make you read the book, but you do have to read this post.

## Title blocks

In my post on [Diagrams and Clarity](/blog/clarity-in-diagrams-threat-model-thursday/), I mentioned titles and
title blocks, and here I want to talk about those title blocks.

Title blocks are a requirement for those physical-world systems
that require an engineer’s approval, because exactly what the
engineer is approving has to be visible; engineers either stamp, seal
or sign these documents. A seal of approval was a thing before it
was a metaphor. What goes in a title block? That’s an
organizational decision, which should be informed by norms. The
Chapter on Models and Diagrams lists:

* Title
* Creator, approver
* Client name (ISO 7200 mandates the document’s owner!)
* Date, revision history
* Sheet number and total number of sheets
* Professional seals or stamps (e.g., architect’s license)
* Confidentiality block (typical in technology)

## Key or Legend

A legend can remind the creator to tell a consistent story, and
a key unlocks the diagram for the viewer. Which name to use? 🤷
Either one can be used to show all
the elements in use, or the unusual ones. If your organization uses [DFD3](https://github.com/adamshostack/DFD3/), there’s no
reason to list those elements, but listing the AWS icons is nice,
as is listing conventions like “TLS 1.3 unless starred.” I found no reason to prefer
either. Key is shorter and I’d look askance at anyone who brought
that up in a review meeting.

## What’s fixed and what’s in flux

The first question of threat modeling is “what are we working on?”
Most systems have elements being worked on in this sprint/this
iteration, and elements which are both fixed and worth showing on
a diagram. For example, if you’re working on a front end, it
might be worth including a load balancer and a database. Show
what’s being worked on with hatch-marks, dots, bold lines, or
other conventions. Again, the convention you’re using should be in the key
unless you have a strongly enforced organizational norm, and
the diagram won’t be shared with customers.

## Map grids

The final commonality you can use in a diagram is an old-fashioned
map grid. Back when maps were printed on paper, they had grids to
help you find a place (“If you’re on page 29, Market street is at
F-6.”) As diagrams increase in complexity, a map grid can help
people focus on the right part of the diagram. This is most useful
as diagrams get bigger, more detailed, or both.

All this and a whole lot more is part of Chapter 3, Diagrams and
Models, in the [second edition of Threat Modeling](/blog/threat-modeling-2nd-edition/).

Map grid from [HandtoMind](https://www.hand2mind.com/blog/free-printable-treasure-map-for-kids).

Originally published by Adam on 17 Sep 2026

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

[![A combined title block and legend from the new book](/images/blog/img/2026/title-blocks-and-legends-175w.png)](/blog/diagram-common-elements-threat-model-thursday/)

### [Diagrams and Common Elements (Threat Model Thursday)](/blog/diagram-common-elements-threat-model-thursday/)

17 Sep 2026

All diagrams should have common elements, and using them consistently is a mark of skill and maturity

[![Image of robots acting out the Four Question Framework](/images/blog/img/2026/threat-modeling-from-a-software-pov-175w.png)](/blog/threat-modeling-from-a-software-pov/)

### [Threat Modeling Intensive with Complete AI: From a Developer's POV](/blog/threat-modeling-from-a-software-pov/)

15 Sep 2026

Reflections from a Developer

[![A watercolor image of a book-covered desk in autumn. An open book with diagrams sits open on the desk, with a pencil and coffee nearby.](/images/blog/img/2026/back-to-school-sale-2026-175w.jpeg)](/blog/2026-back-to-school-sale-CBT-training/)

### [Dive into our annual Back to School sale on self-paced training](/blog/2026-back-to-school-sale-CBT-training/)

11 Sep 2026

Upgrade your engineering skills this fall with 20% off our self-paced Threat Modeling courses.

[![a very confused whiteboard diagram](/images/blog/img/2026/diagram-style-175w.jpeg)](/blog/diagram-style-threat-model-thursday/)

### [Diagram Style (Threat Model Thursday)](/blog/diagram-style-threat-model-thursday/)

10 Sep 2026

What makes a diagram good or useful?

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

[Podcast...