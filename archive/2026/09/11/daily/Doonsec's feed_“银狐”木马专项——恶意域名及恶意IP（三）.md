---
title: “银狐”木马专项——恶意域名及恶意IP（三）
url: https://mp.weixin.qq.com/s/GsxkCgYDKYo01ppXGNqVkg
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:45:38.281421
---

# “银狐”木马专项——恶意域名及恶意IP（三）

# “银狐”木马专项——恶意域名及恶意IP（三）

原创

CNCERT
CNCERT

国家互联网应急中心CNCERT

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRglPda6b8qGD3hbngrz2iaYkPrG6Rf5Q6vrECF7KiahfMSBEJmeeB1KdFJ348nI5xIA3QIpRMYq7XbY2TTdT6l4ooOZjAGgJYHm0/640?wx_fmt=png&from=appmsg)

近期，中国互联网网络安全威胁治理联盟（以下简称CCTGA）启动了“银狐”木马专项打击行动，重点围绕控制端打击、被控端处置、恶意样本传播链治理、成效评估和机制完善等重点任务统筹推进，保护人民群众合法权益。

本周，CCTGA研判确认了“银狐”木马使用的一批恶意网络资产，现予以披露。本次重点披露近期控制规模较大的TOP 10恶意网络资产，归属地主要分布于美国、中国香港等国家和地区。

一、黑客团伙概述

“银狐”黑产团伙团伙又称“游蛇”“谷堕大盗”，长期通过仿冒软件下载站、搜索引擎恶意推广、钓鱼邮件及即时通信等渠道传播恶意程序，如Gh0st、Win0s、DcRat等一系列具备远程控制能力的木马程序，利用木马程序携带功能的如文件下发、进程管理、命令执行、屏幕监控、键盘记录以及敏感信息窃取等实施违法犯罪活动，对网络安全和人民群众合法权益造成较大危害。

恶意网络资产信息如下：

（一）恶意IP地址：104.21.3.223

关联域名：

18.mlcro.net

22.mlcro.net

20.mlcro.net

82.mlcro.net

82.mlcro.net

1x46.mlcrosoft.me23.mlcro.net

92.mlcro.net

关联端口：443

归属地：美国

日控制规模：20628

（二）恶意IP地址：172.67.153.160

关联域名：

28.mlcro.net

54.mlcro.net

22.mlcro.net

23.mlcro.net

19.mlcro.net

关联端口：443

归属地：美国

日控制规模：18152

（三）恶意IP地址：104.21.71.30

关联域名：

11x.mlcrosoft.vip

113.mlcrosoft.vip

11.mlcrosoft.vip

112.mlcrosoft.vip

10.mlcrosoft.vip

关联端口：443

归属地：美国

日控制规模：12456

（四）恶意IP地址：172.67.142.197

关联域名：

113.mlcrosoft.vip

112.mlcrosoft.vip

11.mlcrosoft.vip

11x.mlcrosoft.vip

关联端口：443

归属地：美国

日控制规模：12281

（五）恶意IP地址：122.10.85.4

关联域名：

www.ijt1.com

aopdyrtdvhss.cn

关联端口：80

归属地：中国 中国香港

日控制规模：7091

（六）恶意IP地址：103.97.3.19

关联域名：

kaol.one

54.11new.webcamcn.xyz

关联端口：443

归属地：中国 中国香港

日控制规模：6549

（七）恶意IP地址：198.44.185.131

关联域名：

masike4.preech.top

otaku.mlcrosoft.vip

cvqthu.net

关联端口：80

归属地：中国 中国香港

日控制规模：6413

（八）恶意IP地址：39.109.122.128

关联端口：443

归属地：中国 中国香港

日控制规模：6268

（九）恶意IP地址：177.4.3.107

关联域名：

1x421.mlcrosoft.me

1x6.mlcrosoft.me

1x5.mlcrosoft.me

20.mlcro.net

1x46.mlcrosoft.me

19.mlcro.net

20.mlcro.net

关联端口：443

归属地：中国 中国香港

日控制规模：4610

（十）恶意IP地址：177.4.3.104

关联域名：

113.mlcrosoft.vip

关联端口：443

归属地：中国 中国香港

日控制规模：4125

二、排查方法

（一）详细查看分析近期浏览器历史记录、DNS请求及网络流量，重点排查是否存在访问银狐相关钓鱼网站、恶意域名及IP地址的记录。如发现相关访问行为，可进一步提取源IP、终端信息及访问时间等信息进行分析。

（二）重点检查终端近期下载文件及可疑程序，关注是否存在从钓鱼网站下载并执行恶意木马的情况，同时排查异常进程、启动项及网络连接等信息，判断终端是否存在木马感染。

（三）对发现的可疑终端进行重点勘验取证，并结合恶意文件哈希、网络通信地址等 IOC，在单位内部开展关联排查，确认是否存在其他受影响终端。

三、处置建议

（一）及时在威胁情报平台、网络出口及终端安全防护设备中更新相关 IOC，对恶意域名、IP及木马文件进行检测和拦截。

（二）对确认感染木马的终端及时进行网络隔离，清理恶意文件及相关持久化机制，并全面排查是否存在其他异常程序及网络通信行为。

（三）加强对钓鱼网站及恶意软件下载行为的安全防范，避免通过非官方渠道下载软件或打开来源不明的链接、文件，降低终端感染风险。

（四）向"银狐"木马专项打击行动线索征集邮箱silverfox@cert.org.cn报告相关线索及样本信息。

---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRg3jia4cr8WiaAibnq1T9iciaficaZtraVRsfYibQxIgoSXtgdl6iaAuQ2hQmFKZHNoice4ST0kcdhR0RGg1RLeWbQmF7WFjlBHSR3kR79s/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1HvTteAHz65uZccENTFwtVytvibEnzNbibwZw0F5MItQaglR2pQNzcw4dYE1FfLGuMhRztcV49nmwkkexPBKZPibQ/0?wx_fmt=png)

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