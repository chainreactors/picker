---
title: 研究人员打造AI智能体 可全自动实施诈骗通话
url: https://www.anquanke.com/post/id/315106
source: 安全客-有思想的安全新媒体
date: 2026-03-11
fetch_date: 2026-03-12T04:06:43.979873
---

# 研究人员打造AI智能体 可全自动实施诈骗通话

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

# 研究人员打造AI智能体 可全自动实施诈骗通话

阅读量**23350**

发布时间 : 2026-03-11 13:59:37

**x**

##### 译文声明

本文是翻译文章，文章原作者 Abinaya，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/scamagent-ai/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

**ScamAgent** 是由罗格斯大学研究员 Sanket Badhe 开发的**全自动多轮对话 AI 框架**，该系统展示了大型语言模型（LLM）如何被恶意利用，用于实施**完全自动化的诈骗通话**。

通过整合**目标驱动规划、上下文记忆与实时语音合成（TTS）**，该系统成功绕过现有 AI 安全机制，实现高度逼真的社会工程学攻击。

ScamAgent 的架构不同于传统提示词注入，它采用**中央调度器**，在多轮交互中统一管理对话状态与欺骗策略。

当接收到恶意任务时，该智能体会通过**目标拆解**，将攻击目标分解为一系列看似无害的子目标，模拟人类诈骗分子逐步获取受害者信任的过程。

为绕过 GPT‑4、LLaMA3‑70B 等模型的安全过滤器，ScamAgent 会将恶意指令包装在**角色扮演场景**中，在标准单轮审核工具面前成功隐藏核心恶意意图。

在五种常见诈骗场景的实验评估中，ScamAgent 均能**有效突破模型对齐机制与安全协议**。

**目标拆解**：攻击者将恶意目标拆分为多个看似无害的步骤。防护需对多轮对话进行全程追踪检测。

**欺骗与角色扮演**：恶意请求隐藏在虚假剧情或官方身份中。可通过禁止身份仿冒、限制 AI 人设来降低风险。

**上下文记忆**：系统会记录历史对话并调整诈骗策略。限制记忆长度可降低此类风险。

**实时语音合成**：将文本转化为逼真的诈骗语音。在生成语音前对内容进行审核可防止滥用。

直接发送恶意查询的拒绝率为 84%～100%，而该智能体框架通过**在多轮对话中分散恶意意图**，将拒绝率降至 17%～32%。

值得注意的是，在求职身份诈骗模拟中，Meta 的 **LLaMA3‑70B** 模型完整对话完成率高达 **74%**，可完成所有子任务且不触发任何安全拦截。

研究人员表示，防御此类**全自动生成式攻击**，安全系统必须从简单的提示词过滤，升级为**可理解用户意图的持续监控**。

研究团队呼吁 AI 平台与安全团队部署**多层防御体系**，包括使用序列分类器预测长期攻击结果，并严格限制模型的记忆存储行为。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/scamagent-ai/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315106](/post/id/315106)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/scamagent-ai/)

如若转载,请注明出处： <https://cybersecuritynews.com/scamagent-ai/>

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

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1080**

* 粉丝
* **6**

### TA的文章

* ##### [侧边栏里的间谍假冒AI浏览器插件窃取90万用户数据](/post/id/315092)

  2026-03-11 14:01:17
* ##### [Kubernetes安全预警Ingress-Nginx注入漏洞可致集群密钥全局泄露](/post/id/315095)

  2026-03-11 14:00:47
* ##### [Budibase存在高危漏洞 可导致生产环境密钥全面泄露](/post/id/315099)

  2026-03-11 14:00:25
* ##### [Radware推出Alteon Protect实现云级ADC应用安全防护](/post/id/315102)

  2026-03-11 14:00:03
* ##### [研究人员打造AI智能体 可全自动实施诈骗通话](/post/id/315106)

  2026-03-11 13:59:37

### 相关文章

* ##### [侧边栏里的间谍假冒AI浏览器插件窃取90万用户数据](/post/id/315092)

  2026-03-11 14:01:17
* ##### [Kubernetes安全预警Ingress-Nginx注入漏洞可致集群密钥全局泄露](/post/id/315095)

  2026-03-11 14:00:47
* ##### [Budibase存在高危漏洞 可导致生产环境密钥全面泄露](/post/id/315099)

  2026-03-11 14:00:25
* ##### [Radware推出Alteon Protect实现云级ADC应用安全防护](/post/id/315102)

  2026-03-11 14:00:03
* ##### [黑客利用微软Teams诱骗员工开放远程访问权限](/post/id/315110)

  2026-03-11 13:59:13
* ##### [微软推出365 E5升级套件与Agent 365 AI管控平台](/post/id/315113)

  2026-03-11 13:58:42
* ##### [GhostClaw伪装成OpenClaw窃取开发者设备数据](/post/id/315116)

  2026-03-11 13:58:16

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