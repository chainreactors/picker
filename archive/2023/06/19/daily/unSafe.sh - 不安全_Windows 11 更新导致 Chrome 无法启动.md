---
title: Windows 11 更新导致 Chrome 无法启动
url: https://buaq.net/go-169247.html
source: unSafe.sh - 不安全
date: 2023-06-19
fetch_date: 2025-10-04T11:44:52.888985
---

# Windows 11 更新导致 Chrome 无法启动

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

Windows 11 更新导致 Chrome 无法启动

微软本周二例行安全更新释出的累积补丁 Windows 11 22H2 KB5027231 被发现会导致 Chrome 浏览器与用户安装的安全软件发生冲突而无法启动。与 Chrome 发生冲
*2023-6-18 17:6:29
Author: [www.solidot.org(查看原文)](/jump-169247.htm)
阅读量:14
收藏*

---

微软本周二例行安全更新释出的累积补丁 Windows 11 22H2 KB5027231 被发现会导致 Chrome 浏览器与用户安装的安全软件发生冲突而无法启动。与 Chrome 发生冲突的安全软件包括 Malwarebytes、思科的 Secure Endpoint 和 WatchGuard 的 Endpoint Security 等。用户点击 Chrome 图标之后浏览器进程在运行，但由于冲突浏览器无法完全启动界面无法加载。一位系统管理员称，他们在数千台计算机上部署了 Secure Endpoint 8.1.7，早上收到大量报告称在尝试打开 Chrome 后浏览器没有显示在界面上。通过试错，杀死 Secure Endpoint 进程或卸载 Secure Endpoint 后浏览器能正常启动。WatchGuard 和 Malwarebytes 都报告了类似的现象。

https://support.malwarebytes.com/hc/en-us/articles/17571529651475

文章来源: https://www.solidot.org/story?sid=75275
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)