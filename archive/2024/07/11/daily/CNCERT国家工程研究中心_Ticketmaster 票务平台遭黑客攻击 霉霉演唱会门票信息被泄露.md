---
title: Ticketmaster 票务平台遭黑客攻击 霉霉演唱会门票信息被泄露
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247545770&idx=3&sn=f2fccebabbb34f4e03256794dd9475f8&chksm=fa93856bcde40c7dff4344d16da905273b76014c9a75d557bcecc0d501ffce3441b156172f0d&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-07-11
fetch_date: 2025-10-06T17:45:43.487191
---

# Ticketmaster 票务平台遭黑客攻击 霉霉演唱会门票信息被泄露

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176nFYfjIMF0ibFULnyqyS2v8OwyV9w127jZib2kVEEwC5RwAY4LXMwP9qIRAk6a4Aib3DQuGumVCmuWiaA/0?wx_fmt=jpeg)

# Ticketmaster 票务平台遭黑客攻击 霉霉演唱会门票信息被泄露

网络安全应急技术国家工程中心

昨日，Ticketmaster 发布最新声明表示，黑客泄露了 166,000 张泰勒·斯威夫特时代巡回演唱会门票的 Ticketmaster 条形码数据，并警告说，如果不支付 200 万美元的勒索要求，将会泄露更多活动的信息。

自 5 月起，一个名叫 ShinyHunters 的威胁分子开始以 500,000 美元的价格出售 5.6 亿 Ticketmaster 客户的数据。

Ticketmaster 后来证实了数据泄露事件，并承认数据来自他们在 Snowflake 上的账户。据悉，Snowflake 是一家基于云的数据仓库公司，企业使用该公司来存储数据库、处理数据和执行分析。

今年 4 月，威胁分子开始利用恶意软件窃取的凭证下载至少 165 个组织的 Snowflake 数据库。威胁者随后勒索这些公司，要求他们支付费用以防止数据泄露或出售给其他威胁者。

已确认被窃取 Snowflake 账户数据的公司包括 Neiman Marcus、洛杉矶联合学区、Advance Auto Parts、Pure Storage 和 Satander。

# **泰勒·斯威夫特巡演门票信息被泄露**

昨日，一个名为 Sp1d3rHunters 的威胁分子泄露了他们所声称的 166,000 个泰勒·斯威夫特时代巡演条形码的门票数据，这些条形码可用于在各个音乐会日期入场。

Sp1d3rHunters（之前名为 Sp1d3r）是出售从 Snowflake 账户窃取的数据的威胁分子，并公开勒索各公司付款。

威胁情报服务 HackManac 最先分享的勒索要求是：“向我们支付 200 万美元，否则我们将泄露全部 6.8 亿用户信息和 3000 万个活动条形码，其中包括：泰勒·斯威夫特的更多活动、P!nk、Sting、体育赛事 F1 方程式赛车、MLB、NFL 和数千个其他活动。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28ibib59mh4R1poAmaOPKzsxJcS5RXVTsKg8qeJ3HPlNiaLZxxthmKiaeYMrJeFLCw8So6QdtibiavTTClw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

泰勒·斯威夫特演唱会门票信息在黑客论坛上泄露

该帖声称条形码数据是泰勒·斯威夫特即将在迈阿密、新奥尔良和印第安纳波利斯举行的演唱会的数据。

该帖子包含一小部分所谓的条形码数据样本，其中包含用于创建可扫描条形码的值、座位信息、票面价值和其他信息。威胁者进一步分享了如何将这些数据转换为可扫描条形码的详细信息。

虽然条形码数据不是威胁分子 5 月份发布的被盗 Ticketmaster 数据样本的初始泄露的一部分，但一些新泄露的数据可以在旧的泄露中找到，包括散列的信用卡和门票的销售订单信息。

这些攻击背后的组织是 ShinyHunters，多年来，该组织造成了多起数据泄露事件。其中包括 2020 年泄露 18 家公司的 3.86 亿条用户记录数据、影响 7000 万客户的 AT&T 数据泄露事件，以及最近泄露 Authy 多因素身份验证应用程序使用的 3300 万个电话号码。

Ticketmaster 随后称，唯一的条形码每隔几秒钟就会更新一次，因此被盗的门票无法使用。“Ticketmaster 的 SafeTix 技术通过每隔几秒自动刷新新的独特条形码来保护门票，以防止其被盗或复制。”

Ticketmaster 还证实，他们没有与威胁者进行任何赎金谈判，并对 ShinyHunter 声称他们被出价 100 万美元以删除数据的说法表示是无稽之谈。

**参考及来源：**

https://www.bleepingcomputer.com/news/security/hackers-leak-alleged-taylor-swift-tickets-amp-up-ticketmaster-extortion/

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