---
title: North Korean APT43 Uses PowerShell and Dropbox in Targeted South Korea Cyberattacks
url: https://thehackernews.com/2025/02/north-korean-apt43-uses-powershell-and.html
source: The Hacker News
date: 2025-02-14
fetch_date: 2025-10-06T20:39:38.066480
---

# North Korean APT43 Uses PowerShell and Dropbox in Targeted South Korea Cyberattacks

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

# [North Korean APT43 Uses PowerShell and Dropbox in Targeted South Korea Cyberattacks](https://thehackernews.com/2025/02/north-korean-apt43-uses-powershell-and.html)

**Feb 13, 2025**Ravie LakshmananUnited States

[![South Korea Cyberattacks](data:image/png;base64... "South Korea Cyberattacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjUK_l8y76ePfgjY51HPnR1W1fNUGGT1qEoPKpBpxWBZd63ojYgv30SQjWwxcv9VxxO5g54Hvka3BNyuGpkHXMK-26j50Kjf9NT9GN6Dyl88Ykcb8BcMO8oMEO-I87E64yKNobhKuzVwfmZw0-nCJDL0U6TEsnjHu5RCaaKc9xY1eTj8a8oXB78-iRZIdLe/s790-rw-e365/malware-attack.png)

A nation-state threat actor with ties to North Korea has been linked to an ongoing campaign targeting South Korean business, government, and cryptocurrency sectors.

The attack campaign, dubbed **DEEP#DRIVE** by Securonix, has been attributed to a hacking group known as [Kimsuky](https://thehackernews.com/2025/02/north-korean-hackers-exploit-powershell.html), which is also [tracked](https://www.cyfirma.com/research/apt-profile-apt43/) under the names APT43, Black Banshee, Emerald Sleet, Sparkling Pisces, Springtail, TA427, and Velvet Chollima.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Leveraging tailored phishing lures written in Korean and disguised as legitimate documents, the attackers successfully infiltrated targeted environments," security researchers Den Iuzvyk and Tim Peck [said](https://www.securonix.com/blog/analyzing-deepdrive-north-korean-threat-actors-observed-exploiting-trusted-platforms-for-targeted-attacks/) in a report shared with The Hacker News, describing the activity as a "sophisticated and multi-stage operation."

The decoy documents, sent via phishing emails as .HWP, .XLSX, and .PPTX files, are disguised as work logs, insurance documents and crypto-related files to trick recipients into opening them, thereby triggering the infection process.

The attack chain is notable for its heavy reliance on PowerShell scripts at various stages, including payload delivery, reconnaissance, and execution. It's also characterized by the use of Dropbox for payload distribution and data exfiltration.

[![South Korea Cyberattacks](data:image/png;base64... "South Korea Cyberattacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgziQKBW89E9CrVk0PbcvbN8dupUdlOYjlQaLDCG-JlWweNXOkv0LwhT7i3W8OoIr81TdthzQH9G-ozwIhRfbGX2nRToAWoNhI8zizOwkz648Yua8N3dLikw_CGh_BNq27fWOhcrBafGx5fj1pT3sTRQj8FFHHB6fgSLOZsKz7o6srLJqwmPEsyPTK5Eiy4/s790-rw-e365/cyberattack.png)

It all starts with a ZIP archive containing a single Windows shortcut (.LNK) file that masquerades as a legitimate document, which, when extracted and launched, triggers the execution of PowerShell code to retrieve and display a lure document hosted on Dropbox, while stealthily establishing persistence on the Windows host via a scheduled task named "ChromeUpdateTaskMachine."

One such lure document, written in Korean, pertains to a safety work plan for forklift operations at a logistics facility, delving into the safe handling of heavy cargo and outlining ways to ensure compliance with workplace safety standards.

The PowerShell script is also designed to contact the same Dropbox location to fetch another PowerShell script that's responsible for gathering and exfiltrating system information. Furthermore, it drops a third PowerShell script that's ultimately responsible for executing an unknown .NET assembly.

"The use of OAuth token-based authentication for Dropbox API interactions allowed seamless exfiltration of reconnaissance data, such as system information and active processes, to predetermined folders," the researchers said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"This cloud-based infrastructure demonstrates an effective yet stealthy method of hosting and retrieving payloads, bypassing traditional IP or domain blocklists. Additionally, the infrastructure appeared dynamic and short-lived, as evidenced by the rapid removal of key links after initial stages of the attack, a tactic that not only complicates analysis but also suggests the attackers actively monitor their campaigns for operational security."

Securonix said it was able to leverage the OAuth tokens to gain additional insights into the threat actor's infrastructure, finding evidence that the campaign may have been underway since September last year.

"Despite the missing final stage, the analysis highlights the sophisticated techniques employed, including obfuscation, stealthy execution, and dynamic file processing, which demonstrate the attacker's intent to evade detection and complicate incident response," the researchers concluded.

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
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[APT group](https://thehackernews.com/search/label/APT%20group)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data exfiltration](https://thehackernews.com/search/label/data%20exfiltration)[Digital Espionage](https://thehackernews.com/search/label/Digital%20Espionage)[dropbox](https://thehackernews.com/search/label/dropbox)[Malware](https://thehackernews.com...