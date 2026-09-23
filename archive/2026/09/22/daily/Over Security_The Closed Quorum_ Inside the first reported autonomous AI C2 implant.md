---
title: The Closed Quorum: Inside the first reported autonomous AI C2 implant
url: https://blog.talosintelligence.com/the-closed-quorum-inside-the-first-reported-autonomous-ai-c2-implant/
source: Over Security
date: 2026-09-22
fetch_date: 2026-09-23T06:54:43.494058
---

# The Closed Quorum: Inside the first reported autonomous AI C2 implant

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

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/09/closed-quorum-header.jpg)

# The Closed Quorum: Inside the first reported autonomous AI C2 implant

By
[Ryan Fetterman](https://blog.talosintelligence.com/author/ryan-fetterman/)

Tuesday, September 22, 2026 06:00

[AI](/category/ai/)
[Threat Spotlight](/category/threat-spotlight/)

* CLOSEDQUORUM, a malware binary discovered through Cisco Talos’ [CAIRN project](https://blog.talosintelligence.com/introducing-cairn-frontier-tracking-for-ai-integrated-malware), exhibits fully autonomous command and control (C2). While we do not have confirmation of in-the-wild deployment, artifacts from the binary were used to connect the developer to postings on criminal forums related to carding, dating back to 2025.
* This malware is a useful reference example of how attackers can collapse the decision space of a particular attack phase into a constrained set of choices, allowing AI models to provide reasoning and act independently.
* CLOSEDQUORUM represents a shift in effort displacement for attackers, in which expanding portions of the attack chain can be executed without operator involvement.

AI’s impact on offensive cyber operations has thus far mainly focused on two dimensions: *speed* and *scale*. Attackers can generate phishing lures faster and produce more malicious code variants with less effort. These are real effects, visible in the proliferation of AI-generated coding samples and agent-assisted intrusions that have become common in the past few years. But in each case, the human operator remains present: directing the tooling, selecting targets, and guiding the execution. AI makes the operator faster and more productive but does not remove them from the operation.

A third dimension has received less attention in the malware space: effort displacement. This is not merely augmenting what an operator can accomplish in a session but transferring an entire phase of the attack from the operator to the system. Effort displacement compounds the effects of speed and scale because the human-in-the-loop is no longer the bottleneck. Human operators are bound by attention, working hours, and cognitive load. An AI system capable of executing a phase of the attack chain can continue when the operator is no longer watching. It does not go offline when the attacker sleeps.

Today Cisco Talos released [CAIRN](https://blog.talosintelligence.com/introducing-cairn-frontier-tracking-for-ai-integrated-malware), our [open-source research toolkit](https://github.com/Cisco-Talos/Cognitive-Artifact-Intelligence-Research-Network) for tracking AI-integrated malware. This is the first in a series of posts sharing what we've found. While the threat class of CAIRN findings may span from experimental proof-of-concept to sophisticated active campaigns, the nature of the threat is aside from the focus: actively studying this frontier provides actionable insights to offset how threat actors are operationalizing AI.

## Introducing CLOSEDQUORUM

CLOSEDQUORUM is, to our knowledge, the first publicly documented Windows implant to apply this model to tactical command and control (C2). After deployment, it delegates the selection of its next action to a panel of commercial large language models (LLMs) and executes the resulting decision, with the intent of harvesting user credentials and crypto wallets. It does not require continued commands from a human operator or tasking from a dedicated, attacker-operated C2 server; the complete dynamic operation is delegated to the AI.

The name reflects the architecture. A quorum is a decision-making body that requires some minimum of participants to act. CLOSEDQUORUM's quorum is up to four LLM providers: DeepSeek, Qwen, Mistral, and Google Gemini. The session is closed; no humans are admitted. Four models are queried in sequence, their independent verdicts tallied, and the binary acts, based on their judgment.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/09/Artboard-24-copy-4.jpg)

Figure 1. CLOSEDQUORUM architecture.

The CLOSEDQUORUM C2 architecture supports up to four LLM provider integrations. Each active model votes on the next action, and the action receiving the most votes is selected.

Our static analysis confirms the full details of the autonomous decision loop, and development builds demonstrate build-time injection of provider credentials. The public distribution build, however, contains placeholder API keys and a dummy webhook, so we did not observe a complete end-to-end execution of the architecture.

Further details of this post document how CLOSEDQUORUM works, what it can do, and what it means for the future of autonomous offensive AI tooling.

## “LLM-as-C2" architecture

CLOSEDQUORUM is a 16.4MB, 64-bit Windows executable compiled in Go. It contains a range of offensive implant functionality, but that isn’t what makes it unique. The foundational design choice in CLOSEDQUORUM is the treatment of LLM providers as the C2 infrastructure.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/09/importsignificance.png)

Figure 2. Ghidra import results summary. `CGO_ENABLED=1` confirms the binary mixes Go and C code, which is how it makes direct Windows system calls.

Traditional C2 architecture requires the attacker to operate server infrastructure: a domain, an IP, a protocol, and a listener. That infrastructure is attributable, blockable, and expensive to rotate. Defenders track C2 domains. Threat intelligence feeds publish C2 IPs. Certificate transparency logs expose new C2 infrastructure before it's used. Instead of a singular, unique C2 server, CLOSEDQUORUM calls up to four commercial LLM provider endpoints used by thousands of legitimate applica...