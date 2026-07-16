---
title: Researcher Drops New Windows Zero-Day PoC Hours After Microsoft Patch Tuesday
url: https://thehackernews.com/2026/07/researcher-drops-new-windows-zero-day.html
source: The Hacker News
date: 2026-07-15
fetch_date: 2026-07-16T04:58:59.763218
---

# Researcher Drops New Windows Zero-Day PoC Hours After Microsoft Patch Tuesday

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Researcher Drops New Windows Zero-Day PoC Hours After Microsoft Patch Tuesday](https://thehackernews.com/2026/07/researcher-drops-new-windows-zero-day.html)

**Ravie Lakshmanan**Jul 15, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvtiVnhkF-YVsPEXyedqj9REY5pN1-KiSsf-rCeXK5yClGbAcsL1Tg7-9UDDA8VQg5RbM0uWkV23rDxqiFFIJ2RkpkY6cn90-5LPbZOC2oktF7_3FjD5La_FGkYdVBEKeXMJGiGRZfPvxmMBXd99tncWdEZ4HxX62hbxmWEnA02eu-LSVwZtmecjuykqDb/s1700-e365/windows-0day.jpg)

Security researcher **Chaotic Eclipse** (aka **Nightmare-Eclipse**) has [released](https://blog.projectnightcrawler.dev/posts/2026-07-14-legacyhive-public-disclosure/) a new proof-of-concept (PoC) exploit called LegacyHive.

It has been described as a Windows User Profile Service arbitrary hive load elevation of privileges vulnerability. The Windows User Profile Service, also referred to as ProfSvc, is a core system component that manages user accounts and environments.

"The PoC requires another standard user credential and a third username (which can be an administrator account)," Chaotic Eclipse [said](https://git.projectnightcrawler.dev/NightmareEclipse/LegacyHive). "If the PoC is successful, it will end up mounting the target user hive in the current user classes root."

The researcher said the exploit was stripped down to prevent public exploitation, adding the original exploit did not require additional user credentials and was not limited to the "usrclass.dat" hive.

"Any hive could be loaded using this vulnerability, but you would need some brain cells to make the PoC do it," the researcher noted.

What makes it notable is that it's functional on all supported desktop and server versions of Windows, including those running the latest July 2026 Patch Tuesday update.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Chaotic Eclipse and Microsoft have been [locked in a heated dispute](https://thehackernews.com/2026/05/microsoft-slams-public-zero-day.html) since at least April 2026, with the researcher releasing details of multiple exploits before the Windows maker had a chance to patch them, citing a breakdown in communication. Three of the vulnerabilities in Microsoft Defender came under active exploitation shortly after public disclosure.

Earlier this month, the tech giant released security updates for another Defender vulnerability known as RoguePlanet that was disclosed by the researcher. However, it emerged that the newly introduced "defense-in-depth updates" to address the flaw can cause Microsoft Defender to leak 8 bytes of data when attempting to open a file in certain scenarios.

Microsoft [told](https://thehackernews.com/2026/07/microsoft-patches-rogueplanet-defender.html) The Hacker News that it's investigating the new report. We have contacted the company for comment regarding LegacyHive, and we will update the story if we hear back.

### SharePoint Server Flaws in Spotlight

The development comes as Microsoft shipped patches for a [record 622 flaws](https://thehackernews.com/2026/07/microsoft-patches-record-622-flaws.html), including two privilege escalation shortcomings in SharePoint Server (CVE-2026-56164, CVSS score: 5.3) and Active Directory Federation Services (CVE-2026-56155, CVSS score: 7.8) that have been flagged as actively exploited.

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has [added](https://www.cisa.gov/news-events/alerts/2026/07/14/cisa-adds-four-known-exploited-vulnerabilities-catalog) both vulnerabilities to its Known Exploited Vulnerabilities ([KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)) catalog, which mandates that Federal Civilian Executive Branch (FCEB) agencies apply the fixes by July 17 and July 28, 2026, respectively.

"After years of relative stability, the Patch Tuesday process has experienced significant turbulence so far in 2026," Adam Barnett, lead software engineer at Rapid7, said in a statement. "As well as the AI-fuelled exponential growth of vulnerability reporting and discovery, Microsoft is grappling with the emergence of a series of vulnerabilities disclosed in such a way as to bring maximum discomfort for Redmond."

In a separate advisory, the agency [said](https://www.cisa.gov/news-events/alerts/2026/07/14/cisa-urges-sharepoint-hardening-after-new-exploitations) it's aware of active exploitation of multiple SharePoint Server flaws, including [CVE-2026-32201](https://www.cve.org/CVERecord?id=CVE-2026-32201), [CVE-2026-45659](https://www.cve.org/CVERecord?id=CVE-2026-45659), and CVE-2026-56164, that enable cyber threat actors to gain unauthorized access to susceptible instances.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHcvlLVmAqlffm6kG54_0cGVf8WfcgzqT9B0fBSizSSeIjh8tBepXnrf6BMqKiG344WgqNejcRtEFKT1PmOzQNQBhdmu2iz9Po10z0SSDlFuZ37iip2uYibJDoxTEkbUI7Bx8NJM2Io_z_nl5p4YA-ZhqFLfi0GW1axyu-lQx-iytCn9RGSJ2iqCwdyv8m/s1600/sy-d-2.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-2)

"These vulnerabilities affect all supported on-premises SharePoint Server versions (Subscription Edition, 2019, and 2016) and involve establishing remote code execution (RCE) and post-exploitation activities, such as stealing Internet Information Services (IIS) machine keys and performing deserialization techniques, to gain persistence and deploy malware," CISA said.

"The flaw stems from missing authentication for a critical function, enabling an attacker to reach functionality that should require authorization," Alex Vovk, CEO and co-founder of Action1, said about CVE-2026-56164.

"An attacker can send specially crafted network requests to access functionality that should require authentication, resulting in privilege escalation. The vulnerability primarily impacts system integrity by allowing unauthorized actions without requiring prior authentication or user interaction. Internet-facing SharePoint servers a...