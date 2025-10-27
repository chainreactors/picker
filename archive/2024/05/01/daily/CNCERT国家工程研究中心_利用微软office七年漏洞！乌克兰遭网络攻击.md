---
title: 利用微软office七年漏洞！乌克兰遭网络攻击
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247544353&idx=4&sn=c4345a7d4befb2ee37dd1dd4f44a2722&chksm=fa9398e0cde411f60ca41b0d019e560a98f379bdea923b94060a4e567e17cc7d0b4c886547bf&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-05-01
fetch_date: 2025-10-06T17:19:06.590683
---

# 利用微软office七年漏洞！乌克兰遭网络攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176mzyzRZwSJ9O4PB67Yn0SkHwPGOHaPKibNxmiccTKZdoJu8NfQJcB6dmWBALjDDU3CHHXG3pARDRj7w/0?wx_fmt=jpeg)

# 利用微软office七年漏洞！乌克兰遭网络攻击

网络安全应急技术国家工程中心

# **摘要**

网络安全研究人员发现，这次针对乌克兰的行动利用了微软Office中一个近七年的漏洞，将Cobalt Strike传送到被攻击的系统上。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QmbJGbR2j6yicxoGy6Kym2HBVkDdq1tHgAibibqm0u5kzDpziaR7Yv3K7IpsXfS6kWo31NVewvu65VxNT6x2yc5v6g/640?wx_fmt=jpeg&from=appmsg&wxfrom=13)

这次攻击链在2023年底发生，据Deep Instinct公司称，攻击者使用了一个PowerPoint幻灯片文件("signal-2023-12-20-160512.ppsx")作为起点，文件名暗示它可能是通过Signal即时通讯应用分享的。

尽管如此，实际上并没有证据表明PPSX文件是以这种方式分发的，尽管乌克兰计算机应急响应小组(CERT-UA)已经发现了两次不同的活动，它们都使用了这个通讯应用作为恶意软件的传播途径。

就在上周，该机构披露，乌克兰武装部队正日益成为UAC-0184组织通过通讯和约会平台传播恶意软件的目标，这些恶意软件包括HijackLoader（又名GHOSTPULSE和SHADOWLADDER）、XWorm和Remcos RAT，以及开源程序如sigtop和tusc，用于从计算机中窃取数据。

"PPSX（PowerPoint幻灯片）文件似乎是美国军队的一个旧版清雷刀（MCB）使用说明书，"安全研究员Ivan Kosarev说。"PPSX文件包含了一个远程关联到外部OLE对象的链接。"

这涉及到对CVE-2017-8570（CVSS评分：7.8）的利用，这是一个现已修补的Office远程代码执行漏洞，如果攻击者能够说服受害者打开一个特制的文件，就可以执行任意操作，加载托管在weavesilk[.]space上的远程脚本。

这个高度混淆的脚本随后启动一个包含JavaScript代码的HTML文件，该文件通过Windows注册表在主机上建立持久性，并且释放一个伪装成Cisco AnyConnect VPN客户端的下一阶段有效载荷。

该有效载荷包含一个动态链接库（DLL），最终将一个破解的Cobalt Strike Beacon（一个合法的渗透测试工具）直接注入到系统内存中，并等待来自命令和控制（C2）服务器("petapixel[.]fun")的进一步指令。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QmbJGbR2j6yicxoGy6Kym2HBVkDdq1tHgpKHlBNdD324Gvxx2zlzqicjfk0FV15IfGjFbZsXE8hWB8uYdUH8CzCA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

这个DLL还包含了一些功能，可以检查它是否在虚拟机中执行，并规避安全软件的检测。

Deep Instinct表示，它既无法将这些攻击与特定的威胁行为者或组织联系起来，也不能排除这是一次红队演练的可能性。目前还不清楚入侵的确切目标是什么。

"诱饵包含了与军事相关的内容，这表明它是针对军事人员的，"Kosarev说。

"但是，域名weavesilk[.]space和petapixel[.]fun伪装成了一个不太知名的生成艺术网站（weavesilk[.]com）和一个流行的摄影网站（petapixel[.]com）。这两者并无关联，我们对于攻击者为何会特意使用这两个域名来欺骗军事人员感到有些困惑。"

# **Sandworm针对乌克兰的关键基础设施#**

这次披露是在CERT-UA揭示了大约20家乌克兰的能源、水和供暖供应商已经成为一个名为UAC-0133的俄罗斯政府赞助的组织的目标之后，该组织是Sandworm（又名APT44、FROZENBARENTS、Seashell Blizzard、UAC-0002和Voodoo Bear）的一个子集，该组织对乌克兰进行了大量的破坏性行动。

这些攻击旨在破坏关键操作，涉及使用像Kapeka（又名ICYWELL、KnuckleTouch、QUEUESEED和wrongsens）及其Linux变种BIASBOAT，以及GOSSIPFLOW和LOADGRIP等恶意软件。

GOSSIPFLOW是一个基于Golang的SOCKS5代理，而LOADGRIP是一个用C编写的ELF二进制文件，用于在被攻击的Linux主机上加载BIASBOAT。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QmbJGbR2j6yicxoGy6Kym2HBVkDdq1tHgQvdWA4mRQpuKWxiczOEiciabFoQIywRicSsbYRZvaMHGOIajYHYcSJSf4w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QmbJGbR2j6yicxoGy6Kym2HBVkDdq1tHgQvdWA4mRQpuKWxiczOEiciabFoQIywRicSsbYRZvaMHGOIajYHYcSJSf4w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

Sandworm是一个多产且高度适应性的威胁组织，与俄罗斯联邦武装力量总参谋部主要指挥部的74455部队有关。它自2009年以来就已知活跃，该对手还与三个黑客和泄露黑客活动人物如XakNet Team、CyberArmyofRussia\_Reborn和Solntsepek有关。

由俄罗斯军事情报部门赞助，APT44是一个动态且在操作上成熟的威胁行为者，自2022年1月以来，他们积极参与全方位的间谍、攻击和影响操作，"Mandiant公司说，描述这个持续性威胁（APT）正在进行多管齐下的努力，以帮助俄罗斯在冲突时获得优势。

原文来源：E安全

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

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