---
title: SYS01stealer: New Threat Using Facebook Ads to Target Critical Infrastructure Firms
url: https://thehackernews.com/2023/03/sys01stealer-new-threat-using-facebook.html
source: The Hacker News
date: 2023-03-08
fetch_date: 2025-10-04T08:57:59.316477
---

# SYS01stealer: New Threat Using Facebook Ads to Target Critical Infrastructure Firms

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

# [SYS01stealer: New Threat Using Facebook Ads to Target Critical Infrastructure Firms](https://thehackernews.com/2023/03/sys01stealer-new-threat-using-facebook.html)

**Mar 07, 2023**Ravie LakshmananData Safety / Cyber Threat

[![SYS01stealer](data:image/png;base64... "SYS01stealer")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEif1sNEwDxAp2MiNYxnKhoxss-j8_PQ8TQw_wbki3zATCp_Z4tEwtMn9gytUMEKE52YSZrIP6iIdhbx60RI1H5R04MZqgoxBmXCuDAZsyr0u3-YVz6r2VgI1GFQTYP43sz_Ixigd38vCyIWhJ2-0yiVFX7t3qsbZLvZmZWFH1iUOlII3h0oA7vMJ31Zpg/s790-rw-e365/hacking.png)

Cybersecurity researchers have discovered a new information stealer dubbed **SYS01stealer** targeting critical government infrastructure employees, manufacturing companies, and other sectors since November 2022.

"The threat actors behind the campaign are targeting Facebook business accounts by using Google ads and fake Facebook profiles that promote things like games, adult content, and cracked software, etc. to lure victims into downloading a malicious file," Morphisec said in a [report](https://blog.morphisec.com/sys01stealer-facebook-info-stealer) shared with The Hacker News.

"The attack is designed to steal sensitive information, including login data, cookies, and Facebook ad and business account information."

The Israeli cybersecurity company said the campaign was initially tied to a financially motivated cybercriminal operation [dubbed Ducktail](https://thehackernews.com/2022/10/new-php-version-of-ducktail-malware.html) by Zscaler.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

However, WithSecure, which [first documented](https://thehackernews.com/2022/07/new-ducktail-infostealer-malware.html) the Ducktail activity cluster in July 2022, said the [two intrusion sets](https://thehackernews.com/2022/11/ducktail-malware-operation-evolves-with.html) are different from one another, indicating how the threat actors managed to confuse attribution efforts and evade detection.

The attack chain, per Morphisec, commences when a victim is successfully lured into clicking on a URL from a fake Facebook profile or advertisement to download a ZIP archive that purports to be cracked software or adult-themed content.

Opening the ZIP file launches a based loader – typically a legitimate C# application – that's vulnerable to [DLL side-loading](https://attack.mitre.org/techniques/T1574/002/), thereby making it possible to load a malicious dynamic link library (DLL) file alongside the app.

[![SYS01stealer](data:image/png;base64... "SYS01stealer")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJbMlJnMw57sXMHTGpfPcDYqUs4agU5RdzocwHzNAqlLcre0U1ZpfdrCoLAlV6WQEdvWm4ZzQEkMmCFoDT4AobdDeDdMOJYUv6J2JOgsEMRGjb4cdBUn1rAz2gRfWeNTnYnEQCXL6fEDkx9ght_7yoosK9pnMN3CSkiTR7fjWT9GpnXGiKw3Ped8Se/s790-rw-e365/dll.png)

Some of the applications abused to side-load the rogue DLL are Western Digital's WDSyncService.exe and Garmin's ElevatedInstaller.exe. In some instances, the side-loaded DLL acts as a means to deploy Python and Rust-based intermediate executables.

Irrespective of the approach employed, all roads lead to the delivery of an installer that drops and executes the PHP-based SYS01stealer malware.

The stealer is engineered to harvest Facebook cookies from Chromium-based web browsers (e.g., Google Chrome, Microsoft Edge, Brave, Opera, and Vivaldi), exfiltrate the victim's Facebook information to a remote server, and download and run arbitrary files.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

It's also equipped to upload files from the infected host to the command-and-control (C2) server, run commands sent by the server, and update itself when a new version is available.

The development comes as Bitdefender revealed a similar stealer campaign known as [S1deload](https://thehackernews.com/2023/02/new-s1deload-malware-hijacking-users.html) that's designed to hijack users' Facebook and YouTube accounts and leverage the compromised systems to mine cryptocurrency.

"DLL side-loading is a highly effective technique for tricking Windows systems into loading malicious code," Morphisec said.

"When an application loads in memory and search order is not enforced, the application loads the malicious file instead of the legitimate one, allowing threat actors to hijack legitimate, trusted, and even signed applications to load and execute malicious payloads."

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

[critical infrastructure](https://thehackernews.com/search/label/critical%20infrastructure)[data security](https://thehackernews.com/search/label/data%20security)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Information Stealer](https://thehackernews.com/search/label/Information%20Stealer)[Malware](https://thehackernews.com/search/label/Malware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE...