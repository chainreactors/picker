---
title: Windows高危漏洞来袭？已有补丁不需惊慌！
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247507418&idx=1&sn=da776c2f8240abafa5a269743b0deeec&chksm=fa520864cd25817216f28ff61b81ac5b9477849715e27a45a49f27279812b3afdf958ef45cc1&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2024-08-11
fetch_date: 2025-10-06T18:02:45.460038
---

# Windows高危漏洞来袭？已有补丁不需惊慌！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnRlCNmtlMvn32OVHQZXvhljXklAkBSgsQGficyM7A8851YKmoibELfuGWFz5Y7NfwBv5Jib8q64zTiaYg/0?wx_fmt=jpeg)

# Windows高危漏洞来袭？已有补丁不需惊慌！

山石网科安全技术研究院

**关于此漏洞**

CVE-2024-38077算是Windows平台近十年来比较罕见的可以稳定利用、影响广泛的远程零点击且不需认证的漏洞，山石网科在上个月就收到了微软MAPP的信息通报，利用还是有一定限制的，微软的评价也是Exploitation Less Likely。不过是影响的版本比较广泛，涉及Windows 2000后所有Windows服务器操作系统。通过该漏洞，攻击者只须针对开启了远程桌面授权服务（Remote Desktop License Service)的服务器发送特制数据包，即可完全控制目标系统，获得最高的SYSTEM权限。研究者将其命名为MadLicense（狂躁许可），POC已经在GitHub公开，有兴趣的研究者可自行验证。

**漏洞修复和防御**

所有未安装2024年7月补丁的Windows服务器操作系统均受此漏洞影响，大家可以检查服务器上的Remote Desktop Licensing服务是否启动，或者查看lserver.dll文件版本是否为易受攻击版本。

最好的防御是尽快安装微软官方的相关补丁更新。如非必要就直接关闭Remote Desktop Licensing服务，这个服务会影响远程桌面授权认证和分发，可能导致远程桌面出现问题影响正常业务或降低远程桌面安全性。毕竟POC已经公开，估计很快就会有更好的利用方式，避免再次出现永恒之蓝这种严重的勒索攻击。

山石网科作为全球知名的安全厂商一直和微软都有安全漏洞情报上的合作，同时也是国内为数不多的微软主动防护计划（MAPP）成员，获得了微软颁发的MAPP（Microsoft Active Protections Program）优秀合作厂商奖杯，在每个月获得微软的漏洞同步信息之后，我们都会在第一时间进行分析验证并把相关防御规则加入到全系列的安全产品当中。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

山石网科安全技术研究院

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

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