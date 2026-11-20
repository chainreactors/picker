---
title: Validate, Don't Sanitize
url: https://shostack.org/blog/validate-dont-sanitize/
source: Shostack & Friends Blog
date: 2026-11-19
fetch_date: 2026-11-20T09:21:47.059605
---

# Validate, Don't Sanitize

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
3. Validate, Don't Sanitize

Shostack + Friends Blog

# Validate, Don't Sanitize

Adam Shostack, Shostack + Associates

Sanitization is almost always a mistake, and it’s important to understand why.
![A broken, out of spec coin sits in the coin return tray of a vending machine.](/images/blog/img/2026/validate-dont-sanitize-gemnb-1000w.jpeg)

Advice to sanitize input is maddeningly common in security
advice. It’s always a mistake, and it’s a mistake that collects
compounding technical debt interest.

Let’s start with what you should do. Check that input is what you
expect. If it’s not, issue a specific error like “malformed input at byte
X. See our spec at URL.” (This advice doesn’t apply to web
browsers, and we’ll come to that.)

The most important reason is that when you sanitize, you’re parsing
input that doesn’t meet your spec. Let me repeat that: you’re
parsing input that doesn’t meet your spec. And so you’re helpfully
trying to make it right. The trouble is, it’s out of spec. And
getting it in spec carries both a security hazard (you might bypass
your own checks) and a reliability hazard (you might not fix it in
alignment with the caller’s intent even if they’re not attacking).

You’re
parsing input that doesn’t meet your spec.

A security example would be: if you filter out slashes, and then do a URL
decoding, your %2F will become a slash, and that slash might get
passed to somewhere that your
code treats as a path. Of course, it’s *possible* to get this right
every time. The work to get that right and to build unit tests to ensure
it’s right, grows with each such element. The portion of your
codebase and build time dedicated to security special cases grows
without bounds.

The debt isn’t just yours. Once you accept bad input, your
sanitizer is subject to a perversely ugly version of [Hyrum’s Law](https://www.hyrumslaw.com/): you’re committing to parse input
that’s now included in the unwritten part of your spec.

The best you can get from all the investment is the chance to
invest more, which is, admittedly, sometimes worth it.

That brings me back to web browsers. In the [first browser war](https://en.wikipedia.org/wiki/Browser_wars), they did their
damnedest to turn bad HTML into properly displayed web pages. They
did that because if the browser parsed carefully, it was “broken.”
The user
would open their other browser and not switch back until the other
browser ~~broke~~ didn’t display a page. This contributed
to it being so expensive to create and maintain a browser that
only a few companies make the investment.

It might be tempting to try to parse more of the input, so you can
provide “more useful” errors. And again, you’re parsing input your code doesn’t
understand. Enjoy! Now, that’s not to say you can’t put a copy of
your parser on the far side of a boundary to provide a fast, local test. But
you cannot trust that that parser ran, or that its output is
unmodified.

Sometimes people argue that the robustness principle of “Be conservative
in what you send and liberal in what you accept” implies
sanitization. It does not. You can be liberal about what you
accept and robustly send “malformed input” errors. The input is
accepted and handled robustly.

The distinction between validation and sanitization is an example
of how to code denseively, which is a layer of [the Swiss cheese model](https://shostack.org/blog/cybersecurity-defenses-a-swiss-cheese-model/) in the [new book](https://amzn.to/4urxcBJ).

As I say in Threats: What Every Engineer Should Learn from
Star Wars, you can never quite get the stink of Tauntaun out
of your clothes. Stop trying.

Image by Gemini Nano Banana 2: "A watercolor painting of the front panel of a pale cream vending machine, with a round coin slot and a small coin return tray. A single bent lime green coin sits in the return tray, rejected. Deep indigo purple only as thin outlines around the slot and tray and in small shadows, bright orange trim along the panel edge, red-orange highlights on the coin return button. Mostly warm cream and white, light and airy."

Originally published by Adam on 19 Nov 2026

Categories:
  [books](/blog/category/books)
  [software engineering](/blog/category/software-engineering)
  [security](/blog/category/security)
  [threat modeling 2nd edition](/blog/category/threat-modeling-2nd-edition)
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

[![A broken, out of spec coin sits in the coin return tray of a vending machine.](/images/blog/img/2026/validate-dont-sanitize-gemnb-175w.jpeg)](/blog/validate-dont-sanitize/)

### [Validate, Don't Sanitize](/blog/validate-dont-sanitize/)

19 Nov 2026

Sanitization is almost always a mistake, and it’s important to understand why.

[![A robot sits beside a small carry-on suitcase while contemplating what to pack from the mountain of choices beside it.](/images/blog/img/2026/defenses-tradeoffs-175w.jpeg)](/blog/modeling-and-analyzing-defenses/)

### [Defenses: Protect, Detect, Respond and much more (Threat Model Thursday)](/blog/modeling-and-analyzing-defenses/)

12 Nov 2026

How do you choose defenses when you can’t cover everything and useability is something you shouldn't trade away?

[![A banner from the Software Safety Initiative with their logo stating that Software runs the world; it should be safe.](/images/blog/img/2026/software-safety-initiative-ssi-175w.png)](/blog/Welcome-to-the-Software-Safety-Initiative/)

### [A warm welcome to the Software Safety Institute](/blog/Welcome-to-the-Software-Safety-Initiative/)

09 Nov 2026

A significant new voice for software safety has joined the field, and Adam is proud to lend his support.

[![A header image for conferences with a full audience ready for a threat modeling talk on the right and space for talk names and venues on the left.](/images/blog/img/2026/OWASP-and-TMC-slide-heade...