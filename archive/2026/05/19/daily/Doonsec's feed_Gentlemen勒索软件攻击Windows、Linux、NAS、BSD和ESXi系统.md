---
title: Gentlemen勒索软件攻击Windows、Linux、NAS、BSD和ESXi系统
url: https://mp.weixin.qq.com/s/xLoBkG-XEr09C6PzAdq3PQ
source: Doonsec's feed
date: 2026-05-19
fetch_date: 2026-05-20T06:00:59.968975
---

# Gentlemen勒索软件攻击Windows、Linux、NAS、BSD和ESXi系统

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7MEkhJibcDgwFDPRktmxdhnoib4e0yr99uC2e1icnN9b1oIauaVQjNr29rNSVH5Bj3ngfCOqpucNPricdFuZCrnEjj0SvhTsyicF23c/0?wx_fmt=jpeg)

# Gentlemen勒索软件攻击Windows、Linux、NAS、BSD和ESXi系统

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

自 2025 年下半年公开出现以来，Gentlemen 勒索软件行动已迅速成为最活跃、最具可扩展性的网络犯罪威胁之一。

The Gentlemen 的突出之处在于它能够针对各种企业系统，包括 Windows、Linux、NAS、BSD 和VMware ESXi 环境。

这一传承表明，该集团受益于成熟的基础设施、经验和附属网络，使其能够在 2026 年迅速崛起。

这种跨平台能力使攻击者能够最大限度地造成破坏，尤其是在虚拟化基础设施中，攻破 ESXi 服务器可能会影响整个数据中心。

事件中观察到的攻击链包括利用暴露的远程服务、凭证泄露以及滥用 VPN 或防火墙访问。

Levelblue 的安全研究人员评估认为，该组织并非完全是新成立的，而是先前勒索软件关联活动的延续，与麒麟生态系统和一位名为“hastalamuerte”的俄语行为者有关联。

一旦入侵成功，攻击者会进行网络侦察、提升权限、关闭安全工具，并在整个域内部署勒索软件。数据窃取是核心步骤，强化了该组织双重勒索策略。

## **勒索软件即服务模式**

The Gentlemen 采用结构化的勒索软件即服务 (RaaS)模式，并配备专门的联盟营销平台。据报道，该后端支持有效载荷生成、勒索信定制、受害者追踪和谈判管理。

关联方也可能使用 Tox 或 Session 等外部通信工具，这使得事件跟踪变得复杂。

该组织的勒索信通常名为“README-GENTLEMEN.txt”，随附加密文件，这些文件使用“.7mtzhh”或其他随机变体等扩展名。

据报道，该恶意软件本身是用 Go 语言编写的，并且在执行时需要密码参数，这有助于关联方控制部署并逃避自动分析。

加密采用混合模型，较小的文件完全加密，而较大的文件分块部分加密，以加快加密速度。

在加密之前，恶意软件会终止与备份、数据库和企业应用程序相关的服务，以阻碍恢复。

截至 2026 年 5 月，“绅士”组织在其泄露网站上声称已有 352 名受害者，使其成为全球最活跃的勒索软件组织之一。

然而，事件响应数据显示，实际受攻击的组织数量要高得多，超过 1500 个环境显示出相关活动，但这些活动从未出现在公共泄露网站上。

该集团的目标行业范围广泛，其中重点领域包括：

* 专业服务（18.8%）。
* 制造业（17.9%）。
* 技术（11.6%）。
* 医疗保健（8.8%）。

从地域上看，业务遍及 70 多个国家，其中亚太地区 (28.7%)、欧洲 (28.4%) 和美洲的份额最大。

美国在国家层面位居榜首，其次是泰国、法国和巴西。值得注意的是，俄罗斯和独联体国家不在榜单之列，这与典型的勒索软件攻击目标模式相符。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7OibJlQua2Y4bT4veDXMdVZR6tVqKPkD4mmFTSsBWAFiaR6j02GbjEbb8s14SFCHF6r1uF8uzrB0ibBKf5zlYyhH90vwOq0HnGoKE/640?wx_fmt=png&from=appmsg)

数据窃取在“绅士”（The Gentlemen）勒索软件的运作中扮演着核心角色。窃取的数据会通过泄露网站和潜在的转售行为向受害者施压。

最近，一些地下论坛声称有与该组织有关的数据以约 10,000 美元的比特币价格出售。

威胁行为者分享的一些样本似乎包含敏感信息，例如凭证文件、内部聊天记录和受害者数据映射。在一个案例中，样本中还发现了对先前已知的受害组织的引用。

然而，研究人员提醒说，这些说法仍未经证实，应被视为情报线索，而不是已确认的对该组织基础设施的入侵。

The Gentlemen 的崛起反映了勒索软件行动的更广泛趋势：联盟驱动的规模、对被盗凭证的依赖以及对暴露基础设施的利用。

风险不仅限于加密，还包括数据泄露、监管后果和声誉损害。

例如，即使制造公司在遭受攻击后从备份中恢复了系统，被盗的设计文档或财务记录仍然可能被泄露或出售，从而造成长期的业务影响。

建议各组织优先保障远程访问服务的安全，强制执行多因素身份验证，监控特权帐户，并确保具有弹性和隔离性的备份。

检测策略应侧重于攻击者在勒索软件部署之前，进行异常的管理活动、横向移动和数据暂存等早期行为。

随着绅士帮不断扩大其业务规模，其技术能力和附属机构驱动的扩张相结合，使其成为一个持续且不断演变的全球威胁。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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