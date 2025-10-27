---
title: Abandoned Sogou Zhuyin Update Server Hijacked, Weaponized in Taiwan Espionage Campaign
url: https://thehackernews.com/2025/08/abandoned-sogou-zhuyin-update-server.html
source: The Hacker News
date: 2025-08-30
fetch_date: 2025-10-07T00:50:22.124407
---

# Abandoned Sogou Zhuyin Update Server Hijacked, Weaponized in Taiwan Espionage Campaign

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

# [Abandoned Sogou Zhuyin Update Server Hijacked, Weaponized in Taiwan Espionage Campaign](https://thehackernews.com/2025/08/abandoned-sogou-zhuyin-update-server.html)

**Aug 29, 2025**Ravie LakshmananCyber Espionage / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlMjfZMk2hdkae7SCb_d4KXuVVEQG3TAO5supo1M2tdAMUJP8kB_XaGkiE4PjVqlZhmmSk3YzDMrq7RDlV305hbb6fHR_fO1UAwci4Z0uiRaOY6A5jT8Vl5UY75PcRF7UweNozMx5emwMi3APyplzQnam_LX_41ctl-ezhnddH95CSBctT7iQSEjkBqKiY/s790-rw-e365/server-update.png)

An abandoned update server associated with input method editor (IME) software Sogou Zhuyin was leveraged by threat actors as part of an espionage campaign to deliver several malware families, including C6DOOR and GTELAM, in attacks primarily targeting users across Eastern Asia.

"Attackers employed sophisticated infection chains, such as hijacked software updates and fake cloud storage or login pages, to distribute malware and collect sensitive information," Trend Micro researchers Nick Dai and Pierre Lee [said](https://www.trendmicro.com/en_us/research/25/h/taoth-campaign.html) in an exhaustive report.

The campaign, identified in June 2025, has been codenamed **TAOTH** by the cybersecurity company. Targets of the activity mainly include dissidents, journalists, researchers, and technology/business leaders in China, Taiwan, Hong Kong, Japan, South Korea, and overseas Taiwanese communities. Taiwan accounts for 49% of all targets, followed by Cambodia (11%) and the U.S. (7%).

It's said the attackers, in October 2024, took control of the lapsed domain name ("sogouzhuyin[.]com") associated with Sogou Zhuyin, a legitimate IME service that stopped receiving updates in June 2019, to disseminate malicious payloads a month later. It's estimated that several hundred victims were impacted.

"The attacker took over the abandoned update server and, after registering it, used the domain to host malicious updates since October 2024," the researchers said. "Through this channel, multiple malware families have been deployed, including GTELAM, C6DOOR, DESFY, and TOSHIS."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The deployed malware families serve different purposes, including remote access (RAT), information theft, and backdoor functionality. To evade detection, the threat actors also leveraged third-party cloud services to conceal their network activities across the attack chain.

These malware strains enable remote access, information theft, and backdoor functionality, with the attackers also using legitimate cloud storage services like Google Drive as a data exfiltration point and to conceal the malicious network traffic.

The attack chain begins when unsuspecting users download the official installer for Sogou Zhuyin from the Internet, such as the [Traditional Chinese Wikipedia page entry](https://zh.wikipedia.org/w/index.php?title=%E6%90%9C%E7%8B%97%E8%BE%93%E5%85%A5%E6%B3%95%E6%B3%A8%E9%9F%B3%E7%89%88&oldid=82318029) for Sogou Zhuyin, which, in March 2025, was modified to point users to the malicious domain dl[.]sogouzhuyin[.]com.

While the installer is completely innocuous, the malicious activity kicks in when the automatic update process is triggered a couple of hours after installation, causing the updater binary, "ZhuyinUp.exe," to fetch an update configuration file from an embedded URL: "srv-pc.sogouzhuyin[.]com/v1/upgrade/version."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUFEKA6MgbkUOaQLlLaG2ViH5A5fFyCHRZQ-CTuBVhplPsJgo4wOJdZ_ZPBx8E9vZ8y70cn9cgN9Hs62AhOeiZF2hTIxkmd7s6V-4Yp69QLc_5gL2r7U2NB98Ei7kJYMQjt7WhI6cMABVkOv3XPUB0nV9ojnH1x8Hwwi2ES_iGVNRxk3zM5xY_wEWkP1zn/s2600/map-1.png)

It's this update process that has been tampered with to DESFY, GTELAM, C6DOOR, and TOSHIS with the ultimate goal of profiling and gathering data from high-value targets -

* **TOSHIS** (First detected December 2024), a loader designed to fetch next-stage payloads (Cobalt Strike or Merlin agent for Mythic framework) from an external server. It's also a variant of [Xiangoop](https://malpedia.caad.fkie.fraunhofer.de/details/win.xiangoop), which has been attributed to [Tropic Trooper](https://thehackernews.com/2024/09/chinese-speaking-hacker-group-targets.html) and has been used to [deliver](https://blog-en.itochuci.co.jp/entry/2023/10/06/173200) Cobalt Strike or a backdoor called EntryShell in the past.
* **DESFY** (First detected May 2025), a spyware that collects file names from two locations: Desktop and Program Files
* **GTELAM** (First detected May 2025), another spyware that collects file names matching a specific set of extensions (PDF, DOC, DOCX, XLS, XLSX, PPT, and PPTX), and exfiltrates the details to Google Drive
* **C6DOOR**, a bespoke Go-based backdoor that uses HTTP and WebSocket protocols for command-and-control so as to receive instructions to gather system information, run arbitrary commands, perform file operations, upload/download files, capture screenshots, list running processes, enumerate directories, and inject shellcode into a targeted process

Further analysis of C6DOOR has uncovered the presence of embedded Simplified Chinese characters within the sample, suggesting that the threat actor behind the artifact may be proficient in Chinese.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"It appears that the attacker was still in the reconnaissance phase, primarily seeking high-value targets," Trend Micro said. "As a result, no further post-exploitation activities were observed in the majority of victim systems. In one of the cases we analyzed, the attacker was inspecting the victim's environment and establishing a tunnel using Visual Studio Code."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEge8UOr0l3y8P_AtlFlCJ6HLilDkr9TkJkFBWFfFaIfvWaa-m4jtnzPtuGV5XwPkns8nzgkdhhJZPIs_71u2WdDtXMu0Q56G44FZsxUCPhWPS8zOPucAmLT2I...