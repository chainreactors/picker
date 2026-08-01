---
title: Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw
url: https://thehackernews.com/2026/07/researchers-report-84-flaws-in-4g-and.html
source: The Hacker News
date: 2026-07-31
fetch_date: 2026-08-01T05:13:35.234705
---

# Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw

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

![cybersecurity](data:image/svg+xml;base64...)

# [Researchers Report 84 Flaws in 4G and 5G Cores, Including a Session Hijacking Flaw](https://thehackernews.com/2026/07/researchers-report-84-flaws-in-4g-and.html)

**Ravie Lakshmanan**Jul 31, 2026Mobile Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhx5Qzkfu4WC4nW5n_nmFDP3CoZsw91wzaKcfKRZBx7DXHggnqqxqun757BOQey3jOUCGe4928DBU6fy4dPX04Cmp94xqWdNkZgkp1DuenVewYZFxSs9YSQdArKp1Ma3hAGkDAIA7zH8_7hXubNrJbP27r6XxIlCrzrYYoi3vAVFaLVdu1tnN6blLhE61xE/s1700-e365/ifinder.jpg)

An academic study has [disclosed](https://arxiv.org/abs/2607.10315) a "widespread class" of security vulnerabilities impacting 4G and 5G core networks that, if successfully exploited, could trigger denial-of-service (DoS) attacks and even session hijacking, allowing an attacker to seize control of a user's network session.

The findings have been released by a group of researchers from Singapore's Nanyang Technological University in a paper titled "Understanding Implicit Trust Errors in Core Carrier Networks through Multi-Agent Flaw Discovery and Analysis."

The study has uncovered dozens of vulnerabilities in the signaling interfaces of LTE/5G core networks, and specifically covers two LTE implementations (Open5GS and OpenAirInterface) and five 5G implementations (Open5GS, free5GC, OpenAirInterface, SD-Core, and eUPF) across two core signaling protocols, GPRS Tunnelling Protocol Control Plane ([GTP-C](https://en.wikipedia.org/wiki/GPRS_Tunnelling_Protocol)) and Packet Forwarding Control Protocol ([PFCP](https://free5gc.org/blog/20260204/20260204/#34-qos-enforcement-rule-qer)).

"Our research finds these vulnerabilities share a single recurring root cause, implicit trust between core network functions, and are present in widely used open-source LTE/5G cores that back research testbeds and commercial deployments alike," the researchers said.

While cellular core networks (CNs) have historically incorporated physical isolation as a means to ensure interfaces between core network functions operate within a trust zone, the transition to cloud-native deployments has made the trust model "fragile" and expanded the attack surface, allowing adversaries to potentially reach previously internal interfaces.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

The researchers said they found a pattern of blind trust among CN components, which, coupled with weaknesses in those interfaces, can be exploited by an external actor for conducting malicious activities, including DoS and session hijacking, when they become reachable over the internet. These errors have been codenamed implicit trust errors (iTrue).

To better detect such iTrues and understand their consequences, the study involved the development of a large language model (LLM)-assisted multi-agent system dubbed [iFinder](https://linziyuu.github.io/iFinder-Website/) that performs a series of tasks: summarize known flaws, categorize them into detection patterns, and use them as a foundation to discover new iTrues in CN implementations.

Some of the identified weaknesses relate to a lack of due diligence in validating message format, message semantics, and resource availability, with the CN components opting to blindly act on messages received from internal peers.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhS6YLGG0SWx3KaKLofmdD6oWZiL6XlOUcToQX7mzBHOX6M38saM-My5qwgTTv4U5kalk2kXVxgcmgu1zt9FfmzSETFgndk5bc5t6kuDFbftGjqYfCMLfX982xoT2FCDxLDEicOUxVcyoEffV6lTiQseiCuTgDT-doEhj7KHH4KmjlsFMu-1yG00EUA8m8F/s1700-e365/x3.png) |
| Overview of the iFinder framework |

In the next phase, hallucinations and false positives are weeded out using a "novel code-specification cross-checking technique," following which an LLM-driven approach is used to generate proof-of-concept (PoC) exploits for potential iTrues and refine them iteratively by executing them against CN implementations and analyzing the results.

The elimination of false positives, the researchers said, involves mapping an iTrue candidate to the protocol procedure it implements and checking whether the necessary validation and resource checks are actually enforced in the codebase.

Running the agent against the aforementioned seven 4G and 5G open-source CN implementations has uncovered 84 previously unknown vulnerabilities, out of which 83 have already been confirmed and 81 have been assigned CVE identifiers.

Some of the iTrue flaws in 5G systems are said to have been inherited from their 4G counterparts, indicating how security risks can jump generations and how a failure to adapt legacy to modern deployments can bring forth new concerns not previously accounted for.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMSJLtE11syRlygo7JRijsb2C2vIdRGbIalp70IBTL_qW_5S-s9kaJ-sp-P24bg_RgLojv9hwRClVHg2jraw73FqctLUNP8oTD4tBz9rZdeHClQNRQzszhear60nWdBJ2_6iuoEXqVbUHvL4sgBqFxcIHWHQ8J7CMMQG75hc1P1XUaJAcv7ncNSoIgzIZa/s1700-e365/x5.png) |
| Example attack exploiting duplicate PDR IDs in PFCP Session Modification Request messages to trigger session hijacking in UPF by abusing missing uniqueness validation |

That said, successful attacks based on the DoS and session hijacking iTrue flaws assumes the adversary can obtain the IP address of core network components, such as from public documentation, passive enumeration, or active scanning, as well as have access to internal core network interfaces and send arbitrary PFCP and GTP-C messages in violation of the trust model by exploiting misconfigurations in cloud deployment.

This attacker could be remote (i.e., located outside of the cellular core network) or a malicious User Equipment (UE) used to connect to a mobile network, the latter of which entails injecting carefully crafted payloads into the uplink data stream.

"By exploiting protocol tunnelling and network boundary bridging, the attacker smuggles crafted PFCP or GTP-C messages inside GTP-U messages so that, absent strict boundary enforcement, they cross the boundary and are delivered to and parsed by core-network components," the researchers said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d...