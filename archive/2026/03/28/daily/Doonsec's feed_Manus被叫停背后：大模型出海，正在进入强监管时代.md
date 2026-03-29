---
title: Manus被叫停背后：大模型出海，正在进入强监管时代
url: https://mp.weixin.qq.com/s/tliuN0jF6ce4gVnQdWqK4w
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:31:53.124355
---

# Manus被叫停背后：大模型出海，正在进入强监管时代

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibRSkqHWDIlWJicoCTXDWc8sNBpDy7eeK3DvqRstm0mlzRWibykZajUaHqUo8gXhYTjicwbDf9lSr13Eat21o7QzNbEAGZe7GCnfpk/0?wx_fmt=jpeg)

# Manus被叫停背后：大模型出海，正在进入强监管时代

原创

兰花豆
兰花豆

兰花豆说网络安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/AiaxibnzDXa1asshEnCgBMF2CiayVQfx8e9XK6C8MH2YkouAoA6DRk6ibnPNQ3eSY4Ejfibh8hy8tOGNLnVoicJlWnIg/640?wx_fmt=gif&from=appmsg)

# 一、突发事件背后，一个值得关注的信号

近日，关于“Manus创始人被限制出境、相关收购被叫停”的网传消息，引发了业内广泛关注。

从表面看，这似乎只是一次常规的跨境并购审查。但如果从更深层观察，这一事件更像是一个信号：

监管关注的重点，正在发生变化。

过去，更多聚焦在“数据是否出境”；而现在，正在逐步转向：

能力是否出境。

在大模型与智能体快速发展的背景下，这一变化，对所有计划“出海”的AI企业而言，都值得认真对待。

## 二、一个常见误区：模型出海 ≠ 数据出境？

在实际交流中，很多从业者都有一个共识：

模型只是训练后的参数，并不包含原始数据，因此不属于数据出境。

这句话并不完全错误，但并不完整。

从监管视角看，大模型具有一些特殊属性：

●  参数本质是数据的统计压缩表达

●  模型可能“记住”部分训练数据（尤其是小样本或敏感数据）

●  存在被攻击利用的可能，例如：

模型反演（Model Inversion）

提示注入（Prompt Injection）

数据抽取攻击（Data Extraction）

换句话说：

模型本身不是数据，但它承载了“数据的能力”。

而监管真正关注的，往往是：

这种能力，是否可能被境外利用。

## 三、为什么相关AI交易会被叫停？

从合规角度来看，此类事件通常涉及三类核心风险。

### 1. 技术出口风险：AI能力的“类军工化”趋势

依据《出口管制法》，部分技术能力可能被纳入管控范围，例如：

●  核心算法与模型架构

●  智能体调度与自主执行能力

●  网络攻防相关能力

在AI时代，这些不再只是软件功能，而更像是：

具有战略价值的数字基础设施能力。

一旦向境外输出，可能被认定为技术出口行为。

### 2. 数据安全风险：模型成为“数据载体”

在《数据安全法》《个人信息保护法》的框架下，监管重点不仅是：

●  数据是否出境

还包括：

●  数据价值是否外流

典型风险包括：

●  模型基于国内敏感数据训练（政务、电信、金融等）

●  模型可被诱导输出特定信息

●  模型行为体现国内数据特征

本质上：

模型成为了数据的一种“变形存在”。

### 3. 控制权风险：AI资产整体外移

在收购场景中，问题会更加复杂：

●  模型控制权转移至境外主体

●  推理数据与用户日志流向境外

●  后续训练数据来源不可控

这不仅是技术问题，更涉及：

数据主权 + 技术主权 + 平台主权 的叠加风险。

## 四、哪些场景需要重点关注合规问题？

在实际业务中，以下几类场景建议重点进行合规评估：

1. 国内数据训练 + 海外提供服务

→ 最典型的风险场景

2. 模型权重/参数向境外提供

→ 本质上属于能力输出

3. 跨境API调用（数据参与再训练）

→ 用户数据可能被二次利用

4. 具备自动数据采集能力的智能体

尤其是具备自主执行能力的Agent

5. 涉及敏感行业

政务

电信

网络安全

金融

可以简单理解为一句话：

只要模型使用过国内数据，同时服务海外用户，就需要认真评估合规风险。

## 五、从网安视角看：风险不止于合规

相比合规问题，从网络安全角度看，大模型出海还存在更隐性的风险。

### 1. 模型被“套取数据”

攻击者可以通过：

●  精心设计提示词

●  多轮对话诱导

逐步获取：

●  训练数据片段

●  内部知识结构

●  敏感业务逻辑

在开放的海外环境中，这类风险更容易被放大。

### 2. 智能体被“利用执行攻击”

对于具备工具调用能力的Agent系统：

攻击者可能通过：

●  注入恶意任务

●  绕过安全策略

●  利用工具链执行操作

其本质是：

将AI转化为“攻击执行代理”。

### 3. 模型成为“情报入口”

在以下场景中尤为典型：

●  免费工具推广

●  SaaS平台

●  API开放服务

用户可能在不经意间：

●  上传敏感文件

●  输入业务数据

●  提供内部信息

如果数据流向不可控，就可能演变为：

一种新型情报收集渠道。

## 六、企业如何更稳妥地推进出海？

结合当前趋势，可以从五个层面进行系统化设计。

### 1. 数据层：分域治理

