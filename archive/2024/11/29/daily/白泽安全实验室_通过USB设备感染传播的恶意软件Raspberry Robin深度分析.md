---
title: 通过USB设备感染传播的恶意软件Raspberry Robin深度分析
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492438&idx=1&sn=ddbd62d5303ea7775fcfff9eeb7ee294&chksm=e90dc97cde7a406a9e7e62a23a12cf1df022a3d4edd39f2a506602b238c3edb4caab47968347&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-11-29
fetch_date: 2025-10-06T19:18:53.596089
---

# 通过USB设备感染传播的恶意软件Raspberry Robin深度分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 通过USB设备感染传播的恶意软件Raspberry Robin深度分析

BaizeSec

白泽安全实验室

**1. 事件概述**

Raspberry Robin（也称为Roshtyak）是一种先进的恶意下载器，自2021年被发现以来，因其独特的二进制混淆技术、广泛的反分析方法和一系列权限提升漏洞而出名。这种恶意软件能够通过感染USB设备传播，主要针对商务专业人士，其复杂性和隐蔽性对全球网络安全都构成了重大挑战。Raspberry Robin的传播和执行涉及到多个层次的技术，包括代码模拟检测、解压缩、反分析等，其中第六层包含了大部分反分析技术，并在检测到分析环境时部署诱饵有效载荷。

**2. 攻击技术特点分析**

**通过USB设备传播：**Raspberry Robin利用USB设备作为其主要的初始感染媒介，通过放置具有诱惑性的文件或图标，诱使用户执行它们。恶意软件利用操作系统的自动播放功能，通过修改USB设备的固件或创建恶意的autorun.inf文件，实现自动执行。一旦Raspberry Robin在主机上建立据点，它会寻找连接到同一网络的其他设备，并尝试通过RDP或SMB协议进行传播，迅速在内网中扩散。

**多层执行与反分析：**Raspberry Robin通过一系列复杂的执行层来隐藏其核心功能，每一层都有特定的任务，如解密下一层或执行反分析技术。例如，第一层使用段寄存器GS/CS进行代码模拟检测，并（XOR）解密下一层。第二层是解压缩（使用修改后的aPLib算法）并执行下一层。第三层通过测量CPU性能来验证是否身处分析或沙箱环境中，确定是否执行，并使用RC4算法解密下一层。第四层解密（通过XOR）并执行下一层。第五层解压缩（使用修改后的aPLib算法）并执行下一层。第六层则运行了一系列反分析技术，并在检测到非分析环境时执行诱饵有效载荷。否则，它将使用Rabbit流密码解密下一层。第七层主要是解密（使用XOR）并执行下一层。第八层是解压缩（使用修改后的aPLib算法）并执行核心层。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIPBGTYnefbjbuPE9u6kRcbuApT629ib7PVzsoy7DiajTX1fibQKDjkMw7fSedCQTb5FKzL7BhoJ3fd6w/640?wx_fmt=png&from=appmsg)图 1 Raspberry Robin  多层架构示意图

**混淆技术：**Raspberry Robin广泛使用了控制流平坦化、混合布尔算术（MBA）操作和自定义加密算法。每个混淆的函数都包含一个加密的数组表，用于解密字符串和映射变量。

**核心层功能：**核心层的功能包括同步和代码执行行为、逃避和反分析、隐蔽的注册表修改、持久性、网络传播、本地权限提升和网络通信。

**网络通信与C2服务器：**Raspberry Robin通过建立与C2服务器的通信来接收进一步的指令。通过USB设备传播后，恶意软件会利用TOR网络进行通信，以增加其匿名性和抗检测能力。这种通信机制使得攻击者能够远程控制受感染的设备，并部署额外的有效载荷。

**漏洞利用与权限提升：**在某些情况下，Raspberry Robin还会利用已知的系统漏洞来提升其在受感染系统上的权限。这些漏洞包括本地权限提升漏洞，如CVE-2024-26229和CVE-2021-31969，使得恶意软件能够以更高权限执行操作，进一步扩大其控制范围。

**3. 总结**

Raspberry Robin的分析揭示了网络攻击者在恶意软件领域的技术进步。这种恶意软件通过利用USB设备、操作系统特性和网络通信，能够有效地在目标环境中建立持久性，并为进一步的网络攻击奠定基础。Raspberry Robin的复杂性和隐蔽性对全球网络安全构成了重大威胁，全球组织必须加强其网络安全措施，以抵御这类日益复杂的威胁。

参考链接：

https://www.zscaler.com/blogs/security-research/unraveling-raspberry-robin-s-layers-analyzing-obfuscation-techniques-and

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