---
title: 扫地机器人变身间谍！扫地机和割草机爆出严重安全漏洞
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546359&idx=2&sn=df3daa0069b98945b731490f87c06a82&chksm=fa938336cde40a20d0d0227fa9167dd34ce4b5204443400cbb5e84ba4d3c5a553d221fd62c13&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-14
fetch_date: 2025-10-06T18:05:39.359177
---

# 扫地机器人变身间谍！扫地机和割草机爆出严重安全漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kK7yOJ7Nl2ia20Dgl7T6cx9HwOPnY6W6uBia092saia7uibFA8K3LhBxMpCa5TbIY1tHgsSiaaKTfQ44Q/0?wx_fmt=jpeg)

# 扫地机器人变身间谍！扫地机和割草机爆出严重安全漏洞

网络安全应急技术国家工程中心

以下文章来源于网空闲话plus
，作者网空闲话

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM66kAclWVgNvfjr86OjY0XhbScmMc5RGNPzgL9G5cm4Gw/0)

**网空闲话plus**
.

原《网空闲话》。主推网络空间安全情报分享，安全意识教育普及，安全文化建设培育。将陆续推出网安快讯、网安锐评、网安政策、谍影扫描、APT掠影、密码技术、OT安全等专集。

**网络安全研究人员Dennis Giese和Braylynn在8月11日的Def Con会议上披露其研究成果，****指出科沃斯的机器人吸尘器和割草机可能被用于监视其所有者。研究发现，攻击者可以通过蓝牙在130米范围内控制这些设备，并利用其内置摄像头和麦克风进行监视。更严重的是，这些设备在几秒钟内就可能被黑客入侵。**

**主要的安全漏洞在于机器人的蓝牙连接，一旦连接，由于设备已连接Wi-Fi，黑客便能通过互联网接管设备。黑客可以控制机器人，访问房间地图，并打开摄像头和麦克风。尤其令人担忧的是，大多数新款科沃斯型号都配备了至少一个摄像头和麦克风，却没有设备活动指示器，使得用户难以察觉被监视。**

**此外，研究人员还发现用户数据即使在账户被删除后仍保留在公司云服务器上，割草机上的PIN码安全性不足，且以明文形式存储。尽管研究人员试图联系科沃斯报告这些漏洞，但未收到回复。专家们对科沃斯至今仍未解决这些问题表示严重担忧，因为这使得全球数百万用户容易受到潜在攻击。受影响的型号包括Deebot 900系列、N8/T8、N9/T9、N10/T10、X1、T20、X2、Goat G1、Spybot Airbot Z1、Airbot AVA和Airbot ANDY等。如果一台设备被黑客入侵，攻击者甚至还能访问附近的其他科沃斯机器人。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/0KRmt3K30icXn7nCUL7ialDMIDI0nA4Xnx9B6d4O5FqWTc1goicXWjXh8n2mnJcve2lUoXRDxibS5BJRicVicfrwjL9Q/640?wx_fmt=webp&from=appmsg)

**与蓝牙相关的漏洞**

安全研究员Dennis Giese和Braelynn将在周六的Def Con黑客大会上详细介绍他们对Ecovacs机器人的研究。当他们分析了几款Ecovacs产品时，发现了多个问题，这些问题可以被用来通过蓝牙黑客攻击这些机器人，并偷偷远程开启麦克风和摄像头。

