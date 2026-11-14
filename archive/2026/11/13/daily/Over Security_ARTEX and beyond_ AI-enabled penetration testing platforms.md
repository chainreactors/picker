---
title: ARTEX and beyond: AI-enabled penetration testing platforms
url: https://blog.talosintelligence.com/artex-and-beyond/
source: Over Security
date: 2026-11-13
fetch_date: 2026-11-14T08:21:13.726655
---

# ARTEX and beyond: AI-enabled penetration testing platforms

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

# ARTEX and beyond: AI-enabled penetration testing platforms

By
[Cisco Talos](https://blog.talosintelligence.com/author/cisco/)

Friday, November 13, 2026 15:57

[Threat Advisory](/category/threat-advisory/)

Cisco Talos is tracking the growing in-the-wild usage of AI-enabled penetration testing frameworks. AI-enabled penetration testing and red team frameworks can automate and chain reconnaissance, vulnerability testing, and follow-on actions, lowering the skill threshold for attackers and accelerating intrusions when the tools are misused. Talos has seen full automation of the attack chain by these frameworks, which not only use free and open-source tools, like nmap and nuclei, but also take advantage of internet mapping services like Censys and Shodan, CAPTCHA bypass services, credential leak management services, residential proxies, and even hash cracking services. This is the case of Hephaestus, which we mentioned in our [previous report](https://blog.talosintelligence.com/keep-going-bro-youve-got-this-a-data-driven-look-at-how-adversaries-are-weaponizing-ai/).

Although these frameworks all have the same purpose, they come in different flavors. Some, like Hephaestus, are command line tools which can be deployed with a single script on a VPS and are completely controllable via Telegram.

[PentAGI](https://pentagi.com/) has a web interface to monitor the agent activity with a full attack chain graph design and monitoring. Talos found more than [700 instances](https://platform.censys.io/search?q=%28web.endpoints.http.html_title%3A+%22PentAGI%22%29) of currently reachable PentAGI instances on the internet. [HexStrike AI](https://github.com/0x4m4/hexstrike-ai) integrates with many different clients like Claude Code, VS Code, or any other client that supports MCP.

One such framework making waves, ARTEX, has enabled threat actors to scale offensive operations, compressing work that may have previously taken skilled teams hours or days into activity that can unfold at machine speed.

Talos’ analysis of ARTEX-associated IP addresses identified a diverse set of tools concurrently present on that infrastructure, reinforcing ARTEX’s role in a broader and varied threat environment.

# AI-enabled frameworks: A new reality

Before we delve into ARTEX, it is clear that these frameworks are the new reality. Their evolution will most likely include autonomous lateral movement followed by data identification and exfiltration. The precursor of this can already be seen in the victim prioritization of the Volta Infostealer, described in detail in this Talos [report](https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer/). It is highly likely that future attack chains involving these frameworks will culminate in data exfiltration and ransomware activation, all being done autonomously by one of these frameworks.

Such evolutions present new challenges to defenders:

* It reduces the time it takes to detect a compromise without any known indicators of compromise (IOCs). We provide guidance to help overcome this challenge in the Recommendations section.
* After malicious activity is identified, it is crucial to contain the incidents. These frameworks work at speeds that can make it impossible for human operators to identify, assess and react in time to disrupt the attack.

These frameworks make mitigation and containment, along with a battle-tested cybersecurity incident response plan, imperative for organizations' resiliency. Defenders using AI can be a force multiplier to provide much-needed improvements, both in the speed and scale of response to such attacks.

# ARTEX

ARTEX is an AI-enabled penetration testing framework developed under the pseudonym Autumn-27 and published on GitHub in July 2026. An operator gives it a target and objective, a planner agent breaks the objective into tasks, worker agents perform them using security tools, and the framework records assets, findings, and progress in a shared graph. ARTEX can use different large language models (LLMs) and requires relatively little operator input after a task begins. It was designed for authorized security testing, but recent public reporting documented its use in both criminal and targeted intrusion campaigns within weeks of its release.

It is important to note that ARTEX is not natively bundled with any traditional command-and-control (C2) framework, though the Model Context Protocol (MCP) extensibility layer means any compatible tool server can be added by an operator. This explains why we have observed multiple instances of ARTEX being deployed alongside tools such as VShell, GoPhish, and AdaptixC2.

## Threat actors leveraging ARTEX in offensive campaigns

Multiple threat actors with distinct motives and tradecraft have been associated with ARTEX activity; its release as open-source software, followed by the continued availability of forks and copies, almost certainly facilitated adoption across different actor groups. Public reporting (referenced below) and Talos observations indicate ARTEX is largely used by financially motivated cybercriminals and threat actors with a China nexus.

Observed ARTEX campaigns range from opportunistic scanning and credential theft to targeted intrusions and supply chain activity, with targets spanning financial services, cryptocurrency, government, telecommunications, defense, pharmaceuticals, semiconductors, and technology organizations across multiple regions. Reported outcomes vary from unsuccessful attempts to confirmed compromise and data exfiltration.

*Reported campaigns:*

* [**VAPOR PANDA**](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/)**:** CrowdStrike attributed an espionage campaign (beginning Oct. 17, 2026) leveraging ARTEX to China-nexus actor V...