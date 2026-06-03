---
title: Pakistan-Linked SideCopy Targets Afghanistan Finance Ministry with Xeno RAT
url: https://thehackernews.com/2026/06/pakistan-linked-sidecopy-targets.html
source: The Hacker News
date: 2026-06-02
fetch_date: 2026-06-03T06:47:00.633209
---

# Pakistan-Linked SideCopy Targets Afghanistan Finance Ministry with Xeno RAT

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Pakistan-Linked SideCopy Targets Afghanistan Finance Ministry with Xeno RAT](https://thehackernews.com/2026/06/pakistan-linked-sidecopy-targets.html)

**Ravie Lakshmanan**Jun 02, 2026Cyber Espionage / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiilTEadDjLrLdKByKVP6n_zfNSbhTTutHu-9BbbIDTBotobmqmIOI7fDdGGHZQQB7wTo00L66NAKZBA3iRBLQpSf_NgH9hKe9Xd-WUoijt7y-CUbdZore_qSZpTmuBhExaAxeXn39EPCVPYugMnJ85c15e161ttOMRmbSAv7NcbUlYrqDV4NnbzHZvw0A5/s1700-e365/paki.gif)

Cybersecurity researchers have disclosed details of a spear-phishing campaign likely undertaken by the Pakistan-aligned **SideCopy** group targeting Afghanistan's Ministry of Finance with an open-source remote access trojan called [Xeno RAT](https://thehackernews.com/2024/02/open-source-xeno-rat-trojan-emerges-as.html).

"The campaign opens with a spear phishing delivery - a ZIP archive containing a malicious LNK file bearing a carefully crafted Pashto-language filename," Seqrite Labs researcher Dixit Panchal [said](https://www.seqrite.com/blog/operation-xenofiscal-sidecopy-deploying-persistent-xenorat-targeting-the-mof-afghanistan/) in a technical breakdown of the activity.

Also targeted as part of the campaign are provincial revenue and finance directorates, Pashto-speaking government officials, and provincial-level government employees. The campaign has been codenamed Operation XENOFISCAL.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The choice of Pashto for the lure file is a deliberate choice on the part of the attacker, as it's the main language spoken in the Afghan government circles. This aspect reflects the attacker's familiarity with the target environment.

SideCopy is the name given to a Pakistan-linked threat group operating under the broader Transparent Tribe (aka APT36) umbrella, using a wide range of malware families to steal sensitive data from compromised hosts. In April 2025, the adversary was [attributed](https://thehackernews.com/2025/04/pakistan-linked-hackers-expand-targets.html) to a set of attacks targeting various sectors in India with Xeno RAT, Spark RAT, and CurlBack RAT.

Viewed in that light, the latest campaign is a continuation of a broader cluster of malicious cyber activity aimed at South Asian entities.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgIfJvqG3ktFP2xVcCUmW-ZMaYhAGI5WF4Szi5M8ZmSWTD9KjgAf_xy5mOzG-RJO7AaLTy-N3WmA7krlrx3e0dfwKNnTAK4iiQcK_K76KsqnHgT58sMxHWOyrCdwFS1UJJcQfgKRH1TOOsv2n-W3Bh7XaGiS9hUBqYJfZbt1aDr_HJnfY7yKU9mkDl4_ed6/s1700-e365/mta.jpg)

Once executed, the Windows Shortcut (LNK) file leverages "mshta.exe" to fetch a remote HTML Application (HTA) from a compromised Afghan education domain, leading to the execution of obfuscated JavaScript in memory. The malware also establishes Registry-based persistence by mimicking Microsoft Edge, while dropping Xeno RAT 1.8.7 and a decoy document as a distraction mechanism by means of a DLL-based loader.

Xeno RAT is designed to connect with a remote server over TCP to handle commands sent by the operator. The malware is equipped to load and execute external DLL modules, transmit data to the server, launch the malware via a scheduled task, retrieve antivirus information, support SOCKS5 proxy-based network tunneling, perform file operations, log keystrokes, take screenshots, monitor the clipboard, track webcam/microphone, delete persistence methods, and uninstall itself from the host.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

The disclosure comes as details have emerged of a targeted phishing operation leveraging weaponized Linux .desktop files to target the Indian military infrastructure using contract-related lures associated with Indian-armored vehicle procurement operations. The campaign is assessed to be the work of [Transparent Tribe](https://thehackernews.com/2025/08/transparent-tribe-targets-indian-govt.html).

"The campaign appears to target individuals connected to Indian military and defense infrastructure ecosystems using WhatsApp-based social engineering and staged shell payload delivery," security researcher R.D. Tarun [said](https://medium.com/%40tarunrd77/pakistans-apt36-vibeware-targets-indian-military-infrastructure-75a853437c03) in a report published last month.

"Once executed, the malicious .desktop launcher initiates a heavily obfuscated shell-based infection chain involving staged payload retrieval, inline decoding routines, and deployment of a Golang-based ELF implant tracked in this report as [DeskRAT](https://thehackernews.com/2025/10/apt36-targets-indian-government-with.html)."

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

[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Malware](https://thehackernews.com/search/label/Malware), [Phishing](https://thehackernews.com/search/label/Phishing), [Remote Access Trojan](https://thehackernews.com/search/label/Remote%20Access%20Trojan), [SideCopy](https://thehackernews.com/search/label/SideCopy), ...