![](https://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icXn7nCUL7ialDMIDI0nA4XnxZ5J6QyYTd4MC5S3d02pJzk3Tn1hjwTcoqWicgpaRia3Icfsq8YjZUsnQ/640?wx_fmt=png&from=appmsg)

研究团队称，在过去的5年里，他们一直在各种活动（如c3 或DEFCON）上介绍如何破解和root真空机器人。涵盖了Roborock、Dreame、小米和一些较小公司的真空机器人。但是，他们有没有研究过其他供应商，也许还有一些新的有趣的设备类别？在这次演讲中，他们的目标是Ecovacs机器人！Ecovacs是目前智能家居机器人市场的领导者，最近扩展到其他家用机器人领域。

Giese在接受TechCrunch采访时表示：“他们的安全性真的非常非常糟糕。”

研究人员表示，他们曾联系Ecovacs报告这些漏洞，但未收到公司的回复，并认为这些漏洞可能仍未修复，可能会被黑客利用。

Ecovacs没有回应TechCrunch的评论请求。

研究人员称，主要问题在于一个漏洞，允许任何使用手机的人通过蓝牙连接并控制Ecovacs机器人，距离可达450英尺（约130米）。一旦黑客控制了设备，他们可以通过Wi-Fi连接到互联网进行远程控制。

Giese表示：“你发送一个负载，这只需一秒钟，然后它会连接回我们的机器。例如，它可以连接回互联网上的服务器。从那里，我们可以远程控制机器人。我们可以读取Wi-Fi凭据，读取所有的[保存的房间]地图。因为我们坐在机器人的Linux操作系统上，我们可以访问摄像头、麦克风等。”

Giese表示，割草机器人始终启用蓝牙，而吸尘机器人则在开机时蓝牙启用20分钟，每天自动重启时启用一次，这使得它们更难被黑客攻击。

由于大多数新款Ecovacs机器人配备了至少一个摄像头和一个麦克风，一旦黑客控制了被攻击的机器人，这些机器人可以被变成间谍。根据研究人员的说法，机器人没有硬件指示灯或其他任何提示周围人摄像头和麦克风开启的警告。

![](https://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icXn7nCUL7ialDMIDI0nA4XnxcRf1w8muuTWnTHu43fP4kLqq7ia6a9AKB0DqJtDpo0bA4YDvib8icxbKw/640?wx_fmt=png&from=appmsg)

在某些型号上，理论上有一个每五分钟播放的音频文件表示摄像头开启，但黑客可以轻松删除该文件以保持隐秘，Giese说：“你基本上可以删除或覆盖该文件为空文件。因此，如果你远程访问摄像头，警告就不会播放。”

**数据同样面临严重风险**

除了黑客攻击的风险，Giese和Braelynn还发现了Ecovacs设备的其他问题。

他们指出的问题包括：即使删除用户账户后，机器人上存储的数据仍保留在Ecovacs的云服务器上；认证令牌也留在云端，允许在删除账户后仍访问机器人吸尘器，并可能使购买了二手机器人的人被监视；此外，割草机器人的反盗窃机制要求有人捡起机器人时输入PIN码，但PIN码以明文形式存储在割草机内部，因此黑客可以轻易找到并使用它。

研究人员表示，一旦Ecovacs机器人被攻击，如果设备在其他Ecovacs机器人的范围内，这些设备也可能被黑客入侵。

**影响范围较大**

Giese和Braelynn分析了以下设备：Ecovacs Deebot 900系列、Ecovacs Deebot N8/T8、Ecovacs Deebot N9/T9、Ecovacs Deebot N10/T10、Ecovacs Deebot X1、Ecovacs Deebot T20、Ecovacs Deebot X2、Ecovacs Goat G1、Ecovacs Spybot Airbot Z1、Ecovacs Airbot AVA以及Ecovacs Airbot ANDY。

**关于Ecovacs机器人公司**

Ecovacs Robotics（科沃斯机器人）是一家中国的高新技术企业，专注于家庭服务机器人的研发、设计、制造和销售。公司成立于1998年，总部位于中国苏州，是全球较早的家用机器人研发和制造商之一。

主要产品：

**机器人吸尘器**：Ecovacs以生产各种型号的机器人吸尘器而闻名，其中包括Deebot系列，这些吸尘器具备自动导航、定时清洁、智能避障等功能。

**机器人割草机**：公司也生产自动化割草机，能够自动完成草坪的修剪工作。家庭服务机器人：除了清洁和割草机器人，Ecovacs还开发了其他类型的家庭服务机器人，如窗户清洁机器人等。

**智能家电**：公司还涉足智能家电领域，生产如空气净化器等产品。

Ecovacs的客户遍布全球，包括北美、欧洲、亚洲等多个国家和地区。其产品主要面向追求智能家居生活的消费者，特别是那些希望减少日常家务劳动、提高生活质量的用户。公司的客户群体也包括对高科技产品感兴趣的技术爱好者和环保意识较强的用户。

Ecovacs Robotics通过不断的技术创新和产品升级，致力于为用户提供更加智能化、便捷化的家居清洁解决方案。随着智能家居市场的不断扩大，Ecovacs Robotics的产品和服务受到了越来越多消费者的认可和青睐。

**参考资源**

1、https://www.securitylab.ru/news/551043.php

2、https://techcrunch.com/2024/08/09/ecovacs-home-robots-can-be-hacked-to-spy-on-their-owners-researchers-say/

3、https://info.defcon.org/event/?id=54998

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