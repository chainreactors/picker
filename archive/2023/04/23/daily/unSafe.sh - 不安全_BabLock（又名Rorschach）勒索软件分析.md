---
title: BabLock（又名Rorschach）勒索软件分析
url: https://buaq.net/go-159936.html
source: unSafe.sh - 不安全
date: 2023-04-23
fetch_date: 2025-10-04T11:31:35.456866
---

# BabLock（又名Rorschach）勒索软件分析

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/265167611e5f1630c0fe6ea989c27bfe.jpg)

BabLock（又名Rorschach）勒索软件分析

导语：本文会分析一种名为BabLock（又
*2023-4-22 12:0:0
Author: [www.4hou.com(查看原文)](/jump-159936.htm)
阅读量:26
收藏*

---

导语：本文会分析一种名为BabLock（又名Rorschach）的勒索软件，它与LockBit有许多共同的特点。

本文会分析一种名为BabLock（又名Rorschach）的勒索软件，它与LockBit有许多共同的特点。

最近，一种名为BabLock(又名Rorschach)的勒索软件因其复杂而快速的攻击链而引起轰动，该软件使用的技术非常有创新性。虽然主要基于LockBit，但也汲取了其他不同勒索软件部分的功能，并最终组合成为BabLock(检测为Ransom.Win64.LOCKBIT.THGOGBB.enc)。LockBit现在已经开始第三次迭代。

我们会在本文中详细介绍它的攻击链，并分析其可能的起源。

**发现过程**

2022年6月，研究人员发现了一个勒索软件（后来被证明是BabLock），它使用了一种独特的附加扩展方式，而不是勒索软件攻击中通常使用的“一个样本，一个扩展”方法，我们发现，攻击者在针对这种特定感染的固定勒索软件扩展的顶部添加了从00-99的数值增量。因此，即使在一台受感染的计算机上，一次执行也可能产生多个扩展变体。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682045320199321.png "1681980129341644.png")

该勒索软件的独特特征是显示扩展的数值增量

调查发现，勒索软件总是以多组件包的形式部署，主要由以下文件组成：

加密的勒索软件文件config.ini；

恶意侧载DLL (DarkLoader, config.ini解密器和勒索软件注入器)；

用于加载恶意DLL的非恶意可执行文件；

使用正确密码执行非恶意二进制文件的CMD文件。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682045321144556.png "1681980138119502.png")

在一个感染实例中发现的主要勒索软件包

DarkLoader DLL将检查特定的命令，特别是--run，它会检查启动加密过程所需的正确的4位密码。虽然它对config.ini本身的内容的解包意义不大，但如果提供正确，DLL将执行基本的勒索软件例程。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682045322626937.png "1681980147184843.png")

如果在命令行中添加了正确的密码，勒索软件将继续进行整个加密过程

一旦DLL组件被非恶意可执行文件加载，它将立即在当前可执行文件的路径中查找config.ini文件。一旦找到它，DLL将解密config.ini，然后用一组特定的命令行执行notepad.exe。

在这个异常的活动中，研究人员发现了一些显著且一致的模式：

主要的勒索软件二进制文件通常以加密的config.ini文件的形式发送；

DarkLoader是通过使用合法可执行文件的DLL侧加载来执行的；

config.ini文件由专门为这些活动设计的自定义加载程序解密（检测为Trojan.Win64.DarkLoader）；

在同一受感染的计算机中，BabLock为每个文件的扩展名字符串附加一个从00到99的随机数（例如，extn00-extn99作为同一感染中的扩展名）；

任何DarkLoader DLL都可以用来解密任何加密的勒索软件config.ini，不需要特定的二进制配对。

DarkLoader DLL使用 Direct SysCall API来选择几个但重要的调用，以避免API读取分析。解密后的BabLock勒索软件总是使用VMProtect进行反虚拟化。

BabLock是通过挂钩API Ntdll的攻击注入加载的。RtlTestBit跳转到包含勒索软件代码的内存。

针对不同攻击的密码有几种变体，但它们都在一定的范围内。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682045323159415.png "1681980159143103.png")

提供给notepad.exe的命令行参数，用于在最近的攻击中加载和执行勒索软件

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682045324109959.png)

DLL使用几个直接的SysCall指令来避免API读取

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682045325100785.png "1681980176861786.png")

notepad.exe文件被注入到RtlTestBit的API调用线程中，该线程已被修复/挂起以跳转到恶意例程

**精妙的攻击技术**

在2022年6月首次发现BabLock时，研究人员搜索了类似的文件，发现这些文件的最早记录可以追溯到2022年3月。在发现这一点后，研究人员想弄清楚它是如何逃避检测这么长时间的。

自2022年6月以来，只有少数几起涉及该勒索软件的记录事件，包括最近的一起。由于数量较少，截至撰写本文时，还没有涉及地区、行业或受害者资料的统计数据。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682045326550003.png "1681980184113168.png")

BabLock勒索软件相关事件

