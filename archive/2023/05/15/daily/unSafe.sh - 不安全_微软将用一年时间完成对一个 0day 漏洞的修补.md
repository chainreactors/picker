---
title: 微软将用一年时间完成对一个 0day 漏洞的修补
url: https://buaq.net/go-163321.html
source: unSafe.sh - 不安全
date: 2023-05-15
fetch_date: 2025-10-04T11:36:41.997301
---

# 微软将用一年时间完成对一个 0day 漏洞的修补

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

微软将用一年时间完成对一个 0day 漏洞的修补

微软本周释出了补丁修复了一个被 BlackLotus bootkit 利用的 Secure Boot 绕过漏洞。微软在今年 1 月释出补丁修复了编号为 CVE-2022-21894 的漏洞
*2023-5-14 23:52:10
Author: [www.solidot.org(查看原文)](/jump-163321.htm)
阅读量:48
收藏*

---

微软本周释出了补丁修复了一个被 BlackLotus bootkit 利用的 Secure Boot 绕过漏洞。微软在今年 1 月释出补丁修复了编号为 CVE-2022-21894 的漏洞，但该补丁并不完整，攻击者很快找到了绕过方法。本周释出的补丁修复了新漏洞 CVE-2023-24932。微软称能物理访问系统或拥有管理员权限的攻击者可利用该漏洞。但新补丁不会默认启用，因为它涉及到修改 Windows 启动管理器，一旦更改将是无法撤销的，它会导致现有的启动媒介无法启动。为了避免导致客户的系统无法启动，补丁将会分三个阶段应用，直到 2024 年第一季度补丁才会默认启用，届时旧的启动媒介将会无法使用。

https://arstechnica.com/information-technology/2023/05/microsoft-patches-secure-boot-flaw-but-wont-enable-fix-by-default-until-early-2024/

文章来源: https://www.solidot.org/story?sid=74957
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)