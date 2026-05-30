---
title: Kimsuky Deploys HTTPSpy, Expands Arsenal with HelloDoor and VS Code Tunnels
url: https://thehackernews.com/2026/05/kimsuky-deploys-httpspy-expands-arsenal.html
source: The Hacker News
date: 2026-05-29
fetch_date: 2026-05-30T05:44:31.874969
---

# Kimsuky Deploys HTTPSpy, Expands Arsenal with HelloDoor and VS Code Tunnels

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [Kimsuky Deploys HTTPSpy, Expands Arsenal with HelloDoor and VS Code Tunnels](https://thehackernews.com/2026/05/kimsuky-deploys-httpspy-expands-arsenal.html)

**Ravie Lakshmanan**May 29, 2026Threat Intelligence / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJfUl1K-os1XyLN-SBt6PgMia_jFG03ArRa3H0FI2hsiUqNa3lqSWY2NJcvOhY33TArSKJxeookUpkATdERUpEwKw-IUi6iv9ZVuUq4c1A99mLwgQB4ibCxBx4MBR1XXmM98zH7v-QWDO7bhh1AONQ8Op0htvwHhuivwI1Cch9rgLPO-zSGCjjQbvXdDte/s1700-e365/north-korea.png)

The North Korean state-sponsored threat actor known as **[Kimsuky](https://thehackernews.com/2026/01/fbi-warns-north-korean-hackers-using.html)** (aka Velvet Chollima) has been attributed to a fresh set of cyber attacks targeting South Korean military and corporate entities through March and April 2026.

"Kimsuky employed a range of tailored social engineering tactics, such as spoofing security software installation pages and crafting a fake Webex meeting page that leveraged a legitimate meeting schedule," ENKI [said](https://www.enki.co.kr/en/media-center/blog/kimsuky-s-advanced-attack-techniques-jsonping-webex-spoofing-and-a-new-httpspy-variant) in an analysis published this week.

The attacks have been found to deliver a variant of a known malware family dubbed **HTTPSpy** by disguising it as installers from South Korean security software, a tactic the [threat actor](https://www.estsecurity.com/public/security-center/notice/view/542031?category-id=) has [consistently](https://asec.ahnlab.com/ko/61666/) [adopted](https://blog.alyac.co.kr/5564) since 2023.

In the latest campaign observed in March 2026, the adversary has been found to propagate malicious payloads through a bogus web page impersonating the security software installation page of a South Korean B2B messaging service. Given the nature of the lure, it's suspected that the activity may have been specifically designed to single out messaging administrators within corporate environments.

The page claims to offer two security tools: a firewall and a keyboard security program. Once unsuspecting users initiate the download, it results in the download of either of the two executables - "nos-setup.exe" and "astx-setup.exe" - that masquerade as nProtect Online Security and AhnLab Safe Transaction (ASTx). Despite the differences in the name, the malicious behavior embedded in them is identical.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

The primary responsibility of the binaries is to launch a second-stage DLL payload ("MemLoader.dll") via "regsvr32.exe," after which a batch script is run to delete themselves from disk. The DLL establishes persistence on the host using a scheduled task and contacts a command-and-control (C2) server to retrieve an as-yet-unknown payload.

"The attacker likely monitored the recurring GET requests from the malware and selectively delivered payloads to specific victims," ENKI said.

In another campaign observed in April 2026, a counterfeit web page mimicking Cisco Webex is said to have been used to display a pop-up message urging the victim to download and run a script to address issues with accessing the camera. Doing so results in the retrieval of a ZIP archive containing an encrypted JavaScript (JSE) file ("fix-camera.jse").

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8doGyhBdCMrdajLAo1uLfUdOuonnQxBL_Q8P4f8uJM1J027h3_WZP3pAroSoUKTre8VtoDPZpRYrkgpaRMIAcIzMZM_zwlK3pFYZ0f0eosqIA_IncLFzuYchkxQhkzimHpWieieGuDtFBYs08xpoKuxgpQsdENty_LGkS9Yzw6XyspuAlsPEos0Rc_Dup/s1700-e365/spoofing.jpg)

The execution of the JSE file results in the deployment of an intermediate downloader ("mTSTCv8.mdxm") using PowerShell, which then runs anti-analysis checks and contacts a C2 server to fetch the next-stage malware ("engine.dat" or "spyInster.dll"). In the final stage, the DLL drops a loader component ("cacheMon.dat") that, in turn, executes HTTPSpy on the compromised system.

HTTPSpy is a full-featured remote access trojan that supports a wide range of capabilities to run shell commands, upload/download files, execute processes, capture screenshots, inject DLL paths into specified PID processes, and erase itself from the endpoint.

This is not the first time Kimsuky has deployed HTTPSpy. In its 2025 European Threat Landscape Report, CrowdStrike [said](https://www.crowdstrike.com/en-us/resources/reports/2025-european-threat-landscape-report/) the hacking group likely targeted a German defense manufacturer's employees via a credential phishing campaign deploying the malware between May 2024 and at least September 2024. The first use of HTTPSpy dates back to 2022.

Simultaneously, the malware also drops and opens an HTML file named "meeting.html," which immediately redirects the victim to a Webex meeting room. Accessing the URL opens a legitimate Webex meeting room associated with an actual scheduled event that took place around the same time.

"This indicates that the attacker likely compromised a service member's device or account to obtain the meeting schedule, then crafted a fake meeting page to distribute malware to the other attendees," the cybersecurity company said.

ENKI said it also discovered additional fake web pages that query a local server set up by the malware on the victim's machine via JSONP (JSON with Padding) to verify malware execution status and display an installation prompt if it's not running. The technique has been codenamed JSONPing. However, the exact nature of the downloaded malware remains unknown as the URL is currently inactive.

"Kimsuky went beyond simple malware distribution, introducing sophisticated mechanisms to maximize delivery success, including real-time infection verification via JSONPing and crafting a fake page using a stolen meeting schedule," ENKI said.

### Kimsuky Evolves with HelloDoor and HttpMalice

The disclosure comes as Kaspersky detailed the threat actor'...