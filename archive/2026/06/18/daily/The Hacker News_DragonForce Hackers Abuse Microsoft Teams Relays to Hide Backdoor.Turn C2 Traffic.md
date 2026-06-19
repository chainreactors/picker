---
title: DragonForce Hackers Abuse Microsoft Teams Relays to Hide Backdoor.Turn C2 Traffic
url: https://thehackernews.com/2026/06/dragonforce-hackers-abuse-microsoft.html
source: The Hacker News
date: 2026-06-18
fetch_date: 2026-06-19T07:09:17.657907
---

# DragonForce Hackers Abuse Microsoft Teams Relays to Hide Backdoor.Turn C2 Traffic

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

# [DragonForce Hackers Abuse Microsoft Teams Relays to Hide Backdoor.Turn C2 Traffic](https://thehackernews.com/2026/06/dragonforce-hackers-abuse-microsoft.html)

**Ravie Lakshmanan**Jun 18, 2026Remote Access Trojan / Ransomware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidEg1Q-FcDTwCPci3OMxGy0TghiI1dbWJoaJVc88gpGgO2ia6bgne18KfS3A9qAzBnMX2rGY9H78ewtofXQO22RRpzHxWXmvQJvRZ1nsvwj37aZBtLOXXltzd1KkNRKhu2N5LpIro5Fi0BBkftPqP_IO6B3HCKx5WPtFXZKA1bfbP3xV71CpEqpT7H6RPN/s1700-e365/teams.jpg)

Threat actors associated with the [DragonForce](https://thehackernews.com/2025/10/lockbit-qilin-and-dragonforce-join.html) ransomware have been observed using a custom Go-based remote access trojan (RAT) called **Backdoor.Turn** to conceal command-and-control (C2) traffic inside Microsoft Teams relay infrastructure.

According to findings from Broadcom-owned Symantec and Carbon Black, the backdoor was deployed against a major U.S. services firm. The name of the company was not disclosed.

"Backdoor.Turn obtains an anonymous Teams visitor token from Microsoft’s Skype-backed identity services, uses a legitimate Microsoft TURN relay to set up the connection, and then runs a QUIC session to the attacker’s real command-and-control (C2) server," the Threat Hunter Team [said](https://www.security.com/threat-intelligence/dragonforce-msteams-backdoor) in a report shared with The Hacker News.

"To network defenders, the only traffic they could see was outbound connections to legitimate Microsoft Teams servers. The attackers were on the victim network for between one and two months."

The development marks the first publicly documented instance of the threat actors abusing Microsoft's Traversal Using Relays around NAT ([TURN](https://techcommunity.microsoft.com/discussions/azurevirtualdesktopforum/turn-relay-regional-expansion-for-azure-virtual-desktop/4419721)) relay infrastructure.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

It's suspected the threat actor obtained initial access by exploiting a vulnerability in either an SQL or MS-SQL server, although the exact nature of the flaw is unknown. It's also possible that the access was acquired from an initial access broker (IAB).

Initial malicious activity on the victim network began in December 2025, with the attackers running a PowerShell command to drop a ZIP archive under the pretext of a tech support hotfix. The ZIP file responsible for launching a DLL side-loading attack, which then runs a rogue DLL to conduct reconnaissance, set up persistence, and silence security software using a Huawei driver ("HWAuidoOs2Ec.sys").

This is achieved by means of an attack technique called bring your own vulnerable driver (BYOVD) technique. The driver has been put to use in a [large-scale malvertising campaign](https://thehackernews.com/2026/03/tax-search-ads-deliver-screenconnect.html) targeting U.S.-based individuals searching for tax-related documents, although this is said to have taken place after the ransomware incident.

Some of the other drivers used for this purpose are listed below -

* wsftprm.sys ([CVE-2023-52271](https://nvd.nist.gov/vuln/detail/CVE-2023-52271))
* GameDriverX64.sys ([CVE-2025-61155](https://nvd.nist.gov/vuln/detail/CVE-2025-61155))
* K7RKScan.sys ([CVE-2025-1055](https://nvd.nist.gov/vuln/detail/CVE-2025-1055))
* [ABYSSWORKER](https://thehackernews.com/2025/03/medusa-ransomware-uses-malicious-driver.html), a custom-built malicious driver previously observed in Medusa ransomware attacks

What's notable about the attack is the execution of Backdoor.Turn by injecting it into the legitimate "DbgView64.exe" process after the DragonForce ransomware has been deployed. This suggests an attempt to maintain continued access to the compromised host for later attacks or reselling it for profit.

Backdoor.Turn's underlying TURN-based mechanism leans on a stealthy C2 communication technique called [Ghost Calls](https://thehackernews.com/2025/08/weekly-recap-badcam-attack-winrar-0-day.html#:~:text=Praetorian%20Releases%20ChromeAlone) that was documented by Praetorian in August 2024. The backdoor supports a wide range of capabilities, including command execution, process creation, network scanning, LDAP and Active Directory search, credential-based lateral movement, and browser credential theft.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

"The backdoor requests a visitor token from the Microsoft Teams/Skype backend, uses that token to interact with Teams-associated infrastructure (TURN relay), and then establishes outbound connectivity," Symantec and Carbon Black explained.

"It obtains a Teams visitor (anonymous) authentication token backed by Skype identity services. It then uses a legitimate Microsoft server as the TURN relay server during connection setup. After relay-assisted setup, the malware establishes a direct QUIC session to the C&C server, which is malicious."

The findings paint a picture of a hacking group leaning on sophisticated cyber tradecraft to pull off high-impacted targeted attacks, while leaving victims in the dark about covert data exfiltration. This is particularly significant as Hackledorb, the threat actor behind DragonForce, has pivoted from a conventional ransomware-as-a-service (RaaS) model to a highly organized, formalized cartel structure.

"The operational timeline reveals a pattern of continuous capability development, with the adoption of highly advanced techniques becoming a hallmark of their post-2025 activity," the company said. "The deployment of Backdoor.Turn, combined with their multi-vector BYOVD evasion, marks them as one of the most capable and persistent ransomware groups operating today."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and...