---
title: How Threat Intelligence Feeds Help During Incident Response
url: https://any.run/cybersecurity-blog/threat-intelligence-feeds-in-incident-response/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-24
fetch_date: 2025-10-06T22:06:57.220643
---

# How Threat Intelligence Feeds Help During Incident Response

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2022/10/mini-logo.png)](/cybersecurity-blog/)

* + Search

![How Threat Intelligence Feeds Help During Incident Response](/cybersecurity-blog/wp-content/uploads/2025/04/feeds_incident_blog.jpg)

[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

# How Threat Intelligence Feeds Help During Incident Response

April 23, 2025

[Add comment](#comments-13086)
2235 views
8 min read

[Home](/cybersecurity-blog/)[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

How Threat Intelligence Feeds Help During Incident Response

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1578
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3150
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3157
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

How Threat Intelligence Feeds Help During Incident Response

When data meets automation, two pillars of modern tech converge to create something smarter: Threat Intelligence Feeds. Real-time insights, machine-speed decisions, and a global perspective — all working together to outsmart threats before they become incidents.

[ANY.RUN’s TI Feeds](https://any.run/cybersecurity-blog/ti-feeds-integration/) are structured, continuously updated streams of fresh threat data. They contain network-based IOCs — **[IP addresses, domain names, and URLs](https://any.run/cybersecurity-blog/inside-cyber-threat-intelligence-feeds/)** — and are enriched by additional context-providing indicators like file hashes and port indicators.

The Feeds enhance threat detection capabilities of security systems, enable SOC teams to quickly mitigate attacks, including emerging malware and persistent threats.

## Source, Structure, Benefits of ANY.RUN’s TI Feeds

![](/cybersecurity-blog/wp-content/uploads/2025/04/tifeeds_page-1-1024x592.png)

Threat Intelligence Feeds provided by [ANY.RUN](http://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=ti_feeds_incident_response&utm_term=230425&utm_content=linktolanding) are sourced from analysis sessions in our [cloud-based sandbox](https://app.any.run/), where users [including the SOC teams of 15,000 organizations](https://any.run/cybersecurity-blog/threat-intelligence-from-organizations/) from a variety of industries detonate and dissect real-world malware samples.

The indicators are pre-processed using proprietary algorithms and whitelists to minimize false positives, ensuring high accuracy and relevance. Each indicator of compromise is enriched with contextual metadata providing deeper insights into the threat.

This means that an IP, URL, or domain in TI Feeds are enriched with:

* **External references**: Links to relevant sandbox sessions.

* **Label**: Name of the malware family or campaign.

* **Detection timestamps**: Last/first seen dates provide a timeline to understand if a threat is ongoing or historical.

* **Related objects**: IDs of files and network indicators related to the IOC.

* **Score**: Value representing the severity level of the IOC.

ANY.RUN’s TI Feeds come in STIX or MISP format with indicators of your choice. [Set up a test sample](https://intelligence.any.run/feeds) to start leveraging actionable IOCs data in your security operations. ANY.RUN also runs a dedicated MISP instance that you can synchronize your server with or connect to your security solutions. To get started, [contact our team via this page](https://intelligence.any.run/plans/?utm_source=anyrunblog&utm_medium=article&utm_campaign=ti_feeds_iocs&utm_term=270225&utm_content=linktotiplans).

By delivering insights into threats and their indicators of compromise (OCs), TI Feeds support organizations across multiple phases of incident response: Incident Triage, Threat Hunting, and Post-Incident Analysis.

Boost detection and expand threat coverage in your SOC
with TI Feeds from ANY.RUN

[Request 14-day trial](https://intelligence.any.run/plans/?utm_source=anyrunblog&utm_medium=article&utm_campaign=ti_feeds_incident_response&utm_term=230425&utm_content=linktotiplans)

## Incident Triage

Incident Triage involves assessing and prioritizing security alerts to determine their severity and potential impact. This must be done quickly and yet precisely, saving analysts from wasting time on false positives and highlighting critical true positives.

TI Feeds streamline this process by providing contextual data to validate and enrich alerts, enabling faster and more accurate decision-making.

### TI Feeds for Triage:

* **Correlation with Known Threats**: Feeds supply IOCs (e.g., malicious IPs, domains, file hashes) that can be cross-referenced with incoming alerts to confirm whether an incident is legitimate or a false positive.

* **Prioritization**: Feeds provide threat severity scores and context (e.g., association with a known ran...