---
title: Credential Theft and Remote Access Surge as AllaKore, PureRAT, and Hijack Loader Proliferate
url: https://thehackernews.com/2025/07/credential-theft-and-remote-access.html
source: The Hacker News
date: 2025-07-23
fetch_date: 2025-10-06T23:55:41.295429
---

# Credential Theft and Remote Access Surge as AllaKore, PureRAT, and Hijack Loader Proliferate

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

# [Credential Theft and Remote Access Surge as AllaKore, PureRAT, and Hijack Loader Proliferate](https://thehackernews.com/2025/07/credential-theft-and-remote-access.html)

**Jul 22, 2025**Ravie LakshmananFinancial Fraud / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhgFCHPT2_DXUO_0lXIgxT25WAG3EGxxSfCupaOaYjg_ni3kJ9UQX7RNd_5h501oyXIc2YbQsfgGhpMoS00qSUhatBir3egSc23UaTC6PjlVKI4gtT0zbnF47pd6vQgXeo_XcgpOePewXloR6zKGR5vLFmMEgUv62bC1olfRUgOF6N9hFv_XVleQm8a93Bl/s790-rw-e365/rat-malware.jpg)

Mexican organizations are still being targeted by threat actors to deliver a modified version of AllaKore RAT and SystemBC as part of a long-running campaign.

The activity has been attributed by Arctic Wolf Labs to a financially motivated hacking group called **Greedy Sponge**. It's believed to be active since early 2021, indiscriminately targeting a wide range of sectors, such as retail, agriculture, public sector, entertainment, manufacturing, transportation, commercial services, capital goods, and banking.

"The AllaKore RAT payload has been heavily modified to enable the threat actors to send select banking credentials and unique authentication information back to their command-and-control (C2) server, for the purpose of conducting financial fraud," the cybersecurity company [said](https://arcticwolf.com/resources/blog/greedy-sponge-targets-mexico-with-allakore-rat-and-systembc/) in an analysis published last week.

Details of the campaign were [first documented](https://thehackernews.com/2024/01/allakore-rat-malware-targeting-mexican.html) by the BlackBerry Research and Intelligence Team (which is now part of Arctic Wolf) in January 2024, with the attacks employing phishing or drive-by compromises to distribute booby-trapped ZIP archives that ultimately facilitate the deployment of AllaKore RAT.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Attack chains analyzed by Arctic Wolf show that the remote access trojan is designed to optionally deliver secondary payloads like [SystemBC](https://thehackernews.com/2024/01/systembc-malwares-c2-server-analysis.html), a [C-based malware](https://www.bitsight.com/blog/systembc-multipurpose-proxy-bot-still-breathes) that turns compromised Windows hosts into [SOCKS5 proxies](https://news.sophos.com/en-us/2020/12/16/systembc/) to allow attackers to communicate with their C2 servers.

Besides dropping potent proxy tools, Greedy Sponge has also refined and updated its tradecraft to incorporate improved geofencing measures as of mid-2024 in an attempt to thwart analysis.

"Historically, geofencing to the Mexican region took place in the first stage, via a .NET downloader included in the trojanized Microsoft software installer (MSI) file," the company said. "This has now been moved server-side to restrict access to the final payload."

The latest iteration sticks to the same approach as before, distributing ZIP files ("Actualiza\_Policy\_v01.zip") containing a legitimate Chrome proxy executable and a trojanized MSI file that's engineered to drop [AllaKore RAT](https://thehackernews.com/2023/05/sidecopy-using-action-rat-and-allakore.html), a malware with capabilities for keylogging, screenshot capture, file download/upload, and remote control.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgiu43TIPwPOHpkVKZKAL9D7x05WVu9LpIcKM2Ejab9mgO6XYdQHF-mocL4u71a4CkELOVMIwsnjYmkQUGvfsT1PSsfPnH_Qi9q1yvLTYqIhzCAcGMyMtYJ7PyEYz57VbtkLU1AGoebzcxwsETPYzGsnxZv2oR1LIcGOMFBHuzTVF66hcaxUL2GXn7xX4-L/s790-rw-e365/comapre.png)

The MSI file is configured to deploy a .NET downloader, which is responsible for retrieving and launching the remote access trojan from an external server ("manzisuape[.]com/amw"), and a PowerShell script for cleanup actions.

This is not the first time AllaKore RAT has been used in attacks targeting Latin America. In May 2024, HarfangLab and Cisco Talos [revealed](https://thehackernews.com/2024/05/brazilian-banks-targeted-by-new.html) that an AllaKore variant known as AllaSenha (aka CarnavalHeist) has been used to single out Brazilian banking institutions by threat actors from the country.

"Having spent those four years-plus actively targeting Mexican entities, we would deem this threat actor persistent, but not particularly advanced," Arctic Wolf said. "The strictly financial motivation of this actor coupled with their limited geographic targeting is highly distinctive."

"Additionally, their operational longevity points to probable operational success – meaning they've found something that works for them, and they are sticking with it. Greedy Sponge has held the same infrastructure models for the duration of their campaigns."

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhC9-bwaNEbL2AiaVzxjZi9hEQ5fBKWGCZjoCwUGlu_8-iXXfKK3DyW1hfZct_emyFbVqU0KtD9W5tfLySwB5JV8Ql47Q3TkJgCfxWFICzc_uPvHTwnscSJsLo01ULzPbCAVFtdxkJQGiQiIDVzvrsE_rCNvcSjs-Ae84q2beLzpQ1nJgnmyv2AKXA2DMJD/s790-rw-e365/Ghost.png) |
| Attack Flow of Campaign Using Ghost Crypt |

The development comes as eSentire detailed a May 2025 phishing campaign that employed a new [crypter-as-a-service](https://thehackernews.com/2023/05/acecryptor-cybercriminals-powerful.html) offering known as Ghost Crypt to deliver and run [PureRAT](https://thehackernews.com/2025/05/purerat-malware-spikes-4x-in-2025.html).

"Initial access was gained through social engineering, where the threat actor impersonated a new client and sent a PDF containing a link to a Zoho WorkDrive folder containing malicious zip files," the Canadian company [noted](https://www.esentire.com/blog/ghost-crypt-powers-purerat-with-hypnosis). "The attacker also created a sense of urgency by calling the victim and requesting that they extract and execute the file immediately."

Further examination of the attack chain has revealed that the malicious file contains a DLL payload that's encrypted with Gho...