---
title: 十大未查出幕后组织的APT攻击
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247531783&idx=3&sn=d90f1c478c97d07051d5730275189a7c&chksm=c1e9f156f69e7840c3a575074e0a2567ca4ade5f7cea8c5c6534f3cb5f691a6c6dd2585319c0&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2022-10-18
fetch_date: 2025-10-03T20:07:39.684027
---

# 十大未查出幕后组织的APT攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogs8R8PzyaSEJ1PKicib1ECicuRDRzZDn5aWJ7E1fcvMkhDCX6HApHsIoA4Ayj1cMXicOBaQtQZDeaaQSg/0?wx_fmt=jpeg)

# 十大未查出幕后组织的APT攻击

关键基础设施安全应急响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogs8R8PzyaSEJ1PKicib1ECicuRZgicZZfbzGdOuX4ovF8FyKoD6dOKFtAuKaGz3FfBRlr9ERM0w2KXD4w/640?wx_fmt=jpeg)

**1.TajMahal**

早在2018年底，卡巴斯基的研究人员就发现了一个复杂的间谍框架，他们称之为“TajMahal”。它由两个不同的软件包组成，分别称为“Tokyo”和“Yokohama”，它们能够窃取各种数据，包括从受害者设备上盗窃的CD数据和发送到打印机队列的文件。每个软件包都包含许多恶意工具：后门、键盘记录器、下载器、编排器、屏幕和网络摄像头抓取器、音频记录器等。总共发现了多达80个恶意模块。

在第一次发现它之前，TajMahal项目已经活跃了至少5年。更为神秘的是，它唯一已知的受害者是一个知名的外交对象。谁是这次袭击的幕后主使，是否还有其他受害者，或者整个工具的开发是否只是针对一个特定目标，这些问题仍然没有答案。

**2. DarkUniverse**

DarkUniverse是研究人员在2018年发现并公布的另一个APT框架。从2009年到2017年，它在野外活动了至少八年，针对叙利亚、伊朗、阿富汗、坦桑尼亚、埃塞俄比亚、苏丹、俄罗斯、白俄罗斯和阿拉伯联合酋长国的至少20个民用和军事对象。该恶意软件通过带有恶意Microsoft Office文档附件的钓鱼电子邮件传播。它由几个模块组成，负责不同的间谍活动，如键盘记录、邮件流量拦截、截屏、收集各种系统信息等。

DarkUniverse在野外被发现的唯一示例是，他们复杂的ItaDuke恶意软件释放了一个名为“Visaform Turkey.pdf”的零日PDF漏洞。DarkUniverse目前尚未被公开公布，也不清楚2017年之后它发生了什么。

**3.PuzzleMaker**

2021年4月，研究人员利用复杂的零日漏洞链检测到几次有针对性的攻击。为了渗透系统，攻击者使用了谷歌Chrome RCE漏洞。虽然研究人员无法获取该漏洞的详细信息，但却非常怀疑存在问题的漏洞是CVE-2021-21224，该漏洞使攻击者能够在浏览器沙箱内执行任意代码。发起攻击后，攻击者利用Windows内核中的信息泄露漏洞CVE-2021-31955获取EPROCESS结构的内核地址，并利用另一个Windows内核漏洞CVE-2021-31956提升权限。

成功利用这些漏洞后，由四个模块组成的自定义恶意软件将被发送到受感染的系统。这些模块是一个stager、dropper、service和远程shell，最后一个是最终的有效负载。研究人员将APT称为“PuzzleMaker”。

已知APT活动的唯一薄弱环节是一种后利用技术，PuzzleMaker和CHAINSHOT恶意软件都使用了这种技术，至少有两个国家支持的攻击者也使用了这种技术。然而，这项技术是公开的，可以被不同的组织独立使用。

**4. ProjectSauron(又名Strider)**

ProjectSauron于2015年9月首次被发现，当时卡巴斯基反目标攻击平台在一个客户组织中检测到异常的网络流量。该流量来自一个可疑库，该库被加载到域控制器服务器的内存中，并注册为Windows密码过滤器，该过滤器可以访问管理帐户的纯文本密码。事实证明，它是针对俄罗斯、伊朗、卢旺达，可能还有意大利语国家的政府、电信、科学、军事和金融组织的复杂APT平台的一部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLyUyoIVqgqwI6nyPcFCFMcx5e5AuGtHWjEPdF8WwibicwkAoWYibguMoh8Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

