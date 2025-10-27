---
title: Analyzing Attack Opportunities Against Information Security Practitioners
url: https://buaq.net/go-171662.html
source: unSafe.sh - 不安全
date: 2023-07-11
fetch_date: 2025-10-04T11:51:16.927474
---

# Analyzing Attack Opportunities Against Information Security Practitioners

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

![](https://8aqnet.cdn.bcebos.com/8208668ff3fcc1e885c20c652b88083a.jpg)

Analyzing Attack Opportunities Against Information Security Practitioners

In partnership with vx-underground, SentinelOne recently ran its first Malware Research Challenge,
*2023-7-10 21:0:27
Author: [www.sentinelone.com(查看原文)](/jump-171662.htm)
阅读量:42
收藏*

---

In partnership with [vx-underground](https://twitter.com/vxunderground), SentinelOne recently ran its first [Malware Research Challenge](https://www.sentinelone.com/lp/vx-s1/), in which we asked researchers across the cybersecurity community to submit previously unpublished work to showcase their talents and bring their insights to a wider audience.

Today’s post is the second in a [series](https://www.sentinelone.com/blog/neo_net-the-kingpin-of-spanish-ecrime/) highlighting the best entries. Jared Stroud ([@DLL\_Cool\_J](https://twitter.com/dll_cool_j) / [Arch Cloud Labs](https://www.archcloudlabs.com/projects)) explores the risks faced by security researchers from attacks by APTs and other threat actors through compromise of security research tools. The study includes discussion of a novel attack vector through popular open-source reverse engineering platform, Ghidra.

![](https://www.sentinelone.com/wp-content/uploads/2023/07/Analyzing-Attack-Opportunities-Against-Information-Security-Practitioners-9.jpg)

## Background

Attacks against the Information Security research community have historically ranged from fake proof-of-concept Github repos to modifying Visual Studio project data resulting in the execution of  PowerShell commands. In recent years threat actors have begun targeting software heavily used within the Information Security community. Observed targeting techniques include directly selecting individuals of the security research community through phishing campaigns or by casting a wider opportunistic net by seeding illegal software torrents. As an industry, one’s circle of trust creates an environment where the attack surface to security practitioners is unique and wider than one may think.

Sophisticated attacks are focused on those that provide much value to the Information Security community through blog posts, Youtube Channels, and other various forms of information sharing. This article will explore some of these historical attacks along with identifying the attack surface of a researcher’s toolkit as well as defensive strategies for the community for said attacks.

## Historical Targeted Attacks Against Software Used by Security Practitioners

Security Company ESET reported in 2021 that threat actors linked to DPRK backdoored IDA Pro torrents via malicious DLLs within the installation folder of IDA Pro. Arch Cloud Labs does not condone the use of pirated software, but it is likely this software was chosen due to the probability of discovering additional security research on a victim’s machine. After all, why choose IDA Pro? Other actors have [backdoored](https://blog.avast.com/malicious-cracked-games-pose-risks-avast) popular resource-intensive video game torrents to make use of GPUs for Cryptojacking campaigns. Per ESET’s [tweets](https://twitter.com/ESETresearch/status/1458438155149922312), upon launching IDA Pro, a scheduled task is created which downloads an additional DLL by the name of IDA Helper to fetch and execute a remotely hosted payload for follow-on post-exploitation activity.

Abusing DLL hijacking opportunities within Windows software is nothing new, but rather demonstrates the intent of the threat actor to focus on the individuals that use IDA Pro, such as security researchers. By focusing on torrent software, the threat actor also gains the security that even if an endpoint security product flags this software as malicious, the victim themselves downloading software illegally, perhaps they’ll think it’s simply something to do with the torrent, associated crack but certainly not that they’ve been targeted by a nation-state adversary.

In 2022, Google’s Threat Analytic Group (TAG) [reported](https://blog.google/threat-analysis-group/new-campaign-targeting-security-researchers/) a targeted phishing campaign focusing on security researchers under the guise of having known security researchers aid the attacker in finalizing a proof-of-concept exploit. This proof-of-concept exploit ultimately was a Visual Studio project which executed a PowerShell command to aid in data exfiltration of a Security Researcher’s lab environment. Numerous individuals on Twitter came forward saying they had some established contact with puppet accounts that were requesting help.

Those that seek to mentor and help one another in this industry should be applauded for their efforts, but also be wary of how this can be abused in elaborate phishing campaigns such as those reported by Google TAG. It’s unlikely that these types of attacks will slow down in the coming years, and as security practitioners understanding our tools of the trade and their associated attack surface is critical in protecting ourselves as well as our research. If one looks hard enough, the ability to use a given reverse engineering or digital forensics tool to achieve [living off the land](https://lolbas-project.github.io/) types of attacks can be found. Arch Cloud Labs analyzed how these types of attacks could be applied to other widely used software such as Ghidra to enable a threat actor to target members of the security community and will demonstrate such an attack later in this article.

## Opportunistic Attacks During a CVE Crisis

Academic scholars from Leiden University recently published a [paper](https://arxiv.org/abs/2210.08374) stating that 10% of proof-of-concept exploitation repos on Github contain code meant to exfiltrate sensitive data from the targeted environment. In the event a researcher’s VM is not appropriately air-gapped or isolated to an individual project, the opportunity for sensitive data loss exists. During moments of crisis such as a high-impact vulnerability (*Ex: unauthenticated RCE*), defenders seek to quickly understand, assess and remediate the potential impact a given vulnerability may have in their organization. This leads to researchers publishing proof-of-concept (PoC) code on GitHub for use in the wider community.

As defenders rush to Github, this creates a “watering hole” attack scenario where independent or otherwise unknown researchers have the opportunity to name a Github repo “*PoC CVE-XXXX-XXXX*” to gain incoming traffic for the latest vulnerability. In 2020, [Andy Gill](https://blog.zsec.uk/cve-2020-1350-research/) demonstrated a perfect example of this by creating a Github repo with a bash script that would Rick Roll security researchers.

When seeking to identify whether or not a Github repo is trustworthy, how do you or your research colleagues determine this? Do you audit the code or simply look at the number of stars a repo has and think “*this is probably fine*”? The concept of trust in PoC-exploitation is unique to the Information Security arena as outside of commercial or well-known offensive frameworks, how often is malicious software being executed in your corporate environment intentionally? Ideally never, but a framework or risk matrix for assessing a proof-of-concept legitimacy is an area that the industry has yet to fully explore.

## Identifying Attack Surface of Researcher’s Tools: Case Study Ghidra

Complex software such as Visual Studio or IDA Pro contains numerous ways to achieve code execution. Understanding the tool and how its functionality can be abused is critical to understand the paths an adversary could take to leverage re...