---
title: 微软修复影响火狐浏览器性能长达5年的BUG 火狐用户真是辛苦了
url: https://buaq.net/go-157727.html
source: unSafe.sh - 不安全
date: 2023-04-10
fetch_date: 2025-10-04T11:29:33.087674
---

# 微软修复影响火狐浏览器性能长达5年的BUG 火狐用户真是辛苦了

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

![](https://8aqnet.cdn.bcebos.com/27dbf88c9e935d7672985ef55134a085.jpg)

微软修复影响火狐浏览器性能长达5年的BUG 火狐用户真是辛苦了

据谋智基金会工程师发布的消息，微软在 4 月 4 日发布 Microsoft Defender 反病毒引擎更新，终于解决了影响火狐浏览器性能长达 5 年的 BUG。这个问题最早在 20
*2023-4-9 01:7:20
Author: [www.landiannews.com(查看原文)](/jump-157727.htm)
阅读量:51
收藏*

---

据谋智基金会工程师发布的消息，微软在 4 月 4 日发布 Microsoft Defender 反病毒引擎更新，终于解决了影响火狐浏览器性能长达 5 年的 BUG。

这个问题最早在 2018 年 5 月被用户发现，有用户在 [Bugzilla](https://bugzilla.mozilla.org/show_bug.cgi?id=1441918) 提交过反馈，这个问题虽然没被忽略但也一直没得到解决，火狐浏览器的工程师们花费了很长时间进行排查，并一步一步缩小范围，最终认定是 Microsoft Defender 反病毒引擎存在问题。

具体来说问题出在微软反病毒引擎的服务中，Microsoft Defender 附带 Antimalware Service Executable 服务 (MsMpEng.exe)，该服务是微软用来提供实时保护、扫描、更新病毒库版本的，由于权限问题用户无法在任务管理器中直接杀掉该服务对应的进程。

[![微软修复影响火狐浏览器性能长达5年的BUG 火狐用户真是辛苦了](https://img.lancdn.com/landian/2023/04/98239-2.png)](https://img.lancdn.com/landian/2023/04/98239-2.png)

当 Firefox 运行时，MsMpEng.exe 会访问 sechost.dll 运行 ProcessTrace，用来生成进程的 Windows 事件跟踪，但使用 Firefox 时 ProcessTrace 生成的事件跟踪要比其他进程多的多，这导致当 Firefox 运行时 CPU 资源使用率比正常情况下提升了五倍。

而使用 Chrome 和 Microsoft Edge 等浏览器则没有这种情况，这个问题只影响 Firefox 浏览器，所以用户如果观察任务管理器会发现 Antimalware Service Executable 持续占用较高的 CPU 资源，如果是配置较低的笔记本电脑，使用 Firefox 时风扇转速可能都会明显提升，用户可以通过风扇声音注意到这个问题。

在火狐工程师确认这个问题并提交给微软后，微软在 4 月 4 日发布更新修复问题，该更新目前已经自动推送到 Windows 10 和 Windows 11。

**图片说明：**

上半部分是修复前，可以看到使用 Firefox 时，MsMpEng.exe 占用大量 CPU，显示为红色部分代表占用率高

下半部分是修复后，可以看到 MsMpEng.exe 出现红色的情况大幅度减少

[![微软修复影响火狐浏览器性能长达5年的BUG 火狐用户真是辛苦了](https://img.lancdn.com/landian/2023/04/98239-1.png)](https://img.lancdn.com/landian/2023/04/98239-1.png)

**版本方面：**

经过修复的版本是：Microsoft Defender 引擎版本 1.1.20200.4、反恶意软件客户端版本 4.18.2302.x (将于 2023 年 4 月 11 日发布)

[![微软修复影响火狐浏览器性能长达5年的BUG 火狐用户真是辛苦了](https://img.lancdn.com/landian/2023/04/98239-3.png)](https://img.lancdn.com/landian/2023/04/98239-3.png)

注：蓝点网使用的是 Beta 版所以已经收到 4.18.2302.7 的推送，正式版通道要等 4 月 11 日推送

一些用户可能会注意到使用其他安全软件也存在类似问题，火狐浏览器工程师还在继续排查，如果发现其他安全软件也有类似问题后续也会修复。

另外 Antimalware Service Executable 这个服务经常在开机时占用大量 CPU，有时候使用其他软件也可能会发现它占用不少 CPU，这个属于 Microsoft Defender 的问题，正常情况下如果没有执行系统扫描功能那这个服务不应该占用太多 CPU，这类问题还需要微软继续优化。

版权声明：感谢您的阅读，除非文中已注明来源网站名称或链接，否则均为蓝点网原创内容。转载时请务必注明：来源于蓝点网、标注作者及[本文完整链接](https://www.landiannews.com/archives/98239.html)，谢谢理解。

文章来源: https://www.landiannews.com/archives/98239.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)