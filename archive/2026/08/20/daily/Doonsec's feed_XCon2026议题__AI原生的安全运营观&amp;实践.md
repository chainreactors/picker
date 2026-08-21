---
title: XCon2026议题||AI原生的安全运营观&amp;实践
url: https://mp.weixin.qq.com/s/6Akz7mdJF0L5whP1TY7xVw
source: Doonsec's feed
date: 2026-08-20
fetch_date: 2026-08-21T02:59:41.291721
---

# XCon2026议题||AI原生的安全运营观&amp;实践

# XCon2026议题||AI原生的安全运营观&实践

嘶吼专业版

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/mibLibLia0X2icAGkHqLeTHuqooxNpxic666vhxkJZx0a6FKMVcxKCeB5SbWytQTg8ib50HrrksMclFRCpZ3W6aTeP1sKtYXWws2KILt0OsniaF6Ng/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

XCon2026||定义·未定义

安全运营中最让人头疼的，往往不是告警太少，而是告警出现之后，没人能马上说清楚：威胁到底意味着什么，将带来多大的风险和损失。

一条WAF告警可能只是自动化扫描，也可能是一次真实的漏洞利用；一条EDR告警看似指向恶意进程，背后却未必存在完整攻击链。每当告警出现，分析师往往需要把来自不同系统的线索放在一起，持续核对访问日志、进程执行、文件变更、登录行为和网络连接，才能判断攻击是否成功、攻击者走到了哪一步，以及影响范围究竟有多大。

这种调查方式在过去主要依赖分析师的经验和耐心。但当攻击者开始借助AI加速侦察、漏洞利用和攻击链编排，防守方如果仍停留在“告警触发—人工检索—逐条确认”的模式，面对的将不只是告警数量的增加，而是调查效率与攻击速度之间差距的持续扩大。

在8月28日即将启幕的XCon2026大会现场，虎符网络创始人、安全焦点（XFOCUS）核心成员王伟（alert7）将带来议题《AI原生的安全运营观&实践》的分享。从真实安全运营中的调查困境出发，讨论 AI 如何进入告警确认、攻击溯源和风险识别流程，以及支撑这些能力的安全数据、证据链和工程体系应当如何建设。

01

议题简介

过去多年，企业陆续建设了SOC、SIEM、态势感知、WAF、EDR、NDR、HIDS、堡垒机、数据库审计等系统，安全检测能力不断完善。但在真实事件处置中，分析师依然需要在多个平台之间反复切换：从一条WAF告警追到Web 访问日志，再关联DNS、认证、主机进程、命令执行、文件变更和网络连接。

调查过程中，字段语义不统一、日志采集不完整、资产关系不清晰、IP与主机无法准确映射等问题十分常见。安全产品告警能够提示“可能存在风险”，但要进一步确认攻击是否成功、攻击者是否落地、有没有横向移动，以及影响范围究竟多大，仍然需要大量人工取证和交叉验证。

因此，仅仅把告警接入SOC或SIEM，再增加一个大模型问答入口，并不等于 AI原生安全运营。AI如果只能读取告警摘要，就只能停留在“解释告警”的层面；如果无法理解数据源、调用证据、关联实体、识别数据缺口，就很难参与真正的调查与溯源。

本议题提出的 AI 原生安全运营观，是将安全运营从“告警中心”转向“安全数据注册与证据调查中心”。通过提前为AI准备可理解、可获取、可关联、可复核的数据资产，把告警、日志、主机、账号、网络、进程、文件、连接等对象组织为可调查的证据空间，让AI在真实证据链之上完成规模化取证、关联分析与报告生成。

02

议题亮点

* **亮点一：一针见血地戳破建设幻觉**

  "把告警接进SOC，就算完成了 AI 数据准备"——这是普遍误区。WAF、IDS、NDR、EDR 的告警只能告诉你"可能有问题"，却回答不了"攻击是否成功、是否落到主机、有没有横向移动和外联"。**碎片不是证据链。**