●  国内数据 → 仅用于国内模型

●  海外数据 → 本地采集、本地训练

核心目标：避免数据混用。

### 2. 模型层：能力分级

●  通用模型：可出海

●  行业模型：限制出海

●  敏感能力：禁止出海

核心思路：对“能力”进行分层管理。

### 3. 部署层：本地化架构

●  在海外部署推理节点

●  尽量避免跨境调用国内服务

核心目标：降低数据跨境流动风险。

### 4. 安全层：模型防护体系

●  Prompt Injection防护

●  输出内容安全过滤

●  模型行为审计

●  数据泄露检测

建议将大模型视为“高风险系统”进行防护。

### 5. 合规层：前置评估机制

重点关注：

●  是否涉及重要数据

●  是否触发数据出境评估

●  是否涉及技术出口

核心原则：

不要等问题发生后再处理。

## 七、一个趋势判断：AI出海将进入强监管阶段

结合当前政策与行业发展，可以做一个相对审慎的判断：

未来几年，可能会逐步出现以下趋势：

●  AI模型纳入出口管制体系

●  智能体系统进入安全监管范围

●  数据跨境规则进一步细化

●  行业分级管理逐步落地（类似等保体系）

从更宏观的角度看：

AI能力，正在成为类似数据与芯片的重要战略资源。

## 结语

Manus事件本身或许只是一个个案，但它所反映的趋势，值得整个行业重视。

在AI快速发展的同时：

●  技术能力在增强

●  风险边界在扩展

●  监管逻辑也在同步演进

对于企业而言，“出海”不再只是市场问题，也不仅是技术问题，而是：

技术、数据、安全与合规的系统工程。

在这个过程中，走得快很重要，但走得稳，可能更重要。

END

了解更多知识，欢迎关注ima知识库

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ribStUdgfRibTwTWfbPWbuznxMApccY8gaLLMynbNCYDurCmPsc2xicfVX0qzbPWBTt1CGcq0ysT2edD95xeETBRkbFxgoZd7N2AhhC7z3aOoM/640?wx_fmt=png&from=appmsg)

推荐阅读

[AI时代，为什么说Skills是未来？](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492776&idx=1&sn=c45810dd9ab2f00844b5e3cd0d08a89a&scene=21#wechat_redirect)

2026-03-27

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibQgEg9Jm9tOlibuqpWfStrOS326dCZiak9Xzib9sLep3Ulpus58z6W2Sshr3FNtsrxkVV4UZFa08tBCSMPQWAZA99bibTdHkGYZElA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492776&idx=1&sn=c45810dd9ab2f00844b5e3cd0d08a89a&scene=21#wechat_redirect)

[谨防国外情报机构通过新型AI工具收集情报](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492757&idx=1&sn=b86f1c70208768e8269727fad4e28088&scene=21#wechat_redirect)

2026-03-17

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibQ1O3tZDtMM1ibrGzvxccCRu8PJDVcQQ6XIOs3wJzbsfZCIxs65eckCN9pibmO2XV3BlBr4OKSk8YVBmFCRzWG6H1nJ6icyF7EKTo/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492757&idx=1&sn=b86f1c70208768e8269727fad4e28088&scene=21#wechat_redirect)

[从SEO投毒到GEO投毒：AI时代的新型网络攻击](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492748&idx=1&sn=453b52eaba8c34f5675374b410032953&scene=21#wechat_redirect)

2026-03-16

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibR9gtiasJfRSiceiahicxToH8UBIFLnog1xHibpKNSFCHwPoBmAhCNuQhTsW2UUQuUXsCX7r2WbCMF2KHvhq00MIYibT9kLJ11ccz518/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492748&idx=1&sn=453b52eaba8c34f5675374b410032953&scene=21#wechat_redirect)

[十五五规划里的网络安全机会在哪里？](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492741&idx=1&sn=70ba67bfad6a41a469006e8d43f0b8b4&scene=21#wechat_redirect)

2026-03-14

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibT9lfHoZ7icDHsBkIMLPhI23eqicRibgYYCJ4IZkwoic8auiarvicsoUQB91johctUtnmuRbiazPoWGr9UbWXoXrGrdE32JQVNTAic9JaE/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492741&idx=1&sn=70ba67bfad6a41a469006e8d43f0b8b4&scene=21#wechat_redirect)

[养“龙虾”的现实与困境：从小龙虾养殖谈到OpenClaw的安全边界](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492736&idx=1&sn=8c0817afe1d8aa29346c34907fa9cf5c&scene=21#wechat_redirect)

2026-03-13

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibShWooXSqhHOyCzfMKDe6CmMsVSTfAZc6przky2d33TG7xiaFXQleOtLiakdF6hlv6jJ6LYBeAOQ6aVkD6MIMJV58SV7sicXGFPnA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492736&idx=1&sn=8c0817afe1d8aa29346c34907fa9cf5c&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/AiaxibnzDXa1Y7uRicSTtCequUrbj3R6CelD6j6kTdgeaBdywoCOdImg0P7WnB8zQTYveOJzTzHtSely8qFvufmiaA/0?wx_fmt=png)

兰花豆说网络安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/AiaxibnzDXa1Y7uRicSTtCequUrbj3R6CelD6j6kTdgeaBdywoCOdImg0P7WnB8zQTYveOJzTzHtSely8qFvufmiaA/0?wx_fmt=png)

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