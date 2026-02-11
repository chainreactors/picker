---
title: Warlock Ransomware Breaches SmarterTools Through Unpatched SmarterMail Server
url: https://thehackernews.com/2026/02/warlock-ransomware-breaches.html
source: The Hacker News
date: 2026-02-10
fetch_date: 2026-02-11T04:24:31.416778
---

# Warlock Ransomware Breaches SmarterTools Through Unpatched SmarterMail Server

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [Warlock Ransomware Breaches SmarterTools Through Unpatched SmarterMail Server](https://thehackernews.com/2026/02/warlock-ransomware-breaches.html)

**Ravie Lakshmanan**Feb 10, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQg_RBFvjX4CSOktzf6QU0KcmxaSjFhOLkaPXZkzfoqHaq2A4TUCu-GxQCBQsKTK3PoDM-RLpolaRFIdbityIpVRtZA-5-VK2aYjRQZl0NWsHCpw-VrIkgUOYvOi4Pg0Le44LPnmMb5xQYQ4r3V6WT8Ukll2rt6mTBCRCFE3f3OD1LJCBK6G0XBAExHTw0/s1700-e365/smart.jpg)

SmarterTools confirmed last week that the Warlock (aka Storm-2603) ransomware gang breached its network by exploiting an unpatched SmarterMail instance.

The incident took place on January 29, 2026, when a mail server that was not updated to the latest version was compromised, the company's Chief Commercial Officer, Derek Curtis, said.

"Prior to the breach, we had approximately 30 servers/VMs with SmarterMail installed throughout our network," Curtis [explained](https://portal.smartertools.com/community/a97747/summary-of-smartertools-breach-and-smartermail-cves.aspx). "Unfortunately, we were unaware of one VM, set up by an employee, that was not being updated. As a result, that mail server was compromised, which led to the breach."

However, SmarterTools emphasized that the breach did not affect its website, shopping cart, My Account portal, and several other services, and that no business applications or account data were affected or compromised.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

About 12 Windows servers on the company's office network, as well as a secondary data center used for quality control (QC) tests, are confirmed to be affected. According to its CEO, Tim Uzzanti, the "attempted ransomware attack" also impacted hosted customers using SmarterTrack.

"Hosted customers using SmarterTrack were the most affected," Uzzanti [said](https://portal.smartertools.com/community/a97721/hack-1-29-26-how-can-i-help.aspx) in a different Community Portal threat. "This was not due to any issue within SmarterTrack itself, but rather because that environment was more easily accessible than others once they breached our network."

Furthermore, SmarterTools acknowledged that the Warlock group waited for a couple of days after gaining initial access to take control of the Active Directory server and create new users, followed by dropping additional payloads like [Velociraptor](https://thehackernews.com/2025/10/hackers-turn-velociraptor-dfir-tool.html) and the locker to encrypt files.

"Once these bad actors gain access, they typically install files and wait approximately 6–7 days before taking further action," Curtis said. "This explains why some customers experienced a compromise even after updating -- the initial breach occurred prior to the update, but malicious activity was triggered later."

It's currently not clear which SmarterMail vulnerability was weaponized by attackers, but it's worth noting that multiple flaws in the email software – [CVE-2025-52691](https://thehackernews.com/2025/12/csa-issues-alert-on-critical.html) (CVSS score: 10.0), [CVE-2026-23760](https://thehackernews.com/2026/01/smartermail-auth-bypass-exploited-in.html), and [CVE-2026-24423](https://thehackernews.com/2026/01/smartermail-fixes-critical.html) (CVSS scores: 9.3) – have come under active exploitation in the wild.

CVE-2026-23760 is an authentication bypass flaw that could allow any user to reset the SmarterMail system administrator password by sending a specially crafted HTTP request. CVE-2026-24423, on the other hand, exploits a weakness in the ConnectToHub API method to achieve unauthenticated remote code execution (RCE).

The vulnerabilities were addressed by SmarterTools in build 9511. Last week, the U.S. Cybersecurity and Infrastructure Security Agency (CISA) confirmed that CVE-2026-24423 was being exploited in ransomware attacks.

In a report published Monday, cybersecurity company ReliaQuest said it identified activity likely linked to Warlock that involved the abuse of CVE-2026-23760 to bypass authentication and stage the ransomware payload on internet-facing systems. The attack also leverages the initial access to download a malicious MSI installer ("v4.msi") from Supabase, a legitimate cloud-based backend platform, to install [Velociraptor](https://thehackernews.com/2025/11/matrix-push-c2-uses-browser.html).

"While this vulnerability allows attackers to bypass authentication and reset administrator passwords, Storm-2603 chains this access with the software's built-in 'Volume Mount' feature to gain full system control," security researcher Alexa Feminella [said](https://reliaquest.com/blog/threat-spotlight-storm-2603-exploits-CVE-2026-23760-to-stage-warlock-ransomware/). "Upon entry, the group installs Velociraptor, a legitimate digital forensics tool it has used in previous campaigns, to maintain access and set the stage for ransomware."

The security outfit also noted that the two vulnerabilities have the same net result: while CVE-2026-23760 grants unauthenticated administrative access via the password reset API, which can then be combined with the mounting logic to attain code execution, CVE-2026-24423 offers a more direct path to code execution through an API path.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

The fact that the attackers are pursuing the former method is an indication that it likely allows the malicious activity to blend in with typical administrative workflows, helping them avoid detection.

"By abusing legitimate features (password resets and drive mounting) instead of relying solely on a single 'noisy' exploit primitive, operators may reduce the effectiveness of detections tuned specifically for known RCE patterns," Feminella added. "This pace of weaponization is consistent with ransomware operators rapidly analyzing vendor fixes and developing working tradecraft shortly after release."

When reached for comment about the ...