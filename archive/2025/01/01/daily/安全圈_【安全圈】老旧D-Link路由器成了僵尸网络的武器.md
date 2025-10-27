---
title: 【安全圈】老旧D-Link路由器成了僵尸网络的武器
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067033&idx=4&sn=02e788cd1d37c6ecc9e6e4b8820b6a00&chksm=f36e7899c419f18fdf86690aea168d3416d5902ba032120157f33266ce2108231ee38dd3c10d&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-01
fetch_date: 2025-10-06T20:08:04.991941
---

# 【安全圈】老旧D-Link路由器成了僵尸网络的武器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaibIy800sLiaj9ibq6rYbMktRdhVQ49rt5wQt9tWCd5RMp57XHzrPEFxqibuMjfu920p3hUbrhUoolqg/0?wx_fmt=jpeg)

# 【安全圈】老旧D-Link路由器成了僵尸网络的武器

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

僵尸网络

近期，两个名为“Ficora”和“Capsaicin”的僵尸网络在针对已停产或运行过时固件版本的D-Link路由器的攻击活动中表现活跃。受影响的设备包括个人和组织常用的D-Link型号，如DIR-645、DIR-806、GO-RT-AC750和DIR-845L。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaibIy800sLiaj9ibq6rYbMktRnut5wOwiajsQdia8RjR0JyX92aYliaYCWcF9HicPpdnUia2KVKwh2lkcL2Q/640?wx_fmt=jpeg&from=appmsg)

这两个恶意软件利用已知的漏洞进行初始入侵，其中包括CVE-2015-2051、CVE-2019-10891、CVE-2022-37056和CVE-2024-33112。一旦设备被攻破，攻击者会利用D-Link管理接口（HNAP）中的弱点，通过GetDeviceSettings操作执行恶意命令。

这些僵尸网络具备窃取数据和执行Shell脚本的能力。攻击者似乎利用这些设备进行分布式拒绝服务（DDoS）攻击。

Ficora是Mirai僵尸网络的一个新变种，专门针对D-Link设备的漏洞。根据Fortinet的遥测数据，该僵尸网络在10月和11月期间活动显著增加，表现出随机攻击的特点。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaibIy800sLiaj9ibq6rYbMktRKqzTrQ9ajdFxSXZ0ia5pcsx8AKEEPP92TA4gpxxRQMHMuMHZduiaiaOOA/640?wx_fmt=jpeg&from=appmsg)

感染过程

Ficora在获得D-Link设备的初始访问权限后，会使用名为“multi”的Shell脚本，通过多种方法（如wget、curl、ftpget和tftp）下载并执行其有效载荷。该恶意软件包含一个内置的暴力破解组件，使用硬编码的凭据感染其他基于Linux的设备，并支持多种硬件架构。

Ficora支持UDP洪水攻击、TCP洪水攻击和DNS放大攻击，以最大化其攻击威力。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaibIy800sLiaj9ibq6rYbMktRQApHQtiaJIDVf8aHwrmRjiaZH3fIiaOavZiauWl0v17KLBOdOXgljDatfA/640?wx_fmt=jpeg&from=appmsg)

Capsaicin是Kaiten僵尸网络的一个变种，被认为是Keksec组织开发的恶意软件，该组织以“EnemyBot”和其他针对Linux设备的恶意软件家族而闻名。Fortinet仅在10月21日至22日期间观察到其爆发性攻击，主要针对东亚国家。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaibIy800sLiaj9ibq6rYbMktRGfa7g6slzmPluO8l9S4qIGfKpibKEWmRAKHUPf8WMibqVn2YxLKr1VqA/640?wx_fmt=jpeg&from=appmsg)

Capsaicin的感染通过一个下载脚本（“bins.sh”）进行，该脚本获取不同架构的二进制文件（前缀为“yakuza”），包括arm、mips、sparc和x86。该恶意软件会主动查找并禁用同一主机上其他活跃的僵尸网络有效载荷。

除了与Ficora相似的DDoS能力外，Capsaicin还可以收集主机信息并将其外泄到命令与控制（C2）服务器以进行跟踪。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaibIy800sLiaj9ibq6rYbMktR50BXvRz1O6EEyWPcMWjtKfPmPqfdOsDQWAia5GlAHUGQW2ib8M5XPHBg/640?wx_fmt=jpeg&from=appmsg)

防止路由器和物联网设备感染僵尸网络恶意软件的一种方法是确保它们运行最新的固件版本，以修复已知漏洞。如果设备已停产且不再接收安全更新，则应更换为新设备。

参考来源：https://www.bleepingcomputer.com/news/security/malware-botnets-exploit-outdated-d-link-routers-in-recent-attacks/

***END***

阅读推荐

[【安全圈】大众集团80万电动汽车车主个人数据被泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067016&idx=1&sn=6603384db2288a2926a144a8eac4bf06&scene=21#wechat_redirect)

[【安全圈】大量Chrome扩展程序遭黑客攻击，60万用户数据危险](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067016&idx=2&sn=c6d0c4c40675a96032fc8819d5d12bc5&scene=21#wechat_redirect)

[【安全圈】WPA3协议存在安全漏洞，黑客可获取WiFi密码](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067016&idx=3&sn=8a2de7555b1f2f62a08ba91e461c72ba&scene=21#wechat_redirect)

[【安全圈】亚太地区恐在2025年面临更多深度伪造、量子攻击威胁](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067016&idx=4&sn=166b595d367a5786467ef6200b20dc4c&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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