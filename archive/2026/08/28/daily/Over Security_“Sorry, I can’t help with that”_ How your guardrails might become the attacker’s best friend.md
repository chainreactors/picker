---
title: “Sorry, I can’t help with that”: How your guardrails might become the attacker’s best friend
url: https://blog.talosintelligence.com/sorry-i-cant-help-with-that-how-your-guardrails-might-become-the-attackers-best-friend/
source: Over Security
date: 2026-08-28
fetch_date: 2026-08-29T08:32:57.820861
---

# “Sorry, I can’t help with that”: How your guardrails might become the attacker’s best friend

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

# “Sorry, I can’t help with that”: How your guardrails might become the attacker’s best friend

By
[David J. Bianco](https://blog.talosintelligence.com/author/david-j-bianco/)

Thursday, August 27, 2026 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

Hello, everyone. Long time reader, first time writer here at the Threat Source newsletter! I wanted to start out by introducing myself. My colleague and friend Mick Baccio set the bar pretty high [last week](https://blog.talosintelligence.com/is-cyber-missing-the-marque/), so I was planning to tell you all about myself, including:

* How I did my first real IR under the influence of *The Cuckoo’s Egg* while an undergraduate (and failed)
* My pre-bug bounty flirtation with vulnerability research, including an arbitrary file overwrite in biff(1) and how I once hacked MIT’s website
* My first ever hands-on experience with a computer, the display demo Commodore 64 at the Montgomery Ward

Unfortunately, my *editor* says we don’t have the “space” for that, the MIT thing might open me up to “liability,” and it’s not the kind of “professional image” we strive for here at Talos. (I'm watching. Always watching. -Amy)

So instead, I’ll just play it safe and say that I’ve been in the security field for a little over 30 years now, mostly concentrating on the defensive side (Go, Team Blue!). I’ve helped set up SOCs, run threat hunting teams, and even published a [few things](https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html) you might have [heard of](https://www.splunk.com/en_us/blog/security/peak-threat-hunting-framework.html).

Speaking of things I’ve published, I’ve written before about the [Attacker’s Dilemma](https://techcrunch.com/2023/02/07/cybersecurity-teams-beware-the-defenders-dilemma-is-a-lie/). The idea that defenders have inherent advantages over attackers runs contrary to what most of us have heard throughout our careers. An attacker must evade monitoring and technical controls at every step of their attack lifecycle, because the defender only needs to notice *once* in order to respond and prevent them from achieving their goal. This is one of the most important advantages of any security team has, but we are currently witnessing a self-imposed erosion of this advantage through the rise of poorly-designed AI guardrails.

I’m not opposed to guardrails, but we have to carefully consider what we’re guarding against and where we deploy them. As I explored in a recent piece on [The Safety Penalty](https://blog.talosintelligence.com/the-safety-penalty-reclaiming-operational-sovereignty-in-the-age-of-ai/), by allowing third-party AI providers to implement and control safety filters and the policies behind them, we may in fact be helping the attacker. If agentic SOC process experience refusals, it can slow or even halt investigations. Of course, these should get flagged for human intervention, but that takes time and may give the attacker breathing room in which to complete their mission.

It may turn out that the *where* of the guardrails is even more important than the *what*. Operational sovereignty relies on having control of our own limits. Any vision of an agentic SOC must allow the security teams to customize the guardrails according to their own threat model. They should also have the flexibility to temporarily remove specific safeguards under authorized circumstances, something you won’t get with guardrails from a frontier provider. These controls belong inside your organization’s agentic harness where you can set the policies and technical controls to allow you to analyze threats while ensuring your agents stay within their lanes.

Ultimately, operational sovereignty means engaging with the reality of the threat landscape, ensuring that the adversary can’t derail the defender’s investigation and response processes, either accidentally or intentionally. We need to move toward a model where each organization can choose the guardrails that work for them, rather than having inflexible guardrails chosen for them.

## The one big thing

Cisco Talos recently [evaluated 66 large language model (LLM) and reasoning combinations](https://blog.talosintelligence.com/choose-your-fighter-balancing-competing-requirements-to-select-models-for-your-ai-soc/) to see if we could find a clear winner for security operations. Instead, we found that selecting the right model is a complex balancing act between efficacy, speed, cost, and consistency. Cranking up a model's reasoning effort doesn't guarantee better analysis and can actually degrade performance. Ultimately, we developed a repeatable methodology to help organizations navigate these tradeoffs for their own workflows.

### Why do I care?

Choosing an AI model based solely on generic leaderboard scores is a recipe for operational disaster. An exceptionally smart model might cost a fortune, take half an hour to analyze a single log, or completely fail to format its output. Assuming more compute power equals better results is a costly trap, as higher reasoning settings sometimes produce weaker or blocked responses. Defenders must remember that prompts, analyst personas, and model consistency drastically alter an investigation's outcome.

### So now what?

Test models against your organization’s specific workflows before deploying them. Build a focused set of representative cases and test them multiple times using the exact prompts and tools your analysts will actually use. Track the quality, cost, time, consistency, and usable-answer rates in a simple spreadsheet to expose the real-world tradeoffs. Finally, establish acceptable thresholds for these variables to eliminate underperforming models, and regularly revisit your dec...