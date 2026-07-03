---
title: Claude Fable 5全球解禁，7 天限时、额度减半
url: https://mp.weixin.qq.com/s/UQ0sjqi5sE8fSFKM5EB0qA
source: Doonsec's feed
date: 2026-07-02
fetch_date: 2026-07-03T05:46:10.075830
---

# Claude Fable 5全球解禁，7 天限时、额度减半

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3cz9MS8SZibU0XkXFc9epjZO8PToVI8nyDezwReicKTIg5vmIOnVNrtJ5VibzwcWs2Gu9bpKdiaiaV5WGiceA1nw9O5e5fE4icDWsEiao/0?wx_fmt=jpeg)

# Claude Fable 5全球解禁，7 天限时、额度减半

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX1IsCTD6VYeMLUAFptqUYGX3vn55IbFCpqo6rpiboMyuGJON1KgDgiadrcJLiarwXUt7FZPuadM4vUib5AKZYl0iaHCCyTjomARSEEU/640?wx_fmt=gif)

![文章配图](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2ia2W22YhddVRKJM33f9BhRHjXFbJoQic36ib8L5iaQKicXulgQ0Vd9AnEYVZlwFnaJ4GMUGaWGAmpwGbLB5avHvBDupOfApLr4MNc/640?wx_fmt=jpeg)

Anthropic 正在全球范围内重新上线 Claude Fable 5。6月30日，美国商务部解除了约两周半前对 Fable 及其管控更严格的姊妹模型 Mythos 5 实施的出口管制。

7月1日周三起，Fable 5 将重新面向 Claude.ai、Claude Platform、Claude Code 和 Claude Cowork 平台的用户开放。出口管制限制了技术的接收或使用对象。根据6月12日的命令，Anthropic 需切断所有非美国公民（无论身处美国境内境外，包括该公司非公民员工）对这两个模型的访问。

Part01

越狱事件触发紧急管制

管制令立即生效，由于公司无法实时核查每位用户的国籍，最终选择全面暂停两个模型的服务。事件导火索是研究人员发现的越狱（jailbreak）技术——即通过特定提示词使模型绕过安全规则。亚马逊研究团队在 Fable 5 中发现此类技术，据 Anthropic 描述，该提示词导致模型标记出若干软件漏洞，并在某案例中生成了展示漏洞利用方式的代码。

Anthropic 淡化了这一发现，指出相同请求在其 Claude Opus 4.8、OpenAI 的 GPT-5.5 和中国 Kimi K2.7 等性能较弱的模型上同样有效。公司称被标记的行为属于常规防御性安全工作，并非隐藏的超强能力。但美国政府与报告该越狱技术的合作方认为其严重性足以启动紧急管制。

Part02

安全升级与分级恢复

为解决隐患，Anthropic 训练了名为 classifier 的新型安全过滤器，可精准识别并阻断报告中提及的技术。截至6月30日的文件显示，该技术目前拦截成功率超过99%。被阻断的请求将转由较弱的 Opus 4.8 处理，并通知用户，代价是正常编码和调试场景可能产生更多误报。

基础架构相同但安全防护更少的 Mythos 5 仍受严格限制。6月26日起，约100家美国关键基础设施防护企业及联邦机构已恢复访问。Anthropic 表示正与政府协商扩大适用范围。

Part03

政企博弈与行业影响

签署解除令的美国商务部长霍华德·卢特尼克称，其部门与 Anthropic 进行了为期两周的模型审查。根据协议文件，公司承诺自主排查安全问题、协调未来产品发布，并上报发现的恶意使用行为。据报道，谈判由联合创始人汤姆·布朗主导，而非与政府长期存在分歧的CEO达里奥·阿莫代伊。

事件自始争议不断。《华尔街日报》等媒体指出亚马逊的研究及CEO安迪·贾西的担忧推动了初始禁令。前AI事务主管大卫·萨克斯指责Anthropic"将消费者模型服务置于安全之上"，也有人认为这是过度反应。悉尼大学AI治理研究员弗朗西斯科·巴伊洛向半岛电视台表示，政策逆转显示政府承认管制过当，此前已有安全专家联名要求解除禁令。

Part04

行业共性问题与监管困境

