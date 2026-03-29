---
title: 银狐新攻势携税务主题钓鱼诱饵袭击日本企业
url: https://mp.weixin.qq.com/s/vBK6NUML-q-laU0v6dqpKg
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:35:43.116471
---

# 银狐新攻势携税务主题钓鱼诱饵袭击日本企业

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7MsIUKxyib66lE464eAKiaKRmib0n7xY841N4cpY26y2nIlseh6wW9j23Peno2xFszJ88pByiammD3ct174OTKB3Y3YMBEIaBHoqEA/0?wx_fmt=jpeg)

# 银狐新攻势携税务主题钓鱼诱饵袭击日本企业

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

日本的报税季已成为一个名为“银狐”的组织严密的威胁行为者的狩猎场。

随着日本企业进入年度报税、薪资审查和人事变动的周期，该组织充分利用了这一时机，发送高度有针对性的鱼叉式网络钓鱼邮件，这些邮件的设计看起来就像是例行的内部沟通。

该活动目前针对日本各地的制造商和其他各种企业，利用员工自然而然地期待收到有关财务和人事事项的电子邮件的这段时间。

银狐组织至少从 2023 年就开始活跃。该组织最初专注于以讲中文的目标为目标，之后将业务扩展到东南亚、日本，甚至可能扩展到北美，每次行动都使用当地语言。

多年来，该组织的目标涵盖了广泛的行业——金融、医疗保健、教育、游戏、政府，甚至网络安全。

这种广泛的影响力表明，银狐并非只会一种战术；它会根据环境和季节调整策略。

此次针对日本的最新袭击行动延续了去年同期观察到的模式，证实该组织有意选择在可预测的商业周期内发动袭击。

WeLiveSecurity 的分析师发现了这一持续进行的攻击活动，并指出 Silver Fox 发送的电子邮件并非普通的群发邮件。攻击者会事先对每个目标进行侦察，收集员工的真实姓名，甚至包括 CEO 的身份信息，并将其用作伪造的发件人。

每封电子邮件的主题行中都直接包含目标公司的名称，使邮件感觉像是一封合法的内部通知。

邮件主题涉及税务违规、薪资调整、员工持股计划变更和人事更新等话题——这正是员工在这个繁忙季节所期望和信任的信息类型。

这种级别的攻击前研究使 Silver Fox 与低级威胁行为者区别开来，也使其攻击活动更难被发现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7P8qrsxrn5WUwo5G2rQx3s7aGqcXOXa2T6MAX3MOMR2vWOFRKnNVMyvKD9R5ZlibiaicptjfmOaNhKSIQIOg0albGR9TkEuONtZtM/640?wx_fmt=png&from=appmsg)

这些电子邮件要么带有恶意附件，要么带有指向网页的链接，指示受害者下载文件。

这些示例分别展示了2026 年 3 月 11 日和 3 月 12 日分发的鱼叉式网络钓鱼电子邮件，以及用于推送恶意下载的与税务相关的诱饵网页。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7NGDKmzicYrz7rgeetCuGNqJV0E68feHq04peicvDbRSFN4wCOqArvdUa1kpuGiaHSDrUSuGl7nOWj5ZOGvF7Biba0RVUE90iaKja74/640?wx_fmt=png&from=appmsg)

打开这些文件中的任何一个都会将 ValleyRAT 植入受害者的计算机——这是一种远程访问木马，ESET 产品会将其检测为 Win64/Valley。一旦安装完成，ValleyRAT 就能让攻击者完全远程控制受感染的系统。

## **攻击的结构**

此次攻击活动的感染链虽然简单，但却十分有效。受害者打开恶意文件（通常伪装成工资单或人事文件）后，ValleyRAT 便会在用户不知情的情况下控制系统。

该木马程序随后会在环境中保持持久性，这意味着即使在重启后它也会继续运行，从而使攻击者的访问权限得以长期保持。

这些文件通常通过 gofile[.]io 或 WeTransfer 等公开的文件托管服务进行传输，由于这些都是知名的平台，这又增加了一层欺骗性。

通常使用 RAR 或 ZIP 格式的压缩文件来打包有效载荷，这样收件人就不容易立即察觉到。

为了降低成为此类攻击的受害者的风险，WeLiveSecurity 的研究人员建议员工在采取任何行动之前，通过单独的渠道（例如电话或直接消息）验证任何有关薪资变化、税务处罚或人事更新的电子邮件。

收件人还应检查发件人的电子邮件地址是否与显示的名称相符，因为不匹配是欺骗的常见迹象。

如果电子邮件中的语言感觉异常生硬或正式，员工也应该谨慎，因为 Silver Fox 的客服人员并非以日语为母语，邮件中有时会出现一些细微的措辞错误。

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