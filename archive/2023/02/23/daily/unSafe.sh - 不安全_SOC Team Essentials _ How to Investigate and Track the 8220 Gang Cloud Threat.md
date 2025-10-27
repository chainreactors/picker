---
title: SOC Team Essentials | How to Investigate and Track the 8220 Gang Cloud Threat
url: https://buaq.net/go-150572.html
source: unSafe.sh - 不安全
date: 2023-02-23
fetch_date: 2025-10-04T07:49:13.037180
---

# SOC Team Essentials | How to Investigate and Track the 8220 Gang Cloud Threat

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

![](https://8aqnet.cdn.bcebos.com/8378d511f8cdec1d7e96f4533184556f.jpg)

SOC Team Essentials | How to Investigate and Track the 8220 Gang Cloud Threat

8220 Gang is a low-skill crimeware actor known for infecting cloud hosts through n-day vulnerabilit
*2023-2-22 21:0:10
Author: [www.sentinelone.com(查看原文)](/jump-150572.htm)
阅读量:35
收藏*

---

8220 Gang is a low-skill crimeware actor known for infecting cloud hosts through [n-day](https://www.sentinelone.com/cybersecurity-101/cyber-threat-intelligence/) vulnerabilities and remote access brute forcing. We have previously detailed how 8220 [expanded its botnet](https://www.sentinelone.com/blog/from-the-front-lines-8220-gang-massively-expands-cloud-botnet-to-30000-infected-hosts/) and [rotated its infrastructure](https://www.sentinelone.com/blog/8220-gang-cloud-botnet-targets-misconfigured-cloud-workloads/). Since our last write up in October, the group has again switched to new infrastructure and samples, providing us with an opportunity to share an educational walkthrough of the process of investigating cybercrime activity that may be useful to new or lesser experienced SOC teams, analysts and researchers.

In this post, we use 8220 Gang activity as a lens through which to explain the process of investigating a threat, researching the threat activity as a whole, and gaining a perspective into attacker objectives, ultimately concluding with a wider understanding of related threat intelligence.

![](https://www.sentinelone.com/wp-content/uploads/2023/02/SOC-Team-Essentials-How-to-Investigate-and-Track-the-8220-Gang-Cloud-Threat-4.jpg)

## Refresher on 8220 Gang

8220 Gang (pronounced eighty-two twenty), also known as 8220 Mining Group, was first publicly reported by Talos in 2018. Victims of 8220 Gang are typically, but not exclusively, users of cloud networks operating vulnerable and misconfigured Linux applications and services.

Attacks make use of SSH brute forcing post-infection to automate local and global spreading attempts. Victims using cloud infrastructure (AWS, Azure, GCP, Aliyun, QCloud) are often infected via publicly accessible hosts running Docker, Confluence, Apache WebLogic, and Redis. Victims are not targeted geographically but simply identified by their internet accessibility.

## Initial Discovery

Our walkthrough starts with the initial discovery of an interesting script found on a compromised AWS machine with publicly available SSH service secured with weak credentials. For readers not running a honeypot, this initial discovery could have also been observed in the monitoring of new files uploaded to file scanning services like [VirusTotal](https://www.virustotal.com/) or [MalShare](https://malshare.com/). For those looking to monitor this group, international SSH honeypots plus VirusTotal YARA rules offer a reliable method of catching new activity as it occurs.

The script in question has the SHA1 [a9da0947243333d95f84f6a0e37b9fc29b2fb054](https://www.virustotal.com/gui/file/cf399072dcc8c479ae2358610f5a3e83028fb11df1ffb63d99520d3d44c11d35).

![8220 Infection Script Snippet](https://www.sentinelone.com/wp-content/uploads/2023/02/SOC-8220_4.jpg)

8220 Infection Script Snippet

We can see it is quite simple in design and built around the process of downloading and setting persistence of some other file.

With a few string pivots inside VT, or even a few Google searches, we can quickly discover the core functionality of the script has been widely reported on as it has been reused by many amateur cryptocurrency mining groups and opportunistic profit-seeking attackers.

![Pivoting on part of the script’s content in VTi](https://www.sentinelone.com/wp-content/uploads/2023/02/SOC-8220_3.jpg)

Pivoting on part of the script’s content in VirusTotal Intelligence

One example of such reporting is our [July 2022 post](https://www.sentinelone.com/blog/from-the-front-lines-8220-gang-massively-expands-cloud-botnet-to-30000-infected-hosts/) on 8220 Gang expanding their botnet to roughly 30,000 hosts. However, this time the attacker-specific infrastructure is different, and we have not determined if it has delivered similar malware. Remember, this “infection script” is used by many attackers, and it alone is a very weak source of attribution.

## 8220 Infection Script Analysis

The script goes through a set of instructions, often at multiple levels of encoded commands, aimed at the delivery of setting persistence on the victim machine by downloading itself from malicious servers. The multiple levels of Base64 encoding attempt to hide the fact that it is also downloading a specific payload as well. This is first observed under the `createservices` function.

![Infection Script createservices Function](https://www.sentinelone.com/wp-content/uploads/2023/02/SOC-8220_2.jpg)

Infection Script *createservices* Function

One difference that’s quickly apparent to past reporting on the script is that the attacker began adding the `lwp-download` command as a failover for `wget` and `curl` to enable downloading commands. We initially observed this activity on January 6th, and since then the actor has continued to standardize it in their infection scripts today. Sysdig [also noted this activity](https://sysdig.com/blog/8220-gang-continues-to-evolve) in a recent blog.

![Infection Script use of lwp-download](https://www.sentinelone.com/wp-content/uploads/2023/02/SOC-8220_6.jpg)

Infection Script use of *lwp-download*

The key take away from analyzing these infection scripts is noting unique additions, like `lwp–download`, combined with the destination of download requests. By clustering infection scripts based on function names and order, if the functions are called, and what infrastructure is associated, we can weed out the non-8220 Gang samples.

Additionally, we can link this further based on the encoding quantity and repetition to past 8220 Gang samples. For example, in our infection scripts `createservices` makes use of three [base64 encoded](https://www.sentinelone.com/blog/guide-encode-decoded-base64/) `echo` commands. The first command can be decoded into a new script which pings associated attacker infrastructure and then starts a “payload” command.

![Infection Script’s encoded payload](https://www.sentinelone.com/wp-content/uploads/2023/02/SOC-8220_5.jpg)

Infection Script’s encoded payload

The payload contains two additional base64 encoded scripts to set permissions, download, and configure miner and IRC bot infections. This functionality communicates with `194.38.23[.]170`.

## Post-Infection Activity & Sample Pivots

The post infection activity for this and other recent 8220 infection scripts evolve slightly, but generally proceed with infecting the victim with an updated PwnRig cryptocurrency miner and IRC bot.

In the infection scripts we observed in this campaign, the group continued to use old bash IRC bot “Tsunami”. The sample delivered remains unchanged; however, the network it communicates with evolves over campaigns. The infection script here delivered [472548a4b8295182f6ba8641d74725c2250b7243](https://www.virustotal.com/gui/file/0013b356966c3d693b253cdf00c7fdf698890c9b75605be07128cac446904ad9/details) – the Tsunami sample.

More useful for tracking 8220 Gang are the samples of PwnRig – the custom version of the open source XMRig cryptocurrency miner – that they drop. In this campaign, the script downloads the UPX packed sample [38be55f1fc4ce1cb5438236abc5077019e5e1cdf](https://www.virustotal.com/gui/file/e2c3e81aa24b20ac71147340adc1eaedf077ad00e4a2359e3db47b166cf5411a/details), which unpacks to [332485bd460f55117a254f8164736b90d74aa9f6](https://...