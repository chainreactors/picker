---
title: DORA Year Two: Can Your SOC Actually See the Attack?
url: https://thehackernews.com/2026/09/dora-year-two-can-your-soc-actually-see.html
source: The Hacker News
date: 2026-09-22
fetch_date: 2026-09-23T06:54:53.365948
---

# DORA Year Two: Can Your SOC Actually See the Attack?

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

# [DORA Year Two: Can Your SOC Actually See the Attack?](https://thehackernews.com/2026/09/dora-year-two-can-your-soc-actually-see.html)

**The Hacker News**Sep 22, 2026Network Security / Incident Response

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgSfPPym5AUNkyGqTS_emtDBNfEzrtWQJSHGSMl0V3KkDS2_hMcu_cpDslIX9LUv9nvHbQzY9hnwDEKjdlxe6vFS3N2_PHkTk_0TdKBE7RrAdniL9dObHd24tudc-Ymy8FTsV9y6Io68EhjR6fRrRwMEJhdKczg6vpRP2Bp06cxX_EqgmqXps8ih3Tfq08/s1700-nu-rw-lo-l85-e365/core.jpg)

When the Digital Operational Resilience Act (DORA) became enforceable across the European Union in January 2025, it triggered an administrative sprint. Financial entities spent the first year establishing risk governance, assessing third-party service providers, updating contract clauses, and documenting incident escalation workflows.

Now in its second year, the harder part of DORA is demonstrating how well frameworks work in practice. EU regulators are increasing their focus on DORA implementation, Information and Communication Technology (ICT) incident analysis, and the effectiveness of ICT risk supervision. For security teams, that raises an important question: *does the SOC have enough visibility to detect, investigate, and scope an active intrusion across critical systems?*

While DORA doesn’t prescribe a particular security stack, several of its requirements rely on continuous visibility in the ICT environment to identify behavior that may indicate an emerging risk.

## Continuous monitoring requires more than an inventory

For DORA, continuous monitoring therefore isn’t just about knowing what should be happening in a network; it’s about having enough visibility to recognize when operational patterns begin to diverge from the norm.

Article 9, the ninth numbered provision of DORA, requires financial entities to continuously monitor and manage the security and functioning of their ICT ecosystem, and implement processes to minimize the impact of ICT risk.

An asset inventory shows the systems a financial institution owns or operates. Configuration records will show how those systems are intended to interact. Security logs and endpoint telemetry provide detailed visibility into activity on monitored systems.

Yet, none of those sources necessarily provides a comprehensive view of communication between systems, particularly across legacy infrastructure, specialized appliances, unmanaged devices, or systems where endpoint telemetry is limited. When confronting adaptive, AI-speed threats, a comprehensive view is necessary to identify the blind spots adversaries specifically target. Unmonitored connections between systems may hold evidence of exploitation, and companies that have visibility into what’s happening in those gaps have a greater likelihood of disrupting the attack chain.

[Network Detection and Response (NDR)](https://corelight.com/cp/ndr-essentials?utm_source=thehackernews&utm_medium=article-9&utm_campaign=awareness-wave-2) is a catalyst for bringing that level of detail together, and thus allowing organizations to work toward meeting the demands of DORA. With continuous monitoring across the environment, NDR helps establish baselines of normal behavior and evaluates timing, volume, and directionality to identify when communications deviate from expected patterns.

For example, if a payment routing application that normally communicates with an external credit assessment service suddenly communicates substantially more with unfamiliar internal hosts during non-work hours, network telemetry can expose the anomaly even when the application's own logs don't.

## Detecting anomalies requires context

Article 10, the next rule in DORA, requires financial institutions to swiftly detect anomalous activities, including network performance issues and related incidents. Further, thresholds must be established for when incident response needs to be triggered.

Security alerts are plentiful, but the volume of noise often overwhelms teams and hides the true signals of anomalous behavior. Determining if an alert is part of a larger incident is the real issue. For instance, EDR may identify a suspicious process while an identity system flags a suspicious login. [Network data can connect the two](https://corelight.com/blog/10-reasons-why-ndr-is-essential-alongside-edr?utm_source=thehackernews&utm_medium=article-9&utm_campaign=awareness-wave-2) by showing which systems communicated, the protocols used, and what happened next. Command-and-control traffic, reconnaissance, lateral movement, and data transfers all leave traces in network traffic, even when other telemetry is incomplete or unavailable.

NDR makes network evidence usable at scale by extracting structured, protocol-level data that helps analysts investigate alerts in context and in a correlated view rather than reconstructing incidents from siloed sources. Context allows responders to establish an incident’s scope and impact, especially in light of today’s AI-speed attacks, both of which inform Article 19 reporting requirements.

Under applicable rules, the initial notification must be submitted as early as possible, but no later than four hours after classification as a major ICT-related incident and no later than 24 hours after the organization becomes aware of the incident. Rapid access to [network evidence](https://corelight.com/cp/elitedefense#platform?utm_source=thehackernews&utm_medium=article-9&utm_campaign=awareness-wave-2) gives responders the clarity needed to move quickly across complex IT environments, tracing affected systems, isolating rogue connections, and assembling the required incident records within the regulation’s required timeframe.

## Third-party risk extends beyond the contract

Third-party ICT risk management and contractual agreements are the focus of Articles 28 through 30.

Contracts and vendor assessments define a provider’s authorized access and operational boundaries on paper. Ne...