---
title: Dragon Breath Uses RONINGLOADER to Disable Security Tools and Deploy Gh0st RAT
url: https://thehackernews.com/2025/11/dragon-breath-uses-roningloader-to.html
source: The Hacker News
date: 2025-11-17
fetch_date: 2025-11-18T03:15:22.042281
---

# Dragon Breath Uses RONINGLOADER to Disable Security Tools and Deploy Gh0st RAT

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

# [Dragon Breath Uses RONINGLOADER to Disable Security Tools and Deploy Gh0st RAT](https://thehackernews.com/2025/11/dragon-breath-uses-roningloader-to.html)

**Nov 17, 2025**Ravie LakshmananMalware / Endpoint Protection

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9N_SUrEcfHdyrM_8wzo21DFLFtDBZPlKPLyFLYRfQWYCS8wyhxYLj35JrSqYNFT9739fS9yXd3HSwlcTw4k3j-v96987CW9AWYoaC-BcCCnmTUJ09p7mk07aa1Cn9tYKOuUBS0GQ9oVgoKMfVCbhdWNVF4f5YdAvkAl2PeGDWEKBu1Q3BX58WfqowgUlX/s790-rw-e365/malware-attack.jpg)

The threat actor known as **Dragon Breath** has been observed making use of a multi-stage loader codenamed RONINGLOADER to deliver a modified variant of a remote access trojan called Gh0st RAT.

The campaign, which is primarily aimed at Chinese-speaking users, employs trojanized NSIS installers masquerading as legitimate like Google Chrome and Microsoft Teams, according to Elastic Security Labs.

"The infection chain employs a multi-stage delivery mechanism that leverages various evasion techniques, with many redundancies aimed at neutralising endpoint security products popular in the Chinese market," security researchers Jia Yu Chan and Salim Bitam [said](https://www.elastic.co/security-labs/roningloader). "These include bringing a legitimately signed driver, deploying custom WDAC policies, and tampering with the Microsoft Defender binary through [PPL](https://thehackernews.com/2025/08/researchers-detail-windows-epm.html) [Protected Process Light] abuse."

Dragon Breath, also known as APT-Q-27 and Golden Eye, was [previously highlighted](https://thehackernews.com/2023/05/dragon-breath-apt-group-using-double.html) by Sophos in May 2023 in connection with a campaign that leveraged a technique called double-dip DLL side-loading in attacks targeting users in the Philippines, Japan, Taiwan, Singapore, Hong Kong, and China.

The hacking group, assessed to be active since at least 2020, is linked to a larger Chinese-speaking entity tracked as Miuuti Group that's known for attacking the online gaming and gambling industries.

In the latest campaign documented by Elastic Security Labs, the malicious NSIS installers for trusted applications act as a launchpad for two more embedded NSIS installers, one of which ("letsvpnlatest.exe") is benign and installs the legitimate software. The second NSIS binary ("Snieoatwtregoable.exe") is responsible for stealthily triggering the attack chain.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

This involves delivering a DLL and an encrypted file ("tp.png"), with the former used to read the contents of the supposed PNG image and extract shellcode designed to launch another binary in memory.

RONINGLOADER, besides attempting to remove any userland hooks by loading a fresh new "[ntdll.dll](https://thehackernews.com/2022/12/guloader-malware-utilizing-new.html)," tries to elevate its privileges by using the [runas](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc771525%28v%3Dws.11%29) command and scans a list of running processes for hard-coded antivirus-related solutions, such as Microsoft Defender Antivirus, Kingsoft Internet Security, Tencent PC Manager, and Qihoo 360 Total Security.

The malware then proceeds to terminate those identified processes. In the event the identified process is associated with Qihoo 360 Total Security (e.g., "360tray.exe," "360Safe.exe," or "ZhuDongFangYu.exe"), it takes a different approach. This step involves the following sequence of actions -

* Block all network communication by changing the firewall
* Inject shellcode into the process (vssvc.exe) associated with the Volume Shadow Copy (VSS) service, but not before granting itself the [SeDebugPrivilege](https://thehackernews.com/2025/04/pipemagic-trojan-exploits-windows-clfs.html) token
* Start the VSS service and get its process ID
* Inject shellcode into the VSS service process using the technique called [PoolParty](https://thehackernews.com/2023/12/new-poolparty-process-injection.html)
* Load and make use of a signed driver named "ollama.sys" to terminate the three processes by means of a temporary service called "xererre1"
* Restore the firewall settings

For other security processes, the loader directly writes the driver to disk and creates a temporary service called "ollama" to load the driver, perform process termination, and stop and delete the service.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjv4fyHNecI-4FNyRjVSUSnpCPDkjpa8RsRvc1Wyjlbd-NKv3ihQKlG_xPIx-pvTfixRwfVPyKcz5tiqMLhowqATu2yVKC9BKJsSnXgkNljyNS_CQU7fGxvg8HXs_AvRRJLG_QzS0eNRMcNZBQSX6gyjna-vGqo4UHDBT1Zqx37v9rJMjaUhZFNorm1b0V/s2600/flow.jpg) |
| RONINGLOADER Execution flow |

Once all security processes have been killed on the infected host, RONINGLOADER runs batch scripts to bypass User Account Control (UAC) and create firewall rules to block inbound and outbound connections associated with Qihoo 360 security software.

The malware has also been observed using two techniques documented earlier this year by security researcher Zero Salarium that abuse [PPL](https://www.zerosalarium.com/2025/08/countering-edrs-with-backing-of-ppl-protection.html) and the Windows Error Reporting ("WerFaultSecure.exe") system (aka [EDR-Freeze](https://www.zerosalarium.com/2025/09/EDR-Freeze-Puts-EDRs-Antivirus-Into-Coma.html)) to disable Microsoft Defender Antivirus. Furthermore, it targets Windows Defender Application Control (WDAC) by writing a malicious policy that explicitly blocks Chinese security vendors Qihoo 360 Total Security and Huorong Security.

The end goal of the loader is to inject a rogue DLL into "regsvr32.exe," a legitimate Windows binary, to conceal its activity and launch a next-stage payload into another legitimate, high-privilege system process like "TrustedInstaller.exe" or "elevation\_service.exe." The final malware deployed is a modified version of Gh0st RAT.

The trojan i...