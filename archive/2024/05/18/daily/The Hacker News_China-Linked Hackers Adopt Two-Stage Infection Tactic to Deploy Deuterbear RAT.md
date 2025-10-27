---
title: China-Linked Hackers Adopt Two-Stage Infection Tactic to Deploy Deuterbear RAT
url: https://thehackernews.com/2024/05/china-linked-hackers-adopt-two-stage.html
source: The Hacker News
date: 2024-05-18
fetch_date: 2025-10-06T16:52:53.966879
---

# China-Linked Hackers Adopt Two-Stage Infection Tactic to Deploy Deuterbear RAT

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

# [China-Linked Hackers Adopt Two-Stage Infection Tactic to Deploy Deuterbear RAT](https://thehackernews.com/2024/05/china-linked-hackers-adopt-two-stage.html)

**May 17, 2024**Ravie LakshmananMalware / Artificial Intelligence

[![Deuterbear RAT](data:image/png;base64... "Deuterbear RAT")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjd44DTDc43zIEkapTS7x1xzyCuyAq_BI-BiV3FPnh7kVYP1TcsOx6e8Vrbg1HCEfH5WSLrvA5nQqj6MuOxwidV_Z932WsQP4IY4evbsueNrOTCA41v9AK8CSs7sEGvsiLkFMK9y_wVU6sMKHy3ga73CEwIJjnJjLdbfBUD2QihTjVvHBxrbWQXpYfiiNKn/s790-rw-e365/cyber.jpg)

Cybersecurity researchers have shed more light on a remote access trojan (RAT) known as Deuterbear used by the China-linked **BlackTech** hacking group as part of a cyber espionage campaign targeting the Asia-Pacific region this year.

"Deuterbear, while similar to Waterbear in many ways, shows advancements in capabilities such as including support for shellcode plugins, avoiding handshakes for RAT operation, and using HTTPS for C&C communication," Trend Micro researchers Pierre Lee and Cyris Tseng [said](https://www.trendmicro.com/en_us/research/24/e/earth-hundun-2.html) in a new analysis.

"Comparing the two malware variants, Deuterbear uses a shellcode format, possesses anti-memory scanning, and shares a traffic key with its downloader unlike Waterbear."

[BlackTech](https://thehackernews.com/2024/04/blacktech-targets-tech-research-and-gov.html), active since at least 2007, is also tracked by the broader cybersecurity community under the monikers Circuit Panda, Earth Hundun, HUAPI, Manga Taurus, Palmerworm, Red Djinn, and Temp.Overboard.

Cyber attacks [orchestrated by the group](https://thehackernews.com/2020/09/chinese-apt-group-targets-media-finance.html) have long involved the deployment of a malware called Waterbear (aka DBGPRINT) for nearly 15 years, although campaigns observed since October 2022 have also utilized an updated version called Deuterbear.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Waterbear is delivered by means of a patched legitimate executable, which leverages DLL side-loading to launch a loader that then decrypts and executes a downloader, which subsequently contacts a command-and-control (C&C) server to retrieve the RAT module.

Interestingly, the RAT module is fetched twice from the attacker-controlled infrastructure, the first of which is just used to load a Waterbear plugin that furthers the compromise by launching a different version of the Waterbear downloader to retrieve the RAT module from another C&C server.

Put differently, the first Waterbear RAT serves as a plugin downloader while the second Waterbear RAT functions as a backdoor, harvesting sensitive information from the compromised host through a set of 60 commands.

The infection pathway for Deuterbear is a lot similar to that of Waterbear in that it also implements two stages to install the RAT backdoor component, but also tweaks it to some extent.

The first stage, in this case, employs the loader to launch a downloader, which connects to the C&C server to fetch Deuterbear RAT, an intermediary that serves to establish persistence through a second-stage loader via DLL side-loading.

This loader is ultimately responsible for executing a downloader, which again downloads the Deuterbear RAT from a C&C server for information theft.

"In most of the infected systems, only the second stage Deuterbear is available," the researchers said. "All components of the first stage Deuterbear are totally removed after the 'persistence installation' is completed."

[![Deuterbear RAT](data:image/png;base64... "Deuterbear RAT")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQP9APziGfSgn7SWhyFK2kCmMrL0EHVBik_rSsU9fH5eO8dKp3wHU0ULqqlhtCv9Cb_ZFw_6i9tldKy-poQa73Iv8a-JgRPtLR-NLob5wd17bP-149CXiu22KKUcFRlc9ZIU0FtSzt9fy1miY3cUfvqtyuYAehyWNFb2ICg4allxT6GHulji57TFJXfZ5l/s790-rw-e365/fig-3.png)

"This strategy effectively protects their tracks and prevents the malware from easily being analyzed by threat researchers, particularly in simulated environments rather than real victim systems."

Deuterbear RAT is also a more streamlined version of its predecessor, retaining only a subset of the commands in favor of a plugin-based approach to incorporate more functionality.

"Waterbear has gone through continuous evolution, eventually giving rise to the emergence of a new malware, Deuterbear," Trend Micro said. "Interestingly, both Waterbear and Deuterbear continue to evolve independently, rather than one simply replacing the other."

### Targeted Campaign Delivers SugarGh0st RAT

The disclosure comes as Proofpoint detailed an "extremely targeted" cyber campaign targeting organizations in the U.S. that are involved in artificial intelligence efforts, including academia, private industry, and the government, to deliver a malware called SugarGh0st RAT.

The enterprise security company is tracking the emerging activity cluster under the name UNK\_SweetSpecter.

"SugarGh0st RAT is a remote access trojan, and is a customized variant of Gh0st RAT, an older commodity trojan typically used by Chinese-speaking threat actors," the company [said](https://www.proofpoint.com/us/blog/threat-insight/security-brief-artificial-sweetener-sugargh0st-rat-used-target-american). "SugarGh0st RAT has been historically used to target users in Central and East Asia."

SugarGh0st RAT was [first documented](https://thehackernews.com/2023/12/chinese-hackers-using-sugargh0st-rat-to.html) late last year by Cisco Talos in connection with a campaign targeting the Uzbekistan Ministry of Foreign Affairs and South Korean users since August 2023. The intrusions were attributed to a suspected Chinese-speaking threat actor.

The attack chains entail sending AI-themed phishing messages containing a ZIP archive that, in turn, packs a Windows shortcut file to deploy a JavaScript dropper responsible for launching the SugarGh0st payload.

[![CIS Build Kits](data:image/png;base64...)](https://...