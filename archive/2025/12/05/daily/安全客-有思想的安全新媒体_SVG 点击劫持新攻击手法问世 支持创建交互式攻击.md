---
title: SVG 点击劫持新攻击手法问世 支持创建交互式攻击
url: https://www.anquanke.com/post/id/313594
source: 安全客-有思想的安全新媒体
date: 2025-12-05
fetch_date: 2025-12-06T03:10:10.982595
---

# SVG 点击劫持新攻击手法问世 支持创建交互式攻击

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

# SVG 点击劫持新攻击手法问世 支持创建交互式攻击

阅读量**12288**

发布时间 : 2025-12-05 17:26:04

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/svg-clickjacking-attack/>

译文仅供参考，具体内容表达以及含义原文为准。

在网络安全领域，**点击劫持（Clickjacking）** 长期以来被视为一种 “低级” 攻击手段。传统的点击劫持通过在合法网站上方覆盖**隐形框架**，诱导用户点击非本意的按钮 —— 例如用虚假的 “播放视频（Play Video）” 覆盖层遮挡 “删除账户（Delete Account）” 按钮。

然而，名为**Lyra**的安全研究员披露了一种名为 “**SVG 点击劫持（SVG Clickjacking）** ” 的复杂新技术，这一技术从根本上改变了威胁格局。作为一种**新型漏洞利用技术**，它彻底颠覆了传统点击劫持的运作模式 —— 将其从简单的 “隐藏按钮” 骗局，升级为能够**读取屏幕内容**并**执行逻辑指令**的复杂交互式漏洞利用工具。

该技术由化名**Lyra（又名 rebane2001）** 的研究员发现并命名，其核心是利用**可缩放矢量图形（Scalable Vector Graphics，SVG）滤镜**创建 “智能” 覆盖层，该覆盖层能够检测目标网站的状态并做出响应。

![]()

与传统点击劫持不同 —— 攻击者仅需叠加**隐形 iframe（内联框架）** 诱导用户点击按钮 —— 这种新方法能让攻击页面 “读取” 目标网站的**像素数据**，并根据用户实际看到的内容动态调整自身界面。

![]()

### SVG 点击劫持攻击（SVG Clickjacking Attack）

该漏洞的核心在于现代浏览器对**feDisplacementMap（位移贴图滤镜）** 、**feColorMatrix（颜色矩阵滤镜）** 、**feComposite（合成滤镜）** 等 SVG 滤镜的处理机制。这些工具原本用于实现折射、颜色偏移等图形效果，但 Lyra 的测试表明，它们可被篡改用于执行**逻辑运算**。

通过将这些滤镜**串联组合**，攻击者可在浏览器的**渲染引擎**内直接构建可正常工作的**逻辑门（与门 / AND、或门 / OR、异或门 / XOR）** 。这一操作相当于将 SVG 滤镜转化为一台**简易计算机**，使其能够对**跨源 iframe（内联框架）** 实施监控。

例如，攻击者可通过该技术检测特定**对话框是否弹出**、**复选框是否勾选**或**红色错误文本是否可见**，随后动态更新虚假覆盖层，引导用户完成多步骤操作流程。

Lyra 通过针对**谷歌文档（Google Docs）** 的概念验证攻击，证实了该技术的严重危害 —— 这一攻击为其赢得了谷歌漏洞奖励计划（Google’s Vulnerability Reward Program）提供的**3133.70 美元**赏金。

此次攻击的显著之处在于，覆盖层需能**响应文档状态**：当用户成功 “输入” 验证码后，虚假输入框会自动隐藏；仅当文档准备就绪时，才会显示新按钮。

“过去，这类攻击的单个环节或许能通过传统点击劫持实现…… 但整个攻击流程会过于冗长复杂，缺乏实际可操作性，”Lyra 写道。

SVG 点击劫持最引人注目的应用，或许是其**数据窃取能力**。该研究员展示了该技术如何从目标网站读取**敏感像素数据**，并将这些数据编码为 URL—— 随后通过**feDisplacementMap（位移贴图滤镜）** 将其渲染为可扫描的**二维码（QR code）** 。

这就形成了一种攻击场景：攻击者可诱导用户 “扫描此码以验证人机身份”，而该二维码实际包含一个 URL—— 其参数中已嵌入窃取的用户**会话数据（session data）** 或**隐私信息**。

这项研究标志着 “**UI 篡改攻击（UI redress attacks）** ” 的显著升级。通过证实 SVG 滤镜可作为**侧信道（side-channel）** 读取跨源像素并执行逻辑运算，该研究表明：仅依赖视觉隐藏已不再是抵御点击劫持的充分防御手段。

正如 Lyra 所指出的，该技术支持构建 “交互式” 且 “响应式” 的攻击，彻底摆脱了以往限制此类漏洞利用效果的**盲目猜测（blind guesswork）** 环节。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/svg-clickjacking-attack/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313594](/post/id/313594)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/svg-clickjacking-attack/)

如若转载,请注明出处： <https://cybersecuritynews.com/svg-clickjacking-attack/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **780**

* 粉丝
* **6**

### TA的文章

* ##### [AI boom 催生全球存储芯片荒 价格将涨三倍至 2027 年](/post/id/313587)

  2025-12-05 17:36:12
* ##### [哈维 AI 完成 7.6 亿美元融资 估值达 80 亿美元](/post/id/313583)

  2025-12-05 17:35:29
* ##### [Cacti 中存在高危漏洞（CVE-2025-66399），通过SNMP团体字符串注入可导致远程代码执行](/post/id/313602)

  2025-12-05 17:34:09
* ##### [“PDF陷阱”：Apache Tika核心组件存在严重漏洞（CVE-2025-66516，CVSS 10.0）](/post/id/313590)

  2025-12-05 17:33:30
* ##### [APT组织“拼凑者”部署StreamSpy木马，通过将命令与控制指令隐匿于WebSocket流量中进行隐秘间谍活动](/post/id/313606)

  2025-12-05 17:31:23

### 相关文章

* ##### [AI boom 催生全球存储芯片荒 价格将涨三倍至 2027 年](/post/id/313587)

  2025-12-05 17:36:12
* ##### [哈维 AI 完成 7.6 亿美元融资 估值达 80 亿美元](/post/id/313583)

  2025-12-05 17:35:29
* ##### [Cacti 中存在高危漏洞（CVE-2025-66399），通过SNMP团体字符串注入可导致远程代码执行](/post/id/313602)

  2025-12-05 17:34:09
* ##### [“PDF陷阱”：Apache Tika核心组件存在严重漏洞（CVE-2025-66516，CVSS 10.0）](/post/id/313590)

  2025-12-05 17:33:30
* ##### [APT组织“拼凑者”部署StreamSpy木马，通过将命令与控制指令隐匿于WebSocket流量中进行隐秘间谍活动](/post/id/313606)

  2025-12-05 17:31:23
* ##### [Splunk中存在高危漏洞，因Windows平台上的不当文件权限设置，可导致本地攻击者实现权限提升](/post/id/313598)

  2025-12-05 17:30:23
* ##### [智能可观测平台Dynatrace深化其AWS服务集成，新增多项AI与云原生监控功能](/post/id/313610)

  2025-12-05 17:29:29

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