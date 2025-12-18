---
title: Kimwolf Botnet Hijacks 1.8 Million Android TVs, Launches Large-Scale DDoS Attacks
url: https://thehackernews.com/2025/12/kimwolf-botnet-hijacks-18-million.html
source: The Hacker News
date: 2025-12-17
fetch_date: 2025-12-18T03:21:10.064210
---

# Kimwolf Botnet Hijacks 1.8 Million Android TVs, Launches Large-Scale DDoS Attacks

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [Kimwolf Botnet Hijacks 1.8 Million Android TVs, Launches Large-Scale DDoS Attacks](https://thehackernews.com/2025/12/kimwolf-botnet-hijacks-18-million.html)

**Dec 17, 2025**Ravie LakshmananInternet of Things / Botnet

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj6-q5Xa6KgWXYqaE_Gb7hCK-lfm5MRlkicK1xFVL8HwS5-jHv0MAY5YYAyTmuRfITo4hEjKmhAnfXMpWLSpqS5jQkSMFVw2DSPnu_CvTCpwTrFBUwN_wWoPF8NqrPJo7GR7cUYEQ4AIz339JY4MqyGx6OZk7GQih_fGBPu9S5RrYPXSMRbnRHuJnhNEQa5/s790-rw-e365/android-tvs.jpg)

A new distributed denial-of-service (DDoS) botnet known as **Kimwolf** has enlisted a massive army of no less than 1.8 million infected devices comprising Android-based TVs, set-top boxes, and tablets, and may be associated with another botnet known as [AISURU](https://thehackernews.com/2025/12/record-297-tbps-ddos-attack-linked-to.html), according to findings from QiAnXin XLab.

"Kimwolf is a botnet compiled using the [NDK](https://developer.android.com/ndk) [Native Development Kit]," the company [said](https://blog.xlab.qianxin.com/kimwolf-botnet-en/) in a report published today. "In addition to typical DDoS attack capabilities, it integrates proxy forwarding, reverse shell, and file management functions."

The hyper-scale botnet is estimated to have issued 1.7 billion DDoS attack commands within a three-day period between November 19 and 22, 2025, around the same time one of its command-and-control (C2) domains – 14emeliaterracewestroxburyma02132[.]su – [came first](https://thehackernews.com/2025/11/weekly-recap-fortinet-exploit-chrome-0.html#:~:text=environments.-,Microsoft%20Mitigates%20Record%2015.72%20Tbps%20DDoS%20Attack) in Cloudflare's list of top 100 domains, briefly even surpassing Google.

Kimwolf's primary infection targets are TV boxes deployed in residential network environments. Some of the affected device models include TV BOX, SuperBOX, HiDPTAndroid, P200, X96Q, XBOX, SmartTV, and MX10. Infections are scattered globally, with Brazil, India, the U.S., Argentina, South Africa, and the Philippines registering higher concentrations. That said, the exact means by which the malware is propagated to these devices is presently unclear.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/windows-stealer-alert-d)

XLab said its investigation into the botnet commenced after it received a "version 4" artifact of Kimwolf from a trusted community partner on October 24, 2025. Since then, an additional eight samples were discovered last month.

"We observed that Kimwolf's C2 domains have been successfully taken down by unknown parties at least three times [in December], forcing it to upgrade its tactics and turn to using ENS (Ethereum Name Service) to harden its infrastructure, demonstrating its powerful evolutionary capability," XLab researchers said.

That's not all. Earlier this month, XLab managed to successfully seize control of one of the C2 domains, enabling it to assess the scale of the botnet.

An interesting aspect of Kimwolf is that it's tied to the infamous AISURU botnet, which has been behind some of the record-breaking DDoS attacks over the past year. It's suspected that the attackers reused code from AISURU in the early stages, before opting to develop the Kimwolf botnet to evade detection.

XLab said it's possible some of these attacks may not have come from AISURU alone, and that Kimwolf may be either participating or even leading the efforts.

"These two major botnets propagated through the same infection scripts between September and November, coexisting in the same batch of devices," the company said. "They actually belong to the same hacker group."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgoagCiQreHKCPg3bAeEHen4IRoTL2DCeq55mXbawbXrEc6Fnrj2GQvMWvHBpcPCe9EB0w9zxiZp8q7WF-Qk7INgdYEMm4z-oKgFw7RFeK322l9WGLvqVXEY6h5zAyVREbrYNf0maaBLyDTcBK_ZBwrVHOjLH8CjdPDAX2IAMEsbPxHDny8QyoAwUYZIjH2/s790-rw-e365/kim.png)

This assessment is based on [similarities](https://www.virustotal.com/gui/file/84cf4aac1e063394be3be68fea3cb9526e567c0aeaaf39b4834411970c00921e) in APK packages uploaded to the VirusTotal platform, in [some cases](https://www.virustotal.com/gui/file/750a3e2ab2941705672cbeb6ec4d265e7ed79f21a18371de0c960a873b8cbbfd) even using the [same code signing certificate](https://www.virustotal.com/gui/file/77366b3b2dc016fea0f8461a1cb06e089b9186059a73d67e6ba28d088c06431d) ("John Dinglebert Dinglenut VIII VanSack Smith"). Further definitive evidence arrived on December 8, 2025, with the discovery of an active downloader server ("93.95.112[.]59") that contained a script referencing APKs for both Kimwolf and AISURU.

The malware in itself is fairly straightforward. Once launched, it ensures that only one instance of the process runs on the infected device, and then proceeds to decrypt the embedded C2 domain, uses DNS-over-TLS to obtain the C2 IP address, and connects to it in order to receive and execute commands.

Recent versions of the botnet malware detected as recently as December 12, 2025, have introduced a technique known as [EtherHiding](https://thehackernews.com/2025/10/hackers-abuse-blockchain-smart.html) that makes use of an ENS domain ("pawsatyou[.]eth") to fetch the actual C2 IP from the associated smart contract ([0xde569B825877c47fE637913eCE5216C644dE081F](https://etherscan.io/address/0xde569B825877c47fE637913eCE5216C644dE081F)) in an effort to render its infrastructure more resilient to takedown efforts.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

Specifically, this involves extracting an IPv6 address from the ["lol" field of the transaction](https://etherscan.io/tx/0xac165115069ea91503c29af14322cf84cbd39133bb59a447c2aa704999cd334f), then taking the last four bytes of the address and performing an XOR operation with the key "0x93141715" to get the actual IP address.

Besides encrypting sensitive data related to C2 servers and DNS resolvers, Kimwolf uses TLS encryption for network communicat...