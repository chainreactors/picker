---
title: Six Malicious Python Packages in the PyPI Targeting Windows Users
url: https://buaq.net/go-171761.html
source: unSafe.sh - 不安全
date: 2023-07-12
fetch_date: 2025-10-04T11:51:31.511305
---

# Six Malicious Python Packages in the PyPI Targeting Windows Users

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

![](https://8aqnet.cdn.bcebos.com/64ae168726c5353a2c1017bd97a400eb.jpg)

Six Malicious Python Packages in the PyPI Targeting Windows Users

This post is also available i
*2023-7-11 21:0:57
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-171761.htm)
阅读量:32
收藏*

---

![A pictorial representation of malicious PyPI packages targeting Windows users](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/07/Cloud-21-illustration_black.png)

This post is also available in:
[日本語 (Japanese)](https://unit42.paloaltonetworks.jp/malicious-packages-in-pypi/)

## Executive Summary

In March 2023, Unit 42 researchers discovered six malicious packages on the Python Package Index (PyPI) package manager. The malicious packages were intended to steal Windows users’ application credentials, personal data and tracking information for their crypto wallets. The attack was an attempted imitation of the attack group W4SP, which had previously launched several supply chain attacks using malicious packages.

We will discuss the ease with which threat actors can use malicious packages to release malicious code in an open-source ecosystem. The behavior we observed is not an organized campaign planned by an attack group, but most likely an imitator who read technical reports of previous campaigns to execute their own attack. We will walk through a technical analysis of the malicious code and unravel what the threat actor tried to achieve in the attack.

We will describe the indicators used by Palo Alto Networks Prisma Cloud modules that identified the malicious packages discussed here. Palo Alto Networks customers receive protections from open-source packages containing malicious code via Prisma Cloud.

| **Related Unit 42 Topics** | [**Cloud**](https://unit42.paloaltonetworks.com/category/cloud/), **[Python](https://unit42.paloaltonetworks.com/tag/Python/)**, **[Open Source](https://unit42.paloaltonetworks.com/tag/open-source/)** |
| --- | --- |

## Table of Contents

[Overview](#post-129019-_by1wt6yuxz57)

## Overview

Malicious packages are software components that were intentionally designed to cause harm to computer systems or the data they process. Such packages can be distributed through various means, including phishing emails, compromised websites or even legitimate software repositories.

Malicious packages can have far-reaching consequences, from surreptitiously pilfering sensitive data to causing system disruptions and even assuming control over entire systems. Moreover, these nefarious packages possess the ability to spread to other interconnected systems, instigating widespread damage and impeding productivity. Thus, it is important to exercise utmost caution when engaging in software downloads and installations, especially when the source is unfamiliar or untrusted.

By remaining vigilant and discerning, users can safeguard their systems and prevent potential harm from threat actors infiltrating their technological environment.

## New Malicious Packages Discovered in PyPI

In March 2023, Prisma Cloud researchers discovered six malicious packages on the [PyPI package manager](https://pypi.org/) targeting Windows users. The malicious packages were intended to steal application credentials, personal data and cryptocurrency wallet information.

Our Prisma Cloud engine, designed to detect malicious PyPI packages, identified several packages with suspicious attributes that were uploaded within a short time frame:

* The packages lacked an associated GitHub repository, which is commonly found with legitimate packages. This could indicate a desire to hide the code from view. This, coupled with a limited number of downloads, further raised our suspicions.
* When executed, the packages performed malicious actions such as collecting sensitive data and sending it to third-party URLs.
* The packages contained a malicious code pattern (as will be demonstrated later), which was detected by our engine.
* Because the package authors were newly created, had only uploaded one package, and did not provide supporting information such as links to other projects or to any repository, they were not considered reputable.
* Finally, the usernames of the packages’ author(s) were created within minutes of each other, following a distinctive pattern (e.g., Anne1337, Richard1337). Each of these usernames had uploaded only a single package.

The second stage of the attack was similar to previous attacks we have seen by the [W4SP](https://thehackernews.com/2022/11/w4sp-stealer-constantly-targeting.html) attack group. This group specializes in exploiting vulnerabilities in the open-source ecosystem, targeting organizations and spreading malware. Their primary goal is to gain unauthorized access to sensitive information, such as user credentials and financial data. They often use automated tools to scan for vulnerabilities and attempt to exploit them. In addition to traditional attacks, W4SP attackers were also seen executing supply chain attacks.

## Findings

Prisma Cloud engine detected the packages that were marked as potentially containing malicious code. Each package contained a link to a suspicious remote URL, trying to download contents after having been uploaded individually by a single user.

The users for each uploaded package, whose usernames were created just before the upload, didn’t have any history of previously uploading packages. Each package reached hundreds of downloads, until they and the fraudulent user accounts that uploaded them were removed by PyPI due to our research team reporting the abuse.

We analyzed the code and tried to track down the package authors. We discovered a pattern in every package author’s username where they used “1337” as a suffix, which indicates that some automatic process created those users, as shown in Table 1. Figure 1 shows an author page for one of these usernames.

|  |  |  |  |
| --- | --- | --- | --- |
| **Package Name** | **Author** | **Malicious Link** | **Number of Downloads** |
| ligitgays | Anne1337 | hxxps://paste.bingner[.]com/paste/o27gb/raw | 191 |
| xboxredeemer | Richard1337 | hxps://paste.bingner[.]com/paste/47rpu/raw | 160 |
| syntax-init | Debbie1337 | hxxps://paste.bingner[.]com/paste/q77t3/raw | 140 |
| xboxlivepy | Christopher1337 | hxxps://paste.bingner[.]com/paste/jr7ow/raw | 153 |
| Ligitkidss | Sara1337 | hxxps://paste.bingner[.]com/paste/9mzzs/raw | 158 |
| tls-python | Kevin1337 | hxxps://paste.bingner[.]com/paste/97vnn/raw | 240 |

*Table 1. Malicious package findings.*

![Image 1 is a screenshot of an author page on PyPI. The user has not uploaded any projects. The name of the user is Travis Elliott, they joined March 13, 2023, and their user name is Richard1337.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/07/word-image-129019-1-1.png)

Figure 1. An author page on PyPI.

## **The Attack: Custom Package Entry Point**

The attack was similar to previous attacks we have seen by the W4SP attack group, which was covered in detail in the Bleeping Computer article, “[Devs targeted by W4SP Stealer malware in malicious PyPi packages](https://www.bleepingcomputer.com/news/security/devs-targeted-by-w4sp-stealer-malware-in-malicious-pypi-packages/).” These similarities led us to believe this was a copycat attack.

There were aspects of this case that were less complex than we would expect for a true W4SP attack, for example:

* There was no targeting of any organization.
* The malicious packages did not use typosquatting for common popular packages, as expected for W4SP attacks.
* The second phase of the attack was not encrypted. In the true attacks from W4S...