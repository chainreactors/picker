---
title: 网络安全领域研究人员遭遇假PoC专项攻击
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492518&idx=1&sn=d4196de8b812e3a2d29209b50328cec0&chksm=e90dc98cde7a409a795581029d39c4e66bc71c3ad662c7e7c84782d0baae9a74a858889ab838&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2025-01-13
fetch_date: 2025-10-06T20:09:27.324135
---

# 网络安全领域研究人员遭遇假PoC专项攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 网络安全领域研究人员遭遇假PoC专项攻击

BaizeSec

白泽安全实验室

## **一、事件概述**

近期，网络安全领域接连曝出针对研究人员的假PoC（概念验证）攻击事件，引发业界高度关注。2024年12月，微软在当月的补丁星期二更新中修复了两个关键的LDAP漏洞，分别是CVE-2024-49112和CVE-2024-49113。其中，CVE-2024-49113是一个拒绝服务（DoS）漏洞。然而，就在漏洞修复后不久，Trend Micro发现了一个名为“LDAPNightmare”的恶意利用，它伪装成CVE-2024-49113的PoC，通过一个恶意代码仓库，诱骗安全研究人员下载并执行信息窃取型恶意软件。该恶意软件会从受感染机器上收集敏感数据，包括计算机信息、运行进程、网络详情和已安装更新等，并将其传输到攻击者控制的远程服务器。

无独有偶，2023年，Palo Alto Networks的研究人员也发现了一个新的恶意软件活动，该活动针对WinRAR的CVE-2023-40477漏洞。攻击者使用一个基于GeoServer漏洞CVE-2023-25157公开PoC代码修改而来的假PoC脚本，诱骗研究人员下载并执行VenomRAT有效载荷。一旦执行，该恶意软件会在系统中创建计划任务，每隔三分钟运行一次，以持续运行恶意软件，进而控制受害者系统、执行命令并窃取数据。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIOL9lndSXFheyYJd6wljicLkzBAtDc7maOGPzIicNBQYmHTycWb0b8WZibQlFhz06A9WIPsuyAenkscg/640?wx_fmt=png&from=appmsg)  包含 “poc.exe” 的存储库

**二、技术分析过程**

### **（1）LDAPNightmare攻击技术分析**

攻击者精心构建了一个看似合法的恶意代码仓库，其中的Python文件被替换为恶意可执行文件。当研究人员下载并执行该文件后，会释放并执行一个PowerShell脚本。该脚本随后建立计划任务，从Pastebin下载并执行另一个恶意脚本，最终收集受害者的公网IP地址，并将窃取的数据传输到外部FTP服务器。

SafeBreach Labs对CVE-2024-49113进行了深入研究，并开发出了一个PoC利用工具（概念验证漏洞），这个工具能够致使任何未打补丁的Windows服务器（不仅仅是域控制器）崩溃，来证明此漏洞的严重危害程度。根据Microsoft的分析发现，还可以进一步利用此漏洞导致远程代码执行。其次，研究人员确实验证了Microsoft的补丁修复了越界漏洞，并且该漏洞无法使修补的服务器崩溃。具体其攻击流程如下：

* 攻击者向受害服务器发送DCE/RPC请求。
* 受害服务器被触发，向攻击者的DNS服务器发送关于SafeBreachLabs.pro的DNS SRV查询。
* 攻击者的DNS服务器回复攻击者的主机名和LDAP端口。
* 受害服务器发送NBNS请求，以查找收到的主机名（攻击者的）的IP地址。
* 攻击者发送带有其IP地址的NBNS响应。
* 受害服务器成为LDAP客户端，向攻击者的机器发送CLDAP请求。
* 攻击者发送带有特定值的CLDAP转介响应包，导致LSASS崩溃并强制重启受害服务器。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIOL9lndSXFheyYJd6wljicLkTjnd3MN0gBvwFN2siaayKyfDExSotGXd699b0VR2JQWDQQ5yEny7Pfw/640?wx_fmt=png&from=appmsg)LDAPNightmare攻击流程

### **（2）VenomRAT恶意软件活动技术分析**

Palo Alto Networks的安全研究人员发现了一个针对WinRAR中 CVE-2023-40477 漏洞的新恶意软件活动。该活动使用虚假的概念验证（PoC） 脚本来诱骗研究人员下载并执行VenomRAT有效载荷。虚假的PoC脚本基于跟踪的GeoServer中漏洞CVE-2023-25157公开可用的PoC代码。该代码已经过修改，以删除有关CVE-2023-25157漏洞详细信息的注释，并添加了下载和执行带有“检查依赖关系”注释的批处理脚本的其他代码。该脚本在%TEMP%/bat.bat创建批处理文件，连接到特定URL并运行响应内容，进而下载可执行文件并保存到%APPDATA%\Drivers\Windows.Gaming.Preview.exe，同时创建计划任务，每三分钟运行一次该可执行文件，以实现持久化运行。Windows.Gaming.Preview.exe 可执行文件是VenomRAT的变体，VenomRAT是一种远程访问木马（RAT）。VenomRAT可用于窃取数据、在受害者系统上执行命令以及远程控制系统。

Palo Alto Networks研究人员认为，该攻击活动背后的攻击者是以网络安全研究人员为目标的，以便控制与访问他们的系统并窃取他们的数据。研究人员还认为，攻击者还可能正在使用受感染的系统对其他组织发起进一步的攻击活动。

## **三、结论与建议**

这些假PoC攻击事件凸显了网络安全领域面临的严峻挑战。攻击者利用研究人员对安全漏洞的关注和研究热情，通过伪装成PoC的恶意软件，成功渗透并窃取了研究人员的敏感信息，甚至可能进一步利用这些系统对其他组织发动攻击。因此，安全研究人员在下载和执行来自在线仓库的代码时必须保持高度警惕，优先选择官方来源，仔细审查仓库内容，验证仓库所有者或组织的真实性，并关注社区反馈，寻找可能的安全风险警示。同时，用户应确保及时更新软件至最新版本，避免点击不明链接，并使用有效的安全解决方案来检测和阻止恶意软件。

参考链接：

https://hackread.com/fake-poc-exploit-hit-cybersecurity-researchers-malware/

https://hackread.com/fake-poc-script-researchers-download-venomrat/

https://www.safebreach.com/blog/ldapnightmare-safebreach-labs-publishes-first-proof-of-concept-exploit-for-cve-2024-49113/

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