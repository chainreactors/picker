---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 14
url: https://buaq.net/go-157575.html
source: unSafe.sh - 不安全
date: 2023-04-08
fetch_date: 2025-10-04T11:29:50.967153
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 14

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

![](https://8aqnet.cdn.bcebos.com/e27868c0a79146eab03e5adbd74ca9fc.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 14

Operation Cookie Monster | Genesis Market Bites the DustThis week, cyber cops from multiple countr
*2023-4-7 21:0:51
Author: [www.sentinelone.com(查看原文)](/jump-157575.htm)
阅读量:24
收藏*

---

## Operation Cookie Monster | Genesis Market Bites the Dust

This week, cyber cops from multiple countries took down another major marketplace that traded stolen credentials and other sensitive information, known as Genesis market. According to the [DoJ](https://www.justice.gov/usao-edwi/pr/genesis-market-disrupted-international-cyber-operation), Genesis offered access to over 1.5 million compromised devices worldwide and was a key enabler of [ransomware](https://www.sentinelone.com/anthology/).

![](https://www.sentinelone.com/wp-content/uploads/2023/04/Genesis-Market-scaled.jpg)

Operation Cookie Monster involved law enforcement agencies from the Australia, Canada, Germany, Poland, Sweden, the U.K and the U.S. Aside from the dismantling of the site, authorities arrested 120 people known to be regular users of the site and conducted 200 searches across a number of countries.

Genesis offered criminals a variety of stolen data, including [session cookies](https://www.sentinelone.com/blog/session-cookies-keychains-ssh-keys-and-more-7-kinds-of-data-malware-steals-from-macos-users/) (hence the operation name) and other metadata criminals could use to access victim’s personal and business accounts even when those were protected by [MFA](https://www.sentinelone.com/blog/has-mfa-failed-us-how-authentication-is-only-one-part-of-the-solution/).

The DoJ said that credentials and other data found on the site included those belonging to victims associated with the White House, Department of State, Justice Department, the IRS, the Department of Energy, the U.S. Postal Service, NASA, and the Department of Defense.

A list of compromised victims has been provided to the [Have I Been Pawned (HIBP)](https://haveibeenpwned.com) website. Concerned readers can check with HIBP to see if their credentials have appeared in various data breaches including Operation Cookie Monster.

The seizure of Genesis follow last month’s shuttering of [BreachForums](https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-12-4/) and represents a significant step forward in thwarting cybercrime and bringing to justice criminals who make use of [such services](https://www.sentinelone.com/blog/more-evil-markets-how-its-never-been-easier-to-buy-initial-access-to-compromised-networks/).

## Unpatched Windows | Millions of Endpoints Vulnerable to CISA KEVs

If the first rule of cybersecurity is “Patch early, and patch often”, then it seems the owners of millions of internet-facing endpoints have yet to hear it. Researchers this week [said](https://www.rezilion.com/blog/get-to-know-kev-in-our-new-research-report/) almost 900 known exploitable vulnerabilities (KEVs) [catalogued](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) by CISA over the last decade remain unpatched on around 15 million services today.

According to the research, around 3.5 million [Windows hosts](https://www.sentinelone.com/blog/why-your-operating-system-isnt-your-cybersecurity-friend/) reachable from the public internet are vulnerable to one or more of 137 CVEs in CISA’s KEV. 4.5 million endpoints of the 15 million total are vulnerable to KEVs discovered between 2010 and 2020. There are almost 200,000 exposed hosts that remain vulnerable to CVE-2014-0160, *aka* Heartbleed, disclosed nearly ten years ago. Of the more recent bugs such as [ProxyShell](https://www.sentinelone.com/blog/enterprise-security-essentials-top-15-most-routinely-exploited-vulnerabilities-2022/) and [ProxyLogon](https://www.sentinelone.com/blog/sentinelone-and-hafnium-microsoft-exchange-0-days/), both of which received a deluge of media attention in 2021, there remain 14.5K and 4.9K unpatched machines exposed to the internet.

Using data from [Greynoise](https://www.greynoise.io/), the researchers established that the Confluence bug CVE-2022-26134 was the most exploited, with over 800 exploitation attempts in the past month alone. The last 30 days prior to the report also showed 66 exploitation attempts of [Log4Shell](https://www.sentinelone.com/lp/log4j-log4shell-cve-2021-44228-staying-secure/).

![](https://www.sentinelone.com/wp-content/uploads/2023/04/greynoise.jpeg)

Source: Rezilion

Organizations can have multiple dependencies that make patching complex. However, the researchers report that Microsoft Windows, Internet Explorer, Microsoft Office, and Win32k along with Adobe Flash Player account for a quarter of CISA’s Known Exploited Vulnerabilities catalog. Therefore, it is advisable to patch these as a priority and/or reduce dependencies on these services where practicable.

## SmoothOperator Keeps Calling | Backdoors Target Cryptocurrency Companies

Details about targets and payloads are still emerging in the wake of last week’s supply chain attack on 3CX, dubbed [SmoothOperator](https://www.sentinelone.com/blog/smoothoperator-ongoing-campaign-trojanizes-3cx-software-in-software-supply-chain-attack/) and widely attributed to North Korean aligned threat actor [Lazarus](https://www.sentinelone.com/blog/lazarus-operation-interception-targets-macos-users-dreaming-of-jobs-in-crypto/). However, [researchers](https://securelist.com/gopuram-backdoor-deployed-through-3cx-supply-chain-attack/109344/) this week linked the campaign to a known backdoor dubbed “Gopuram”, used in attacks against cryptocurrency companies.

Gopuram was seen in an attack associated with [AppleJeus](https://www.sentinelone.com/blog/four-distinct-families-of-lazarus-malware-target-apples-macos-platform/) as long ago as 2020, but a spike in Gopuram infections had been observed in the weeks just prior to disclosure of the 3CX compromise. These compromises subsequently turned out to be related to the SmoothOperator campaign and targeted cryptocurrency companies.

![](https://www.sentinelone.com/wp-content/uploads/2023/04/gopuram-backdoor.jpg)

The Gopuram backdoor reaches out to a C2 server and requests tasking from the operator. Available commands include:

|  |  |
| --- | --- |
| **Command** | **Description** |
| Ping | Pings a host specified in the argument. |
| Connect | Connects to a given host via a socket and waits for the server to send data. |
| Registry | Manipulates registry (lists, adds, deletes and exports keys). |
| Service | Manipulates (creates, lists, starts, stops and deletes) services. |
| Timestomp | Performs timestomping on files. |
| Inject | Performs payload injections through syscalls via mapping a shellcode to a remote process and creating a remote thread. |
| KDU | Kernel Driver Utility that allows an attacker to bypass driver signature enforcement. |
| Update | Encrypts a provided payload and writes it to the C:\Windows\System32\config\TxR\.TxR.0.regtrans-ms file. |
| Net | Partially implements features of the net command: management of users, groups, sessions and network shares. |

The researchers identified the following additional [indicators of compromise](https://www.sentinelone.com/cybersecurity-101/what-are-indicators-of-compromise-iocs-a-comprehensive-guide/):

```
SHA1
011660842c3299e14a6ee7122494b9c78d448388
1b204f5969eb2ec9326f27244545d1f56547b14e
c8c21c8a5d86c57650a887bf798ae83095a40e97

FILE PATHS
C:\Windows\System32\config\TxR\.TxR.0.regtrans-ms
C:\Windows\system32\catroot2\edb.chk.log
```

Security teams are advised to conduct additional...