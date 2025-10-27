---
title: 3CX Supply Chain Attack — Here's What We Know So Far
url: https://thehackernews.com/2023/03/3cx-supply-chain-attack-heres-what-we.html
source: The Hacker News
date: 2023-04-01
fetch_date: 2025-10-04T11:25:16.291582
---

# 3CX Supply Chain Attack — Here's What We Know So Far

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

# [3CX Supply Chain Attack — Here's What We Know So Far](https://thehackernews.com/2023/03/3cx-supply-chain-attack-heres-what-we.html)

**Mar 31, 2023**Ravie LakshmananCyber Threat / Supply Chain Attack

[![3CX Supply Chain Attack](data:image/png;base64... "3CX Supply Chain Attack")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh61NC2LeNHnL7VCXbTQpyj2j0kCZkVU82sxQqWGXf_mb1AzIScS8sUnH2Sd-q74EmFts7ONz4U76aL8bU_aRVHFLL99QN36AxQBcy2DzB_uYLp47t91a4SHwgLHalZkxp1fYLOkz8BXFhEax_OLFGT-xkmYELOPUh4X1SMUxBJTiebLPBVJh1CF1Gd/s790-rw-e365/3cx.png)

Enterprise communications software maker 3CX on Thursday confirmed that multiple versions of its desktop app for Windows and macOS are affected by a [supply chain attack](https://thehackernews.com/2023/03/3cx-desktop-app-targeted-in-supply.html).

The version numbers include **18.12.407 and 18.12.416** for Windows and **18.11.1213, 18.12.402, 18.12.407, and 18.12.416** for macOS. The issue has been assigned the CVE identifier [CVE-2023-29059](https://nvd.nist.gov/vuln/detail/CVE-2023-29059).

The company said it's engaging the services of Google-owned Mandiant to review the incident. In the interim, it's urging its customers of self-hosted and on-premise versions of the software to update to version 18.12.422.

"3CX Hosted and StartUP users do not need to update their servers as we will be updating them over the night automatically," 3CX CEO Nick Galea [said](https://www.3cx.com/blog/news/desktopapp-security-alert-updates/) in a blog post. "Servers will be restarted and the new Electron App MSI/DMG will be installed on the server."

Evidence available so far points to either a compromise of 3CX's software build pipeline to distribute Windows and macOS versions of the app package, or alternatively, the poisoning of an upstream dependency. The scale of the attack is currently unknown.

Telemetry data [shared by Fortinet](https://www.fortinet.com/blog/threat-research/3cx-desktop-app-compromised) shows that the geographic spread of victim machines calling out to known actor controlled infrastructure chiefly spans Italy, Germany, Austria, the U.S., South Africa, Australia, Switzerland, the Netherlands, Canada, and the U.K.

The earliest period of potentially malicious activity is said to have been detected on or around March 22, 2023, according to a [post on the 3CX forum](https://www.3cx.com/community/threads/threat-alerts-from-sentinelone-for-desktop-update-initiated-from-desktop-client.119806/), although preparations for the sophisticated campaign commenced no later than February 2022.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

3CX [said](https://www.3cx.com/community/threads/3cx-desktopapp-security-alert.119951/post-559059) the [initial alert](https://www.3cx.com/community/threads/3cx-desktopapp-security-alert-mandiant-appointed-to-investigate.119973/post-559381) flagging a potential security problem in its app last week was treated as a "false positive" owing to the fact that none of the antivirus engines on VirusTotal labeled it as suspicious or malware.

The [Windows version of the attack](https://blog.checkpoint.com/2023/03/29/3cxdesktop-app-trojanizes-in-a-supply-chain-attack-check-point-customers-remain-protected/) leveraged a technique called DLL side-loading to load a rogue library referred to as "ffmpeg.dll" that's designed to read encrypted shellcode from another DLL called "d3dcompiler\_47.dll."

|  |
| --- |
| [![3CX Supply Chain Attack](data:image/png;base64... "3CX Supply Chain Attack")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvb_5Mjd7Foe7EsweTsUa9ozcj-nHZmGkpIbahiJGKIKRuLZ_hFWLv-fOZGjzr34zyFX4LrbqriLKGMwezn_rwbueKdjT3IVzg2scHkQn_0UFzQh4K2xDXQH8BxLAwWw3KjiQ6SB-m_xYlP1-fFXiyuEUEEc9CsA9jeYjPBxt14nY27Xd3K0bmbumR/s790-rw-e365/malware-download.png) |
| SUDDENICON downloading a new executable |

This involved the use of a downloader (known as [SUDDENICON](https://www.elastic.co/security-labs/elastic-users-protected-from-suddenicon-supply-chain-attack)) to access an actor-controlled [GitHub repository](https://www.group-ib.com/blog/3cx-supply-chain-attack) and retrieve an ICO file containing URLs hosting the final-stage payload – an information stealer (dubbed [ICONIC Stealer](https://www.volexity.com/blog/2023/03/30/3cx-supply-chain-compromise-leads-to-iconic-incident/)) capable of harvesting system information and sensitive data stored in web browsers.

British cybersecurity vendor Sophos [pointed out](https://news.sophos.com/en-us/2023/03/29/3cx-dll-sideloading-attack/) that the [shellcode](https://www.todyl.com/blog/post/threat-advisory-3cx-softphone-telephony-campaign) utilized in the attack is a "byte-to-byte match" to prior samples seen in incidents exclusively attributed to the Lazarus Group.

"The choice of these two DLLs – ffmpeg and d3dcompiler\_47 – by the threat actors behind this attack was no accident," ReversingLabs security researcher Karlo Zanki [said](https://www.reversinglabs.com/blog/red-flags-fly-over-supply-chain-compromised-3cx-update).

"The target in question, 3CXDesktopApp, is built on the Electron open source framework. Both of the libraries in question usually ship with the Electron runtime and, therefore, are unlikely to raise suspicion within customer environments."

[![3CX Supply Chain Attack](data:image/png;base64... "3CX Supply Chain Attack")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5VJRTYr3x2bJRK6unuDhLgt81RdE1VMC2mJjYwtl802ZSDYJjQsW_yLKTuw1e9j8b9taS6BErNZAA7bby475eKWsh2H34rHxnVNIV8muOO1WIJHxu4Vd7Xlu8jrciYwMDlz1lY6MqhGR7AeFovsIQGoF6OR-SSzALgxnWFTJc-u5_DWlO5wzWO-3j/s790-rw-e365/zip.png)

The macOS attack chain, in the same vein, bypassed Apple's notarization checks to download an unknown payload from a command-and-control (C2) server that's currently unresponsive.

"The macOS version does not use GitHub to retrieve its C2 server," Volexity [said](https://www.volexity.com/blog/2023/03/30/3cx-supply-chain-compromise-leads-to-iconic-incident/), which is ...