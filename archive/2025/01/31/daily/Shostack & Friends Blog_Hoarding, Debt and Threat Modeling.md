---
title: Hoarding, Debt and Threat Modeling
url: https://shostack.org/blog/hoarding-debt-and-threat-modeling/
source: Shostack & Friends Blog
date: 2025-01-31
fetch_date: 2025-10-06T20:10:29.372115
---

# Hoarding, Debt and Threat Modeling

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
3. Hoarding, Debt and Threat Modeling

Shostack + Friends Blog

# Hoarding, Debt and Threat Modeling

The psychology of getting started threat modeling
![An ai image of a hoarder office](/images/blog/img/2025/hoarding-debt-and-threatmodeling-1000w.png)

During a recent threat modeling course, one of our students, Aleksei\*, made a striking comparison that resonated with a lot of us: starting security analysis is like tackling a hoarder’s house. That visceral image of looking at mountains of accumulated issues, feeling overwhelmed by where to begin, captures a challenge many engineering leaders face when they first attempt to systematically assess their system’s security.

Perhaps the reason it’s evocative is most of us have been in the situation of everywhere we look, there’s more problems. Where do you begin? And that feeling of being overwhelmed, of not knowing where to start... well, again, evocative.

This is a common situation. Without security analysis techniques, we’re unlikely to design good security. (We’re actually likely to design bad security if we only consider performance, usability and exclude security.) So when we start threat modeling, we quickly find reasons to regret previous decisions.

So how can we start threat modeling when there’s all this technical debt? Some thoughts:

* **Define clean**. Maybe one person thinks a good dusting is enough; another that things need to be in containers (books on shelves, desk clutter in baskets, papers in files) and yet another thinks that without bleach, it’s a waste.
* **No new problems**. We start threat modeling by asking “what are we working on?” And that means we can set aside the global problem and look to make sure that the code we’re building today doesn’t make things worse.
* **Clean a room**. Pick a problem area, and go nuts on improving it. (This is similar to the [strangler fig pattern](https://martinfowler.com/bliki/StranglerFigApplication.html).)
* **Do a security sprint**. In the late 90s, Microsoft started having “security pushes” where all feature work was paused to improve security. The executive-visible success of these pushes was a crucial step in the issuance of the Trustworthy Computing memo. Getting all hands on deck to clean something shows its priority. This is a little different than cleaning a room: Everyone does cleaning on the areas they own.

However you want to handle the situation, acknowledging that it seem insurmountable can be important. We all have too many tasks, and those where you can’t imagine success, or where success seems not worth the price, are ones we want to skip. (This is why I included interpersonal factors in the [Jenga whitepaper](https://shostack.org/resources/whitepapers).)

The questions of “how do I get started” or “how do I take this from ‘me’ to ‘us’” are just one of the places where our team’s experience driving successful threat modeling initiatives distinguishes us.

Need help getting started? Our team has guided organizations from initial threat modeling through to mature security practices. [Reach out](https://shostack.org/contact) if you want to talk about your specific challenges.

I’ve left Aleksei’s last name out for privacy. Image by Midjourney:
“Today in one of our classes, a student compared starting to threat model to cleaning, home of a hoarder, boxes and books and stacks of paper to the cielings, hard to see evocative analogy, conversation. To one side, a 'murder board' is visible, with photographs, twine and other interconnections. On the other side is a whiteboard with a software architecture diagram”

Originally published by Adam on 30 Jan 2025

Categories:
  [threat modeling](/blog/category/threat-modeling)
  [usability](/blog/category/usability)

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

What can a signed Apollo 15 print teach us about modern threat modeling and risk management?

## Popular Blog Topics

[Threat Model Thursday](/blog/category/threat-model-thursday/),
exploring specific published threat models

[Threat Modeling](/blog/category/threat-modeling/) (general topic)

[Application Security](/blog/category/application-security/)

[Software Engineering](/blog/category/software-engineering/)

[Cloud Security](/blog/category/cloud-security/)

[Compliance](/blog/category/compliance/)

[AI](/blog/category/ai/) + [ChatGPT](/blog/category/chatgpt/)

[Privacy](/blog/category/privacy/) + [Personal Security](/blog/category/personal-security/)

[Research](/blog/category/research-papers/) + [Reports](/blog/category/reports-and-data/)

[Book Reviews](/blog/category/book-reviews/)

[News](/blog/category/news/)

[Podcasts](/blog/category/podcasts/), [Videos](/blog/category/videos/) + [Webinars](/blog/category/webinars/)

Our site works best with Javascript enabled, h...