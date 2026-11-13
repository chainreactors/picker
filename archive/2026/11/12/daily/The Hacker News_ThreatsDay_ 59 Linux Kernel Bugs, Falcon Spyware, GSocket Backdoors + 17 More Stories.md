---
title: ThreatsDay: 59 Linux Kernel Bugs, Falcon Spyware, GSocket Backdoors + 17 More Stories
url: https://thehackernews.com/2026/11/threatsday-59-linux-kernel-bugs-falcon.html
source: The Hacker News
date: 2026-11-12
fetch_date: 2026-11-13T09:07:44.639861
---

# ThreatsDay: 59 Linux Kernel Bugs, Falcon Spyware, GSocket Backdoors + 17 More Stories

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueiGhtTJ4g8vfPjVOP22mnT6eczZI-CgiOkXQ_Zv0gVno2MkG5UlOExxvSSAylm8NAtCfFkeaPxbyR3vYtpyOVi9ROWrrVZ9FKHFBH1IrQCCR46b2kh7JNKxenqefzCkCUewWhqRlds-IYjwzH7N7iWGpXxzeqhS6vIHDWIohTDx2ZZZReOOwVWv-SAmG/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-infographic-d)

# [ThreatsDay: 59 Linux Kernel Bugs, Falcon Spyware, GSocket Backdoors + 17 More Stories](https://thehackernews.com/2026/11/threatsday-59-linux-kernel-bugs-falcon.html)

**Ravie Lakshmanan**Nov 12, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhpHFMwpmKB3Mn6eMpEHMAX_8gqnyi4xwTCuYj7NTrCcTMWAsSZtaUsHYUa1kvi3jQf92A5pR_Qz7kzgTarHmo6q6YsXVeVSJEkkx0JkioCXa6GbKJzG9eZz0dkotf9QEpdcRMy94hoYhGfIoEk7pPOFUSgTY5ciU7_wkSOJc7kgXcS1GS3qGC-Ql7kMrks/s1700-nu-rw-lo-l85-e365/thd.jpg)

A search result isn't always safe. An access request isn't always harmless. And a familiar account doesn't always mean a familiar person is using it. Simple things to remember. Yet a surprising amount of this week's trouble starts right there.

Attackers are using fake websites, stolen access, and trusted tools to get into places they shouldn't be. AI is helping them build attacks faster, while also giving them new systems to target. Some intruders are staying hidden even after security holes are fixed. Others are moving stolen money through a maze of transactions. And researchers keep finding small coding mistakes that can cause much bigger problems. Different stories, but much of the trouble comes down to making something dangerous look normal.

There is some good news, too. Criminal servers have been seized, and a few defenses are getting stronger. Still, plenty of things are going wrong in ways that shouldn't be this easy. Here's what turned up this week.

**The threats change every week. Subscribe, and we’ll alert you when each new ThreatsDay Bulletin is out.**

1. North Korea's crypto laundering network

   [How North Korea Is Laundering $6.4B Stolen from Binance](https://www.elliptic.co/insights/how-north-korea-is-laundering-the-6-4-billion-stolen-from-binance/)

   The North Korean threat actors linked to the [record-breaking theft of $6.43 billion](https://thehackernews.com/2026/11/binance-reveals-how-fake-job-interviews.html) from Binance are using a highly complex and clearly automated method to launder the illicit proceeds. "Since the theft it has used more than 20,000 wallets on 16 blockchains, at least 36 services and at least 65,000 transactions," Dr. Tom Robinson, Elliptic's founder and chief scientist, [said](https://www.elliptic.co/insights/how-north-korea-is-laundering-the-6-4-billion-stolen-from-binance/). "Around $3.0 billion remains in addresses linked to the theft, mostly as ETH and BTC. A negligible amount has likely been cashed out." The attackers have also been observed [creating six meme coins](https://www.elliptic.co/insights/north-korea-meme-coins-binance-hack/) on the NEAR blockchain network (FUK, OLCCL, MEILI, MMLI, DABI, and SINU) to launder a slice of the ill-gotten funds, passing through about $430,000 of the stolen cryptocurrency. The goal is to disguise the path of money and make it harder to trace where the assets eventually end up. Other tactics used to make funds tracing more difficult include moving between blockchains through bridges and cross-chain swap services, swapping between assets on DEXs, hopping through lending vaults and liquid-staking services, and mixing bitcoin through coinjoins, and ETH and SOL through the Privacy Cash privacy pool. The Binance breach is by no means the first to affect a major cryptocurrency exchange, but it is the biggest ever by magnitude. North Korean spokesperson Kim Yo Jong [denied](https://kcnawatch.org/newstream/1793655240-736016532/press-statement-of-kim-yo-jong-department-director-of-c-c-wpk/) the country's role in the attack, calling it an "absurd" effort to "damage the international image of the DPRK."

   [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQl2mj4ZaDqjSfeRZqNw5CHDIIW4zqatYMtChfMxybdcNrZJgSihO0Mvs6jbraOYdHcGhYe7tY3dYAiEO5KuW3pmqkE_ur62woJRIFczinZ3GSx71PEwskKyNjWdgkSf2RprrQQ7a9TBz18oBGaVtD8AaHgd02kXXgR0dU22dzOg3lrnKprJHWtAcj8PkT/s1700-nu-rw-lo-l85-e365/stolen.jpg)
2. GSocket detections surge 356%

   [Attacks Leveraging GSocket Spike in 2026](https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/)

   Microsoft said it has observed multiple incidents in which threat actors deployed [GSocket](https://github.com/hackerschoice/gsocket), an open-source remote access tool, on internet-facing Linux servers to maintain access after the original vulnerabilities were addressed, turning a single web application compromise into persistent access. "Because GSocket relays traffic through a shared public network, there is no threat actor-owned IP address or domain to block," Microsoft [said](https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/). "Defenders should look for GSocket deployment, persistence, privilege escalation, and outbound connections on affected hosts, not treat application patching alone as complete remediation." According to telemetry data, devices with GSocket-related detections increased 356.2% from March through August 2026, with most of them associated with PHP web applications, cPanel hosts, and Apache. The majority of targets of GSocket activity are in the education and research sector, followed by technology and communications, manufacturing, and government entities.
3. 235 servers seized in Europol takedown

   [Europol Operation Dismantles GootLoader, CastleRAT, and StealC Infrastructure](https://www.europol.europa.eu/media-press/newsroom/news/64-million-victim-datasets-secured-in-international-operation-against-malware-networks)

   Europol, along with global partners, has disrupted the criminal infrastructure behind [GootLoader](https://thehackernews.com/2022/01/gootloader-hackers-targeting-employees.html), [CastleRAT](https://thehackernews.com/2025/09/tag-150-develops-castlerat-in-python.html), and [StealC](https://thehackernews.com/2023/02/researchers-discover-dozens-samples-o...