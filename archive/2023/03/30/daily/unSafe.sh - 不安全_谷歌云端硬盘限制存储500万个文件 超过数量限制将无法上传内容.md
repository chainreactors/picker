---
title: 谷歌云端硬盘限制存储500万个文件 超过数量限制将无法上传内容
url: https://buaq.net/go-155939.html
source: unSafe.sh - 不安全
date: 2023-03-30
fetch_date: 2025-10-04T11:06:00.070420
---

# 谷歌云端硬盘限制存储500万个文件 超过数量限制将无法上传内容

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

![](https://8aqnet.cdn.bcebos.com/9ad66019417db127df1d54334990a25c.jpg)

谷歌云端硬盘限制存储500万个文件 超过数量限制将无法上传内容

据网友讨论谷歌提供的网盘服务似乎悄悄限制文件数量，谷歌在没有事先公告的情况下限制存储的文件总量。如果用户上传的文件总量超过限制那就无法上传新内容，也不能创建文件夹，只能先删除部分文件后
*2023-3-29 20:41:10
Author: [www.landiannews.com(查看原文)](/jump-155939.htm)
阅读量:20
收藏*

---

据网友讨论谷歌提供的网盘服务似乎悄悄限制文件数量，谷歌在没有事先公告的情况下限制存储的文件总量。

如果用户上传的文件总量超过限制那就无法上传新内容，也不能创建文件夹，只能先删除部分文件后再上传。

目前谷歌官方发言人已经确认谷歌云端硬盘确实有文件总量限制 ，具体来说每个账户的限额为500万个文件。

这个文件总量限制与用户存储空间无关，即便还有剩余存储空间，只要超过文件总量限制后也无法再传文件。

**这种情况对应的报错提示为：***The limit for the number of items, whether trashed or not, created by this account has been exceeded。***如果使用 API 则会报错：***Error 403: This account has exceeded the creation limit of 5 million items. To create more items, move items to the trash and delete them forever., activeItemCreationLimitExceeded*

![](https://img.lancdn.com/landian/public/thumb/workspace.png)

**影响部分特定场景的用户：**

对多数用户来说确实不太可能存储巨量文件，但毕竟世界这么大，总会有些用户的使用场景会触发这类限制。

比如有位网友在英国研究动物健康 ，他们公司利用谷歌云端硬盘存储巨量的小文件，总文件数量超过500万。

在谷歌悄悄施加限制后这家公司的某个关键业务系统受到重大干扰，他们无法再使用云端硬盘同步共享文件。

而且该公司使用的是付费的Google Workspace，最大的问题在于：谷歌为何不提前发公告就悄悄增加限制。

**另外目前似乎还存在BUG：**

从网友讨论来看说是最大限制500万个文件，但有用户存储不到 100 万个文件后谷歌云端硬盘还是出现异常。

这导致用户无法通过API上传文件，在尝试删除一部分文件/文件夹后依然如此，因此这显然是谷歌存在问题。

例如有用户所在企业订阅的是Google Workspace企业标准版，在垃圾箱清理数百万个文件后还是不能上传。

目前谷歌方面还在处理这些问题，不过面向企业提供的服务，随意修改限制确实不太好，至少应该提前公告。

注：500万文件总量限制适用于Google Drive所有版本，不论是最便宜的基本版还是最贵的高级版限制相同。

版权声明：感谢您的阅读，除非文中已注明来源网站名称或链接，否则均为蓝点网原创内容。转载时请务必注明：来源于蓝点网、标注作者及[本文完整链接](https://www.landiannews.com/archives/98054.html)，谢谢理解。

文章来源: https://www.landiannews.com/archives/98054.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)