---
title: AI 系统将攻击重建时间从数周缩短至数小时
url: https://www.anquanke.com/post/id/314389
source: 安全客-有思想的安全新媒体
date: 2026-01-19
fetch_date: 2026-01-20T03:30:36.556550
---

# AI 系统将攻击重建时间从数周缩短至数小时

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

# AI 系统将攻击重建时间从数周缩短至数小时

阅读量**14530**

发布时间 : 2026-01-19 16:49:30

**x**

##### 译文声明

本文是翻译文章，文章原作者 Robert Lemos, Contributing Writer Robert Lemos

译文仅供参考，具体内容表达以及含义原文为准。

![]()
美国一家联邦实验室正致力于让**威胁仿真流程**变得更高效，以便安全团队能够更快地测试其系统是否能抵御最新的攻击。

据太平洋西北国家实验室（PNNL）的研究团队称，一个名为 **ALOHA（Agentic LLMs for Offensive Heuristic Automation）** 的人工智能系统可以快速**重建攻击**并生成变体来测试防御。PNNL 数据科学家、ALOHA 研究负责人 Loc Truong 表示，通过让系统能够根据威胁报告和描述自动生成攻击，PNNL 将保护系统的时间从**数周缩短到了数小时**。

他说，其目标是让测试防御是否能应对最新攻击的过程变得尽可能高效。

“我们希望能够拿到一个新发现的攻击，然后迅速复制它，并在内部系统防御上进行测试，看看它们是否能检测到这种新攻击。”Truong 说，“每个团队，每个大型组织，都必须经历这个过程：首先重建攻击，而这通常需要一支熟练的工程专家团队、几周时间，以及大量资金。”

ALOHA 并不是第一个利用 AI 来提高攻击生成效率的攻击性安全项目。AI 系统的使用已经迅速演变成攻击者与防御者之间的**军备竞赛**。安全研究人员警告说，所有主要的基础 AI 模型 —— 从 Anthropic 的 Claude、OpenAI 的 ChatGPT、Google 的 Gemini，到 xAI 的 Grok—— 不是已经被攻击者使用，就是存在可能被攻击者利用的弱点。

PNNL 还指出，在一年一度的 DEF CON 夺旗赛（CTF）中，每支参赛队伍都将 AI 作为其工具包的一部分；而 Google 也发现证据表明，恶意软件作者正在开发能在运行时调用大语言模型（LLM）的程序，以更好地**隐藏其恶意本质**。

### **防御性 AI 系统可能会改变攻防力量的平衡。**

在发现新攻击后，网络安全研究人员通常会发布一份威胁报告，其中包含漏洞利用的描述、受影响软件的细节，甚至可能包括攻击者使用的技术、工具和流程（TTPs）。组织的安全团队会分析这份报告，但要创建一条足够接近真实威胁、可用于测试防御的攻击链，往往需要**几天到几周**的时间。

ALOHA 项目的网络安全研究员 Kris Willis 表示，将 ALOHA 引入流程可以帮助组织的 **紫队（Purple Team）** 工作更有效。

相关报道：委内瑞拉军事行动中可能包含网络攻击

“你不仅能进行攻击模拟，还能同时开展防御工作，” 他说，并补充道，虽然有不少工具可以帮助安全团队分析攻击，但将 TTP 与攻击者进行匹配的工具并不常见。“最难的部分是开发 TTP，然后与防御团队合作编写缓解措施。”

ALOHA 不仅能分析威胁报告并生成攻击者最可能使用的 TTP 攻击手册，还能在测试网络、仿真环境或网络靶场中测试这些攻击。此外，该 AI 系统还能帮助为系统弱点编写缓解措施，并协助配置防御系统，以便在攻击正在进行时更好地提醒组织。

ALOHA 使用 Anthropic 的 Claude 大语言模型，并与 MITRE 的开源工具 **Caldera** 协同工作，Caldera 常用于自动化对手仿真、测试和开发防御检测、原型设计、攻击研究以及红队训练。研究人员表示，借助该系统，安全团队可以快速构建包含 20 多种战术、需要数十个步骤的攻击仿真。

“你用简单的英文描述你想要的攻击，生成式 AI 就会自动运行攻击，”Truong 在 ALOHA 的在线介绍中说。“这项技术加快了防御者的响应速度，使网络安全专家不必亲自执行那么多操作。只需点击即可运行。”

相关报道：不再唱反调：对 AI 的怀疑正在上升

### 超越 “我是否存在漏洞？”

Aviatrix（一家专注于 AI 的云网络安全公司）的首席产品策略经理 Benson George 表示，MITRE Caldera 的用户会发现使用 ALOHA 的过程相当简单。该公司已经在使用 Caldera 进行对手仿真，并计划尝试这个新框架，尤其是如果它能改善开源框架中一些较繁琐的部分。

“红队很可能会成为重度用户 —— 我们这边肯定会用，” 他说。“它是对 Caldera 的补充。Caldera 是一个很棒的工具，但它非常耗时，而且对细节要求极高。”

Willis 表示，最终，PNNL 研究团队希望让 AI 对更多类型的组织有用，而不仅仅是高级安全团队。

“关键在于优化防御，” 他说，并指出当前的集成使该工具能够完成整个攻击仿真和防御缓解周期。“它先运行攻击能力，然后回头查看防御工具，接着制定防御对策，再重新运行攻击，看看防御工具是否能检测到它。”

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314389](/post/id/314389)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **930**

* 粉丝
* **6**

### TA的文章

* ##### [1340 亿美元豪赌：马斯克起诉 OpenAI，加州监管重拳同时砸向 xAI](/post/id/314365)

  2026-01-19 16:54:15
* ##### [CVE-2026-0695：ConnectWise PSA 2026.1 修复高危跨站脚本（XSS）漏洞](/post/id/314368)

  2026-01-19 16:53:36
* ##### [虚假生产力工具：5 款恶意 Chrome 扩展劫持企业会话](/post/id/314370)

  2026-01-19 16:53:09
* ##### [未修补的远程代码执行漏洞：Livewire Filemanager 文件上传缺陷（CVE-2025-14894）影响 Laravel 应用](/post/id/314374)

  2026-01-19 16:52:22
* ##### [Deno 高危漏洞可导致密钥泄露（CVE-2026-22863）与代码执行（CVE-2026-22864）](/post/id/314377)

  2026-01-19 16:51:31

### 相关文章

* ##### [1340 亿美元豪赌：马斯克起诉 OpenAI，加州监管重拳同时砸向 xAI](/post/id/314365)

  2026-01-19 16:54:15
* ##### [CVE-2026-0695：ConnectWise PSA 2026.1 修复高危跨站脚本（XSS）漏洞](/post/id/314368)

  2026-01-19 16:53:36
* ##### [虚假生产力工具：5 款恶意 Chrome 扩展劫持企业会话](/post/id/314370)

  2026-01-19 16:53:09
* ##### [未修补的远程代码执行漏洞：Livewire Filemanager 文件上传缺陷（CVE-2025-14894）影响 Laravel 应用](/post/id/314374)

  2026-01-19 16:52:22
* ##### [Deno 高危漏洞可导致密钥泄露（CVE-2026-22863）与代码执行（CVE-2026-22864）](/post/id/314377)

  2026-01-19 16:51:31
* ##### [2026 年会迎来微芯片植入的 “ChatGPT 时刻” 吗？](/post/id/314380)

  2026-01-19 16:51:12
* ##### [大规模清理行动：X 平台禁用 “信息金融”，彻底打击 AI 生成的加密垃圾帖](/post/id/314383)

  2026-01-19 16:50:29

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