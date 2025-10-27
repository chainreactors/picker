---
title: 多方受害！Donut勒索组织正对企业部署双重勒索
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247532909&idx=1&sn=19247042baced1505b46a36ce541c4ad&chksm=fa93f7accde47eba5622fd76735bdeaebada61c815b66831580b70df7ae379513e7b99cda018&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2022-11-25
fetch_date: 2025-10-03T23:44:29.530884
---

# 多方受害！Donut勒索组织正对企业部署双重勒索

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176k253jFZwgyZ3FSLQlgB7V8FnC4AHVGIRJEXUhTrcm2wppWZ3Ejz5GG6phYupClmSMicUOz7mdiab7g/0?wx_fmt=jpeg)

# 多方受害！Donut勒索组织正对企业部署双重勒索

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176k253jFZwgyZ3FSLQlgB7V8RljYmghAnUJSA2NSWJZCk94C8zIImB0xef3kIIbVcAaQ1bLX45KgCw/640?wx_fmt=png)

BleepingComputer在8月首次报道了Donut 勒索集团，将他们与对希腊天然气公司DESFA、英国建筑公司Sheppard Robson和跨国建筑公司Sando的袭击联系起来，证实Donut在对企业的双重勒索攻击中部署勒索软件。

而近期，BleepingComputer再次发现了用于Donut操作的加密器样本“VirusTotal”，进一步表明该组织正在使用自己定制的勒索软件进行双重勒索攻击。奇怪的是，Sando和DESFA的数据也被发布到几个勒索软件操作的网站上，Hive勒索软件声称发起了Sando攻击，Ragnar Locker则声称发起了DESFA攻击。

Unit 42研究员Doel Santos还表示：“赎金记录中使用的TOX ID可以在HelloXD勒索软件的样本中看到。这种被盗数据和附属关系的交叉发布让我们相信Donut Leaks背后的威胁行为者是众多行动的附属机构，现在正试图在他们自己的行动中将数据货币化。”、

**Donut 勒索软件介绍**

对于Donut勒索软件的分析仍在进行中。目前已知的是，在执行时，它会扫描匹配特定扩展名的文件进行加密。加密文件时，勒索软件会避开包含以下字符串的文件和文件夹：

![](https://mmbiz.qpic.cn/mmbiz_png/QmbJGbR2j6w1552icU8U4SFA59OSXKlmA7wd5evBa14X6HspdU3nyicA12L4xq1tWicJ9n5Bdd6z7ibZObRBQcbibdw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

当文件被加密时，Donut勒索软件会将.donut扩展名附加到加密文件。例如，1.jpg将被加密并重命名为1.jpg.donut。

![](https://mmbiz.qpic.cn/mmbiz_png/QmbJGbR2j6w1552icU8U4SFA59OSXKlmA1UdgZGou8wG6yBKFvqrjtgTsNAWJqibsI6Z2sOgXTe7Qb9rEqacSRibw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

由Donut勒索软件加密的文件

Donut Leaks的操作非常独特，其使用有趣的图形，在攻击中体现了一丝“幽默”。它甚至为可执行文件提供构建器，作为其Tor数据泄漏站点的网关。这种独特尤其体现在其赎金记录中，他们在其中使用了不同的ASCII艺术，例如旋转的ASCII甜甜圈。

![](https://mmbiz.qpic.cn/mmbiz_png/QmbJGbR2j6w1552icU8U4SFA59OSXKlmA26usVrB1icxXgyzDj8jWY5mXoFIibdnbu32Sv3RuNIM4LpUia48OaMJLw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

Donut赎金记录

BleepingComputer看到的另一个勒索软件笔记会伪装成一个显示PowerShell错误的命令提示符，然后打印一个滚动的勒索笔记。为了避免被发现，赎金票据被严重混淆，所有字符串都经过编码，JavaScript在浏览器中解码赎金票据。这些赎金票据包括联系威胁行为者的不同方式，包括通过TOX和Tor协商站点。

![](https://mmbiz.qpic.cn/mmbiz_png/QmbJGbR2j6w1552icU8U4SFA59OSXKlmArOicc5fk77ibHuw1fcBNqZiaBDaydjicryLsZKM17UibyDJj1cWPzqDTVicA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

Donut赎金谈判现场

Donut勒索软件操作还在其数据泄露站点上包含一个“构建器”，该构建器由一个bash脚本组成，用于创建Windows和Linux Electron应用程序，并带有捆绑的Tor客户端以访问其数据泄露站点

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176k253jFZwgyZ3FSLQlgB7V8KSXsAytia0xTQcBal6W2ibgWiaGNbicngOKpBIkygIPExPZo0wIGrA6DsQ/640?wx_fmt=jpeg)

D0nut勒索软件electron应用程序

原文来源：E安全

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176njVOPvfib4X3jQ6GIHLtX8SSDvbpmcpr4uu3X7ELG7PDjdaLVeq4Er02ZoicTPvxrC6KCVH3bssUVw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

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