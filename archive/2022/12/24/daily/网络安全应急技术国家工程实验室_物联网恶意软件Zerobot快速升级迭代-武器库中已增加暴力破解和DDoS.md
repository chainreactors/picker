---
title: 物联网恶意软件Zerobot快速升级迭代-武器库中已增加暴力破解和DDoS
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247533470&idx=1&sn=90174499cffeb7b1bbf42010c6b9e14d&chksm=fa93f55fcde47c4907f8cc44588a37a1b816d5cf0a569283af4afbee9d2c1a65f2c43e29f51a&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2022-12-24
fetch_date: 2025-10-04T02:26:12.262208
---

# 物联网恶意软件Zerobot快速升级迭代-武器库中已增加暴力破解和DDoS

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176nq1AmeUibe5dWiat6g4Eu31U7EWA0BibuibYicQw35Fmgkq9YeQ2xOQua5KJX9dqEn5E5KGS9o4erVUAg/0?wx_fmt=jpeg)

# 物联网恶意软件Zerobot快速升级迭代-武器库中已增加暴力破解和DDoS

网络安全应急技术国家工程中心

微软安全分析师近日发文表示，最近发现的一个通过物联网(IoT)漏洞实施网络攻击的僵尸网络增加了暴力破解和分布式拒绝服务(DDoS)攻击向量，以及将新漏洞武器化以丰富强大其武器库。据微软安全威胁情报中心(MSTIC)称，Zerobot是Fortinet研究人员本月早些时候首次发现的恶意软件，随着威胁的不断发展，该恶意软件的更新迭代为更高级的攻击铺平了道路。MSTIC在12月21日的博客文章中透露，威胁参与者已将Zerobot更新到1.1版，现在可以通过DDoS攻击资源并使其无法访问，从而扩大了攻击和进一步实施危害的可能性。研究人员表示，成功的DDoS攻击可能会被威胁行为者用来勒索赎金、分散其他恶意活动的注意力或破坏运营。几乎在每一次攻击中，目标端口都是可定制的，购买该恶意软件的威胁行为者可以根据他们的目标实施定制化攻击。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ss7c5mF5JlRdbybv33KsIX23x1XVvjo719FG4brvOxRLGVMjNISBQxakWRvHbcFsosRhWwicPo8LlBZNs6CecqQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

**Zerobot是什么？**

Zerobot是一种基于Go的僵尸网络，主要通过物联网和Web应用程序漏洞传播，是不断演变的威胁的一个例子，运营者不断向恶意软件添加新的攻击和功能。

Zerobot影响各种设备，包括防火墙设备、路由器和摄像头，将受感染的设备添加到分布式拒绝服务(DDoS)僵尸网络中。使用多个模块，该恶意软件可以感染构建在不同体系结构和操作系统上的易受攻击的设备，找到要感染的其他设备，实现持久性并攻击一系列协议。Microsoft将此活动跟踪为DEV-1061。

Zerobot的最新发行版包括其他功能，例如利用Apache和Apache Spark中的漏洞（分别为CVE-2021-42013和CVE-2022-33891），以及新的DDoS攻击功能。

Microsoft使用DEV-####名称作为未知、新兴或发展中的威胁活动集群的临时名称，允许Microsoft将其作为一组独特的信息进行跟踪，直到我们对威胁的来源或身份达到高度信任为止活动背后的参与者。一旦满足定义的标准，DEV组就会转换为指定的威胁行为者。

**暴力破解和其他策略**

Fortinet研究人员已经跟踪了Zerobot的两个先前版本——一个非常基础，另一个更高级。僵尸网络的主要攻击模式最初是针对各种物联网设备——包括来自D-Link、华为、RealTek、TOTOLink、Zyxel等的产品——通过在这些设备中发现的缺陷，然后传播到网络上连接的其他资产传播恶意软件和发展僵尸网络的方法。

微软研究人员现在已经观察到僵尸网络在对设备的攻击中变得更加激进，使用新的暴力向量来破坏安全性较弱的物联网设备，而不是仅仅试图利用已知的漏洞。

微软研究人员在博文中写道：“物联网设备通常暴露在互联网上，使未打补丁和安全保护不当的设备容易受到威胁行为者的利用。” “Zerobot 能够通过使用默认或弱凭据的不安全配置对易受攻击的设备进行暴力攻击来传播。”

微软研究人员称，该恶意软件试图通过SSH和telnet在端口23和2323上使用物联网设备的八个常用用户名和130个口令的组合来获得设备访问权限，以传播到设备。仅在他们的观察中，MSTIC团队就发现了默认端口22和23上的大量SSH和telnet连接尝试，以及尝试打开端口并通过端口敲门在端口80、8080、8888和2323上连接到它们。

