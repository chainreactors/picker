---
title: 2024 年第一季度 IT 威胁演变趋势分析
url: https://www.4hou.com/posts/qpP0
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-06-07
fetch_date: 2025-10-06T16:55:17.750947
---

# 2024 年第一季度 IT 威胁演变趋势分析

2024 年第一季度 IT 威胁演变趋势分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 2024 年第一季度 IT 威胁演变趋势分析

胡金鱼
[趋势](https://www.4hou.com/category/observation)
2024-06-06 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)680766

收藏

导语：网络攻击者经常使用合法工具来逃避检测系统，并将开发成本降至最低。

**有针对性的攻击**

**三角测量行动：最后的谜团**

去年六月，有关“三角行动”的一系列报告被正式发布。这是一个之前未知的 iOS 恶意软件平台，通过零点击 iMessage 漏洞进行传播，允许攻击者浏览和修改设备文件、获取存储在钥匙串中的密码和凭据、检索地理位置信息并执行其他模块，从而扩展对受感染设备的控制。

12 月下旬，全球研究和分析团队 (GReAT) 的专家在演讲中详细描述了攻击链，并首次介绍了攻击者如何利用 CVE-2023-38606 硬件漏洞。

![trng_final_mystery_en_01-1536x864.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240604/1717494061119307.png "1717492529104642.png")

最近的 iPhone 型号包含额外的基于硬件的安全保护，即使攻击者可以读取和写入内核内存，也无法完全控制设备——正如利用 CVE-2023-32434 漏洞进行的 Operation Triangulation 攻击中实现的那样。

攻击者能够使用 Apple 设计的 SoC（片上系统）的另一个硬件功能绕过这种基于硬件的安全保护：他们将数据、目标地址和数据哈希写入固件未使用的芯片的未知硬件寄存器中。

目前猜测这个未知的硬件功能可能是为了调试或测试目的而设计的，或者是错误添加的。由于固件没有使用它，暂不知道攻击者是如何学会使用它的。

**一种检测潜在 iOS 恶意软件的轻量级方法**

过去几年，研究人员分析了多台 iOS 设备上的 Pegasus 恶意软件感染情况。分析 iOS 移动感染的常用方法是检查加密的完整 iOS 备份或分析受影响设备的网络流量。然而，这两种方法都很耗时，而且需要很高的专业知识。这促使安全研究人员寻找一种更快、更简单的方法来识别可能的 iPhone 感染。

在分析过程中，安全研究人员发现感染在意外的系统日志shutdown.log中留下了痕迹。

这是一个基于文本的系统日志文件，可在每台移动iOS设备上使用。每个重启事件都记录在此文件中，同时记录了多个环境特征：这些日志文件可以包含数年前的条目，提供大量信息。

shutdown.log文件存储在sysdiagnose（sysdiag）存档中——这可以被认为是可以生成用于调试和故障排除的系统日志和数据库的集合。生成sysdiag的方法可能因iOS版本的不同而不同。不过，此存档通常位于操作系统常规设置中，具体位于“隐私和分析”下（确切的位置名称可能因iOS版本的不同而不同）。

创建存档通常只需几分钟。结果是一个大小约为 200-400MB 的 .TAR.GZ 文件，然后可以将其传输到分析机器。解压存档后，shutdown.log 文件位于 \system\_logs.logarchive\Extra 目录中。

此 sysdiag 转储分析是一种侵入性最低且资源占用较少的方法，使用基于系统的工件来识别可能的 iPhone 感染。它可用于从不同的角度补充感染识别。

**DinodasRAT Linux 植入程序针对全球实体**

2023 年 10 月初，在 ESET 发布了一篇关于针对 Windows 用户的名为 Operation Jacana 的活动的文章后，研究人员发现了 DinodasRAT（又名 XDealer）的新 Linux 版本。

代码和网络 IoC（入侵指标）与 ESET 描述的用于攻击圭亚那政府实体的 Windows 样本重叠。样本工件表明，此版本（根据攻击者的版本控制系统为 V10）可能已于 2022 年开始运行，尽管第一个已知的 Linux 变体（V7）尚未公开描述，可以追溯到 2021 年。

