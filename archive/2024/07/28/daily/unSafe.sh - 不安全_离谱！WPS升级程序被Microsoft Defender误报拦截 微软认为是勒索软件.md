---
title: 离谱！WPS升级程序被Microsoft Defender误报拦截 微软认为是勒索软件
url: https://buaq.net/go-252820.html
source: unSafe.sh - 不安全
date: 2024-07-28
fetch_date: 2025-10-06T17:41:08.382154
---

# 离谱！WPS升级程序被Microsoft Defender误报拦截 微软认为是勒索软件

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

离谱！WPS升级程序被Microsoft Defender误报拦截 微软认为是勒索软件

*2024-7-27 22:12:37
Author: [www.landiannews.com(查看原文)](/jump-252820.htm)
阅读量:20
收藏*

---

[![](https://img.lancdn.com/public/images/view/%E9%98%BF%E9%87%8C%E4%BA%91-%E6%97%A5%E5%B8%B8%E6%B4%BB%E5%8A%A8-%E8%93%9D%E7%82%B9%E7%BD%91%E9%A6%96%E9%A1%B5-%E6%A8%AA%E5%B9%85-20240716.webp)](https://ourl.co/aliold "阿里云服务器仅需99元/年，续费同价，限时抢购中")

#软件资讯 WPS 办公软件升级程序被 Microsoft Defender 误报拦截，微软认为是臭名昭著的勒索软件 Conti。该问题目前应该只影响 WPS 64 位测试版，暂时还未看到使用正式版的用户反馈，当然这个问题肯定是误报，毕竟 WPS 再离谱也不太可能使用 Conti 的软件代码。https://ourl.co/105154

金山办公旗下的 WPS Office 日前正在测试 64 位版，上周日就有蓝点网网友向我们反馈称 WPS 的升级程序被 Microsoft Defender 报毒并拦截，不过当时蓝点网安装的测试版没发现问题，网友也没截图。

今天蓝点网在测试机上安装的 WPS 终于也被报毒了，我们安装的同样是 64 位测试版，被报毒的是 WPS 主升级程序 wpsupdate.exe，并且非常离谱的是微软给出的说明竟然是勒索软件(Ransom:Win64/Conti.IIP!MTB)。

原本网友还在怀疑是不是 WPS 搞什么小动作被微软发现了，但蓝点网现在看到提示几乎可以确认就是误报，[微软将其误报为臭名昭著的勒索软件 Conti](https://www.landiannews.com/archives/93934.html)。

这款勒索软件与 Ryuk 勒索软件使用相同的代码库，在过去两年 Conti 造成的各种问题也非常多，只不过 WPS 升级程序再怎么有问题也不至于被离谱的报告为勒索软件吧。

这个问题暂时应该只影响 WPS 64 位测试版，不知道使用 WPS Office 当前正式版的用户是否遇到了类似问题，主程序路径为：C:\User\{USERNAME}\AppData\Romaing\kingsoft\office6\update\down\wpsupdate.exe

由于蓝点网使用的 Microsoft Defender 已经关闭了文件自动提交功能，所以微软还弹出通知询问是否要提交 wpsupdate 这个 “病毒” 文件样本。

**感谢蓝点网网友 @Sheldon 提供的消息**

**下面是截图：**

[![离谱！WPS升级程序被Microsoft Defender误报拦截 微软认为是勒索软件](https://img.lancdn.com/landian/2024/07/105154-1.png)](https://img.lancdn.com/landian/2024/07/105154-1.png)

[![离谱！WPS升级程序被Microsoft Defender误报拦截 微软认为是勒索软件](https://img.lancdn.com/landian/2024/07/105154-2.png)](https://img.lancdn.com/landian/2024/07/105154-2.png)

[![离谱！WPS升级程序被Microsoft Defender误报拦截 微软认为是勒索软件](https://img.lancdn.com/landian/2024/07/105154-3.png)](https://img.lancdn.com/landian/2024/07/105154-3.png)

[![离谱！WPS升级程序被Microsoft Defender误报拦截 微软认为是勒索软件](https://img.lancdn.com/landian/2024/07/105154-4.png)](https://img.lancdn.com/landian/2024/07/105154-4.png)

文章来源: https://www.landiannews.com/archives/105154.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)