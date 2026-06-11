---
title: Microsoft Patches Record 206 Flaws, Including Three Zero-Days and Critical RCE Bugs
url: https://thehackernews.com/2026/06/microsoft-patches-record-206-flaws.html
source: The Hacker News
date: 2026-06-10
fetch_date: 2026-06-11T06:37:06.243139
---

# Microsoft Patches Record 206 Flaws, Including Three Zero-Days and Critical RCE Bugs

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

# [Microsoft Patches Record 206 Flaws, Including Three Zero-Days and Critical RCE Bugs](https://thehackernews.com/2026/06/microsoft-patches-record-206-flaws.html)

**Ravie Lakshmanan**Jun 10, 2026Vulnerability / Zero-Day

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgDOIX9PorKjXDciuKmL8xLL9vrOVtBou5tBhn4T-u7cgllDKei3HRDr8vsXGM-MllL1eb6E_pdEID5s_sRUxbjHiA6AhlLUQLFi6vDXM5v0Mq0hM43eWSh8Pc_qdYtcjqushm7Wl-S64w6qEGg5P6ETD_o9l5VGGoflzGo3VpgFqmL9NhIe2RUuilVAB0c/s1700-e365/windows-patch.jpg)

Microsoft on Tuesday released fixes for a record [206 security vulnerabilities](https://msrc.microsoft.com/update-guide/releaseNote/2026-Jun) impacting its software portfolio, including three flaws that have been publicly disclosed at the time of release.

Of the 206 flaws, 39 are rated Critical, and 167 are rated Important in severity. This includes 63 privilege escalation, 56 remote code execution, 30 information disclosure, 27 spoofing, 20 security feature bypass, seven denial-of-service, and three tampering vulnerabilities.

The patches also include two non-Microsoft CVEs, a privilege escalation vulnerability impacting Windows Kernel ([CVE-2025-10263](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-10263)) and a UEFI Secure Boot [security feature bypass](https://kb.cert.org/vuls/id/616257) ([CVE-2026-8863](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-8863)). They are in addition to more than 350 security flaws that Google has addressed in Chromium, which is used in Microsoft's Edge browser.

Topping the list of fixes is [CVE-2026-45657](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45657) (CVSS score: 9.8), a use-after-free flaw affecting Windows Kernel that could result in remote code execution.

"An attacker could exploit this vulnerability by sending specially crafted network traffic to a vulnerable Windows system," Microsoft said. "If successful, the malicious network packets could trigger a flaw in how the Windows kernel processes certain TCP/IP data, potentially allowing the attacker to run code with system-level privileges without needing to sign in or interact with a user."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Other important vulnerabilities of note are listed below -

* [CVE-2026-47291](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-47291) (CVSS score: 9.8) - An integer overflow or wraparound flaw in Windows HTTP.sys that allows an unauthorized attacker to execute code over a network.
* [CVE-2026-44815](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-44815) (CVSS score: 9.8) - A stack-based buffer overflow vulnerability in Windows DHCP Client that allows an unauthorized attacker to execute code over a network.

"This flaw needs no credentials or user action and can turn network traffic into a full system compromise," Alex Vovk, CEO and co-founder of Action1, [said](https://www.action1.com/patch-tuesday/patch-tuesday-june-2026/) about CVE-2026-44815. "An attacker could send specially crafted network traffic to a system configured for DHCP services."

"Successful exploitation could allow unauthorized code execution over the network with high impact to confidentiality, integrity, and availability. This vulnerability creates serious risk because DHCP is a core network function. Successful exploitation could lead to server compromise, malware deployment, data theft, service disruption, and movement deeper into the network. Systems handling DHCP traffic should be treated as high-priority patch targets."

Microsoft has also released patches to address [CVE-2026-45585](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45585) (CVSS score: 6.8), a Windows BitLocker security feature bypass vulnerability for which a proof-of-concept (PoC) exploit called [YellowKey](https://thehackernews.com/2026/05/microsoft-releases-mitigation-for.html) was released by security researcher Chaotic Eclipse (aka Nightmare-Eclipse) last month.

CVE-2026-45585 is one of several secure feature bypasses that the Windows makers has addressed this month -

* [CVE-2026-45655](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45655) (CVSS score: 5.3)
* [CVE-2026-45658](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45658) (CVSS score: 7.8)
* [CVE-2026-50507](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50507) (CVSS score: 6.8)

"A successful attacker could bypass the BitLocker Device Encryption feature on the system storage device," Microsoft said in its advisories for the three issues. "An attacker with physical access to the target could exploit this vulnerability to gain access to encrypted data."

According to security researcher Will Dormann, CVE-2026-50507 is [assessed](https://infosec.exchange/%40wdormann/116699350092887103) to be a fix for a BitLocker bypass dubbed [bitskrieg](https://x.com/jonasLyk/status/2062768028090007773) that grants full access to encrypted data. It's worth noting that CVE-2026-50507, along with CVE-2026-49160 and CVE-2026-45586, are listed as publicly disclosed zero-days.

* [CVE-2026-45586](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45586) (CVSS score: 7.8) - Windows Collaborative Translation Framework (CTFMON) privilege escalation vulnerability
* [CVE-2026-49160](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-49160) (CVSS score: 7.5) - HTTP.sys denial-of-service vulnerability

CVE-2026-49160 is related to [HTTP2/Bomb](https://thehackernews.com/2026/06/new-http2-bomb-vulnerability-allows.html), an [attack technique](https://github.com/califio/publications/tree/main/MADBugs/http2-bomb) that can be used to knock web servers offline in seconds. In tests conducted by Calif, an IIS server was found to exhaust 64 GB RAM in about 45 seconds. To mitigate the attack, Microsoft has introduced a new "MaxHeadersCount" registry setting to limit the ...