---
title: Armadin获1.9亿美元融资 用AI实现自动化红队攻防
url: https://www.anquanke.com/post/id/315161
source: 安全客-有思想的安全新媒体
date: 2026-03-13
fetch_date: 2026-03-14T04:03:10.413779
---

# Armadin获1.9亿美元融资 用AI实现自动化红队攻防

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

# Armadin获1.9亿美元融资 用AI实现自动化红队攻防

阅读量**24647**

发布时间 : 2026-03-13 10:32:28

**x**

##### 译文声明

本文是翻译文章，文章原作者 Michael Novinson，文章来源：govinfosecurity

原文地址：<https://www.govinfosecurity.com/armadin-launches-190m-to-automate-red-teaming-ai-a-30987>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

由 Kevin Mandia 领衔的一家初创公司正式公开亮相，获得近**1.9 亿美元**融资，旨在通过**自主 AI 智能体**革新渗透测试与红队服务模式。

由 Accel 领投的种子轮及 A 轮融资，将帮助总部位于旧金山的**Armadin**公司研发基于专业红队方法训练的 AI 智能体，实现大规模、持续性安全评估。联合创始人兼攻击安全主管 Evan Pena 表示，依托智能体编排、集群架构与智能体间通信协议，现已可复现复杂的攻击安全工作流。

“此前大家看到的大多是聊天机器人与大模型处理大量文本，提供建议与报告”，Pena 在接受《信息安全媒体集团》采访时表示，“如今我们可以编排任务并真正执行。从对话交互，走向**实际攻击执行**。”

该公司由 Kevin Mandia 掌舵，他曾在威胁情报与事件响应厂商 Mandiant 任职二十年。2013 年他将 Mandiant 出售给 FireEye；2016 年出任 FireEye 首席执行官；2021 年以 12 亿美元将产品业务出售给 Symphony Technology Group；2022 年又以 54 亿美元将更名为 Mandiant 的服务业务出售给谷歌，并于 2024 年离开谷歌。

### AI 智能体协同如何实现网络攻击

**智能体间通信协议**可让多个 AI 实体在 Web 应用、外部基础设施、内部网络等不同域内协同攻击，实现**并行攻击**而非串行执行。传统评估通常只能发现单条有效攻击路径，而 AI 驱动系统可挖掘数十乃至上百条潜在路径。

“在红队层面，我们目前在做两件事”，Pena 说道，“第一是**训练 AI 智能体复刻人类红队的攻击思路与手法**。”

Pena 表示，人类红队专家将多年渗透测试经验、攻击行为理解与专用工具开发能力，转化为 AI 可理解与执行的标准化方法。团队会对攻击流程、工具与决策逻辑进行完整沉淀，包括具体操作背后的研判依据。

“一个通用前沿大模型，你直接让它去攻击某个系统，很可能无法奏效”，Pena 说，“它必须经过**微调**，具备**攻击方法论**，并拥有可实际调用的**攻击工具**。这些价值正是人类红队专家提供的。”

人类渗透测试团队天然倾向于选择**阻力最小的攻击路径**，一旦找到有效入口，测试往往结束，大量潜在攻击路径未被挖掘。而 AI 驱动系统可**持续评估**，而非每年单次测试，探索远超人力可覆盖的攻击路径。

“我整个职业生涯都在做企业安全评估”，Pena 说，“我们几乎总能成功。原因很简单，一直是人力主导，每年测一次，挑最简单的路径，完成目标，交个报告就结束了。”

### Armadin 如何助力漏洞修复

未来，AI 智能体将持续发起攻击、发现漏洞、分析攻击链，由人类专家复核结果、验证复杂攻击链，并挖掘系统尚未掌握的新型技术。人类发现的新攻击方法可纳入 AI 策略库，让模型能力持续进化。

“除非是高度定制化需求，否则我认为已没必要再做人力主导的评估”，Pena 表示，“AI 不仅**更快、更精准**，还能实现**大规模扩展**。人力覆盖不足，必须依靠 AI 智能体。”

Armadin 希望通过分析攻击链，定位**业务影响最大**的漏洞，平台将优先推荐可**彻底切断整条攻击链**的修复方案。AI 未来或可实现自动化修复，但自动重置账号、修改配置、重装系统可能影响业务运行。

“我们希望提供可落地的改进路径，切实帮助你提升安全态势”，Pena 说，“平台会给出**战术与战略级修复建议**，更重要的是完成漏洞闭环。”

通过在完整攻击生命周期中编排多轮攻击，AI 智能体可快速验证检测系统是否能识别恶意行为。若防御系统未检出某类攻击，AI 可生成检测规则，直接接入**SIEM 或 EDR**。这一过程依赖标准化格式与技术文档，正是 AI 模型的强项。

“每次评估都会由人类操作员、我的团队与 AI 分别执行，然后对比结果”，Pena 说，“我们想知道 AI 的**效能提升幅度**，比如是否比人工快 80%。”

本文翻译自govinfosecurity [原文链接](https://www.govinfosecurity.com/armadin-launches-190m-to-automate-red-teaming-ai-a-30987)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315161](/post/id/315161)

安全KER - 有思想的安全新媒体

本文转载自: [govinfosecurity](https://www.govinfosecurity.com/armadin-launches-190m-to-automate-red-teaming-ai-a-30987)

如若转载,请注明出处： <https://www.govinfosecurity.com/armadin-launches-190m-to-automate-red-teaming-ai-a-30987>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1090**

* 粉丝
* **6**

### TA的文章

* ##### [Ally WordPress插件高危SQL注入漏洞 威胁40万个网站](/post/id/315140)

  2026-03-13 10:34:49
* ##### [OpenAI战略调整Sora视频AI将直接接入ChatGPT](/post/id/315145)

  2026-03-13 10:34:23
* ##### [HPE发布Aruba OS高危漏洞预警 可未授权重置密码](/post/id/315148)

  2026-03-13 10:34:00
* ##### [能感知自身正在被测试的AI Anthropic关于Claude自我意识的惊人发现](/post/id/315152)

  2026-03-13 10:33:36
* ##### [GitLab发布紧急安全更新 修复高危XSS与API拒绝服务漏洞](/post/id/315155)

  2026-03-13 10:33:13

### 相关文章

* ##### [Ally WordPress插件高危SQL注入漏洞 威胁40万个网站](/post/id/315140)

  2026-03-13 10:34:49
* ##### [OpenAI战略调整Sora视频AI将直接接入ChatGPT](/post/id/315145)

  2026-03-13 10:34:23
* ##### [HPE发布Aruba OS高危漏洞预警 可未授权重置密码](/post/id/315148)

  2026-03-13 10:34:00
* ##### [能感知自身正在被测试的AI Anthropic关于Claude自我意识的惊人发现](/post/id/315152)

  2026-03-13 10:33:36
* ##### [GitLab发布紧急安全更新 修复高危XSS与API拒绝服务漏洞](/post/id/315155)

  2026-03-13 10:33:13
* ##### [Telegram的黑色面 网络罪犯利用机器人API隐秘窃取数据](/post/id/315158)

  2026-03-13 10:32:51
* ##### [Splunk修复文件预览功能中的高危RCE漏洞](/post/id/315164)

  2026-03-13 10:32:03

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