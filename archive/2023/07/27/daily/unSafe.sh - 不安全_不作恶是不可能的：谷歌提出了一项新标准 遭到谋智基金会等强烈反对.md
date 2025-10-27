---
title: 不作恶是不可能的：谷歌提出了一项新标准 遭到谋智基金会等强烈反对
url: https://buaq.net/go-172993.html
source: unSafe.sh - 不安全
date: 2023-07-27
fetch_date: 2025-10-04T11:52:57.795322
---

# 不作恶是不可能的：谷歌提出了一项新标准 遭到谋智基金会等强烈反对

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

不作恶是不可能的：谷歌提出了一项新标准 遭到谋智基金会等强烈反对

不作恶，那是不可能的。谷歌工程师日前在 GitHub 上发布的一篇 Web 环境完整性解释器引起了轩然大波，实际上这篇内容是 3 个月发布的，但被业界注意到后立即就引起了巨大争议。按照
*2023-7-26 19:58:3
Author: [www.landiannews.com(查看原文)](/jump-172993.htm)
阅读量:15
收藏*

---

不作恶，那是不可能的。

谷歌工程师日前在 GitHub 上发布的一篇 Web 环境完整性解释器引起了轩然大波，实际上这篇内容是 3 个月发布的，但被业界注意到后立即就引起了巨大争议。

按照谷歌工程师的说明，网站和服务器可以调用环境完整性解释器 API，从而检测客户端也就是用户是否为真实用户，如果是真实用户则提供访问，如果不是真实用户则直接拒绝访问。

[![不作恶是不可能的：谷歌提出了一项新Web标准 遭到谋智基金会等强烈反对](https://img.lancdn.com/landian/2019/10/65423.png)](https://img.lancdn.com/landian/2019/10/65423.png)

**谷歌举例这个 API 的好处：**

示例 1：免费网站靠广告获得收入，但广告商只付人类观看广告的费用，而不是机器人。所以用户访问网站时要进行验证挑战，比如选红绿灯这类，证明自己是人类才能访问，这导致用户体验比较差。

示例 2：用户想要知道网站上的帖子、评论、商品评价是真人而非机器人编造的虚假内容；

示例 3：有时候黑客会诱骗用户下载仿冒银行的恶意软件，里面调用银行接口进行验证，从而导致用户蒙受损失。

在以上案例中，如果网站和银行都采用环境完整性 API 进行检查，则可以判断非真人环境从而拦截请求，这可以介绍各种与此类相关的问题。

**所以这听起来是不是还是挺有用的？但其实这里暗藏着巨大的雷，那就是网站也可以检测用户使用的环境进行过滤，例如在 Android 上，如果检测到设备已经 root，则直接拒绝访问或拒绝提供某些功能。**

**在 PC 上，如果用户使用沙盒环境或虚拟机，也可以检测然后拒绝访问，甚至网站还可以拒绝不支持该 API 的浏览器访问，比如如果火狐浏览器不支持该 API，那么用户将无法通过火狐浏览器访问该网站。**

所以当前谋智基金会已经发文强烈反对该提议，同时在 GitHub 上已经有大量网友在 issue 里讨论并反对该提议，一旦该提议被实现，那可能会对开放互联网造成严重打击。

那么谷歌的真实目的是什么？从谷歌字里行间的描述来看，谷歌目的至少包含广告方面，毕竟谷歌广告是目前业界排名第一的平台，广告也是谷歌的支柱业务。

**如果后续网站利用环境 API 检测用户修改网页、拦截广告那都拒绝访问，想想看这是个多么恐怖的事情。**

提议原文：<https://github.com/RupertBenWiser/Web-Environment-Integrity/blob/main/explainer.md>

issue 中的讨论：<https://github.com/RupertBenWiser/Web-Environment-Integrity/issues/28#issuecomment-1642228846>

版权声明：感谢您的阅读，除非文中已注明来源网站名称或链接，否则均为蓝点网原创内容。转载时请务必注明：来源于蓝点网、标注作者及[本文完整链接](https://www.landiannews.com/archives/99634.html)，谢谢理解。

文章来源: https://www.landiannews.com/archives/99634.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)