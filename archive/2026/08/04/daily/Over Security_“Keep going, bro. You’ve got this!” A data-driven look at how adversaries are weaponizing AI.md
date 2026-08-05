---
title: “Keep going, bro. You’ve got this!” A data-driven look at how adversaries are weaponizing AI
url: https://blog.talosintelligence.com/keep-going-bro-youve-got-this-a-data-driven-look-at-how-adversaries-are-weaponizing-ai/
source: Over Security
date: 2026-08-04
fetch_date: 2026-08-05T04:59:59.061446
---

# “Keep going, bro. You’ve got this!” A data-driven look at how adversaries are weaponizing AI

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

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/07/aiartifactheader.jpg)

# “Keep going, bro. You’ve got this!” A data-driven look at how adversaries are weaponizing AI

By
[Nick Biasini](https://blog.talosintelligence.com/author/nick-biasini/),
[Dmytro Korzhevin](https://blog.talosintelligence.com/author/dmytro/),
[Jaeson Schultz](https://blog.talosintelligence.com/author/jaeson-schultz/),
[Vanja Svajcer](https://blog.talosintelligence.com/author/vanja-svajcer/),
[Vitor Ventura](https://blog.talosintelligence.com/author/vitor-ventura/),
[Arnaud Zobec](https://blog.talosintelligence.com/author/arnaud/)

Tuesday, August 4, 2026 06:00

[AI](/category/ai/)
[Threat Spotlight](/category/threat-spotlight/)
[Threats](/category/threats/)

* Actor usage of AI is exploding. By analyzing artifacts left behind, Talos has created a detailed analysis of how we are seeing adversaries leverage the technology to include development, force multiplication, and vulnerability research.
* Based on the evidence Talos gathered, guardrails did not provide much protection, with most actors able to convince the models to comply despite the lack of sophisticated techniques or encoding.
* The pre-existing skill of the actor has a large impact on what they can accomplish with AI. Talos observed novice users able to create malicious capabilities, albeit with limited capabilities and success. Advanced users were able to build astonishing capabilities, pushing the models to create sophisticated and complex outputs.

---

Artificial intelligence (AI) and associated language models are now ubiquitous and heavily used in both personal and professional contexts to streamline tasks and expand capabilities. With AI being used everywhere and by almost everyone, one of the biggest questions is how malicious actors are taking advantage. Fortunately, actors make mistakes and chatbots leave artifacts.

Leveraging cloud-based AI models leaves behind a variety of artifacts, most notably a prompt log. These logs can take on a variety of shapes and sizes, but they are left on endpoints that are running various applications, such as Claude Code, CodeX, Cursor, or Gemini.

Over the course of our research, we’ve collected a significant corpus of these files and can start discussing the ways we see bad actors leveraging these technologies. In conducting the research, three categories of activity emerged. One was using AI as a malicious software engineer, leveraging AI to write (in some cases) very sophisticated code with clear malicious intentions. Another was actors leveraging AI to scale criminal operations and campaigns. Finally, there were a lot of actors leveraging it for bug bounty or vulnerability research, rapidly accelerating their capabilities of discovery and disclosure.

Each category demonstrates how threat actors are currently leveraging AI. Within each category is a wide disparity in sophistication based on the knowledge level of the actors involved. We tried to include use cases to cover the breadth of what we found.

## Takeaways and high-level findings

With the recent disclosures from [Hugging Face](https://huggingface.co/blog/security-incident-july-2026) and [OpenAI](https://openai.com/index/hugging-face-model-evaluation-security-incident/), it's clear the era of agentic attackers has effectively arrived. In that incident, the models were operating inside a sanctioned evaluation with safeguards deliberately relaxed — but they autonomously escaped their sandbox, found and chained real vulnerabilities, and compromised production infrastructure to reach their objective. The capabilities exist; the only missing ingredient is malicious intent, and it's a matter of time before threat actors supply it. For defenders, this is a wake-up call: Vulnerabilities will surface faster, exploitation will happen sooner, and the actors behind it won't need rest or downtime. As the case studies below show, the central challenge for guardrails right now is supporting legitimate dual-use work — red teaming and vulnerability research — without empowering malicious actors.

One of the immediate takeaways is that guardrails are not functioning as expected. We did not encounter any sophisticated encoding or techniques designed to trick the models — most of the time it was a simple “I'm allowed to do this,” and the model complied. When guardrails did engage, they accomplished little. In one instance, we watched an actor abandon a censored model and pivot to an uncensored version, which completed the task without question. In another, a model pushed back on a distributed denial-of-service (DDoS) operator, but by that point the tooling had already been built. This wasn't specific to a single model or platform; it was across the board.

The other big takeaway is that an actor's skill level largely determines how effectively AI can be leveraged and how much impact it ultimately has. Unsophisticated actors can use AI to cobble together malicious projects that technically work, but lacking the expertise to push the tools further, they end up with substandard results — limited functionality and little ability to update or improve what they've built. By contrast, sophisticated actors have pushed the bounds of what we thought possible: building highly effective platforms for compromise or assembling pipelines of zero-days to disclose or sell depending on their intentions. In their hands, AI is a true force multiplier.

From an enterprise perspective, organizations need to understand that threat actors are heavily leveraging AI capabilities in their pipelines, and defenders need to do the same. The organizations best equipped to handle the coming deluge of additional vulnerabilities, alerts, and incidents will be the ones that prepare now. Agents are going to become ...