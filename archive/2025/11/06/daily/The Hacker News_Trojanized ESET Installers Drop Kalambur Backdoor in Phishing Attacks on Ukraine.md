---
title: Trojanized ESET Installers Drop Kalambur Backdoor in Phishing Attacks on Ukraine
url: https://thehackernews.com/2025/11/trojanized-eset-installers-drop.html
source: The Hacker News
date: 2025-11-06
fetch_date: 2025-11-07T03:11:54.693031
---

# Trojanized ESET Installers Drop Kalambur Backdoor in Phishing Attacks on Ukraine

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Trojanized ESET Installers Drop Kalambur Backdoor in Phishing Attacks on Ukraine](https://thehackernews.com/2025/11/trojanized-eset-installers-drop.html)

**Nov 06, 2025**Ravie LakshmananMalware / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJgTnRaxG26x8DH7Ls4GJHR837IVsXDgmZVGVAFPSaUr0X4T1L4SW86A1IiQ5xQpq4V6K3UGzTyCMT-YsMndBRtpkPCnNJJRiT00Md8zO0SFFuaRbQjaJVguUUPHQmnQmNrpZBLVxoqPUxqLfVpmqUHXgg6G8p_w13M4wqmIPXe5izThcbXU-NE85dW7W7/s790-rw-e365/software.jpg)

A previously unknown threat activity cluster has been observed impersonating Slovak cybersecurity company ESET as part of phishing attacks targeting Ukrainian entities.

The campaign, detected in May 2025, is tracked by the security outfit under the moniker **InedibleOchotense**, describing it as Russia-aligned.

"InedibleOchotense sent spear-phishing emails and Signal text messages, containing a link to a trojanized ESET installer, to multiple Ukrainian entities," ESET [said](https://www.welivesecurity.com/en/eset-research/eset-apt-activity-report-q2-2025-q3-2025/) in its APT Activity Report Q2 2025–Q3 2025 shared with The Hacker News.

InedibleOchotense is assessed to share tactical overlaps with a campaign [documented](https://thehackernews.com/2025/02/microsoft-uncovers-sandworm-subgroups.html) by EclecticIQ that involved the deployment of a backdoor called BACKORDER and by CERT-UA as [UAC-0212](https://thehackernews.com/2025/02/cert-ua-warns-of-uac-0173-attacks.html), which it describes as a sub-cluster within the Sandworm (aka APT44) hacking group.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

While the email message is written in Ukrainian, ESET said the first line uses a Russian word, likely indicating a typo or a translation error. The email, which purports to be from ESET, claims its monitoring team detected a suspicious process associated with their email address and that their computers might be at risk.

The activity is an attempt to capitalize on the widespread use of ESET software in the country and its brand reputation to trick recipients into installing malicious installers hosted on domains such as esetsmart[.]com, esetscanner[.]com, and esetremover[.]com.

The installer is designed to deliver the legitimate ESET AV Remover, alongside a variant of a C# backdoor dubbed Kalambur (aka SUMBUR), which uses the Tor anonymity network for command-and-control. It's also capable of dropping OpenSSH and enabling remote access via the Remote Desktop Protocol (RDP) on port 3389.

It's worth noting that CERT-UA, in a report [published](https://thehackernews.com/2025/10/from-phishing-to-malware-ai-becomes.html) last month, attributed a nearly identical campaign to [UAC-0125](https://thehackernews.com/2024/12/uac-0125-abuses-cloudflare-workers-to.html), another sub-cluster within Sandworm.

### Sandworm Wiper Attacks in Ukraine

Sandworm, per ESET, has continued to mount [destructive](https://thehackernews.com/2023/01/new-report-reveals-nikowiper-malware.html) [campaigns](https://thehackernews.com/2025/06/new-pathwiper-data-wiper-malware.html) in Ukraine, launching two wiper malware tracked as ZEROLOT and Sting aimed at an unnamed university in April 2025, followed by the deployment of multiple data-wiping malware variants targeting government, energy, logistics, and grain sectors.

"During this period, we observed and confirmed that the [UAC-0099](https://thehackernews.com/2025/08/cert-ua-warns-of-hta-delivered-c.html) [group](https://thehackernews.com/2025/07/researchers-uncover-batavia-windows.html) conducted initial access operations and subsequently transferred validated targets to Sandworm for follow-up activity," the company said. "These destructive attacks by Sandworm are a reminder that wipers very much remain a frequent tool of Russia-aligned threat actors in Ukraine."

### RomCom Exploits WinRAR 0-Day in Attacks

Another Russia-aligned threat actor of note that has been active during the time period is RomCom (aka Storm-0978, Tropical Scorpius, UNC2596, or Void Rabisu), which launched spear-phishing campaigns in mid-July 2025 that weaponized a WinRAR vulnerability ([CVE-2025-8088](https://thehackernews.com/2025/08/winrar-zero-day-under-active.html#winrar-flaw-also-exploited-by-romcom), CVSS score: 8.8) as part of attacks targeting financial, manufacturing, defense, and logistics companies in Europe and Canada.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

"Successful exploitation attempts delivered various backdoors used by the RomCom group, specifically a SnipBot [aka SingleCamper or RomCom RAT 5.0] variant, RustyClaw, and a Mythic agent," ESET said.

In a detailed profile of RomCom in late September 2025, AttackIQ characterized the hacking group as closely keeping an eye out for geopolitical developments surrounding the war in Ukraine, and leveraging them to carry out credential harvesting and data exfiltration activities likely in support of Russian objectives.

"RomCom was initially developed as an e-crime commodity malware, engineered to facilitate the deployment and persistence of malicious payloads, enabling its integration into prominent and extortion-focused ransomware operations," security researcher Francis Guibernau [said](https://www.attackiq.com/2025/09/23/evolution-of-romcom/). "RomCom transitioned from a purely profit-driven commodity to become a utility leveraged in nation-state operations."

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
[**Share ...