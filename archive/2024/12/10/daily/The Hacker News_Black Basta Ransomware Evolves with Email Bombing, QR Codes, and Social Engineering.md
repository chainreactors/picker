---
title: Black Basta Ransomware Evolves with Email Bombing, QR Codes, and Social Engineering
url: https://thehackernews.com/2024/12/black-basta-ransomware-evolves-with.html
source: The Hacker News
date: 2024-12-10
fetch_date: 2025-10-06T19:42:44.867631
---

# Black Basta Ransomware Evolves with Email Bombing, QR Codes, and Social Engineering

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

# [Black Basta Ransomware Evolves with Email Bombing, QR Codes, and Social Engineering](https://thehackernews.com/2024/12/black-basta-ransomware-evolves-with.html)

**Dec 09, 2024**Ravie LakshmananThreat Intelligence / Malware

[![Black Basta Ransomware](data:image/png;base64... "Black Basta Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgH0ydjAyWCR8V206KFt3hnhnJ5qfA4eM3u86O43eFgPT6tfE1g9ePUrtzgMm3TBaPrCEGSBjKLJYDR-H-GWcXgNtf1fqB29nz1GLU7U2wxVP_0iCXdP4wnJsgvfVI5ntVN0tz8koc-psoNoPzIjNXyV46c7VjdTpVru_wpB0Qi0tJGGmt4c6PjSm_LdiYM/s790-rw-e365/rnsomware.png)

The threat actors linked to the Black Basta ransomware have been observed switching up their [social engineering tactics](https://thehackernews.com/2024/05/ongoing-campaign-bombarded-enterprises.html), distributing a different set of payloads such as [Zbot](https://thehackernews.com/2024/01/new-zloader-malware-variant-surfaces.html) and [DarkGate](https://thehackernews.com/2024/06/darkgate-malware-replaces-autoit-with.html) since early October 2024.

"Users within the target environment will be email bombed by the threat actor, which is often achieved by signing up the user's email to numerous mailing lists simultaneously," Rapid7 [said](https://www.rapid7.com/blog/post/2024/12/04/black-basta-ransomware-campaign-drops-zbot-darkgate-and-custom-malware/). "After the email bomb, the threat actor will reach out to the impacted users."

As [observed](https://thehackernews.com/2024/08/black-basta-linked-attackers-targets.html) back in August, the attackers make initial contact with prospective targets on Microsoft Teams, pretending to be support personnel or IT staff of the organization. In some instances, they have also been observed impersonating IT staff members within the targeted organization.

Users who end up interacting with the threat actors are urged to install legitimate remote access software such as AnyDesk, ScreenConnect, TeamViewer, and Microsoft's Quick Assist. The Windows maker is tracking the cybercriminal group behind the abuse of Quick Assist for Black Basta deployment under the name [Storm-1811](https://thehackernews.com/2024/05/cybercriminals-exploiting-microsofts.html).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Rapid7 said it also detected attempts made by the ransomware crew to leverage the OpenSSH client to establish a reverse shell, as well as send a malicious QR code to the victim user via the chats to likely steal their credentials under the pretext of adding a trusted mobile device.

However, cybersecurity company ReliaQuest, which also [reported](https://www.reliaquest.com/blog/black-basta-social-engineering-technique-microsoft-teams/) on the same campaign, theorized the QR codes are being used to direct users to further malicious infrastructure.

The remote access facilitated by the installation of AnyDesk (or its equivalent) is then used to deliver additional payloads to the compromised host, including a custom credential harvesting program followed by the execution of Zbot (aka ZLoader) or DarkGate, which can serve as a gateway for follow-on attacks.

"The overall goal following initial access appears to be the same: to quickly enumerate the environment and dump the user's credentials," Rapid7 security researcher Tyler McGraw said.

"When possible, operators will also still attempt to steal any available VPN configuration files. With the user's credentials, organization VPN information, and potential MFA bypass, it may be possible for them to authenticate directly to the target environment."

Black Basta emerged as an autonomous group from the ashes of Conti in the wake of the [latter's shutdown](https://thehackernews.com/2022/05/conti-ransomware-gang-shut-down-after.html) in 2022, initially leaning on [QakBot](https://thehackernews.com/2022/10/black-basta-ransomware-hackers.html) to infiltrate targets, before diversifying into social engineering techniques. The threat actor, which is also referred to as [UNC4393](https://thehackernews.com/2024/07/vmware-esxi-flaw-exploited-by.html), has since put to use [various bespoke malware families](https://cloud.google.com/blog/topics/threat-intelligence/unc4393-goes-gently-into-silentnight) to carry out its objectives -

* KNOTWRAP, a memory-only dropper written in C/C++ that can execute an additional payload in memory
* KNOTROCK, a .NET-based utility that's used to execute the ransomware
* DAWNCRY, a memory-only dropper that decrypts an embedded resource into memory with a hard-coded key
* PORTYARD, a tunneler that establishes a connection to a hard-coded command-and-control (C2) server using a custom binary protocol over TCP
* COGSCAN, a .NET reconnaissance assembly used to gather a list of hosts available on the network

"Black Basta's evolution in malware dissemination shows a peculiar shift from a purely botnet-reliant approach to a hybrid model that integrates social engineering," RedSense's Yelisey Bohuslavskiy [said](https://redsense.com/publications/evolution-of-blackbasta-malware-dissemination/).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure comes as Check Point [detailed](https://research.checkpoint.com/2024/inside-akira-ransomwares-rust-experiment/) its analysis of an updated Rust variant of the [Akira](https://thehackernews.com/2024/04/akira-ransomware-gang-extorts-42.html) ransomware, highlighting the malware authors' reliance on ready-made boilerplate code associated with third-party libraries and crates like indicatif, rust-crypto, and seahorse.

Ransomware attacks have also employed a variant of the Mimic ransomware called [Elpaco](https://securelist.com/elpaco-ransomware-a-mimic-variant/114635/), with Rhysida infections also employing [CleanUpLoader](https://thehackernews.com/2024/06/oyster-backdoor-spreading-via.html) to aid in data exfiltration and persistence. The malware is often disguised as installers for popular software, such as Microsoft Teams...