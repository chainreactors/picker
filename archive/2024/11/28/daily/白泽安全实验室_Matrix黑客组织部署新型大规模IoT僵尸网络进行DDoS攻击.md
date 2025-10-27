---
title: Matrix黑客组织部署新型大规模IoT僵尸网络进行DDoS攻击
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492435&idx=1&sn=9ccf468e02b40c2f862d73e7c493780f&chksm=e90dc979de7a406f209d19e9a90e835e9d00a7d7f927bc6728b55e11b01d5ce90642b6627547&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-11-28
fetch_date: 2025-10-06T19:21:28.438667
---

# Matrix黑客组织部署新型大规模IoT僵尸网络进行DDoS攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# Matrix黑客组织部署新型大规模IoT僵尸网络进行DDoS攻击

BaizeSec

白泽安全实验室

**一、事件概述**

网络安全研究人员发现了一个由名为Matrix的黑客组织发起的新型分布式拒绝服务（DDoS）攻击活动，该组织可能是俄罗斯的网络攻击者。此次攻击活动利用了大量互联网连接设备，包括IoT设备、摄像头、路由器、DVR和企业系统，标志着DDoS攻击焦点的转变。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIPl2D9sZzVuaOKKYzN1gictL8cj7jLhOrQ1iaKrib37PZr9s13PDgD8LdHQXZHPYxicj8IonOGcTSAibNQ/640?wx_fmt=png&from=appmsg)

**二、攻击过程技术分析**

Matrix黑客组织主要依赖暴力破解攻击，利用默认的弱口令和配置错误来获得初始访问权限。一旦设备被入侵，它们就会被纳入一个更大的僵尸网络。攻击者还使用各种公共脚本和工具来扫描易受攻击的系统、部署恶意软件和执行攻击。Matrix黑客组织还利用GitHub账户存储和管理恶意工具和脚本，主要使用Python、Shell和Golang编写。他们专注于如\_scanner\_、gggggsgdfhgrehgregswegwe、\_musersponsukahaxuidfdffdf\_和\_DHJIF\_等存储库，这些存储库包含各种工具，旨在扫描、利用和在IoT设备和服务器上部署恶意软件，主要是Mirai和其他与DDoS相关的工具。研究人员从Virus Total识别出用于发起DDoS攻击的各种工具，包括DDoS Agent、SSH Scan Hacktool、PyBot、PYnet、DiscordGo Botnet、HTTP/HTTPS Flood Attack和Homo Network。这些工具允许攻击者控制被入侵的设备，对目标发起大规模DDoS攻击，并使用Discord进行通信和远程控制。

此次攻击活动利用了一系列新旧漏洞，包括CVE-2014-8361、CVE-2017-17215、CVE-2018-10562、CVE-2022-30525、CVE-2024-27348等。这些漏洞与广泛使用的弱口令相结合，为攻击者提供了一个巨大的攻击面。大约95%的活动发生在工作日，说明这是有预谋和组织的攻击，以确保攻击效果最大化。这场活动可能影响数百万互联网连接设备。研究人员指出，如果1%的设备被入侵，僵尸网络可能达到35万设备；如果5%被入侵，可能增长到170万，与过去主要攻击相媲美。

参考链接：

https://hackread.com/matrix-hackers-new-iot-botnet-ddos-attacks/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

白泽安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

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