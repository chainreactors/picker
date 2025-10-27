---
title: The Good, the Bad and the Ugly in Cybersecurity – Week 7
url: https://buaq.net/go-149895.html
source: unSafe.sh - 不安全
date: 2023-02-18
fetch_date: 2025-10-04T07:20:09.889481
---

# The Good, the Bad and the Ugly in Cybersecurity – Week 7

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

![](https://8aqnet.cdn.bcebos.com/33f87e150a56dc45811192262694628e.jpg)

The Good, the Bad and the Ugly in Cybersecurity – Week 7

The GoodVladislav Klyushin, the owner of Russian cybersecurity firm M-13, was this week convicted
*2023-2-17 22:0:45
Author: [www.sentinelone.com(查看原文)](/jump-149895.htm)
阅读量:36
收藏*

---

## The Good

Vladislav Klyushin, the owner of Russian cybersecurity firm [M-13](https://en.m13.ru/it-security), was this week convicted in a U.S. court on charges of wire fraud, securities fraud, and obtaining unauthorized access to computers. Klyushin, along with four co-conspirators who remain at large, is believed to have netted around $90 million through securities trades based on information stolen from U.S. computer networks.

According to the [DoJ](https://www.justice.gov/usao-ma/pr/russian-businessman-found-guilty-90-million-hack-trade-conspiracy), Klyushin used hacking techniques similar to those offered by his cybersecurity company to repeatedly hack into U.S. computer networks and steal confidential earnings reports ahead of their release. He then used the information obtained to trade illegally in the shares of hundreds of publicly traded companies.

![](https://www.sentinelone.com/wp-content/uploads/2023/02/wall-street-scaled.jpg)

In a trial that lasted 10 days, the court in Boston heard how Klyushin and his co-conspirators stole login information of employees at two U.S.-based filing agents used by publicly-traded companies to file their quarterly and annual earning reports to the SEC. They used proxy networks outside of Russia to conceal the true origin of their activities and stole filings from hundreds of companies, including Tesla, Roku and Snap. Much of the stolen data was downloaded through a computer server located in downtown Boston. Klyushin used the stolen information to trade in brokerage accounts held in his own name and the names of others.

The charges of securities fraud and wire fraud alone each provide for a sentence of up to 20 years in prison. Klyushin, who was arrested in Switzerland in 2021 and subsequently extradited to the U.S., is due to be sentenced on May 4th.

## The Bad

Threat actors have been leveraging the cloud services of Dropbox, Microsoft Azure, Microsoft 365 Mail, and Google Firebase in what appears to be espionage-related activity against telecommunications companies in the Middle East.

A new [report](https://s1.ai/WIP26) from SentinelLabs reveals that a cluster of threat activity targeting telcos used malicious WhatsApp messages to infect employees with malware hosted on Dropbox. Backdoors leveraging Microsoft 365 Mail and Google Firebase instances as C2 servers were then deployed on victims’ machines.

The backdoors masquerade as utility software, such as a PDF editor or browser, and use filenames, application icons, and digital signatures of known software vendors. Their capabilities include reconnaissance, privilege escalation, staging of additional malware, and data exfiltration. [PowerShell](https://www.sentinelone.com/cybersecurity-101/windows-powershell/) commands were used to exfiltrate browser data and reconnaissance information to Microsoft Azure instances.

![WIP26: Use of Cloud infrastructure](https://www.sentinelone.com/wp-content/uploads/2023/02/WIP26_17.jpg)

The use of public Cloud infrastructure for malware hosting, data exfiltration, and C2 purposes aims at making malicious traffic look legitimate. This gives attackers the opportunity to conduct their activities unnoticed, the SentinelLabs’ researchers say.

The cluster of activity at present remains unattributed to any known group and is tracked by SentinelLabs under the moniker “WIP26”. However, the threat actor behind the activity appeared to have made some OPSEC (operational security) errors. The researchers noted that a JSON file on a Google Firebase C2 server was publicly accessible and provided further insights into the WIP26 activity.

## The Ugly

CISA is this week warning of four critical bugs in Microsoft and Apple software that may be under active exploitation and giving federal agencies 21 days to ensure their devices are patched.

A patch for a WebKit [zero-day](https://www.sentinelone.com/cybersecurity-101/zero-day-vulnerabilities-attacks/) tracked as [CVE-2023-23529](https://support.apple.com/en-us/HT213635) was released by Apple on Monday. The Cupertino outfit says that the bug allows maliciously crafted web content to cause arbitrary code execution and that it is aware of a report that the vulnerability may have been exploited in the wild. The WebKit bug affects macOS, iOS and iPadOS systems.

> 4 🆕 [#CVEs](https://twitter.com/hashtag/CVEs?src=hash&ref_src=twsrc%5Etfw) have been added to [@CISAgov](https://twitter.com/CISAgov?ref_src=twsrc%5Etfw)’s Known Exploited Vulnerabilities Catalog. Visit <https://t.co/myxOwap1Tf> and mitigate to protect your organization from [#cyberattacks](https://twitter.com/hashtag/cyberattacks?src=hash&ref_src=twsrc%5Etfw)❗[#CVE](https://twitter.com/hashtag/CVE?src=hash&ref_src=twsrc%5Etfw) [#Cybersecurity](https://twitter.com/hashtag/Cybersecurity?src=hash&ref_src=twsrc%5Etfw) [#VulnerabilityManagement](https://twitter.com/hashtag/VulnerabilityManagement?src=hash&ref_src=twsrc%5Etfw) [pic.twitter.com/wY78WcyqQH](https://t.co/wY78WcyqQH)
>
> — CISA Cyber (@CISACyber) [February 14, 2023](https://twitter.com/CISACyber/status/1625585114510946304?ref_src=twsrc%5Etfw)

Tuesday saw Microsoft patch three bugs thought to be actively exploited, two of which could allow attackers to gain remote code execution. [CVE-2023-21823](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-21823) affects the Windows Graphics Component and, if successfully exploited, could allow an attacker to gain SYSTEM privileges. [CVE-2023-23376](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-23376) affects the Windows Common Log File System Driver and is an elevation of privileges vulnerability that requires no user interaction. Microsoft says the attack is of low complexity to carry out.

A third Microsoft bug patched this week, [CVE-2023-21715](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-21715), is a Microsoft [Office macro](https://www.sentinelone.com/labs/who-needs-macros-threat-actors-pivot-to-abusing-explorer-and-other-lolbins-via-windows-shortcuts/) policy bypass. Macro policies are intended to block untrusted or malicious files, but an attacker could use the bug to socially engineer a victim into downloading and opening a specially crafted file that could lead to a local attack on the victim’s computer.

CISA says bugs such as these are frequent attack vectors for malicious cyber actors and has given federal agencies until March 7 to patch affected systems. Enterprises would be well-advised to act somewhat faster than that.

文章来源: https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-7-4/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)