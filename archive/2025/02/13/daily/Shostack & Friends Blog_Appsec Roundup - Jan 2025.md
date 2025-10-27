---
title: Appsec Roundup - Jan 2025
url: https://shostack.org/blog/appsec-roundup-jan-2025/
source: Shostack & Friends Blog
date: 2025-02-13
fetch_date: 2025-10-06T20:35:34.821707
---

# Appsec Roundup - Jan 2025

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
3. Appsec Roundup - Jan 2025

Shostack + Friends Blog

# Appsec Roundup - Jan 2025

An exciting month, with new threat modeling tools, cool thoughts on STAMP, bounds checking, ADRs and more!
![a photograph of a robot, sitting in a library, working on a jigsaw puzzle](/images/blog/img/2024/appsec-roundup-oct-2024-1000w.png)

What a month! It was even eventful in the appsec world, with new threat modeling tools, a self-servingly dramatic fork of semgrep, and oh, let's not talk about “regulation.” Oh, fine, lets, but only towards the end.

### Secure by Design and threat modeling

* Hendrik Ewerlin [shared](https://threatmodelingconnect.discourse.group/t/meet-threatpad/741) ThreatPad, a lightweight editor with some nice prompts . (It could use more emojis, somehow. 😉)
* [Guardio](https://dev.guardio.click/app) is another lightweight tool for recording threats.
* [Generating 1000 Threat Models Using Gemini 2.0 and AI Security Analyzer](https://xvnpw.github.io/posts/scaling-threat-modeling-with-ai/) by xvnpw. Fascinating.
* [The Evolution of SRE at Google: Using STAMP to improve resilience in Google production systems](https://www.usenix.org/publications/loginonline/evolution-sre-google) is fascinating. I think one of the advantages of rebuilding tech stacks the way Google does is that it gives you a chance to think about interfaces and the optionality they give a caller. The models that evolved for successful interactive computing have very flexible interfaces, where adding controls and ensuring they do what you want is hard.

### Appsec

* [Story-time: C++, bounds checking, performance, and compilers](https://chandlerc.blog/posts/2024/11/story-time-bounds-checking/)  by Chandler Carruth.
* [How to create Architectural Decision Records (ADRs) — and how not to](https://medium.com/olzzio/how-to-create-architectural-decision-records-adrs-and-how-not-to-93b5b4b33080) and [How to review Architectural Decision Records](https://medium.com/olzzio/how-to-review-architectural-decision-records-adrs-and-how-not-to-2707652db196), both by Doc SoC in April, 2023 but I'd missed them.
* [What’s going on with (Sem|open)grep?](https://joshcgrossman.com/2025/01/28/whats-going-on-with-sem-open-grep/) by Josh Grossman and relatedly [Opengrep - The Security Industry Deserves Better](https://crashoverride.com/blog/opengrep-the-security-industry-deserves-better?utm_content=354884849&utm_medium=social&utm_source=linkedin&hss_channel=lis-FEfOQ2e04a) by Mark Curphey.

### Regulation

* [HHS proposes major overhaul of HIPAA security rule](https://iapp.org/news/a/hhs-proposes-major-overhaul-of-hipaa-security-rule/) by Jim Dempsey gives an overview of a proposed update to regulation for hospitals.
* [Secure by Demand Priority considerations for operational technology owners and operators when selecting digital products](https://www.cyber.gov.au/resources-business-and-government/governance-and-user-education/secure-by-design/secure-demand-priority-considerations-operational-technology-owners-and-operators-when-selecting-digital-products) (I like the Australian version, in HTML.)
* The final Biden executive order on cyber is out, and this Reuters article ([As China hacking threat builds, Biden to order tougher cybersecurity standards](https://www.reuters.com/technology/cybersecurity/china-hacking-threat-builds-biden-order-tougher-cybersecurity-standards-2025-01-10/)) gives some good context: “Biden's proposal calls for tougher standards for secure software development, the ability to verify that those standards have been met, and a process for the Cybersecurity and Infrastructure Security Agency (CISA) to evaluate the process, according to the draft.” And while that’s a lot of process, it reflects a growing perception that the “impose costs” team has failed to score a goal, and the “norms” people have been hoisted on their own peTAOrd.

As of this writing on Feb 3, neither seems to be cancelled, and Joe Menn [reports](https://www.washingtonpost.com/technology/2025/02/03/cisa-china-trump-noem-hacking-cyberthreats/) that the cybersecurity one may not be.

### Books

I’m enjoying [Medical Device Cybersecurity for Engineers and Manufacturers, Second Edition](https://amzn.to/3PUwWcD) by Axel Wirth, Christopher Gates and Jason Smith. I expect to write up a fuller review, but it’s an excellent broad overview. Wish I’d had it when I started collaborating with the FDA.

### Shostack + Associates updates

* We delivered a new mini-course overlay, “Facilitating Effective Threat Modeling” for a longtime customer. The course helps experienced threat modelers add nuance to their practice as they support their teams.
* My paper, [Who are we: Power Centers in Threat Modeling](https://shostack.org/blog/who-are-we/) was accepted for [Rossfest](https://www.cl.cam.ac.uk/events/rossfest/).
* Our Quad paper, [Lessons for Cybersecurity from the American Public Health System](https://shostack.org/blog/lessons-for-cyber-from-the-public-health-system/) was released by the Computing Research Association.
* The final version of [Handling Pandemic-Scale Cyber Threats: Lessons from COVID-19](https://doi.org/10.1145/3703465.3703466 "Handling Pandemic-Scale Cyber Threats: Lessons from COVID-19") was added to the ACM library.
* At RSA, Adam and Tanya Janca will be presenting “Red Teaming AI: 50 Years of Failure, But This Time, For Sure!” (May 1, 10:50 AM).

Image by Midjourney: “a photograph of a robot, sitting in a library, working on a jigsaw puzzle”

Originally published by Adam on 12 Feb 2025

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

### [Secure By Design roundup - September 2025](/blog/appsec-roundup-s...