---
title: New BPFDoor Controller Enables Stealthy Lateral Movement in Linux Server Attacks
url: https://thehackernews.com/2025/04/new-bpfdoor-controller-enables-stealthy.html
source: The Hacker News
date: 2025-04-17
fetch_date: 2025-10-06T22:09:29.334752
---

# New BPFDoor Controller Enables Stealthy Lateral Movement in Linux Server Attacks

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

# [New BPFDoor Controller Enables Stealthy Lateral Movement in Linux Server Attacks](https://thehackernews.com/2025/04/new-bpfdoor-controller-enables-stealthy.html)

**Apr 16, 2025**Ravie LakshmananCyber Espionage / Network Security

[![Lateral Movement in Linux Server Attacks](data:image/png;base64... "Lateral Movement in Linux Server Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3jAeGZEdviAIbzqGGLZJt8AuWKbxcUfjw27kzLNYtYi-20KUqbcsCfDT9xRL8IuUykEdYPCGsESTfX9nI39elVdkSsaOcWbmEDZ1jgpqJ0gcqrltWf-mwDjM6kzUnb30etvXVvIkqAm9lGagXGWK6zoqCpzzfN-toU_2z88Mxjem-ZugTe_5bDD00aE4E/s790-rw-e365/linux.jpg)

Cybersecurity researchers have unearthed a new controller component associated with a known backdoor called [BPFDoor](https://thehackernews.com/2023/05/new-variant-of-linux-backdoor-bpfdoor.html) as part of cyber attacks targeting telecommunications, finance, and retail sectors in South Korea, Hong Kong, Myanmar, Malaysia, and Egypt in 2024.

"The controller could open a reverse shell," Trend Micro researcher Fernando Mercês [said](https://www.trendmicro.com/en_us/research/25/d/bpfdoor-hidden-controller.html) in a technical report published earlier in the week. "This could allow lateral movement, enabling attackers to enter deeper into compromised networks, allowing them to control more systems or gain access to sensitive data.

The campaign has been attributed with medium confidence to a threat group it tracks as Earth Bluecrow, which is also known as DecisiveArchitect, Red Dev 18, and Red Menshen. The lower confidence level boils down to the fact that the BPFDoor malware source code was [leaked in 2022](https://github.com/gwillgues/BPFDoor), meaning it could also have bee adopted by other hacking groups.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

BPFDoor is a Linux backdoor that [first came to light](https://sandflysecurity.com/blog/bpfdoor-an-evasive-linux-backdoor-technical-analysis/) in 2022, with the malware positioned as a long-term espionage tool for use in attacks targeting entities in Asia and the Middle East at least a year prior to public disclosure.

The most distinctive aspect of the malware is that it creates a persistent-yet-covert channel for threat actors to control compromised workstations and access sensitive data over extended periods of time.

The malware gets its name from the use of Berkeley Packet Filter ([BPF](https://www.trendmicro.com/en_us/research/23/g/detecting-bpfdoor-backdoor-variants-abusing-bpf-filters.html)), a technology that allows programs to attach network filters to an open socket in order to inspect incoming network packets and monitor for a specific Magic Byte sequence so as to spring into action.

"Because of how BPF is implemented in the targeted operating system, the magic packet triggers the backdoor despite being blocked by a firewall," Mercês said. "As the packet reaches the kernel's BPF engine, it activates the resident backdoor. While these features are common in rootkits, they are not typically found in backdoors."

The latest analysis from Trend Micro has found that the targeted Linux servers have also been infected by a previously undocumented malware controller that's used to access other affected hosts in the same network after lateral movement.

"Before sending one of the 'magic packets' checked by the BPF filter inserted by BPFDoor malware, the controller asks its user for a password that will also be checked on the BPFDoor side," Mercês explained.

In the next step, the controller directs the compromised machine to perform one of the below actions based on the password provided and the command-line options used -

* Open a reverse shell
* Redirect new connections to a shell on a specific port, or
* Confirm the backdoor is active

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

It's worth pointing out that the password sent by the controller must match one of the hard-coded values in the BPFDoor sample. The controller, besides supporting TCP, UDP, and ICMP protocols to commandeer the infected hosts, can also enable an optional encrypted mode for secure communication.

Furthermore, the controller supports what's called a direct mode that enables the attackers to directly connect to an infected machine and obtain a shell for remote access – but only when provided the right password.

"BPF opens a new window of unexplored possibilities for malware authors to exploit," Mercês said. "As threat researchers, it is a must to be equipped for future developments by analyzing BPF code, which will help protect organizations against BPF-powered threats."

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
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data breach](https://thehackernews.com/search/label/data%20breach)[linux](https://thehackernews.com/search/label/linux)[Malware](https://thehackernews.com/search/label/Malware)[network security](https://thehackernews.com/search/label/network%20security)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[!...