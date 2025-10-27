---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 23
url: https://buaq.net/go-168066.html
source: unSafe.sh - 不安全
date: 2023-06-10
fetch_date: 2025-10-04T11:44:30.884328
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 23

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

![](https://8aqnet.cdn.bcebos.com/37803413304ab05bdbc73495c09e09b4.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 23

The Good | SEC Gets Tough With ‘Wild West’ CryptoWhatever its merits, it’s fair to say that the bo
*2023-6-9 21:0:32
Author: [www.sentinelone.com(查看原文)](/jump-168066.htm)
阅读量:28
收藏*

---

## The Good | SEC Gets Tough With ‘Wild West’ Crypto

Whatever its merits, it’s fair to say that the boom in [cryptocurrency](https://www.sentinelone.com/blog/malware-analyst-guide-bitcoin/) has helped fuel the rampant cybercrime and ransomware scene organizations face today, as well as [help fund](https://www.bleepingcomputer.com/news/security/lazarus-hackers-linked-to-the-35-million-atomic-wallet-heist/) certain nation-state threat actors. Good news, then, that the SEC is starting to [flex its muscles](https://cybernews.com/crypto/coinbase-crypto-exchange-suit-follows-binance-sec-case/) and hold crypto firms accountable to the same rules and standards of good governance expected elsewhere in our financial system.

On Monday, the SEC filed charges against Binance, the world’s largest cryptocurrency exchange, and its founder, Changpeng Zhao, and by Tuesday brought further [charges](https://www.cnbc.com/2023/06/06/sec-asks-for-emergency-order-to-freeze-binance-us-assets-anywhere-in-the-world.html) seeking to freeze the company’s U.S. assets. The initial charges alleged that Binance and Zhao had defrauded investors, operated as an unregistered broker and improperly commingled investor and Binance’s funds. The charges saw investors pull almost [$800 million](https://www.cnbc.com/2023/06/06/binance-outflows-investors-pull-790-million-after-sec-charges.html) from the firm in 24 hours.

> BREAKING: [@SECGov](https://twitter.com/SECGov?ref_src=twsrc%5Etfw) has sued [@coinbase](https://twitter.com/coinbase?ref_src=twsrc%5Etfw) on charges of violating federal securities law, a day after filling a similar suit against rival [@binance](https://twitter.com/binance?ref_src=twsrc%5Etfw). By [@nikhileshde](https://twitter.com/nikhileshde?ref_src=twsrc%5Etfw).<https://t.co/ATcyrrDiCN>
>
> — CoinDesk (@CoinDesk) [June 6, 2023](https://twitter.com/CoinDesk/status/1666061200877051904?ref_src=twsrc%5Etfw)

The SEC followed its actions against Binance with [charges](https://www.sec.gov/news/press-release/2023-102) against Coinbase for operating as an unregistered securities exchange, broker and clearing house, as well as for the unregistered sale of its crypto asset staking-as-a-service program. The action was followed by Moody’s downgrading its rating of Coinbase to ‘negative’ and other financial services firms saying that shares in the company were ‘uninvestable’ in the short term.

“The whole business model is built on a noncompliance with the U.S. securities laws and we’re asking them to come into compliance,” the SEC said in a statement. Both companies deny the charges.

## The Bad | Clop Gang Hits Hundreds of Orgs via MOVEit Bug

Cl0p (*aka* Clop) ransomware gang has [claimed](https://www.theguardian.com/technology/2023/jun/07/cybercrime-clop-ultimatum-british-airways-boots--bbc-mass-hack) responsibility this week for breaches of multiple organizations after exploiting a now-patched bug (CVE-2023-34362) in the [MOVEit file transfer](https://www.sentinelone.com/blog/moveit-transfer-exploited-to-drop-file-stealing-sql-shell/) application.

Aer Lingus, British Airways, Boots and the BBC are among hundreds of organizations [the gang](https://www.sentinelone.com/anthology/clop/) say they have stolen data from and are threatening to leak unless the victims pay a ransom. No fixed sum has been demanded by the attackers, who insist victims need to contact them and begin negotiations.

![clop ransomware BA Boots MOVEit](https://www.sentinelone.com/wp-content/uploads/2023/06/GBU4-Wk22_1.jpg)

The mass scale of the attack appears to have been facilitated by a supply chain attack on payroll services firm Zellis, used by many of the victims. [Technical details](https://www.sentinelone.com/blog/moveit-transfer-exploited-to-drop-file-stealing-sql-shell/) of the attack were published by SentinelOne on Wednesday. The attacks are conducted against Windows servers running a vulnerable version of the MOVEit file transfer application, specifically one of the following versions:

* MOVEit Transfer 2023.0.0 (patched in 2023.0.1)
* MOVEit Transfer 2022.1.x (patched in 2022.1.5)
* MOVEit Transfer 2022.0.x (patched in 2022.0.4)
* MOVEit Transfer 2021.1.x (patched in 2021.1.4)
* MOVEit Transfer 2021.0.x (patched in 2021.0.6)

The vulnerability allows an unauthorized attacker to inject SQL commands and conduct an arbitrary file upload. The final payload is a minimal webshell that queries information about the database configuration, enabling the actor to connect to specified SQL databases and exfiltrate the contents of files hosted by MOVEit Transfer and, where connected, files in Azure’s blob storage service.

Organizations are urged to ensure that any instances of MOVEit Transfer are patched without delay. SentinelOne has provided hunting queries and a script to scan for potential exploitation of the MOVEit Transfer vulnerability [here](https://s1.ai/MOVEit).

## The Ugly | Suspected Nation State Targets US Aerospace

An unknown threat actor [infiltrated](https://adlumin.com/post/powerdrop-a-new-insidious-powershell-script-for-command-and-control-attacks-targets-u-s-aerospace-defense-industry/) a U.S. defense contractor it was revealed this week, using a combination of [WMI](https://www.sentinelone.com/labs/labscon-replay-blasting-event-driven-cornucopia-wmi-based-user-space-attacks-blind-siems-and-edrs/) and [PowerShell](https://www.sentinelone.com/cybersecurity-101/windows-powershell/) to evade detection in a novel RAT dubbed ‘PowerDrop’.

According to researchers, PowerDrop is not particularly sophisticated but its focus on obfuscation and evasion, along with the targeting of an aerospace contractor point the finger at a nation-state actor. The malware takes the form of a single command line argument containing base64-encoded PowerShell script passed to `wmic.exe` for execution.

The script reaches out as a beacon to a hard-coded IP address every 120 seconds over an ICMP Echo Request message and then waits 60 seconds for a response from the C2.

![PowerDrop Backdoor RAT ](https://www.sentinelone.com/wp-content/uploads/2023/06/GBU4-Wk22_2.jpg)

Source: [Adlumin](https://adlumin.com/post/powerdrop-a-new-insidious-powershell-script-for-command-and-control-attacks-targets-u-s-aerospace-defense-industry/)

The remote operators can then task the backdoor via a 128-bit AES encrypted payload. PowerDrop decrypts the command, runs it and returns the results to the C2. The researchers say that PowerDrop uses the strings “DRP” and “OCD” to indicate the start and end of the response content unless it is split into multiple messages, in which case all messages have the “DRP” string prefix, and only the final message contains both the “DRP” prefix and “ORD” suffix.

The discovery is yet another reminder of the ongoing threat to our [critical infrastructure](https://www.sentinelone.com/blog/securing-the-nations-critical-infrastructure-action-plans-to-defend-against-cyber-attacks/) and the need for organizations to ensure they have a robust [cyber defense posture](https://www.sentinelone.com/industry-recognition/)

文章来源: https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-23-4/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* adm...