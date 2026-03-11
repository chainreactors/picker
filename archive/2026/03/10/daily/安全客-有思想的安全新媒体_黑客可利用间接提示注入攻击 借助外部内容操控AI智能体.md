---
title: 黑客可利用间接提示注入攻击 借助外部内容操控AI智能体
url: https://www.anquanke.com/post/id/315071
source: 安全客-有思想的安全新媒体
date: 2026-03-10
fetch_date: 2026-03-11T04:03:25.146355
---

# 黑客可利用间接提示注入攻击 借助外部内容操控AI智能体

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

# 黑客可利用间接提示注入攻击 借助外部内容操控AI智能体

阅读量**20488**

发布时间 : 2026-03-10 14:01:03

**x**

##### 译文声明

本文是翻译文章，文章原作者 cybersecuritynews，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/hackers-can-use-indirect-prompt-injection-allows-adversaries/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

人工智能工具已成为日常工作流程的核心 —— 从能总结网页内容的浏览器，到帮助用户在线决策的自动化智能体，无处不在。

随着这些工具能力不断增强，攻击者正研究如何**将 AI 反制于其原本服务的用户**。

一种名为**间接提示注入（IDPI）** 的攻击手段，可让攻击者在外观正常的网页内容中嵌入隐藏指令，诱骗 AI 智能体执行未获授权的命令。

与直接向聊天机器人输入恶意指令的**直接提示注入**不同，**IDPI 攻击完全在后台静默进行**。

攻击者将指令藏匿于网页中 —— 嵌入**HTML 代码、用户评论、元数据或不可见文本**—— 然后等待 AI 工具访问或处理该页面。

当 AI 执行总结内容、审核广告等常规任务读取页面时，可能会在不知情的情况下将这些隐藏指令当作合法命令并执行。

![]()

Unit 42 研究人员证实，这类攻击**已不再停留在理论阶段**。通过对大规模真实环境流量的分析确认，IDPI 攻击正活跃部署在各大网站中，研究已记录到**22 种构造恶意载荷的独立技术**。

研究结果还揭示了此前未被记载的攻击者目的，包括**全球首个公开的、利用 IDPI 绕过 AI 广告审核系统的真实案例**。

![]()

这类攻击可造成的危害范围极广。攻击者已利用 IDPI 实现**SEO 投毒**以抬高钓鱼网站搜索排名、发起未授权金融交易、迫使 AI 泄露敏感信息，甚至执行可摧毁整个数据库的**服务器端指令**。

在一起监测到的案例中，单个网页内包含**多达 24 次独立注入尝试**，通过叠加多种投递方式提高至少一种方式成功触达 AI 的概率。

![]()

在所有监测流量中，攻击者最常见的目的是制造**无关或干扰性 AI 输出**，占比 28.6%；其次是**数据销毁**，占 14.2%；绕过 AI 内容审核占 9.5%。

这表明攻击者针对 AI 系统的目的极为多样 —— 从制造低级别干扰，到实施严重的金融欺诈。

### 攻击者如何隐藏与投递恶意载荷

这项研究最重要的发现之一，是攻击者为**隐藏注入指令**所投入的复杂程度。

他们不会简单粗暴地在页面中插入覆盖指令，而是**多层叠加隐匿手段**，在确保 AI 智能体可读取并执行的同时，躲避人工审核与自动化扫描检测。

最常见的投递方式为**可见明文注入**，占比 37.8%—— 将命令直接插入绝大多数用户不会留意的页脚区域。

**HTML 属性隐匿**位居第二，占 19.8%：将恶意提示词放入 HTML 标签属性中，浏览器不可见，但 AI 可读取。

**CSS 渲染隐藏**占 16.9%：攻击者通过将字体大小设为 0 或把内容移出屏幕实现文本隐藏。

在**越狱诱导**（绕过安全过滤器迫使 AI 服从注入指令）方面，**社会工程学占绝对主导**，出现在 85.2% 的案例中。

攻击者将指令伪装成来自开发者或管理员，使用 “god mode”“developer mode” 等触发词，让模型认为指令合法且必须执行。

安全团队与 AI 开发者应**将所有不可信网页内容视为潜在攻击源**，在 AI 处理外部数据的所有环节实施输入校验。

部署**隔离（spotlighting）技术**—— 将不可信内容与受信任的系统指令分离 —— 可降低攻击面。AI 系统应遵循**最小权限设计**，执行高影响操作前必须获得用户明确授权。

检测工具必须超越关键词过滤，引入**行为分析与意图分类**，能够识别依靠编码、混淆、多语言等方式绕过防御的 IDPI 攻击。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/hackers-can-use-indirect-prompt-injection-allows-adversaries/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315071](/post/id/315071)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/hackers-can-use-indirect-prompt-injection-allows-adversaries/)

如若转载,请注明出处： <https://cybersecuritynews.com/hackers-can-use-indirect-prompt-injection-allows-adversaries/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1070**

* 粉丝
* **6**

### TA的文章

* ##### [Windows 12的幻影 微软如何用AI重构取代全新系统发布](/post/id/315052)

  2026-03-10 14:05:39
* ##### [依托Polygon公链 越南黑客组织通过GitHub部署历经16代迭代的LuaJIT恶意程序](/post/id/315056)

  2026-03-10 14:05:01
* ##### [OpenAI依托ChatGPT技术打造AI搜索引擎，正面对标谷歌搜索](/post/id/315059)

  2026-03-10 14:04:24
* ##### [AVideo平台存在高危零点击命令注入漏洞 可被用于劫持直播流](/post/id/315062)

  2026-03-10 14:02:53
* ##### [恶意浏览器插件针对imToken用户窃取私钥](/post/id/315065)

  2026-03-10 14:02:18

### 相关文章

* ##### [Windows 12的幻影 微软如何用AI重构取代全新系统发布](/post/id/315052)

  2026-03-10 14:05:39
* ##### [依托Polygon公链 越南黑客组织通过GitHub部署历经16代迭代的LuaJIT恶意程序](/post/id/315056)

  2026-03-10 14:05:01
* ##### [OpenAI依托ChatGPT技术打造AI搜索引擎，正面对标谷歌搜索](/post/id/315059)

  2026-03-10 14:04:24
* ##### [AVideo平台存在高危零点击命令注入漏洞 可被用于劫持直播流](/post/id/315062)

  2026-03-10 14:02:53
* ##### [恶意浏览器插件针对imToken用户窃取私钥](/post/id/315065)

  2026-03-10 14:02:18
* ##### [Viber即时通讯软件存在TLS漏洞，Cloak代理模式失效并导致用户暴露](/post/id/315068)

  2026-03-10 14:01:44
* ##### [海康威视与罗克韦尔自动化高危漏洞纳入CISA已知被利用漏洞清单](/post/id/315077)

  2026-03-10 14:00:36

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