然而，由于其显著特征，与BabLock相关的攻击可以很容易地识别。如上所述，在每次文件加密后，勒索软件都会在其硬编码扩展名中添加一个介于00-99之间的随机数字符串，这导致相同的勒索软件扩展多达100种不同的变体。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682045326845964.png "1681980193586702.png")

显示将00-99之间的随机数字符串附加到加密文件的代码片段

它还有一个相当复杂的执行例程：

它使用特定的数字代码来正确执行；

它将包拆分为多个组件；

它将实际有效负载拆解并隐藏到加密文件中；

它使用普通应用程序作为加载程序；

最后，BabLock使用公开可用的工具作为其感染链的一部分。我们发现最常用的工具如下：

Chisel-传输控制协议（TCP）和用户数据报协议（UDP）通道；

Fscan-一个扫描工具；

通过使用这两个工具，再加上拥有设置活动目录(AD)组策略的功能的BabLock/LockBit，攻击者可以毫不费力地在网络中翱翔。

**BabLock与LockBit等勒索软件的异同**

根据调查，BabLock使用的大多数例程与Lockbit（2.0）的关系密切。除此之外，它还与Babuk、Yanloowang等勒索软件存在相似之处。

最初，由于勒索通知的相似性，我们怀疑它与DarkSide勒索软件有关。然而，与DarkSide勒索软件不同，BabLock通过执行以下命令行来删除卷影副本：

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682045327442383.png "1681980201901221.png")

因此，研究人员立即排除了这种关系，因为它不同于DarkSide的操作，即通过Windows Management Instrumentation（WMI）和PowerShell删除卷影副本（这在技术上更复杂，很难通过标准监控工具检测到）。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682045328167075.png "1681980210730911.png")

勒索软件二进制文件解密并执行命令行以删除卷影副本

Lockbit(2.0)的一个共同特征是使用相同的组策略来生成桌面放置路径。同样，使用vssadmin删除卷影副本也是LockBit攻击中大量使用的例程（尽管也是许多现代勒索软件的常见例程）。尽管如此，这种相似之处还是不可思议的。此外，它运行相同的命令来为AD执行GPUpdate。因此，该勒索软件的检测仍属于LockBit家族。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682045329361906.png "1681980219186541.png")

将BabLock生成桌面放置路径的组策略（左）与LockBit的组策略进行比较（右）

BabLock看起来像是一个由不同的已知勒索软件家族拼接而成的怪物。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682045330361911.png "1681980229188550.png")

BabLock与其他勒索软件家族的相似之处

**总结**

研究人员发现BabLock时已经是其第三个迭代版了。然而，由于其大部分结构仍然类似于Lockbit v2.0，我们推测这可能来自另一个分支机构或组织。LockBit v3.0发布近一年来，即使在最近的攻击中，研究人员也没有发现BabLock的有效负载发生任何变化，这进一步说明它与实际的LockBit组织既没有联系。据分析，BabLock背后的攻击者成功地利用了LockBit v2.0的许多基本功能，并添加了不同勒索软件家族功能，以创建他们自己的独特变体，这些变体可能在未来进一步增强。

安全建议如下：

对资产和数据进行盘点；

识别授权和未经授权的设备和软件；

审计事件和事件日志；

管理硬件和软件配置；

仅在必要时授予员工角色的管理权限和访问权限；

监控网络端口、协议和服务；

建立只执行合法应用程序的软件许可列表；

实施数据保护、备份和恢复措施；

启用多因素身份验证(MFA)；

将最新版本的安全解决方案部署到系统的所有层，包括电子邮件、端点、web和网络；

注意攻击的早期迹象，例如系统中存在可疑工具；

实施多方面的方法可以帮助组织保护其系统（如端点、电子邮件、web和网络）的潜在入口点。

本文翻译自：https://www.trendmicro.com/en\_us/research/23/d/an-analysis-of-the-bablock-ransomware.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

![](https://www.4hou.com/captcha/flat?T7xrEuGD)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/微信截图_20230421104758.png)

  BabLock（又名Rorschach）勒索软件分析](https://www.4hou.com/posts/lkOl)
* [![](https://img.4hou.com/images/微信截图_20230421103932.png)

  黑入AI：通过MLflow漏洞接管系统和云](https://www.4hou.com/posts/KEKn)
* [![](https://img.4hou.com/images/微信截图_20230420103425.png)

  Mac恶意软件MacStealer伪装成P2E应用程序大肆传播](https://www.4hou.com/posts/lkYl)
* [![](https://img.4hou.com/images/5-1636388615.jpeg)

  【技术原创】Server Backup Manager漏洞调试环境搭建](https://www.4hou.com/posts/ZXJ5)
* [![](https://img.4hou.com/images/微信截图_20230417090354.png)

  多个 TPM 2.0 实现存在越界写入和越界读取漏洞](https://www.4hou.com/posts/gDY6)
* [![](https://img.4hou.com/images/微信截图_20230414171019.png)

  新兴信息窃取程序——Rhadamanthys的分析](https://www.4hou.com/posts/3r1r)

![]()

文章来源: https://www.4hou.com/posts/lkOl
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)