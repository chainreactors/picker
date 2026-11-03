---
title: DarkBlinders Compromises Israeli Target and Iraqi Kurdish Government Cloud Environment
url: https://thehackernews.com/2026/11/darkblinders-compromises-israeli-target.html
source: The Hacker News
date: 2026-11-02
fetch_date: 2026-11-03T08:51:44.938137
---

# DarkBlinders Compromises Israeli Target and Iraqi Kurdish Government Cloud Environment

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [DarkBlinders Compromises Israeli Target and Iraqi Kurdish Government Cloud Environment](https://thehackernews.com/2026/11/darkblinders-compromises-israeli-target.html)

**Ravie Lakshmanan**Nov 02, 2026Cyber Espionage / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg7nIwDn7LIoF8OUZdj0NRjq4ZMu-xjzcOPQJDwouwkwqwVe618e77am9iyAIez63Q8jVqZi7OtU43gJlhbZT-_4l_4pUq3tYpDUe4ErouPlkNi8YTNZiPQ6KmX2Ci028oT24DRcPtCdKv_zZ33_ZHOodARrbmcwxYWCAx4r45Qc0qVOQNmCCoWZmAWJnzt/s1700-nu-rw-lo-l85-e365/shelby-hacker.png)

Cybersecurity researchers have disclosed details of a cyber espionage campaign targeting Israel and the Kurdistan Region of Iraq by an Iran state-aligned threat actor between August and October 2026.

According to a report [published](https://dreamgroup.com/blog/darkblinders-inside-an-active-espionage-campaign) by Dream Research Labs, the campaign has led to the compromise of a high-profile individual in Israel, along with additional compromises affecting a government cloud environment in the Kurdistan Region.

The activity has been attributed to a threat actor known as **DarkBlinders**, an Iran-nexus group assessed to be active since at least September 2024 and linked to attacks aimed at aviation infrastructure and telecommunications in the U.A.E. and Iraq. It exhibits no technical overlap with other known hacking groups.

Attacks mounted by the group are known to rely on spear-phishing as an initial access pathway to lure recipients into opening trojanized utilities or clicking on attacker-controlled websites that host similar tools as direct downloads.

Previous attack chains documented by [Elastic Security Labs](https://thehackernews.com/2025/04/new-malware-loaders-use-call-stack.html#shelby-malware-uses-github-for-command-and-control) and [Group-IB](https://www.group-ib.com/masked-actors/darkblinders/) have led to the deployment of SHELBYLOADER (aka HOTAIR), which is launched via DLL sideloading to ultimately execute a backdoor called SHELBYC2 (aka AEROSTAT) that uses GitHub for command-and-control (C2), data exfiltration, and remote control. Elastic is tracking the threat cluster under the moniker REF8685.

Then early last month, Palo Alto Networks shed light on a campaign dubbed Blinder Tunnel in which the threat actor, which it calls CL-STA-1178, was observed masquerading as the Dubai Airports IT department to distribute malware-laced coding challenges to high-value targets.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The [bogus recruitment scheme](https://thehackernews.com/2026/09/iranian-hackers-pose-as-recruiters-to.html) was first detected in late March 2026, although evidence indicates that the attackers were staging and testing attack infrastructure as far back as November 2025.

The social engineering campaign is assessed to have approached specific targets with lucrative job offers to trick them into executing a self-contained application that mimicked a career portal and instructed them to complete a questionnaire.

Submitting the questionnaire does not cause any data to be exfiltrated or initiate any response from an external domain. Instead, it's meant to serve as a harmless decoy and build credibility before delivering the next stage payload containing the malware in the form of a Microsoft Visual Studio project archive that's dressed up as a coding assessment.

The attack chain makes use of three techniques to establish persistent access: A malicious C# project ".csproj" file is used to trigger [AppDomainManager injection](https://thehackernews.com/2026/11/netamloader-malware-targets-government.html), followed by DLL sideloading to deliver an updated version of SHELBYLOADER (aka ShelbyLoader V2), which then launches SHELBYC2. Also deployed via SHELBYC2 is a tunneling utility called Blackwood.

"The attackers behind the activity used tailored social engineering techniques to masquerade as Dubai Airports recruiters, using a trojanized Visual Studio coding challenge to target a high-value job seeker based in Iraq," Unit 42 [said](https://unit42.paloaltonetworks.com/blinder-tunnel-targets-critical-infrastructure/).

"The campaign is characterized by misuse of built-in developer tools and DLL sideloading. Attackers also used AppDomainManager hijacking to bypass security monitors like [ETW](https://learn.microsoft.com/en-us/windows-hardware/test/wpt/event-tracing-for-windows) [Event Tracing for Windows]."

The latest findings from Dream show that the threat actor continues to rely on social engineering, while combining both credential phishing and malware delivery. This involves the use of government, webmail, and cloud-service lookalike domains to collect credentials or present attacker-controlled file downloads. Some of the highlighted domains include -

* gcc-sg[.]cloud/owa/auth/logon.aspx
* mfakuwait[.]online/owa/auth/logon.aspx
* moelcloud[.]online/drive/file/d/1JpH3ySmJpvX6TyGnF7C-S8qYiaoxyC5O

The threat actor has also been observed setting decoy brand domains for a fake videoconferencing application called StarkMeet (stark-meet[.]com, stark-meet[.]online, and stark-meet[.]website). Installing and launching the app leads to the execution of ShelbyLoader V2 and SHELBYC2.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg108vJy3jLgDQMX32qSLhTzfDHWpTiH8LI6ttGrNZterNOUNxiChnk31YPfBd3j3sTalBJrG_V2F0oXhxjiCY-32MfIlzquOIYjgFQQf_gXuWbGV5AkSqstDiYQnHbeOVrnqGraKKVS1jeM1zGQkao3KkeLJbGCu5t4jIJU7vJjnm6gfrypqx43hIJNbAN/s1700-nu-rw-lo-l85-e365/StarkMeet.png)

The development is also a sign that the threat actor is trying out different methods for malware delivery, ranging from coding assessments to counterfeit software.

Dream said the DarkBlinders activity belongs to the same operational cluster as [UNC5795](https://security.googlecloudcommunity.com/security-validation-5/validation-content-update-june-24-2026-7779) and Dust Specter, citing infras...