政企拉扯背后，本次管制事件暴露的矛盾并非 Anthropic 一家独有，而是整个高端大模型行业共同面临的监管难题。OpenAI 也曾遭遇同类风险顾虑：大模型具备攻防双重属性，既可辅助安全人员修补漏洞，也会被不法分子用来挖掘高危漏洞。出于管控考量，GPT-5.6 仅对经过政府审批的少量机构开放预览，并未全面面向公众上线。

这类安全威胁绝非理论假设。今年春季 Anthropic 测试早期 Mythos 模型时，该模型可根据指令挖掘主流操作系统、浏览器的各类 0Day 漏洞，其中甚至包含 OpenBSD 系统中存续 27 年之久的底层缺陷；红队测试人员仅需一天时间，就能把刚曝光的漏洞编译成可执行攻击代码。

眼下 Fable 5 虽已解除封禁，但根源性监管制度短板并未补齐。6 月 2 日落地的 AI 行政令仅搭建了前沿模型自愿预审机制，划定了受控模型的判定标准，却没有出台强制上线许可流程，本次解禁的 Fable 5 上线前就未经过官方前置审核。监管层面只能临时启用出口管制手段干预模型服务，足以说明美国现行体系缺少常态化、有约束力的前沿 AI 管控流程，应对新型大模型始终被动滞后。

Part05

**Fable 5限时7天，额度砍半**

监管层面的长效约束机制尚未成型，作为折中平衡手段，Anthropic 在放开 Fable 5 访问权限的同时，叠加了严苛的短期使用限制，通过限时、限额的方式平衡算力成本与安全风险。

官方发布博文《Claude Fable 5 promotional access》，出台两条面向所有订阅用户的硬性使用规则，也是开发者最为关心的实操政策：

## 规则一：仅开放 7 天限时体验窗口

活动周期自 7 月 1 日起，截止至太平洋时间 7 月 7 日 23:59:59。窗口期结束后，Fable 5 将不再纳入订阅套餐免费额度，想要继续调用只能充值用量积分按 Token 单独计费。其 API 收费标准为输入 10 美元 / 百万 Token、输出 50 美元 / 百万 Token，整体成本约为 Opus 4.8 的两倍。

## 规则二：每周套餐额度上限仅五成

所有模型共用一套每周额度池，Fable 5 最多只能占用每周总配额的 50%。举个直观例子：倘若本周使用其他模型已经消耗掉一半额度，那么剩余全部余量都可分配给 Fable 5 调用。并且所有窗口期内的可用额度必须在 7 月 7 日截止前消耗完毕，超时未使用的额度直接清零失效。

## 额度耗尽后的两种解决方案

若窗口期内套餐额度提前用尽，用户有两种选择：

1. 充值 usage credits 用量积分，采用单独付费模式持续使用 Fable 5；

2. 切换至 Opus 4.8 等其他模型，依托订阅套餐剩余额度正常开展工作。

这 7 天是所有订阅用户均可体验 Fable 5 的专属窗口期，时限有限，错过不再有套餐低价使用资格。

###

### 整体来看，限时限额只是现阶段平衡安全与使用需求的临时方案。在 AI 监管体系落地前，这类分级、限时开放模式或将成为高端模型上线常态。

参考来源：

Anthropic Restores Claude Fable 5 After U.S. Lifts Jailbreak-Linked Export Controls

https://thehackernews.com/2026/07/anthropic-restores-claude-fable-5-after.html

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX24B8SGpjtPNurWcSlpApNEFvAvemslibiaNDIP9r5rUpOOr7bldmoTgsRqBAho97xVeKrGPEh3CJHn55QqFCOKZOzMn3CAnUyC0/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651341548&idx=1&sn=bb9edaa490d92c0258ff47c5dd29faf4&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX01JzsmUwE4vIMgNU0wJMU6KQJl9dPmQiasQPhk4XicPz5E9aUGGrN6LLALlxxjew7Vks5QabJJwtkIffw9c4OwbItR1tY3qVRbc/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0UGcrYtIkSYDEgbDkib0yMF23VlKQibpJyRnibia1cD3no5XF7Je0Sic98ytMyvbY9LhO8tKoxBlnibsAXh8CnBTYoAxLReujuqjomI/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1cNPEia7j7bXCX8P8iaDo801yQlaF965NduoqX5nEfgC2mLLgM6VdzcRdkYkeGebHaia3JRK31e08ibfS1WnmYl8DtvPf83e6XW6k/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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