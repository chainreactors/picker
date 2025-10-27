---
title: CVE Futures
url: https://shostack.org/blog/cve-futures/
source: Shostack & Friends Blog
date: 2025-04-25
fetch_date: 2025-10-06T22:05:52.775836
---

# CVE Futures

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
3. CVE Futures

Shostack + Friends Blog

# CVE Futures

What’s next for the CVE program?
![The cve logo](/images/blog/img/2025/cve2-416w.jpeg)

Since [last week’s CVE budget kerfuffle](https://shostack.org/blog/thoughts-on-cve/), I’ve been drawn into many conversations about “what comes next?” And while I want to say that I don’t know and I haven’t been involved in too long, it turns out I have a perspective that I keep sharing. To summarize: Decide what problem you’re solving.

Since I wrote my post, CISA has made a [strong statement](https://www.cisa.gov/news-events/news/statement-matt-hartman-cve-program):

> To set the record straight, there was no funding issue, but rather a contract administration issue that was resolved prior to a contract lapse. There has been no interruption to the CVE program and CISA is fully committed to sustaining and improving this critical cyber infrastructure.

That mirrors what I was told and put in my April 17 update to my [prior post](https://shostack.org/blog/thoughts-on-cve/). This morning, Jen Easterly weighed in with a long post on Linkedin, [Trust, Transparency, & the Future of the CVE Program](https://www.linkedin.com/pulse/trust-transparency-future-cve-program-jen-easterly-vcs9e/).

I’m glad that we’re talking about how to strenthen and improve the program. To start, what is CVE?

### First and foremost, CVE is a naming system

Naming is a hard problem. To me, the core value CVE provides is a way to cross-reference between databases and tools. I remember when, shortly after the launch of CVE, a vendor launched their own ID system. I think it was bugtraq IDs. I was annoyed. Why would they not use CVE? I’ve learned that each institution wants an identifier that works for them, much like we have ISBNs and UPC codes on books. One serves authors, the other retailers. Bugtraq needed to issue a permanent identifier when things went in their database, and then have that included in the CVE entry. It was the right choice.

A huge reason that CVE has been valuable is the focus on simplicity, and the rejection (or deflection) of requests to do more. The simplicity of the system allows others to layer on things like CVSS, to the point where people conflate and refer to CVE scores. Adding enrichment doesn’t require coordination with CVE, it requires an RSS feed from them.

CVEs are generally public, and the faster CVEs are public, the more useful they are. Generally, CVEs don’t have enough data to point to an 0day. There’s a lot of people who think that more opacity will serve the program, and I disagree. CVE ran very publicly, with the mail archives being public, and that’s to everyone’s benefit, even with the kerfuffle.

### What problem do you want to solve?

A lot of the folks who are asking what comes next lack clarity on what they want to do. That’s fine, but it’s also the first thing to settle. When I talk about why we start threat modeling with the question “what are we working on,” I often say that if I come into a room and people can’t answer that question, we can’t do a lot of threat modeling. As we start to answer it, we can get into the question of “what can go wrong?”

If funding is the thing you want to settle, Jen Easterly lays out an important argument, which is that naming is likely a public good. She points out the conflict of interest in letting companies control that, and I’ll add — companies are incredibly opposed to even *breach* disclosure laws, admitting when they’ve been vicitmized. She’s right that letting them control vuln naming...while, there’s an obvious answer to what can go wrong.

There’s a bit of an elephant in the room when the former director of the Cyber Security and Infrastructure Security Agency of *The United States* talks about *the* public good. Perhaps other countries feel that the US view of the public good excludes their public, or that the English-centered nature of CVE should be corrected, or that the US government is now less focused on public good than it has been.

Those concerns are unlikely to be raised in tweets or blog posts, but that doesn’t obviate them. My perspective is that MITRE has the organizational maturity to handle them, and alternate hosts who would do better are ... rare.

If you want to improve the CVE, the first step is identifying the problem. If the problem is funding, I believe that MITRE’s Center for Threat Informed Defense is standing by for donations.

If the problem is something else, start by explaining what it is.

Originally published by Adam on 24 Apr 2025

Categories:
  [books](/blog/category/books)
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

[![Astronaut Jim Irwin in front of Apollo 15 and a moon rover](/images/blog/img/2025/as15-88-11866-signed-175w.jpeg)](/blog/apollo-15-lrv-boeing/)

### [Apollo 15 Lunar Rover Vehicle](/blog/apollo-15-lrv-boeing/)

15 Sep 2025

What can a signed Apollo 15 print teach u...