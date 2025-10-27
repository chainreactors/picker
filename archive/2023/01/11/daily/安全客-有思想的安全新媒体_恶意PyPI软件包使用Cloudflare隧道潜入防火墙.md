---
title: 恶意PyPI软件包使用Cloudflare隧道潜入防火墙
url: https://www.anquanke.com/post/id/285352
source: 安全客-有思想的安全新媒体
date: 2023-01-11
fetch_date: 2025-10-04T03:28:33.534547
---

# 恶意PyPI软件包使用Cloudflare隧道潜入防火墙

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

# 恶意PyPI软件包使用Cloudflare隧道潜入防火墙

阅读量**213747**

发布时间 : 2023-01-10 14:00:23

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

在另一个针对Python 包索引（PyPI）存储库的活动中，发现了六个恶意包在开发人员系统上部署信息窃取程序。

Phylum 在2022年12月22日至12月31日期间发现的现已删除的软件包包括 pyrologin、easytimestamp、discorder、discord-dev、style.py 和 pythonstyles。越来越多的恶意代码隐藏在这些库的安装脚本 (setup.py) 中，这意味着运行“pip install”命令足以激活恶意软件部署过程。

该恶意软件旨在启动检索 ZIP 存档文件的 PowerShell 脚本，安装 pynput、pydirectinput 和 pyscreenshot 等侵入性依赖项，并运行从存档中提取的 Visual Basic 脚本以执行更多 PowerShell 代码。[[阅读原文]](https://thehackernews.com/2023/01/malicious-pypi-packages-using.html)

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/285352](/post/id/285352)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [Python](/tag/Python)
* [恶意程序](/tag/%E6%81%B6%E6%84%8F%E7%A8%8B%E5%BA%8F)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t01546a096e83e700fe.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t01a1ab830955b940ce.png)

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

* ##### [Android贷款应用骗取1200 万用户数据](/post/id/291713)

  2023-12-07 12:08:16
* ##### [安全错觉：黑客已学会模仿iOS中的锁定模式](/post/id/291727)

  2023-12-07 12:01:58
* ##### [Python开发人员警告木马化恶意PyPI包](/post/id/286709)

  2023-02-24 12:00:04
* ##### [恶意程序滥用微软IIS功能在Windows上执行恶意代码](/post/id/286520)

  2023-02-20 11:00:27
* ##### [安装量达1500万，诈骗软件专门针对发展中国家](/post/id/284013)

  2022-12-05 11:00:46
* ##### [W4SP恶意软件借供应链攻击，盯上Python开发人员](/post/id/283446)

  2022-11-18 14:00:54
* ##### [Google Play商店4款恶意应用总下载量超百万次](/post/id/282607)

  2022-11-03 15:00:02

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