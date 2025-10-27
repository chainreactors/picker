---
title: 游戏机黑客披露了“实际上无法修补”的PS4/PS5 漏洞
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247531881&idx=3&sn=431fbbfdd6d4289044979c28af52d62a&chksm=fa93cba8cde442bee88d05d015a39bcc32594e774108ceff530298c9ebcf698d371be8636943&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2022-10-13
fetch_date: 2025-10-03T19:47:37.884404
---

# 游戏机黑客披露了“实际上无法修补”的PS4/PS5 漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176k9OuKqdtNIHzZ0Db4q9lOrsHOLN3kG9Uc48VJrnS9P2ycDPNCmNMky6FELPvcQvMA1sRHvhocLiaQ/0?wx_fmt=jpeg)

# 游戏机黑客披露了“实际上无法修补”的PS4/PS5 漏洞

网络安全应急技术国家工程中心

知名的游戏机黑客 CTurt近日炮轰了PS4和PS5游戏机中一个“实际上无法修补”的漏洞，他详细说明了一种概念验证方法（https://www.youtube.com/watch?v=GIl1mR0HLnc），这种方法允许在索尼游戏机上安装任意的自制应用程序。

CTurt表示，一年前他通过漏洞悬赏计划向索尼披露了他编写的漏洞利用工具Mast1c0re，但看不到索尼发布补丁的迹象。这种攻击方法利用了在PS4（和 PS5）上运行某些PS2游戏的模拟器所使用的即时（JIT）编译中存在的错误。这种编译为模拟器提供了特殊权限，可以在应用程序层本身执行PS4就绪的代码（基于原始的S2代码）前一刻不断写入代码。

如果黑客控制该进程的两端，就可以编写系统认为合法且安全的特权代码。CTurt谈到PS4网络浏览器上的一个此后已修补的JIT漏洞时说：“由于我们将JIT系统调用用于预期用途，这其实不是漏洞，而是巧妙的花招。”

**趁虚而入**

为了控制模拟器，黑客理论上可以利用存在于几十年前的PS2游戏中任意数量的已知漏洞。虽然其中一些漏洞只需摁下按钮即可激活，但大多数漏洞需要使用一款已知的可被利用的游戏，访问存储卡上特殊格式的保存文件，从而导致缓冲区溢出，进而可以访问原本受保护的内存（多年来类似的漏洞被用于PSP和任天堂3DS黑客攻击）。

不过这种方法有点受限制，因为PS4和PS5无法直接识别标准的PS2光盘。这意味着任何可被利用的游戏都必须是这种形式：可以通过PSN下载的PS2-on-PS4游戏，或者是通过Limited Run Games等游戏发行商以与PS4兼容的物理光盘形式发布的少数PS2游戏。

将可被利用的PS2保存文件放到PS4上也不是简单的过程。CTurt不得不使用已经被黑入的PS4，对修改后的Okage Shadow King保存文件进行数字签名，让它可以与他的PSN ID协同使用。然后CTurt使用系统的USB保存导入功能，将该文件导入到目标系统上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29eiaYsD4Tw8dSwGib4iazdsM7V17gvMaX2LpW0ebTicOs6MdibAyye5cvq5W2KbgGSOic885iaZ93vArF9A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图1. CTurt以前的黑客活动显示PS2自制代码从未经修改的硬件上的DVD-R运行。

基本工作到位后，CTurt逐步演示了一系列复杂的缓冲区及堆栈溢出、存储器泄漏以及用来控制PS2模拟器的内存漏洞利用工具。获得这种控制权后，他能够访问内置加载程序功能，通过本地网络传输单独的PS2 ISO文件，然后告诉模拟器通过虚拟光盘加载该游戏。

虽然将其他PS2游戏加载到模拟器中很好，但CTurt的真正目的是以此作为跳板，进而在系统上运行任意的自制代码。

CTurt告诉媒体，黑客仍然需要利用单独的（并且可能是可修补的）内核漏洞来获得对PS4的“全面控制”。但是mast1c0re漏洞利用工具本身应该足以运行复杂的程序，包括JIT经过优化的模拟器，甚至可能一些盗版的商业PS4游戏。理论上来说，Mast1c0re还可以用作黑入PS5虚拟机管理程序的跳板，该虚拟机管理程序控制这款游戏机上的低级系统安全。

**发现不了，就修补不了**

虽然过去曾出现过PS4自制漏洞利用工具，但索尼一直在竭力发布固件更新，旨在使这些工具至少有些过时。但CTurt强调，索尼几乎不可能堵住造就mast1c0re的漏洞。这是由于这种可被利用的PS2模拟器版本与市面上每一款PS2-on-PS4游戏打包在一起，而不是作为游戏机操作系统的核心部分单独存储。

如果是物理PS2-on-PS4光盘，这意味着只要你在播放前拒绝任何在线更新，该漏洞应该会继续带来风险。如果是数字版本，即使该漏洞后来被修补，也有方法可以使用来自本地服务器的代理HTTP流量，降级到存储的、可被利用的版本。

CTurt表示，严格上来讲，它并非完全无法修补——但这款游戏机就是这么设计的，索尼不会改变它。一旦你拥有可被利用的游戏（数字版或物理版），索尼就很难从你的游戏机删除游戏或修补游戏。

PS2仿真“从根本上有悖于[索尼]自己的安全模型，因为它使特权代码没有现成的机制来修补未来的潜在漏洞”，CTurt写道。

虽然任天堂从任天堂eShop删除了可被利用的3DS游戏，试图尽量减小公开黑客活动造成的破坏，但CTurt特别指出，索尼尚未从PSN删除可被利用的PS2游戏。CTurt还特别指出：“PlayStation在报道一年后对我作出的官方回应是，他们决定不尝试修补这条攻击链。”

这一切都表明mast1c0re漏洞可能会继续存在。虽然目前这只是一种概念验证而已，但PlayStation黑客界似乎将来很可能会再接再厉0，在开发PS4和PS5自制代码方面创造众多的机会。

**参考及来源：**

https://arstechnica.com/gaming/2022/09/console-hacker-reveals-ps4-ps5-exploit-that-is-essentially-unpatchable/

原文来源：嘶吼专业版

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176njVOPvfib4X3jQ6GIHLtX8SSDvbpmcpr4uu3X7ELG7PDjdaLVeq4Er02ZoicTPvxrC6KCVH3bssUVw/640?wx_fmt=jpeg)

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