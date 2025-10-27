---
title: Silence is golden partner for Truebot and Clop ransomware
url: https://buaq.net/go-139898.html
source: unSafe.sh - 不安全
date: 2022-12-14
fetch_date: 2025-10-04T01:23:06.281910
---

# Silence is golden partner for Truebot and Clop ransomware

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

![]()

Silence is golden partner for Truebot and Clop ransomware

A recent rise in the number of Truebot infections has been attributed t
*2022-12-13 21:0:0
Author: [www.malwarebytes.com(查看原文)](/jump-139898.htm)
阅读量:18
收藏*

---

A recent rise in the number of Truebot infections has been attributed to a threat actor known as the Silence Group. The Silence Group is an [initial access broker (IAB)](https://www.malwarebytes.com/blog/business/2022/11/initial-access-brokers-iabs-3-ways-they-break-into-corporate-networks-and-how-to-detect-them) that frequently changes tools and tactics to stay on top of the game. An IAB's primary task is to find a weakness or vulnerability, create a foothold in a network, and do some exploratory work to find out how attractive the target is. Once this is done they can sell the access to another threat actor, like a ransomware group. For these tasks Truebot is the tool of choice in the Silence Group.

The Silence Group seems to have a strong relation with the group behind Clop ransomware, often referenced as [TA505](https://attack.mitre.org/groups/G0092/). Which, in turn, has a large overlap with the FIN11 group.

## Truebot

The [researchers](https://blog.talosintelligence.com/breaking-the-silence-recent-truebot-activity/) identified two separate Truebot botnets. One of which appears to be focused on the US, while the other is predominantly focused at Mexico, Pakistan, and Brazil.

We touched on the second one when we wrote about the [recent activities of the Raspberry Robin worm](https://www.malwarebytes.com/blog/news/2022/10/raspberry-robin-worm-used-as-ransomware-prelude). The use of this worm, in combination with an attack vector leveraging a Netwrix vulnerability, seems the have laid the ground work for the creation of a botnet of over 1,000 systems that is distributed worldwide.

The other botnet is almost exclusively composed of Windows servers, directly connected to the internet, and exposes several Windows services such as SMB, RDP, and WinRM. The attack vector that was used to establish this botnet has not yet been identified, although the researchers are confident that it is different from those used for the other botnet, Raspberry Robin and the Netwrix vulnerability ([CVE-2022-31199](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31199)).

## New version

At its core, Truebot is a [Trojan.Downloader](https://www.malwarebytes.com/blog/detections/trojan-downloader). As such, it is an ideal malware for IAB groups that want to plant a backdoor on a system and do some basic reconnaissance of the network. For those purposes, this new version of Truebot collects this information: a screenshot, the computer name, the local network name, and active directory trust relations. Active Directory trust relations allow organizations to share users and resources across domains.

What’s also new is that this version is now capable of loading and executing additional modules and shellcodes in memory, making the payloads [fileless malware](https://www.malwarebytes.com/blog/news/2021/10/what-is-fileless-malware) which is less likely to be detected.

## Exfiltration

Besides the usual suspects designed to act as a backdoor, Cobalt Strike and Grace, the researchers also found a new data exfiltration tool. Finding Grace as a payload seems to confirm the close ties between the Silence Group and TA505 since Grace was almost exclusively used by TA505.

The exfiltration tool, dubbed Teleport, was used extensively by the attackers to steal information from the network. It seems to be a custom data exfiltration tool built in C++ , containing several features that make the process of data exfiltration easier and stealthier. It has some features that are not commonly found in remote copying tools but which make it very useful to an attacker stealthily exfiltrating data.

* It limits the upload speed, which can make the transmission go undetected by tools that monitor for large data exfiltration and avoids slowing down the network.
* The communication is encrypted to hide what information is being transmitted.
* Limiting the file size, which can maximize the number of stolen files by avoiding lengthy copies of files that may not be interesting.
* The ability to delete itself after use, which is ideal to keep it as unknown as possible.

## Clop

[Ransom.Clop](https://www.malwarebytes.com/blog/detections/ransom-clop) was first seen in February of 2019. Besides encrypting systems, the Clop ransomware also exfiltrates data that will be published on a leak site if the victim refuses to pay the ransom. In February of 2021, the group made [headlines](https://www.malwarebytes.com/blog/news/2021/02/clop-targets-execs-ransomware-tactics-get-another-new-twist) by targeting executives' systems specifically to find sensitive data.

## Mitigation

The tools that are used by Silence are versatile, but there are a few logical steps you can take to protect yourself and your organization:

* Do not insert USB drives of unknown or unreliable origin into your systems.
* In Windows, the autorun of USB drives is disabled by default. However, many organizations have widely enabled it through legacy Group Policy changes. If you enabled it, this is a policy worth re-thinking.
* Install [patches](https://www.malwarebytes.com/business/vulnerability-patch-management) as soon as possible, especially for internet facing devices.
* Run an [anti-virus/anti-malware solution](https://www.malwarebytes.com/business) that actively monitors and scans your systems.

Malwarebytes blocks the download URLs and detects Truebot as Malware.AI.{id.nr.}. Clop ransomware is detected as Malware.Ransom.Agent.Generic.

---

文章来源: https://www.malwarebytes.com/blog/news/2022/12/silence-is-golden-partner-for-truebot-and-clop-ransomware
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)