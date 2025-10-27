---
title: New Analysis Reveals Raspberry Robin Can be Repurposed by Other Threat Actors
url: https://thehackernews.com/2023/01/new-analysis-reveals-raspberry-robin.html
source: The Hacker News
date: 2023-01-12
fetch_date: 2025-10-04T03:42:23.015766
---

# New Analysis Reveals Raspberry Robin Can be Repurposed by Other Threat Actors

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

# [New Analysis Reveals Raspberry Robin Can be Repurposed by Other Threat Actors](https://thehackernews.com/2023/01/new-analysis-reveals-raspberry-robin.html)

**Jan 11, 2023**Ravie LakshmananCyber Threat / Malware

[![Raspberry Robin](data:image/png;base64... "Raspberry Robin")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgl8vuVHpX554gUCS4Qzg6_07r7w79LYdTDw7xnWrWS_1LRV7Ng0UNbnosR8KuUlLA-onCkL57QaVcSRhej5KQgInFAJE5qMlTwN4Imstl727qwjkvDm4Iina_U6QrIz9gfbkii1xyElQRYpRW-vDPJj8runjkF6TGSkEFBTaD54TChbYxm2ZasgH7P/s790-rw-e365/hackers.png)

A new analysis of Raspberry Robin's attack infrastructure has [revealed](https://blog.sekoia.io/raspberry-robins-botnet-second-life/) that it's possible for other threat actors to repurpose the infections for their own malicious activities, making it an even more potent threat.

Raspberry Robin (aka QNAP worm), attributed to a threat actor dubbed DEV-0856, is a malware that has [increasingly](https://thehackernews.com/2022/12/raspberry-robin-worm-strikes-again.html) [come under the radar](https://thehackernews.com/2023/01/raspberry-robin-worm-evolves-to-attack.html) for being used in attacks aimed at finance, government, insurance, and telecom entities.

Given its use by multiple threat actors to drop a wide range of payloads such as [SocGholish](https://thehackernews.com/2022/07/microsoft-links-raspberry-robin-usb.html), [Bumblebee](https://thehackernews.com/2023/01/the-evolving-tactics-of-vidar-stealer.html), [TrueBot](https://thehackernews.com/2022/12/new-truebot-malware-variant-leveraging.html), [IcedID](https://www.team-cymru.com/post/inside-the-icedid-backconnect-protocol), and [LockBit](https://thehackernews.com/2022/11/amadey-bot-spotted-deploying-lockbit-30.html) ransomware, it's believed to be a pay-per-install (PPI) botnet capable of serving next-stage malware.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Raspberry Robin, notably, employs infected USB drives as a propagation mechanism and leverages breached QNAP network-attached storage (NAS) devices as first-level command-and-control (C2).

Cybersecurity firm SEKOIA said it was able to identify at least eight virtual private servers (VPSs) hosted on Linode that function as a second C2 layer that likely act as forward proxies to the next as-yet-unknown tier.

[![Raspberry Robin](data:image/png;base64... "Raspberry Robin")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhoZOYLSHWHTZ9x-1P-zlE66S8gHiumwhxAbuJvlrnQj38EzvdntofvjEAxvVu6R0sZqTDfe45Th7iNUovnLX8F7XPrlspost4JLbhLf3kdyy3QV8RklPikndx0Z3NxhhtGhuJmD_makN5Vfb7CBrbFxHm0_ImSWULMdI5pSuuXDjq3GLB0vXdqRPKH/s728/image-2.png)

[![Raspberry Robin](data:image/png;base64... "Raspberry Robin")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgn1XN_8ltrVNMw8nC_IGX98IKAhtH6yUwR2wKL2FPTBdmnHfUtcObJd_M1R-NZrJcojVvxfX4YWAvvyS53WZ1gwM8Btyrs1Tqzbjx-U8uEX8QXisltCBTfUbjArCzz-23V7k3QcV1WLDEAPASkHQGmbd4SASFEFNkaPwnOB5fMlx14dWpIyjaAwQAC/s728/secdo-1.png)

"Each compromised QNAP seems to act as a validator and forwarder," the France-based company said. "If the received request is valid, it is redirected to an upper level of infrastructure."

The attack chain thus unfolds as follows: When a user inserts the USB drive and launches a Windows shortcut (.LNK) file, the [msiexec utility](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/msiexec) is executed, which, in turn, downloads the main [obfuscated Raspberry Robin payload](https://decoded.avast.io/janvojtesek/raspberry-robins-roshtyak-a-little-lesson-in-trickery/) from the QNAP instance.

This reliance on msiexec to send out HTTP requests to fetch the malware makes it possible to hijack such requests to download another rogue MSI payload either by DNS hijacking attacks or purchasing previously known domains after their expiration.

One such domain is tiua[.]uk, which was registered in the early days of the campaign in late July 2021 and used as a C2 between September 22, 2021, and November 30, 2022, when it was suspended by the .UK registry.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"By pointing this domain to our sinkhole, we were able to obtain telemetry from one of the first domains used by Raspberry Robin operators," the company said, adding it observed several victims, indicating "it was still possible to repurpose a Raspberry Robin domain for malicious activities."

The exact origins of how the first wave of Raspberry Robin USB infections took place remain currently unknown, although it's suspected that it may have been achieved by relying on other malware to disseminate the worm.

[![Raspberry Robin](data:image/png;base64... "Raspberry Robin")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjRy5PyyEfK0Alhy4NWCREqAZbAmFBm10IMAU7Ao2AI-eV64bQDvx3DtCdX3EMadlWN2So4IxrAkH-wO_LsCrfSa4zAqChxRRQNX9zFHpImFZ3l-a1XNMZ2Fs36ZC6BTZJ-ahqfZ7XQHebgy1VO6ZwMCB1w40ZguPylQVo1ZsYM0jFQuaFPeZujcxIL/s728/map.png)

This hypothesis is [evidenced](https://thehackernews.com/2022/10/raspberry-robin-operators-selling.html) by the presence of a .NET spreader module that's said to be responsible for distributing Raspberry Robin .LNK files from infected hosts to USB drives. These .LNK files subsequently compromise other machines via the aforementioned method.

The development comes days after Google's Mandiant [disclosed](https://thehackernews.com/2023/01/russian-turla-hackers-hijack-decade-old.html) that the Russia-linked Turla group reused expired domains associated with ANDROMEDA malware to deliver reconnaissance and backdoor tools to targets compromised by the latter in Ukraine.

"Botnets serve multiple purposes and can be reused and/or remodeled by their operators or even hijacked by other groups over time," the researchers said.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter]...