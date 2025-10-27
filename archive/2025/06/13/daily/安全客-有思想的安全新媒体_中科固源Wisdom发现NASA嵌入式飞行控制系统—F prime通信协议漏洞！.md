---
title: 中科固源Wisdom发现NASA嵌入式飞行控制系统—F prime通信协议漏洞！
url: https://www.anquanke.com/post/id/308332
source: 安全客-有思想的安全新媒体
date: 2025-06-13
fetch_date: 2025-10-06T22:51:01.935106
---

# 中科固源Wisdom发现NASA嵌入式飞行控制系统—F prime通信协议漏洞！

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

# 中科固源Wisdom发现NASA嵌入式飞行控制系统—F prime通信协议漏洞！

阅读量**99633**

发布时间 : 2025-06-12 15:27:10

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

F-Prime 是NASA开源的著名航天航空嵌入式飞行控制系统，应用在多个知名航天项目上，如 **“**机智号**” 火星直升机（ Ingenuity Mars Helicopter ）/ CubeSats 和 SmallSats（立方星和小型卫星）以及国际空间站快速散射仪(ISS-RAPIDSCAT)中。**自F Prime 开源以来，全球多所大学和研究机构将其用于开发实验性航天器和教学项目。其开放性和灵活性使其成为教育和研究领域的热门选择，特别是在小型航天器和快速迭代项目中。其组件化架构、自动化工具链和高可靠性，使其成为现代航天任务中不可或缺的软件基础。

![]()

![]()

![]()

中科固源使用Wisdom协议安全测试工具对F-Prime的最新版本V3.6.2进行了协议Fuzzing测试，发现了可远程使其嵌入式飞行控制系统远程崩溃，由于协议解析序列过滤不严谨而导致，目标程序在接收精心构造的危险数据包后，可导致飞行系统远程崩溃！

中科固源Wisdom推出了专注于航天航空领域的测试套件，针对航天航空领域的通信协自动化进行全面的健壮性与安全性验证测试，可输出详细的测试报告与漏洞信息概念证明。同时，也呼吁所有使用第三方飞行控制组件的组织与商业航天机构，尽快进行自查和更新修复。

中科固源的产品贯穿全软件开发生命周期，覆盖针对源代码、固件、协议和AI的多元智能检测工具和能力。固源将秉承持续创新，并肩负推动国内网络安全磅礴发展的使命，旨在成为全球领先的综合网络安全检测工具供应商。

中科固源AI智能助手【查看详情】

https://ada.baidu.com/site/wjzb2t3dc/agent?imid=3a89730c8af5dd5a76de3316cea40f5f

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**中科数测**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308332](/post/id/308332)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**1赞

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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