* **亮点二：把"判断题"重做成"证据题"**

  议题给出告警确认的三层证据法——告警本体（为什么报）、原始日志上下文（有没有打进去）、攻击链后续（影响到哪里）。alert-confirmation Skill 输出的不再是一个冷冰冰的verdict，而是结论、置信度、支持证据、反证点、已关联证据边、缺失数据源与下一步建议。
* **亮点三：攻击链是 Join 出来的，不是画出来的**

  溯源调查强调"从锚点拓线"而非全量检索。一条有价值的join edge必须回答清楚：用什么字段关联、时间窗口多大、是强关联还是弱关联、有没有替代解释。**追不到证据的攻击链图，只是一张漂亮的 PPT。**
* **亮点四：data\_gaps 与 verdict 同等重要**

  **不是所有调查都必须给出确定结论，但所有不确定结论都必须说清缺什么证据。数据缺口不是调查的遗憾，而是下一轮采集治理与检测优化的输入——这正是"复利式运营"的引擎。**

议题还将结合 **SecWeaver**平台，拆解 DataAsset / Connector / Correlation Matrix / Scenario Pattern / Skill / Case Memory 的工程化分层，并厘清落地边界：**站在安全设备之后而非取代设备、控制大模型使用位置而非全量灌日志、专家经验要产品化而非停留在提示词里。**

03

演讲人介绍

![图片](https://mmbiz.qpic.cn/mmbiz_png/mibLibLia0X2icAPBCaNpBYNcAdXrCHRC6szw3FzsoIO38NjI1L0R0TyLbFfA02XVamSBRp9Z40tdtdXC4ibfpMcPheibolPOCFTrFTXtRg6M3iaTs/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

王伟（alert7）——虎符网络创始人&安全焦点（XFOCUS）核心成员

20多年资深安全专家，从2000年开始，陆续公开研究成果《非安全编程系列》，《Linux kernel exploit研究和探索》等二十余篇，2005年和XFOCUS核心成员共著《网络渗透技术》，独立发现并上报上百个高危级安全漏洞，获得腾讯，阿里，Oracle，Adobe，QuickTime，Linux等一厂家的多次致谢。

参与国家重大项目建设：如863（Linux内核加固）项目，主持国家242课题等。帮助政府抵御多起APT攻击，国内首次捕获利用国内软件0day漏洞针对政府部门的 APT攻击事件（被命名为穷奇），引起国家高度重视。深入研究诈骗、薅羊毛等场景中的技术手段并进行技术攻坚。在反诈场景，协同公安32个反诈中心，仅2019年保护10万多消费者。被“国务院联席办”和公安部高度赞扬。

目前虎符网络希望以零信任理念重塑企业新安全，为了解决应用能否不被黑客攻击的问题，第一道防线核心理念是所有的企业应用统一网关/入口（隧道/WEB），做统一暴露面收口和应用安全发布管控，形成了零信任1.0（零信任VPN），零信任2.0（WEB统一收敛），零信任3.0体系（内外网统管）。

**XCon2026售票通道现已全面开启**

**【体验票】****¥0元**，含：分会场+展商互动区

**【学生票】****¥398元，**XCon2026全场通——含：主会场＋分会场+展商互动区

\*特别说明：购买学生票，现场验票时，须出示有效期内学生证。如无法提供有效证件，需按普通票补齐票价

【学生票】团购专项 2张享9折、5张享7折

10张享5折

**【普通票】****¥2790元，**XCon2026全场通——含：主会场＋分会场+展商互动区

【普通票】团购专项 5张享7折、10张享5折

![图片](https://mmbiz.qpic.cn/mmbiz_png/pX30G7omHPotGkiaeRRrfOzpuCIwiaftAr1SRAl0iaELpsPlKnIwEicnic0JwWkFTibSJ7Ttve2eX6PRSKc4Z7mbtMxQ/640?wx_fmt=png&wx_lazy=1&wx_co=1&wxfrom=5&tp=webp#imgIndex=1)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/mibLibLia0X2icBZxXhdgjOf3JPQtmL3cJfz76zBiaM5C2VbG02MerXBzdjNmpSq2DVlJDDjImXYmaLm0eJaNOeiaY8UV90k5bUhplVkjMr7P3LP4/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=4)

微信号：XConXFocus

预览时标签不可点

内容含AI生成图片

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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