---
title: ExchangePE（环境中快速寻找Exchange服务器）
url: https://buaq.net/go-152037.html
source: unSafe.sh - 不安全
date: 2023-03-06
fetch_date: 2025-10-04T08:45:00.060655
---

# ExchangePE（环境中快速寻找Exchange服务器）

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

![](https://8aqnet.cdn.bcebos.com/97abe578f6f0e3d25fb6c00c2501d047.jpg)

ExchangePE（环境中快速寻找Exchange服务器）

我们在内网中想要拿到域控，肯定会想到Exchange Service服务器，Exchange服务器的权限一般都是域管理员权限，所以拿下服务器的权限也就离域控权限不远
*2023-3-5 12:18:0
Author: [xz.aliyun.com(查看原文)](/jump-152037.htm)
阅读量:40
收藏*

---

我们在内网中想要拿到域控，肯定会想到Exchange Service服务器，Exchange服务器的权限一般都是域管理员权限，所以拿下服务器的权限也就离域控权限不远了。这个工具主要是使用Go重构了ExchangeFinder工具，并做了一些更新，减少原工具匹配不全面的问题，以及实现了Go语言的高并发。 工具链接：<https://github.com/M0nster3/ExchangePE>

主要是通过遍历domain.txt文件当作子域名，可以自己搜集子域名进行添加增加概率，然后解析DNS A记录来进行确认是否可以访问，接着通过返回包中的X-Owa-Version，与[微软版本号](https://learn.microsoft.com/zh-cn/exchange/new-features/build-numbers-and-release-dates?view=exchserver-2019 "微软版本号") 进行对比然后显示版本号。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230305121632-82c819bc-bb0c-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230305121651-8dc2680e-bb0c-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230305121715-9c758c78-bb0c-1.png)

文章来源: https://xz.aliyun.com/t/12255
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)