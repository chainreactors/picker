---
title: 3CX Desktop App Supply Chain Attack Leaves Millions at Risk - Urgent Update on the Way!
url: https://thehackernews.com/2023/03/3cx-desktop-app-targeted-in-supply.html
source: The Hacker News
date: 2023-03-31
fetch_date: 2025-10-04T11:18:05.567196
---

# 3CX Desktop App Supply Chain Attack Leaves Millions at Risk - Urgent Update on the Way!

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

# [3CX Desktop App Supply Chain Attack Leaves Millions at Risk - Urgent Update on the Way!](https://thehackernews.com/2023/03/3cx-desktop-app-targeted-in-supply.html)

**Mar 30, 2023**Ravie LakshmananSupply Chain / Software Security

[![3CX Desktop App](data:image/png;base64... "3CX Desktop App")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCcARgOp5JtfJ9huSC9XAoiN9FTVcx0G9wUpnSkB58F5D6agJCYFev5X-10AP2FZTkUjjPNQmYenxp1wDnrJJj6tYPTHE_psykvoHwHoDSjIDSovN_apjiRSh5VUFX4JtP78Zkziyfhx0HSXWj7Yg4V7RTJGUdBxuqSc-h-OhY1a5nGVsxywPPW741/s790-rw-e365/3cx-hack.png)

3CX said it's [working on a software update](https://www.3cx.com/community/threads/3cx-desktopapp-security-alert.119951/) for its desktop app after multiple cybersecurity vendors sounded the alarm on what appears to be an active supply chain attack that's using digitally signed and rigged installers of the popular voice and video conferencing software to target downstream customers.

"The trojanized 3CX desktop app is the first stage in a multi-stage attack chain that pulls ICO files appended with Base64 data from GitHub and ultimately leads to a third-stage infostealer DLL," SentinelOne researchers [said](https://www.sentinelone.com/blog/smoothoperator-ongoing-campaign-trojanizes-3cx-software-in-software-supply-chain-attack/).

The cybersecurity firm is tracking the activity under the name **SmoothOperator**, stating the threat actor registered a massive attack infrastructure as far back as February 2022. There are indications that the attack may have [commenced](https://www.3cx.com/community/threads/threat-alerts-from-sentinelone-for-desktop-update-initiated-from-desktop-client.119806/) around March 22, 2023.

3CX, the company behind 3CXDesktopApp, [claims](https://www.3cx.com/company/) to have more than 600,000 customers and 12 million users in 190 countries, some of which include well-known names like American Express, BMW, Honda, Ikea, Pepsi, and Toyota, among others.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

While the 3CX PBX client is available for multiple platforms, [telemetry data](https://news.sophos.com/en-us/2023/03/29/3cx-dll-sideloading-attack/) shows that the attacks observed so far are confined to the Windows Electron client (versions 18.12.407 and 18.12.416) and macOS versions of the PBX phone system.

The infection chain, in a nutshell, takes advantage of the [DLL side-loading technique](https://attack.mitre.org/techniques/T1574/002/) to load a rogue DLL (ffmpeg.dll) that's designed to retrieve an icon file (ICO) payload. The GitHub repository [hosting the file](https://github.com/IconStorages/images) has since been [taken down](https://twitter.com/_JohnHammond/status/1641270384023719937).

[![3CX Desktop App](data:image/png;base64... "3CX Desktop App")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQkThc5qBn0aKcXerOZ53XgBi34vTIdOei20Ab54SXKfjtS1hhCoZSrJvprLJHm8zzo3SlaVTFXRLAN5CADEH5Q54rWlDetl0cd1XMn61dqsqzDuxRagX-AbCVRcg8zAAiVVBn58P3Us4GAf1NiDN8LM4cWiGvCQQTRh469yCpi0m4-znFk6mWmVcj/s790-rw-e365/logs.png)

The final payload is an information stealer capable of gathering system information and sensitive data stored in Google Chrome, Microsoft Edge, Brave, and Mozilla Firefox browsers.

The [macOS sample](https://www.virustotal.com/gui/file/e6bbc33815b9f20b0cf832d7401dd893fbc467c800728b5891336706da0dbcec) (a 381 MB file), according to [security researcher Patrick Wardle](https://objective-see.org/blog/blog_0x73.html), carries a valid signature and is [notarized by Apple](https://thehackernews.com/2022/12/microsoft-details-gatekeeper-bypass.html), meaning it can be run without the operating system blocking it.

The malicious app, similar to the Windows counterpart, includes a Mach-O binary named [libffmpeg.dylib](https://www.virustotal.com/gui/file/a64fa9f1c76457ecc58402142a8728ce34ccba378c17318b3340083eeb7acc67) that's designed to reach out to an external server "pbxsources[.]com" to download and execute a file named UpdateAgent. The server is currently offline.

Huntress [reported](https://www.huntress.com/blog/3cx-voip-software-compromise-supply-chain-threats) that there are 242,519 publicly exposed 3CX phone management systems. Broadcom-owned Symantec, in its own advisory, [said](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/3cx-supply-chain-attack) "the information gathered by this malware presumably allowed the attackers to gauge if the victim was a candidate for further compromise."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Due to its widespread use and its importance in an organization's communication system, threat actors can cause major damage (for example, by monitoring or rerouting both internal and external communication) to businesses that use this software," Trend Micro [said](https://www.trendmicro.com/en_us/research/23/c/information-on-attacks-involving-3cx-desktop-app.html).

Cybersecurity firm CrowdStrike [said](https://www.reddit.com/r/crowdstrike/comments/125r3uu/20230329_situational_awareness_crowdstrike/) it's attributing the attack with high confidence to a North Korean nation-state actor it tracks as [Labyrinth Chollima](https://thehackernews.com/2022/12/bluenoroff-apt-hackers-using-new-ways.html) (aka Nickel Academy), a sub-cluster within the notorious Lazarus Group.

"The malicious activity includes beaconing to actor-controlled infrastructure, deployment of second-stage payloads, and, in a small number of cases, hands-on-keyboard activity," CrowdStrike [added](https://www.crowdstrike.com/blog/crowdstrike-detects-and-prevents-active-intrusion-campaign-targeting-3cxdesktopapp-customers/).

In a forum post, 3CX's CEO Nick Galea said it's in the process of issuing a new build over the next few hours, and noted that [Android and iOS versions are not impacted](https://www.3cx.com/community/threads/threat-alerts-from-sentinelone-for-desktop-update-initiated-from-desktop-client.119806/...