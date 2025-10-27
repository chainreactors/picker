---
title: New Russian-Backed Gamaredon's Spyware Variants Targeting Ukrainian Authorities
url: https://thehackernews.com/2023/02/new-russian-backed-gamaredons-spyware.html
source: The Hacker News
date: 2023-02-03
fetch_date: 2025-10-04T05:37:43.671848
---

# New Russian-Backed Gamaredon's Spyware Variants Targeting Ukrainian Authorities

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

# [New Russian-Backed Gamaredon's Spyware Variants Targeting Ukrainian Authorities](https://thehackernews.com/2023/02/new-russian-backed-gamaredons-spyware.html)

**Feb 02, 2023**Ravie LakshmananCyber Risk / Threat Detection

[![Spyware](data:image/png;base64... "Spyware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDTl4UQC1zP5wMieJ3LjhcJ9hcsRhq5YY-UCzBrpPMuxg2vuB1VVvKwgkHeHhtcreOvdbccdg4ltIq7eZfSgL49ZXZeCM4523Vy1UA8iaipHaa10IDYb9TLwFfqegSArLGWf7QjK89m3MU66zcJm0fHSaD-1rnNj8gzRetsfg13nJ248TF1g5ZglY9/s790-rw-e365/hackinggg.png)

The State Cyber Protection Centre (SCPC) of Ukraine has called out the Russian state-sponsored threat actor known as **Gamaredon** for its targeted cyber attacks on public authorities and critical information infrastructure in the country.

The advanced persistent threat, also known as Actinium, Armageddon, Iron Tilden, Primitive Bear, Shuckworm, Trident Ursa, and UAC-0010, has a [track record](https://www.elastic.co/security-labs/playing-defense-against-gamaredon-group) of [striking](https://thehackernews.com/2022/06/russian-hackers-exploiting-microsoft.html) [Ukrainian entities](https://thehackernews.com/2022/08/russian-state-hackers-continue-to.html) dating as far back as 2013.

"UAC-0010 group's ongoing activity is characterized by a multi-step download approach and executing payloads of the spyware used to maintain control over infected hosts," the SCPC [said](https://scpc.gov.ua/article/229). "For now, the UAC-0010 group uses [GammaLoad and GammaSteel](https://cert.gov.ua/article/1229152) spyware in their campaigns."

GammaLoad is a VBScript dropper malware engineered to download next-stage VBScript from a remote server. GammaSteel is a PowerShell script that's capable of conducting reconnaissance and executing additional commands.

The goal of the attacks is geared more towards espionage and information theft rather than sabotage, the agency noted. The SCPC also emphasized the "insistent" evolution of the group's tactics by redeveloping its malware toolset to stay under the radar, calling Gamaredon a "key cyber threat."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Attack chains commence with spear-phishing emails carrying a RAR archive that, when opened, activates a lengthy sequence comprising five intermediate stages – an LNK file, an HTA file, and three VBScript files – that eventually culminate in the delivery of a PowerShell payload.

Information pertaining to the IP address of the command-and-control (C2) servers is posted in Telegram channels that are periodically rotated, corroborating a [report](https://thehackernews.com/2023/01/gamaredon-group-launches-cyberattacks.html) from BlackBerry late last month.

All the analyzed VBScript droppers and PowerShell scripts, per SCPC, are variants of GammaLoad and GammaSteel malware, respectively, effectively permitting the adversary to exfiltrate sensitive information.

The disclosure comes as the Computer Emergency Response Team of Ukraine (CERT-UA) [disclosed](https://cert.gov.ua/article/3761023) details of a new malicious campaign targeting state authorities of Ukraine and Poland.

The attacks take the form of lookalike web pages that impersonate the Ministry of Foreign Affairs of Ukraine, the Security Service of Ukraine, and the Polish Police (Policja) in an attempt to trick visitors into downloading software that claims to detect infected computers.

However, upon launching the file – a Windows batch script named "Protector.bat" – it leads to the execution of a PowerShell script that's capable of capturing screenshots and harvesting files with 19 different extensions from the workstation.

CERT-UA has attributed the operation to a threat actor it calls UAC-0114, which is also known as [Winter Vivern](https://www.domaintools.com/resources/blog/winter-vivern-a-look-at-re-crafted-government-maldocs/) – an [activity cluster](https://lab52.io/blog/winter-vivern-all-summer/) that has in the past leveraged weaponized Microsoft Excel documents containing [XLM macros](https://thehackernews.com/2022/07/hackers-opting-new-attack-methods-after.html) to deploy PowerShell implants on compromised hosts.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Russia's invasion of Ukraine in February 2022 has been [complemented](https://www.trellix.com/en-us/about/newsroom/stories/research/growling-bears-make-thunderous-noise.html) by targeted phishing campaigns, [destructive](https://www.elastic.co/security-labs/operation-bleeding-bear) [malware strikes](https://thehackernews.com/2023/01/new-report-reveals-nikowiper-malware.html), and distributed denial-of-service (DDoS) attacks.

Cybersecurity firm Trellix said it [observed](https://www.trellix.com/en-us/about/newsroom/stories/research/cyberattacks-targeting-ukraine-increase.html) a 20-fold surge in email-based cyber attacks on Ukraine's public and private sectors in the third week of November 2022, attributing a majority of the messages to Gamaredon.

Other malware families prominently disseminated via these campaigns consist of Houdini RAT, FormBook, Remcos, and Andromeda, the latter of which has been [repurposed by the Turla hacking crew](https://thehackernews.com/2023/01/russian-turla-hackers-hijack-decade-old.html) to deploy their own malware.

"As the Ukraine-Russia war continues, the cyber attacks on Ukraine energy, government and transportation, infrastructure, financial sector etc. are going on consistently," Trellix said. "In times of such panic and unrest, the attackers aim to capitalize on the distraction and stress of the victims to successfully exploit them."

## Update

CERT-UA has designated the name [Aperetif](https://scpc.gov.ua/article/231) to the malware used by Winter Vivern, noting that its use started no later than May 25, 2022. It also assessed that the group "highly likely" includes Russian-speaking members.

Found this article interesting? Follow us on [Google News](https://news.g...