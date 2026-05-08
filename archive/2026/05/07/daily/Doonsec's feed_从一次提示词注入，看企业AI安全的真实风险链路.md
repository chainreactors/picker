---
title: 从一次提示词注入，看企业AI安全的真实风险链路
url: https://mp.weixin.qq.com/s/jqB280qUtk9Rb4GK6Hd6oQ
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:55:04.910908
---

# 从一次提示词注入，看企业AI安全的真实风险链路

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TFxibKqzXJXLKsDC32Upgnn17jwJohzz3kOLrUricq3dfulicaPARLa79GrTmTFCRrDVRyURzB2gic573hjXicjDicjStMt56iapSgR2QYZulSkxrg/0?wx_fmt=jpeg)

# 从一次提示词注入，看企业AI安全的真实风险链路

观安信息

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

近期，业界披露了两起较受关注的企业级AI事件：Microsoft Copilot Studio与Salesforce Agentforce均被公开指出存在由提示词注入引发的数据泄露风险。公开分析显示，攻击者可以通过公共输入面植入恶意提示词，诱导 AI agent 访问已连接的数据源，并把原本不该暴露的企业信息泄露出去；其中 Copilot Studio 相关问题被分配为 CVE-2026-21520。这类事件说明，大模型应用的风险已经不只是“回答跑偏”，而是可能进一步演变成数据外泄与治理失控。

对企业来说，真正要解决的，已经不只是“怎么把模型接进来”，而是：

****如何安全地在业务中使用模型。****

**一**

**这个事件，问题到底出在哪里？**

##

如果把这类攻击链条拆开看，逻辑并不复杂。

**第一步，**攻击者把恶意提示词隐藏进正常输入面。

在公开案例中，攻击入口并不是复杂的底层漏洞利用，而是公共表单、评论输入、外部交互内容这类看起来很正常的业务入口。模型或AI agent 在读取这些内容时，会把它们当成正常上下文。

**第二步，**模型把这些内容当成“可以执行的指令”。

问题的关键不在于模型“看到了恶意代码”，而在于它往往无法自动区分：哪些是待处理内容，哪些其实是在“指挥它做事”。一旦输入内容中夹带了恶意提示词，agent就可能偏离原本预设的安全边界。

**第三步****，**风险通过业务连接能力进一步扩散。

由于企业级AI agent 往往已经接入知识库、邮件、CRM、协同平台等数据源，一旦被诱导，就可能把原本不该暴露的数据查询出来，再通过允许的业务动作或返回结果泄露出去。也就是说，这类事件的本质，不只是“模型答错了”，而是模型交互链路本身正在成为新的数据泄露通道。

**二**

**企业为什么很难靠人工兜住这类风险？**

在企业场景里，这类问题之所以难处理，核心在于三个现实矛盾。

**一是输入来源越来越复杂。**

企业的AI应用不只处理用户主动输入，还会读取表单、知识内容、业务记录、外部评论等多种上下文。内容越多，其中的隐藏风险越难靠人工提前识别。

**二是风险可能同时出现在输入侧和输出侧。**

输入侧的问题是恶意提示词被带入模型，输出侧的问题则是敏感数据、不合规内容或不当结果被返回。只盯住其中一侧，往往不够。

**三是很多企业缺少统一治理能力。**

当多个模型、多个业务系统并行接入时，如果没有统一接入、统一审核、统一日志，出了问题之后很难快速判断：是哪次调用触发的？是哪条策略没拦住？是输入有问题，还是输出有问题？

**三**

**大模型应用防火墙，补的就是这一层能力**

这也是大模型应用防火墙存在的意义。

它不是传统意义上的Web防火墙，也不是单点内容审核工具，而是部署在业务系统与上游模型之间的一层安全控制与治理体系。它要做的，是把原本分散、不可见、难追溯的模型调用过程，纳入统一接入、统一审核、统一记录和统一管理。

先看一张图，更容易理解它在整条链路中的位置：

