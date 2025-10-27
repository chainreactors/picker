---
title: Hackers Steal Over $55 Million in Mexican Financial Fraud
url: https://buaq.net/go-171864.html
source: unSafe.sh - 不安全
date: 2023-07-13
fetch_date: 2025-10-04T11:53:03.066168
---

# Hackers Steal Over $55 Million in Mexican Financial Fraud

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

![](https://8aqnet.cdn.bcebos.com/8b7dae59889e35305f050dba5fc7aedd.jpg)

Hackers Steal Over $55 Million in Mexican Financial Fraud

In May 2023, hackers carried out a widespread phishing campaign, targeting both individuals and
*2023-7-12 19:32:58
Author: [perception-point.io(查看原文)](/jump-171864.htm)
阅读量:18
收藏*

---

In May 2023, hackers carried out a widespread phishing campaign, targeting both individuals and organizations in Mexico. Researchers from [Perception Point](https://perception-point.io), a leading cybersecurity company based in Israel, found that the operation began as early as 2021. It is estimated that over  the past two years the threat actors have defrauded more than 4,000 victims out of over $55 million.

This attack, dubbed “Manipulated Caiman” by Perception Point researchers due to its Latin American origin and mention of “Loader Manipulado” in the script of the attack, starts off as a seemingly standard phishing scam, in which the target receives an email with a supposed tax receipt attached.

![](https://lh3.googleusercontent.com/Ye9K5mBkk0ZTX2Fot_z2LtR2WE3a3AUbV0E1gUXOQwFwS6d5WUB2uQ1PNfyFaJZjrcsp7GKG6uNCcKk7JGsKRd88nKrQiwThNj1eW20daomd-J7U4ygP7SiDweykdMhFq3O-EHRiaEkmOCghRwvl4Hc)

The target is lured into clicking on the attachment. By using the [CFDI](https://tipalti.com/cfdi-compliance/) electronic invoice format, mandated in Mexico and used in other parts of Latin America, the threat actor effectively localizes and legitimizes the attack for the user. When the target clicks on the attachment, they inadvertently download malware, giving the attacker unauthorized access to their computer and free rein to execute the remainder of the attack flow.

However, when a user with an IP outside of Mexico attempts to access the file, they are redirected to a legitimate website and the attack is terminated. The attacker employs a form of geofencing in the attack to evade detection and also ensure that only the desired targets are compromised. This method can make it extremely difficult for even the most advanced threat detection solutions to identify and catch.

After the target has clicked on the attachment, they effectively install a multi-layered script, containing executables, which monitors the websites that the user visits. It compares accessed URLs to its catalog of targeted banking sites. The script injects a command into the user’s browser that will retrieve the user’s cookie value from banking sites and send it to the threat actor’s C2 server.

To further complicate detection, the attacker hosts the payload on a trusted WordPress-based site. This deters detection, as the compromised site likely has a high reputation, unlike typical phishing sites.

What comes next is what the attacker hopes is the end to a successful phishing excursion: the user enters their bank credentials, only for the attacker to steal them along with the victim’s money. The script downloaded from the initial phishing email fetches the next-stage payload and establishes persistence using AutoIT Downloader and InfoStealer techniques. This script not only steals sensitive Outlook and Chrome credentials from infected machines but also exfiltrates the stolen data by sending a carefully crafted POST request to specific URLs.

## Even a Caiman Can’t Hide Forever

One question remains: How did this threat actor remain largely undetected and operational for so long?

Perception Point researchers discovered that the C2 server had a [Django REST framework](https://www.django-rest-framework.org/) hosted on it, revealing an open API URL that contained a range of logs and data tables. They also found a control panel login page present in all the C2 servers identified (four so far).

![](https://lh4.googleusercontent.com/ydqmh9tiDJFl6ERT2In1LS-fRpmksmxSx0iTCOxq2t3LAn2egtMfqNps5rq0lB2oggHXgxHMpJ8RebkRzvpcSVjmbLLx5Y-56EiT9dYQPlF4VhzlRkPiHcXZZB57adhwHI6vDrg9I_ChL5v3D3ZmGv4)

The attacker uses the panel for efficient email distribution and to control the content and dissemination of their phishing messages. It enables the attacker to manipulate sender names, subjects, email content, and even select SMTPs for widespread campaigns, like the one distributed in May 2023.

However, the actual act of spamming is delegated to a botnet, allowing for mass distribution and amplifying the impact of their malicious campaigns.

Through further research, a pattern emerged: the majority of the IP addresses involved in these attacks were traced back to private IP addresses predominantly located in Mexico. This crucial finding led to the realization that in the event of a successful infection, the attacker downloads and stores tools like Ascan and other malware on the victim’s computer, ensuring persistence and providing an avenue for continued unauthorized access. In layman’s terms: ***the attacker uses victims’ computers to distribute the attack.***

In addition to the discovery of the distribution method, the open API URL contained tables that held crucial data, including the victims’ account balances, dates of infection, latest transactions, and, in some instances, screenshots of their compromised bank accounts.

By aggregating and analyzing data from multiple C2 servers, researchers found that the number of victims identified surpassed 4,000. Based on the balance amounts in the compromised accounts, the analysts estimate a potential theft of over $55 million.

The extent of this attack is further underscored by the timeline of the infections. The earliest sign of infection can be traced back to 2021, implying a protracted campaign that has remained under the radar for nearly two years. This longevity speaks to the attacker’s ability to evade detection, yet also begs the question of how they could have been so careless with their OpSec decisions.

While there is no easy answer why the threat actor slacked on operations security, Perception Point’s researchers believe that it has to do with a [lack of repercussions for cybercrime in Mexico and the region](https://iclg.com/practice-areas/cybersecurity-laws-and-regulations/mexico).

Thank you to [Igal Lytzki](https://twitter.com/0xToxin), Perception Point Threat Analyst & IR Team Lead, [@Merlax](https://twitter.com/Merlax_), and others for their research on subject.

文章来源: https://perception-point.io/blog/hackers-steal-over-55-million-in-mexican-financial-fraud/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)