---
title: 黑客利用Linux eBPF传播恶意软件展开攻击活动
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492478&idx=1&sn=8cf4e1f8b4b3378e053529a9505884c3&chksm=e90dc954de7a4042aee3a16661669be7ee0d92a15145142c7a8108ac842e4e47f3202c136cbe&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-12-20
fetch_date: 2025-10-06T19:39:40.509774
---

# 黑客利用Linux eBPF传播恶意软件展开攻击活动

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 黑客利用Linux eBPF传播恶意软件展开攻击活动

BaizeSec

白泽安全实验室

网络安全研究人员近期披露了一起针对东南亚地区企业和用户的新型Linux恶意软件活动。该活动利用了Linux eBPF（扩展Berkeley包过滤器）技术，通过隐藏网络活动、收集敏感信息和绕过安全措施，使得攻击检测变得异常困难。

Linux eBPF是一种强大的扩展Berkeley包过滤器技术，最初设计用于在Linux操作系统中高效地处理网络数据包。Linux eBPF允许开发者在内核中运行自定义代码，而无需更改内核源代码或加载内核模块，这使得Linux eBPF成为监控和分析网络流量、优化系统性能、实现安全策略等领域的理想选择。

**攻击过程技术分析：**

* **Linux eBPF技术滥用：**

研究人员发现，攻击者滥用Linux eBPF技术，这是一种原本设计用于提供更好控制Linux操作系统网络功能的低级能力。Linux eBPF允许攻击者隐藏其网络活动，收集敏感信息，并绕过安全措施，这对于APT（高级持续性威胁）组织来说尤其有价值，因为它们寻求长期访问目标系统。

* **木马部署：**

在这次活动中，攻击者使用Linux eBPF加载了两个rootkit。第一个eBPF rootkit隐藏了第二个rootkit的存在，后者随后部署了一个远程访问木马（Trojan.Siggen28.58279或Trojan:Win32/Siggen.GR!MTB），该木马能够建立加密传输隧道，允许攻击者即使在私有网络内也能与受感染的设备通信。

* **公共平台作为命令控制中心：**

攻击者改变了他们存储恶意软件配置的方式。他们不再依赖私人命令和控制服务器，而是使用流行的、公开可访问的平台，如GitHub和博客。这种策略使得恶意流量看起来合法，因为它与正常网络活动相结合，同时也消除了攻击者维护单独控制基础设施的需要，这些基础设施更容易被检测和关闭。

自2023年以来，网络安全领域观察到恶意Linux eBPF软件的使用显著增加，这一趋势引起了业界的广泛关注。Linux eBPF技术因其在网络监控和系统性能优化方面的强大能力而被广泛采用，但同时也被网络攻击者用于增强其攻击手段。在这个背景下，多个恶意软件家族，包括Boopkit、BPFDoor和Symbiote，开始利用Linux eBPF技术发起攻击，显示出Linux eBPF在网络攻击中的新趋势。这些恶意软件通过不同的方式利用Linux eBPF技术：

* **Boopkit：**这是一个已知的恶意软件家族，它使用Linux eBPF技术绕过传统的安全检测机制，隐藏其恶意行为，使得攻击者能够在目标系统中维持持久访问。
* **BPFDoor：**这是一种基于Linux eBPF的rootkit，能够加载并执行恶意Linux eBPF程序，这些程序能够执行包括数据窃取和系统监控在内的各种恶意活动。
* **Symbiote：**这是另一个利用Linux eBPF技术的恶意软件，通过感染系统文件和进程，增强了攻击者对受感染系统的控制能力。

此外，Linux eBPF技术中发现的众多漏洞进一步加剧了安全风险。这些漏洞使得攻击者能够利用Linux eBPF的高级功能执行恶意操作，例如提升权限、执行远程代码或绕过安全监控。随着Linux eBPF技术的不断发展和普及，攻击者也在不断研究和开发新的利用方法，使得基于Linux eBPF的恶意软件变得更加复杂和难以检测。

参考链接：

https://hackread.com/hackers-exploit-linux-ebpf-malware-ongoing-campaign/

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