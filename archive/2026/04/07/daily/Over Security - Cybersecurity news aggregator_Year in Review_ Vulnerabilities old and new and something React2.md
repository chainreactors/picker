---
title: Year in Review: Vulnerabilities old and new and something React2
url: https://blog.talosintelligence.com/year-in-review-vulnerabilities-old-and-new-and-something-react2/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-07
fetch_date: 2026-04-08T04:38:54.612776
---

# Year in Review: Vulnerabilities old and new and something React2

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

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/04/2025YiR-topic_vulnerabilities.jpg)

# Year in Review: Vulnerabilities old and new and something React2

By
[Kri Dontje](https://blog.talosintelligence.com/author/kri/)

Tuesday, April 7, 2026 06:00

[2025YiR](/category/2025yir/)
[Year In Review](/category/year-in-review/)

Speed and age shouldn’t be allowed to pair up, but that is the theme of the [Talos 2025 Year in Review](https://blog.talosintelligence.com/2025yearinreview/) vulnerability findings.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/04/YiR_top10_vulns.jpg)

Figure 1. React/React2Shell (2025) at the top, with PHPUnit (2017) and Log4j (2021) following up.

The year was characterized by an unending beat-down on infrastructure that relied on older enmeshed dependencies (e.g., Log4j and PHPUnit), while React2Shell rocketed to the highest percentage of attacks for the entire year within the last three weeks of 2025. Agentic AI's capacity for building and deploying new proofs-of-concepts and exploit kits lowered attacker time-to-exploit, and the landscape shifted for defenders.

*“The speed at which these CVEs climbed into the top tier reflects a larger systemic challenge: Newly disclosed vulnerabilities in widely deployed software can generate significant, organization-wide impact long before typical patch cycles catch up, leaving defenders with small reaction windows and escalating consequences for even short-lived exposure.” – 2025 Talos Year in Review*

## Top-targeted infrastructure

Outdated infrastructure continues to expand the attack surface. Components like PHPUnit, ColdFusion, and Log4j are often embedded within applications, tightly coupled to legacy applications. Technologies age quickly, and companies are under pressure to adopt first, ask questions later. Low-use systems in a network can fossilize, unnoticed and unpatched. Others become mainstays that often cannot be swapped out or even patched without destabilizing an organization.

Attackers prioritized software and firmware inside network appliances, identity-adjacent systems, and widely deployed open-source components:

* Remote code execution (RCE) flaws, which enable access without requiring user interaction, avoiding a need for social engineering
* Legacy systems and widely used components
* Perimeter devices, especially without endpoint detection and response (EDR)

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/04/YiR_top50_CVEs.jpg)

Figure 2. Top 50 network infrastructure CVEs.

The theme was identity, identity, identity. Controlling identity meant controlling access, so attackers focused on components that authenticate users, enforce access decisions, and broker trust between systems. A small number of vulnerabilities targeting these vectors drove outsized risk. This can invalidate multi-factor authentication (MFA) checks and bypass segmentation.

## Defender recommendations

Attacker prioritization is now guided less by vulnerability age or maturity and more by exposure, exploitability, and proximity to trust, reshaping how organizations must think about risk in modern environments.

Attackers exploit patching gaps and policy weaknesses in vendor lifecycles. Organizations should evaluate their identity-centric network components and management platforms and prioritize patching of network devices accordingly.

For a more in-depth analysis of these trends, as well as how company size impacted CVE targeting trends, why the management plane matters, and the shortening window defenders have for putting defenses in place, see the [2025 Year in Review report](https://blog.talosintelligence.com/2025yearinreview/).

##### Share this post

#### Related Content

[### Talos Takes: 2025's ransomware trends and zombie vulnerabilities

April 7, 2026 08:03

In this episode of Talos Takes, Amy and Pierre Cadieux unpack the ransomware and vulnerability trends that defined 2025.](/talos-takes-2025s-ransomware-trends-and-zombie-vulnerabilities/)

[### [Video] The TTP Ep 21: When Attackers Become Trusted Users

April 2, 2026 09:06

An episode of the Talos Threat Perspective on the 2025 Year in Review trends. We explore how identity is being used to gain, extend, and maintain access inside environments.](/video-the-ttp-ep-21-when-attackers-become-trusted-users/)

[### Inside the Talos 2025 Year in Review: A discussion on what the data means for defenders

April 2, 2026 06:00

A conversation between Cisco Talos and Cisco Security leaders on the 2025 threat landscape, from identity attacks and legacy vulnerabilities to AI-driven threats, and what defenders should prioritize now.](/inside-the-talos-2025-year-in-review-a-discussion-on-what-the-data-means-for-defenders/)

* + ###### [Intelligence Center](https://talosintelligence.com/reputation)
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* + ###### [Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* + ###### [Incident Response](https://talosintelligence.com/incident_response)
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* + ###### Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosi...