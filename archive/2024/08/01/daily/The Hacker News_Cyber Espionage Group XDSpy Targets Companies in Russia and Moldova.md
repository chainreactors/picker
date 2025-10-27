---
title: Cyber Espionage Group XDSpy Targets Companies in Russia and Moldova
url: https://thehackernews.com/2024/07/cyber-espionage-group-xdspy-targets.html
source: The Hacker News
date: 2024-08-01
fetch_date: 2025-10-06T18:12:06.916640
---

# Cyber Espionage Group XDSpy Targets Companies in Russia and Moldova

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

# [Cyber Espionage Group XDSpy Targets Companies in Russia and Moldova](https://thehackernews.com/2024/07/cyber-espionage-group-xdspy-targets.html)

**Jul 31, 2024**Ravie LakshmananCyber Espionage / Threat Intelligence

[![Cyber Espionage](data:image/png;base64... "Cyber Espionage")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMiIRNJotCRCmOzAPY6Fu2qXnZXYZoODmPDFy9qAe9db1RkorDAPM2DGfY3HJRjBt4GNuuMqs57nfmYlWwfCZzb5wWhC1nG3i2QnRGT3YjmDQJ97MDvwaHDwQBrAljDpyITa65LaRafp4_zUfBFzO1ljuNtVdkaQoKBiewx24OWWENId-Cf7Qkrmf-ZgGM/s790-rw-e365/hackers.png)

Companies in Russia and Moldova have been the target of a phishing campaign orchestrated by a little-known cyber espionage group known as **XDSpy**.

The [findings](https://habr.com/ru/companies/f_a_c_c_t/news/831420/) come from cybersecurity firm F.A.C.C.T., which said the infection chains lead to the deployment of a malware called DSDownloader. The activity was observed this month, it added.

[XDSpy](https://cert.by/?p=1458) is a threat actor of indeterminate origin that was [first](https://cert.by/?p=1807) [uncovered](https://cert.by/?p=1869) by the Belarusian Computer Emergency Response Team, CERT.BY, in February 2020. A subsequent analysis by ESET [attributed](https://www.welivesecurity.com/2020/10/02/xdspy-stealing-government-secrets-since-2011/) the group to [information-stealing attacks](https://vblocalhost.com/uploads/VB2020-Faou-Labelle.pdf) aimed at government agencies in Eastern Europe and the Balkans since 2011.

Attack chains mounted by the adversary are known to leverage spear-phishing emails in order to infiltrate their targets with a main malware module known as XDDown that, in turn, drops additional plugins for gathering system information, enumerating C: drive, monitoring external drives, exfiltrating local files, and gathering passwords.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Over the past year, XDSpy has been [observed](https://habr.com/ru/companies/f_a_c_c_t/news/747540/) [targeting](https://habr.com/ru/companies/f_a_c_c_t/news/775944/) Russian organizations with a C#-base dropper named UTask that's responsible for downloading a core module in the form of an executable that can fetch more payloads from a command-and-control (C2) server.

The latest set of attacks entails the use of phishing emails with agreement-related lures to propagate a RAR archive file that contains a legitimate executable and a malicious DLL file. The DLL is then executed by means of the former using DLL side-loading techniques.

In the next phase, the library takes care of fetching and running DSDownloader, which, in turn, opens a decoy file as a distraction while surreptitiously downloading the next-stage malware from a remote server. F.A.C.C.T. said the payload was no longer available for download at the time of analysis.

The onset of the Russo-Ukrainian war in February 2022 has witnessed a significant escalation in cyber attacks on both sides, with Russian companies [compromised](https://habr.com/ru/companies/f_a_c_c_t/news/776660/) by [DarkWatchman RAT](https://thehackernews.com/2021/12/new-fileless-malware-uses-windows.html) as well as by activity clusters tracked as [Core Werewolf](https://www.facct.ru/blog/core-werewolf/), [Hellhounds](https://thehackernews.com/2024/06/russian-power-companies-it-firms-and.html), [PhantomCore](https://www.facct.ru/blog/phantomdl-loader/), [Rare Wolf](https://bi.zone/eng/expertise/blog/rare-wolf-okhotitsya-za-privatnymi-dannymi-s-pomoshchyu-falshivykh-nakladnykh-1s-predpriyatie/), [ReaverBits](https://www.facct.ru/blog/reaverbits/), and [Sticky Werewolf](https://thehackernews.com/2024/06/sticky-werewolf-expands-cyber-attack.html), among others in recent months.

What's more, pro-Ukrainian [hacktivist groups](https://cloud.google.com/blog/topics/threat-intelligence/global-revival-of-hacktivism) such as Cyber.Anarchy.Squad have also set their sights on Russian entities, conducting hack-and-leak operations and disruptive attacks against [Infotel](https://www.strikesource.com/2023/06/11/cyber-anarchy-squad-ukraines-answer-to-killnet/) and [Avanpost](https://t.me/cyber_anarchy_squad/215).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development comes as the Computer Emergency Response Team of Ukraine (CERT-UA) [warned](https://cert.gov.ua/article/6280159) of a spike in phishing attacks carried out by a Belarusian threat actor called [UAC-0057](https://thehackernews.com/2024/06/spectr-malware-targets-ukraine-defense.html) (aka GhostWriter and UNC1151) that distribute a malware family referred to as [PicassoLoader](https://thehackernews.com/2023/07/picassoloader-malware-used-in-ongoing.html) with an aim to drop a Cobalt Strike Beacon on infected hosts.

It also follows the discovery of a new campaign from the Russia-linked [Turla](https://thehackernews.com/2024/05/turla-group-deploys-lunarweb-and.html) group that utilizes a malicious Windows shortcut (LNK) file as a conduit to serve a fileless backdoor that can execute PowerShell scripts received from a legitimate-but-compromised server and disable security features.

"It also employs memory patching, bypass AMSI and disable system's event logging features to impair system's defense to enhance its evasion capability," G DATA researchers [said](https://www.gdatasoftware.com/blog/2024/07/37977-turla-evasion-lnk-files). "It leverages Microsoft's msbuild.exe to implement AWL (Application Whitelist) Bypass to avoid detection."

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
[*...