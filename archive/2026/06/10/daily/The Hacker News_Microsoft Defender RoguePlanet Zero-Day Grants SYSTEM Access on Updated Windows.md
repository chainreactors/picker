---
title: Microsoft Defender RoguePlanet Zero-Day Grants SYSTEM Access on Updated Windows
url: https://thehackernews.com/2026/06/microsoft-defender-rogueplanet-zero-day.html
source: The Hacker News
date: 2026-06-10
fetch_date: 2026-06-11T06:37:06.665686
---

# Microsoft Defender RoguePlanet Zero-Day Grants SYSTEM Access on Updated Windows

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Microsoft Defender RoguePlanet Zero-Day Grants SYSTEM Access on Updated Windows](https://thehackernews.com/2026/06/microsoft-defender-rogueplanet-zero-day.html)

**Ravie Lakshmanan**Jun 10, 2026Zero-Day / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibnTGKGBThpUUZgwRx8hcclb0nuPbrV9o3MSZhFoGEp_3DLGRzdJVpj8Xfrnk1cEPUu76_u8R5Lpt10tcaWPUlbHMwbY225I3jyiBx91pYb4dmdBFbDYVai8DS3UcXAk98dTqEuyW0r3D5c2OaHHaXJzRyCAwS32tpmB83cAJRwKxI4GIT2iGnrdBI_EV7/s1700-e365/windows-exploit.jpg)

The anonymous security researcher going by the name Chaotic Eclipse (aka Nightmare-Eclipse) has [released](https://deadeclipse666.blogspot.com/2026/06/its-patch-tuesday.html) a proof-of-concept (PoC) exploit for yet another Microsoft Defender zero-day named **RoguePlanet**.

"The exploit is a race condition, so it's a hit or miss," the researcher, who published the exploit under a new GitHub account "MSNightmare" [said](https://github.com/MSNightmare/RoguePlanet). "I have managed to get a 100% success rate on some machines while it struggled to work on others."

Should the exploit succeed, the result is a shell with SYSTEM-level privileges, granting the attacker the ability to run arbitrary code or perform unauthorized actions.

The researcher said the exploit has been tested on Windows 11 and 10 machines with the June 2026 Patch Tuesday updates installed, meaning the exploit works on the up-to-date versions of the desktop operating system.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

That said, the exploit does not work on Windows Server instances in its current form since "standard users cannot mount an ISO image." Chaotic Eclipse emphasized that Windows Server installations are also vulnerable to the flaw and that the exploit needs to be redesigned for it to work.

"Getting this PoC to work genuinely drained my soul, it severely degraded my mental and physical health but in the end of May [sic], a full PoC was developed," the researcher said.

"Microsoft's efforts to protect Defender from path redirection attacks are useless, I have a batch of memory corruption vulnerabilities in defender as well and not to mention the other batch of vulnerabilities I have in several other components."

*Video Credit: [ThreatLocker](https://x.com/ThreatLocker/status/2064462208793202873)*

Security researcher Will Dormann, in a post [shared](https://infosec.exchange/%40wdormann/116722435763533255) on Mastodon, said "it's reportedly not 100% reliable, but it worked on the first attempt for me."

RoguePlanet is the latest in a series of Microsoft Defender flaws uncovered by Chaotic Eclipse in recent months -

* [BlueHammer](https://thehackernews.com/2026/04/three-microsoft-defender-zero-days.html) (CVE-2026-33825)
* [UnDefend](https://thehackernews.com/2026/05/microsoft-warns-of-two-actively.html) (CVE-2026-45498)
* [RedSun](https://thehackernews.com/2026/05/microsoft-warns-of-two-actively.html) (CVE-2026-41091)

These uncoordinated disclosures are part of what's assessed to be a retaliatory effort following an alleged breakdown in communication between the researcher, who has not publicly identified themselves, and Microsoft.

In cryptographically signed posts on their Blogger page, Chaotic Eclipse expressed dissatisfaction with the way Microsoft handled the disclosure process and called out the company for revoking access to their Microsoft Security Response Center (MSRC) account, where researchers can report vulnerabilities. The researcher has also accused Redmond of humiliating them, dismissing their reports, failing to compensate them for the identified vulnerabilities, and defaming them.

Late last month, Microsoft [condemned](https://thehackernews.com/2026/05/microsoft-slams-public-zero-day.html) the public vulnerability disclosures, stating they are "never justifiable" and put customers at "unnecessary risk." It's worth noting that all three aforementioned Defender vulnerabilities have since been exploited in the wild.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

The public feud has also resulted in the takedown of their GitHub and GitLab accounts. "Microsoft is attempting to misuse its ownership of GitHub to protect only its own products, and misuse its extensive links to law enforcement by branding publishing information about vulnerabilities in its own products as criminal behaviour," security researcher Kevin Beaumont [said](https://doublepulsar.com/microsofts-stance-on-zero-day-exploits-is-a-dumpster-fire-of-their-own-making-0946117940a4).

"To be clear about our approach to legal matters, we have no intention to pursue action against individuals conducting or publishing their security research," Microsoft [said](https://x.com/msftsecresponse/status/2061293718942908925) in an X post. "When an individual breaks the law and engages in malicious activity causing real harm to our customers, we will work with law enforcement as appropriate."

"We are committed to approaching every interaction with transparency, clear communication, and professionalism. We continue to believe strongly in Coordinated Vulnerability Disclosure as the foundation for protecting customers and improving our products."

### Update

When reached for comment, a Microsoft spokesperson shared the below statement with The Hacker News -

*Microsoft is aware of the reported vulnerability and is actively investigating the validity and potential applicability of these claims. Microsoft is committed to investigating security issues and updating impacted products to protect customers as soon as possible. Importantly, we support coordinated vulnerability disclosure, an industry standard that protects customers and supports the research community by ensuring their findings are thoroughly investigated and addressed before being made public.*

*(The story was updated after publication to include a response from Microsoft.)*

Found this...