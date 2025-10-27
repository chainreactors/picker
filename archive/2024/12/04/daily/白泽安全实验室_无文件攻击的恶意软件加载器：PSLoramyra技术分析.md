---
title: 无文件攻击的恶意软件加载器：PSLoramyra技术分析
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492450&idx=1&sn=e25fe33cdbf7b2905dddbe3f503934ad&chksm=e90dc948de7a405edc87eb9a76f2f74ab72838e0a7505799c3f6957cce0688a33c3aa6c0fa18&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-12-04
fetch_date: 2025-10-06T19:39:43.802472
---

# 无文件攻击的恶意软件加载器：PSLoramyra技术分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 无文件攻击的恶意软件加载器：PSLoramyra技术分析

BaizeSec

白泽安全实验室

#### **1. 事件概述**

PSLoramyra是一款被归类为无文件（fileless）加载器的恶意软件，可以通过利用PowerShell、VBS和BAT脚本，直接在系统内存中注入并执行的恶意负载，从而绕过传统的检测方法。PSLoramyra恶意软件的设计目的在于在受感染的系统中引入额外的有效载荷，其“无文件”的感染过程意味着辅助恶意程序在内存中执行，不会在磁盘上留下直接痕迹。

PSLoramyra的感染链始于一个包含主要恶意负载和执行所需脚本的PowerShell脚本。该恶意软件还通过执行一个VBScript来确保持久性，该脚本设计为每两分钟运行一次，通过Windows任务计划程序来运行其他脚本，确保感染链的持续进行。在已知的PSLoramyra攻击活动事件中，目标进程是RegSvcs.exe——一个与.NET Framework相关的微软组件，用于注册和配置组件。PSLoramyra的这种直接内存执行方式，涉及到引入一个.NET程序集，其中调用的Execute方法会将恶意代码注入到一个合法进程中。这种复杂的恶意软件对个人用户和企业都构成了严重威胁，因为它不仅能够导致多重系统感染，还可能造成数据丢失、隐私泄露、财务损失和身份盗窃等严重后果。PSLoramyra的传播途径也是多样化的，包括受感染的电子邮件附件、恶意在线广告、社交工程、软件破解等。

#### **2. 技术过程分析**

PSLoramyra恶意软件的攻击过程是一个复杂且隐蔽的攻击链，它主要通过利用PowerShell、VBScript（VBS）和批处理文件（BAT）脚本来实现其无文件的网络攻击操作。这种无文件的攻击方式使得PSLoramyra能够在不留下硬盘痕迹的情况下，完全在计算机内存中运行，从而躲避传统安全工具的检测。

PSLoramyra恶意软件攻击感染过程开始于一个精心构造的PowerShell脚本，该脚本包含了主要的恶意代码和执行攻击所需的指令。PSLoramyra恶意软件还会利用Windows任务计划程序来确保其持久性，通过设置一个任务每两分钟运行一次特定的VBS脚本，继续攻击感染过程并确保其在系统中的持续存在。该恶意脚本的主要目的是将其恶意代码注入到合法的系统进程中。例如，在一次攻击中，PSLoramyra针对的是名为RegSvcs.exe的正版Windows组件，它是.NET Framework的一部分。通过使用.NET程序集，PSLoramyra能够将有害代码直接注入到这个受信任的进程中，使其在不被察觉的情况下运行。

PSLoramyra的执行链涉及多个脚本的协同工作。初始的PowerShell脚本负责生成roox.ps1、roox.bat和roox.vbs三个关键文件，这些文件共同构成了感染链的核心。roox.vbs作为起始点，负责启动roox.bat，而roox.bat则执行roox.ps1 PowerShell脚本。这个PowerShell脚本再进一步利用Reflection.Assembly.Load将主要恶意负载直接加载到内存中，并利用RegSvcs.exe来执行这个负载。该脚本还使用了简单的混淆技术，例如使用#字符，使检测更具挑战性。在整个攻击过程中，PSLoramyra展示了其高度的隐蔽性和复杂性。它不仅能够绕过基于磁盘文件的安全检测机制，还能够通过注入合法进程来避免被其它安全软件发现。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIPgvKF8Wc45XbibwsKTUnd4p4Y5MC5tbEezhfskpSmr6BDwfND4QYCH4QrRnDeZHjBVshmq6XVd3lA/640?wx_fmt=png&from=appmsg)图 1 PSLoramyra攻击的执行链

#### **3. 总结**

PSLoramyra恶意软件的兴起象征着网络威胁领域一个令人关注的趋势：无文件攻击的普及化。这种攻击手法通过在系统内存中执行恶意代码，巧妙地避开了基于磁盘的传统安全检测手段，从而极大地提升了其隐蔽性和防御难度。PSLoramyra展示了其高级的逃避技术，通过复杂的脚本执行链和系统进程注入，使得它能够在不留下明显痕迹的情况下活跃于受感染系统，进行数据窃取、间谍活动或其他恶意行为。在面对PSLoramyra及其同类恶意软件的攻击威胁，传统的网络安全防护措施已不再足够奏效。为了有效防御，必须采取更为全面和多层次的安全防御策略，特别是需要增强对系统内存的检测机制，以识别和阻止这类无文件攻击行为。PSLoramyra的复杂性和攻击能力提醒我们，网络安全防御必须要不断适应和进化，以应对这些不断演变的攻击威胁。

参考链接：

https://any.run/cybersecurity-blog/psloramyra-malware-technical-analysis/

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