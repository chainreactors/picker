---
title: Threat Modeling Tools
url: https://shostack.org/blog/threat-modeling-tools/
source: Shostack & Friends Blog
date: 2025-08-26
fetch_date: 2025-10-07T00:48:32.972922
---

# Threat Modeling Tools

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
3. Threat Modeling Tools

Shostack + Friends Blog

# Threat Modeling Tools

A 2025 view of threat modeling tools
![a photograph of a robot standing at a whiteboard, trying to explain a crazy complicated diagram to a group of people seated around a conference table.](/images/blog/img/2025/threat-modeling-tools-1000w.png)

People frequently ask me what threat modeling tooling they should use. My answer is always: The best threat modeling tool for you is the one that solves a specific problem that you can articulate. To help you articulate the problems, this is one part of a two-part series. The second post will dive deep into LLMs for threat modeling.

Threat modeling tools generally fall into four groups:

* General purpose tools like whiteboards or Google docs
* Programmer threat modeling tools tools (eg, [pytm](https://github.com/OWASP/pytm))
* Individual/small team threat modeling tools (eg, [MS-TMT](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool) or [Threat Dragon](https://owasp.org/www-project-threat-dragon/))
* Enterprise threat modeling tools (eg, [IriusRisk](https://www.iriusrisk.com/))

This model foreshadows how LLMs fit in. (Spoiler: Any of these can add an LLM, which limits the value we get from talking about “AI supported threat modeling,” and which is why it’s helpful to start with this model of types of tools.)

Any threat modeling project or program has tools, even if they’re not specialized. Editors, drawing tools and more get picked because they’re familiar, integrated into workflows, and often insufficient because they don’t do things that you hope they’d do, like analyze your diagram. But from whiteboards to Word to Miro, your existing tools can take you a long way — and leave you wanting more.

As we consider threat modeling specific tooling, we should consider who’ll use it. “Scaling” is a common goal, and usually involves more people threat modeling. Considering their learning curve and other elements of adoption can help us to think about what can go wrong and what we’re going to do about those things. Familiarity is valuable, but not the only value. It’s one of the things that keeps companies running on Excel long past the time when they should replace it.

I often use the metaphor of Excel versus SAP or Oracle Financials to illustrate the relationship between Microsoft’s TMT and IriusRisk. Microsoft TMT is the Excel in this metaphor. You can manage files and otherwise make it work as you grow, but it's not an enterprise tool with permissions, change management, approvals, project status, et cetera. There’s a tremendous amount of error-prone busywork in trying to scale Excel to running a business.

When people talk about LLMs to help threat modeling, there’s a few ways they might be working with them. Those are:

1. Standard chatbots
2. Standard chatbots with structured prompts, used manually
3. Security chatbots ([Deep Hat](https://www.deephat.ai/) (Formerly Whiterabbit), StrideGPT)
4. Security chatbots, structured prompts
5. One time investment in RAG (etc) to provide structure
6. Ongoing product development effort

LLM support for threat modeling can fit into any of the tool types above (programmer, small team, or enterprise) or work in the general purpose tools. I don’t really want an LLM-enabled whiteboard, but here we are.

Scaling is a very common goal for tooling. If you’re thinking carefully about what I’m saying, you’ll see I’ve outlined at least two scaling challenges that tools can help address. The first is “more people threat modeling,” the second is “managing the process and outputs.” Being even more specific, more people threat modeling may involve help in creating diagrams, analyzing what can go wrong, or selecting or implementing mitigations. Being precise will make it easier to reach a goal and see that you’re reaching it.

I’ll walk through some of the tradeoffs for LLMs in another post, now live at [Mansplaining your threat model, as a service](https://shostack.org/blog/mansplaining-your-threat-model-as-a-service/).

Midjourney: a photograph of a robot standing at a whiteboard, trying to explain a crazy complicated diagram to a group of people seated around a conference table. On the conference table are old fashioned brass and glass scientific tools. the people at the table are bored:3 and skeptical:2. --ar 8:3 --v 6.1

Originally published by Adam on 25 Aug 2025

Categories:
  [threat modeling](/blog/category/threat-modeling)

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

[Threat Modeling](/blog/...