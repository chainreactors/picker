---
title: North Korean Hackers Using New VeilShell Backdoor in Stealthy Cyber Attacks
url: https://thehackernews.com/2024/10/north-korean-hackers-using-new.html
source: The Hacker News
date: 2024-10-04
fetch_date: 2025-10-06T18:54:49.228466
---

# North Korean Hackers Using New VeilShell Backdoor in Stealthy Cyber Attacks

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

# [North Korean Hackers Using New VeilShell Backdoor in Stealthy Cyber Attacks](https://thehackernews.com/2024/10/north-korean-hackers-using-new.html)

**Oct 03, 2024**Ravie LakshmananCyber Espionage / Threat Intelligence

[![Stealthy Cyber Attacks](data:image/png;base64... "Stealthy Cyber Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgYEfXN87k4Pzn7PnwX6FKcPhemB4Hfo1Ls4sXTFYzUtwzYMhPUzuyD23AUarS5cLAIOuKJQ43jP350Sop3GJhFSw9FcKALYvzJDh3ThY5ACpYnETQC3Uw2sAJ5UZ6tY_5k0lOHVeL30uf8mURzLaTFb566N22BCTEuxq2sD91Eu0fxVLbJg439CAOU7K_w/s790-rw-e365/malware-code.png)

Threat actors with ties to North Korea have been observed delivering a previously undocumented backdoor and remote access trojan (RAT) called VeilShell as part of a campaign targeting Cambodia and likely other Southeast Asian countries.

The activity, dubbed **SHROUDED#SLEEP** by Securonix, is believed to be the handiwork of [APT37](https://thehackernews.com/2024/01/north-korean-hackers-weaponize-fake.html), which is also known as InkySquid, Reaper, RedEyes, Ricochet Chollima, Ruby Sleet, and ScarCruft.

Active since at least 2012, the adversarial collective is assessed to be part of North Korea's Ministry of State Security (MSS). Like with other state-aligned groups, those affiliated with North Korea, including the Lazarus Group and Kimsuky, vary in their modus operandi and likely have ever-evolving objectives based on state interests.

A key malware in its toolbox is [RokRAT](https://thehackernews.com/2024/05/north-korean-hackers-deploy-new-golang.html) (aka Goldbackdoor), although the group has also developed custom tools to facilitate covert intelligence gathering.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

It's currently not known how the first stage payload, a ZIP archive bearing a Windows shortcut (LNK) file, is delivered to targets. However, it's suspected that it likely involves sending spear-phishing emails.

"The [VeilShell] backdoor trojan allows the attacker full access to the compromised machine," researchers Den Iuzvyk and Tim Peck said in a technical [report](https://www.securonix.com/blog/shroudedsleep-a-deep-dive-into-north-koreas-ongoing-campaign-against-southeast-asia/) shared with The Hacker News. "Some features include data exfiltration, registry, and scheduled task creation or manipulation."

The LNK file, once launched, acts as a dropper in that it triggers the execution of PowerShell code to decode and extract next-stage components embedded into it.

This includes an innocuous lure document, a Microsoft Excel or a PDF document, that's automatically opened, distracting the user while a configuration file ("d.exe.config") and a malicious DLL ("DomainManager.dll") file are written in the background to the Windows startup folder.

[![Stealthy Cyber Attacks](data:image/png;base64... "Stealthy Cyber Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjAWp1hQtjr_BXz9BiLoerCLM3H0_9dJ5JFYo0-1fkdZsMnzX9LeigOkOLt4zH4bEBDooVOZCfBwLFpQaW8Unp-X2tHnGtQ-sv-mdDT2N-1v84Bu5iDb2IwKgLbPOkQRdEluWKu8FdfudaLkjkfs82PXT-iXbR4i4sVfHhXFsPrqGyjg26DzRvqjWZ14yCO/s790-rw-e365/malware.png)

Also copied to the same folder is a legitimate executable named "dfsvc.exe" that's associated with the ClickOnce technology in Microsoft .NET Framework. The file is copied as "d.exe."

What makes the attack chain stand out is the use of a lesser-known technique called AppDomainManager injection in order to execute DomainManager.dll when "d.exe" is launched at startup and the binary reads the accompanying "d.exe.config" file located in the same startup folder.

It's worth noting that this approach was recently also put to use by the China-aligned [Earth Baxia](https://thehackernews.com/2024/09/chinese-hackers-exploit-geoserver-flaw.html) actor, indicating that it is slowly gaining traction among threat actors as an alternative to DLL side-loading.

The DLL file, for its part, behaves like a simple loader to retrieve JavaScript code from a remote server, which, in turn, reaches out to a different server to obtain the VeilShell backdoor.

VeilShell is a PowerShell-based malware that's designed to contact a command-and-control (C2) server to await further instructions that allow it to gather information about files, compress a specific folder into a ZIP archive and upload it back to the C2 server, download files from a specified URL, rename and delete files, and extract ZIP archives.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Overall, the threat actors were quite patient and methodical," the researchers noted. "Each stage of the attack features very long sleep times in an effort to avoid traditional heuristic detections. Once VeilShell is deployed it doesn't actually execute until the next system reboot."

"The SHROUDED#SLEEP campaign represents a sophisticated and stealthy operation targeting Southeast Asia leveraging multiple layers of execution, persistence mechanisms, and a versatile PowerShell-based backdoor RAT to achieve long-term control over compromised systems."

Securonix's report comes a day after Broadcom-owned Symantec [revealed](https://thehackernews.com/2024/10/andariel-hacker-group-shifts-focus-to.html) that the North Korean threat actor tracked as Andariel targeted three different organizations in the U.S. in August 2024 as part of a financially motivated campaign.

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
[**Sh...