ProjectSauron的名字来源于其配置中提到的“Sauron”

ProjectSauron平台采用模块化结构。它会针对每个受害者各自定义一个核心植入程序，它们具有不同的文件名和大小，以及针对目标环境自定义的时间戳。这样一来，在另一个组织中发现的程序对其他受害者来说就没有什么价值了。这些核心植入程序就像后门一样，可以下载额外的模块并在内存中运行命令。该模块执行特定的间谍功能，如键盘记录，窃取文件，或从受感染的计算机和连接的USB设备劫持加密密钥。一个特殊的模块负责通过受感染的USB驱动器访问气隙系统。

ProjectSauron背后的组织使用了复杂的指挥与控制基础设施，涉及美国和欧洲范围广泛的不同ISP和多个IP地址。攻击者尽了一切努力在其操作中不创建可识别的模式。唯一可以自信地说的是，如果没有一个民族国家赞助商，这种复杂程度很难实现。值得注意的是，这个组织可能从其他知名的APT学习过，比如Duqu、Flame、Equation和Regin。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLyJ6Lmsc3VE7ccqLyxCmVTAAcf6bZfIbU7MsaKCyLXEuoL5T474ibyX1Q/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

**5. USB Thief**

早在2016年，研究人员就发现了一种USB恶意软件，其特点是具有复杂的自我保护机制。它被称为“USB Thief”，由六个文件组成，其中两个是配置文件，而其他四个是可执行文件。这些文件被设计成按照预先定义的顺序执行，其中一些文件是aes128加密的。加密密钥是使用唯一的USB设备ID和某些磁盘属性生成的这使得解密和运行文件变得很困难，除非是在受感染的USB驱动器上。

其中三个可执行文件是加载下一阶段文件的加载程序。为了确保文件按正确的顺序加载，它们使用以前加载的文件的哈希作为名称。此外，有些文件检查父进程的名称，如果名称错误就终止。最后一个有效负载是一个数据窃取器，它查看配置文件以获取关于要窃取什么数据、如何加密数据以及在哪里存储数据的信息。数据总是被转移到受感染USB设备上的某个位置。

USB Thief中实现的另一个有趣的技术是使用某些应用程序的便携版本，如记事本，Firefox和TrueCrypt，诱骗用户运行第一个恶意软件加载程序。为了实现这一目标，它将自己作为插件或动态链接库注入到这些应用程序的命令链中。当用户运行受感染的应用程序时，恶意软件也会启动。这种恶意软件并不普遍，极有可能用于涉及人力资源的高度针对性攻击。

研究人员怀疑它可能与Lamberts APT组织有关：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLy9Gub6VVrnRwGjymIhn4k0hT4BFe4Y0QaGdicH3JNiaBEBCRoL3vXmK7Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**6. TENSHO (又名White Tur)**

2021年初，在搜索假冒政府网站的钓鱼页面时，普华永道公司的研究人员偶然发现了一个用于仿冒塞尔维亚国防部证书的页面。这个页面引导他们找到了一个被称为“TENSHO”或“White turr”的未知攻击者。这个攻击者至少从2017年开始活跃，使用了多种独特的技术和工具，包括武器化文档、HTA和PowerShell脚本、Windows可执行程序和模仿政府网站的钓鱼页面。

在其他工具中，TENSHO使用OpenHardwareMonitor开源项目，其表面目的是监控设备温度、风扇速度和其他硬件健康数据。攻击者传播恶意的OpenHardwareMonitor包，该包旨在以PowerShell脚本或Windows二进制文件的形式传递TENSHO的恶意软件。

到目前为止，尚未发现该攻击者与任何已知的APT组织之间存在联系。TENSHO的目标是塞尔维亚和斯普斯卡共和国(波斯尼亚-黑塞哥维那境内的一个对象)境内的组织，显示出非常具体的区域利益。

**7. PlexingEagle**

在阿姆斯特丹举行的2017年HITBSec会议上，Emmanuel Gadaix介绍了一个非常有趣的GSM网络间谍工具集的发现，该工具集可能是由一个非常先进的攻击组织部署的，是在对客户系统进行常规安全扫描时发现的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLyNDGrhsW2E4yOQDb2Pg3siaowX8KmdDMTAf2T5F3TicHrqZ47aGic9Q2lw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

