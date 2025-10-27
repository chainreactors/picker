---
title: Subverting AIOps Systems Through Poisoned Input Data
url: https://www.schneier.com/blog/archives/2025/08/subverting-aiops-systems-through-poisoned-input-data.html
source: Schneier on Security
date: 2025-08-21
fetch_date: 2025-10-07T00:50:13.394605
---

# Subverting AIOps Systems Through Poisoned Input Data

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Subverting AIOps Systems Through Poisoned Input Data

In this input integrity attack against an AI system, researchers were able to [fool](https://www.theregister.com/2025/08/12/ai_models_can_be_tricked) AIOps tools:

> AIOps refers to the use of LLM-based agents to gather and analyze application telemetry, including system logs, performance metrics, traces, and alerts, to detect problems and then suggest or carry out corrective actions. The likes of [Cisco](https://www.theregister.com/2025/06/10/cisco_live_cloud_control_news/) have deployed AIops in a conversational interface that admins can use to prompt for information about system performance. Some AIOps tools can respond to such queries by automatically implementing fixes, or suggesting scripts that can address issues.
>
> These agents, however, can be tricked by bogus analytics data into taking harmful remedial actions, including downgrading an installed package to a vulnerable version.

The paper: “[When AIOps Become “AI Oops”: Subverting LLM-driven IT Operations via Telemetry Manipulation](https://arxiv.org/abs/2508.06394)“:

> **Abstract:** AI for IT Operations (AIOps) is transforming how organizations manage complex software systems by automating anomaly detection, incident diagnosis, and remediation. Modern AIOps solutions increasingly rely on autonomous LLM-based agents to interpret telemetry data and take corrective actions with minimal human intervention, promising faster response times and operational cost savings.
>
> In this work, we perform the first security analysis of AIOps solutions, showing that, once again, AI-driven automation comes with a profound security cost. We demonstrate that adversaries can manipulate system telemetry to mislead AIOps agents into taking actions that compromise the integrity of the infrastructure they manage. We introduce techniques to reliably inject telemetry data using error-inducing requests that influence agent behavior through a form of adversarial reward-hacking; plausible but incorrect system error interpretations that steer the agent’s decision-making. Our attack methodology, AIOpsDoom, is fully automated—combining reconnaissance, fuzzing, and LLM-driven adversarial input generation—and operates without any prior knowledge of the target system.
>
> To counter this threat, we propose AIOpsShield, a defense mechanism that sanitizes telemetry data by exploiting its structured nature and the minimal role of user-generated content. Our experiments show that AIOpsShield reliably blocks telemetry-based attacks without affecting normal agent performance.
>
> Ultimately, this work exposes AIOps as an emerging attack vector for system compromise and underscores the urgent need for security-aware AIOps design.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/), [cyberattack](https://www.schneier.com/tag/cyberattack/), [integrity](https://www.schneier.com/tag/integrity/), [LLM](https://www.schneier.com/tag/llm/)

[Posted on August 20, 2025 at 7:02 AM](https://www.schneier.com/blog/archives/2025/08/subverting-aiops-systems-through-poisoned-input-data.html) •
[4 Comments](https://www.schneier.com/blog/archives/2025/08/subverting-aiops-systems-through-poisoned-input-data.html#comments)

### Comments

[Shashank](https://muskdeer.blogspot.com/) •
[August 20, 2025 7:34 AM](https://www.schneier.com/blog/archives/2025/08/subverting-aiops-systems-through-poisoned-input-data.html/#comment-447263)

This is an interesting lab POC but it would be more interesting to see how well this works against actual AIOps platforms (Datadog, Dynatrace, Elastic AIOps etc). The assumption that attackers can inject arbitrary telemetry into production pipelines can be faulty, telemetry generally goes through some normalization before coming of use.

David P Sanford •
[August 20, 2025 8:05 AM](https://www.schneier.com/blog/archives/2025/08/subverting-aiops-systems-through-poisoned-input-data.html/#comment-447264)

I think this is one of the many cases where we may want to use AI to design and develop the system, but the final code and system should be a deterministic finite state machine, with every state and event response accounted for. We can use AI to make systems that are not black boxes – even if the AI is. I would postulate that this may apply to any high-safety or high-security system. How to do this is a longer conversation, involving discussion of unit tests, etc.

Clive Robinson •
[August 20, 2025 12:10 PM](https://www.schneier.com/blog/archives/2025/08/subverting-aiops-systems-through-poisoned-input-data.html/#comment-447268)

@ David P Sanford,

You say,

> “…we may want to use AI to design and develop the system, but the final code and system should be a deterministic finite state machine, with every state and event response accounted for.

If you think about it that was how we were designing “fail safe” and “intrinsically safe” systems back in the 1980’s when the only “AI of use” was a combination of “fuzzy logic” and “expert systems”.

Where the basic rules were created by human “experts” as a corse matrix and “fuzzy logic” was used to fill in the gaps by reduce the resulting rule processing issues so 8bit CMOS CPUs like the 1802, 6502 and even some 8bit NMOS CPU’s like the 8080 and Z80 could do the job required within the limits of the resources available.

Embedded system engineers still use that basic process four decades later… and yes still use “Lookup tables” with interpolation to “fill the gaps”. Only the interpolation is more than “fill in by straight line” the use of fuzzy logic “hunts the line” or it’s tangent with a partial stochastic process especially if it is likely to be too complex to analyse or otherwise intractable. Thus can produce non constant but close in results that account for many of the defects that arise from simple interpolation between two points using Monte Carlo type methods. Also the resulting stochastic nature reduces certain types of wear in physical systems.

You go on to say,

> “I would postulate that this may apply to any high-safety or high-security system. How to do this is a longer conversation, involving discussion of unit tests, etc.
> “

So yes it’s already being done but not by “Current AI LLM and ML systems” nor are they likely to do so any time soon.

Because LLM systems are the equivalent of “filters” working on multidimensional spectra. And ML if used correctly with an LLM only makes the LLM filter “adaptable” to match a new set of spectra during use.

The finding of the new required filter mask happens by a simple statistical method to find patterns in existing or past data. As such the ML can not come up with new predictions thus new “unit tests” though if some already exist it can make limited stochastic changes.

Ardaw •
[August 20, 2025 9:14 PM](https://www.schneier.com/blog/archives/2025/08/su...