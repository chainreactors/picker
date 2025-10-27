---
title: Microsoft Rolls Out Patches for 80 New Security Flaws — Two Under Active Attack
url: https://thehackernews.com/2023/03/microsoft-rolls-out-patches-for-80-new.html
source: The Hacker News
date: 2023-03-16
fetch_date: 2025-10-04T09:46:19.815840
---

# Microsoft Rolls Out Patches for 80 New Security Flaws — Two Under Active Attack

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

# [Microsoft Rolls Out Patches for 80 New Security Flaws — Two Under Active Attack](https://thehackernews.com/2023/03/microsoft-rolls-out-patches-for-80-new.html)

**Mar 15, 2023**Ravie LakshmananPatch Tuesday / Software Update

[![Microsoft Patch Tuesday Updates](data:image/png;base64... "Microsoft Patch Tuesday Updates")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYLlUAr0ruzgKuzoHoe1e0B8I4qsuhNp0XiA-FfqB6QFh3Aa4J0x4W0015PvXO6_-wLDns2apQkiblNma4ax6vJ3hNIfz6MSsxDPLIAUvgUk5gMjurzSI-0rwUwYe9rBJRxWQKbXqWFFzZAMGqCG12X0aivvmUmU6xFvbwG8g2ST4LOTBt3e521HfX/s790-rw-e365/windows-update.jpg)

Microsoft's Patch Tuesday update for March 2023 is rolling out with remediations for a set of [80 security flaws](https://msrc.microsoft.com/update-guide/releaseNote/2023-Mar), two of which have come under active exploitation in the wild.

Eight of the 80 bugs are rated Critical, 71 are rated Important, and one is rated Moderate in severity. The updates are in [addition to 29 flaws](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnotes-security) the tech giant fixed in its Chromium-based Edge browser in recent weeks.

The two vulnerabilities that have come under active attack include a Microsoft Outlook privilege escalation flaw ([CVE-2023-23397](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23397), CVSS score: 9.8) and a Windows SmartScreen security feature bypass ([CVE-2023-24880](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-24880), CVSS score: 5.1).

CVE-2023-23397 is "triggered when an attacker sends a message with an extended MAPI property with a UNC path to an SMB (TCP 445) share on a threat actor-controlled server," Microsoft [said](https://msrc.microsoft.com/blog/2023/03/microsoft-mitigates-outlook-elevation-of-privilege-vulnerability/) in a standalone advisory.

A threat actor could leverage this flaw by sending a specially crafted email, activating it automatically when it is retrieved and processed by the Outlook client for Windows. As a result, this could lead to exploitation without requiring any user interaction and before even the message is viewed in the Preview Pane.

Microsoft credited the Computer Emergency Response Team of Ukraine (CERT-UA) with reporting the flaw, adding it is aware of "limited targeted attacks" mounted by a Russia-based threat actor against government, transportation, energy, and military sectors in Europe.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

CVE-2023-24880, on the other hand, concerns a security bypass flaw that could be exploited to evade Mark-of-the-Web (MotW) protections when opening untrusted files downloaded from the internet.

It is also the consequence of a narrow patch released by Microsoft to resolve another SmartScreen bypass bug ([CVE-2022-44698](https://thehackernews.com/2022/12/december-2022-patch-tuesday-get-latest.html), CVSS score: 5.4) that came to light last year and which was [exploited](https://thehackernews.com/2022/10/unofficial-patch-released-for-new.html) by financially motivated actors to deliver Magniber ransomware.

"Vendors often release narrow patches, creating an opportunity for attackers to iterate and discover new variants," Google Threat Analysis Group (TAG) researcher Benoit Sevens [said](https://blog.google/threat-analysis-group/magniber-ransomware-actors-used-a-variant-of-microsoft-smartscreen-bypass/) in a report.

"Because the root cause behind the SmartScreen security bypass was not addressed, the attackers were able to quickly identify a different variant of the original bug."

TAG said it observed over 100,000 downloads of malicious MSI files signed with malformed Authenticode signature since January 2023, thereby permitting the adversary to distribute Magniber ransomware without raising any security warnings. A majority of those downloads have been associated with users in Europe.

[![Microsoft](data:image/png;base64... "Microsoft")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4X33PM-brfAmibmlYH5ciro-GTl4d6hM3mG7iaDoQ-MN0Hs9ae5Azddry2XoWri6NUXEItzDmBhuk2FblKj_8SAKXXI-PTPOJnIlDMztuDovcYBMuU1hBBOGb-33VH7yhCJpbpxl98LG5dudq7jmiFk9VoeluwTLBr3QMzHUn3-ZV7oUBB5Xir1Vvmg/s790-rw-e365/0day.png)

The disclosure comes as the U.S. Cybersecurity and Infrastructure Security Agency (CISA) [added](https://www.cisa.gov/news-events/alerts/2023/03/14/cisa-adds-three-known-exploited-vulnerabilities-catalog) the two flaws to the Known Exploited Vulnerabilities ([KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)) catalog and [announced](https://www.cisa.gov/news-events/news/cisa-establishes-ransomware-vulnerability-warning-pilot-program) a new [pilot program](https://www.cisa.gov/stopransomware/Ransomware-Vulnerability-Warning-Pilot) that aims to warn critical infrastructure entities about "vulnerabilities commonly associated with known ransomware exploitation."

Also closed out by Microsoft are a number of critical remote code execution flaws impacting HTTP Protocol Stack ([CVE-2023-23392](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23392), CVSS score: 9.8), Internet Control Message Protocol ([CVE-2023-23415](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23415), CVSS score: 9.8), and Remote Procedure Call Runtime ([CVE-2023-21708](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21708), CVSS score: 9.8).

Other notable mentions include patches for four privilege escalation bugs identified in the Windows Kernel, 10 remote code execution flaws affecting Microsoft PostScript and PCL6 Class Printer Driver, and a [WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/) spoofing vulnerability in the Edge browser.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Microsoft also remedied two information disclosure flaws in OneDrive for Android ([CVE-2023-24882](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-24882) and [C...