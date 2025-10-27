---
title: 组策略成摆设！微软向Windows 10/11强制推送AMD和英伟达显卡驱动
url: https://buaq.net/go-168418.html
source: unSafe.sh - 不安全
date: 2023-06-13
fetch_date: 2025-10-04T11:44:17.151517
---

# 组策略成摆设！微软向Windows 10/11强制推送AMD和英伟达显卡驱动

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

![](https://8aqnet.cdn.bcebos.com/a951e30de652a87f836646fd7ff22e77.jpg)

组策略成摆设！微软向Windows 10/11强制推送AMD和英伟达显卡驱动

组策略是 Windows NT 系统中的一个重要功能，该功能允许用户尤其是企业 IT 管理员批量进行管理和控制某些功能，避免没有管理员权限的用户修改系统重要配置。但估计没多用户能想到组
*2023-6-12 22:56:3
Author: [www.landiannews.com(查看原文)](/jump-168418.htm)
阅读量:25
收藏*

---

组策略是 Windows NT 系统中的一个重要功能，该功能允许用户尤其是企业 IT 管理员批量进行管理和控制某些功能，避免没有管理员权限的用户修改系统重要配置。

但估计没多用户能想到组策略配置策略也能被微软忽略吧？这段时间就有不少用户发现微软绕过系统已经修改后的组策略，继续向用户推送 AMD 和英伟达的显卡驱动程序。

最近微软向 Windows 10/11 AMD 用户推送过时的显卡驱动程序导致部分功能异常，[AMD 不得不在系统上弹出公告提醒用户此事](https://www.landiannews.com/archives/98894.html)，并建议用户前往 AMD 或 OEM 网站重新下载显卡驱动覆盖安装。

[![组策略成摆设！微软向Windows 10/11强制推送AMD和英伟达显卡驱动](https://img.lancdn.com/landian/2023/05/98894.png)](https://img.lancdn.com/landian/2023/05/98894.png)

现在这种情况似乎也影响了英伟达用户，有网友发现自己明明在组策略里设置了禁止推送驱动，结果微软还是给系统安装了英伟达的显卡驱动程序。

[![组策略成摆设！微软向Windows 10/11强制推送AMD和英伟达显卡驱动](https://img.lancdn.com/landian/2023/06/99128-1.png)](https://img.lancdn.com/landian/2023/06/99128-1.png)

图片来自：[@Ghost\_motley](https://twitter.com/ghost_motley/status/1663181809193041920)

这个组策略选项名为 “Windows 更新不包括驱动程序”，位于组策略、本地计算机策略、计算机配置、管理模板、Windows 组件、Windows 更新中。

至少以前在 Windows 10 上是可以正常工作的，因为蓝点网每次装机后都是第一时间启用此策略 (启用后就是禁止驱动自动更新)，禁止更新目的就是防止微软推送不合适和过时的驱动程序。

蓝点网搜索发现遇到这种情况的用户并不少，都是已经配置了禁止更新驱动结果还是被更新了，目前还不知道这是什么情况。

对用户来说组策略配置策略都会忽略着实是个大问题，微软这属于不按套路出牌了，目前不知道这是 BUG 还是微软有意为之。

版权声明：感谢您的阅读，除非文中已注明来源网站名称或链接，否则均为蓝点网原创内容。转载时请务必注明：来源于蓝点网、标注作者及[本文完整链接](https://www.landiannews.com/archives/99128.html)，谢谢理解。

文章来源: https://www.landiannews.com/archives/99128.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)