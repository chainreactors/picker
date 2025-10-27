---
title: New Linux Variant of Play Ransomware Targeting VMware ESXi Systems
url: https://thehackernews.com/2024/07/new-linux-variant-of-play-ransomware.html
source: The Hacker News
date: 2024-07-23
fetch_date: 2025-10-06T17:48:20.367847
---

# New Linux Variant of Play Ransomware Targeting VMware ESXi Systems

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

# [New Linux Variant of Play Ransomware Targeting VMware ESXi Systems](https://thehackernews.com/2024/07/new-linux-variant-of-play-ransomware.html)

**Jul 22, 2024**Ravie LakshmananLinux / Ransomware

[![Linux Play Ransomware](data:image/png;base64... "Linux Play Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiN1EpNr2IixAgc9YAuhAUOoVi8puDrTI7yCDJkTDOAxO9ga_GwMQGZHHnu8bPiUGzum-GvdWnAdUDzqbS4ghaFOjBSfni8OAgfP_RjgSnORDY4TMqsgyriCr9RUa-lsAgEmq2SOG8gi5F_O-l6xZdF6Ab94uiiJfbnhuZCeO4lFJqR-x9ZBZcOi-njpp1X/s790-rw-e365/linux.png)

Cybersecurity researchers have discovered a new Linux variant of a ransomware strain known as [Play](https://thehackernews.com/2023/12/double-extortion-play-ransomware.html) (aka Balloonfly and PlayCrypt) that's designed to target VMware ESXi environments.

"This development suggests that the group could be broadening its attacks across the Linux platform, leading to an expanded victim pool and more successful ransom negotiations," Trend Micro researchers [said](https://www.trendmicro.com/en_us/research/24/g/new-play-ransomware-linux-variant-targets-esxi-shows-ties-with-p.html) in a report published Friday.

Play, which arrived on the scene in June 2022, is known for its double extortion tactics, encrypting systems after exfiltrating sensitive data and demanding payment in exchange for a decryption key. According to estimates released by Australia and the U.S., as many as 300 organizations have been victimized by the ransomware group as of October 2023.

Statistics shared by Trend Micro for the first seven months of 2024 show that the U.S. is the country with the highest number of victims, followed by Canada, Germany, the U.K., and the Netherlands.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Manufacturing, professional services, construction, IT, retail, financial services, transportation, media, legal services, and real estate are some of the top industries affected by the Play ransomware during the time period.

The cybersecurity firm's analysis of a Linux variant of Play comes from a RAR archive file hosted on an IP address (108.61.142[.]190), which also contains other tools identified as utilized in previous attacks such as PsExec, NetScan, WinSCP, WinRAR, and the Coroxy backdoor.

"Though no actual infection has been observed, the command-and-control (C&C) server hosts the common tools that Play ransomware currently uses in its attacks," it said. "This could denote that the Linux variant might employ similar tactics, techniques, and procedures (TTPs)."

The ransomware sample, upon execution, ensures that it's running in an ESXi environment before proceeding to encrypt virtual machine (VM) files, including VM disk, configuration, and metadata files, and appending them with the extension ".PLAY." A ransom note is then dropped in the root directory.

Further analysis has determined that the Play ransomware group is likely using the services and infrastructure peddled by [Prolific Puma](https://thehackernews.com/2023/11/dns-abuse-exposes-prolific-pumas.html), which offers an illicit link-shortening service to other cybercriminals to help them evade detection while distributing malware.

[![RDGAs](data:image/png;base64... "RDGAs")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5KK90o_FpqxcfckghxWZVXnlmypHSXdOGiBl4uAXFBcHu7F_Gap9nVr1t5jVZfBdYP7rOg79nVDIMXr5JagIPAc5Jzg5oiWC0ASuyNarir0b6b2GywoH7KEVF0lmGJHr1YBPQ_NVFHjsdBJskJPBzvqV3SuIzDyjx8hWlIdz8krH4IjigzIFhovbYQoOo/s790-rw-e365/dga.png)

Specifically, it employs what's called a registered domain generation algorithm (RDGA) to spin up new domain names, a programmatic mechanism that's increasingly being used by several threat actors, including [VexTrio Viper](https://thehackernews.com/2024/01/vextrio-uber-of-cybercrime-brokering.html) and Revolver Rabbit, for phishing, spam, and malware propagation.

Revolver Rabbit, for instance, is believed to have registered over 500,000 domains on the ".bond" top-level domain (TLD) at an approximate cost of more than $1 million, leveraging them as active and decoy C2 servers for the [XLoader](https://thehackernews.com/2023/08/new-variant-of-xloader-macos-malware.html) (aka FormBook) stealer malware.

"The most common RDGA pattern this actor uses is a series of one or more dictionary words followed by a five-digit number, with each word or number separated by a dash," Infoblox [noted](https://blogs.infoblox.com/threat-intelligence/rdgas-the-next-chapter-in-domain-generation-algorithms/) in a recent analysis. "Sometimes the actor uses ISO 3166-1 country codes, full country names, or numbers corresponding to years instead of dictionary words."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

RDGAs are a lot more challenging to detect and defend against than traditional DGAs owing to the fact that they allow threat actors to generate many domain names to register them for use – either all at once or over time – in their criminal infrastructure.

"In an RDGA, the algorithm is a secret kept by the threat actor, and they register all the domain names," Infoblox said. "In a traditional DGA, the malware contains an algorithm that can be discovered, and most of the domain names will not be registered. While DGAs are used exclusively for connection to a malware controller, RDGAs are used for a wide range of malicious activity."

The latest findings indicate a potential collaboration between two cybercriminal entities, suggesting that the Play ransomware actors are taking steps to bypass security protocols through Prolific Puma's services.

"ESXi environments are high-value targets for ransomware attacks due to their critical role in business operations," Trend Micro concluded. "The efficiency of encrypting numerous VMs simultaneously and the valuable data they hold further elevate their lucrativeness for cybercriminals."

Found this article interesting? Follow us on [Google News](https://news.google.com...