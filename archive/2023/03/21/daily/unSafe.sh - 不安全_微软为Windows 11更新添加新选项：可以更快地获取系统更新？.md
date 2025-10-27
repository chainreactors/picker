---
title: 微软为Windows 11更新添加新选项：可以更快地获取系统更新？
url: https://buaq.net/go-154399.html
source: unSafe.sh - 不安全
date: 2023-03-21
fetch_date: 2025-10-04T10:06:25.630618
---

# 微软为Windows 11更新添加新选项：可以更快地获取系统更新？

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

![](https://8aqnet.cdn.bcebos.com/5b2853ba915e81244be12eb754510c15.jpg)

微软为Windows 11更新添加新选项：可以更快地获取系统更新？

我们知道微软每个月会发布B/C/D类更新 , 其中B类代表稳定版更新 , C/D类更新属于非安全更新也是可选的。当微软发布非安全更新时，仅在用户主动点击检查更新按钮系统才会安装，究其原
*2023-3-20 22:14:49
Author: [www.landiannews.com(查看原文)](/jump-154399.htm)
阅读量:15
收藏*

---

我们知道微软每个月会发布B/C/D类更新 , 其中B类代表稳定版更新 , C/D类更新属于非安全更新也是可选的。

当微软发布非安全更新时，仅在用户主动点击检查更新按钮系统才会安装，究其原因是这些更新带测试性质。

既然带有测试性质自然不可能向所有用户推送，所以微软设置为仅在用户主动检查更新时才会获得可选更新。

有趣的是在 [Windows 11 Can Build 25309+](https://www.landiannews.com/archives/97758.html) 版中 , 微软似乎开发了个新选项可以让用户更快获得最新更新。

**从字面意义上看：**

这个新选项名为：在最新的更新可用于你的电脑后立即获取它们。从字面意义上看就是微软可主动推送更新。

如果蓝点网猜测的没错，这个新功能旨在替代之前的手动检查更新，让用户无需点击即可获得系统主动推送。

按理说这个功能更适合C/D类可选更新，既然用户主动愿意测试，那第一时间就安装测试补丁自然没啥问题。

不过微软已预留开关，所以即便B类更新也是如此那用户也可以禁用 ，避免第一时间安装补丁以免出现翻车。

注：目前该功能并未公开发布所以微软也没有发布说明，估计本周或者下周发布的新版本应该会介绍该功能。

[![微软为Windows 11更新添加新选项：可以更快地获取系统更新？](https://img.lancdn.com/landian/2023/03/97927-4.png)](https://img.lancdn.com/landian/2023/03/97927-4.png)

**如何启用此功能：**

👇正常情况下是这样的

[![微软为Windows 11更新添加新选项：可以更快地获取系统更新？](https://img.lancdn.com/landian/2023/03/97927-1.png)](https://img.lancdn.com/landian/2023/03/97927-1.png)

我们使用ViveTool开启功能ID：[[图文教程] Windows 11开发版必备神器ViveTool到底怎么用？其实很简单](https://www.landiannews.com/archives/94547.html)

```
#启用测试功能
vivetool /enable /id:43132439
#启用后无需重启资源管理器，下图中后面的命令是重启资源管理器可以忽略
```

[![微软为Windows 11更新添加新选项：可以更快地获取系统更新？](https://img.lancdn.com/landian/2023/03/97927-2.png)](https://img.lancdn.com/landian/2023/03/97927-2.png)

转到这个注册表路径：*HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\WindowsUpdate\UX\Settings*

在右侧空白处点右键新建 DOWRD 32 位值并命名为 *IsContinuousInnovationOptedIn* 并将键值修改为1。

[![微软为Windows 11更新添加新选项：可以更快地获取系统更新？](https://img.lancdn.com/landian/2023/03/97927-3.png)](https://img.lancdn.com/landian/2023/03/97927-3.png)

启用功能 ID 和修改注册表后重启系统，重启后进入设置、系统更新，此时应该就可以看到这个新功能选项。

![](https://img.lancdn.com/landian/2023/03/97927-4.png)

版权声明：感谢您的阅读，除非文中已注明来源网站名称或链接，否则均为蓝点网原创内容。转载时请务必注明：来源于蓝点网、标注作者及[本文完整链接](https://www.landiannews.com/archives/97927.html)，谢谢理解。

文章来源: https://www.landiannews.com/archives/97927.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)