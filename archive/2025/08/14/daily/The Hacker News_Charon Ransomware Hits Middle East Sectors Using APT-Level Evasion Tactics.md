---
title: Charon Ransomware Hits Middle East Sectors Using APT-Level Evasion Tactics
url: https://thehackernews.com/2025/08/charon-ransomware-hits-middle-east.html
source: The Hacker News
date: 2025-08-14
fetch_date: 2025-10-07T00:50:50.757613
---

# Charon Ransomware Hits Middle East Sectors Using APT-Level Evasion Tactics

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

# [Charon Ransomware Hits Middle East Sectors Using APT-Level Evasion Tactics](https://thehackernews.com/2025/08/charon-ransomware-hits-middle-east.html)

**Aug 13, 2025**Ravie LakshmananEndpoint Security / Cybercrime

[![Charon Ransomware](data:image/png;base64... "Charon Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgPlk6KMyUFpS0JeUyO-NkNyXRacxY3dB0LYc9QJyNCpIMxGZ8124GjkyWMPbKw2sB0S9Rtcf7QiqWpvx1KMIwrgvW4PqgVVx1ZGHMVHN8X2-QEvTIz7S4EyvL0lC3tU2p3lsLleIZLqSAVbkbEsClteAzN02clRPlzfw-X2YaPAdA7Xdlkn7wd5Lr9LlKf/s790-rw-e365/cyberattack-ransomware.jpg)

Cybersecurity researchers have discovered a new campaign that employs a previously undocumented ransomware family called Charon to target the Middle East's public sector and aviation industry.

The threat actor behind the activity, according to Trend Micro, exhibited tactics mirroring those of advanced persistent threat (APT) groups, such as DLL side-loading, process injection, and the ability to evade endpoint detection and response (EDR) software.

The DLL side-loading techniques resemble those previously documented as part of attacks orchestrated by a China-linked hacking group called [Earth Baxia](https://thehackernews.com/2024/09/chinese-hackers-exploit-geoserver-flaw.html), which was flagged by the cybersecurity company as targeting government entities in Taiwan and the Asia-Pacific region to deliver a backdoor known as EAGLEDOOR following the exploitation of a now-patched security flaw affecting OSGeo GeoServer GeoTools.

"The attack chain leveraged a legitimate browser-related file, Edge.exe (originally named cookie\_exporter.exe), to sideload a malicious msedge.dll (SWORDLDR), which subsequently deployed the Charon ransomware payload," researchers Jacob Santos, Ted Lee, Ahmed Kamal, and Don Ovid Ladore [said](https://www.trendmicro.com/en_us/research/25/h/new-ransomware-charon.html).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Like other ransomware binaries, Charon is capable of disruptive actions that terminate security-related services and running processes, as well as delete shadow copies and backups, thereby minimizing the chances of recovery. It also employs [multithreading](https://thehackernews.com/2025/07/chaos-raas-emerges-after-blacksuit.html) and partial encryption techniques to make the file-locking routine faster and more efficient.

Another notable aspect of the ransomware is the use of a driver compiled from the open-source [Dark-Kill project](https://github.com/SaadAhla/dark-kill) to disable EDR solutions by means of what's called a bring your own vulnerable driver (BYOVD) attack. However, this functionality is never triggered during the execution, suggesting that the feature is likely under development.

There is evidence to suggest that the campaign was targeted rather than opportunistic. This stems from the use of a customized ransom note that specifically calls out the victim organization by name, a tactic not observed in traditional ransomware attacks. It's currently not known how the initial access was obtained.

[![Charon Ransomware](data:image/png;base64... "Charon Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPyS4C8QkrnyepCYGAdddXSkx6LDd_L6sQpuM4Qba1Kt_DpwbRUh2rxtAnxFv9L_cRs3GSVVMFgVlC1OgoupkiNoWjRhOsuWI0lz15xjDT5xrMv7JrKSJurmNIq6M-glpyPkqkNIPbpgCdUKt2XscQZ7Y3H5_Sy9tnsN6KS939G7fQdv3nJ8YCzzIYAmMg/s790-rw-e365/ransomware.png)

Despite the technical overlaps with Earth Baxia, Trend Micro has emphasized that this could mean one of three things -

* Direct involvement of Earth Baxia
* A false flag operation designed to deliberately imitate Earth Baxia's tradecraft, or
* A new threat actor that has independently developed similar tactics

"Without corroborating evidence such as shared infrastructure or consistent targeting patterns, we assess this attack demonstrates limited but notable technical convergence with known Earth Baxia operations," Trend Micro pointed out.

Regardless of the attribution, the findings exemplify the ongoing trend of ransomware operators increasingly adopting sophisticated methods for malware deployment and defense evasion, further blurring the lines between cybercrime and nation-state activity.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"This convergence of APT tactics with ransomware operations poses an elevated risk to organizations, combining sophisticated evasion techniques with the immediate business impact of ransomware encryption," the researchers concluded.

The disclosure comes as eSentire detailed an [Interlock ransomware](https://thehackernews.com/2025/07/new-php-based-interlock-rat-variant.html) campaign that leveraged ClickFix lures to drop a PHP-based backdoor that, in turn, deploys NodeSnake (aka Interlock RAT) for credential theft and a C-based implant that supports attacker-supplied commands for further reconnaissance and ransomware deployment.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixiz4dHTbnmuLHWY3Fk1d80oxvbpnOBt6rVWo5UP6knXaUMC3xr1Web_AtPILvjE-z7wr_J3ikgcYalN-T1WwF84oVUENj4t-D5YZZ10SOGbxRHPBb9Kra-BQN99-2Bzme4j5avzJGsO1wJPTXpeZMBZ1-r8XukO38MsujUGKq4n6D83a33UMCuKPaipF0/s790-rw-e365/Interlock.png)

"Interlock Group employs a complex multi-stage process involving PowerShell scripts, PHP/NodeJS/C backdoors, highlighting the importance of monitoring suspicious process activity, LOLBins, and other TTPs," the Canadian company [said](https://www.esentire.com/blog/unmasking-interlock-groups-evolving-malware-arsenal).

The findings show that ransomware continues to be an [evolving threat](https://www.semperis.com/blog/new-ransomware-statistics-reveal-need-for-ad-security/), even as victims continue to pay ransoms to quickly recover access to systems. Cybercriminals, on the other hand, have begun resorting to physical threats and DDoS attacks as a way of putting pressure on victims.

Statistics shared by Barracuda [...