---
title: Exposed Infrastructure Reveals How Ransomware Affiliates Used AI Agents to Execute Intrusions
url: https://thehackernews.com/2026/10/exposed-infrastructure-reveals-how.html
source: The Hacker News
date: 2026-10-23
fetch_date: 2026-10-24T06:48:21.633044
---

# Exposed Infrastructure Reveals How Ransomware Affiliates Used AI Agents to Execute Intrusions

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Exposed Infrastructure Reveals How Ransomware Affiliates Used AI Agents to Execute Intrusions](https://thehackernews.com/2026/10/exposed-infrastructure-reveals-how.html)

**Ravie Lakshmanan**Oct 23, 2026Ransomware / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg6gkXKzxUypnUKbTuo7Xq-8TSUpDD8TNF5XEG-bV6zcA7V3z_cO2pJeTiX1KIFi-rFNX5SOlMY93oGQpfQUuWOl0RJ35nM1XeIqu2ZV4aAIZXEd9RXQVQk0rMmeI67ysGsTJ1OXLIQg2LvGjMLHCQQ8dgqalHaBE9yCZKwIOVjHCD_lOTlsP1HdBziZ3Sb/s1700-nu-rw-lo-l85-e365/ai-hacker-kimi.jpg)

Cybersecurity researchers have discovered an artificial intelligence (AI)-driven intrusion ecosystem run by affiliates of the [INC](https://thehackernews.com/2026/06/inc-ransomware-claims-830-victims-since.html) and [The Gentlemen](https://thehackernews.com/2026/06/the-gentlemen-raas-uses-gentlekiller.html) ransomware groups.

Central to the operation is an "Autonomous Red Team Kill Chain Framework" referred to as Phantom. The threat actor is assessed to be Russian-speaking and functions both as an intrusion and data-extortion operator, as well as an infrastructure provider supporting different partners across the ransomware ecosystem.

"The operators exploited edge and remote-access systems at scale, including FortiClient EMS, SimpleHelp, cPanel, and VPN gateways," SOCRadar [said](https://socradar.io/blog/inc-gentlemen-ransomware-ai-infrastructure/). "They used AI-managed knowledge bases to track victims, stolen credentials, and campaign progress."

A notable aspect that defines the campaign is its "AI-executed, human-approved operating structure" in which a human operator provides a victim-specific prompt and reviews every step, while the intrusions themselves are executed through OpenCode with OpenRouter-hosted commercial models.

An examination of the exposed directory at 45.227.254[.]43 has revealed the activity logged 8,257 messages across 133 sessions. Should the models refuse to act on the prompts, the operator has been found to [rewrite requests](https://thehackernews.com/2026/10/cyberxero-uses-claude-code-in-campaign.html) as an authorized red team assessment instead of simply switching models.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

Initial access is achieved by exploiting public-facing edge devices at scale, following which the attackers move laterally, establish persistence, exfiltrate data, and escalate toward ransomware deployment. Operator records indicate that the attacks involve the exploitation of the following flaws -

* [CVE-2024-57727](https://nvd.nist.gov/vuln/detail/cve-2024-57727) (SimpleHelp path traversal) (Actively exploited)
* [CVE-2026-35616](https://nvd.nist.gov/vuln/detail/CVE-2026-35616) (Fortinet FortiClient authentication bypass) (Actively exploited)
* [CVE-2026-41940](https://nvd.nist.gov/vuln/detail/CVE-2026-41940) (cPanel/WHM authentication bypass) (Actively exploited)
* [CVE-2026-15409](https://nvd.nist.gov/vuln/detail/CVE-2026-15409) (SonicWall SMA 1000 SSRF) (Staged for targeting, no confirmed compromise)
* [CVE-2026-63030](https://nvd.nist.gov/vuln/detail/CVE-2026-63030) (WordPress [wp2shell](https://www.akamai.com/blog/security-research/wordpress-unauthenticated-rce-cve-2026-63030-cve-2026-60137)) (Developed)
* [CVE-2026-42208](https://nvd.nist.gov/vuln/detail/CVE-2026-42208) (LiteLLM SQL injection) (Developed or referenced)
* [CVE-2026-9082](https://nvd.nist.gov/vuln/detail/CVE-2026-9082) (Drupal SQL injection) (Developed or referenced)

"Once inside, the operators followed a recurring lifecycle: enumerate the domain, escalate to domain admin where possible, harvest credentials with stealer tooling, prioritize finance, HR, legal and executive files, and collect them over reverse-SOCKS tunnels," SOCRadar said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhd7Q03kMD-vN-ifJWrZyxZg80pzYWbsQyVtrta5BGwbGQn-7NQ-mCYqyQr2f-6e5i0k07rPgQwzd9mRZeYzr0shFEZwqna3-DCE8xwch6Zlpcl2NInlDyVYCB8sD-XG59x3TOvrA9dWjr_BvWSogfeQzU9CUYLh4HxH7-xTS-yXVTXBCsk9687VjoTAdwC/s1700-nu-rw-lo-l85-e365/soc1.jpg)

"Credential reuse was the main force multiplier; in one case, a single reused password unlocked the VPN, servers, RMM, backup and security management platforms at once. Security products were impaired with a [BYOVD killer](https://thehackernews.com/2026/03/54-edr-killers-use-byovd-to-exploit-34.html) and loader-level evasion, although the operators' own logs record mixed results against enterprise EDRs."

Supporting the threat actor in their goals is a diverse toolkit comprising bespoke frameworks, modified open-source tools, and compiled binaries -

* Phantom, an AI-powered offensive security and penetration testing framework that's deployed in live operations via OpenCode and employs an agent that communicates with an external server to retrieve tasks, execute commands, and return outputs. It supports 18 skill modules to facilitate reconnaissance, binary reverse engineering, exploit research, steganography, telemetry assessment, and EDR fingerprinting, among others.
* WormGPT-MCP, a set of 32 Model Context Protocol (MCP) servers connecting the AI system to 32 different modules that span functions ranging from reconnaissance to extortion.
* Ghost C2, a collection of three generations of polymorphic implants that communicate with a remote server over Cloudflare, Telegram, or DNS, and execute tasking and maintain persistent beacons on compromised endpoints.
* RevSocks, a reverse SOCKS5 framework used to pivot inside victim networks and stage data for exfiltration.

Other tools include a Cloudflare-fronted [Mythic agent](https://thehackernews.com/2025/11/romcom-uses-socgholish-fake-update.html) dubbed QuickLine, a Quick Heal/Seqrite EDR killer that abuses the Zemana driver ("zam64.sys") as part of a BYOVD attack, and exfiltration programs such as rks3 and BackupAgent.

Analysis of dozens of AI-authored extortion records shows that...