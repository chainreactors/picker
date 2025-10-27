---
title: FBI的受审查信息共享网络“InfraGard”被黑
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247533545&idx=1&sn=6dd839720438e20b22a01ed578fc90a5&chksm=fa93f528cde47c3e2e2e299376a1860b7031e8200fbae1c08bdfcd8da48135077248934ae958&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2022-12-29
fetch_date: 2025-10-04T02:40:45.928454
---

# FBI的受审查信息共享网络“InfraGard”被黑

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176lgjO4XKBt8qZl6kRO21GVPCsb52umDCaOylqNAt0XbibFPU41U1gn7gXzvBRl6S5x9Oxs9IshZtUQ/0?wx_fmt=jpeg)

# FBI的受审查信息共享网络“InfraGard”被黑

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176lgjO4XKBt8qZl6kRO21GVPv2e4RFcJgupUN55gyUhqibR4xjTUuLCckbGy7BzGJU46l0UeBHB1kkQ/640?wx_fmt=png)

InfraGard是美国联邦调查局（FBI）开展的一个项目，旨在与私营部门建立起线上线下威胁信息共享合作伙伴关系。本周，该项目发现其8万多成员的联系信息数据库在一个英文网络犯罪论坛上被公然兜售。与此同时，幕后黑客正在通过InfraGard门户网站直接与成员们联系——黑客使用的一个新帐户盗用了一位已通过FBI审查的金融行业公司首席执行官（CEO）的身份。

2022年12月10日，新开设不久的网络犯罪论坛Breached发布了一则令人震惊的新帖子：兜售InfraGard的用户数据库，包括数万名InfraGard成员的姓名和联系信息。

FBI的InfraGard项目可谓是一份已通过审查的名人录，列出了私营部门从事网络安全岗位和物理安全岗位的重要人物，这些公司管理着美国大多数关键基础设施，包括饮用水及电力公用事业公司、通信及金融服务公司、交通运输及制造公司、医疗保健机构以及核能公司。

FBI的InfraGard信息一览表写道：“InfraGard将关键基础设施所有者、运营商和利益相关者与FBI联系起来，提供安全威胁和风险方面的教育、网络和信息共享。”

FBI在回应KrebsOnSecurity网站分享的信息时表示，它已获悉与InfraGard门户网站有关的一个潜在的虚假帐户，正在积极调查此事。

FBI在一份书面声明中表示：“这起事件还在调查中，目前我们无法透露任何更多的信息。”

KrebsOnSecurity联系上了InfraGard数据库的卖家，Breached论坛的这名成员使用了“USDoD”化名，其头像是美国国防部的印章。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icYjKKQsWfiaibiabH2woFeyPU0XHwycT83icV66pdxqLIBibyxdA2fu1ENPV1aoDTxBPJDaTuIUa9SNiag/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图1. USDoD的InfraGard在Breached上公然兜售的帖子

USDoD表示，他们使用一家极有可能获得InfraGard成员资格的公司的首席执行官的姓名、社会保险号、出生日期及其他个人信息申请了一个新帐户，从而成功访问了FBI的InfraGard系统。

这位首席执行官目前是一家对大多数美国人的信用有直接影响的美国大型金融公司的负责人，他告诉KrebsOnSecurity，FBI从来没有联系过自己以审查InfraGard申请。

USDoD告诉KrebsOnSecurity，他们的虚假申请是在11月以这位首席执行官的名义提交的，申请附有他们控制的联系电子邮件地址，但也附有这位首席执行官的真实手机号。

USDoD说：“当你注册时，他们说批准至少需要三个月。我没料到会得到批准。”

但USDoD表示，12月初，他们以这位首席执行官的名义发送的电子邮件地址收到了回复，声称申请已获批准（见经过编辑的截图）。虽然FBI的InfraGard系统默认要求进行多因素身份验证，但用户可以选择通过短信还是电子邮件来接收一次性验证码。

USDoD表示“如果只能通过手机接收，我的处境就很糟糕。因为那样我收不到一次性验证码。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icYjKKQsWfiaibiabH2woFeyPUXz2Hlu0lzAjUAjVogKyRzOmpINlxmwF8wjUAOISl1q61XXtSwQRUtw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图2

USDoD表示，InfraGard用户数据可以通过内置在网站几个关键组件中的应用编程接口（API）轻松获取，这些组件可以帮助InfraGard成员相互联系和沟通。

USDoD表示，在InfraGard成员资格获得批准后，他们请一位朋友用Python编写了一个脚本，以查询该API，并检索所有可用的InfraGard用户数据。

USDoD表示：“InfraGard是知名人士的社交媒体情报中心。他们甚至设有专门用来讨论的论坛。”

为了证明他们在周二晚上发布时仍然可以访问InfraGard，USDoD通过InfraGard的消息传递系统向一名InfraGard成员发送了私信，该成员的个人资料最初是作为数据库售卖帖子的噱头来发布的。

这位InfraGard成员是美国一家大型科技公司的安全主管，他证实收到了USDoD发来的消息，但不愿透露姓名。

USDoD承认，对InfraGard数据库开出5万美元的售价可能有点高，因为这只是基本列出了已经非常有安全意识的那些人。此外，只有大约一半的用户帐户含有电子邮件地址，而大多数其他数据库字段（如社会保险号和出生日期）空空如也。

USDoD解释道：“我不认为有人会出这个价，但我总得把价格标高一点，才能谈成我想要的价格。”

虽然入侵InfraGard所泄露的数据可能极少，但用户数据可能并不是入侵者真正的终极目标。

USDoD表示，他们希望这个冒名顶替的帐户能够持续使用足够长的时间，以便以首席执行官的身份通过InfraGuard消息传递门户向其他高管发送私信。USDoD发来了下面这个经过编辑的截图，不过没有附上额外的上下文。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icYjKKQsWfiaibiabH2woFeyPU07NDvjkxt5iaJ9aSvnBRSZAFEPsMj1S7tiahjTZul9y1ibEtQlC0QVosA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图3. USDoD发来的截图显示了FBI InfraGard系统中的消息帖子

USDoD在售卖帖子中表示，这笔交易的担保人将是网络犯罪论坛Breached的管理员Pompompurin。如果潜在买家通过该论坛管理员的托管服务购买该数据库，理论上可以避免被骗，并确保在资金交易之前，交易双方都能满意。

多年来，Pompompurin一直是FBI的眼中钉。其Breached论坛被广泛认为是RaidForums的第二个版本，RaidForums是一个非常相似的英文网络犯罪论坛，今年4月已被美国司法部关闭。在被FBI渗透之前，RaidForums兜售全球一些最重大的数据泄露事件中被盗的100多亿份消费者记录的访问权。

2021年11月，KrebsOnSecurity详细介绍了Pompompurin如何滥用FBI在线门户网站的一个漏洞（该门户网站原本旨在与州和地方执法部门共享信息），以及该访问权如何被用来发送数千封恶作剧电子邮件，所有邮件都是从FBI的电子邮箱和互联网地址发送出去的。

**参考及来源：**

https://krebsonsecurity.com/2022/12/fbis-vetted-info-sharing-network-infragard-hacked/

原文来源：嘶吼专业版

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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