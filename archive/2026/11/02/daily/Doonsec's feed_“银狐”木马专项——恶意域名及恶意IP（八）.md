---
title: “银狐”木马专项——恶意域名及恶意IP（八）
url: https://mp.weixin.qq.com/s/VRV1NHzSw4HHDmWiTcipfQ
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:49:40.250114
---

# “银狐”木马专项——恶意域名及恶意IP（八）

# “银狐”木马专项——恶意域名及恶意IP（八）

原创

CNCERT
CNCERT

国家互联网应急中心CNCERT

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRhhIyaKiaibicVA52mvfx6RAx4RUajvowicT36HU8RMgM0cgtLg7SaicpJunguBXv13xNWD922GEK37EqTjrYBic7YKwDCtoEwbBDP9o/640?wx_fmt=png&from=appmsg)

近期，中国互联网网络安全威胁治理联盟（以下简称CCTGA）启动了“银狐”木马专项打击行动，重点围绕控制端打击、被控端处置、恶意样本传播链治理、成效评估和机制完善等重点任务统筹推进，保护人民群众合法权益。

本周，CCTGA研判确认了“银狐”木马使用的一批恶意网络资产，现予以披露。本次重点披露近期控制规模较大的TOP 20恶意网络资产，归属地主要分布于中国香港、日本、美国、德国等国家和地区。

一、黑客团伙概述

“银狐”黑产团伙团伙又称“游蛇”“谷堕大盗”，长期通过仿冒软件下载站、搜索引擎恶意推广、钓鱼邮件及即时通信等渠道传播恶意程序，如Gh0st、Win0s、DcRat等一系列具备远程控制能力的木马程序，利用木马程序携带功能的如文件下发、进程管理、命令执行、屏幕监控、键盘记录以及敏感信息窃取等实施违法犯罪活动，对网络安全和人民群众合法权益造成较大危害。

恶意网络资产信息如下：

（一）恶意IP地址：177.4.3.114

关联域名：113.mlcrosoft.vip

关联端口：443

归属地：中国 中国香港

日控制规模：2090

（二）恶意IP地址：157.90.33.74

关联域名：cc.bsjdwn.com

关联端口：80

归属地：德国

日控制规模：1646

（三）恶意IP地址：38.47.240.20

关联域名：kkabcd168.xyz

关联端口：22

归属地：中国 中国香港（IDC）

日控制规模：1415

（四）恶意IP地址：104.143.42.1

关联域名：

local72.mlcrosoft.my

localx.mlcrosoft.my

local82.mlcrosoft.my

关联端口：443

归属地：中国 中国香港

日控制规模：989

（五）恶意IP地址：154.55.127.9

关联域名：sfdeqwgeryhe5.vip

关联端口：443

归属地：日本

日控制规模：867

（六）恶意IP地址：8.218.53.1

关联域名：

www.rhe5gj.com

www.pyex8an.com

xssx.sumucompanyuo.com

关联端口：22

归属地：中国 中国香港（IDC）

日控制规模：812

（七）恶意IP地址：137.220.155.13

关联域名：yilushunf168.vip

关联端口：22

归属地：中国 中国香港（IDC）

日控制规模：716

（八）恶意IP地址：118.107.43.236

关联域名：

kkabcd168.xyz

kkkkorg.com

kk2029uu.org

关联端口：80

归属地：中国 中国香港（IDC）

日控制规模：613

（九）恶意IP地址：186.241.79.252

关联域名：

chat.rundatas.com

chat.stcpudp.com

chat.hao1151.com

关联端口：80

归属地：美国

日控制规模：585

（十）恶意IP地址：38.45.122.174

关联域名：

xiaoshihou39.top

xiaoshihou39.org

关联端口：56311

归属地：美国

日控制规模：470

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

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRjLHxFgGibCmUibVWn8WAAQeVzqC5iccB9sAZ4mbicnoic0hxe32tfqkiaMdB2DVTYqaulH6gmhBmLbqiaOG3icacgSQO52M5niaAEPzoJA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

不喜欢

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