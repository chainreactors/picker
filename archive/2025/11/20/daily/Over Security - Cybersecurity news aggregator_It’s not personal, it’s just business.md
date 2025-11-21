---
title: It’s not personal, it’s just business
url: https://blog.talosintelligence.com/its-not-personal-its-just-business/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-20
fetch_date: 2025-11-21T03:13:48.406518
---

# It’s not personal, it’s just business

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

# It’s not personal, it’s just business

By
[Martin Lee](https://blog.talosintelligence.com/author/martin-lee/)

Thursday, November 20, 2025 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

This week, we explore how advances in agentic AI are rapidly transforming the cyber crime business.

Agentic AI programming gives AI agents autonomy, allowing them to interact with external systems to collect information, make decisions with the help of a generative AI system, and then effect changes in the external environment. The activity takes place through various APIs according to the instructions provided to the agent and in the context of a defined workflow.

The advantage for human operators is that these systems can efficiently execute routine activities that would otherwise require accessing multiple systems. Essentially, the AI agent acts as a trusted assistant who is able to get on with things with minimal supervision while the human operator can focus on other things.

As this approach brings advantages to the legitimate economy, so it brings similar efficiencies to the cyber crime economy. More recently, the [publication](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf) of the discovery of the first AI-orchestrated cyber campaign should give us pause. It signals a new era for cybersecurity teams.

We’re entering a time when we can expect to see much experimentation and innovation with AI in both the legitimate and cyber crime economies. AI can act as a force enabler, making tasks easier and faster to perform. Similarly, AI can lower barriers to entry, allowing lower skilled actors to perform tasks that they lack the skills to perform. While AI does not bring new capabilities, it can make existing capabilities easier to execute. However, AI systems still require skillful instruction and supervision.

AI is not infallible, it gets things wrong, and it is prone to inventing nonsense. When it does go off the rails, a human needs to step in and resolve the situation. This is not necessarily easy to do and may prove tricky for low-skilled threat actors.

Don’t be discouraged: We can also leverage these developments to our advantage. Defensive teams can write their own agentic systems to find and fix weaknesses in their own systems before malicious actors identify them. We can deploy honeypot systems designed to be found by malicious AI systems, engage with them and tie up their resources.

The threat landscape has never been static. While AI does make some tasks more accessible to threat actors, it is a double-edged sword and also brings opportunities to defenders.

## The one big thing

Cisco Talos has [introduced new features](https://blog.talosintelligence.com/new-in-snort3-enhanced-rule-grouping-for-greater-flexibility-and-control/) for Snort3 users within Cisco Secure Firewall. A new "Severity" rule group allows you to organize detection rules by CVSS-based vulnerability severity (low, medium, high, critical). This allows teams to better prioritize and manage rules according to risk and urgency. You can also select rules based on vulnerability age (e.g., last 2, 5, or 10 years).

### Why do I care?

This update allows you greater flexibility and control. It makes it simpler to maintain consistent, targeted detection coverage, whether you’re running large, distributed networks or smaller environments with tailored security priorities.

### So now what?

Review your current Snort3 rule configurations in Cisco Secure Firewall and consider adopting the new Severity and time-based grouping features. By tailoring rule sets to your organization’s specific risk tolerance and patching cycles, you can optimize detection coverage, streamline management, and better protect your environments.

## Top security headlines of the week

**Critical** **railway** **braking** **systems** **open to** **tampering**
Researchers have figured out how to spoof the signals that tell train conductors to brake, opening the door to any number of dangerous attack scenarios. ([Dark Reading](https://www.darkreading.com/ics-ot-security/critical-railway-braking-systems-tampering))

**EchoGram** **flaw bypasses guardrails in major LLMs**
A flaw discovered in early 2025 and dubbed EchoGram allows simple, specially chosen words or code sequences to completely trick the automated defences, or guardrails, meant to keep the AI safe. ([HackRead](https://hackread.com/echogram-flaw-bypass-guardrails-major-llms/?utm_source=tldrinfosec))

**Over 67,000 fake** **npm** **packages flood registry in worm-like spam attack**
The worm-life propagation mechanism and the use of a distinctive naming scheme that relies on Indonesian names and food terms for the newly created packages have lent it the moniker IndonesianFoods Worm. The bogus packages masquerade as Next.js projects. ([The Hacker News](https://thehackernews.com/2025/11/over-46000-fake-npm-packages-flood.html?utm_source=tldrinfosec))

**Cornerstone Staffing ransomware attack leaks 120,000 resumes, claims** **Qilin** **gang**
The notorious Qilin gang posted the industry-leading recruitment agency on its dark leak blog last Thursday. The group claims to have exfiltrated 300GB of sensitive information from Cornerstone. ([Cybernews](https://cybernews.com/security/cornerstone-staffing-ransomware-attack-qilin-group-exposes-resumes/?utm_source=tldrinfosec))

**Surveillance tech provider** **Protei** **was hacked, its data stolen, and its website defaced**
It’s not clear exactly when or how Protei was hacked, but a copy of the company’s website saved on the Internet Archive’s Wayback Machine shows it was defaced on November 8 and restored soon af...