---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 50
url: https://buaq.net/go-139401.html
source: unSafe.sh - 不安全
date: 2022-12-10
fetch_date: 2025-10-04T01:05:26.539006
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 50

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

![](https://8aqnet.cdn.bcebos.com/b607b16e1af51b291496f6d2bb0b8520.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 50

The GoodWhen programmers make mistakes that turn into news, it’s almost invariably because some th
*2022-12-9 22:0:27
Author: [www.sentinelone.com(查看原文)](/jump-139401.htm)
阅读量:45
收藏*

---

## The Good

When programmers make mistakes that turn into news, it’s almost invariably because some threat actor or another has weaponized that coding error into a [zero-day exploit](https://www.sentinelone.com/blog/enterprise-security-essentials-top-15-most-routinely-exploited-vulnerabilities-2022/), and the rest of us are urged to rush off and patch the affected software. Good news this week, then, to see that a [cryptomining](https://www.sentinelone.com/labs/caught-in-the-cloud-how-a-monero-cryptominer-exploits-docker-containers/) botnet has effectively been made redundant due to a developer mistake.

![](https://www.sentinelone.com/wp-content/uploads/2022/12/game-over-scaled.jpg)

Researchers at Akamai had previously [reported](https://www.akamai.com/blog/security-research/kmdsbot-the-attack-and-mine-malware) on their discovery of KmsdBot, a cryptomining botnet written in Go that they said had infected unnamed brands within the gaming industry, the technology industry, and luxury car manufacturing. KmsdBot was found to be propagating by [brute forcing](https://www.sentinelone.com/blog/detecting-brute-force-password-attacks/) weak SSH credentials.

This week, the same researchers observed that the [botnet](https://www.sentinelone.com/blog/8220-gang-cloud-botnet-targets-misconfigured-cloud-workloads/) had a fatal flaw: the malware crashed after receiving a malformed command, and since the botnet also had no persistence capabilities, crashing it effectively removed the botnet from the infected device.

The researchers [say](https://www.akamai.com/blog/security-research/kmsdbot-part-two-crashing-a-botnet) that the malformed command likely crashed all the botnet code running on infected machines and talking to the C2, essentially, killing the botnet. The developer had failed to write error handling code to handle typos in input received from the botnet operator.

No doubt that’s a bug the botnet developer will be rushing to fix, but they’ll also have to start over from scratch in terms of infecting devices, and that’s good news for those companies that had fallen prey to KmsdBot.

## The Bad

Sticking with botnets, on the flip side the bad news this week is that a recently discovered [botnet](https://www.fortinet.com/blog/threat-research/zerobot-new-go-based-botnet-campaign-targets-multiple-vulnerabilities) called Zerobot is doing the rounds with a hardcoded list of 21 known exploits in BIG-IP, Zyxel, D-Link and other devices.

Like Kmdsbot, Zerobot is written in Go, but the developers are clearly more technically proficient. The botnet targets any of the hardcoded exploits to gain initial access and then tries to reproduce itself and infect any Windows or Linux endpoints on the network that have the known vulnerabilities.

On Windows devices, it copies itself to the “Startup” folder using the filename “FireWall.exe”; on Linux, three file paths are targeted to drop the malware: `%HOME%`, `/etc/init/`, and `/lib/systemd/system/`. Zerobot also attempts to protect itself by intercepting any signal sent to terminate or kill the process.

The botnet tries to communicate with its C2 over `176[.]65[.]137[.]5`. However, as the malware appears to be under active development, that is sure to change, as will the list of known CVES, which currently include:

|  |  |
| --- | --- |
| **CVE ID** | **Affected Product** |
| CVE-2014-08361 | minigd SOAP service in Realtek SDK |
| CVE-2017-17106 | Zivif PR115-204-P-RS V2.3.4.2103 Webcams |
| CVE-2017-17215 | Huawei HG532 Router |
| CVE-2018-12613 | phpMyAdmin |
| CVE-2020-10987 | Tend AC15 AC1900 Router |
| CVE-2020-25506 | D-Link DNS-320 NAS |
| CVE-2021-35395 | Realtek Jungle SDK |
| CVE-2021-36260 | Hikvision product |
| CVE-2021-46422 | Telesquare SDT-CW3B1 Router |
| CVE-2022-01388 | F5 BIG-IP |
| CVE-2022-22965 | Spring MVC or Spring WebFlux application (Spring4Shell) |
| CVE-2022-25075 | TOTOLink A3000RU Router |
| CVE-2022-26186 | TOTOLINK N600R Router |
| CVE-2022-26210 T | otolink A830R Router |
| CVE-2022-30525 | Zyxel USG FLEX 100(W) Firewall |
| CVE-2022-34538 | Digital Watchdog DW MEGApix IP cameras |
| CVE-2022-37061 | FLIR AX8 thermal sensor cameras |

Organizations or individuals running any of the affected devices are urged to contact the device manufacturers’ support services and apply patches as soon as possible.

## The Ugly

Things have been turning ugly for a while now in state-sponsored cyber warfare, and this week it’s the use of wiper malware that’s grabbing the headlines as two separate reports show threat actors doing their best to infect and destroy data belonging to their adversaries.

Iranian-linked APT [Agrius](https://www.sentinelone.com/labs/from-wiper-to-ransomware-the-evolution-of-agrius/) has been actively attacking targets in Hong Kong, Israel and South Africa with a new wiper named [Fantasy](https://www.welivesecurity.com/2022/12/07/fantasy-new-agrius-wiper-supply-chain-attack/), hidden inside software commonly used in the diamond industry. Known targets include a diamond wholesaler, a jeweler, an IT support services firm, and an HR consulting company. Fantasy targets Windows devices and overwrites the content of files with random data. It also overwrites the master boot record, deletes itself, and reboots the system.

Fantasy is a variant of the [Apostle](https://www.sentinelone.com/labs/from-wiper-to-ransomware-the-evolution-of-agrius/) software first identified by [SentinelLabs](https://www.sentinelone.com/labs/), a wiper that was later turned into a fully functional ransomware. Unlike ransomware though, wipers are not meant to leverage the victim and are only intended to disrupt the target’s ability to operate by destroying systems, services and data.

> [#ESETresearch](https://twitter.com/hashtag/ESETresearch?src=hash&ref_src=twsrc%5Etfw) identified a new wiper from [#Agrius](https://twitter.com/hashtag/Agrius?src=hash&ref_src=twsrc%5Etfw), a suspected Iranian 🇮🇷 threat actor that previously deployed the Apostle [#ransomware](https://twitter.com/hashtag/ransomware?src=hash&ref_src=twsrc%5Etfw) and [#wiper](https://twitter.com/hashtag/wiper?src=hash&ref_src=twsrc%5Etfw). 1/5 <https://t.co/3YgyjZ2SQF>
>
> — ESET Research (@ESETresearch) [December 7, 2022](https://twitter.com/ESETresearch/status/1600439616128942081?ref_src=twsrc%5Etfw)

Meanwhile, it’s also been [reported](https://arstechnica.com/information-technology/2022/12/never-before-seen-malware-is-nuking-data-in-russias-courts-and-mayors-offices/) this week that Russian courts and mayoral offices have been targeted with a wiper dubbed [CryWiper](https://www.kaspersky.com/blog/crywiper-pseudo-ransomware/46480/). Researchers say that CryWiper pretends to be ransomware: it adds a .CRY extension to files and drops a ransom note with a [bitcoin](https://www.sentinelone.com/blog/malware-analyst-guide-bitcoin/) address and other details for payment. In reality, however, targeted files are not encrypted: they are overwritten with random data, making the originals unrecoverable.

Although these wipers are highly-targeted, malware used by APTs often finds itself in the hands of cybercriminals. Fortunately, the defence against wipers and ransomware, not to mention cryptomining botnets and other malware  is the same: [a trusted endpoint security solution](https://www.sen...