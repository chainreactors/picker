---
title: Trojanized Windows 10 Installer Used in Cyberattacks Against Ukrainian Government Entities
url: https://thehackernews.com/2022/12/trojanized-windows-10-installer-used-in.html
source: The Hacker News
date: 2022-12-17
fetch_date: 2025-10-04T01:50:19.510117
---

# Trojanized Windows 10 Installer Used in Cyberattacks Against Ukrainian Government Entities

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

# [Trojanized Windows 10 Installer Used in Cyberattacks Against Ukrainian Government Entities](https://thehackernews.com/2022/12/trojanized-windows-10-installer-used-in.html)

**Dec 16, 2022**Ravie LakshmananCyber Espionage / Supply Chain Attack

[![Windows 10 Installer](data:image/png;base64... "Windows 10 Installer")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPNCu3-CFyVK3VXUNoTAIAp2BgEgkye7ZX4oLUEMPP1JBb_FQg17FWUxiAb4poTlNopoz5NhBcjJqooswDvkaMMyNM26sK_ouqKoudu6I1rECzs-VRXqjRBDgl6qdExT1pCN_R27x2suDbx2uB_jR_suahxqV7IKLPJOhkg9UyJLk6DpnnSxl5LKa5/s790-rw-e365/windows-10-installer.png)

Government entities in Ukraine have been breached as part of a new campaign that leveraged trojanized versions of Windows 10 installer files to conduct post-exploitation activities.

Mandiant, which discovered the "socially engineered supply chain" attack around mid-July 2022, said the malicious ISO files were distributed via Ukrainian- and Russian-language Torrent websites. It's tracking the threat cluster as **UNC4166**.

"Upon installation of the compromised software, the malware gathers information on the compromised system and exfiltrates it," the cybersecurity company [said](https://www.mandiant.com/resources/blog/trojanized-windows-installers-ukrainian-government) in a technical deep dive published Thursday.

Although the adversarial collective's provenance is unknown, the intrusions are said to have targeted organizations that were previously victims of disruptive wiper attacks attributed to [APT28](https://thehackernews.com/2022/09/researchers-identify-3-hacktivist.html), a [Russian state-sponsored actor](https://thehackernews.com/2022/09/hackers-using-powerpoint-mouseover.html).

The ISO file, per the Google-owned threat intelligence firm, was designed to disable the transmission of telemetry data from the infected computer to Microsoft, install PowerShell backdoors, as well as block automatic updates and license verification.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The primary goal of the operation appears to have been information gathering, with additional implants deployed to the machines, but only after conducting an initial reconnaissance of the compromised environment to determine if it contains the intelligence of value.

These included [Stowaway](https://github.com/ph4ntonn/Stowaway/blob/master/README_EN.md), an open source proxy tool, [Cobalt Strike Beacon](https://thehackernews.com/2022/11/google-identifies-34-cracked-versions.html), and SPAREPART, a lightweight backdoor programmed in C, enabling the threat actor to execute commands, harvest data, capture keystrokes and screenshots, and export the information to a remote server.

In some instances, the adversary attempted to download the TOR anonymity browser onto the victim's device. While the exact reason for this action is not clear, it's suspected that it may have served as an alternative exfiltration route.

[![Windows 10 Installer](data:image/png;base64... "Windows 10 Installer")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhStjmksM-0CjWSQzhtIiZF4RWOSMqQYxz6Mi22Ll2GoYScRwxiZSjD6lYPcVVMnb-EmLOYde-SfQpurl-yyhYQnDUwkiIiUNuAwBWbuQL_HKtcPlJ8CsQSH_l-p8Ir6NMY_4KNcgMLkoiBy-FC0RPK_VeuNaMyhet24UjeUUVyCY3vy3nZSCxgLVCf/s790-rw-e365/windows-10-installer.png)

SPAREPART, as the name implies, is assessed to be a redundant malware deployed to maintain remote access to the system should the other methods fail. It's also functionally identical to the PowerShell backdoors dropped early on in the attack chain.

"The use of trojanized ISOs is novel in espionage operations and included anti-detection capabilities indicates that the actors behind this activity are security conscious and patient, as the operation would have required a significant time and resources to develop and wait for the ISO to be installed on a network of interest," Mandiant said.

### Cloud Atlas Strikes Russia and Belarus

The findings come as [Check Point](https://research.checkpoint.com/2022/cloud-atlas-targets-entities-in-russia-and-belarus-amid-the-ongoing-war-in-ukraine/) and [Positive Technologies](https://www.ptsecurity.com/ww-en/analytics/pt-esc-threat-intelligence/apt-cloud-atlas-unbroken-threat/) disclosed attacks staged by an espionage group dubbed **Cloud Atlas** against the government sector in Russia, Belarus, Azerbaijan, Turkey, and Slovenia as part of a persistent campaign.

The hacking crew, active since 2014, has a track record of attacking entities in Eastern Europe and Central Asia. But the outbreak of the [Russo-Ukrainian war](https://thehackernews.com/2022/02/new-wiper-malware-targeting-ukraine.html) earlier this February has led to it shifting its attention to organizations in Russia, Belarus, and Transnistria.

"The actors are also maintaining their focus on the Russian-annexed Crimean Peninsula, Lugansk, and Donetsk regions," Check Point said in an analysis last week.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

[Cloud Atlas](https://securelist.com/recent-cloud-atlas-activity/92016/), also called Clean Ursa, Inception, Oxygen, and Red October, [remains unattributed](https://securelist.com/top-10-unattributed-apt-mysteries/107676/) to date, joining the likes of other APTs like [TajMahal](https://thehackernews.com/2019/04/apt-malware-framework.html), DarkUniverse, and [Metador](https://thehackernews.com/2022/09/researchers-uncover-new-metador-apt.html). The group gets its name for its reliance on cloud services like CloudMe and OpenDrive to host malware and for command-and-control (C2).

[![Windows 10 Installer](data:image/png;base64... "Windows 10 Installer")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnZLISirPDQ5UaWelaTeGLzPK_uoq_IZKhdu6F5b4TfYX4dEvDpEkBDogFs5UEfHeLCyR18OyNDLbnwg_u1MvrjoNGf5Dzb1RgHO6-X1ZDv7-utZPimKml6rZH6EQPotK4se_cU1XlayNueEN4m7JmVuItOkf4qkimWqUFFgjqYbVby1IJ14HSiBmY/s790-rw-e365/cyberattacl.png)

Attack chains orchestrated by t...