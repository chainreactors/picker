---
title: Fake Software Installers Disable Windows Update and Weaken Microsoft Defender
url: https://thehackernews.com/2026/09/fake-software-installers-disable.html
source: The Hacker News
date: 2026-09-02
fetch_date: 2026-09-03T07:02:41.656864
---

# Fake Software Installers Disable Windows Update and Weaken Microsoft Defender

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Fake Software Installers Disable Windows Update and Weaken Microsoft Defender](https://thehackernews.com/2026/09/fake-software-installers-disable.html)

**Ravie Lakshmanan**Sep 02, 2026Malware / Social Engineering

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhKCtgI2bIF4kLY71qjkluS80XAm5YPA9y9GzTxC8XBTaxq1d42jyZ-bxAr7OlZ-wCc4-RDp_NmUPKxd9TS1dvtjt3gysB86SkMuQ5q6vGb7HTh-DVMNC8VJcJFC2sJmiSQ740SX-miCoyiGfkAXLqO1ySH3zenWcAP7g6ilReO9jRsnl3Tnw279K7NYF3/s1700-nu-rw-lo-l85-e365/windows-updates.jpg)

An active malware campaign is using bogus software-download websites to impersonate trusted vendors and distribute malicious installers.

"The campaign has targeted users looking to download popular software and has resulted in compromises across multiple organizations and industries, primarily affecting China-based operations of multinational organizations and Chinese-speaking users," Microsoft [said](https://www.microsoft.com/en-us/security/blog/2026/09/01/counterfeit-installers-system-compromise-tracking-deceptive-software-download-campaign/).

The installers, once launched, deploy malware that's capable of setting up persistence, weakening security protections, and communicating with attacker-controlled infrastructure.

The activity has resulted in victims spanning healthcare, manufacturing, gaming, technology, logistics, government, and education sectors. The Windows maker has assessed with moderate confidence that the campaign is consistent with a [Chinese threat cluster](https://otx.alienvault.com/pulse/6a36fe5a3c1568785b59c4d7) dubbed [Silver Fox](https://thehackernews.com/2026/08/spark-rat-targets-cambodia-abuses.html) (aka Yinhu), which has a track record of using [spoofed vendor download pages](https://thehackernews.com/2025/06/chinese-group-silver-fox-uses-fake.html) to distribute Gh0st RAT and ValleyRAT (aka WinOS 4.0).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The websites observed as part of the campaign are hosted on the .com.cn and .hl.cn infrastructure and use Chinese-language lure content to trigger the download of a ZIP archive from "gehie246[.]com." Some of the counterfeit websites are listed below -

* app-microsoft-edge[.]com[.]cn
* baidu-pan[.]com[.]cn
* calibre-ebook[.]com[.]cn
* cn-drawio[.]com[.]cn
* gw-sogou[.]com[.]cn
* kaspersky-lab[.]hl[.]cn
* mindmoster[.]com[.]cn
* ocam-pc[.]com[.]cn
* pc-razerzone[.]com[.]cn
* sejda[.]hl[.]cn
* steelseries-cn[.]com[.]cn
* translate-youdao[.]hl[.]cn
* zh-diskgenius[.]com[.]cn

The web pages are high-fidelity clones of the legitimate vendor's site and feature a prominent download call-to-action. Tellingly, the archive downloaded from the site maintains the same file name while its hash changes on every download, indicating that the payload is generated server-side on the fly for every request.

Opening the archive leads to a wrapper installer (e.g., "a\_instapp83353001.exe" or "ainst8663586104.exe"), which, upon execution, launches the first stage payload. Separately, Microsoft said it observed a second execution vector that makes use of the trusted Windows Installer service ("msiexec.exe") to launch a randomized executable, mirroring the same masquerade pattern as the wrapper chain.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgu_NhG7agmNGHf-knq6gxQz4dO5VzWYvEdXOGMMZDwIhQ2YtZEysNN_beYTAayGMzvp-T2HXRUux5oa6rfYR2LTG884ELDFsTvgGxijveWoJaKEfgtk4-4Fo1BEAPDLvYr7zYj06wZQVIigOnLPKlU4PrCslKAgHcs8Bdx2-VlXn1HJnxV-y49HuDsktvw/s1700-nu-rw-lo-l85-e365/ms-main.jpg)

Regardless of the method used, persistence is achieved through scheduled tasks that imitate routine IT or productivity jobs. The malware is also responsible for creating a short-lived scheduled task that runs as SYSTEM and configures Microsoft Defender exclusions via PowerShell, deletes volume shadow copies, and ensures payload directories cannot be removed by standard users by modifying their discretionary access control lists (DACLs) using [icacls](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/icacls).

In addition, it tampers with Windows Update by stopping and disabling wuauserv, UsoSvc, uhssvc, and WaaSMedicSvc, renaming update dynamic-link libraries (DLLs), and deleting the SoftwareDistribution cache.

Once all these steps are carried out, the malware establishes command-and-control (C2) over application-layer protocols on non-standard ports like 5090, 7031, 7032, 7088–7090, 8050, 28290, and 28300. Two C2 domains associated with the activity are "iualef[.]net" and "oijfwe[.]net."

It's unclear what the end goal of the campaign is, as Microsoft said Defender detected and initiated automated containment procedures through [attack disruption](https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption) to limit the attack's impact further.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPem0Jebd4RkJRH1cRK_tSeNcnmNKfhSp9kAtuFKB8fgThUU00ySd2Dm0sdJIh3wbWNU3ShLaNM1w1NGsiMcofL71PQmlcHfNkLXbNsz2tLjtZFQkJ2BTCrMft639B_KnGeRUeucYF_G9OCI7sL6hA0ISSCJs18L-OiSuwLfCrStIofRtfh5CG3ggdscen/s1700-nu-rw-lo-l85-e365/tasks.jpg)

The disclosure comes merely days after Kaspersky detailed a malicious installer that deploys a modified Chinese desktop wallpaper management tool known as QN Wallpaper, while using it to initiate a DLL sideloading chain responsible for delivering ValleyRAT.

"The original version of QN Wallpaper is genuine adware: on installation, it delivers bundled partner apps to the device and then displays ad banners to the user," Kaspersky [said](https://securelist.com/valleyrat-backdoor-adware/121175/). "In this case, however, the attackers use it to carry out DLL sideloading, a technique that allows malicious code to run under the guise of a signed process by way of a malicious DLL."

The backdoor, besides taking steps to protect its process and ...