该攻击方案最初是由Gadaix的团队在一台被攻击者用作操作基础的Solaris 10设备上发现的。这样，攻击者利用对GSM基础设施和网络的先进知识，对执法部门通常用于窃听电话的功能进行修复，以实现他们自己的机制来拦截感兴趣的电话。在攻击中使用的恶意软件使用LUA编写，研究人员看到其他高级攻击者使用的语言，比如Flame和Project Sauron背后的那些人。该攻击和所谓的 “Athens Affair”之间有许多相似之处，这两个示例是已知的唯一在野外抓获的攻击者的示例。

**8. SinSono**

2021年5月，向At&T、Verizon、T-Mobile等运营商提供短信路由服务的电信公司Syniverse检测到对其IT系统的未经授权访问。一项内部调查显示，2016年，一个未知的攻击者首次攻击了Syniverse的基础设施。五年来，他们一直在不被发现的情况下运行，访问了公司的内部数据库，并泄露了235名客户的电子数据传输(EDT)环境登录凭证。通过这些账户，攻击者可以访问高度敏感的消费者数据，例如通话记录和短信内容。

虽然该公司重置或停用了所有EDT客户的凭据，并联系了受影响的组织，但仍存在许多问题：例如，攻击者是否真得窃取了敏感数据。尽管该公司本身和一些依赖其服务的运营商没有发现重大攻击迹象，也没有试图破坏其流程，但研究人员既不知道谁是攻击者，也不知道他们的目标是什么。对与攻击有关的数据的分析表明，确认其背后的组织很困难。

**9. MagicScroll(又名AcidBox)**

MagicScroll是一个复杂的恶意框架，于2019年首次被Palo Alto的研究人员发现。这是一种多级恶意软件，已知的样本很少，已知的受害者只有一个，位于俄罗斯，于2017年受到攻击。MagicScroll的初始感染阶段信息目前是缺失的。第一个已知阶段是作为安全支持提供者创建的加载程序，这是一个通常提供某些安全功能（如应用程序身份验证）的DLL。MagicScroll滥用这个功能来实现对lass .exe进程的注入和可能的持久性。

加载程序的主要目的是解密和加载存储在注册表中的下一阶段模块。此模块利用VirtualBox驱动程序漏洞在内核模式下加载未签名的恶意驱动程序。据Palo Alto的研究人员说，以前在Turla活动中发现有攻击者利用了这一漏洞，但是没有迹象表明该攻击者与Turla活动背后的组织有任何联系。Palo Alto的研究人员还发现了与ProjectSauron的一些相似之处，但这些相似之处不足以表明这两个活动之间的联系。研究人员也没有发现MagicScroll和任何其他已知APT之间存在任何联系。

**10. Metador**

2022年9月，SentinelLabs首次曝光了Metador组织。它主要针对中东和非洲几个国家的ISP、电信公司和大学，其中至少有一名受害者被近十个不同的APT组织攻击过。

Metador运营着两个被称为“metaMain”和“Mafalda”的恶意软件平台，它们完全部署在内存中。metaMain平台是一个功能丰富的后门，它为攻击者提供了对受感染系统的长期访问。它可以记录键盘和鼠标事件，制作屏幕截图，下载和上传文件，并执行任意shell代码。

Mafalda是一个正在积极开发的后门。其最新版本的时间戳为2021年12月。它具有许多反分析技术，支持67条命令，比上一个版本的恶意软件多了13条。

除了典型的后门功能，metaMain和Mafalda还能够与其他未知的植入程序建立连接，并与这些植入程序交换数据。其中一种植入程序被称为“Cryshell”，充当metaMain或Mafalda与C2之间的中间服务器。有理由相信存在未知的Linux植入程序，可以将从Linux设备收集的数据发送到Mafalda。

目前还不清楚Metador背后的攻击者是谁以及他们的目标是什么。设计用于长时间不被发现的复杂恶意软件表明，这是一个由高端攻击者发起的网络间谍活动。至少有些C2响应是西班牙语的，这可能表明攻击者或它的一些开发人员说西班牙语。此外，在Metador的恶意软件中还发现了一些文化参考，包括英国流行朋克歌词和阿根廷政治漫画。痕迹的多样性使得很难确定它是在哪个国家运作的。其中一个假设是，该集团是一家高端承包商。

**参考及来源：**

https://securelist.com/top-10-unattributed-apt-mysteries/107676/

原文来源：嘶吼专业版

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogucKMiatGyfBHlfj74r3CyPxEBrV0oOOuHICibgHwtoIGayOIcmJCIsAn02z2yibtfQylib07asMqYAEw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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