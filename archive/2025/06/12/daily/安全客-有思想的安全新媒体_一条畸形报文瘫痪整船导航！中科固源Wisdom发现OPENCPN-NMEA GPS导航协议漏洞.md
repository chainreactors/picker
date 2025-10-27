---
title: 一条畸形报文瘫痪整船导航！中科固源Wisdom发现OPENCPN-NMEA GPS导航协议漏洞
url: https://www.anquanke.com/post/id/307820
source: 安全客-有思想的安全新媒体
date: 2025-06-12
fetch_date: 2025-10-06T22:47:52.236702
---

# 一条畸形报文瘫痪整船导航！中科固源Wisdom发现OPENCPN-NMEA GPS导航协议漏洞

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

# 一条畸形报文瘫痪整船导航！中科固源Wisdom发现OPENCPN-NMEA GPS导航协议漏洞

阅读量**84880**

发布时间 : 2025-06-11 18:57:58

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

NMEA 0183（National Marine Electronics Association 0183）是航海电子设备和定位系统（如GPS、雷达、声呐等）之间进行数据通信的标准化协议。它于1983年由美国国家海洋电子协会制定，目前广泛应用于航海、车载导航、无人机、测绘等领域。NMEA 0183的核心目的是在设备间共享定位、导航和环境数据，典型应用包括：

**1.航海导航**

 – GPS接收器向雷达、自动舵（Autopilot）发送实时位置、速度、航向。

– 声呐设备输出水深数据，供导航系统避开浅滩。

**2.车载系统**

– 车载GPS模块向中控屏或行车记录仪传输位置、速度、时间。

**3.无人机与测绘**

– 无人机通过NMEA 0183输出定位数据，供地面站记录轨迹或绘制地图。

![]()

**关于OpenCPN**

OpenCPN是一款非常知名的开源海洋绘图导航软件，被应用到各大海洋船舶研究机构与教学中，以其轻巧便利且功能强大而著称。

在美国海洋研究船的ECDIS（电子海图显示与信息系统）中，船员使用OpenCPN 作为科学任务的主导航界面，对采集到的航迹和声呐数据进行实时监控。

美国海岸警卫队第一区在其官方指南中推荐OpenCPN作为免费海图查看工具，支持PC和macOS平台，为巡逻及航行培训提供便利。

中科固源使用完全自主研发的-Wisdom协议安全测试与分析平台对OPENCPN导航定位程序j进行协议安全自动化测试，通过自动生成的测试用例发现可导致OpenCPN导航程序远程崩溃漏洞。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**中科数测**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307820](/post/id/307820)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**3赞

收藏

![](https://p4.ssl.qhimg.com/t11fd941d712ac4e71048598691.png)中科数测

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t11fd941d7193e6e009506afa34.png)

[![](https://p4.ssl.qhimg.com/t11fd941d712ac4e71048598691.png)](/member.html?memberId=175961)

[中科数测](/member.html?memberId=175961)

致力于成为全球领先的软件应用安全解决方案提供商

* 文章
* **24**

* 粉丝
* **1**

### TA的文章

* ##### [从技术到安全：中科固源拆解车载以太网的演进路径与防护策略](/post/id/310094)

  2025-08-21 21:48:41
* ##### [从原理到实战：中科固源带你吃透 ASAN 工作机制，影子内存 + 投毒技术捕捉漏洞全流程](/post/id/309321)

  2025-07-03 17:21:58
* ##### [技术向｜Cybellum 实战：从固件上传到漏洞报告生成，我是如何定位路由器安全隐患的？](/post/id/308334)

  2025-06-13 15:21:03
* ##### [中科固源Wisdom发现NASA嵌入式飞行控制系统—F prime通信协议漏洞！](/post/id/308332)

  2025-06-12 15:27:10
* ##### [中科固源获NVIDIA产品安全团队致谢！](/post/id/308330)

  2025-06-12 13:33:12

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
* ##### [从技术到安全：中科固源拆解车载以太网的演进路径与防护策略](/post/id/310094)

  2025-08-21 21:48:41
* ##### [智能体防御 | 一文了解3种系统提示词加固方法](/post/id/311279)

  2025-08-18 16:34:50

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