---
title: China-Linked Flax Typhoon Cyber Espionage Targets Taiwan's Key Sectors
url: https://thehackernews.com/2023/08/china-linked-flax-typhoon-cyber.html
source: The Hacker News
date: 2023-08-26
fetch_date: 2025-10-04T12:02:21.899381
---

# China-Linked Flax Typhoon Cyber Espionage Targets Taiwan's Key Sectors

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

# [China-Linked Flax Typhoon Cyber Espionage Targets Taiwan's Key Sectors](https://thehackernews.com/2023/08/china-linked-flax-typhoon-cyber.html)

**Aug 25, 2023**Ravie LakshmananCyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhE8SwyldZw2XQ-eC-9FBFTliDcs2KXGTySOjWS-QjMD3ZNHg7ITdVFTbJxOPmCczBHE7GOnOV-6P4tr7n98xClLQkJW9qE-bh8jD6Gj9qbwV2O7u0wK-7IZ9IRIalKNHi3xoH0MAkLS4CxLzsuDNw24IqREMV61bEB8N7alomU5c-QMluyl-WZgEV8pT80/s790-rw-e365/china.jpg)

A nation-state activity group originating from China has been linked to cyber attacks on dozens of organizations in Taiwan as part of a suspected espionage campaign.

The Microsoft Threat Intelligence team is tracking the activity under the name **Flax Typhoon**, which is also known as Ethereal Panda.

"Flax Typhoon gains and maintains long-term access to Taiwanese organizations' networks with minimal use of malware, relying on tools built into the operating system, along with some normally benign software to quietly remain in these networks," the company [said](https://www.microsoft.com/en-us/security/blog/2023/08/24/flax-typhoon-using-legitimate-software-to-quietly-access-taiwanese-organizations/).

It further said it hasn't observed the group weaponize the access to conduct data-collection and exfiltration. A majority of the targets include government agencies, educational institutions, critical manufacturing, and information technology organizations in Taiwan.

A smaller number of victims have also been detected in Southeast Asia, North America, and Africa. The group is suspected to have been active since mid-2021.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Ethereal Panda operations primarily focus on entities in the academic, technology, and telecommunications sectors in Taiwan," CrowdStrike [notes](https://www.crowdstrike.com/adversaries/ethereal-panda/) in its description of the hacker crew. "Ethereal Panda relies heavily on SoftEther VPN executables to maintain access to victim networks, but has also been observed deploying the GodZilla web shell."

The primary focus of the actor revolves around persistence, lateral movement, and credential access, with the actor employing living-off-the-land ([LotL](https://www.microsoft.com/security/blog/2018/09/27/out-of-sight-but-not-invisible-defeating-fileless-malware-with-behavior-monitoring-amsi-and-next-gen-av/)) methods and hands-on keyboard activity to realize its goals.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjqgGcXw286iLfHQOJhtTYMakLO39FbS5t3cS7BiOe-TVS9un3iZSM8aY9HN7YIAMTNMn-wdn5uZ3ujLJbUNZ67QxZv3ltrUCN4zkn5k5_R8TqYXFHpag_v6AFi0efjEaIMl4NkEBJRgCEMnr2UgetpiZtSW_PNBozrjrNl15BWnvW9cXQAAa2-IQ3OsDri/s790-rw-e365/ms.jpg)

The modus operandi is in line with threat actors' practice of continually updating their approaches to evade detection, banking on available tools in the target environment to avoid unnecessary download and creation of custom components.

Initial access is facilitated by means of exploiting known vulnerabilities in public-facing servers and deploying web shells like China Chopper, followed by establishing persistent access over Remote Desktop Protocol (RDP), deploy a VPN bridge to connect to a remote server, and harvest credentials using Mimikatz.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

A noteworthy aspect of the attacks is the [modification of the Sticky Keys behavior](https://thehackernews.com/2023/06/state-backed-hackers-employ-advanced.html) to launch Task Manager, enabling Flax Typhoon to conduct post-exploitation on the compromised system.

"In cases where Flax Typhoon needs to move laterally to access other systems on the compromised network, the actor uses LOLBins, including Windows Remote Management (WinRM) and WMIC," the Windows maker said.

|  |
| --- |
| [![CrowdStrike](data:image/png;base64... "CrowdStrike")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjosM251m8S0p91eUs1gd4ka8_SuE8al2TjY_hx2HJ9lvPYdJ6rujDPPzKQrQFJLeRUcv8i6gUaezYiUj46wre0fD3oT6ccO7suRdmTl-X4S-Pqt7bR1tw9eDOZm_D3FvPWv07SMdups_j-cPhOl0BSHxOl2RTV1Uhe0JaXDtSGdw0935ZdaSlBwgl4GooO/s790-rw-e365/c.jpg) |
| Source: CrowdStrike |

CrowdStrike, which [highlighted](https://www.crowdstrike.com/blog/global-threat-report-preview-2023/) in February 2023 a case study involving an Ethereal Panda intrusion, said the actor likely abused an Apache Tomcat instance to breach an unnamed organization in order to enumerate various resources within the host and dump credentials using both ProcDump and Mimikatz.

The development comes three months after Microsoft exposed another China-linked actor named [Volt Typhoon](https://thehackernews.com/2023/06/chinese-hackers-using-never-before-seen.html) (aka Bronze Silhouette or Vanguard Panda), which has been observed exclusively relying on LotL techniques to fly under the radar and exfiltrate data.

While crossover of tactics and infrastructure among threat actors operating out of China isn't unusual, the findings paint the picture of a constantly evolving threat landscape, with adversaries shifting their tradecraft to become more selective in their follow-on operations.

*(The story was updated after publication to include additional information shared by CrowdStrike.)*

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News]...