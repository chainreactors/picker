---
title: Tool Release: Code Query (cq)
url: https://buaq.net/go-165948.html
source: unSafe.sh - 不安全
date: 2023-05-27
fetch_date: 2025-10-04T11:37:05.670709
---

# Tool Release: Code Query (cq)

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

Tool Release: Code Query (cq)

Code Query is a new, open source universal code security scanning tool.
*2023-5-26 23:14:16
Author: [research.nccgroup.com(查看原文)](/jump-165948.htm)
阅读量:29
收藏*

---

Code Query is a new, open source universal code security scanning tool.

CQ scans code for security vulnerabilities and other items of interest to security-focussed code reviewers. It outputs text files containing references to issues found, into an output directory. These output files can then be reviewed, filtered by unix command line tools such as grep, or used as a means to ‘jump’ into the codebase at the specified file:line reference.

One popular mode of use is to consider the output files as a ‘todo’ list, deleting references as they are reviewed and either considered false positives, or copying the references into some report file to either review in detail or provide the basis for a bug report.

The tool is extremely basic, largely manual, and assumes deep knowledge of application security vulnerabilities and code review. It does, however, have the advantages of being relatively fast and reliable, and working even when only partial code is available.

CQ is intended to be used in a security code review context by human experts. It is not intended for use in automated scenarios, although it might be applied in that context.

The CQ project is located at: <https://github.com/nccgroup/cq>

### Here are some related articles you may find interesting

[#### CowCloud](https://research.nccgroup.com/2023/05/25/cowcloud/ "CowCloud")

A common challenge technical teams (e.g. penetration testers) face is centralized deployment and pipelining execution of security tools. It is possible that at some point you have thought about customising several tools, buying their commercial licenses, and allowing a number of people to run the tools from AWS. The problem…

[#### OffensiveCon 2023 – Exploit Engineering – Attacking the Linux Kernel](https://research.nccgroup.com/2023/05/23/offensivecon-2023-exploit-engineering-attacking-the-linux-kernel/ "OffensiveCon 2023 – Exploit Engineering – Attacking the Linux Kernel")

Cedric Halbronn and Alex Plaskett presented at OffensiveCon on the 19th of May 2023 on Exploit Engineering – Attacking the Linux kernel. Slides The slides for the talk can be downloaded below: libslub libslub can be downloaded from here. Abstract The abstract for the talk was as follows: Over the…

[#### Tool Release: Code Credential Scanner (ccs)](https://research.nccgroup.com/2023/05/23/tool-release-code-credential-scanner-ccs/ "Tool Release: Code Credential Scanner (ccs)")

Code Credential Scanner is a new open source tool designed to detect hardcoded credentials, or credentials present in configuration files within a repository. These represent a serious security issue, and can be extremely hard to detect and manage. The tool is intended to be used directly by dev teams in…

### View articles by category

## Call us before you need us.

Our experts will help you.

[Get in touch](https://www.nccgroup.com/uk/contact-us/ "Get in touch")

文章来源: https://research.nccgroup.com/2023/05/26/tool-release-code-query-cq/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)