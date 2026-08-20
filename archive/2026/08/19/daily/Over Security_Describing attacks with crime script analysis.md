---
title: Describing attacks with crime script analysis
url: https://blog.talosintelligence.com/describing-attacks-with-crime-script-analysis/
source: Over Security
date: 2026-08-19
fetch_date: 2026-08-20T02:56:44.348062
---

# Describing attacks with crime script analysis

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

# Describing attacks with crime script analysis

By
[Martin Lee](https://blog.talosintelligence.com/author/martin-lee/)

Wednesday, August 19, 2026 06:00

[On The Radar](https://blog.talosintelligence.com/category/on-the-radar/)

* Crime script analysis is a narrative-driven technique that can be used alongside, or as an alternative to, tactics, techniques, and procedures (TTPs) — creating human-readable stories that describe attacks in a way non-technical audiences can understand.
* By analyzing the attacker’s workflow, we can identify how AI can be used to industrialize attacks. Through considering a business email compromise (BEC) example, we demonstrate how attackers may scale the attack to target previously unprofitable victims.
* Deconstructing an attack into discrete steps allows defenders to pinpoint intervention points where defenses can be effectively deployed, or where strategic disruption can break the script and thwart the threat actor's operation.

---

Effective defense against cyber attacks requires understanding how attacks are carried out and identifying where the attack can be disrupted or detected.

Lockheed Martin’s Cyber Kill Chain was one of the earliest models to describe the steps required to conduct a cyber attack. However, its seven-step linear sequence is too rigid to apply to many attacks.

The Attack Flow model of the MITRE ATT&CK framework allows various tactics, techniques, and procedures (TTPs) to be chained together to describe exactly how attacks are conducted, including branches and loops if necessary. The resulting graphs are comprehensive, but can be daunting to a non-technical audience. In a world of evolving threats and shrinking budgets, defenders need techniques to communicate threats to a wider audience.

Crime script analysis (CSA) is a technique originally developed in the mid-1990s as a criminology tool to understand how crimes are committed. CSA allows us to decompose an attack into a sequence of actions, decisions, and situational requirements. Describing an attack as a narrative using everyday language not only makes the description accessible to non-technical audiences, but also to identify "choke points" where the crime can be disrupted.

If MITRE ATT&CK TTPs describe the building blocks that comprise an attack, Attack Flow diagrams are the structural engineering blueprints showing how the blocks fit together, and CSA is the architect’s artistic impression of the finished building. Each component has their place in providing a picture of what is happening at different levels of abstraction for different audiences.

## Business email compromise as a case study

The business email compromise (BEC) is a common scam. Someone with financial authority receives a message purporting to be from a superior in the same organization requesting an urgent payment. If the victim is fooled, payment is released to the scammer, who acts quickly to launder the money to disguise its origin before the scam is uncovered.

[In April](https://blog.talosintelligence.com/the-democratisation-of-business-email-compromise-fraud/) I wrote about such an attack against a small, community sports club of which I am a member. The sum requested in the attack wasn’t large, so the reason was plausible. However, the tone of the email wasn’t quite correct. The treasurer’s suspicions were raised and the attempted fraud uncovered.

This incident was particularly interesting because of the small scale of the attack. Historically, the research necessary to conduct the attack — the identification of the target victim, the person spoofed, the nature of the social engineering lure — has limited its scalability. Carrying out these tasks manually takes time and has meant that it has typically been conducted against larger businesses.

The advent of AI means that the previously time-consuming preparative work can be automated. Expressing the attack as a crime script helps us understand where AI may assist the attacker and how the attack could be disrupted.

## Putting BEC in the crime script narrative

We can imagine the crime script for the attack as follows:

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/08/BECCrimeScript.jpg)

Figure 1. A general BEC crime script.

Steps 1 – 4 are time consuming to perform manually, but can be automated with AI. This efficiency improvement allows an attacker to identify many targets and shifts the execution of the attack from a higher value fraud against a few targets to a lower value fraud against many targets.

The personalization of the social engineering in Step 5 can also be conducted using AI. The attacker can generate urgent requests for payment that are relevant to the target organization and may appear credible to the victim.

## Identifying intervention points

Considering the narrative of the attack helps with reflection on how the attack might be disrupted. Clearly, Steps 1 – 4 can be disrupted by seeding AI with fake canary organizations. These are fictitious honeypot entities that have public personas discoverable by AI agents, but otherwise serve no purpose. The source of messages sent to honeypot organizations can then be blocked, disrupting Step 6.

Interactions with large language models (LLMs) leave traces that can be identified by security teams. While distinguishing malicious prompts from legitimate business inquiries is difficult, there is potential for AI providers to detect repeated patterns of reconnaissance and the generation of social engineering messages. This leaves Step 5 vulnerable to disruption by providers of AI systems.

The most effective disruption point remains Step 6, the delivery mechanism. Anomalous account behavior or high volumes of outgoing mail from a single source should trigger immediate rate-limiting or reputation...