---
title: ViciousTrap Uses Cisco Flaw to Build Global Honeypot from 5,300 Compromised Devices
url: https://thehackernews.com/2025/05/vicioustrap-uses-cisco-flaw-to-build.html
source: The Hacker News
date: 2025-05-24
fetch_date: 2025-10-06T22:31:14.959815
---

# ViciousTrap Uses Cisco Flaw to Build Global Honeypot from 5,300 Compromised Devices

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

# [ViciousTrap Uses Cisco Flaw to Build Global Honeypot from 5,300 Compromised Devices](https://thehackernews.com/2025/05/vicioustrap-uses-cisco-flaw-to-build.html)

**May 23, 2025**Ravie LakshmananThreat Intelligence / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhvIKMNKLPfkBPlZCVjsRe3yoNfSdge7ahzI-fhDudt75eazJeTVWI_rRENUAj77WpXZHa2dVkfdZKmLfGkkKAehCV2kxasoanP0JoLqZ-o2lM_YsQ0yMfujtyU5cTZqhoJgThloktwxRTkwG1cHLpiNAkKAEFv4wLphsJ_OlG0m5UE01nUEdnj-s18SimV/s790-rw-e365/mm.jpg)

Cybersecurity researchers have disclosed that a threat actor codenamed ViciousTrap has compromised nearly 5,300 unique network edge devices across 84 countries and turned them into a honeypot-like network.

The threat actor has been observed exploiting a critical security flaw impacting Cisco Small Business RV016, RV042, RV042G, RV082, RV320, and RV325 Routers (CVE-2023-20118) to corral them into a set of honeypots en masse. A majority of the infections are located in Macau, with 850 compromised devices.

"The infection chain involves the execution of a shell script, dubbed NetGhost, which redirects incoming traffic from specific ports of the compromised router to a honeypot-like infrastructure under the attacker's control allowing them to intercept network flows," Sekoia [said](https://blog.sekoia.io/vicioustrap-infiltrate-control-lure-turning-edge-devices-into-honeypots-en-masse/) in an analysis published Thursday.

It's worth noting that the exploitation of CVE-2023-20118 was previously attributed by the French cybersecurity company to another botnet dubbed [PolarEdge](https://thehackernews.com/2025/02/polaredge-botnet-exploits-cisco-and.html).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEid0Tbydo_6BV-6tKFQvuQDiqqlCbO_jDUHMuIFr4bI0T11fyM_uaYoqwqC5jgJei9sNsIR0656xFJN9_KFD6vP_LK5_4PyydHD_yqTJUuqzl8nIIzOcJpPlH1BsvhLgpUcQxOTq6KcKBIw-OFyVJb6B_Zbt8c-AWqSeCRF4SvaBRZW3fvAzfK29rG-RFlB/s790-rw-e365/lists.jpg)

While there is no evidence that these two sets of activities are connected, it's believed that the threat actor behind ViciousTrap is likely setting up honeypot infrastructure by breaching a wide range of internet-facing equipment, including SOHO routers, SSL VPNs, DVRs, and BMC controllers from more than 50 brands like Araknis Networks, ASUS, D-Link, Linksys, and QNAP.

"This setup would allow the actor to observe exploitation attempts across multiple environments and potentially collect non-public or zero-day exploits, and reuse access obtained by other threat actors," it added.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The attack chain entails the weaponization of CVE-2023-20118 to download and execute a bash script via ftpget, which then contacts an external server to fetch the wget binary. In the next step, the Cisco flaw is exploited a second time, using it to execute a second script retrieved using the previously dropped wget.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCQx_tcBsXEz-0M1_8qJRr6pDPxSipw1L-kgxFWSY4hl2z9BAZ2uSWbzljhUDhvbyLcZW5mr8zC4S4-zoPJHPKnhpZWAV8vRJB4n9EVDlaE85V-VFkHMZ_yd3LPE9QzM39sd42r0pZxg1zxuVEFoJ0209Unc1_CXM1B4hn5bOk_RORCsRqbLi26ovtP7tm/s790-rw-e365/map.png)

The second-stage shell script, internally referenced as NetGhost, is configured to redirect network traffic from the compromised system to third-party infrastructure controlled by the attacker, thereby facilitating adversary-in-the-middle (AitM) attacks. It also comes with capabilities to remove itself from the compromised host to minimize forensic trail.

Sekoia said all exploitation attempts have originated from a single IP address ("101.99.91[.]151"), with the earliest activity dating back to March 2025. In a noteworthy event observed a month later, the ViciousTrap actors are said to have repurposed an undocumented web shell previously employed in PolarEdge botnet attacks for their own operations.

"This assumption aligns with the attacker's use of NetGhost," security researchers Felix Aimé and Jeremy Scion said. "The redirection mechanism effectively positions the attacker as a silent observer, capable of collecting exploitation attempts and, potentially, web shell accesses in transit."

As recently as this month, exploitation efforts have also targeted ASUS routers but from a different IP address ("101.99.91[.]239"), although the threat actors have not been found to create any honeypot on the infected devices. All the IP addresses actively used in the campaign are located in Malaysia and are part of an Autonomous System (AS45839) operated by hosting provider Shinjiru.

The actor is believed to be of Chinese-speaking origin on the basis of a weak overlap with the GobRAT infrastructure and the fact that traffic is redirected to numerous assets in Taiwan and the United States.

"The final objective of ViciousTrap remains unclear even [though] we assess with high confidence that it's a honeypot-style network," Sekoia concluded.

### Update

In a follow-up analysis published on May 28, GreyNoise revealed that it has been tracking an ongoing exploitation campaign in which attackers have gained unauthorized, persistent access to roughly 9,000 ASUS routers exposed to the internet. The threat intelligence firm said it first discovered the activity on March 18, 2025.

"This appears to be part of a stealth operation to assemble a distributed network of backdoor devices — potentially laying the groundwork for a future botnet," it [added](https://www.greynoise.io/blog/stealthy-backdoor-campaign-affecting-asus-routers).

"The tactics used in this campaign — stealthy initial access, use of built-in system features for persistence, and careful avoidance of detection — are consistent with those seen in advanced, long-term operations, including activity associated with advanced persistent threat (APT) actors and operational relay box (ORB) networks."

The attackers have been obs...