Zerobot 1.1除了具备之前版本恶意软件的功能和攻击方式外，还增加了DDoS攻击能力。这些功能允许威胁行为者瞄准资源并使其无法访问。威胁行为者可能会利用成功的 DDoS攻击来勒索赎金、分散其他恶意活动的注意力或中断运营。在几乎每一次攻击中，目标端口都是可定制的，购买恶意软件的威胁行为者可以根据他们的目标修改攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/ss7c5mF5JlRdbybv33KsIX23x1XVvjo7gQRWicOgtcuDYpxBricXz1LWdk8TeZWu0vaM30vWHQRrfuszicT9TF0qA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/ss7c5mF5JlRdbybv33KsIX23x1XVvjo7ord43ZXUCxB9JiaWTUhnwwNap7Qx1cjKkficicXeFYxMyegiaVFRkqx6Yw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**扩展的安全漏洞利用列表**

然而，Zerobot并没有放弃其访问设备的原始方式，甚至还扩展了这种做法。在其新版本之前，Zerobot已经可以利用各种设备中的20多个漏洞，包括路由器、网络摄像头、网络附加存储、防火墙和许多知名制造商的其他产品。

研究人员发现，该僵尸网络现已在Apache、Roxy-WI、Grandstream和其他平台中发现了七个新漏洞利用漏洞。

MSTIC还发现了新的证据，表明Zerobot通过破坏具有已知漏洞的设备进行传播，这些漏洞未包含在恶意软件二进制文件中，例如CVE-2022-30023，Tenda GPON AC1200 路由器中的一个命令注入漏洞，他们补充说。

除了对设备进行暴力尝试外，Zerobot还利用了数十个漏洞，恶意软件运营商在滚动的基础上添加这些漏洞以获得访问权限并注入恶意负载。Zerobot 1.1包含几个新漏洞，如下表所示。

![](https://mmbiz.qpic.cn/mmbiz_png/ss7c5mF5JlRdbybv33KsIX23x1XVvjo7f4WY0x2R3QUJkubGiaWDfllye8SCYCaaWCWYlJNV4g3CaTxVYiaZpq2g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**Zerobot成功入侵后的行动**

研究人员还进一步观察了Zerobot在获得设备访问权限后的行为。一方面，它会立即注入恶意负载——可能是一个名为“zero.sh”的通用脚本 ，用于下载并尝试执行机器人程序，或者是一个用于下载特定架构的Zerobot二进制文件的脚本，他们说。

研究人员写道：“尝试下载不同Zerobot二进制文件的bash脚本试图通过暴力识别架构，尝试下载和执行各种架构的二进制文件，直到成功为止。”

根据设备的操作系统，恶意软件具有不同的持久化机制。恶意软件操作员使用持久性策略来获取和维护对设备的访问。虽然Zerobot 无法传播到Windows 机器，但研究人中已发现了几个可以在Windows上运行的样本。

一旦Zerobot实现持久化，它就会扫描暴露在互联网上并可能被感染的其他设备，方法是随机生成一个介于0-255之间的数字，并扫描所有以此值开头的IP。

微软研究人员写道：“使用名为new\_botnet\_selfRepo\_isHoneypot的功能，该恶意软件试图识别蜜罐IP地址，网络诱饵使用这些地址来吸引网络攻击并收集有关威胁和尝试访问资源的信息。” “此功能包括61个IP子网，防止扫描这些IP。”

Zerobot 1.1使用针对各种架构的脚本，包括ARM64、MIPS 和 x86\_64。研究人员还观察了Windows和Linux设备上的僵尸网络样本，展示了基于操作系统的不同持久化方法。

**如何防范？**

Fortinet研究人员已经强调了组织立即更新到受Zerobot影响的任何设备的最新版本的重要性。根据Netacea去年发布的一份报告，鉴于企业每年因不必要的僵尸网络攻击损失高达2.5亿美元，危险是真实存在的。

为了帮助确定一个组织是否容易受到攻击，微软研究人员在他们的帖子中包含了一份更新的CVE 列表，Zerobot可以利用这些列表。MSTIC团队还建议组织使用具有跨域可见性和检测功能的安全解决方案来检测Zerobot恶意软件变体和与威胁相关的恶意行为。

微软表示，企业还应采用全面的物联网安全解决方案，以实现对所有物联网和运营技术(OT)设备的可见性和监控、威胁检测和响应，以及与SIEM/SOAR和扩展检测和响应 (XDR) 平台的集成。

研究人员表示，作为该策略的一部分，他们应通过将默认口令更改为强口令并阻止 SSH进行外部访问以及使用包括VPN服务在内的最低权限访问来进行远程访问，从而确保设备的安全配置。

他们说，避免Zerobot攻击危害的另一种方法是使用全面的安全解决方案来强化端点，该解决方案管理员工可以使用的应用程序并为非托管解决方案提供应用程序控制。该解决方案还应及时清理位于组织设备上的未使用和过时的可执行文件。

**参考资源：**

1.https://www.microsoft.com/en-us/security/blog/2022/12/21/microsoft-research-uncovers-new-zerobot-capabilities/

2.https://www.darkreading.com/threat-intelligence/zerobot-adds-brute-force-ddos-iot-attack-arsenal

原文来源：网空闲话

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

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