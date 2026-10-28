---
title: 工具推荐|解放双手系列，一个管模型，一个研究安全边界，重点是开源的(Magpie+dsh-purge)
url: https://mp.weixin.qq.com/s/vMbHmWY0dMddzu1x1TnIgw
source: Doonsec's feed
date: 2026-10-27
fetch_date: 2026-10-28T07:43:38.539682
---

# 工具推荐|解放双手系列，一个管模型，一个研究安全边界，重点是开源的(Magpie+dsh-purge)

# 工具推荐|解放双手系列，一个管模型，一个研究安全边界，重点是开源的(Magpie+dsh-purge)

原创

小白哥
小白哥

小白安全成长记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

最近 AI Agent 相关的开源项目越来越多，除了模型本身，**模型管理、Agent 运行环境以及安全边界**也开始成为值得关注的问题。今天推荐两个比较有意思的项目：**Magpie** 和 **dsh-purge**。它们关注的方向不同，但都和 AI Agent 的实际使用与安全有关，折腾一下也挺有意思。

---

## 01Magpie：统一管理你的 AI Agent 模型

![](https://mmbiz.qpic.cn/mmbiz_png/Ueoom4Tb3S9QCba5C6YlkSJFkVeydriaiciaw38G9INgAd86Mw8g6UshGEchSCPFv5sGnZiaVfgWDcuRk6XmtmKdLX5hs1QXmoX9AzDJLwzyzQo/640?wx_fmt=png&from=appmsg)

如果电脑上同时使用 Claude Code、Codex、Gemini CLI、OpenCode、dsh 等工具，应该都会遇到一个问题：每个 Agent 都有自己的模型配置。想换模型、换 API Provider，或者多个模型之间进行切换，经常需要修改不同 Agent 的配置。Magpie 的思路很简单：在 Agent 和模型之间增加一个统一的 Gateway。这样可以把不同 Agent 的模型请求集中管理，并支持 OpenAI、Anthropic、Gemini 等不同协议。更方便的是，可以根据自己的需求进行模型路由。例如让不同 Agent 使用不同模型，也可以配置多个 Provider，在某个模型额度用完后切换到其他模型。除此之外，Magpie 还提供了 Privacy Masking，可以在请求发送给模型之前，对 API Key、密码等敏感信息进行脱敏。如果你平时经常使用多个 Coding Agent，或者需要频繁切换不同模型，Magpie 是一个值得尝试的工具。
我用的比较多就是脱敏和多账号，太爽了，以前用cc switch,但是它不能多账号。

---

## 02dsh-purge：从 Harness 层研究 AI Agent 安全

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ueoom4Tb3Sib9nKKIEW7Cx0KsVgOibKD89qI4qsJF1DLfN2otpXWNw2R30Oe0e2K06O8jiaN4tn9ZSyUHhia9QzVuibTRGjDFjmlKW8ONRkHibvSg/640?wx_fmt=png&from=appmsg)

相比 Magpie，dsh-purge 更偏向 **AI 安全研究**。它主要针对 DeepSeek Harness 进行安全研究，关注的并不只是“模型能不能被 Jailbreak”，而是进一步研究：\*\*Agent 本身的限制到底来自哪里？\*\*一个 AI Agent 除了模型之外，还可能存在 Prompt、Harness、权限控制、工具策略等多层限制。因此，当 Agent 拒绝执行某个操作时，未必意味着模型本身拒绝了，也可能是 Agent 的运行环境进行了限制。dsh-purge 提供了相关 Patch、Rule Sets、Skills 以及安全测试能力，可以用于研究 Harness 的行为和安全边界。对于关注 **AI Agent Security、Jailbreak、Prompt Injection、Agent Runtime Security** 的安全研究人员来说，这个项目比较值得关注。当然，这类工具涉及的能力比较敏感，应仅在自己管理的环境或获得明确授权的测试环境中使用。
这个就不用多说了，大家常说的破甲类工具，关键时刻一击毙命！最烦气大模型磨磨唧唧的，牛马的时间比较宝贵。

---

## 03我为什么推荐这两个项目？

这两个项目其实代表了 AI Agent 的两个不同方向。\*\*Magpie 更偏“怎么把 Agent 用得更方便”。\*\*它解决的是模型管理、Provider 切换、请求路由以及敏感信息保护等实际问题。**dsh-purge 更偏“怎么理解 Agent 的安全边界”。** 它关注的是 Harness、策略以及运行环境对 Agent 行为产生的影响。如果你最近正在折腾 **Claude Code、Codex、DeepSeek、Gemini CLI 等 AI Agent**，Magpie 可以作为一个模型管理工具体验一下。如果你更关注 **AI Agent 安全、红队测试和 Harness Security**，那么 dsh-purge 值得深入研究。
两个项目的定位不同，但放在一起看，也能看到一个越来越明显的趋势：

> **AI Agent 的竞争已经不只是模型能力的竞争，围绕 Agent 的基础设施和安全体系同样值得关注。一流agent + 一流的大模型才能大力出奇迹，当然你要想用的爽，这两个工具我认为如虎添翼，值得一试。**

**项目地址：**

* Magpie：

  github.com/yetone/magpie
* dsh-purge：

  github.com/YuJunZhiXue/dsh-purge

Deepseek harness 插件市场链接直接安排给大家，好多插件直接在市场里找就可以，时间是宝贵的。

* https://dshfind.com
* https://dshmarket.com
* https://awesome-dsh-plugin.com
* https://dsh-plugin.org

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EhWx22VKFBg0hrB58Q3PaRC6G2rPMW7pruxicEKOicpBXrickYY3FNnkPwknibIgaEH9dTVfhpAiafhHkhkZ7O8iaeNQ/0?wx_fmt=png)

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