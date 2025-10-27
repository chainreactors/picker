---
title: Spacecolon Toolset Fuels Global Surge in Scarab Ransomware Attacks
url: https://thehackernews.com/2023/08/spacecolon-toolset-fuels-global-surge.html
source: The Hacker News
date: 2023-08-24
fetch_date: 2025-10-04T12:04:02.397107
---

# Spacecolon Toolset Fuels Global Surge in Scarab Ransomware Attacks

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

# [Spacecolon Toolset Fuels Global Surge in Scarab Ransomware Attacks](https://thehackernews.com/2023/08/spacecolon-toolset-fuels-global-surge.html)

**Aug 23, 2023**Ravie LakshmananRansomware / Malware

[![Scarab Ransomware Attacks](data:image/png;base64... "Scarab Ransomware Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxfDexMGGk_enSDrUQIoaHkPJQPCBZ3jMglUwpDKiHq5oWd6E1DMlzquKXeqXvEC-ieegaSBi7Fkv98OTAjV7V2wAhpuDuqpjciT1m_AQLdE4QV71suX3FWWuzCUHQ7lH4dCkZGWECL8wLNTi9syUPkUyPKJ-0_RJPNLS8Uy4ByFTAyie_tx6DI7KxFbES/s790-rw-e365/ransomware.jpg)

A malicious toolset dubbed **Spacecolon** is being deployed as part of an ongoing campaign to spread variants of the Scarab ransomware across victim organizations globally.

"It probably finds its way into victim organizations by its operators compromising vulnerable web servers or via brute forcing RDP credentials," ESET security researcher Jakub Souček [said](https://www.welivesecurity.com/en/eset-research/scarabs-colon-izing-vulnerable-servers/) in a detailed technical write-up published Tuesday.

The Slovak cybersecurity firm, which dubbed the threat actor CosmicBeetle, said the origins of the Spacecolon date back to May 2020. The highest concentration of victims has been detected in France, Mexico, Poland, Slovakia, Spain, and Turkey.

While the exact provenance of the adversary is unclear, several Spacecolon variants are said to contain Turkish strings, likely pointing to the involvement of a Turkish-speaking developer. There is no evidence currently linking it to any other known threat actor group.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Some of the targets include a hospital and a tourist resort in Thailand, an insurance company in Israel, a local governmental institution in Poland, an entertainment provider in Brazil, an environmental company in Turkey, and a school in Mexico.

"CosmicBeetle does not choose its targets; rather, it finds servers with critical security updates missing and exploits that to its advantage," Souček pointed out.

[![Scarab Ransomware](data:image/png;base64... "Scarab Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEghW1ikpNXGkvUUpauc15KeHkK3plWLexhKXTz1WE5ZWSM9gDtsZtnIgsBV_l9Mdl7UWtNYOMOjKxWjegnMOHQfyNrC6y1SbIxVElbo2QWgXFDbSCxq-YOkgg1FKRg6Q3-OQ3slTNXm1KxUCJxl9t9MOGnR5Hmy8g71FoeGOFDVU0dNBAC-QiRwryaQ_7iV/s790-rw-e365/exploit.jpg)

It's worth noting that Spacecolon was [first documented](https://zaufanatrzeciastrona.pl/post/kiedy-nawet-dobry-edr-nie-wystarcza-case-study-prawie-udanego-ataku-z-polskiej-firmy/) by Polish company Zaufana Trzecia Strona in early February 2023, likely prompting the adversary to tweak its arsenal in response to public disclosures.

The primary component of Spacecolon is ScHackTool, a Delphi-based orchestrator that's used to deploy an installer, which, as the name implies, installs ScService, a backdoor with features to execute custom commands, download and execute payloads, and retrieve system information from compromised machines.

ScHackTool also functions as a conduit to set up a wide array of third-party tools fetched from a remote server (193.149.185[.]23). The ultimate goal of the attacks is to leverage the access afforded by ScService to deliver a variant of the [Scarab ransomware](https://malpedia.caad.fkie.fraunhofer.de/details/win.scarab_ransom).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

An alternate version of the infection chain identified by ESET entails the use of [Impacket](https://github.com/fortra/impacket) to deploy ScService as opposed to using ScHackTool, indicating that the threat actors are experimenting with different methods.

CosmicBeetle's financial motives are further bolstered by the fact that the ransomware payload also drops a clipper malware to keep tabs on the system clipboard and modify cryptocurrency wallet addresses to those under the attacker's control.

[![Scarab Ransomware](data:image/png;base64... "Scarab Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyJe2rG36VJMDFv3Gw4bcPD-2RgbgEVJ_iNz1qeWpwV_gl9Y4aOE7qnb2u0bW8rhT0Vo0XDql-_nc28N-hWj-g_AD2qnOI3PXOO2QOQ-ymPIfbi47kohtTlc_iGI7sx_fqBAt34uAlgZHKY3ciOxrDRvQmVfm_qNbcO3Lz4PrxtSy86_Hditz1lbU5BAT7/s790-rw-e365/728.jpg)

Furthermore, there is evidence that the adversary is actively developing a new ransomware strain dubbed ScRansom, which attempts to encrypt all hard, removable, and remote drives using the [AES-128](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) algorithm with a key generated from a hard-coded string.

"CosmicBeetle doesn't make much effort to hide its malware and leaves plenty of artifacts on compromised systems," Souček said. "Little to no anti-analysis or anti-emulation techniques are implemented. ScHackTool relies heavily on its GUI, but, at the same time, contains several nonfunctional buttons."

"CosmicBeetle operators use ScHackTool mainly to download additional tools of choice to compromised machines and run them as they see fit."

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

[ESET](https://thehackernews.com/search/label/ESET)[hacking news...