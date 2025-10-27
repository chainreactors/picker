---
title: Estée Lauder targeted by Cl0p and BlackCat ransomware groups
url: https://buaq.net/go-172688.html
source: unSafe.sh - 不安全
date: 2023-07-22
fetch_date: 2025-10-04T11:52:24.909699
---

# Estée Lauder targeted by Cl0p and BlackCat ransomware groups

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

Estée Lauder targeted by Cl0p and BlackCat ransomware groups

Estée Lauder is currently at the heart of a compromise storm, revealing
*2023-7-21 22:0:0
Author: [www.malwarebytes.com(查看原文)](/jump-172688.htm)
阅读量:15
收藏*

---

Estée Lauder is currently at the [heart of a compromise storm](https://www.bleepingcomputer.com/news/security/est-e-lauder-beauty-giant-breached-by-two-ransomware-gangs/), revealing a major security issue via a Security Exchange Commission (SEC) filing on Tuesday.

Although no detailed explanation of what has taken place is given, there is confirmation that an attack allowed access to some systems and involved potential data exfiltration. Meanwhile, two ransomware groups are taking credit for compromises unrelated to one another. Is one of the compromises the attack mentioned in the filing? It’s worth mentioning here that Estée Lauder does not name either ransomware group. With this in mind, the relevant section from the [filing reads as follows](https://otp.tools.investis.com/clients/us/estee_lauder4/SEC/sec-show.aspx?Type=page&FilingId=16797601-5240-9157&CIK=0001001250&Index=20000):

> The Estée Lauder Companies Inc. (NYSE: EL) has identified a cybersecurity incident, which involves an unauthorized third party that has gained access to some of the Company’s systems.  After becoming aware of the incident, the Company proactively took down some of its systems and promptly began an investigation with the assistance of leading third-party cybersecurity experts. The Company is also coordinating with law enforcement.  Based on the current status of the investigation, the Company believes the unauthorized party obtained some data from its systems, and the Company is working to understand the nature and scope of that data.
>
> The Company is implementing measures to secure its business operations and will continue taking additional steps as appropriate. During this ongoing incident, the Company is focused on remediation, including efforts to restore impacted systems and services. The incident has caused, and is expected to continue to cause, disruption to parts of the Company’s business operations.

Bleeping Computer notes that the ALPHV/BlackCat and Cl0p groups are claiming responsibility for the two unrelated ransomware compromises specifically. Worse, both ransomware groups have what they claim to be Estée Lauder data up for grabs on their leak portals.

If you’re unfamiliar with such sites, they’re places where ransomware groups store stolen data. The compromised organisation is then threatened with the data being made public, traded, or sold off to the highest bidder unless a ransom is paid. This is a common tactic in so-called "double extortion" ransomware, where the encrypting of devices is merely the first step to extracting money.

The Cl0p group claims to have somewhere in the region of 131GB of data to hand. Meanwhile BlackCat is complaining of the lack of communication from Estée Lauder, sending multiple emails but receiving no replies. It also claims to still have network access despite various attempts to secure the network.

Supposedly, the information taken could “impact customers, employees, and suppliers”. There are no further details on the contents at this time. Regular readers will know that these attacks typically target confidential information, company secrets, personal data, payroll, and identity scans. The attackers could be bluffing, or it really could be as bad as they claim. We’ll have to wait and see.

The Cl0p compromise is said to have made use of a [MOVEit Transfer vulnerability](https://www.malwarebytes.com/blog/news/2023/06/update-now-moveit-transfer-vulnerability-actively-exploited) to gain access to the target systems. Both Cl0p and BlackCat tend to feature heavily in our [ransomware review posts](https://www.malwarebytes.com/blog/threat-intelligence/2023/07/ransomware-review-july-2023). In our June post, Cl0p was the most active group around with BlackCat falling suspiciously quiet. Perhaps it was focusing on heavy-hitter attacks such as this the whole time.

## How to avoid ransomware

* **Block common forms of entry**. Create a plan for [patching vulnerabilities](https://www.malwarebytes.com/business/vulnerability-patch-management) in internet-facing systems quickly; disable or [harden remote access](https://www.malwarebytes.com/blog/news/2022/03/blunting-rdp-brute-force-attacks-with-rate-limiting) like RDP and VPNs; use [endpoint security software](https://www.malwarebytes.com/business/edr) that can detect exploits and malware used to deliver ransomware.
* **Detect intrusions**. Make it harder for intruders to operate inside your organization by segmenting networks and assigning access rights prudently. Use [EDR](https://www.malwarebytes.com/business/edr) or [MDR](https://www.malwarebytes.com/business/managed-detection-and-response) to detect unusual activity before an attack occurs.
* **Stop malicious encryption**. Deploy Endpoint Detection and Response software like [Malwarebytes EDR](https://www.malwarebytes.com/business/edr) that uses multiple different detection techniques to identify ransomware, and ransomware rollback to restore damaged system files.
* **Create offsite, offline backups**. Keep backups offsite and offline, beyond the reach of attackers. Test them regularly to make sure you can restore essential business functions swiftly.
* **Don’t get attacked twice.** Once you've isolated the outbreak and stopped the first attack, you must remove every trace of the attackers, their malware, their tools, and their methods of entry, to avoid being attacked again.

---

文章来源: https://www.malwarebytes.com/blog/news/2023/07/este-lauder-targeted-by-cl0p-and-blackcat-ransomware-groups
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)