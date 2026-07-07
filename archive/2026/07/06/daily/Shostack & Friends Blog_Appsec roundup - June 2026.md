---
title: Appsec roundup - June 2026
url: https://shostack.org/blog/appsec-roundup-june-2026/
source: Shostack & Friends Blog
date: 2026-07-06
fetch_date: 2026-07-07T06:03:56.488949
---

# Appsec roundup - June 2026

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
3. Appsec roundup - June 2026

Shostack + Friends Blog

# Appsec roundup - June 2026

From near misses to a new book on the C4 model and fundamental work by NIST showing the limits of today’s AI Guardrails, lots of exciting news about Application security.
![a photograph of a robot, sitting in a library, working on a jigsaw puzzle.](/images/blog/img/2026/appsec-roundup-spring-1000w.png)

This month leads off with [Close Calls in Cyberspace:
Strengthening Cybersecurity by Learning from Near-Misses](https://ojs.iscram.org/index.php/Proceedings/article/download/311/217) by Tommy
van Steen, Jeroen Wolbers, and Cristina Del-Real. I’m
happy to see research on how we can learn faster and better. All of our
security work should be informed by experience, and near misses
should be a rich source of such experience.

### Threat Modeling

* Simon Brown has an O’Reilly book on the [C4 Model](https://www.amazon.com/gp/product/B0GC5YKYFD). Amazon says it’ll
  be out this month.
* ThreatModCon Vienna happened: I was honored to be part of the
  unkeynote, which focused on the role of the [Threat
  Modeling Manifesto](https://www.threatmodelingmanifesto.org/) in a changing world. We talked about the
  importance of a journey of understanding, and how AI can exemplify
  both the “Hero Threat Modeler” and “Tendency to Overfocus”
  anti-patterns. I also led a mastermind session on how to apply
  layers, and James Reason’s “Swiss Cheese Model” to
  defenses stretching our answers to “What are we going
  to do about it?” beyond “controls” or mitigations.
![Adam presenting an awared to Brook](/images/blog/img/2026/brook-schoenfield-lifetime-achievement-award-400w.jpeg)* Saving the best
  for last, the conference awarded [Brook
  Schoenfield](https://brookschoenfield.com/) a lifetime achievement award. Brook was
  coincidentally in Vienna for vacation earlier in the week, so
  we presented him with the certificate on Tuesday, and I led a
  celebration on Saturday. (I hope to blog more about each of these
  over the coming weeks.)

### Appsec

* In [A Grounded Conceptual Model for Ownership Types in Rust](https://cacm.acm.org/research-highlights/a-grounded-conceptual-model-for-ownership-types-in-rust/), Will Crichton, Gavin Gray, and Shriram Krishnamurthi take a problem: Why don't people understand the borrow checker, and run it down from "how might they understand it now (and how can we find the problems they really experience), how can we teach it to them, and how can we evaluate that work?"
* The CVE program has a blog post, [Preserving
  Vulnerability-Level
  Identification in a Time of
  Increased Disclosure
  Volume](https://medium.com/%40cve_program/preserving-vulnerability-level-identification-in-a-time-of-increased-disclosure-volume-42adde0147d3) arguing that a CVE
  identifies a
  vulnerability. It’s a useful reminder.
* Relatedly, Jay Jacobs and Art Manion wrote [The Vulnerability Identity Crisis](https://research.empiricalsecurity.com/research/the-vulnerability-identity-crisis), about what we need to know to
  assign an identifier to a
  vulnerability. I kicked off a side conversation on
  Mastodon, [here](https://infosec.exchange/%40zmanion/116839758444006288).

### AI

* NIST released a [Mathematical
  Proof Supports Transition to a Continuous-Monitor-and-Update
  Security Model for AI Systems](https://www.nist.gov/news-events/news/2026/06/nist-mathematical-proof-supports-transition-continuous-monitor-and-update). Their summary says “The proof
  provides a rigorous explanation of the importance of transitioning
  from a ‘one and done’ security model.” I prefer Covertswarm’s
  summary, [AI guardrails will
  always fail](https://www.covertswarm.com/post/ai-guardrails-will-fail-nist-mathematical-proof), and their pull quote: “**There is no finite set of
  guardrails that is universally robust against adversarial
  prompts**.” Of course, this is what Shoshana Cox has been saying
  **for years** and that’s part of why we’re so excited
  that she and Mike Novack designed and teach our [Threat
  Modeling AI Systems](https://courses.shostack.org/courses/Threat-Modeling-AI-Systems-225) course: they [understand the limits](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A7470584934194315265/) of today’s defenses, and have not been shy
  about speaking about them. If you’re interested in the only
  training course that’s ahead of that news, we’d be happy to [hear from you](https://shostack.org/contact).

### Games Received

* [Cyber Defense Dice](https://cyberdefencedice.com/), created by Steven Furnell and team and the University of Nottingham. “A Cyber Awareness Game of Attack and Defence for 2 Players or Teams. Easy to play and suitable for casual use or as an engaging activity for cyber security awareness-raising sessions.”

![A set of dice](/images/blog/img/2026/cyberdefencedice-500w.png)

---

### Shostack + Associates News

* Adam and team will be delivering [Threat
  Modeling Intensive with
  Complete AI](https://blackhat.com/us-26/training/schedule/#adam-shostacks-threat-modeling-intensive-with-complete-ai-51473) at Blackhat
  August 1-4.
* Adam will be presenting [Threat
  Modeling LLMs: The PHANTOM-B model](https://blackhat.com/us-26/briefings/schedule/index.html#threat-modeling-llms-the-phantom-b-model-53809) Wednesday, August 5 |
  11:05am-11:45am ( Oceanside C ). He’ll reprise the talk at the
  AppSec Village during DEF CON.

Originally published by Adam on 06 Jul 2026

Categories:
  [ai](/blog/category/ai)
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

RSS/ATOM: The RSS [feed is here](https://shostack.org/feed.xml). We recommend RSS as the best way to follow this blog, and think generally RSS is the best way to take control of the information you take in. You can [read our thinking here](https://shostack.org/blog/take-control-of-what-you-read).

Email: If you’d like a lower volume set of updates on what Adam is doing, [Adam’s New Thing](/contact) gets only a few messages a year, guaranteed. We include a subset of posts in each.

## Recent posts

[![a photograph of a robot, sitting in a library, working on a jigsaw puzzle.](/images/blog/img/2026/appsec-roundup-spring-175w.png)](/blog/appsec-roundup-june-2026/)

### [Appsec roundup - June 2026](/blog/appsec-roundup-june-2026/)

06 Jul 2026

From near misses to a ne...