DinodasRAT 是一个用 C++ 编写的多平台后门，提供多种功能。此 RAT 允许攻击者监视目标计算机并收集敏感数据。该后门功能齐全，可让操作员完全控制受感染的机器，从而实现数据泄露和间谍活动。

DinodasRAT Linux 植入程序主要针对基于 Red Hat 的发行版和 Ubuntu Linux。根据遥测数据和自 2023 年 10 月以来对该威胁的持续监控，发现受影响最严重的国家和地区是中国、土耳其和乌兹别克斯坦。

**其他恶意软件**

**新的 macOS 后门窃取加密钱包**

去年 12 月，一些破解的应用程序在盗版网站上流传，并感染了木马代理。最近，安全研究人员发现一个新的 macOS 恶意软件家族正在利用破解的软件窃取加密钱包。

破解的应用程序是攻击者将恶意软件植入人们的计算机的最简单方法之一：要提升权限，他们只需要询问密码，这通常在软件安装期间不会引起怀疑。

然而，恶意软件攻击者想出的一些东西非常巧妙，例如将他们的 Python 脚本放在 DNS 服务器上的域 TXT 记录中。该脚本后来被添加到启动代理中，以无限循环下载并执行下一阶段的有效负载，因此恶意软件操作员可以根据需要向受感染的机器提供更新。最终的有效负载是一个后门，它可以以管理员权限运行脚本，并用受感染的版本替换 Exodus 和比特币加密钱包应用程序，这些版本会在钱包解锁过程中窃取秘密恢复短语。

**Coyote：一种多阶段银行木马**

银行木马的开发者一直在寻找新的方法来分发植入程序。在最近的一次调查中，研究人员发现了一种名为 Coyote 的新恶意软件，该恶意软件针对的是 60 多家银行机构的客户，主要来自巴西。

引起观察者注意的是其复杂的感染链，它利用了多种先进技术，使其有别于其他银行木马。Coyote 不使用 Delphi 或 MSI 安装程序进行分发，而是使用一种相对较新的工具来安装和更新 Windows 桌面应用程序，名为 Squirrel。通过这种方式，恶意软件作者希望将木马伪装成更新打包程序。

当 Squirrel 执行时，它最终会运行一个用 Electron 编译的 NodeJS 应用程序。此应用程序执行混淆的 JavaScript 代码，将本地文件夹中名为 temp 的所有可执行文件复制到用户的 Videos 文件夹内的 captures 文件夹中：然后从该目录运行已签名的应用程序。

感染链中一个有趣的元素是使用 Nim（一种相对较新的编程语言）来加载最后阶段。加载器的目标是解压 .NET 可执行文件并使用 CLR 在内存中执行它。这意味着加载器旨在加载可执行文件并在其进程中执行它，这让人想起了 Donut 的工作方式。

完成以上所有步骤后，Coyote 木马病毒就被执行了。

![Coyote_A_multi_staged_banking_trojan_abusing_the_Squirrel_installer_01.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240604/1717494062463372.png "1717492796130095.png")

Coyote感染链

Coyote 木马的目标与典型的银行木马行为一致。它会监视受感染系统上所有打开的应用程序，并等待用户访问特定的银行应用程序或网站。

**使用 QEMU 进行网络隧道传输**

网络攻击者经常使用合法工具来逃避检测系统，并将开发成本降至最低。网络扫描、捕获进程内存转储、泄露数据、远程运行文件，甚至加密驱动器——所有这些都可以通过受信任的软件完成。

为了在受感染的基础设施中立足并发起攻击，攻击者可以使用之前安装的恶意软件或通过公司的 RDP 服务器或公司 VPN 连接到网络（为此，攻击者必须能够访问具有适当权限的帐户）。

连接到受攻击组织的内部网络的另一种方法是使用实用程序在公司系统和对手的服务器之间设置网络隧道或转发网络端口，从而使攻击者能够绕过 NAT 和防火墙来访问内部系统。可用于在两个系统之间创建网络隧道的实用程序有很多，有些直接连接，而有些则使用代理，从而隐藏攻击者服务器的 IP 地址。