![1.png](https://mmbiz.qpic.cn/sz_mmbiz_png/TFxibKqzXJXJwyibqHTwJZ4rkDiawtSRPDSk5nibIrVicCl4lUlib7gk8GFRXe6hVqE43HWKEqNbtwtKRa6erKLmmLDnushK0Yg50QrPfBsShb6ZY/640?wx_fmt=png&from=appmsg)

图1：观安观御大模型应用防火墙系统位于业务系统与上游模型之间，提供统一接入、审核控制与审计追溯能力

如果对应到这次“提示词注入导致企业数据外泄”的事件，观安观御大模型应用防火墙系统主要可以在三个环节进行干预：

**1. 在输入侧识别提示词风险**

对于用户输入、外部表单、上下文内容中的异常提示词，平台可通过提示词注入检测进行识别与控制，降低恶意指令进入模型的风险。

**2. 在输出侧检测敏感信息与内容风险**

即使输入表面上看是正常内容，模型输出结果仍可能泄露企业敏感数据或不符合要求的内容。平台支持内容价值观审核、敏感数据检测，可以在结果返回前提供统一审核机制。

**3. 在治理侧统一留痕与追溯**

对于企业来说，真正难的往往不是发现一次风险，而是长期管理和事后复盘。平台通过审核记录、访问日志、登录日志和监控看板，对每一次调用实现留痕，帮助用户进行问题定位、风险追溯和策略优化。

下面这张图，可以更直观看到平台如何对不同审核策略进行统一配置：

**![2.png](https://mmbiz.qpic.cn/sz_mmbiz_png/TFxibKqzXJXL8DtjcyP1svVZLLXhUExuBf8QjkzrG3bQJCByGrWE66BKNst2Tqs7AEZvcCMqNDEjq0Jzia6HNP291iaaz48J4QNe99iauKCgJMo/640?wx_fmt=png&from=appmsg)**

图2：平台支持对提示词注入检测、内容价值观审核、敏感数据检查等策略进行统一配置

**四**

**除了“能防护”，企业还会问怎么落地？**

真实项目里，企业关心的往往不只是“能不能防”，还会进一步问：

**能不能快速接入？会不会带来很重的改造负担？部署方式灵不灵活？**

观安观御大模型应用防火墙系统提供了两种部署模式：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/TFxibKqzXJXKQ1V408rbhcyxPLJVj57ib95Qaia4Aic8miaeBdghKnFSbtibhibz7YvlqCcrbdX6d78PmqKmnB1K0VRuny2fX3icNFoClCVNrYs9iayI/640?wx_fmt=png&from=appmsg)

**托管代理模式：**由平台统一托管上游模型地址、调用密钥和模型标识，业务系统通过平台统一调用模型能力，适合希望统一接管模型安全链路的场景；

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/TFxibKqzXJXJ288gHYkicyGtl7ibBZUW7T6QFNUl9cUSYlwiaicHpv4jyUhzpsOuXGVibMsmy5axmK3QLA5FrdvlYNC6iaZ9Fq1OheqIyRtuNoYJib8/640?wx_fmt=png&from=appmsg)

**接口调用模式：**平台以独立审核接口提供能力，由业务系统按需调用并自行执行后续处置，适合已有模型网关或既有调用体系、希望平滑集成安全能力的场景。

这意味着，企业不一定需要推翻现有系统，而是可以根据现网条件，选择更合适的接入方式。

**五**

**从“能用”走向“可控、可审、可运营”**

这次Copilot Studio和 Agentforce的安全事件提醒企业一个越来越明确的事实：

当大模型越来越深地进入真实业务，提示词注入、敏感数据外泄和治理失控，已经不再是理论风险，而是企业必须面对的现实问题。

从“把模型接进来”，到“把模型管起来”，企业真正缺的，往往不是再多一个接口，而是一种能够建立安全边界、统一治理规则、保留审计证据的控制能力。

观安观御大模型应用防火墙系统，正是围绕这一目标进行设计，希望帮助企业把大模型应用从可用推进到可控、可审、可运营，在保障业务创新效率的同时，守住生成式AI 落地的安全边界。

![](https://mmbiz.qpic.cn/mmbiz_gif/DXJBkGBzRzHV8ibPXY7ibTck5C3e7GYxQYPoicprEnwPJbibgeBnHYLMibbAYBGC3jicywvCicKpTwKKIJia3VG9JPjDPQ/640)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/DXJBkGBzRzFUjgxYzWzYYAosaDJrlFe79Wic8icjicNORau9IkMz7heFZiaXPkjzBCdywIya3od2iaCHkpJf4xgJMRw/0?wx_fmt=png)

观安信息

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/DXJBkGBzRzFUjgxYzWzYYAosaDJrlFe79Wic8icjicNORau9IkMz7heFZiaXPkjzBCdywIya3od2iaCHkpJf4xgJMRw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过