---
title: Python开发人员警告木马化恶意PyPI包
url: https://www.anquanke.com/post/id/286709
source: 安全客-有思想的安全新媒体
date: 2023-02-25
fetch_date: 2025-10-04T08:01:35.527142
---

# Python开发人员警告木马化恶意PyPI包

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# Python开发人员警告木马化恶意PyPI包

阅读量**272853**

发布时间 : 2023-02-24 12:00:04

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Python开发人员警告，PyPI上存在流氓HTTP包，指出它们能够启动一个木马下载程序。

网络安全研究人员警告说，“冒牌货包”会模仿 Python 包索引 (PyPI) 存储库中可用的流行库。

已发现41个恶意 PyPI 包伪装成合法模块（如 HTTP、AIOHTTP、请求、urllib 和 urllib3）的错别字变体。包的名称如下：aio5, aio6, htps1, httiop, httops, httplat, httpscolor, httpsing, httpslib, httpsos, httpsp, httpssp, httpssus, httpsus, httpxgetter, httpxmodifier, httpxrequester, httpxrequesterv2, httpxv2, httpxv3, libhttps, piphttps, pohttp, requestsd, requestse, request, ulrlib3, urelib3, urklib3, urlkib3, urllb, urllib33, urolib3, xhttpsp。

ReversingLabs 研究员 Lucija Valentić在一篇新的文章中说：“在大多数情况下，这些软件包的描述并没有暗示他们的恶意意图。” “有些伪装成真正的库，并在它们的功能与已知的合法 HTTP 库的功能之间进行美化比较。”

但实际上，它们要么藏有下载器，充当向受感染主机提供第二阶段恶意软件的渠道，要么藏有信息窃取器，旨在泄露密码和令牌等敏感数据。[[阅读原文]](https://thehackernews.com/2023/02/python-developers-warned-of-trojanized.html)

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/286709](/post/id/286709)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [木马](/tag/%E6%9C%A8%E9%A9%AC)
* [Python](/tag/Python)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t01546a096e83e700fe.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t01a1ab830955b940ce.png)

[![](https://p0.ssl.qhimg.com/t01546a096e83e700fe.jpg)](/member.html?memberId=2)

[安全客](/member.html?memberId=2)

有思想的安全新媒体

* 文章
* **3687**

* 粉丝
* **225**

### TA的文章

* ##### [ISC.AI2024热点资讯](/post/id/297785)

  2024-07-10 17:00:28
* ##### [ISC2023热点资讯](/post/id/289102)

  2023-06-06 17:21:40
* ##### [数说安全《攻击面管理产品》报告发布 360以第一顺位入选国内代表性安全厂商](/post/id/288540)

  2023-05-05 12:03:24
* ##### [伪装成ChatGPT的 恶意软件被用来引诱受害者](/post/id/288531)

  2023-05-05 12:01:24
* ##### [研究人员发现Microsoft Azure API管理服务中的3个漏洞](/post/id/288526)

  2023-05-05 11:59:52

### 相关文章

* ##### [新一波“银狐”木马攻势来袭，功能更新目标不变](/post/id/290716)

  2023-10-12 12:21:03
* ##### [木马版Tor浏览器以俄语用户为目标窃取加密钱包](/post/id/288007)

  2023-03-30 14:15:20
* ##### [恶意PyPI软件包使用Cloudflare隧道潜入防火墙](/post/id/285352)

  2023-01-10 14:00:23
* ##### [BitRAT恶意软件活动使用被盗银行数据进行网络钓鱼](/post/id/285083)

  2023-01-05 11:00:31
* ##### [W4SP恶意软件借供应链攻击，盯上Python开发人员](/post/id/283446)

  2022-11-18 14:00:54
* ##### [15年前未修补Python漏洞或影响35万+项目](/post/id/280661)

  2022-09-23 11:15:56
* ##### [朝鲜黑客部署木马版PuTTY SSH盯上媒体](/post/id/280290)

  2022-09-16 11:30:48

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)