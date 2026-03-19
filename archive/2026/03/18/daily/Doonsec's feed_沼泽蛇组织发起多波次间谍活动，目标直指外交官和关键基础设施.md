---
title: 沼泽蛇组织发起多波次间谍活动，目标直指外交官和关键基础设施
url: https://mp.weixin.qq.com/s/FgpwsQZhOk7A4EMACUOS3g
source: Doonsec's feed
date: 2026-03-18
fetch_date: 2026-03-19T04:16:57.311707
---

# 沼泽蛇组织发起多波次间谍活动，目标直指外交官和关键基础设施

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7Os44PvVTX2zZRAR9j0aiaRtRVs5dlcsTXkERTnum4o4cWicQVPXdmvOhzn7IABYhgbUMwrzhukP8YPpSyIVAQicva1F8jDdFoDFw/0?wx_fmt=jpeg)

# 沼泽蛇组织发起多波次间谍活动，目标直指外交官和关键基础设施

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

一个名为“沼泽蛇”（Boggy Serpens，又名“MuddyWater”）的伊朗国家级网络组织，拥有雄厚的资源，大幅升级了其网络间谍活动，对外交使团、能源公司、海事运营商和金融机构开展了持续且有针对性的攻击活动。

该组织据称隶属于伊朗情报与安全部（MOIS），至少从2017年起就一直活跃，但其近期的行动反映出其战略和技术能力都发生了明显的演变。

在它的大部分历史中，Boggy Serpens 偏爱喧闹、高音量的鱼叉式网络钓鱼行动，优先考虑速度而不是隐蔽性。

该组织依靠“自给自足”的策略，滥用远程监控和管理工具，如 Atera、ScreenConnect 和 SimpleHelp，以及 LaZagne 和 CrackMapExec 等公共事业工具。

早期的那些战役规模庞大但手段粗糙——但这种作战方式后来被一种更加精心策划的方式所取代。

Unit 42 的分析师发现该组织的行为发生了决定性的转变，并指出 Boggy Serpens 已经转向以长期坚持和信任关系妥协为中心的模式。

该组织现在使用 Rust（一种内存安全的语言，可以增加逆向工程的难度）构建定制植入程序，并将生成式人工智能集成到其开发流程中，以更快地生成新的恶意软件家族。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7OgWibAdAbO0LVECoqzcGn1CicyAIDIKQwmuiaibsiauzOHxOHzv5zj0W2zAEWA2p4aRLQY1y6nbLzPibuYZIvUm4ssxBctB1vZGJOeM/640?wx_fmt=png&from=appmsg)

2025年初的行动还揭示了其与名为“Lyceum”的“Evasive Serpens”组织的协调，这表明伊朗威胁生态系统内存在共享资源。

这场运动的影响范围很广。“沼泽巨蛇”已经袭击了以色列、匈牙利、土耳其、沙特阿拉伯、阿联酋、土库曼斯坦、埃及和南美洲的多个组织，涵盖政府、航空、海事和金融等各个领域。

从 2025 年 8 月到 2026 年 2 月，针对一家与沙特阿美有关联的阿联酋海洋能源公司发动了四波袭击，这是该组织持续性最鲜明的例证。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7PC9S6iaOMSq4xs9eclhv9R5F3Ij5wKhfsBjPS4vKo5W3cBAToAkEyicC43CySWLcQ92UTu9NfaqQhibhl2U65eGPRiaw3DzQH8WgY/640?wx_fmt=png&from=appmsg)

2025年8月，该组织还利用阿曼外交部一个被入侵的邮箱，向世界各地的使馆和国际组织发送伪造的外交邀请函，谎称举办“可持续和平”研讨会。

这些攻击活动之所以难以阻止，是因为它们构建了一个基于两阶段欺骗模型的传播链，同时利用了自动化过滤器和人们的信任。

## **双层社会工程和宏观交付**

第一阶段依赖于劫持政府机构或企业的合法电子邮件账户。

这些帐户发送的消息会被标记为负垃圾邮件置信度（SCL -1），因为它们来自经过身份验证的内部发件人，可以绕过垃圾邮件过滤器。

该策略曾被用于攻击土库曼斯坦的一家电信运营商和以色列的多个组织，该团伙直接从受害者的电子邮件环境中发送“网络安全指南”和与人力资源相关的附件 。

第二阶段会在目标打开附件文档时启动——通常是模糊的 Word 文件、伪造的 Excel 财务报告或伪造的阿拉伯航空公司机票。

该文件显示一条消息，声称它是用旧版本的 Microsoft Office 创建的，并要求用户单击“启用内容”。

当这种情况发生时，一个VBA宏会在后台静默执行，投放恶意代码，然后清除模糊效果，露出下面一份看起来完全合法的文档——让受害者感觉整个过程完全正常。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7MDVNGX279cSD0eYvNia2lm5SIB7q9nNxbau4CtnvXdicHvy7xOVeTjzXo2DWdBiaQiavadKY0OQURUvdHmiauiaRf2uJajZSals1hMA/640?wx_fmt=png&from=appmsg)

法证分析发现，有两个平行的 VBA 构建器分支与同一个开发团队有关：Phoenix Lineage，提供完整的后门程序，包括 BugSleep 和新发现的 Nuso HTTP 后门；以及 UDPGangster Operations，通过 UDP 部署较轻的后门程序。

两者使用相同的解密密钥和 `novaservice.exe` 文件路径，证实它们来自同一数据管道。

组织应在所有 Microsoft Office 环境中强制执行严格的宏执行策略，并部署能够检测丢弃并执行活动的行为端点监控。

为降低账户被盗风险，所有电子邮件账户都必须启用多因素身份验证。除了发件人信誉之外，能够评估行为和主题异常的电子邮件控制措施对于拦截内部网络钓鱼活动至关重要。

定期搜寻基于 UDP 的信标、进程注入事件和非标准注册表项修改等威胁，有助于在持久访问完全建立之前识别活跃的感染。

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