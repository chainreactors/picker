---
title: Orchid Security安全报告：三分之二非人类账户处于失控状态
url: https://mp.weixin.qq.com/s/GVifbQVIRaUKllhtv3RFOw
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:34:15.981727
---

# Orchid Security安全报告：三分之二非人类账户处于失控状态

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3VBp2tLiazADzRs1eeUT7Q5B2q7U96PHrL1FCjZknYhYGgLUx7F1P2X9nKk4SeLiaxlhEDLmRzhGRNwyvHHAckOd0yzs050zy3U/0?wx_fmt=jpeg)

# Orchid Security安全报告：三分之二非人类账户处于失控状态

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX1t3c5g3n2TibgVG1fbFAahRNG9P4LD7tgbQAVvK3KRiayHCIyIcH300FM3hiblExibd6Pf7tNzyH2FFL9FZofSbOXUOJdf22y7Ohk/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3ZpYyW62XV71uvxic3ibibfZHWtVEgBX0XUiclOcmN5DxE18ms2hXiaE4V1lhf8P4nRLTicNtpYUgKdrDWNFPD7PicdKrzlicFe99T1Ow/640?wx_fmt=jpeg&from=appmsg)

致力于解决核心身份安全问题的Orchid Security 今日发布《身份鸿沟：2026年现状报告》，揭示当前大多数企业身份信息实际游离于身份与访问管理系统（IAM）的监管范围之外。

报告发现，企业环境中不可见身份（"身份暗物质"）占比已达57%，远超43%的可见身份比例。更值得警惕的是，67%的非人类账户直接在应用程序内部创建，完全脱离IAM系统的管理视野。

这一发现正值关键时期——企业正在快速部署AI Agent，而这反过来又加剧了身份暴露风险。传统IAM系统本是为管理人类身份而设计，根本无法应对那些继承凭证、自主行动且常在身份暗物质盲区运作的自治系统。

其他重要发现包括：

* 70%的企业应用存在特权账户泛滥现象，极大增加了滥用或入侵的潜在影响
* 57%的应用绕过集中式身份提供商进行认证
* 40%的账户沦为"孤儿账户"，在原始用户离开后仍保持可用状态
* 36%的凭证以明文形式硬编码在应用程序中

Orchid Security CEO兼联合创始人Roy Katmor指出："企业身份已跨过危险临界点：不可见身份数量首次超越可见身份，这原本已是重大的安全与合规隐患。在AI Agent时代，它将演变为运营危机。AI Agent不会等待季度审计，它们实时跨系统行动，利用企业提供的任何访问权限。若企业无法洞察每个身份、理解其权限并管控其行为，就谈不上安全扩展AI应用。"

Part01

非人类账户：最危险时机的巨大盲区

现行非人类身份IAM模型始终存在风险：分析显示，67%的企业应用中，这类账户通常被授予本地长期宽泛权限，其理论基础是预设这些账户行为具有确定性和重复性。执行固定任务的机器、服务或机器人确实存在风险，但至少受代码限制。

然而，最新出现的AI Agent彻底改变了这一局面。虽然技术上属于非人类范畴，但AI Agent的行为既非预设也不重复。相反，它们会不可预测且持续不断地追求目标指令。放任其在监管盲区自主运行将带来巨大风险。

Part02

应用程序：过度授权、缺乏管理、漏洞百出

正式身份控制措施与实际访问机制间存在日益严重的脱节现象。尽管许多企业已通过集中式身份目录、身份提供商（IdP）强认证、特权访问管理（PAM）及日益完善的身份治理管理（IGA）来强化企业IAM系统。

但Orchid Security发现，这些控制措施经常被绕过。数据显示：近四分之三应用存在特权账户过多问题；超半数应用允许通过本地或非受管途径认证；三分之一应用直接在代码或配置文件中明文存储凭证。这些因素共同助长了非受管访问层（即"身份暗物质"）的扩张，持续侵蚀身份安全根基。

"企业在前门安全上投入巨大，但研究表明身份风险正日益集中于侧门：本地账户、非受管访问路径、硬编码凭证以及游离于正式控制之外的过度权限，"Katmor强调。

Part04

风险叠加："毒性组合"兴起

除个体暴露点外，报告还识别出被Orchid Security称为"毒性组合"的现象——多重身份漏洞叠加显著放大风险，包括：

* 具备高权限的孤儿账户
* 既绕过集中身份提供商又明文存储凭证的应用程序
* 无日志记录无监管的休眠账户

单独来看这些漏洞已令人担忧，当它们组合出现时，将形成完全不受监控的访问路径，极大提升系统沦陷的可能性。

Part05

核心结论：AI Agent加速身份暴露

随着企业加速部署AI Agent实现业务流程自动化，这些身份漏洞不仅数量激增，其可见性与可利用性也同步提升。为追求效率而生的AI Agent会本能地识别并利用最直接的访问路径——包括那些位于集中式IAM控制之外的路径，无论相关账户、凭证或权限是否本意供其使用。

"AI Agent以前所未有的方式和速度发现并利用身份控制漏洞，"Katmor表示，"只要环境中存在捷径，自治系统就必定能找到它。"

Part06

身份、意图与现实间的鸿沟扩大

研究结果表明，许多企业在实施AI Agent时，对其环境中的实际访问机制认知存在严重缺失——且往往毫无察觉。这种认知盲区阻碍了伴随AI Agent应用所必需的风险管理措施落地。若不先夯实企业身份基础（每个应用程序），企业将在机器规模上面临日益严峻的网络安全、合规及运营风险。

"身份治理方案在纸面上看似完善，但多数身份活动实际发生在体系之外，"Katmor指出，"那里才是安全、合规和AI风险真正滋生的温床。"

Part07

报告背景

《身份鸿沟：2026年现状报告》基于2025年4月至2026年3月期间从北美及欧洲部署的企业应用中收集的匿名遥测数据。数据覆盖金融服务、医疗保健、零售、制造及能源等行业，反映了企业环境中受管与非受管的身份活动情况。

参考来源：

Two-Thirds of Nonhuman Accounts Are Unseen and Unmanaged, According to Orchid Security’s Identity Gap Report

https://cybersecuritynews.com/two-thirds-of-nonhuman-accounts-are-unseen-and-unmanaged-according-to-orchid-securitys-identity-gap-report/

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0TPDSBGWyOrBX6roghTcfJ7S0Uk6LPc6NiazIJCibS6wTdC64AxlpIAv3YZ2LoZFsJy3UHwic3ohlaRGRMZkKBW03QD5AMj5yuicM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651338385&idx=1&sn=a442efc5bf8726e3e4239bc246e2976b&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2A30nW87bmYJO7PWcHicOLnjA5DRaqykn6a3r9Nvg2PUTX1XkGuXcekoXza0aIXeq8O4ZwnhjLdFba5NEv5NQetNb0KjM9Mnb8/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0Fbuz3XAGmQhRuTK99Goic02sOWxZnmAA9a47pEasicuDoSGOlFLZUKDwcp06t9zFIvOrhUyWJWCyGknlGA6gyTuGbx3p99EyJc/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1YQicmp7cUEdGRLrhzeHCT1dUVwdTibZB1gTKB9TuH4BYn9PyXP4t5xMMWMOLIibwsJIiasLnicq7VLXVON9PQ8e8IG17qGUyjPl7c/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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