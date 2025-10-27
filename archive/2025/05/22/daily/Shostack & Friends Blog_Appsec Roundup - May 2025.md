---
title: Appsec Roundup - May 2025
url: https://shostack.org/blog/appsec-roundup-may-2025/
source: Shostack & Friends Blog
date: 2025-05-22
fetch_date: 2025-10-06T22:30:13.990073
---

# Appsec Roundup - May 2025

[Skip to main content](#main-content)

[![Shostack and Associates logo, click for Homepage](/img/Shostack-logo-white.png)](/)

* [About](/about/)
  + [Shostack + Associates](/about/)
  + [Adam Shostack](/about/adam/)
* [Services](/training/)
  + [Training](/training/)
  + [Accelerator](/secure-design-accelerator/)
  + [Expert Witness](/expert-witness/)
  + [Consulting](/consulting/)
* [Resources](/resources/)
  + [Overview](/resources/)
  + [Threat Modeling](/resources/threat-modeling/)
  + [Books](/books/)
  + [Games](/tm-games/)
  + [Cyber Public Health](/resources/cyber-public-health/)
  + [Lessons Learned](/resources/lessons/)
  + [Videos](/resources/videos/)
  + [Whitepapers](/resources/whitepapers/)
* [Blog](/blog/)
* [Contact](/contact/)

1. [Shostack + Associates](/)
2. [Blog](/blog/)
3. Appsec Roundup - May 2025

Shostack + Friends Blog

# Appsec Roundup - May 2025

Lots of fascinating threat model-related advances, new risk management tools, games, and more!
![a photograph of a robot, sitting in a library, working on a jigsaw puzzle](/images/blog/img/2025/appsec-roundup-feb-25-1000w.png)

### Threat Modeling

* Patrick Opet, Chief Information Security Officer of JP Morgan Chase wrote an  [An open letter to third-party suppliers](https://www.jpmorgan.com/technology/technology-blog/open-letter-to-our-suppliers). Gunnar Peterson has [some thoughts](https://defensiblesystems.substack.com/p/some-thoughts-pat-opets-open-letter), as does [Mike Schwartz](https://www.linkedin.com/pulse/open-letter-patrick-opet-ciso-jpmorgan-chase-put-center-mike-schwartz-dpxhc/?trackingId=8XmqstY3WPV6g%2FRzfWHL8Q%3D%3D). I like Mike’s suggestion of leveraging Capabilities (in the sense of unforgable access tokens), but not his new terminology. So why is this in threat modeling, even though the letter doesn’t mention it? Because being responsive to it will require companies to have good threat modeling records and writeups.
* Paco Hope has some insightful thoughts in on ways people get threat modeling wrong in a [linkedin post](https://www.linkedin.com/posts/pacohope_ive-been-spending-a-lot-of-time-thinking-activity-7324180200101974017-HRzh), including assumptions that input is complete and correct, treating threat models as a deliverable, and the need for context.
* He also has a blog post, [Amazon S3 Shows How LLMs Get Things Wrong](https://blog.paco.to/2025/amazon-s3-shows-how-llms-get-things-wrong/), because of the quantities of training data that have outdated information. That’s highly relevant to how a lot of people hope to use LLMs to threat model, but cuts much more broadly.
* Archival video from [Michael Howard](https://www.youtube.com/watch?v=YkTPpG0iLTc) presenting on threat modeling to Microsoft’s Trustworthy Computing Academic Advisory Board in 2003.

### Appsec

* Jason Chan has a long article in TL;DRSec, [Security for High Velocity Engineering](https://tldrsec.com/p/security-for-high-velocity-engineering), which is worth reading. One of the key points he makes is to focus on high-leverage work, which he defines as impact produced divided by time invested. There are two ways to do this, but the easier way is to drive down time investments through tooling and then ruthless process optimization. Many organizations have developed threat modeling programs that are paperwork-heavy and tedious, and it’s hard to get value from them. But if you drive down the time investment in ways that maintain value, then your leverage improves.

### LLM Security

* [AIRiskButt](https://airiskbutt.com/) is now launched, and I’m really impressed by the hard work that’s gone into it.

### Regulation

* The UK has released a voluntary [Software Security Code of Practice](https://www.gov.uk/government/publications/software-security-code-of-practice/software-security-code-of-practice). It’s somewhat redundant. For example, it starts with “1.1 Follow an established secure development framework.” Then it continues with 1.2, do SCA and 1.3, follow secure by design principles. Is there a secure development framework that misses those things? If not, why are they there? Are they extra important? Are they more important than say, threat modeling? I don’t believe they are. Similarly, 3.3, “detect and manage vulns in components” seems like it overlaps with 1.2 “assess risks linked to the ingestion and maintenance of third-party components throughout the development lifecycle.” I encourage the UK to rebuild it to clearly state what’s addititive to established
  frameworks. That’s undifferentiated work, and the creators ought to do it once and authoritatively.

### Games recieved

![The Cyber Attack Chain game](/images/blog/img/2025/cyber-attack-chain-1000w.png)

I got a copy of [Cyber Attack Chain](https://www.educationarcade.co.nz/product-page/cyber-attack-chain-retail-pack), and it came with a nice handwritten note.

### Shostack + Associates updates

* We’re delivering [free training for displaced Federal workers](https://shostack.org/blog/threat-modeling-training-for-federal-workers/). It’s a distributed, live instruction version of the course.
* Adam will be training at Blackhat USA, [Aug 2-3](https://www.blackhat.com/us-25/training/schedule/#adam-shostacks-threat-modeling-intensive-44283) or [4-5](https://www.blackhat.com/us-25/training/schedule/#adam-shostacks-threat-modeling-intensive-442831736891193).

Image by Midjourney: “a photograph of a robot, sitting in a library, working on a jigsaw puzzle”

Originally published by Adam on 02 Jun 2025

Categories:
  [application security](/blog/category/application-security)
  [software engineering](/blog/category/software-engineering)
  [security](/blog/category/security)

## Our Favorite Content

[General threat modeling posts](/blog/category/threat-modeling/)

[The Security Principles of Saltzer and Schroeder, illustrated with Star Wars](/blog/the-security-principles-of-saltzer-and-schroeder/)

[Other Star Wars blog posts](/blog/category/star-wars/)

[Modeling attackers and their motives](/blog/modeling-attackers-and-their-motives/)

[Doing science with near misses](/blog/doing-science-with-near-misses/)

[Posts about Adam’s “Threats” book](/blog/category/threats-book/)

[Posts about Adam’s “Threat Modeling” book](/blog/category/threat-modeling-book/)

[Posts about “The New School of Information Security” book](/blog/category/the-new-school/)

[About this blog](/blog/about/)

## Subscribe (RSS/Mail)

RSS/ATOM: The RSS [feed is here](https://shostack.org/feed.xml). We recommend RSS as the best way to follow this blog, and think generally RSS is the best way to take control of the information you take in. You can [read our thinking here](https://shostack.org/blog/take-control-of-what-you-read/).

Email: If you’d like a lower volume set of updates on what Adam is doing, [Adam’s New Thing](/contact/) gets only a few messages a year, guaranteed. We include a subset of posts in each.

## Recent posts

[![a photograph of a robot, sitting in a library, working on a jigsaw puzzle](/images/blog/img/2025/appsec-roundup-aug-2025-175w.png)](/blog/appsec-roundup-sept-2025/)

### [Secure By Design roundup - September 2025](/blog/appsec-roundup-sept-2025/)

01 Oct 2025

The secret service, the CSRB, the CMMC, Sept was pretty busy in government. Plus Apple's Memory Integrity and a nice short paper on prompt-based attacks.

[![Thumbnail for podcast episode](/images/blog/img/2025/medtech-innovation-podcast-175w.png)](/blog/medtech-innovation-podcast/)

### [Adam Featured on Inside MedTech Innovation](/blog/medtech-innovation-podcast/)

29 Sep 2025

Learn from the past and advance your threat modeling skills!

[![A moon buggy model at the Museum of Flight](/images/blog/img/2025/moon-buggy-museum-of-flight-175w.png)](/blog/lunar-rover-vehicle-redux/)

### [Lunar Rover Vehicle, Redux](/blog/lunar-rover-vehicle-redux/)

17 Sep 2025

What can the moon buggy teach us about modeling?

[![Astronaut Jim Irwin in front of Apollo 15 and a moon rover](/images/blo...