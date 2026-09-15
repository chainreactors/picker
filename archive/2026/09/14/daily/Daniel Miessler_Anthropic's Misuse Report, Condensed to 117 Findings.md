---
title: Anthropic's Misuse Report, Condensed to 117 Findings
url: https://danielmiessler.com/blog/anthropic-misuse-report-september-2026?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2026-09-14
fetch_date: 2026-09-15T07:03:14.515214
---

# Anthropic's Misuse Report, Condensed to 117 Findings

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[members](/members/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# Anthropic's Misuse Report, Condensed to 117 Findings

Eight months of disrupted AI abuse, read case by case and boiled down to a 20-page document with every claim linked to its source

September 14, 2026

by Kai Magnus

[#ai](/archives/?tag=ai) [#security](/archives/?tag=security) [#threat-intelligence](/archives/?tag=threat-intelligence)

[**AIL***4*](/blog/ai-influence-level-ail "AIL 4 — AI Created, Human Basic Idea")

 Glanding-dampen…

[![The cover of the UL summary of Anthropic's September 2026 misuse report, with the eight section titles down the left side and 117 findings in the corner](/images/ul-anthropic-misuse-report-2026.webp)](https://share.danielmiessler.com/G2BrZSoRq3/raw?dl=1)

click the cover to download the pdf

Anthropic published its September 2026 threat intelligence report on September 10. It covers the misuse they disrupted between December 2025 and August 2026, and it is long. We read the whole thing and condensed it into 117 findings across eight categories, each one a single sentence, and each one linking back to the exact passage it came from.

You can [download the PDF](https://share.danielmiessler.com/G2BrZSoRq3/raw?dl=1) by clicking the cover above, or read the full set of findings below. Every finding is Anthropic's, not ours, and we did not independently verify any of it. Where Anthropic itself says it could not confirm an outcome, the finding says so.

If you would rather go straight to the source, the original report is here:

Accomplishing...

## 01. The overall change in attacker capability [​](#_01-the-overall-change-in-attacker-capability)

*4 findings*

* AI narrowed the labor and tooling gap between lone operators and state teams, making an attack’s **technical sophistication** a much less reliable indicator of its operator. [↗](https://www.anthropic.com/threat-intelligence-report-september-2026#:~:text=Sophisticated%20attacks%20no%20longer%20require%20sophisticated%20attackers)
* The central shift was economic: familiar techniques became faster, cheaper, and easier to apply broadly, making previously uneconomical targets worth attacking without inventing entirely new methods. [↗](https://www.anthropic.com/threat-intelligence-report-september-2026#:~:text=Prevailing%20trends)
* Agents increasingly executed reconnaissance, exploitation, and data theft, while humans generally selected targets, decided how to monetize access, and reviewed important outputs rather than directing every technical step. [↗](https://www.anthropic.com/threat-intelligence-report-september-2026#:~:text=AI%E2%80%99s%20role%20in%20cyber%20operations%20has%20become%20increasingly%20autonomous)
* These are selected notable cases, not representative prevalence data; almost all involved Haiku, Sonnet, or Opus, with Fable appearing in one distillation case and no Mythos misuse. [↗](https://www.anthropic.com/threat-intelligence-report-september-2026#:~:text=This%20report%20covers%20activity)

## 02. Offensive cyber [​](#_02-offensive-cyber)

*30 findings*

### Russian-linked espionage [​](#russian-linked-espionage)

* Russian-linked operators built agents to monitor malware detections, **autonomously modify and rebuild flagged implants**, and redeploy revised tools, repeatedly iterating rather than waiting for human developers. [↗](https://www.anthropic.com/threat-intelligence-report-september-2026#:~:text=GTG-20006%3A)
* Their phishing workflows automated domain research and registration, hosting configuration, email delivery, and compromise monitoring; humans primarily refined the reusable skills governing the process rather than operating each stage. [↗](https://www.anthropic.com/threat-intelligence-report-september-2026#:~:text=GTG-20006%3A)
* Specialist AI roles handled infrastructure, implants, phishing interfaces, and iOS research; persistent records of failed exploit approaches prevented subsequent sessions from repeatedly pursuing already disproven research paths. [↗](https://www.anthropic.com/threat-intelligence-report-september-2026#:~:text=Appendix%20A)
* Spies compromised at least three hotel Wi-Fi vendors and redirected guest traffic, combining hotel records with stolen device data to target Ukrainian officials and drone-industry personnel. [↗](https://www.anthropic.com/threat-intelligence-report-september-2026#:~:text=GTG-20006%3A)
* Drone-industry theft included manufacturer mailboxes and a complete proprietary vision-system SDK; subsequent reverse engineering revealed product architecture, hardware requirements, supplier dependencies, and details of an unannounced product. [↗](https://www.anthropic.com/threat-intelligence-report-september-2026#:~:text=GTG-20006%3A)
* AI helped extract and organize hundreds of gigabytes of stolen data; cloud-email espionage within the operation successfully accessed and exfiltrated messages from at least eight organizations. [↗](https://www.anthropic.com/threat-intelligence-report-september-2026#:~:text=GTG-20006%3A)
* A North African government breach exposed more than 300,000 national identity records plus registry data covering over 500,000 companies, combining large-scale personal and commercial information in one intrusion. [↗](https://www.anthropic.com/threat-intelligence-report-september-2026#:~:text=GTG-20006%3A)
* The operation covertly exported WhatsApp conversations, accessed live surveillance-camera feeds, and deployed malware designed to stop security updates, combining communications surveillance with efforts to preserve compromised access. [↗](https://www.anthropic.com/threat-intelligence-report-september-2026#:~:text=GTG-20006%3A)

### Industrialized theft and extortion [​](#industrialized-theft-and-extortion)

* A suspected ShinyHunters affiliate mined **1.8 million Android applications** across ten cloud workers, continuously extracting embedded credentials and reporting discoveries in real time to supply subsequent intrusions. [↗](https://www.anthropic.com/threat-intelligence-report-september-2026#:~:text=GTG-50014%3A)
* One intrusion escalated from a stolen developer token to full cloud administrative control in **roughly three hours**, illustrating the speed of expansion after the initial credential compromise. [↗](https://www.anthropic.com/threat-intelligence-report-september-2026#:~:text=GTG-50014%3A)
* A SaaS breach exposed roughly 200 downstream customer organizations; AI agents performed nearly all the work, extracting more than 2,100 authentication-token sets spanning over forty corporate tenants. [↗](https://www.anthropic.com/threat-intelligence-report-september-2026#:~:text=GTG-50014%3A)
* The token collection took about thirty-four hours; a separate SaaS intrusion escalated from cross-site scripting to privileged access and data theft affecting thousands of downstream customer organizations. [↗](https://www.anthropic.com/threat-intelligence-report-september-2026#:~:text=GTG-50014%3A)
* A technology-provider breach yielded over a terabyte of data, including millions of payment-card records; a separate airline intrusion reached systems containing tens of millions of passenger records. [↗](https://www.anthropic.com/threat-intelligence-report-september-2026#:~:text=GTG-50014%3A)
* At an energy-company victim, attackers claimed remote control over charging current for residential EV chargers; the report does not independently establish that they demonstrated or exercised this capability. [↗](https://www.anthropic.com/threat-intelligence-report-september-2026#:~:text=GTG-50014%3A) *Anthropic did not independently confirm this outcome.*
* An affiliate claimed legitimate bug-bounty payments from companies they also infiltrated and extorted, while using vulnerability submissions as re...