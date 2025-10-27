---
title: 一种新型横向移动技术后门：DCOM上传和执行
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492469&idx=1&sn=cdda14423f01b8a95db7cac517509baf&chksm=e90dc95fde7a404928ee1b2cf91a9bcfc095742888b04d041b9b5dd2106b88b0fdde53702b2b&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-12-17
fetch_date: 2025-10-06T19:42:45.088321
---

# 一种新型横向移动技术后门：DCOM上传和执行

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 一种新型横向移动技术后门：DCOM上传和执行

BaizeSec

白泽安全实验室

**一、事件概述**

在当今数字化时代，网络安全威胁层出不穷，攻击者不断寻找新的方法来突破系统的防线。网络安全厂商Deep Instinct的安全研究人员最近发现了一种新型且强大的横向移动技术——“DCOM上传和执行”，这种技术重新定义了攻击者如何利用分布式组件对象模型（DCOM）接口来执行远程代码。这项研究不仅详细描述了相关漏洞，还突出了一种先进的方法，利用Windows系统中的IMsiServer接口安装后门程序。DCOM是微软基于组件对象模型（COM）的一系列概念和程序接口，它支持不同计算机上的组件间的通信，不论它们是运行在局域网、广域网还是Internet上。DCOM允许应用程序实例化和访问远程计算机上COM对象的属性和方法。它使用远程过程调用（RPC）技术将组件对象模型（COM）的功能扩展到本地计算机之外，使得在远程系统上托管COM服务器端的软件可以通过RPC向客户端公开其方法。攻击者可以利用DCOM在拥有适当权限的情况下通过Office应用程序以及其他包含不安全方法的Windows对象远程执行命令。DCOM的一个关键特性是位置透明性，这意味着客户端程序无需知道组件程序的具体位置，就可以像访问本地资源一样访问远程资源。这种透明性为攻击者提供了便利，他们可以利用DCOM在远程主机上执行恶意代码，而无需深入了解底层网络协议的细节。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIO3ZTibXbhDjTj12QHAMtohNtpIWBU2gDHTNy1Y4DVRQcJEOuGHvxJIu6ZiaOyiaM2kmsLY3kZxuBgFA/640?wx_fmt=png&from=appmsg)图 1 COM接口和vtable

**二、技术细节及过程分析**

“DCOM上传和执行”攻击方法绕过了传统的DCOM加固机制，通过利用IMsiServer COM接口——Windows安装服务的一个组成部分来实现。这种攻击方法不依赖于常见的IDispatch接口，因此能够规避许多传统的检测机制。该技术被描述为“一种强大的新型DCOM横向移动攻击，允许在目标机器上写入自定义DLL，将它们加载到服务中，并使用任意参数执行它们的功能。”攻击者使用高级逆向工程技术深入到未记录的IMsiServer功能中，实现远程执行。

**攻击过程分为三个阶段：**

* **DLL创建和上传：**

攻击者使用IMsiCustomAction接口中的函数，将恶意DLL上传到目标的全局程序集缓存（GAC）中的可预测路径。

* **远程执行：**

攻击者使用LoadEmbeddedDLL方法加载有效载荷，然后调用CallInitDLL执行恶意DLL中导出的函数。

* **后门功能：**

执行后，攻击者可以远程与有效载荷交互，有效地在受害者的系统中嵌入后门。

**该项后门技术的关键特点：**

* **新颖的利用路径：**

这种攻击方法扩展了攻击面，包括了文档较少的接口，如IMsiServer，与传统针对IDispatch接口的DCOM攻击不同。

* **隐蔽的横向移动：**

通过利用不常见的COM对象，攻击绕过了许多传统的监控工具。

* **可预测的文件路径：**

自定义有效载荷被策略性地放置在GAC中，以确保可靠执行。

**三、事件总结**

该后门技术尽管攻击强大，但它也受到某些条件的限制：

* 攻击者和受害者系统必须位于同一域或内网中。
* 攻击者和受害者计算机必须与DCOM强化补丁一致，要么在两个系统上应用了该补丁，要么在两个系统上都不存在该补丁。
* 有效载荷必须是一个强命名的.NET程序集，可以是x86或x64。

攻击过程会留下了明显的攻击痕迹：

* 显示DCOM访问的远程认证日志。
* MSIEXEC进程与不寻常的子进程。
* 写入并从GAC加载的恶意DLL。

“DCOM上传和执行”技术揭示了横向移动攻击的复杂性和不断演变的趋势。这项研究通过绕过传统的利用路径，展示了那些被忽视的COM接口如何被转化为强大的攻击工具。研究人员在报告中警告说，这项研究显示了许多DCOM对象可能出人意料地被用于横向移动攻击，因此，必须对防御措施进行适当的调整和加强。

参考链接：

https://www.deepinstinct.com/blog/forget-psexec-dcom-upload-execute-backdoor

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