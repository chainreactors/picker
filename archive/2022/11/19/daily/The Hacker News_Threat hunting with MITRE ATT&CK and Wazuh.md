---
title: Threat hunting with MITRE ATT&CK and Wazuh
url: https://thehackernews.com/2022/11/threat-hunting-with-mitre-att-and-wazuh.html
source: The Hacker News
date: 2022-11-19
fetch_date: 2025-10-03T23:15:25.557574
---

# Threat hunting with MITRE ATT&CK and Wazuh

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Threat hunting with MITRE ATT&CK and Wazuh](https://thehackernews.com/2022/11/threat-hunting-with-mitre-att-and-wazuh.html)

**Nov 18, 2022**The Hacker News

[![MITRE ATT&CK and Wazuh](data:image/png;base64... "MITRE ATT&CK and Wazuh")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjG1T4Lng6aFJPVs5a79ItPxeNaLgNWP55xwQ2jS4MrqxE8Bv20E5ytrqP9zUYgfHcqhcpnuB4nR06oalvR3cIA_N-G9PK6k-tyk8pt_u75_eLy8yVQ_XMGN3sylgqMdPcGXJuFP1Wvd6-UqkypU0KT-Y5LAyiSeMLQKqowK4hfBcAfkY6sh-2wNx83/s790-rw-e365/wazuh.png)

Threat hunting is the process of looking for malicious activity and its artifacts in a computer system or network. Threat hunting is carried out intermittently in an environment regardless of whether or not threats have been discovered by automated security solutions. Some threat actors may stay dormant in an organization's infrastructure, extending their access while waiting for the right opportunity to exploit discovered weaknesses.

Therefore it is important to perform threat hunting to identify malicious actors in an environment and stop them before they achieve their ultimate goal.

To effectively perform threat hunting, the threat hunter must have a systematic approach to emulating possible adversary behavior. This adversarial behavior determines what artifacts can be searched for that indicate ongoing or past malicious activity.

## MITRE ATT&CK

Over the years, the security community has observed that threat actors have commonly used many tactics, techniques, and procedures (TTPs) to infiltrate and pivot across networks, elevate privileges, and exfiltrate confidential data. This has led to the development of various frameworks for mapping the activities and methods of threat actors. One example is the MITRE ATT&CK framework.

MITRE ATT&CK is an acronym that stands for MITRE Adversarial Tactics, Techniques, and Common Knowledge (ATT&CK). It is a well-documented knowledge base of real-world threat actor actions and behaviors. MITRE ATT&CK framework has 14 tactics and many techniques that identify or indicate an attack in progress. MITRE uses IDs to reference the tactic or technique employed by an adversary.

## The Wazuh unified XDR and SIEM platform

[Wazuh](https://wazuh.com) is an open source unified XDR and SIEM platform. The Wazuh solution is made up of a single universal agent that is deployed on monitored endpoints for threat detection and automated response. It also has central components (Wazuh server, indexer, and dashboard) that analyze and visualize the security events data collected by the Wazuh agent. It protects on-premises and cloud workloads.

|  |
| --- |
| [![Wazuh security event dashboard](data:image/png;base64... "Wazuh security event dashboard")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYD9HoHL3PCRByZFDN0xjZMQ2DRzBd5x3ZZPdCX_bG7BjREBWXC8Xfx0x60rETuRAAobQyjufUQ4gctKNaWzCoI8cHFlF67crNozuWZbn4E1bKLM_4y7eCJugklyXyKERDIzkJK-ixN7tNpiCvm1fYjHvvnhkr99maQCdxWwz976vX7wMJeDzI7kAb/s790-rw-e365/wazuh-1.jpg) |
| Figure 1: Wazuh security event dashboard |

#### Threat hunting with Wazuh

Threat hunters use various tools, processes, and methods to search for malicious artifacts in an environment. These include but are not limited to using tools for security monitoring, file integrity monitoring, and endpoint configuration assessment.

Wazuh offers robust capabilities like file integrity monitoring, security configuration assessment, threat detection, automated response to threats, and integration with solutions that provide threat intelligence feeds.

#### Wazuh MITRE ATT&CK module

Wazuh comes with the MITRE ATT&CK module out-of-the-box and threat detection rules mapped against their corresponding MITRE technique IDs. This module has four components which are:

a. **The intelligence component of the Wazuh MITRE ATT&CK module**: Contains detailed information about threat groups, mitigation, software, tactics, and techniques used in cyber attacks. This component helps threat hunters to identify and classify different TTPs that adversaries use.

|  |
| --- |
| [![Wazuh MITRE ATT&CK Intelligence](data:image/png;base64... "Wazuh MITRE ATT&CK Intelligence")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdaJQ6NwmsL2ZjN9uhtVe7iiyLtVoWsv58-skbGlBWnpNS4lbXqs7AIrgMDLo3HXP-VYrhf5JsIvGYBL-IBl1YPe6B1Q-1WnS6FvwVSuhaRmOwa-1Fx6VjY52GvVr0rQr7RPfK_Ly96Uxxy4cWzhuhectN4IKKB5m7q2BlJEW8mSE_6hxByDIvEF4K/s790-rw-e365/wazuh-4.jpg) |
| Figure 2: Wazuh MITRE ATT&CK Intelligence |

b. **The framework component of the Wazuh MITRE ATT&CK module**: Helps threat hunters narrow down threats or compromised endpoints. This component uses specific techniques to see all the events related to that technique and the endpoints where these events happened.

|  |
| --- |
| [![Wazuh MITRE ATT&CK framework](data:image/png;base64... "Wazuh MITRE ATT&CK framework")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhu8AMUbDEyoIayU9812CjTv13iORS1RLUQFjaZ7IilHC1RLVxaBMvpY9RGISgghD5sxfx2PWigHbLoU0wVkupE1JrvrNkhZc-22KdzYTvKcsHfNLkp9L8wQoyPbH9CYIGE5Ff89Xv2MM8MJhWqzg8z5e77jyFQ8iTuGg5GztEJr0t_u5Z3lWR_uxW5/s790-rw-e365/wazuh-6.jpg) |
| Figure 3: Wazuh MITRE ATT&CK framework |

c. **The dashboard component of the MITRE ATT&CK module**: Helps to summarize all events into charts to assist threat hunters in having a quick overview of MITRE related activities in an infrastructure.

|  |
| --- |
| [![Wazuh MITRE ATT&CK dashboard](data:image/png;base64... "Wazuh MITRE ATT&CK dashboard")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-oqWF6gxixo9BvhBBrkIan2ULRvymf47u5xPL4slGPxBk_IWNKNSHOc8EV2T76zFUo8nMNyZIIlbyyCF3ZrCkyx8_-NGOFR1OTG6TPngk6DP-oWrKHmxAuXRO4lBUjKo_Njz1Q1J7vd8YYzKTAAuu4jEer--PspVkRVMTM7GLj1LfQuUDa5Rjdu1E/s790-rw-e365/wazuh-3.jpg) |
| Figure 4: Wazuh MITRE ATT&CK dashboard |

d. **The Wazuh MITRE ATT&CK events component**: Displays events in real-time, with their respective MITRE IDs, to better understand each reported alert.

|  |
| --- |
| [![Wazuh MITRE ATT&CK events](data:image/png;base64... "Wazuh MITRE ...