---
title: RansomHub Becomes 2024’s Top Ransomware Group, Hitting 600+ Organizations Globally
url: https://thehackernews.com/2025/02/ransomhub-becomes-2024s-top-ransomware.html
source: The Hacker News
date: 2025-02-15
fetch_date: 2025-10-06T20:57:46.249836
---

# RansomHub Becomes 2024’s Top Ransomware Group, Hitting 600+ Organizations Globally

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

# [RansomHub Becomes 2024's Top Ransomware Group, Hitting 600+ Organizations Globally](https://thehackernews.com/2025/02/ransomhub-becomes-2024s-top-ransomware.html)

**Feb 14, 2025**Ravie LakshmananRansomware / Network Security

[![RansomHub](data:image/png;base64... "RansomHub")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-8H-VtOeOmU5FoJQiDaUF1Z0_UErmMOG6IBlFjsYUma3tmsMbuJCRLKISi-NCSJK5tEfwDcFKycnnZKrZCrY9A3dbcKc-18z8SbQ8o4J-3Fwdld8RWzMIVuLzzqPOHwPhTBFwRUPyEiO2xmXd3cn6ZD38sRF5KMsYmRo-jeL4JR0tvomjxpqTYp1KDGLP/s790-rw-e365/ransomhub.png)

The threat actors behind the [RansomHub](https://thehackernews.com/2025/01/python-based-malware-powers-ransomhub.html) ransomware-as-a-service (RaaS) scheme have been observed leveraging now-patched security flaws in Microsoft Active Directory and the Netlogon protocol to escalate privileges and gain unauthorized access to a victim network's domain controller as part of their post-compromise strategy.

"RansomHub has targeted over 600 organizations globally, spanning sectors such as healthcare, finance, government, and critical infrastructure, firmly establishing it as the most active ransomware group in 2024," Group-IB analysts [said](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/) in an exhaustive report published this week.

The ransomware group [first emerged](https://thehackernews.com/2024/09/ransomhub-ransomware-group-targets-210.html) in February 2024, acquiring the source code associated with the now-defunct Knight (formerly Cyclops) RaaS gang from the RAMP cybercrime forum to speed up its operations. About five months later, an updated version of the locker was advertised on the illicit marketplace with capabilities to remotely encrypt data via SFTP protocol.

It comes in multiple variants that are capable of encrypting files on Windows, VMware ESXi, and SFTP servers. RansomHub has also been observed actively recruiting affiliates from LockBit and BlackCat groups as part of a partnership program, indicating an attempt to capitalize on the law enforcement actions targeting its rivals.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In the incident analyzed by the Singaporean cybersecurity company, the threat actor is said to have unsuccessfully attempted to exploit a critical flaw impacting Palo Alto Networks PAN-OS devices ([CVE-2024-3400](https://thehackernews.com/2024/04/zero-day-alert-critical-palo-alto.html)) using a publicly available proof-of-concept (PoC), before ultimately breaching the victim network by means of a brute-force attack against the VPN service.

"This brute force attempt was based on an enriched dictionary of over 5,000 usernames and passwords," the researchers said. "The attacker eventually gained access through a default account frequently used in data backup solutions, and the perimeter was finally breached."

The initial access was then abused to carry out the ransomware attack, with both data encryption and exfiltration occurring within 24 hours of the compromise.

Particularly, it involved the weaponization of two known security flaws in Active Directory ([CVE-2021-42278](https://thehackernews.com/2021/12/active-directory-bugs-could-let-hackers.html) aka noPac) and the Netlogon protocol ([CVE-2020-1472](https://thehackernews.com/2020/09/detecting-and-preventing-critical.html) aka [ZeroLogon](https://msrc.microsoft.com/blog/2020/10/attacks-exploiting-netlogon-vulnerability-cve-2020-1472/)) to seize control of the domain controller and conduct lateral movement across the network.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjGFbjgsMcUufqJLclMTCibZ4Os7eEe9RXVpT7y6mqm33oz64hAULmM_Wf8TNozrKgOvDmwQdzWjALrU5_YYWBHj-crPMhAw013Ee4dE2N3p8-UDKHBHzyLMyRDHJq7gAzCtZGiZVqy5vZ6x7ha0VPqPNq6JpKGu3R4czpg3I1RKyBBLrN0JK9z0XWzZORY/s790-rw-e365/gib.png)

"The exploitation of the above-mentioned vulnerabilities enabled the attacker to gain full privileged access to the domain controller, which is the nerve center of a Microsoft Windows-based infrastructure," the researchers said.

"Following the completion of the exfiltration operations, the attacker prepared the environment for the final phase of the attack. The attacker operated to render all company data, saved on the various NAS, completely unreadable and inaccessible, as well as impermissible to restore, with the aim of forcing the victim to pay the ransom to get their data back."

Another notable aspect of the attack is the use of PCHunter to stop and bypass endpoint security solutions, as well as Filezilla for data exfiltration.

"The origins of the RansomHub group, its offensive operations, and its overlapping characteristics with other groups confirm the existence of a vivid cybercrime ecosystem," the researchers said.

"This environment thrives on the sharing, reusing, and rebranding of tools and source codes, fueling a robust underground market where high-profile victims, infamous groups, and substantial sums of money play central roles."

The development comes as the cybersecurity firm detailed the inner workings of a "formidable RaaS operator" known as [Lynx](https://thehackernews.com/2024/10/critical-veeam-vulnerability-exploited.html), shedding light on their affiliate workflow, their cross-platform ransomware arsenal for Windows, Linux, and ESXi environments, and customizable encryption modes.

An analysis of the ransomware's Windows and Linux versions shows that it closely resembles INC ransomware, indicating that the threat actors likely acquired the latter's source code.

"Affiliates are incentivized with an 80% share of ransom proceeds, reflecting a competitive, recruitment-driven strategy," it [said](https://www.group-ib.com/blog/cat-s-out-of-the-bag-lynx-ransomware/). "Lynx recently added multiple encryption modes: 'fast,' 'medium,' 'slow,' and 'entire,' giving affiliates the freedom to adjust the trade-off between speed and depth of file encryption."

"The group's recruitment po...