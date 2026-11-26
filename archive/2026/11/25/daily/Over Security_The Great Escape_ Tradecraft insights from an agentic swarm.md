---
title: The Great Escape: Tradecraft insights from an agentic swarm
url: https://blog.talosintelligence.com/the-great-escape-tradecraft-insights-from-an-agentic-swarm/
source: Over Security
date: 2026-11-25
fetch_date: 2026-11-26T10:14:48.968440
---

# The Great Escape: Tradecraft insights from an agentic swarm

[Blog](/)

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/11/swarm-header.jpg)

# The Great Escape: Tradecraft insights from an agentic swarm

By
[Ryan Fetterman](https://blog.talosintelligence.com/author/ryan-fetterman/)

Wednesday, November 25, 2026 06:00

[On The Radar](/category/on-the-radar/)

* The OpenAI-linked swarm activity in 2026 is fully traceable through public records and offers an unprecedented view into how multi-agent AI systems operate and coordinate at scale.
* Distilling and documenting the swarm tradecraft may help defenders understand multi-agent operations and communication, and how agents adapt when a path is  blocked.
* Some documented behaviors may transfer to more purpose-built cyber attack frameworks like ARTEX, including methods to persistently store results, the burst-and-pause timing patterns of reasoning loops, and the self-labeling conventions that can reveal workload assignments and distribution.

---

Beginning in June 2026 and extending for several months, a collection of OpenAI models conducting internal training and evaluation tasks broke out of their containerized environments and accessed websites and databases via the public internet in ways [the company says it did not authorize](https://openai.com/index/how-we-will-do-better-for-australia/).

This activity represents a new kind of cyber event: not a malicious intrusion, but an unintentional series of consequences stemming from an agentic *swarm*, a group of AI agents exhibiting coordinated behavior toward a shared objective. A swarm implies many agents but doesn’t have a rigid count. The main distinction is behavioral; the collective activity of a swarm becomes complex and unpredictable even when individual agents may be explainable. This swarm provided an initial, public glimpse into the behavior and coordination of autonomous, multi-agent operations.

Due to constraints in their evaluation environment, the OpenAI swarm used public internet services as improvised infrastructure, which made the activity visible and traceable. The behaviors exposed revealed methods for persistent probing, iterative payload development, work partitioning and coordination across agents, and adaptation to execution constraints, in ways that are likely to be relevant for understanding agent behavior beyond this just case.

Agentic cyber attack frameworks are [now appearing in intrusion activity](https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks/?utm_source=chatgpt.com), with the ability to support [scaling to multi-agent operations](https://www.trendaisecurity.com/en-us/resources-insights/deep-research/not-only-artex-the-different-levels-ai-is-used-in-attacks-targeting-japan). These attacker swarms largely replace the use of public internet resources with purpose-built infrastructure that removes some of the artifacts visible. However, documenting our understanding of operational swarm techniques can give defenders a baseline for recognizing behaviors as they move into new environments and contexts. In some cases, we can already see the evidence where these techniques *do* transfer.

In this post, we’ll explore and document the tradecraft of the escaped OpenAI swarm and conclude by comparing it to early signals and behaviors from the current agentic attack activity seen in the wild.

## Background

Swarms are an important concept to track because they can divide work across parallel agents, potentially completing complex tasks faster, though the gains depend on the task and the quality of coordination. Parallel agent coordination was crucial to OpenAI’s ability to [solve the Navier-Stokes Millenium Prize Problem,](https://openai.com/index/navier-stokes-solution/) which arrived at a winning solution with a group on the order of 10,000 concurrent agents over the course of 88 hours.

Early evidence suggests swarms transfer effectively to cyber attack problems. The main factors for swarm efficiency are how parallelizable the tasking is, and if the attackers want to pay the inflated token cost. A rough example is using four agents on the same problem, to get it done twice as fast; as Noam Brown of OpenAI said on a [Dwarkesh podcast](https://www.dwarkesh.com/p/noam-brown), “Because there are four agents working for half as long, you’re paying 2x more to get an answer twice as quickly.”

AI models undergoing training and evaluation operate inside sandboxed computing environments. These are controlled workspaces where they can write and run code, search for information, and iterate toward solutions. These environments are designed to be both enabling and constraining. They give models room to practice, while limiting what they can reach and do, so that mistakes or misaligned behavior stay contained.

## Operating under constraint

While the techniques employed by the OpenAI swarm may have crossed the thresholds of intended use, they should not be viewed as malicious intent. A useful framing for understanding these techniques is creativity under constraint. The agents were optimized to meet their objectives, and they displayed considerable persistence and ingenuity to that end.

The constraints the agents were working around were layered and understanding them helps explain the motivation behind every technique. The most fundamental was the absence of a browser runtime: Agents operating in text and code environments cannot natively load JavaScript-heavy pages, call browser APIs, or interact with dynamic web content. The creative solution was submitting URLs to a public scanner like “urlquery.net” which provided a real Chromium instance on demand.

This workaround by itself, however, was still not enough. Browsers apply a security rule called the same-origin policy: JavaScript running on o...