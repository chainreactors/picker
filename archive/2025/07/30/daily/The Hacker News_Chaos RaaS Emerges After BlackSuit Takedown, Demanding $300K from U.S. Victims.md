---
title: Chaos RaaS Emerges After BlackSuit Takedown, Demanding $300K from U.S. Victims
url: https://thehackernews.com/2025/07/chaos-raas-emerges-after-blacksuit.html
source: The Hacker News
date: 2025-07-30
fetch_date: 2025-10-06T23:57:40.304404
---

# Chaos RaaS Emerges After BlackSuit Takedown, Demanding $300K from U.S. Victims

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

# [Chaos RaaS Emerges After BlackSuit Takedown, Demanding $300K from U.S. Victims](https://thehackernews.com/2025/07/chaos-raas-emerges-after-blacksuit.html)

**Jul 29, 2025**Ravie LakshmananRansomware / Cybercrime

[![Chaos RaaS](data:image/png;base64... "Chaos RaaS")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjj4Zcja37l0T66AY6zMHOoBDRmMLQMZZrstpAfJEO-1ZEVlyj4dBOEnhFQtZYhTWeFRKODouDBlJEcKpcwGLMs0KOO4SF-hXTYXuAbpkoOZBQR88_PlUi6FbAux1cieN2zA3kPjVmcALyCU0AP-4P5A0XEeqUQGtFM67mjXsbKC8B92LdDSQkrLKD8m473/s790-rw-e365/ransomware-malware.jpg)

A newly emerged ransomware-as-a-service (RaaS) gang called Chaos is likely made up of former members of the [BlackSuit crew](https://thehackernews.com/2024/08/fbi-and-cisa-warn-of-blacksuit.html), as the latter's dark web infrastructure has been the subject of a law enforcement seizure.

Chaos, which sprang forth in February 2025, is the latest entrant in the ransomware landscape to conduct big-game hunting and double extortion attacks.

"Chaos RaaS actors initiated low-effort spam flooding, escalating to voice-based social engineering for access, followed by RMM tool abuse for persistent connection and legitimate file-sharing software for data exfiltration," Cisco Talos researchers Anna Bennett, James Nutland, and Chetan Raghuprasad [said](https://blog.talosintelligence.com/new-chaos-ransomware/).

"The ransomware utilizes multi-threaded rapid selective encryption, anti-analysis techniques, and targets both local and network resources, maximizing impact while hindering detection and recovery."

It's important to note here that the ransomware group is unrelated to the Chaos ransomware builder variants such as [Yashma](https://thehackernews.com/2022/05/new-chaos-ransomware-builder-variant.html) and [Lucky\_Gh0$t](https://thehackernews.com/2025/05/cybercriminals-target-ai-users-with.html), indicating that the threat actors are using the same name to sow confusion. A majority of the victims are located in the United States, based on [data](https://www.ransomware.live/group/chaos) from Ransomware.live.

Compatible with Windows, ESXi, Linux, and NAS systems, Chaos has been observed seeking ransoms of $300,000 from victims in exchange for a decryptor and a "detailed penetration overview with main kill chain and security recommendations."

The attacks involve a combination of phishing and voice phishing techniques to obtain initial access by tricking victims into installing remote desktop software, particularly [Microsoft Quick Assist](https://thehackernews.com/2024/05/cybercriminals-exploiting-microsofts.html).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The threat actors subsequently carry out post-compromise discovery and reconnaissance, followed by installing other RMM tools such as AnyDesk, ScreenConnect, OptiTune, Syncro RMM, and Splashtop to establish persistent remote access to the network.

Also undertaken are steps to harvest credentials, delete PowerShell event logs, and delete security tools installed on the machine to undermine detection. The attacks culminate with the deployment of the ransomware, but not before lateral movement and data exfiltration using GoodSync.

The ransomware binary supports multithreading to facilitate rapid encryption of both local and network resources, all while blocking recovery efforts and implementing multi-layered anti-analysis techniques to evade debugging tools, virtual machine environments, automated sandboxes, and other security platforms.

The links to BlackSuit stem from similarities in the tradecraft employed, including in the encryption commands, the theme and structure of the ransom note, and the RMM tools used. It's worth noting that BlackSuit is a rebrand of the Royal ransomware group, which, in itself, was an offshoot of Conti, highlighting the shape-shifting nature of the threat.

The development comes around the same time BlackSuit's dark web sites were seized as part of a joint law enforcement effort called Operation Checkmate. Visitors are greeted by a splash screen that states, "This site has been seized by U.S. Homeland Security Investigations as part of a coordinated international law enforcement investigation." There has been no official statement from authorities on the takedown.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5xGXRNN8I9iY4SOhGp6YvNb38fsZWCg5uUtqX77TG4LMDPllTT7obtSJsmMCVWGbjibvDNH_PFtS8q-UQFvlOo4jtJ1kFiozvYQLIEWdXvYp2SCsflw321qdlcNQ2g4fb8TotUc8RVl3pI7qXw0Wo5nFTujVZYSJReZv6Mq8P3zxRvlBejZVBqlGmLSoN/s790-rw-e365/ransomware.jpeg)

Romanian cybersecurity company Bitdefender, which offered expert assistance to law enforcement, [said](https://www.bitdefender.com/en-us/blog/businessinsights/blacksuit-ransomware-seized-takedown) BlackSuit has claimed over 185 victims since it surfaced in the summer of 2023, describing it as a private ransomware group without relying on affiliates to carry out the attacks.

Attacks orchestrated by BlackSuit are both sophisticated and go through several stages, adopting a [hybrid approach](https://www.cybereason.com/blog/blacksuit-data-exfil) to data encryption and data deletion, and giving them the ability to "decide a specific percentage of data to encrypt" as well as speed up the process.

"The disruption of BlackSuit's infrastructure marks another important milestone in the fight against organized cybercrime," a representative of the Draco Team, Bitdefender's cybercrime unit who participated in the takedown, told The Hacker News.

"We commend our law enforcement partners for their coordination and determination. Operations like this reinforce the critical role of public-private partnerships in tracking, exposing, and ultimately dismantling ransomware groups that operate in the shadows. When global expertise is aligned, cybercriminals have fewer places to hide."

In a related move, the U.S. Federal Bureau of Investigation (FBI) and the Department of Justice (DoJ) [publicly](https:/...