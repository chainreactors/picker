---
title: New BlackCat Ransomware Variant Adopts Advanced Impacket and RemCom Tools
url: https://thehackernews.com/2023/08/new-blackcat-ransomware-variant-adopts.html
source: The Hacker News
date: 2023-08-19
fetch_date: 2025-10-04T12:02:51.380849
---

# New BlackCat Ransomware Variant Adopts Advanced Impacket and RemCom Tools

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

# [New BlackCat Ransomware Variant Adopts Advanced Impacket and RemCom Tools](https://thehackernews.com/2023/08/new-blackcat-ransomware-variant-adopts.html)

**Aug 18, 2023**Ravie LakshmananCyber Attack / Ransomware

[![BlackCat Ransomware](data:image/png;base64... "BlackCat Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgmVyzZmYtzcrI1RWjwlKfsXbJFil6GNJVYBil0EwSx6V88OvmCPi5-Prwf5ZsFEwsQ72R6A937DJhdp8Gr-SFumuj0KDo4XW1gtjbdvABwWor3e71PBaLNOFruTUqeXeaBt-MuHWKxMxhCHxEKoweJ0EQn-_Tj5WjvdcMDddR4vS9hnFL630z69ElzJ9vM/s790-rw-e365/rasnomware.jpg)

Microsoft on Thursday disclosed that it found a new version of the **BlackCat** ransomware (aka ALPHV and Noberus) that embeds tools like Impacket and RemCom to facilitate lateral movement and remote code execution.

"The [Impacket tool](https://www.coresecurity.com/core-labs/open-source-tools/impacket) has credential dumping and remote service execution modules that could be used for broad deployment of the BlackCat ransomware in target environments," the company's threat intelligence team [said](https://twitter.com/MsftSecIntel/status/1692212191536066800) in a series of posts on X (formerly Twitter).

"This BlackCat version also has the [RemCom hacktool](https://support.alertlogic.com/hc/en-us/articles/360034494351-Windows-Server-RemCom-Tool-Remote-ShellC%20and%20stream%20it%20back) embedded in the executable for remote code execution. The file also contains hardcoded compromised target credentials that actors use for lateral movement and further ransomware deployment."

RemCom, billed as an open-source alternative to PsExec, has been put to use by Chinese and Iranian nation-state threat actors like [Dalbit](https://asec.ahnlab.com/en/47455/) and [Chafer](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/chafer-latest-attacks-reveal-heightened-ambitions) (aka Remix Kitten) to move across the victim environments in the past.

Redmond said it started observing the new variant in attacks conducted by a BlackCat affiliate in July 2023.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The development [comes](https://twitter.com/vxunderground/status/1692312621477777519) over two months after IBM Security X-Force [disclosed](https://thehackernews.com/2023/06/improved-blackcat-ransomware-strikes.html) details of the updated version of BlackCat, called Sphynx, that first emerged in February 2023 with improved encryption speed and stealth, pointing to continued efforts made by threat actors to refine and retool the ransomware.

"The BlackCat ransomware sample contains more than just ransomware functionality but can function as a 'toolkit,'" IBM Security X-Force noted in late May 2023. "An additional string suggests that tooling is based on tools from Impacket."

The cybercrime group, which launched its operation in November 2021, is marked by constant evolution, having most recently released a [data leak API](https://www.bitdefender.com/blog/hotforsecurity/alphv-blackcat-ransomware-group-unveils-data-leak-api-to-amplify-extortion-efforts/) to boost the visibility of its attacks. According to Rapid7's [Mid-Year Threat Review](https://www.rapid7.com/blog/post/2023/08/17/rapid7s-mid-year-threat-review/) for 2023, BlackCat has been attributed to 212 out of a total of 1,500 ransomware attacks.

It's not just BlackCat, for the [Cuba](https://thehackernews.com/2022/12/cuba-ransomware-extorted-over-60.html) (aka COLDRAW) ransomware threat group has also been observed utilizing a comprehensive attack toolset encompassing [BUGHATCH](https://thehackernews.com/2023/01/microsoft-urges-customers-to-secure-on.html), a custom downloader; [BURNTCIGAR](https://thehackernews.com/2022/12/ransomware-attackers-use-microsoft.html), an antimalware killer; Wedgecut, a host enumeration utility; Metasploit; and Cobalt Strike frameworks.

BURNTCIGAR, in particular, features under-the-hood modifications to incorporate a hashed hard-coded list of targeted processes to terminate, likely in an attempt to impede analysis.

One of the attacks mounted by the group in early June 2023 is said to have weaponized [CVE-2020-1472](https://thehackernews.com/2020/09/detecting-and-preventing-critical.html) (Zerologon) and [CVE-2023-27532](https://thehackernews.com/2023/04/microsoft-confirms-papercut-servers.html), a high-severity flaw in Veeam Backup & Replication software that has been previously exploited by the FIN7 gang, to steal credentials from configuration files.

Canadian cybersecurity company BlackBerry [said](https://blogs.blackberry.com/en/2023/08/cuba-ransomware-deploys-new-tools-targets-critical-infrastructure-sector-in-the-usa-and-it-integrator-in-latin-america) it marks the group's "first observed use of an exploit for the Veeam vulnerability CVE-2023-27532." Initial access is achieved by means of compromised admin credentials via RDP.

"The Cuba ransomware operators continue to recycle network infrastructure and use a core set of TTPs that they have been subtly modifying from campaign to campaign, often adopting readily available components to upgrade their toolset whenever the opportunity arises," it added.

Ransomware remains a [major money-spinner](https://thehackernews.com/2023/07/ransomware-extortion-skyrockets-in-2023.html) for [financially motivated threat actors](https://www.malwarebytes.com/blog/threat-intelligence/2023/08/ransomware-review-august-2023), growing both in sophistication and quantity in the first half of 2023 than all of 2022 despite intensified law enforcement efforts to take them down.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Some groups have also begun moving away from encryption to pure exfiltration and ransom or, alternatively, resorting to [triple extortion](https://thehackernews.com/2023/06/new-linux-ransomware-strain-blacksuit.html), in which the attacks go beyond data encryption and theft to blackmail a victim's employees or customers and carry out D...