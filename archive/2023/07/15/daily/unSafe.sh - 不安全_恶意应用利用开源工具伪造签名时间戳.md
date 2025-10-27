---
title: 恶意应用利用开源工具伪造签名时间戳
url: https://buaq.net/go-172090.html
source: unSafe.sh - 不安全
date: 2023-07-15
fetch_date: 2025-10-04T11:51:25.902316
---

# 恶意应用利用开源工具伪造签名时间戳

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

恶意应用利用开源工具伪造签名时间戳

思科 Talos 安全团队发表了两篇博文，披露恶意应用在利用开源工具伪造签名时间戳，而这些恶意应用主要针对中文用户。从 Windows 10 v1607 开始，微软更新了驱动签名政策，不再
*2023-7-14 19:33:56
Author: [www.solidot.org(查看原文)](/jump-172090.htm)
阅读量:14
收藏*

---

思科 Talos 安全团队发表了两篇博文，披露恶意应用在利用开源工具伪造签名时间戳，而这些恶意应用主要针对中文用户。从 Windows 10 v1607 开始，微软更新了驱动签名政策，不再允许未递交到 Developer Portal 签名的新内核模式驱动，但为了保持向后兼容，使用 2015 年 7 月 29 日之前颁发的最终实体证书签名的驱动程序将继续允许将链式链与受支持的交叉签名 CA 进行关联。这个例外制造了一个漏洞，允许新编译的驱动程序使用 2015 年 7 月 29 日之前颁发或过期的未撤销证书签名。有两个开源工具 HookSignTool 和 FuckCertVerifyTimeValidity 都允许伪造签名日期。主要针对中文用户的恶意程序利用这些开源工具使用窃取的证书进行签名，其中之一是 RedDriver。RedDriver 是一种基于驱动程序的浏览器劫持程序，使用 Windows Filtering Platform (WFP) 拦截浏览器流量，它利用 HookSignTool 伪造签名时间戳，它有一个硬编码的中文浏览器进程名单，针对的明显是中文用户，名单中包含了中国流行的浏览器，如 360 浏览器和 QQ 浏览器。

https://blog.talosintelligence.com/old-certificate-new-signature/

文章来源: https://www.solidot.org/story?sid=75516
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)