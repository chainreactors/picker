---
title: Operation Soft Cell: Chinese Hackers Breach Middle East Telecom Providers
url: https://thehackernews.com/2023/03/operation-soft-cell-chinese-hackers.html
source: The Hacker News
date: 2023-03-24
fetch_date: 2025-10-04T10:32:52.733563
---

# Operation Soft Cell: Chinese Hackers Breach Middle East Telecom Providers

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

# [Operation Soft Cell: Chinese Hackers Breach Middle East Telecom Providers](https://thehackernews.com/2023/03/operation-soft-cell-chinese-hackers.html)

**Mar 23, 2023**Ravie LakshmananCritical Infrastructure Security

[![Middle East Telecom](data:image/png;base64... "Middle East Telecom")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSDDNt_yQZ44jk5yMbKuj9hJRtCL6OzY0dsZRqrgmXalole3xVk5RCrsYmXnX6mo11SuTqhpfgk6DFUxzArEPbOqDiMZ8Cf5TaResgkRS6RRxgtfj4Kwficak3arfierkvXw7Gz8gF_A3SNSLZLsG4CmWOEGY2mWImP9O6G1uwpDoSDnEpim1xrQgx/s790-rw-e365/telecom.png)

Telecommunication providers in the Middle East are the subject of new cyber attacks that commenced in the first quarter of 2023.

The intrusion set has been attributed to a Chinese cyber espionage actor associated with a long-running campaign dubbed **Operation Soft Cell** based on tooling overlaps.

"The initial attack phase involves infiltrating Internet-facing Microsoft Exchange servers to deploy web shells used for command execution," researchers from SentinelOne and QGroup said in a [new technical report](https://www.sentinelone.com/labs/operation-tainted-love-chinese-apts-target-telcos-in-new-attacks/) shared with The Hacker News.

"Once a foothold is established, the attackers conduct a variety of reconnaissance, credential theft, lateral movement, and data exfiltration activities."

Operation Soft Cell, according to [Cybereason](https://thehackernews.com/2021/08/chinese-hackers-target-major-southeast.html), refers to malicious activities undertaken by China-affiliated actors targeting telecommunications providers since at least 2012.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The Soft Cell threat actor, also tracked by Microsoft as [Gallium](https://www.microsoft.com/en-us/security/blog/2019/12/12/gallium-targeting-global-telecom/), is known to target unpatched internet-facing services and use tools like [Mimikatz](https://attack.mitre.org/software/S0002/) to obtain credentials that allows for lateral movement across the targeted networks.

Also put to use by the adversarial collective is a "difficult-to-detect" backdoor codenamed [PingPull](https://thehackernews.com/2022/06/chinese-gallium-hackers-using-new.html) in its espionage attacks directed against companies operating in Southeast Asia, Europe, Africa, and the Middle East.

Central to the latest campaign is the deployment of a custom variant of Mimikatz referred to as mim221, which packs in new anti-detection features.

"The use of special-purpose modules that implement a range of advanced techniques shows the threat actors' dedication to advancing its toolset towards maximum stealth," the researchers said, adding it "highlights the continuous maintenance and further development of the Chinese espionage malware arsenal."

The attacks ultimately proved to be unsuccessful, with the breaches detected and blocked before any implants could be deployed on the target networks.

[![Operation Soft Cell](data:image/png;base64... "Operation Soft Cell")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjfc5g1xurZac7ZibnUcHmYhirfTDVnFdDpzW70kSNYHMrxXLsCQ5y8opHCyUxMGtEQtr_2uiMYnkeDcOLJQvhl7GDQE1Ukovy3aFbyKXmGfwYPLbfPoaXXIVhI4XSIm5x82oNgFnJmUoxf0UUze7yO1Lw7C1gZVI7_Xou64fxbjs4eLIMjMkccEl_f/s790-rw-e365/labs.png)

Prior research into Gallium suggests [tactical similarities](https://raw.githubusercontent.com/yt0ng/cracking_softcell/main/Cracking_SOFTCLL_TLP_WHITE.pdf) [PDF] with multiple Chinese nation-state groups such as [APT10](https://thehackernews.com/2022/11/chinese-hackers-using-new-stealthy.html) (aka Bronze Riverside, Potassium, or Stone Panda), [APT27](https://thehackernews.com/2023/03/sysupdate-malware-strikes-again-with.html) (aka Bronze Union, Emissary Panda, or Lucky Mouse), and [APT41](https://thehackernews.com/2022/08/china-backed-apt41-hackers-targeted-13.html) (aka Barium, Bronze Atlas, or Wicked Panda).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This once again points to signs of closed-source tool-sharing between Chinese state-sponsored threat actors, not to mention the possibility of a "[digital quartermaster](https://thehackernews.com/2023/03/from-ransomware-to-cyber-espionage-55.html)" responsible for maintaining and distributing the toolset.

The findings come amid revelations that various other hacking groups, including [BackdoorDiplomacy](https://thehackernews.com/2022/12/chinese-hackers-target-middle-east.html) and [WIP26](https://thehackernews.com/2023/02/new-threat-actor-wip26-targeting.html), have set their sights on telecom service providers in the Middle East region.

"Both of those are entirely unrelated to the [Soft Cell] activity," Juan Andres Guerrero-Saade (JAG-S), senior director of SentinelLabs at SentinelOne, told The Hacker News. "It speaks more to the importance placed by Chinese taskers towards targeting these verticals."

"CN ops display an almost redundant style of having multiple threat groups often attack the same targets in an uncoordinated fashion. It's not uncommon to find multiple CN threat groups (unwittingly?) cohabitating in the same victim environment."

"Chinese cyber espionage threat actors are known to have a strategic interest in the Middle East," the researchers concluded.

"These threat actors will almost certainly continue exploring and upgrading their tools with new techniques for evading detection, including integrating and modifying publicly available code."

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
[**Share on Facebook](#l...