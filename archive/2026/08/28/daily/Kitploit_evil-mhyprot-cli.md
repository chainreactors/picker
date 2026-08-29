---
title: evil-mhyprot-cli
url: https://kitploit.com/en/tools/github/kkent030315/evil-mhyprot-cli
source: Kitploit
date: 2026-08-28
fetch_date: 2026-08-29T08:31:11.987891
---

# evil-mhyprot-cli

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

evil-mhyprot-cli — A PoC for Mhyprot2.sys vulnerable driver that allowing read/write memory in kernel/user via unprivileged user process. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/kkent030315/evil-mhyprot-cli

![](https://assets.kitploit.com/production/public/tools/53291/05ff6eefcfcb5aa433b967e7f355c5fbb5c003fbfa9e6bf449e1e5684c5f76d6-display-v1.webp)

[Privilege Escalation](/en/categories/privilege-escalation)[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Exploitation](/en/categories/exploitation)[Red Teaming](/en/categories/red-teaming)[Binary Exploitation](/en/categories/binary-exploitation)

![GitHub](/providers/github.png)kkent030315/evil-mhyprot-cli

# evil-mhyprot-cli

A PoC for Mhyprot2.sys vulnerable driver that allowing read/write memory in kernel/user via unprivileged user process.

[View Repository](https://github.com/kkent030315/evil-mhyprot-cli)

35669305 years ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

[Website](https://www.godeye.club/2021/05/20/001-disclosure-mhyprot.html)

![](https://assets.kitploit.com/production/public/readmes/53291/27ff152d7f4f5ae32f866605cd800d4dc64a4d41537dc9a44a58629d194e2cb5/bf31f25a4d8bca227e4977b2687bdd91c109228672dab6b1f8f54a3e7ea10d29-display-v1.webp)

![](https://img.shields.io/github/license/kkent030315/evil-mhyprot-cli?style=for-the-badge)
![](https://img.shields.io/github/last-commit/kkent030315/evil-mhyprot-cli?style=for-the-badge)
![](https://img.shields.io/codefactor/grade/github/kkent030315/evil-mhyprot-cli?style=for-the-badge)

![IMAGE](https://assets.kitploit.com/production/public/readmes/53291/05ff6eefcfcb5aa433b967e7f355c5fbb5c003fbfa9e6bf449e1e5684c5f76d6/3b0519697d6f98a4aad5f08b6aef1b92ca43b1e3e21194f0d04a42308894c60a-display-v1.webp)
![IMAGE](https://assets.kitploit.com/production/public/readmes/53291/a3022c467d249c5bee48fdc946039d91e552c7fb2c42c4de69aaea2b5d765a94/d7684ad6f9681807136e76546260c2f6ce5c58efa446e704a46af4a004ccb595-display-v1.webp)
![IMAGE](https://assets.kitploit.com/production/public/readmes/53291/f6a4e6973a9f4e1a3573c266745bab081acaa6bb3b14592a6ba6c960953fc149/ea741f60f1a3a0fa5fb9d202de96bad10522215d064992ede4142b04a70dc80d-display-v1.webp)

# evil-mhyprot-cli

A PoC for Mhyprot2.sys vulnerable driver that allowing read/write memory in kernel/user via unprivileged user process.

* [libmhyprot](https://github.com/kkent030315/libmhyprot)
* [Wiki](https://github.com/kkent030315/evil-mhyprot-cli/wiki)

# Overview

What we can do with this CLI is as follows:

* Read/Write any kernel memory with privilege of kernel from usermode
* Read/Write any user memory with privilege of kernel from usermode
* Enumerate a number of modules by specific process id
* Get system uptime
* Enumerate threads in specific process, result in allows us to reading `PETHREAD` structure in the kernel directly from CLI as well.
* Terminate specific process by process id with `ZwTerminateProcess` which called in the vulnerable driver context (ring-0).
* All operations are executed as kernel level privilege (ring-0) by the vulnerable driver

Also:

* Administrator privilege only needed if the service is not yet running
* Therefore we can execute commands above as the normal user (w/o administrator privilege)

# Requirements

* Any version of Windows x64 that the driver works on
* Administrator privilege **does not required** if the service already running

Tested on:

* Windows10 x64 1903
* Windows7 x64 6.1
* Windows8.1 x64 6.3

# Usage

root@kitploit:~

```
*.exe <target_process_name> -<options>
```

following options are available as of now:

* `t`
  + Perform Tests
* `d`
  + Print debug infos
* `s`
  + Print seedmap

# Latest

![IMAGE](https://assets.kitploit.com/production/public/readmes/53291/4d56b7ccfd042044e00e6a1fb5b9edf39846d86774b3c261195a1bc129043193/63ff697e17efe66c5858d224aa7074df505ba9024ed489428b751b41ae8df5aa-display-v1.webp)

[Download Tool](https://github.com/kkent030315/evil-mhyprot-cli)