---
title: Konni Hackers Turn Google’s Find Hub into a Remote Data-Wiping Weapon
url: https://thehackernews.com/2025/11/konni-hackers-turn-googles-find-hub.html
source: The Hacker News
date: 2025-11-10
fetch_date: 2025-11-11T03:14:28.595400
---

# Konni Hackers Turn Google’s Find Hub into a Remote Data-Wiping Weapon

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

# [Konni Hackers Turn Google's Find Hub into a Remote Data-Wiping Weapon](https://thehackernews.com/2025/11/konni-hackers-turn-googles-find-hub.html)

**Nov 10, 2025**Ravie LakshmananCyber Espionage / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIpCQ5f-ly7CHt6FDz9ULaJDLRDxJIrT9-GScn1vGk8jXp6zSXDDAMGMMZ-LY2bolu8-7HPoW0BNzFEyouKuyHNukvjbtUF16MiYto_WUV9Ve3x7ZJZYoE0J54qzT0VPtdZ_Bs54xIN53ifzW_Kqrd5QLPAEDEjUgfpUkcLLngM1_KrJaUi44JLAcg5m-f/s2600/hub.jpg)

The North Korea-affiliated threat actor known as **[Konni](https://thehackernews.com/2025/05/north-korean-konni-apt-targets-ukraine.html)** (aka Earth Imp, Opal Sleet, Osmium, TA406, and Vedalia) has been attributed to a new set of attacks targeting both Android and Windows devices for data theft and remote control.

"Attackers impersonated psychological counselors and North Korean human rights activists, distributing malware disguised as stress-relief programs," the Genians Security Center (GSC) [said](https://www.genians.co.kr/en/blog/threat_intelligence/android) in a technical report.

What's notable about the attacks targeting Android devices is also the destructive ability of the threat actors to exploit Google's asset tracking services Find Hub (formerly Find My Device) to remotely reset victim devices, thereby leading to the unauthorized deletion of personal data. The activity was detected in early September 2025.

The development marks the first time the [hacking group](https://www.genians.co.kr/blog/threat_intelligence/konni_disguise) has weaponized legitimate management functions to remotely reset mobile devices. The activity is also preceded by an attack chain in which the attackers approach targets via spear-phishing emails to obtain access to their computers, and leverage their logged-in KakaoTalk chat app sessions to distribute the malicious payloads to their contacts in the form of a ZIP archive.

The spear-phishing emails are said to mimic legitimate entities like the National Tax Service to deceive recipients into opening malicious attachments to deliver remote access trojans like [Lilith RAT](https://thehackernews.com/2024/09/developers-beware-lazarus-group-uses.html) that can remotely commandeer compromised machines and deliver additional payloads.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-Td1SlRx8mBXGkbg8PgZU1qtAdhGDoL6KqoYgb3JTxyCDQL84Qru9yf8QyAXaTyUG4cx9LOYTtTJL1b8VuMEZLWFSKLonXiyPBwtO1jenRLqYy3OApYVFU_JQekH67XZZ4B4-u_1s_nlUyreBDSst_cFC26PU8pj3Bx8K3bRpTfoJp-LVrx0wfTJAoYEh/s2600/google.png) |
| Konni Attack Flow |

"The threat actor stayed hidden in the compromised computer for over a year, spying via the webcam and operating the system when the user was absent," GSC noted. "In this process, the access obtained during the initial intrusion enables system control and additional information collection, while evasion tactics allow long-term concealment."

The deployed malware on the victim's computer allows the threat actors to carry out internal reconnaissance and monitoring, as well as exfiltrate victims' Google and Naver account credentials. The stolen Google credentials are then used to log in to Google's Find Hub and initiate a remote wipe of their devices.

In one case, the attackers have been found to sign into a recovery email account registered under Naver, delete security alert emails from Google, and empty the inbox's trash folder to cover up traces of the nefarious activity.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

The ZIP file propagated via the messaging app contains a malicious Microsoft Installer (MSI) package ("Stress Clear.msi"), which abuses a valid signature issued to a Chinese company to give the application an illusion of legitimacy. Once launched, it invokes a batch script to perform initial setup and proceeds to run a Visual Basic Script (VB Script) that displays a fake error message about a language pack compatibility issue, while the malicious commands are executed in the background.

This includes launching an AutoIt script that's configured to run every minute by means of a scheduled task in order to execute additional commands received from an external server ("116.202.99[.]218"). While the malware shares some similarities with Lilith RAT, it has been codenamed EndRAT (aka [EndClient RAT](https://www.0x0v1.com/endclientrat/) by security researcher Ovi Liber) due to the differences observed.

The list of supported commands is as follows -

* **shellStart**, to start a remote shell session
* **shellStop**, to stop remote shell
* **refresh**, to send system information
* **list**, to list drives or root directory
* **goUp**, to move up one directory
* **download**, to exfiltrate a file
* **upload**, to receive a file
* **run**, to execute a program on host
* **delete**, to delete a file on host

Genians said the Konni APT actors have also utilized an AutoIt script to launch Remcos RAT version 7.0.4, which was [released](https://breakingsecurity.net/remcos/changelog/) by its maintainers, Breaking Security, on September 10, 2025, indicating that the adversary is actively using newer versions of the trojan in its attacks. Also observed on victim devices are Quasar RAT and [RftRAT](https://thehackernews.com/2023/12/lazarus-group-using-log4j-exploits-to.html), another trojan previously put to use by Kimsuky in 2023.

"This suggests that the malware is tailored to Korea-focused operations and that obtaining relevant data and conducting in-depth analysis requires substantial effort," the South Korean cybersecurity company said.

### Lazarus Group's New Comebacker Variant Detailed

The disclosure comes as ENKI detailed the [Lazarus Group's](https://thehackernews.com/2025/11/new-httptroy-backdoor-poses-as-vpn.html) use of an updated version of the Comebacker malware in attacks aimed at aerospace and defense organizations using tailored Microsoft Word document lures consistent w...