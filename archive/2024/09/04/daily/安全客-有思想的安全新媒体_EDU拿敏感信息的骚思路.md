---
title: EDU拿敏感信息的骚思路
url: https://www.anquanke.com/post/id/298022
source: 安全客-有思想的安全新媒体
date: 2024-09-04
fetch_date: 2025-10-06T18:21:48.154528
---

# EDU拿敏感信息的骚思路

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

# EDU拿敏感信息的骚思路

阅读量**262241**

发布时间 : 2024-09-03 16:06:55

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

**本文作者：Track – 郑居中**
**文章中涉及的敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打码处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行承担！**

# 1. 寻找资产

在进行edu漏洞挖掘的时候，我们常常遇到统一认证平台，账号是学号，密码是身份证后6位（甚至是更复杂的密码），同时找到这两者的几率很小，所以我们把关注点放在微信小程序中，因为微信小程序存在一键授权登录，不需要本校学生的学号和密码（小部分），这里我们找学校的小程序，直接搜索`大学`,`职业学院`等字样

![img]()

# 2. 开始渗透

随便点进去一个来，手机号一键登录，这里一键登录可能存在泄露session\_key，可以造成账号接管的风险，我的前几篇文章写过session\_key泄露利用方式，师傅们可以去了解一下，话不多说，回到正题，功能点都点一点，看到一个身份证的功能点

![img]()
这里观察数据包，可以看到只有我的手机号，因为我没有实名认证

![img]()

## 骚思路1

仔细观察数据包,原路径是这样的，猜测开发人员的思路，在后面添加`/list`,可能存在

```
原路径/prod-api/system/info/small/userId修改后的路径/prod-api/system/info/small/userId/list
```

修改后的返回包

![img]()
可以看到并没有，这个这个路径，那这样就放弃了吗？显然是不可能的，删除前面的路径,当删到info时，直接回显了，其他人的实名认证的信息，而`idPhoto`，就是sfz存在的地址，太敏感所以这里不放出来了

```
/prod-api/system/info/list
```

![img]()

![img]()

## 骚思路2

默认只有10条信息，想要获取更多的数据信息，观察其他的数据包，发现他们控制输出内容的参数是`?pageNum=1&pageSize=100`，直接拼接

![img]()
就得到了大量的sfz信息和手机号

## 骚思路3

继续思考，将info改为user，发现显示管理员的信息

```
/prod-api/system/user/list
```

![img]()

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**掌控安全学院**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298022](/post/id/298022)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [web安全，渗透测试](/tag/web%E5%AE%89%E5%85%A8%EF%BC%8C%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t014f774daeca5ec49b.png)掌控安全学院

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [为AI Agent行为立“规矩”——字节跳动提出Jeddak AgentArmor智能体安全框架](/post/id/312426)

  2025-09-28 13:43:32
* ##### [教你打造一款AI安全助手 | 安全MCP的实践指南](/post/id/311884)

  2025-09-05 10:40:51
* ##### [当数字世界的“万能钥匙”被滥用，谁来守护核心资产？火山的 MCP 安全授权新范式](/post/id/311597)

  2025-08-28 09:50:41
* ##### [Python代码保护之重置操作码映射的攻与防探究（一）](/post/id/311484)

  2025-08-26 10:49:47
* ##### [广汽集团×火山引擎：出海合规助力企业新增长](/post/id/311498)

  2025-08-26 10:17:09

### 热门推荐

文章目录

* [骚思路1](#h2-0)
* [骚思路2](#h2-1)
* [骚思路3](#h2-2)

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