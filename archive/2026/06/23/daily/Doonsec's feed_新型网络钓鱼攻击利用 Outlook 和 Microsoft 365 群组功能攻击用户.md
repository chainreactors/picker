---
title: 新型网络钓鱼攻击利用 Outlook 和 Microsoft 365 群组功能攻击用户
url: https://mp.weixin.qq.com/s/nnVcDapOcMD32s6AN-3wKg
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:01:20.129840
---

# 新型网络钓鱼攻击利用 Outlook 和 Microsoft 365 群组功能攻击用户

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7NXhQcWkq9d7sjdbW8jibyuTpp6d6XDt7DbJauLYoMb7RaKQSc3t5cU9RS3eCru3G6q9osX9bbBDM5lcJcJcADQcibQsa0iaOSlW0/0?wx_fmt=jpeg)

# 新型网络钓鱼攻击利用 Outlook 和 Microsoft 365 群组功能攻击用户

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

网络钓鱼攻击变得越来越复杂，攻击者不再依赖笨拙的虚假电子邮件或明显的诈骗信息。

最新发现的一项活动表明，威胁行为者如何将日常使用的 Microsoft 365 工具变成武器，并将攻击隐藏在员工最信任的工作流程中。

这不是微软软件的缺陷，而是对其合法功能的蓄意滥用，而这恰恰是它的危险之处。

此次攻击的目标是 Microsoft 365 Groups，这是一个协作功能，组织每天都使用该功能来协调团队、共享文件和管理内部更新。

通过控制一个群组并将受害者添加到该群组中，攻击者可以同时入侵用户的收件箱、日历和文件存储。

欢迎邮件看起来很简洁，群组名称也很熟悉，没有任何立即引起怀疑的地方。

Fortra 情报与研究专家 (FIRE) 团队的分析师识别并记录了这种技术，并指出它代表着从传统网络钓鱼向受信任工作流滥用的转变。

Fortra 在一份与网络安全新闻 (CSN) 分享的报告中表示，此次攻击旨在使恶意活动看起来像是例行合作。

“IT 支持”、“人力资源更新”、“财务审查”或“全体公司”等群组名称经过精心设计，旨在与内部沟通融为一体。

一旦用户进入攻击者控制的群组，后续内容就会通过群组邮箱、共享文档或日历邀请送达。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7NYFfSTP6wpufMunDPHlCoSWiayC0pEia8z4lZPyov2GAibdpQfFON3NtyEyTAH4kveGE3EEyLFy74cBhReMicVYPj7xErN3iaWHHHI/640?wx_fmt=png&from=appmsg)

每个步骤都模拟了真实的 Microsoft 365 工作流程，而这正是用户不会发出警报的原因。一旦用户采取行动，无论是点击链接、打开文件还是响应请求，风险就会真正出现。

潜在的后果很严重，因为受害者可能面临凭证被盗、令牌被捕获、恶意软件传播、数据泄露或进一步的社会工程攻击。

由于攻击是通过微软自身的基础设施进行的，早期检测工具可能不会标记它，从而让攻击者有更多时间在不被发现的情况下在环境中移动。

## **新型网络钓鱼攻击滥用 Outlook 和 Microsoft 365 群组**

此次攻击活动的机制简单却巧妙。攻击者创建或控制一个 Microsoft 365 群组，然后通过直接添加或邀请的方式将目标添加到该群组中。

群组名称和欢迎信息营造了一种紧迫或例行的氛围，例如工资更新、强制性培训通知或供应商行动事项。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7Mo9j0mgjrvoo1krTaaSPicdDfkIAVW0h5FBCctibVZGbOOncpZfQ8nuVOJO7vicuKnN88ic8lfmnEQswrg7VFUiakNwzJJc6IjE0kE/640?wx_fmt=png&from=appmsg)

在发出初始群组邀请后，后续的网络钓鱼内容会通过群组邮箱或共享文件发送到群组。

群组内共享的文档可能包含虚假的支持流程、指向窃取凭证页面的二维码，或者植入了宏的文件。由于这些内容是通过微软协作平台传输的，用户往往更信任它，而不是直接通过电子邮件附件接收的内容。

## **日历钓鱼：当日历成为诱饵**

此次网络钓鱼活动之所以特别有效，是因为它使用了日历钓鱼（CalPhishing）。

攻击者一旦通过群组邀请获得访问权限，就会向受害者的 Outlook 日历发送一个恶意的 .ics 格式日历事件。该事件会持续发送提醒，即使原始邮件已被删除或错过，钓鱼攻击仍会持续很长时间。

日历邀请可以伪装成项目会议、人事截止日期、管理员提醒或发票审核。每次提醒都会逐步引导用户采取行动。

这种反复接触正是CalPhishing与普通一次性电子邮件攻击的区别所在。钓鱼邮件不再让人感觉像骗局，而更像是一项尚未完成的工作任务。

安全团队在调查此类攻击时，应将目光投向收件箱之外的更广阔区域。防御人员应追踪完整的攻击链，包括群组创建者、添加用户、共享文件以及邮件清理后日历条目是否仍然存在。

组织可以在网关级别阻止发件人域“groups.outlook.com”，以停止外部群组通知。

员工还需要接受培训，以便像对待任何未经请求的电子邮件一样谨慎对待意外的群组添加和会议邀请，尤其是当邮件内容涉及紧急或行政事务时。

预览时标签不可点

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