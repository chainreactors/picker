---
title: 新型 "HinataBot "僵尸网络可以发动大规模的DDoS攻击
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247535631&idx=2&sn=68836d928299c0a8cacdbe406263945b&chksm=fa93facecde473d8e0afe1a57c094109768038b1bef13c05da36abb395fb083f6b9d0077ed41&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2023-03-22
fetch_date: 2025-10-04T10:16:04.659951
---

# 新型 "HinataBot "僵尸网络可以发动大规模的DDoS攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kMMYn0L9k9MplexpNL3E3y1YHGpdsNpvAo0JhMiaCUFYOvd4qVFRyiby9fxcEPRJ5aY80bM0pxVYtQ/0?wx_fmt=jpeg)

# 新型 "HinataBot "僵尸网络可以发动大规模的DDoS攻击

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kMMYn0L9k9MplexpNL3E3yvhX8poZTAiabY9NmzOVibwZwpdOgY8vTYDdCfmXvSmm5o5kjISzEWiamw/640?wx_fmt=jpeg)

Akamai的研究人员发现了一个新型恶意僵尸网络，它以Realtek SDK、华为路由器和Hadoop YARN服务器为目标，将设备引入到DDoS（分布式拒绝服务）群中，有可能进行大规模攻击。

这个新型僵尸网络是研究人员今年年初在自己的HTTP和SSH蜜罐上发现的，该僵尸网络利用了CVE-2014-8361和CVE-2017-17215等漏洞。

Akamai表示，HinataBot以Mirai为基础，是基于Go的变体。

# **显著的DDoS能力**

该恶意软件通过对SSH端点进行暴力攻击或使用已知漏洞的感染脚本和RCE有效载荷进行分发。感染设备后，恶意软件会默默地运行，等待来自命令和控制服务器的命令执行。

HinataBot的旧版本支持HTTP、UDP、ICMP和TCP洪水，但较新的变体只具有前两种。然而，即使只有两种攻击模式，该僵尸网络也可以潜在地进行非常强大的分布式拒绝服务攻击。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibnibF455ogVfD7apkUuAwq4z5ibnD7icus0VS69iatbSoslicrQdKb1ZTmty8iclxT7gutt5vqUW6PeI4Q/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

【攻击函数】

虽然 HTTP 和 UDP 攻击命令不同，但它们都创建了一个包含 512 个工作线程（进程）的工作线程池，这些工作线程在自定义的持续时间内向目标发送硬编码数据包。

HTTP数据包的大小在484和589字节之间。而HinataBot产生的UDP数据包则特别大（65549字节），由大量的空字节组成。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibnibF455ogVfD7apkUuAwq4MJVM1O7XKgDLXgwYn2JkNI12Ms9YR2fla7uITemeYpoFEJRTS0a6ag/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

【UDP泛滥数据包捕获】

HTTP产生大量的网站请求，而UDP则向目标发送大量的垃圾流量；攻击者通过两种不同的方法来实现断网。

Akamai对僵尸网络的HTTP和UDP的10秒攻击进行了基准测试，在HTTP攻击中，恶意软件产生了20430个请求，总大小为3.4MB。UDP产生了6733个包，总大小为421MB。

研究人员估计，如果有1000个节点，UDP可以产生大约336Gbps，而在10000个节点，攻击数据量将达到3.3Tbps。

在HTTP洪的情况下，1000个被捕获的设备将产生每秒2000000个请求，而10000个节点将产生20400000 rps和27 Gbps。

目前，HinataBot仍在不断开发中，随时可能实施更多的漏洞并扩大其目标范围。

**参考链接：**

www.bleepingcomputer.com/news/security/new-hinatabot-botnet-could-launch-massive-33-tbps-ddos-attacks/

原文来源：FreeBuf

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

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