---
title: Chinese Entanglement | DLL Hijacking in the Asian Gambling Sector
url: https://buaq.net/go-174692.html
source: unSafe.sh - 不安全
date: 2023-08-18
fetch_date: 2025-10-04T11:59:07.236320
---

# Chinese Entanglement | DLL Hijacking in the Asian Gambling Sector

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

![](https://8aqnet.cdn.bcebos.com/e713a8d90296656cda15b5778b4badec.jpg)

Chinese Entanglement | DLL Hijacking in the Asian Gambling Sector

By Aleksandar Milenkoski and Tom HegelExecutive SummarySentinelLabs has identified suspected-Chi
*2023-8-17 17:55:8
Author: [www.sentinelone.com(查看原文)](/jump-174692.htm)
阅读量:46
收藏*

---

**By Aleksandar Milenkoski and Tom Hegel**

## Executive Summary

* SentinelLabs has identified suspected-Chinese malware and infrastructure potentially involved in China-associated operations directed at the gambling sector within Southeast Asia.
* The threat actors abuse Adobe Creative Cloud, Microsoft Edge, and McAfee VirusScan executables vulnerable to DLL hijacking to deploy Cobalt Strike beacons.
* We’ve observed related malware using the signature of a likely stolen code signing certificate issued to PMG PTE LTD, a Singapore-based vendor of Ivacy VPN services.
* Indicators point to the China-aligned BRONZE STARLIGHT group; however, the exact grouping remains unclear due to the interconnected relationships among various Chinese APT groups.

## Overview

Thriving after China’s [crackdown](https://asia.nikkei.com/Spotlight/The-Big-Story/Macao-bets-on-a-new-future-as-China-cracks-down-on-gambling) on its Macao-based gambling industry, the Southeast Asian gambling sector has become a focal [point](https://i.blackhat.com/Asia-22/Friday-Materials/AS-22-Li-To-Loot-Or-Not-To-Loot-That-Is-Not-a-Question.pdf) for the country’s interests in the region, particularly data collection for monitoring and countering related activities in China.

We observed malware and infrastructure likely related to China-aligned activities targeting this sector. The malware and infrastructure we analyze are related to indicators observed in [Operation ChattyGoblin](https://www.welivesecurity.com/wp-content/uploads/2023/05/eset_apt_activity_report_q42022_q12023.pdf) and are likely part of the same activity cluster. Operation ChattyGoblin is ESET’s name for a series of attacks by China-nexus actors targeting Southeast Asian gambling companies with [trojanized](https://www.crowdstrike.com/blog/new-supply-chain-attack-leverages-comm100-chat-installer/) [Comm100](https://www.comm100.com/) and [LiveHelp100](https://www.livehelp100.com/) chat applications.

The targeting, used malware, and C2 infrastructure specifics point to past activities that third parties have linked to the China-aligned [BRONZE STARLIGHT](https://www.secureworks.com/research/threat-profiles/bronze-starlight) group (also known as [DEV-0401](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/#DEV-0401) or SLIME34). This is a suspected Chinese ‘ransomware’ group whose main goal [appears](https://www.secureworks.com/research/bronze-starlight-ransomware-operations-use-hui-loader) to be espionage rather than financial gain, using ransomware as means for distraction or misattribution. Team T5 has also reported on BRONZE STARLIGHT’s politically-motivated [involvement](https://i.blackhat.com/Asia-22/Friday-Materials/AS-22-Li-To-Loot-Or-Not-To-Loot-That-Is-Not-a-Question.pdf) in targeting the Southeast Asian gambling industry.

Despite the indicators observed, accurate clustering remains challenging. The Chinese APT ecosystem is plagued by extensive sharing of malware and infrastructure management processes between groups, making high confidence clustering difficult based on current visibility. Our analysis has led us to historical artifacts that represent points of convergence between BRONZE STARLIGHT and other China-based actors, which showcases the complexity of a Chinese threat ecosystem composed of closely affiliated groups.

## Background

ESET reported that a ChattyGoblin-related attack in March 2023 targeted the support agents of a gambling company in the Philippines. In the attack, a trojanized LiveHelp100 application downloaded a .NET malware loader named `agentupdate_plugins.exe`. The final payload was a Cobalt Strike beacon using the `duckducklive[.]top` domain for C2 purposes. The hash of this malware loader was not disclosed.

We subsequently identified malware loaders that we assess are closely related to those observed as part of Operation ChattyGoblin and are likely part of the same activity cluster – a .NET executable also named `agentupdate_plugins.exe` and its variant `AdventureQuest.exe`.

This association is based on naming conventions, code, and functional overlaps with the sample described in ESET’s report. Although we cannot conclusively determine whether the `agentupdate_plugins.exe` we analyzed is the same as that reported by ESET, we note that one of its VirusTotal submissions is dated March 2023 and originates from the Philippines. This aligns with the geolocation of the target and the timeline of the ChattyGoblin-related attack involving `agentupdate_plugins.exe`.

## The Malware Loaders

`agentupdate_plugins.exe` and  `AdventureQuest.exe`  deploy .NET executables based on the [SharpUnhooker](https://github.com/GetRektBoy724/SharpUnhooker) tool, which download second-stage data from Alibaba buckets hosted at `agenfile.oss-ap-southeast-1.aliyuncs[.]com` and `codewavehub.oss-ap-southeast-1.aliyuncs[.]com`. The second-stage data is stored in password-protected zip archives.

The zip archives downloaded by `agentupdate_plugins.exe` and `AdventureQuest.exe` contain sideloading capabilities. Each of the archives we were able to retrieve consists of a legitimate executable vulnerable to DLL search order hijacking, a malicious DLL that gets sideloaded by the executable when started, and an encrypted data file named agent.data.

The executables are components of the software products Adobe Creative Cloud, Microsoft Edge, and McAfee VirusScan. The malicious DLLs masquerade as their legitimate counterparts:  They export functions with the same names, such that specific functions, when invoked by the legitimate executables, decrypt and execute code embedded in the data files. The data files we could retrieve implement Cobalt Strike beacons.

|  |  |  |
| --- | --- | --- |
| ****Zip archive**** | ****Archive content**** | ****Final payload**** |
| adobe\_helper.zip (agentupdate\_plugins.exe) | Adobe CEF Helper.exe libcef.dll agent.data (not available) | / |
| cefhelper.zip (AdventureQuest.exe) | identity\_helper.exe msedge\_elf.dll agent.data | Cobalt Strike C2: www.100helpchat[.]com |
| Agent\_bak.zip (AdventureQuest.exe) | mfeann.exe LockDown.dll agent.data | Cobalt Strike C2: live100heip[.]com |

The `100helpchat[.]com` and `live100heip[.]com` C2 domains follow the naming convention of the LiveHelp100 trojanized application used in operation ChattyGoblin, possibly to make malicious network activity look like legitimate LiveHelp100 activity.

`agentupdate_plugins.exe` and `AdventureQuest.exe` implement geofencing based on the [ifconfig.co](https://ifconfig.co/) IP-based geolocation service. The loaders are meant to stop their execution if they are run on a machine located in the United States, Germany, France, Russia, India, Canada, or the United Kingdom. This may indicate that the threat actors have no interest in intrusions in these countries for this campaign. Due to errors in implementation, the geofencing fails to work as intended.

### Stolen Ivacy VPN Certificate

`AdventureQuest.exe` is signed using a certificate issued to the Ivacy VPN vendor PMG PTE LTD:

* Thumbprint: 62E990CC0A26D58E1A150617357010EE53186707
* Serial number: 0E3E037C57A5447295669A3DB1A28B8A.

Ivacy has been present on the market since 2007 and attracts users...