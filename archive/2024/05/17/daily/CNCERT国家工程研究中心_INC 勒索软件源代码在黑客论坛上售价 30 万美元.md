---
title: INC 勒索软件源代码在黑客论坛上售价 30 万美元
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247544621&idx=1&sn=c22c456f6e07439158a706390823c0d3&chksm=fa9399eccde410fa67d9bc853bed5a8f3540965e6fe8929ce603848c4caa6c0a295d3f827923&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-05-17
fetch_date: 2025-10-06T17:16:33.375086
---

# INC 勒索软件源代码在黑客论坛上售价 30 万美元

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176nr5wx9fECL4VicYicRFMydDbKFTs9o1ibf90udfssr382hyo3ibYiavgWU71Qjlh0aa0IsGSCR7ZVM2hw/0?wx_fmt=jpeg)

# INC 勒索软件源代码在黑客论坛上售价 30 万美元

网络安全应急技术国家工程中心

INC Ransom 是一项于 2023 年 8 月推出的勒索软件即服务 (RaaS) 操作，一位名为“salfetka”的网络犯罪分子声称正在出售 INC Ransom 的源代码。

INC 此前的目标是施乐商业解决方案公司 (XBS) 的美国分部、菲律宾雅马哈汽车公司，以及苏格兰国家医疗服务体系 (NHS)。

在涉嫌出售的同时，INC 赎金业务正在发生变化，其核心团队成员之间或许已存在裂痕，或计划进入涉及使用新加密器的方向。

# **源码出售**

威胁分子宣布在 Exploit 和 XSS 黑客论坛上出售 INC 的 Windows 和 Linux/ESXi 版本，要价 30 万美元，并将买家数量限制为三个。根据发现此次销售的 KELA 威胁情报专家提供的信息，论坛帖子中提到的技术细节，例如在 CTR 模式下使用 AES-128 和 Curve25519 Donna 算法，与 INC Ransom 的公开分析一致样品。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28aKlIehictOAr1G0MyZqSU0YBPQayfYB3UyicyDI0kZkuxb2gMtJB6giatDsFib5I5ibXM4yIaOhn125g/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

涉嫌出售源代码

“salfetka”自 2024 年 3 月以来一直活跃在黑客论坛上。该威胁分子此前曾希望以高达 7000 美元的价格购买网络访问权限，并从勒索软件攻击收益中向初始访问经纪人提供提成。

增加销售合法性的另一点是“salfetka”其签名上包括新旧 INC 勒索页面 URL，表明它们与勒索软件操作有关联。

尽管如此，这次销售可能是一个骗局，威胁分子在过去几个月里精心策划了“salfetka”帐户，宣称有兴趣购买网络访问权限，并设定了高价标签以使报价看起来合法。

目前，INC的新旧网站上都没有关于出售该项目源代码的公告。

# **INC 搬迁至新地点**

2024 年 5 月 1 日，INC Ransom 在其旧泄露网站上宣布，将转移到新的数据泄露勒索“博客”，并共享新的 TOR 地址，并表示旧网站将在两到三个月内关闭。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28aKlIehictOAr1G0MyZqSU0Yrw12CAnmjTaia7sI3Sbkic8nIMjFvHCcd1dwx78zXgpgXLgA9AcFdfQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

旧 INC 勒索网站宣布迁移至新 URL

目前，新网站已经上线，受害者列表与旧门户有一些重叠，并且旧网站上没有看到十二个新受害者。

新网站总共列出了 64 名受害者（12 名新受害者），而旧网站有 91 条帖子，因此 INC 过去的受害者大约有一半失踪。“两个地点之间的差异可能表明某个行动可能经历了领导层变更或分裂成不同的团队，”KELA 的分析师评论道。

然而，“salfetka”在其所谓的项目中引用了这两个网站，在这种情况下，创建新博客可能是为了从销售中获得更多利润。

还值得注意的是，INC 的新勒索页面设计在视觉上与 Hunters International 的设计相似，这可能表明与其他 RaaS 操作存在联系。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28aKlIehictOAr1G0MyZqSU0ibHTVXNclUicia755CamPyOMYC9rtbiabr6JC953yQ1dGDYticiagZHncxrQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

新的 INC 勒索勒索网站

与允许安全分析师破解勒索软件变种加密的公开泄密相反，没有可用解密器的变种的私人源代码销售有可能给全球带来麻烦。

这些勒索软件构建者是由刚进入该领域的威胁分子或希望使用更强大且经过充分测试的加密器来提高游戏水平的半成熟团体购买的。当提供 Linux/ESXi 版本时尤其如此，该版本通常开发起来更具挑战性并且获取成本更高。

当勒索软件团伙重新命名时，他们通常会重用旧加密器的大部分源代码，从而使研究人员能够将旧团伙与新的行动联系起来。使用其他勒索软件操作的加密器也可以达到目的，因为它会混淆执法和研究人员的踪迹。

**参考及来源：**

https://www.bleepingcomputer.com/news/security/inc-ransomware-source-code-selling-on-hacking-forums-for-300-000/

原文来源：嘶吼专业版

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

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