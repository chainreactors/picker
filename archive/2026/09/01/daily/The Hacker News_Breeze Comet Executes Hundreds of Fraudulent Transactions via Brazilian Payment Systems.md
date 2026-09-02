---
title: Breeze Comet Executes Hundreds of Fraudulent Transactions via Brazilian Payment Systems
url: https://thehackernews.com/2026/09/breeze-comet-executes-hundreds-of.html
source: The Hacker News
date: 2026-09-01
fetch_date: 2026-09-02T06:41:52.354739
---

# Breeze Comet Executes Hundreds of Fraudulent Transactions via Brazilian Payment Systems

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Breeze Comet Executes Hundreds of Fraudulent Transactions via Brazilian Payment Systems](https://thehackernews.com/2026/09/breeze-comet-executes-hundreds-of.html)

**Ravie Lakshmanan**Sep 01, 2026Cybercrime / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvGVdje0roDTqKcU541FTx34ODDmuBU-qtwYwoW0-qAYscD9yX5stIs8EhQtC7gnwM4WpqNTjYFRRwXm7w97C5tY7eEhCQJ89Y_uesRzrbbuR7knHdEkoDetSlRpfa8XOD_rdChE5yFh3VtBPlChgYRKp9ZDon-0B1_VAM9NOd0_xvgw9gD_YF7lSBXiPI/s1700-nu-rw-lo-l85-e365/brazil.jpg)

Brazilian financial services, retail, and e-commerce organizations have become the target of a financially motivated threat actor dubbed **Breeze Comet** (formerly UNC5669) since 2024.

Google Threat Intelligence Group (GTIG) and Mandiant teams [described](https://cloud.google.com/blog/topics/threat-intelligence/financially-motivated-threat-actor-breeze-comet-targets-brazil/) the threat actor as "specializing in manipulating payment systems and banking software in Brazil to conduct fraudulent transfers." The adversary is said to have successfully carried out at least one heist of assets worth tens of thousands of U.S. dollars.

The activity overlaps with threat activity clusters tracked by CrowdStrike and Trend Micro under the monikers Plump Spider and [SHADOW-AETHER-064](https://thehackernews.com/2026/05/threatsday-bulletin-linux-rootkits.html#ai-driven-intrusions-surge). According to CrowdStrike, the e-crime group is operating out of Brazil and has been active since September 2023, monetizing their intrusions by gaining unauthorized access to internal payment systems and carrying out fraudulent transactions.

Initial access to financial entities and companies offering financial services is accomplished via password spraying and voice calls impersonating IT support teams to persuade targets to install Remote Monitoring and Management (RMM) tools such as AnyDesk. In one case [highlighted](https://blog.axur.com/en-us/axur-reveals-plump-spider-modus-operandi-systemic-pix-fraud) by Axur in November 2025, the threat actors masqueraded as IT support personnel over a WhatsApp conversation and guided the victim to install a PowerShell reconnaissance script under the pretext of updating a corporate application.

Alternatively, the group has targeted vulnerable JBoss AS servers to deploy web shells, which are then used to deliver additional tooling, including Chisel and other proxy utilities, for follow-on exploitation.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The threat actor's primary targets are organizations with permission to conduct transactions through banking software, APIs, and payment systems such as Pix, STR, and Boleto. This covers a wide range of entities like banks, payment processors, retailers, and exchanges, not to mention fintech and banking software providers.

"Breeze Comet tactics have evolved over time to leverage a customized malware suite and compromised, trusted websites to facilitate initial access, command-and-control (C2), and to interact with financial software and payment APIs," Google said. "Breeze Comet's operational infrastructure may also indicate intent to expand their infrastructure footprint to other countries in Latin America and Africa."

To achieve its goals, however, it must meet four requirements: have access to the National Financial System Network (RSFN) through an entity that already has this access; access to mTLS credentials that allow sending authenticated payloads with transactional orders to Pix or STR; access to several accounts in the targeted organizations' Active Directory and cloud environments; and possess an understanding of an organization's transfer processing procedures, network controls, fintech integrations, and anti-fraud systems.

Some of the other notable tactics are listed below -

* Using compromised Brazilian small government websites to stage RMM tools, infostealers dressed up as legitimate tax or receipt documents, and backdoors like [XWorm](https://thehackernews.com/2025/10/xworm-60-returns-with-35-plugins-and.html), as well as using them as C2 endpoints to bypass reputation filters and avoid detection. A similar modus operandi has been replicated across Nigeria, Paraguay, Ghana, and Venezuela, indicating a growing targeting focus.
* Connecting rogue hardware devices directly into retail store networks as a means to establish direct footholds and then move laterally to internal systems, followed by downloading the Netcat utility and custom scripts to retrieve post-exploitation frameworks.
* Using Impacket, ADRecon, and ADVipscan, and the custom LDAP brute-forcing utility REALBREEZE to conduct internal reconnaissance and escalate privileges by targeting development and cloud environments.
* Moving laterally by initiating unauthorized Remote Desktop Protocol (RDP) sessions and executing commands via SMB network file shares. This step also involves the deployment of COBALTSPIN, a Rust-based routing malware that operates as a network tunneler to communicate with and maintain persistent network access to financial API infrastructure.

"By establishing a reverse SOCKS5 proxy over a WebSocket connection, COBALTSPIN routes network traffic securely back and forth between the C2 and internal targets, enabling lateral movement directly through boundary firewalls without requiring built-in persistence mechanisms that might trigger detection," Google said.

Breeze Comet's persistence mechanisms have evolved from dropping commercial RMM tools in 2024 to deploying malicious Kubernetes pods a year later and stealing cloud secrets by exfiltrating them to public-facing notepad websites like "dontpad[.]com." Since then, the threat actor has also been observed making use of multiple custom backdoors as a redundant access method and expanding their foothold -

* **LIGHTPAINT**, a Java-based backdoor that's used to install the legitimate SoftEther VPN and config...