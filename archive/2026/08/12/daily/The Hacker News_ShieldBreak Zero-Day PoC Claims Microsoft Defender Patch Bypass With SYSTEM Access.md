---
title: ShieldBreak Zero-Day PoC Claims Microsoft Defender Patch Bypass With SYSTEM Access
url: https://thehackernews.com/2026/08/shieldbreak-zero-day-poc-claims.html
source: The Hacker News
date: 2026-08-12
fetch_date: 2026-08-13T04:05:21.560918
---

# ShieldBreak Zero-Day PoC Claims Microsoft Defender Patch Bypass With SYSTEM Access

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

![cybersecurity](data:image/svg+xml;base64...)

# [ShieldBreak Zero-Day PoC Claims Microsoft Defender Patch Bypass With SYSTEM Access](https://thehackernews.com/2026/08/shieldbreak-zero-day-poc-claims.html)

**Ravie Lakshmanan**Aug 12, 2026Zero-Day / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fX7D-qoT4QD3pjSuUtavTiarjtyitt3-JMji-nzNa8XTKefzPp2QGMAR6FkLA8r8Ll9VVFHCMEJSKWgi5Gk0GOdYU4RA1itDyf8ZQc12IXczcxoGHKXcJ9GAWUv-fPaRhRXnDyFfxo9nhjQoJbBPxQQbixY9RxaR_Oz_NrHD2P_EMER6yKTV3nWCSAoq/s1700-e365/zero-day.jpg)

The security researcher going by the name Chaotic Eclipse (aka INFINITE NIGHTMARE, MSNightmare, and Nightmare-Eclipse) has [released](https://blog.projectnightcrawler.dev/posts/2026-08-11-shieldbreak-august-2026-disclosure/) a proof-of-concept (PoC) for a new Microsoft zero-day called **ShieldBreak**.

The vulnerability, rooted in Microsoft Defender for Windows, demonstrates a patch bypass for CVE-2026-50656 (CVSS score: 7.8), otherwise known as [RoguePlanet](https://thehackernews.com/2026/06/microsoft-defender-rogueplanet-zero-day.html).

RoguePlanet has been described as a race condition that, if successfully exploited, could grant an attacker the ability to spawn a shell with SYSTEM-level privileges, enabling them to run arbitrary code or perform unauthorized actions.

Although it was first disclosed by the researcher in June 2026, a patch for the vulnerability was not [released](https://thehackernews.com/2026/07/microsoft-patches-rogueplanet-defender.html) by Microsoft until almost a month later. The tech giant described it as a privilege escalation issue in the Microsoft Malware Protection Engine ("mpengine.dll").

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

Soon after, Chaotic Eclipse said the "defense-in-depth updates" introduced by Microsoft to address CVE-2026-50656 can cause Defender to leak 8 bytes of data when attempting to open a file in certain scenarios on Windows 11 25H2 and Windows Server 2025. Microsoft told The Hacker News at the time that it's aware of the report and is investigating.

ShieldBreak, on the other hand, is assessed to be a full patch bypass for CVE-2026-50656, with the researcher claiming that "Microsoft has failed to properly patch the RoguePlanet vulnerability."

"The PoC was tested in the latest version of Windows 11 25h2 (+Canary channel) and Windows Server 2025, the PoC also have a 100% success rate," the researcher added. "Please note that Windows 10 (and respective server editions) are not currently supported, they are however vulnerable to ShieldBreak as well."

The Hacker News has contacted Microsoft, and we will update the story if we hear back.

The development comes as the Windows maker [shipped](https://thehackernews.com/2026/08/microsoft-patches-398-flaws-including.html) patches for [421 security flaws](https://msrc.microsoft.com/update-guide/releaseNote/2026-Aug), including 236 flaws in Windows. One of the patches involves [CVE-2026-62832](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62832) (CVSS score: 7.8), a Windows User Profile Service privilege escalation vulnerability that was disclosed by Chaotic Eclipse last month under the name [LegacyHive](https://thehackernews.com/2026/07/researcher-drops-new-windows-zero-day.html).

"Improper link resolution before file access ('link following') in Windows User Profile Service allows an authorized attacker to elevate privileges locally," Microsoft said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

"An authenticated attacker who has credentials for another local account could run a specially crafted application to load another user's registry hive. Successful exploitation could allow the attacker to access or modify another user's data and gain administrator privileges. User interaction is not required."

Also remediated by Microsoft is an actively exploited zero-day in the Windows Ancillary Function Driver for WinSock ([CVE-2026-68820](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-68820), CVSS score: 7.0) that grants SYSTEM privileges and a publicly disclosed Windows Container Isolation FS Filter Driver (unionfs.sys) tampering vulnerability ([CVE-2026-72971](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-72971), CVSS score: 5.5).

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has since [added](https://www.cisa.gov/news-events/alerts/2026/08/11/cisa-adds-three-known-exploited-vulnerabilities-catalog) CVE-2026-68820 to its Known Exploited Vulnerabilities ([KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)) catalog, requiring federal agencies to apply the fixes by August 25, 2026.

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

[endpoint security](https://thehackernews.com/search/label/endpoint%20security), [exploit](https://thehackernews.com/search/label/exploit), [Microsoft](https://thehackernews.com/search/label/Microsoft), [Patch Management](https://thehackernews.com/search/label/Patch%20Management), [privilege escalation](https://thehackernews.com/search/label/privilege%20escalation), [Software Security](https://thehackernews.com/search/label/Software%20Security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Windows Security](https://thehackernews.com/search/label/Windows%20Security), [Zero-Day](https://thehackernews.com/search/label/Zero-Day)

⚡ Top Stories This Week

[![Azure Co...