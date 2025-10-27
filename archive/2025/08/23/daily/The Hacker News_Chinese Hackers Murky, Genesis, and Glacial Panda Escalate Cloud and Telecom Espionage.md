---
title: Chinese Hackers Murky, Genesis, and Glacial Panda Escalate Cloud and Telecom Espionage
url: https://thehackernews.com/2025/08/chinese-hackers-murky-genesis-and.html
source: The Hacker News
date: 2025-08-23
fetch_date: 2025-10-07T00:50:57.946868
---

# Chinese Hackers Murky, Genesis, and Glacial Panda Escalate Cloud and Telecom Espionage

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

# [Chinese Hackers Murky, Genesis, and Glacial Panda Escalate Cloud and Telecom Espionage](https://thehackernews.com/2025/08/chinese-hackers-murky-genesis-and.html)

**Aug 22, 2025**Ravie LakshmananCloud Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjI7LhdZrfHdvNIWAe3KrnQnkgy-WHWNfhTv1mG7Yv-rlKXtmXEvqf39-L1mtrf2TARYJFL9kfsQR5BpVFv9avvaK85vWWFOm1rcrF5OI0Oz6WTiu2VVtzqKc9GrVJNCsm-U0a1SGdpEHXviFdOu6J_r0S3ausuwKtsSWe30v4va8pd5Xo16wMItiNxih0J/s790-rw-e365/chinese-hackers.jpg)

Cybersecurity researchers are calling attention to malicious activity orchestrated by a China-nexus cyber espionage group known as **Murky Panda** that involves abusing trusted relationships in the cloud to breach enterprise networks.

"The adversary has also shown considerable ability to quickly weaponize N-day and zero-day vulnerabilities and frequently achieves initial access to their targets by exploiting internet-facing appliances," CrowdStrike [said](https://www.crowdstrike.com/en-us/blog/murky-panda-trusted-relationship-threat-in-cloud/) in a Thursday report.

Murky Panda, also known as [Silk Typhoon](https://www.microsoft.com/en-us/security/security-insider/threat-landscape/silk-typhoon) (formerly Hafnium), is best known for its [zero-day exploitation of Microsoft Exchange Server flaws](https://thehackernews.com/2025/07/chinese-hacker-xu-zewei-arrested-for.html) in 2021. Attacks mounted by the hacking group have targeted government, technology, academic, legal, and professional services entities in North America.

Earlier this March, Microsoft [detailed](https://thehackernews.com/2025/03/china-linked-silk-typhoon-expands-cyber.html) the threat actor's shift in tactics, detailing its targeting of the information technology (IT) supply chain as a means to obtain initial access to corporate networks. It's assessed that Murky Panda's operations are driven by intelligence gathering.

Like other Chinese hacking groups, Murky Panda has exploited internet-facing appliances to obtain initial access and is believed to have also compromised small office/home office (SOHO) devices that are geolocated in the targeted country as an exit node to hinder detection efforts.

Other infection pathways include exploitation of known security flaws in Citrix NetScaler ADC and NetScaler Gateway ([CVE-2023-3519](https://thehackernews.com/2023/10/citrix-devices-under-attack-netscaler.html)) and Commvault ([CVE-2025-3928](https://thehackernews.com/2025/05/commvault-confirms-hackers-exploited.html)). The initial access is leveraged to deploy web shells like [neo-reGeorg](https://thehackernews.com/2025/07/chinese-hackers-exploit-ivanti-csa-zero.html) to establish persistence and ultimately drop a custom malware called CloudedHope.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

A 64-bit ELF binary and written in Golang, CloudedHope functions as a basic remote access tool (RAT) while employing anti-analysis and operational security (OPSEC) measures, such as modifying timestamps and deleting indicators of their presence in victim environments to fly under the radar.

But a notable aspect of Murky Panda's tradecraft concerns the abuse of trusted relationships between partner organizations and their cloud tenants, exploiting zero-day vulnerabilities to breach software-as-a-service (SaaS) providers' cloud environments and conduct lateral movement to downstream victims.

In at least one instance observed in late 2024, the threat actor is said to have compromised a supplier of a North American entity and used the supplier's administrative access to the victim entity's Entra ID tenant to add a temporary backdoor Entra ID account.

"Using this account, the threat actor then backdoored several preexisting Entra ID service principles related to Active Directory management and emails," CrowdStrike said. "The adversary's goals appear targeted in nature based on their focus on accessing emails."

### From Murky to Genesis

Another China-linked threat actor that has proven skilful at manipulating cloud services is **Genesis Panda**, which has been observed using the infrastructure for basic exfiltration and targeting cloud service provider (CSP) accounts to expand access and establish fallback persistent mechanisms.

Active since at least January 2024, Genesis Panda has been attributed to high-volume operations targeting the financial services, media, telecommunications, and technology sectors spanning 11 countries. The goal of the attacks is to enable access for future intelligence-collection activity.

The possibility that it acts as an initial access broker stems from the group's exploitation of a wide range of web-facing vulnerabilities and limited data exfiltration.

"Although Genesis Panda targets a variety of systems, they show consistent interest in compromising cloud-hosted systems to leverage the cloud control plane for lateral movement, persistence, and enumeration," CrowdStrike [said](https://go.crowdstrike.com/rs/281-OBQ-266/images/Threat-Hunt-Report-2025.pdf).

The adversary has observed "consistently" querying the Instance Metadata Service (IMDS) associated with a cloud-hosted server to obtain credentials for the cloud control plane and enumerate network and general instance configurations. It's also known to use credentials, likely obtained from compromised virtual machines (VMs), to burrow deeper into the target's cloud account.

The findings illustrate how Chinese hacking groups are becoming increasingly adept at breaking and navigating cloud environments, while also prioritizing stealth and persistence to ensure sustained access and covert data harvesting.

### Glacial Panda Strikes Telecom Sector

The [telecommunications sector](https://thehackernews.com/2025/06/china-linked-salt-typhoon-exploits.html), per CrowdStrike, has witnessed a 130% increase in [nation-state activity](https://thehackernews.com/2024/11/china-backed-hackers-leverage-sigtran.html) over...