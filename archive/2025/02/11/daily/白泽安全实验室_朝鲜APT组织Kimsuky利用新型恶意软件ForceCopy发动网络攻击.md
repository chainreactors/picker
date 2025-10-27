---
title: 朝鲜APT组织Kimsuky利用新型恶意软件ForceCopy发动网络攻击
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492534&idx=1&sn=61ec9a86fe31f884fa4184f67dc9097e&chksm=e90dc99cde7a408ad941003edd68c1a1b59dfbc542e9105616e3e6ab01b75a4a9dea867d58db&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2025-02-11
fetch_date: 2025-10-06T20:39:25.386015
---

# 朝鲜APT组织Kimsuky利用新型恶意软件ForceCopy发动网络攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 朝鲜APT组织Kimsuky利用新型恶意软件ForceCopy发动网络攻击

BaizeSec

白泽安全实验室

**一．背景概述**

近日，网络安全研究人员发现，朝鲜高级持续性威胁（APT）组织Kimsuky正在使用一种名为ForceCopy的新型恶意软件，针对特定目标进行网络攻击。该恶意软件通过伪装成合法文件或软件更新，诱骗用户下载并执行，从而窃取敏感信息并实施进一步的网络入侵。此次攻击活动主要针对政府机构、外交部门、智库以及研究机构，显示出Kimsuky组织在情报收集和地缘政治操控方面的持续野心。根据ASEC（AhnLab安全应急响应中心）和Security Affairs的报道，ForceCopy恶意软件通过钓鱼邮件或恶意链接传播，攻击者利用社会工程学手段诱导目标打开恶意文件。一旦执行，ForceCopy会窃取受害者的文件、键盘输入、屏幕截图等敏感数据，并将其发送到攻击者控制的远程服务器。

**二、攻击过程分析过程：**

Kimsuky组织通过鱼叉式网络钓鱼攻击分发恶意\*.LNK快捷方式文件，这些文件伪装成PDF、Excel或Word文档等常见的Office文档，具有很强的欺骗性。当用户点击这些文件时，会触发PowerShell或Mshta脚本，从外部服务器下载并执行恶意软件。这种攻击方式利用了用户对常见文件格式的信任，以及对电子邮件附件的疏忽。

**初始感染与传播：**

ForceCopy恶意软件通常通过钓鱼邮件或伪装成合法软件的下载链接传播。攻击者会精心设计邮件内容，使其看起来像是来自可信来源，例如政府机构或知名企业。邮件附件通常为压缩文件（如ZIP或RAR），内含恶意可执行文件（如.exe或.dll）。

**恶意软件执行：**

当受害者打开并执行恶意文件后，ForceCopy会首先在系统中创建持久性机制，确保在系统重启后仍能继续运行。它通过修改注册表或创建计划任务来实现这一目标。

**数据窃取功能：**

ForceCopy的核心功能是窃取受害者的敏感数据。它会扫描系统中的特定文件类型（如文档、图片、数据库等），并将这些文件复制到临时目录中。随后，恶意软件会将这些文件压缩并加密，通过HTTP或FTP协议上传到攻击者控制的远程服务器。

**键盘记录与屏幕截图：**

除了文件窃取，ForceCopy还具备键盘记录和屏幕截图功能。它会记录受害者的键盘输入，捕捉敏感信息（如密码、账号等），并定期截取屏幕内容。这些数据同样会被上传到远程服务器，供攻击者进一步分析。

**隐蔽性与反检测机制：**

ForceCopy采用了多种反检测技术，以逃避安全软件的扫描。例如，它会检查系统中是否安装了常见的杀毒软件或沙箱环境，并在检测到这些环境时停止恶意行为。此外，ForceCopy还会使用加密通信协议，以隐藏其与C2（命令与控制）服务器之间的通信内容。

**C2服务器分析：**

研究人员通过分析ForceCopy的C2服务器，发现其IP地址主要位于朝鲜境内。攻击者通过多层代理和跳板服务器隐藏其真实位置，增加了追踪和取证的难度。

**三、恶意软件分析**

**PebbleDash和RDP Wrapper**

PebbleDash是一种后门恶意软件，用于远程控制受感染系统。RDP Wrapper是一种开源工具，用于在不支持远程桌面功能的Windows系统中启用远程桌面访问。Kimsuky组织对RDP Wrapper进行了自定义修改，增加了导出功能，以绕过安全检测。这种自定义的RDP Wrapper使得攻击者能够在不被发现的情况下，远程访问和控制受感染的系统。

**代理工具**

为了访问位于私有网络中的受感染系统，Kimsuky组织安装了代理恶意软件。这些代理工具作为中间人，允许攻击者通过RDP访问受感染系统。研究人员发现了三种主要类型的代理工具，它们通过创建互斥锁（如“MYLPROJECT”和“LPROXYMUTEX”）来标识自身，并从硬编码路径读取配置文件以执行代理功能。

**键盘记录器**

Kimsuky组织使用PowerShell脚本和可执行文件格式的键盘记录器来记录用户的按键信息。这些键盘记录器将记录的数据存储在特定路径下，如“%LOCALAPPDATA%\CursorCache.txt”和“C:\Programdata\jLog.txt”。通过这种方式，攻击者可以获取用户的敏感信息，如密码和账号。

**信息窃取器（forceCopy）**

forceCopy是一种信息窃取恶意软件，用于从浏览器目录中提取文件。它通过读取“Local State”文件中的密钥值，而不是直接窃取存储在浏览器中的凭据，从而绕过安全产品。forceCopy使用NTFS解析器库来读取文件，而不是常见的ReadFile() API，这种技术使得其更难以被检测到。

**加载器和注入器**

研究人员还发现了加载器和注入器恶意软件。加载器从“%SystemDirectory%\wbemback.dat”路径加载文件到内存中，而注入器则接收目标进程等信息作为参数，执行注入操作。此外，还发现了名为ReflectiveLoader的PowerShell脚本，这是一种开源的内存加载工具，用于在内存中加载恶意软件，从而避免被传统安全软件检测到。

**四、攻击目的分析**

Kimsuky组织的攻击目的主要是窃取敏感信息和远程控制受感染系统。通过使用PebbleDash和RDP Wrapper，攻击者可以远程访问和控制受感染的系统，进而获取系统中的重要数据。代理工具的使用使得攻击者能够访问位于私有网络中的系统，扩大了其攻击范围。键盘记录器和信息窃取器则用于获取用户的敏感信息，如账号密码和浏览器中的凭据。这些信息可能被用于进一步的网络攻击或出售给其他恶意组织。

参考链接：

https://securityaffairs.com/173991/apt/north-koreas-kimsuky-forcecopy-malware.html

https://asec.ahnlab.com/en/86098/

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