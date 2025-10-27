---
title: 新型Windows驱动签名绕过技术允许安装内核级rootkit
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492379&idx=1&sn=9f886c87e996c03fdda2fcd141290502&chksm=e90dc931de7a4027cd186106c27fa7b7bf656dbedf7b1024673934838bf7a6f8123cb0455e10&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-10-29
fetch_date: 2025-10-06T19:02:39.610496
---

# 新型Windows驱动签名绕过技术允许安装内核级rootkit

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 新型Windows驱动签名绕过技术允许安装内核级rootkit

BaizeSec

白泽安全实验室

在最近举办的BlackHat和DEFCON安全会议上，SafeBreach的安全研究员Alon Leviev揭露了一种创新的Windows驱动签名绕过技术。这项技术允许攻击者通过降级Windows内核组件至旧版本，来部署内核级别的rootkit，从而在目标计算机上获得深度控制。

这种降级攻击手法通过操纵Windows更新过程来实现。攻击者能够在不影响操作系统显示为完全修补状态的情况下，引入过时且易受攻击的Windows内核组件。尽管微软认为这种攻击没有越过其设定的安全界限，Leviev的研究却表明，通过获得内核代码的执行权限，这种攻击是完全可行的。为了证明这一点，Leviev开发了一个名为“Windows Downdate”的工具，该工具可以创建自定义的降级，使看似完全更新的系统重新面临已知漏洞的威胁。这样，攻击者就可以利用过时的组件，例如DLL、驱动程序和NT内核，对系统进行攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIMibyF8TlsPVc5DLLUneVtFpqiaFdn3IYYc5y7fH654jSKbAwuQePy0c1NA3bdoU3jAGug9DL1FQXoA/640?wx_fmt=png&from=appmsg)

Leviev在会议上强调，他能够让一台已经完全修补的Windows机器重新变得容易受到过去漏洞的攻击，这实际上使得“完全修补”这一概念在任何Windows机器上都变得毫无意义。尽管Windows内核安全性在过去几年有了显著的提升，Leviev还是成功地绕过了驱动签名强制执行（DSE）特性。他展示了攻击者如何加载未签名的内核驱动程序以部署rootkit恶意软件，这种软件能够禁用安全控制并隐藏可能暴露入侵行为的活动。

Leviev还亲自演示了如何在具有管理员权限的目标机器上，通过降级已修补的组件来绕过DSE保护，即使是在完全更新的Windows 11系统上。攻击者可以通过替换执行DSE的‘ci.dll’文件，用一个忽略驱动程序签名的旧版本，从而绕过Windows的安全检查。一旦组件被降级到易受攻击的版本，机器就需要像经历正常更新过程一样重新启动。

此外，Leviev还介绍了如何禁用或绕过微软的基于虚拟化的安全（VBS）。VBS为Windows创建了一个隔离的环境，用以保护关键资源和安全资产，例如安全内核代码完整性机制（skci.dll）和经过身份验证的用户凭据。然而，如果VBS没有配置为最大安全性（“强制性”标志），攻击者可以通过有针对性的注册表键修改来禁用它。

参考链接：

https://www.bleepingcomputer.com/news/security/new-windows-driver-signature-bypass-allows-kernel-rootkit-installs/

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