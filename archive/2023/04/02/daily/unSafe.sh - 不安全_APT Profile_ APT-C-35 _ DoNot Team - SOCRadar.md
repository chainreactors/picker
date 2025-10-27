---
title: APT Profile: APT-C-35 / DoNot Team - SOCRadar
url: https://buaq.net/go-156444.html
source: unSafe.sh - 不安全
date: 2023-04-02
fetch_date: 2025-10-04T11:26:34.233674
---

# APT Profile: APT-C-35 / DoNot Team - SOCRadar

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/2b87b5d85e6256bfbae9673077db3c71.jpg)

APT Profile: APT-C-35 / DoNot Team - SOCRadar

Advanced Persistent Threat groups are known for their sophisticated attacks and ability to stealth
*2023-4-1 13:54:44
Author: [socradar.io(查看原文)](/jump-156444.htm)
阅读量:50
收藏*

---

[Advanced Persistent Threat](https://socradar.io/from-zero-to-adversary-apts/) groups are known for their sophisticated attacks and ability to stealthily stay in a system for a long time. These groups are commonly nation-state-sponsored, and they carry out various **espionage or sabotage attacks** for the interests of their nations.

Russian, Iranian, Chinese, and North Korean APT actors usually play a role in major incidents globally, such as Russian APT group [Sandworm](https://socradar.io/apt-profile-sandworm/)‘s attack during the 2018 PyeongChang Winter Olympics or the **Wannacry ransomware** attack of North Korean APT group [Lazarus](https://socradar.io/apt-profile-who-is-lazarus-group/). However, some groups are not as sophisticated as other groups that have a global impact but carry out major operations for their national interest. As an example of this, APT-C-35 will be discussed in this article.

## Who is APT-C-35?

APT-C-35, Brainworm or DoNot Team, is an Advanced Persistent Threat (APT) believed to be linked with the **Indian government**. The group is known to have been active since 2016. Also, APT-C-35’s primary motivation seems to be espionage for the interests of the Indian government, and cybersecurity researchers observed that they carried out various campaigns with this aim. When we consider Operation Hangover, a campaign believed to be linked to the group, it is possible to say that they have been active **since 2013** or even 2010.

Some sources also suggest that another Indian state-sponsored APT group **Patchwork** and APT-C-35’s attack patterns overlap and may be the same actor. It is possible to say that their attack patterns are similar, but their targets seem different. There is a possibility that they are the same threat actor, yet there is no certain proof of that claim.

### Who Are APT-C-35’s Targets?

The group’s first observed attack was against a telecom company in **Norway**; however, since the group’s primary motivation seems to be espionage for the interests of the Indian government and backed by observations, the APT-C-35 mainly targets **South Asia**.

![Countries affected by APT-C-35 activities (Source: SOCRadar) ](https://socradar.io/wp-content/uploads/2023/03/apt-c-35-affected-countries-1024x576.png)

Looking at the majority of its observed attacks, it is possible to say that the group mostly targets the **Kashmir region** due to the Kashmir Conflict. The Conflict is a long-standing territorial dispute between India and Pakistan over Kashmir. India and Pakistan claim sovereignty over the entire region, but each controls only a part. The issue remains unresolved, and efforts to find a lasting solution through negotiations and diplomatic channels have so far been unsuccessful.

![apt-c-35 kashmir region](https://socradar.io/wp-content/uploads/2023/03/countries-kashmir-region.png)

Countries with impact in the Kashmir region

The sectors listed below in the observations on affected countries increase the likelihood of attacks due to the Kashmir dispute. The group targets:

* Governments,
* Military organizations,
* Ministries of Foreign Affairs,
* Embassies.

## How Does APT-C-35 Attack?

Based on the observed attacks, the group is conducting [spear phishing](https://socradar.io/how-to-identify-spear-phishing/) campaigns. During spear phishing campaigns, they deliver their malware as documents containing **malicious macros**.

![apt-c-35 pakistan](https://socradar.io/wp-content/uploads/2023/03/pakistan-decoy-document.png)

A decoy document that appears to have been prepared by Pakistan (Source: [Netscout](https://www.netscout.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia))

The group utilizes Macros to gain **remote access** to their target, which is found in various **Microsoft Office** programs such as Word, Excel, and PowerPoint. They achieve this by using Windows Framework RTF files with **.doc extensions**, which include links that allow them to download malware and ultimately gain control over the system.

As observed from various attacks, the group has seen carried out its operations by exploiting [CVE-2018-0802](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-0802) (**Microsoft Office Memory Corruption Vulnerability**), [CVE-2017-0199](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0199) (**Microsoft Office Remote Code Execution Vulnerability**), and [CVE-2017-8570](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-8570) (**Microsoft Office Remote Code Execution Vulnerability.**) But, the group has seen exploiting [CVE-2017-11882](https://cve.mitre.org/cgi-bin/cvename.cgi?name=cve-2017-11882) vulnerability in most of its attacks. This vulnerability is a memory corruption issue seen in Microsoft Office. When the malicious document is opened, it enables the attacker to execute remote code on the victim’s machine without needing any user interaction.

The malicious document, running as a dropper, drops and executes a downloader. Then it downloads plugins such as **keylogger**, **screenshot taker**, etc., to the victim’s machine for espionage purposes. For example, one of the components of **DarkMusical** malware enumerates all files in %public%\Music\Symphony and uploads those that match the extensions: **doc, docx, eml, inp, jpeg, jpg, msg, odt, pdf, pps, ppsx, ppt, pptx, rtf, txt, xls, and xlsx.**

In addition to malicious documents, the group also appears to have **Android malware**, such as Android RAT malware found as a rogue Kashmir News Service Lite app and more like that.

![Some of the rogue applications have been observed to be distributed by APT-C-35 ](https://socradar.io/wp-content/uploads/2023/03/apt-c-35-rogue-applications-1024x248.png)

Some of the rogue applications have been observed to be distributed by APT-C-35 (Source: [360](https://apt.360.net/orgDetail/32))

The group’s Android malware disguises itself in two different ways. **Fake app icons and error messages**. Observations show that after the software runs, it sends a deception message to make it look like the software is deleting itself. In the meantime, the software deletes its shortcuts but continues its espionage activities in the background.

![An example of displaying a pop-up message as a camouflage technique of one of the APT-C-35 Android malware ](https://socradar.io/wp-content/uploads/2023/03/apt-c-35-malware.png)

An example of displaying a pop-up message as a camouflage technique of one of the APT-C-35’s Android malware (Source: [360](https://apt.360.net/orgDetail/32))

## Which Tools and Malware Does APT-C-35 Use?

The group created some malware for espionage activities and developed them over time. Examples of these include **EHDevel**, which the group created itself, and the recently updated version of the EHDevel, the **YTY malware framework**. Also, the malware developed by the group seems to focus on file collection, screenshots, and keylogging.

**YTY Framework**

The YTY is a modular, plugin-based malware framework that gathers and transmits data. The framework is comprised of a series of downloaders that ultimately install a **backdoor**. Once the backdoor is installed, threat actors can use it to retrieve and execute other components of the **Donot Team’s tools**, including applications that collect files, take scre...