在调查一家大型公司的事件时，研究人员注意到其中一个系统内部存在异常恶意活动。分析这些工件后，发现攻击者已经部署并启动了 (a) Angry IP Scanner 网络扫描实用程序、(b) Mimikatz 密码、哈希和 Kerberos 票证提取器和 Active Directory 攻击工具，以及 (c) QEMU 硬件模拟器。

虽然前两个是不言自明的，但 QEMU 提出了一些问题；威胁分子对虚拟化器有什么用处？

我们发现 QEMU 支持虚拟机之间的连接：-netdev 选项会创建网络设备（后端），然后可以连接到虚拟机。因为无法可靠地确定攻击者如何在自己的服务器上运行 QEMU，因此研究人员决定设置一个由三个系统组成的床，如下所示：

**·**“InternalHost”位于网络内部，没有互联网访问，并在端口 3389 上运行 RDP 服务器。它模拟了无法访问互联网的隔离系统。

**·**“PivotHost”位于网络内部，但可以访问互联网。它模拟了被攻击者攻破的系统并用于访问InternalHost。

**·**“AttackerServer”托管在云端，模拟对手的服务器。

目标是从 AttackerServer 到达 InternalHost。下图显示了隧道的总体布局：

![QEMU_persistence_01-1455x1536.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240604/1717494064900771.png "1717493050260201.png")

网络隧道图

虽然使用合法工具执行各种攻击步骤对事件响应专业人员来说并不是什么新鲜事，但攻击者有时会想出一些意想不到的软件的巧妙用途，QEMU 就是这种情况。这也凸显了多层次保护的必要性，既包括可靠的端点保护，也包括专门的解决方案，以检测和防范复杂和有针对性的攻击，例如人为攻击。

文章翻译自：https://securelist.com/it-threat-evolution-q1-2024/112742/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?mtMo5u50)

#### 你可能感兴趣的

* [![]()

  AI部署热潮下潜在的网络安全风险](https://www.4hou.com/posts/6ME7)
* [![]()

  2025年夏季网络安全攻击事件激增](https://www.4hou.com/posts/mk4O)
* [![]()

  【梆梆安全监测】安全隐私合规监管趋势报告（5月1日－5月16日）](https://www.4hou.com/posts/OGpL)
* [![]()

  随着全球紧张局势加剧，针对能源行业的网络威胁激增](https://www.4hou.com/posts/1MDm)
* [![]()

  关于人工智能钓鱼攻击的分析](https://www.4hou.com/posts/RX7E)
* [![]()

  2024年勒索软件支付下降35%，总计8.135亿美元](https://www.4hou.com/posts/NGG8)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [AI部署热潮下潜在的网络安全风险](https://www.4hou.com/posts/6ME7)
  2025-09-30 12:00:00
* [2025年夏季网络安全攻击事件激增](https://www.4hou.com/posts/mk4O)
  2025-09-02 12:00:00
* [【梆梆安全监测】安全隐私合规监管趋势报告（5月1日－5月16日）](https://www.4hou.com/posts/OGpL)
  2025-06-06 16:28:40
* [随着全球紧张局势加剧，针对能源行业的网络威胁激增](https://www.4hou.com/posts/1MDm)
  2025-05-09 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [AI部署热潮下潜在的网络安全风险](https://www.4hou.com/posts/6ME7)

  胡金鱼
* [2025年夏季网络安全攻击事件激增](https://www.4hou.com/posts/mk4O)

  胡金鱼
* [【梆梆安全监测】安全隐私合规监管趋势报告（5月1日－5月16日）](https://www.4hou.com/posts/OGpL)

  梆梆安全
* [随着全球紧张局势加剧，针对能源行业的网络威胁激增](https://www.4hou.com/posts/1MDm)

  胡金鱼
* [关于人工智能钓鱼攻击的分析](https://www.4hou.com/posts/RX7E)

  胡金鱼
* [2024年勒索软件支付下降35%，总计8.135亿美元](https://www.4hou.com/posts/NGG8)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](http...