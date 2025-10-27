---
title: 多个严重CVE漏洞被发现，系内存类安全漏洞
url: https://www.anquanke.com/post/id/286540
source: 安全客-有思想的安全新媒体
date: 2023-02-22
fetch_date: 2025-10-04T07:41:28.240870
---

# 多个严重CVE漏洞被发现，系内存类安全漏洞

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

# 多个严重CVE漏洞被发现，系内存类安全漏洞

阅读量**302228**

发布时间 : 2023-02-21 17:00:20

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 1.漏洞描述

近日，云起无垠的无垠代码模糊测试系统通过对json parse库、MojoJson进行检测发现多个CVE漏洞，漏洞编号为：CVE-2023-23083 ~ CVE-2023-23088，该系列漏洞皆为内存类漏洞，漏洞允许攻击者执行恶意代码进行攻击，从而造成严重后果。其中，CVE-2023-23086~CVE-2023-23088已公开。

MojoJson 是一个极其简单且超快速的JSON 解析器。解析器支持解析Json 格式，并提供简单的API 来访问不同类型的 Json 值。此外，核心算法可以很容易地用各种编程语言实现。

JSON.parse()是Javascript中一个常用的 JSON 转换方法，JSON.parse()可以把JSON规则的字符串转换为JSONObject，JSON.parse()很方便，并且几乎支持所有浏览器。

针对此类漏洞，无垠代码模糊测试系统均给出了相应建议。

## 2.漏洞详情

① CVE-2023-23086 func SkipString中堆缓冲区溢出

MojoJson v1.2.3中的缓冲区溢出漏洞允许攻击者通过SkipString函数执行任意代码。

漏洞等级：严重；CVSS v3.1漏洞评分：9.8

检测截图：

![]()

![]()

② CVE-2023-23087 函数Destory中指针错误

在MojoJson v1.2.3中发现了一个问题，允许攻击者通过destroy函数执行任意代码。

漏洞等级：严重；CVSS v3.1漏洞评分：9.8

检测截图：

![]()

![]()

③ CVE-2023-23088 json\_value\_parse堆缓冲区溢出

Barenboim json-parser master和v1.1.0中的缓冲区溢出漏洞已在v1.1.1中修复，允许攻击者通过json\_value\_parse函数执行任意代码。

漏洞等级：严重；CVSS v3.1漏洞评分：9.8

检测截图：

![]()

![]()

## 3.解决方案

无垠代码模糊测试系统针对每一个CVE漏洞都给出了处置方案，可参照如上截图细看。

### 无垠代码模糊测试系统

无垠代码模糊测试系统是一款基于Fuzzing技术研发的灰盒检测工具，通过它不仅可以发现逻辑类漏洞，还能找到内存破坏的漏洞，比如缓冲区溢出、内存泄露、条件竞争等。该产品技术基于海量测试用例，融合覆盖引导、人工智能AI等关键技术，赋能软件开发的开发、测试、运维、部署等阶段，在软件上线之前发现已知及未知漏洞，可以更好的防止业务系统带病上线。

参考链接：

<https://nvd.nist.gov/vuln/detail/CVE-2023-23086>
<https://github.com/scottcgi/MojoJson/issues/2>
<https://nvd.nist.gov/vuln/detail/CVE-2023-23087>
<https://github.com/scottcgi/MojoJson/issues/3>
<https://nvd.nist.gov/vuln/detail/CVE-2023-23088>
<https://github.com/Barenboim/json-parser/issues/7>

云起无垠（<https://www.clouitera.com>) 是新一代智能模糊测试领跑者，采用新一代Fuzzing技术全流程赋能软件供应链与开发安全，基于智能模糊测试引擎为协议、代码、数据库、API、Web3.0等应用提供强大的软件安全自动化分析能力，从源头助力企业自动化检测并助其修复业务系统安全问题，为每行代码安全运行保驾护航。

![]()

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**云起无垠**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/286540](/post/id/286540)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**2赞

收藏

![](https://p5.ssl.qhimg.com/t01f48af772ce038b2b.png)云起无垠

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t018f32c85e055c68ed.png)

[![](https://p5.ssl.qhimg.com/t01f48af772ce038b2b.png)](/member.html?memberId=167481)

[云起无垠](/member.html?memberId=167481)

新一代智能模糊测试技术领跑者

* 文章
* **12**

* 粉丝
* **2**

### TA的文章

* ##### [重大升级| SecGPT V2.0：打造真正“懂安全”的大模型](/post/id/306612)

  2025-04-23 10:35:22
* ##### [安全开发进阶（1）|典型开发模式的演进](/post/id/287770)

  2023-03-28 16:23:41
* ##### [技术科普|模糊测试背后的2个核心逻辑](/post/id/286736)

  2023-02-27 13:58:42
* ##### [技术科普 | 模糊测试背后的2个核心逻辑](/post/id/286682)

  2023-02-25 10:21:19
* ##### [多个严重CVE漏洞被发现，系内存类安全漏洞](/post/id/286540)

  2023-02-21 17:00:20

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

* [1.漏洞描述](#h2-0)
* [2.漏洞详情](#h2-1)
* [3.解决方案](#h2-2)
  + [无垠代码模糊测试系统](#h3-3)

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