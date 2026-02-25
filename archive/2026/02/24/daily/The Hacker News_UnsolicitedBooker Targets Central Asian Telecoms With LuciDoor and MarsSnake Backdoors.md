---
title: UnsolicitedBooker Targets Central Asian Telecoms With LuciDoor and MarsSnake Backdoors
url: https://thehackernews.com/2026/02/unsolicitedbooker-targets-central-asian.html
source: The Hacker News
date: 2026-02-24
fetch_date: 2026-02-25T04:15:40.620372
---

# UnsolicitedBooker Targets Central Asian Telecoms With LuciDoor and MarsSnake Backdoors

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [UnsolicitedBooker Targets Central Asian Telecoms With LuciDoor and MarsSnake Backdoors](https://thehackernews.com/2026/02/unsolicitedbooker-targets-central-asian.html)

**Ravie Lakshmanan**Feb 24, 2026Malware / Vulnerability

[![LuciDoor and MarsSnake Backdoors](data:image/png;base64... "LuciDoor and MarsSnake Backdoors")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSNzH9FCcwXlaHaCt3zQfmpwV3uesrW_2ISdcvbuKMl7PIENe9w6dhzBVpj19_BmgHKcZIzxBLSBFOmwNx2ahUast29Tk_LJoY8qz-SrJziWhHTHURX8HTvJuIVvMJourUJ0Hw8RKnXYUFcz9wsaO7_halOZmw3gof1-N1-jI-MtNsztV5YYP4WvQdPBcY/s1700-e365/TELECOM.jpg)

The threat activity cluster known as **UnsolicitedBooker** has been observed targeting telecommunications companies in Kyrgyzstan and Tajikistan, marking a shift from prior attacks aimed at Saudi Arabian entities.

The attacks involve the deployment of two distinct backdoors codenamed LuciDoor and MarsSnake, according to a report published by Positive Technologies last week.

"The group used several unique and rare instruments of Chinese origin," researchers Alexander Badaev and Maxim Shamanov [said](https://ptsecurity.com/research/pt-esc-threat-intelligence/poisonous-mars-or-how-lucidoor-knocks-on-the-doors-of-the-cis/).

UnsolicitedBooker was [first documented](https://thehackernews.com/2025/05/chinese-hackers-deploy-marssnake.html) by ESET in May 2025, attributing the China-aligned threat actor to a cyber attack targeting an unnamed international organization in Saudi Arabia with a backdoor dubbed MarsSnake. The group is assessed to be active since at least March 2023 and has a history of targeting organizations in Asia, Africa, and the Middle East.

Further analysis of the threat actor has uncovered tactical overlaps with two other clusters, including Space Pirates and an as-yet-unattributed campaign targeting Saudi Arabia with another backdoor referred to as Zardoor.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

The latest set of attacks documented by the Russian cybersecurity vendor was found to target Kyrgyz organizations in late September 2025 with phishing emails containing a Microsoft Office document, which, when opened, instructs recipients to "[Enable Content](https://support.microsoft.com/en-us/office/enable-or-disable-macros-in-microsoft-365-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)" so as to run a malicious macro.

While the document displays a telecom provider's tariff plan to the victim, the macro stealthily drops a C++ malware loader called LuciLoad that, in turn, delivers LuciDoor. Another attack observed in late November 2025 adopted the same modus operandi, only this time it used a different loader codenamed MarsSnakeLoader to deploy MarsSnake.

As recently as January 2026, UnsolicitedBooker is said to have leveraged phishing emails as a vector to target companies in Tajikistan. While the overall attack chain remains the same, the messages embedded links to the decoy documents as opposed to directly attaching them.

Written in C++, LuciDoor establishes communication with a command-and-control (C2) server, collects basic system information, and exfiltrates the data to the server in encrypted format. It then parses the responses sent by the server to run commands using cmd.exe, write files to the system, and upload files.

|  |
| --- |
| [![LuciDoor and MarsSnake Backdoors](data:image/png;base64... "LuciDoor and MarsSnake Backdoors")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCFTRL30UYyQeCJxw1PnEAwwXgtiSg4D9vCts6Igu19-tATiOvNe8v5ldIZ_SntA5dbt_h0C2hB6D0cwjUts-xvb9jSjHrDyGPZKLkm65zkaiF_ymsiIJyqHmMssx7rRWNtidSejcArb6kWWlG8szP72-IHmHv5s7qudXe5hDPeC20pHObamL2WNl4wFXS/s1700-e365/malware.png) |
| Macros in the document |

MarsSnake, similarly, allows attackers to harvest system metadata, execute arbitrary commands, and read or write any file on disk.

Positive Technologies said it also found signs that MarsSnake was put to use in attacks targeting China. The starting point is a Windows shortcut that masquerades as a Microsoft Word document (\*.doc.lnk) that triggers the execution of a batch script to launch a Visual Basic Script, which then launches MarsSnake without the loader component.

The decoy file is believed to be based on an LNK file associated with a publicly available pentesting tool called [FTPlnk\_phishing](https://github.com/Pizz33/FTPlnk_phishing), owing to the identical LNK file creation time and Machine ID indicators. It's worth noting that a [similar LNK file](https://www.darktrace.com/blog/chinese-apt-target-royal-thai-police-in-malware-campaign) was put to use by the [Mustang Panda group](https://thehackernews.com/2025/09/mustang-panda-deploys-snakedisk-usb.html) in attacks targeting Thailand in 2022.

"In their attacks, the group used rare tools of Chinese origin," Positive Technologies said. "Interestingly, at the very beginning, the group used a backdoor we dubbed LuciDoor, but later switched to the MarsSnake backdoor. However, in 2026, the group made a U-turn and resumed using LuciDoor."

"Furthermore, in at least one case, we observed the attackers using a hacked router as a C2 server, and their infrastructure mimicked that of Russia in some attacks."

### PseudoSticky and Cloud Atlas Target Russia

The disclosure comes as a previously unknown threat actor is deliberately mimicking the tactics of a pro-Ukrainian hacking group called [Sticky Werewolf](https://thehackernews.com/2025/02/sticky-werewolf-uses-undocumented.html) (aka Angry Likho, MimiStick, and PhaseShifters) to attack Russian organizations in the retail, construction, and research sectors with malware like RemcosRAT and DarkTrack RAT for comprehensive data theft and remote control.

The new group, referred to as [PseudoSticky](https://www.f6.ru/blog/pseudo-sticky/), has been active since November 2025. Victims are typically infected by phishing emails containing malicious attachments that lead to the deployment of...