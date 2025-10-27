---
title: QwixxRAT: New Remote Access Trojan Emerges via Telegram and Discord
url: https://thehackernews.com/2023/08/qwixxrat-new-remote-access-trojan.html
source: The Hacker News
date: 2023-08-15
fetch_date: 2025-10-04T12:04:04.490919
---

# QwixxRAT: New Remote Access Trojan Emerges via Telegram and Discord

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

# [QwixxRAT: New Remote Access Trojan Emerges via Telegram and Discord](https://thehackernews.com/2023/08/qwixxrat-new-remote-access-trojan.html)

**Aug 14, 2023**Ravie LakshmananCyber Threat / Malware

[![QwixxRAT Trojan](data:image/png;base64... "QwixxRAT Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLbW81R34EdTj6TsAvrJOESpq8VqwJsF5jwFCIh1zlO37anEBFEI2Ptt7vV1rRBdLTWBnImA9fclVwmTp3c3GHmTh0Bfm4Dbxai3IB_wHEeI9HEt5QC0HknBDqzDIxbctPqAhJ71lR0fpXmFlodGpzgJ1C8kftUhFyDOJStc5gZ-2RIUhLTI04EA5qwV5q/s790-rw-e365/malware.jpg)

A new remote access trojan (RAT) called **QwixxRAT** is being advertised for sale by its threat actor through Telegram and Discord platforms.

"Once installed on the victim's Windows platform machines, the RAT stealthily collects sensitive data, which is then sent to the attacker's Telegram bot, providing them with unauthorized access to the victim's sensitive information," Uptycs [said](https://www.uptycs.com/blog/remote-access-trojan-qwixx-telegram) in a new report published today.

The cybersecurity company, which discovered the malware earlier this month, said it's "meticulously designed" to harvest web browser histories, bookmarks, cookies, credit card information, keystrokes, screenshots, files matching certain extensions, and data from apps like Steam and Telegram.

The tool is offered for 150 rubles for weekly access and 500 rubles for a lifetime license. It also comes in a limited free version.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

A C#-based binary, QwixxRAT comes with various anti-analysis features to remain covert and evade detection. This includes a sleep function to introduce a delay in the execution process as well as run checks to determine whether it's operating within a sandbox or virtual environment.

Other functions allow it to monitor for a specific list of processes (e.g., "taskmgr," "processhacker," "netstat," "netmon," "tcpview," and "wireshark"), and if detected, halts its own activity until the process is terminated.

[![QwixxRAT Trojan](data:image/png;base64... "QwixxRAT Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjitGcp_twfhu3BvijDCImUrvkwRONhrZtn-qp9-rpZkBJh8TuDSpVgzxN-3g5OmDZzS5pbAZi_U1OOYS-HdYQ-3H7L56BpoQ1iE7hW3z1x6r0K6oPmDXwBtOPLJyUmo2z-ILaOJdNoQebovAHoMTUiIEk6k7NAU1WtTEfNeCnfPwo8k50ftY64bDwV9un/s790-rw-e365/tele.jpg)

Also incorporated in QwixxRAT is a clipper that stealthily accesses sensitive information copied to the device's clipboard with an aim to conduct illicit fund transfers from cryptocurrency wallets.

Command-and-control (C2) is facilitated by means of a Telegram bot, through which commands are sent to carry out additional data collection such as audio and webcam recordings and even remotely shutdown or restart the infected host.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure comes weeks after Cyberint disclosed details of two other RAT strains dubbed [RevolutionRAT](https://cyberint.com/blog/research/revolutionrat-discovery/) and [Venom Control RAT](https://cyberint.com/blog/research/venom-control-rat-with-a-sting/) that's also advertised on various Telegram channels with data exfiltration and C2 connectivity features.

It also follows the discovery of an ongoing campaign that employs compromised sites as launchpads to present a fake Chrome web browser update to entice victims to install a remote administration software tool called NetSupport Manager RAT by means of a malicious JavaScript code.

The use of a deceptive browser update lure is synonymous with [SocGholish](https://thehackernews.com/2023/03/cybercriminals-targeting-law-firms-with.html) (aka FakeUpdates), but definitive evidence connecting the two sets of activities remains elusive.

"The abuse of readily available RATs continues as these are powerful tools capable of fulfilling the adversaries’ needs to carry out their attacks and achieve their objectives," Trellix [said](https://www.trellix.com/en-us/about/newsroom/stories/research/new-techniques-of-fake-browser-updates.html). "While these RATs may not be constantly updated, the tools and techniques to deliver these payloads to potential victims will continue to evolve."

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

[Discord](https://thehackernews.com/search/label/Discord)[Remote Access Trojan](https://thehackernews.com/search/label/Remote%20Access%20Trojan)[Telegram](https://thehackernews.com/search/label/Telegram)[Uptycs](https://thehackernews.com/search/label/Uptycs)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling...