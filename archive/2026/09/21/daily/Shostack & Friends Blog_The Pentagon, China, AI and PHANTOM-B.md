---
title: The Pentagon, China, AI and PHANTOM-B
url: https://shostack.org/blog/the-pentagon-china-ai-and-phantom-b/
source: Shostack & Friends Blog
date: 2026-09-21
fetch_date: 2026-09-22T07:04:05.223467
---

# The Pentagon, China, AI and PHANTOM-B

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
3. The Pentagon, China, AI and PHANTOM-B

Shostack + Friends Blog

# The Pentagon, China, AI and PHANTOM-B

Adam Shostack, Shostack + Associates

Could PHANTOM-B have stopped this close call?
![an ai image of an ai ship](/images/blog/img/2026/pentagon-ai-1000w.jpeg)

CNN has an explosive story with [US military
having a
close call after using AI for
false intelligence
report](https://edition.cnn.com/2026/09/18/politics/us-military-ai-false-intelligence-china-ship). There were planes
in the air and the United
States was ready to initiate
military action against a Chinese ship:
> It was only just before the planned operation that officials
> dug deeper into the report put
> together by a special
> operations command analyst and
> found it had been generated
> with the help of artificial
> intelligence (AI) — and that a
> chatbot the analyst had used
> inaccurately identified the
> material the ship was
> carrying. CNN was not able to
> learn what the misidentified
> cargo was.
> The report, according to one of the sources, was “entirely false.” But
> it also “almost started a war,” the source said. Any US
> operation against a Chinese vessel could have risked spiraling
> into an armed conflict between the two nations.

Now, it’s unclear from CNN’s reporting if it was a Chinese-flagged
merchant ship, or a Chinese military vessel. (The other
articles I’ve seen report on what CNN has reported, and have
not developed new facts; I expect more will emerge.) While either would be
bad, attacking a military vessel would be more likely to lead
to a broader
conflict. That broader conflict is yet more likely while the
war with Iran has left the US military with [depleted inventories
of missiles](https://www.japantimes.co.jp/news/2026/09/19/world/us-allies-missile-delivery-delays/) and other supplies.

Whatever sort of ship it was, the issue here is how the military is
using AI, and here, I want to talk about PHANTOM-B and threat
modeling LLM-centered applications. (You can get a broad
overview from [our PHANTOM-B blog post](/blog/phantom-b-talk-summary/) or from our [whitepapers
page](/resources/whitepapers).) The “O” in PHANTOM-B stands for Overreliance, and
it means just that: relying on the model. Apparently, the
command analyst had generated a report, and not checked the
key facts.

In the August paper, I wrote “If you let your model
produce results without oversight, you’re going to be at least
embarrassed, if not worse.” I wasn’t thinking that the
Pentagon’s new AI strategy would go so far as letting AI make
deployment or mission decisions without proper oversight, because after
all, some commander is putting troops in harm’s way, and I
would hope that commander would meet his duty to those
soldiers. (That strategy is described in the CNN article
linked at the top.)

That hope drives demand, and that
demand leads to
pressure to deploy.

Making consequential decisions is at the heart of “what can go
wrong” with LLMs, and the list of ways
over-reliance plays out goes on and on: This [person gets arrested](https://www.valleynewslive.com/2026/09/15/tennessee-woman-sues-fargo-ex-detective-over-wrongful-arrest-tied-facial-recognition-error/). We shouldn’t [hire Asian candidates](https://hai.stanford.edu/news/ai-hiring-tools-can-yield-racial-bias-and-systemic-rejection). We should [lay off
people who took maternity leave](https://www.theguardian.com/technology/2026/jul/14/meta-ai-mass-layoffs-lawsuit).

The reason we made PHANTOM-B a small, usable tool is that there’s
tremendous hope that LLMs will let us make decisions faster
and better. That hope drives demand, and that demand leads to
pressure to deploy. If we have simple ways to analyze a plan,
that simple way is more likely to be used.

PHANTOM-B provides a short set of human-level prompts to consider
what can go wrong. (It’s literally designed to fit on a wallet
card; you can get those [PHANTOM-B wallet cards](https://cybersecgames.com/collections/adam-shostack/products/phantom-b-wallet-cards-by-adam-shostack-pack-of-10) from our partner,
Cybersecurity Games.) It’s free and creative-commons licensed.

That prompting to consider over-reliance can drive
interventions or checkpoints in the design of a system. For example, a
checklist item of “have you checked the key facts” or “will
you stand by the recommendations in this report?” It could
lead to the analyst or their commander asking “what here came
from AI.” The crucial improvement is a recognition that
over-reliance is a threat to the system.

Or, you know, you could start a war. Your choice. (Please don’t
start more wars.)

Image: Overly reliant on Gemini.

Originally published by Adam on 21 Sep 2026

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

[![an ai image of an ai ship](/images/blog/img/2026/pentagon-ai-175w.jpeg)](/blog/the-pentagon-china-ai-and-phantom-b/)

### [The Pentagon, China, AI and PHANTOM-B](/blog/the-pentagon-china-ai-and-phantom-b/)

21 Sep 2026

Could PHANTOM-B have stopped this close call?

[![A combined title block and legend from the new book](/images/blog/img/2026/title-blocks-and-legends-175w.png)](/blog/diagram-common-elements-threat-model-thursday/)

### [Diagrams and Common Elements (Threat Model Thursday)](/blog/diagram-common-elements-threat-model-thursday/)

17 Sep 2026

All diagrams should have common elements, and using them consistently is a mark of skill and maturity

[![Image of robots acting out the Four Question Framework](/images/blog/img/2026/threat-modeling-from-a-software-pov-175w.png)](/blog/threat-modeling-from-a-software-pov/)

### [Threat Modeling Intensive with Complete AI: From a Developer's POV](/blog/threat-modeling-from-a-software-pov/)

15 Sep 2026

Reflections from a Developer

[![A watercolor image of a book-covered desk in autumn. An open book with diagrams sits open on the desk, with a pencil and coffee nearby.](/images/blog/img/2026/b...