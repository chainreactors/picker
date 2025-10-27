---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 17
url: https://buaq.net/go-161013.html
source: unSafe.sh - 不安全
date: 2023-04-29
fetch_date: 2025-10-04T11:32:45.822690
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 17

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

![](https://8aqnet.cdn.bcebos.com/de81abcf4cf5710b99a4f96962fdd31f.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 17

Threat Hunters Power Up with Conversational AIThis was the week that was RSAC 2023, so good news a
*2023-4-28 21:0:50
Author: [www.sentinelone.com(查看原文)](/jump-161013.htm)
阅读量:32
收藏*

---

## Threat Hunters Power Up with Conversational AI

This was the week that was [RSAC 2023](https://www.rsaconference.com/usa), so good news abounded aplenty as vendors across the cybersecurity space made announcements and reveals about new features, services and products designed to help defenders keep their enterprises safe.

Among these, SentinelOne’s [Purple AI](https://www.sentinelone.com/blog/purple-ai-empowering-cybersecurity-analysts-with-ai-driven-threat-hunting-analysis-response/) is set to be a gamechanger as it brings LLM-powered conversational AI to the Singularity platform, allowing threat hunters to replace complex, structured query language with simple questions, from the specific to the vague. “Am I infected with [SmoothOperator](https://www.sentinelone.com/blog/smoothoperator-ongoing-campaign-trojanizes-3cx-software-in-software-supply-chain-attack/)?”, “Which endpoints are exposed to [Log4J](https://www.sentinelone.com/lp/log4j-log4shell-cve-2021-44228-staying-secure/)?”, “What are the most suspicious events in my environment in the last 24 hours?”.

![PurpleAI threat hunting console generative AI](https://www.sentinelone.com/wp-content/uploads/2023/04/purpleAI_fs_3v2.jpg)

The AI returns results along with identified behavior and recommendations for further action. Coupled with [XDR](https://www.sentinelone.com/resources/the-future-is-xdr-how-to-conquer-the-soc-transformation/) to unite a business’ diverse data sources, the AI can help threat hunting teams to overcome the major challenges of threat hunting: time and skill-level. With many SOC teams struggling with alert fatigue and a skills shortage, PurpleAI will provide a much needed tonic for the troops.

RSAC 2023 also saw SentinelOne announce an exclusive [partnership](https://www.sentinelone.com/blog/shift-left-shield-right-early-availability-of-wiz-integration-with-sentinelone/) with CNAP specialists Wiz. Combining SentinelOne’s Cloud Workload Protection with Wiz’s Cloud Native Application Platform is expected to bring huge benefits to enterprise customers needing to manage and secure cloud infrastructure. For more on what happened at RSAC this week, see our dedicated posts on [Days 1](https://www.sentinelone.com/blog/day-1-from-rsac-2023/), [2](https://www.sentinelone.com/blog/day-2-from-rsac-2023/), [3](https://www.sentinelone.com/blog/day-3-from-rsac-2023/) and [4](https://www.sentinelone.com/blog/day-4-from-rsac-2023/).

## PaperCut Vulnerability Leveraged to Deliver Ransomware

PaperCut servers with known vulnerabilities [CVE-2023-27350](https://nvd.nist.gov/vuln/detail/CVE-2023-27350) and [CVE-2023-27351](https://nvd.nist.gov/vuln/detail/CVE-2023-27351) are being exploited to deliver [Cl0p](https://www.sentinelone.com/labs/cl0p-ransomware-targets-linux-systems-with-flawed-encryption-decryptor-available/) and [LockBit](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques/) ransomware, it was [discovered](https://www.trendmicro.com/en_us/research/23/d/update-now-papercut-vulnerability-cve-2023-27350-under-active-ex.html) this week. The print management software is used widely in enterprises to monitor and control printing tasks.

The [vulnerabilities](https://www.papercut.com/kb/Main/PO-1216-and-PO-1219) may have been weaponized as early as April 13, five days prior to the first reported suspicious activity linked to exploitation of unpatched PaperCut servers. The vulnerabilities in PaperCut NG and MF products expose the servers to unauthenticated remote code execution attacks and can also allow unauthorized attackers to steal credentials and PII.

![](https://www.sentinelone.com/wp-content/uploads/2023/04/papercut.jpg)

In one in the wild case, attackers compromised a target with [PowerShell](https://www.sentinelone.com/cybersecurity-101/windows-powershell/) scripts to deliver [LockBit ransomware](https://www.sentinelone.com/anthology/lockbit-3-0-lockbit-black/). Meanwhile, Microsoft reported that a [Cl0p-affiliated ransomware](https://www.sentinelone.com/anthology/clop/) gang was conducting multi-stage attacks on vulnerable PaperCut servers that begin with PowerShell delivering a TrueBot payload and then use Cobalt Strike for lateral movement and data exfiltration.

Needless to say, organizations deploying PaperCut are urged to ensure that all instances are updated as a matter of urgency.

## RTM Locker Ransomware Targets Virtual Machine Servers

Recent weeks have seen a number of examples of how threat actors continue to explore new opportunities for compromise and seek new targets to exploit. In this regard, we’ve seen LockBit experimenting with [macOS ransomware](https://www.sentinelone.com/blog/lockbit-for-mac-how-real-is-the-risk-of-macos-ransomware/), and an increase in payloads targeting [Linux](https://www.sentinelone.com/labs/icefire-ransomware-returns-now-targeting-linux-enterprise-networks/), which of course is widely used in servers as well as devices common in the enterprise, from routers and printers to IoT ‘smart’ appliances and security cameras.

The latest [development](https://www.uptycs.com/blog/rtm-locker-ransomware-as-a-service-raas-linux) is a variant of the RTM Locker ransomware that specifically targets Linux, NAS and, significantly, virtual machines on VMware ESXi hosts. ESXi servers have become increasingly popular with the rise of cloud computing and cloud infrastructure as a means to deploy and manage enterprise level virtual computers, making them attractive targets for threat actors.

The new variant of RTM Locker is said to be based on leaked [Babuk ransomware](https://www.sentinelone.com/anthology/babuk/) source code. On execution, it kills all running VM clients on the ESXi host and begins encrypting files. Locked files are appended with a `.RTM` extension and a ransom note entitled `!!!Warning!!!` is dropped on the compromised server. The ransomware uses asymmetric encryption, meaning decryption is only possible with possession of the private key held by an attacker.

![RTM locker ransom note](https://www.sentinelone.com/wp-content/uploads/2023/04/RTM-locker-ransom-note.jpg)

Source: Uptycs

The hardcoded ransomware note shows that the victims need to install the encrypted chat client Tox in order to negotiate payment of the ransom. Exactly how active the RTM group is at the moment is open to debate, but the developers have been seen advertising for affiliates in darknet forums with translations available in English, Russian and Chinese languages.

文章来源: https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-17-4/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)