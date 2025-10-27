---
title: 记一所中学的的SQL报错注入
url: https://www.anquanke.com/post/id/297649
source: 安全客-有思想的安全新媒体
date: 2024-09-04
fetch_date: 2025-10-06T18:21:50.929119
---

# 记一所中学的的SQL报错注入

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

# 记一所中学的的SQL报错注入

阅读量**331133**

发布时间 : 2024-09-03 16:06:03

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

本文作者：Track – 郑居中

**文章中涉及的敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打码处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行承担！**

# 前言

在挖掘edusrc时，觉得211，985好难哇啊，哎，没有实力，老的打不过，只能挑软柿子捏【狗头】

# “软柿子”

在“无意中”发现一所中学的首页，存在注册的功能点，感觉有问题，什么学校在首页放一个注册点啊，好奇心的驱动下，点进去一探究竟

![img]()

注册页面：

![img]()

在注册admin用户后，提示用户名已存在

![img]()

然后用admin用户去尝试弱口令或爆破密码，很遗憾没有成功

![img]()

使用万能密码admin’or 1=1#，提示SyntaxError报错，想必大家看到这个报错，应该都想得到时sql语法报错的提示符吧，说明sql语句的语法错误

![img]()

抓包，在bp中尝试报错注入

![img]()

直接闭合参数，拼接报错语句，得到数据库名和版本号

```
admin1')and updatexml(1,concat(0x7e,version()),1)#
```

![img]()

![img]()

在注册数据包中，同样存在报错注入

![img]()

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**掌控安全学院**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/297649](/post/id/297649)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [Web安全](/tag/Web%E5%AE%89%E5%85%A8)
* [渗透测试](/tag/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95)

**+1**6赞

收藏

![](https://p2.ssl.qhimg.com/t014f774daeca5ec49b.png)掌控安全学院

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t014f774daeca5ec49b.png)](/member.html?memberId=141365)

[掌控安全学院](/member.html?memberId=141365)

公众号：掌控安全EDU

* 文章
* **26**

* 粉丝
* **53**

### TA的文章

* ##### [记一次某src挖掘](/post/id/297719)

  2024-09-04 10:17:32
* ##### [记某研究院多处漏洞复盘](/post/id/298638)

  2024-09-03 16:30:42
* ##### [EDU拿敏感信息的骚思路](/post/id/298022)

  2024-09-03 16:06:55
* ##### [记一所中学的的SQL报错注入](/post/id/297649)

  2024-09-03 16:06:03
* ##### [记一次AccessKey值泄露的挖掘和分析](/post/id/298882)

  2024-08-30 14:41:59

### 相关文章

* ##### [再创新高！纬安科技斩获国家信息安全漏洞库（CNNVD）五项年度大奖，技术贡献获国家级重磅表彰！](/post/id/307588)

  2025-05-22 14:47:31
* ##### [美实名爆料：马斯克领导的DOGE被指入侵劳工机构系统，敏感数据疑遭泄露](/post/id/306743)

  2025-04-21 16:48:48
* ##### [ISCC-2025-第22届信息安全与对抗技术竞赛通知](/post/id/306659)

  2025-04-18 15:49:50
* ##### [梨子带你刷burpsuite靶场系列之服务器端漏洞篇 - sql注入专题更新部分](/post/id/288407)

  2025-03-26 16:05:51
* ##### [梨子带你刷burpsuite靶场系列之客户端漏洞篇 - 跨站脚本(XSS)及跨站请求伪造(CSRF)专题更新部分](/post/id/288408)

  2025-03-26 16:05:51
* ##### [「奇御」AI.安全技术沙龙 · 3月29日北京开启！](/post/id/305187)

  2025-03-20 11:24:51
* ##### [sign加密小程序漏洞挖掘](/post/id/299052)

  2024-08-29 03:21:11

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