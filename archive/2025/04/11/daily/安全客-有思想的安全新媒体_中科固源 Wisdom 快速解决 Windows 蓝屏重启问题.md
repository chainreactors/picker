---
title: 中科固源 Wisdom 快速解决 Windows 蓝屏重启问题
url: https://www.anquanke.com/post/id/306379
source: 安全客-有思想的安全新媒体
date: 2025-04-11
fetch_date: 2025-10-06T22:02:58.661531
---

# 中科固源 Wisdom 快速解决 Windows 蓝屏重启问题

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

# 中科固源 Wisdom 快速解决 Windows 蓝屏重启问题

阅读量**100612**

发布时间 : 2025-04-10 17:44:22

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

## ​Windows HTTP协议远程代码执行漏洞

漏洞编号：CVE-2021-31166

漏洞评级：严重

影响范围：Windows Server, version 2004 (Server Core installation)

具体包含以下操作系统版本：

1. Windows Server Version 2004 数据中心版 64位中文版

2. Windows Server Version 2004 数据中心版 64位英文版

3. Windows Server Version 2004 with Container 数据中心版 64位中文版

4. Windows Server Version 2004 with Container 数据中心版 64位英文版

        该漏洞存在于Windows 10和Windows Server中的HTTP协议栈（http.sys）处理程序中，该程序广泛地用于应用之间或设备之间的通信，常见的组件（例如Internet Information Services（IIS））便使用该程序进行通信处理。未授权的攻击者可以构造恶意请求包攻击目标服务器，成功利用该漏洞的攻击者可以在目标服务器执行任意代码。微软官方将其标记为可造成蠕虫攻击及易被攻击，攻击者可以利用该漏洞造成大范围蠕虫攻击。

## POC脚本

Github上有很多POC脚本：

<https://github.com/0vercl0k/CVE-2021-31166/blob/main/cve-2021-31166.py>

[GitHub – ZZ-SOCMAP/CVE-2021-31166: Windows HTTP协议栈远程代码执行漏洞 CVE-2021-31166](https://github.com/ZZ-SOCMAP/CVE-2021-31166)

##

## 靶机搭建

1)安装Oracle VM VirtualBox

2)安装受漏洞影响的Windows版本，本次测试使用的操作系统为Windows 10.0.19041.264

3)开启IIS

首先打开控制面板，点击卸载程序，如下图所示：

![]()

点击“启用或关闭Windows功能”：

![]()

开启IIS：

![]()

![]()

然后点击确定，等待更改完成后重启系统

4)查看虚拟机ip

![]()

如上图所示，虚拟机ip为：192.168.3.1

## 使用Wisdom复现漏洞

1)打开HTTP测试套件，点击Request数据模型，如下图所示

![]()

2)创建自定义测试用例attack，将Accept-Encoding的值改成：doar-e,ftw,imo, ,\r\n

![]()

3)启动测试任务

![]()

4)将目标地址改成虚拟机ip地址（192.168.3.1），选择可以和虚拟机连通的发包网卡

![]()

5)添加TCPMonitor监控器

![]()

6)添加刚才制作的测试用例

![]()

7)运行测试用例后，很快可以看到虚拟机重启了，同时Wisdom捕获到了漏洞

![]()

8)漏洞详情中可以看到触发漏洞的测试用例和数据模型![]()

##

## Wisdom能做什么

1. 协议漏洞挖掘

超过60%的软件漏洞利用源于未公开的0day漏洞，Wisdom内置了我们多年总结下来最有效的测试用例，通过模拟攻击者行为，在恶意黑客发现漏洞前提前捕获问题。

2. 协议健壮性、兼容性测试

自研的先进算法，可以增加测试的广度和深度；基于RFC规范构造的协议模型，可以在页面上快速的修改数据报文和状态机，模拟各种通讯数据和交互流程。

3. 协议安全验证

丰富的监控器和可嵌入任意状态机流程中的监控方式，使得Wisdom不仅可以发现程序崩溃、假死等明显漏洞，还可以发现内存泄漏、加密算法缺陷等逻辑漏洞以及设计漏洞。

4. 私有协议测试

可视化的建模功能和强大的插件扩展能力，可以很方便的完成私有协议模型构建和测试用例制作，帮助完成私有协议的全面测试。

中科固源专注于通讯协议安全与模糊测试，提供Wisdom系列工具和Swift系列工具，帮助企业构建全面的网络安全防护体系。了解更多产品与解决方案。加入我们，开启你的高效代码创新之旅！

①扫描二维码或添加微信，获取1V1线上云指导。

②解锁免费高效的开源级开发工具，还有更多专属权益等你来拿。

③关注我们，在评论区留言“我要学习资料”，即可免费获得独家学习资料包，包括详细使用教程、应用案例分析及相关技术文档。

![]()

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**中科数测**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306379](/post/id/306379)

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

* [​Windows HTTP协议远程代码执行漏洞](#h2-0)
* [POC脚本](#h2-1)
* [靶机搭建](#h2-3)
* [使用Wisdom复现漏洞](#h2-4)
* [Wisdom能做什么](#h2-6)

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