---
title: ESET 发现 了BlackLotus 恶意软件：首个可在 Win11 上绕过 Secure Boot 的 UEFI bootkit（一）
url: https://www.4hou.com/posts/PJPw
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-20
fetch_date: 2025-10-04T10:04:25.432745
---

# ESET 发现 了BlackLotus 恶意软件：首个可在 Win11 上绕过 Secure Boot 的 UEFI bootkit（一）

ESET 发现 了BlackLotus 恶意软件：首个可在 Win11 上绕过 Secure Boot 的 UEFI bootkit（一） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# ESET 发现 了BlackLotus 恶意软件：首个可在 Win11 上绕过 Secure Boot 的 UEFI bootkit（一）

luochicun
[技术](https://www.4hou.com/category/technology)
2023-03-19 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)168742

收藏

导语：ESET 的安全研究人员近日发现了一种劫持 UEFI 的恶意软件，并将其命名为 BlackLotus。该恶意软件是首个可以在Win11系统上绕过 Secure Boot 的 UEFI bootkit 恶意软件。

ESET 的安全研究人员近日发现了一种劫持 UEFI 的恶意软件，并将其命名为 BlackLotus。该恶意软件是首个可以在Win11系统上绕过 Secure Boot 的 UEFI bootkit 恶意软件。这个bootkit利用UEFI安全启动的Nday漏洞绕过安全启动并在启动过程中加载恶意的内核模块。设备一旦感染该恶意软件，就会在 Win11 系统中禁用 Defender、Bitlocker 和 HVCI 等防病毒软件。

**BlackLotus UEFI bootkit**

近年来发现的UEFI漏洞数量以及在合理的时间窗口内修复或取消易受攻击的二进制文件的失败都没有引起攻击者的注意。因此，第一个公开的绕过基本平台安全功能的UEFI bootkit——UEFI Secure Boot——现在已经成为现实。在这篇文章中，研究人员首次公开分析了该UEFI bootkit，它能够在启用了UEFI Secure Boot的最新Windows 11系统上运行。bootkit的功能及其单独的功能使研究人员相信研究人员正在处理一个被称为BlackLotus的 bootkit，UEFI bootkit至少从2022年10月起就开始在黑客论坛上以5000美元的价格出售。

UEFI bootkit的破坏性很大，它完全控制系统启动过程，因此能够禁用各种系统安全机制，并在系统启动的早期阶段部署自己的内核模式或用户模式有效负载。这使得他们可以非常隐秘地行动，并拥有很高的权限。到目前为止，只有少数几个在野外被发现并被公开报道，例如，研究人员在2020年发现的多个恶意EFI样本，或功能齐全的UEFI bootkit，如研究人员去年发现的ESPecter bootkit，或卡巴斯基研究人员发现的FinSpy bootkit。

与固件植入（如LoJax）相比，UEFI bootkit可能在隐蔽性方面有所下降。研究人员的团队于2018年发现了第一个野外UEFI固件植入，因为bootkit位于易于访问的FAT32磁盘分区上。然而，作为启动加载程序运行可以提供与固件植入几乎相同的功能，但无需克服多级SPI闪存防御，如BWE、BLE和PRx保护位，或硬件提供的保护（如Intel Boot Guard）。当然，UEFI Secure Boot阻碍了UEFI bootkit，但有一些不可忽视的已知漏洞可以绕过这一基本的安全机制。最糟糕的是，截止发文时，其中一些漏洞仍然很容易在最新系统上被利用，包括BlackLotus所利用的漏洞。

研究人员的调查始于对2022年末监测中的BlackLotus用户模式组件（一个HTTP下载器）的一些点击。经过初步评估，样本中发现的代码模式使研究人员发现了六个BlackLotus安装程序（包括VirusTotal和研究人员自己的遥测）。这使研究人员能够探索整个执行链，并意识到研究人员在这里处理的不仅仅是常规的恶意软件。

以下是有关BlackLotus的要点，以及与之相关的一系列事件的时间表：

1.它能够在启用UEFI Secure Boot的最新、完全修复的Windows 11系统上运行；

2.它利用一个超过一年的漏洞（CVE-2022-21894）绕过UEFI Secure Boot并为bootkit设置持久性，这是该漏洞第一次被公开使用；

3.尽管微软在2022年1月的更新中修复了该漏洞，但由于受影响的、有效签名的二进制文件仍未添加到UEFI取消列表中，因此该漏洞仍有可能被利用。BlackLotus就是利用了这一点，将其合法但易受攻击的二进制文件副本带到系统中，以利用该漏洞；

4.它能够禁用操作系统安全机制，如BitLocker, HVCI和Windows Defender；

5.一旦安装完毕，bootkit的主要目标是部署一个内核驱动程序（其中一个功能是保护bootkit不被删除），以及一个负责与C&C通信并能够加载其他用户模式或内核模式负载的HTTP下载器；

6.至少从2022年10月6日起，BlackLotus就在地下论坛上进行销售；

7.有趣的是，如果受攻击的主机位于以下地区，研究人员分析的一些BlackLotus安装程序不会继续进行bootkit安装：

```
Romanian （Moldova）, ro-MDRussian （Moldova）, ru-MDRussian （Russia）, ru-RUUkrainian （Ukraine） , uk-UABelarusian （Belarus）, be-BYArmenian （Armenia）, hy-AMKazakh （Kazakhstan）, kk-KZ
```

与BlackLotus相关的各事件的时间轴如下图所示。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230306/1678089607720953.png "1678089607720953.png")

与BlackLotus UEFI bootkit相关的主要事件时间轴

如上所述，自2022年10月6日起，bootkit已在地下论坛上销售。目前，研究人员还无法从监测数据中确定用于向受害者部署bootkit的确切传播渠道。研究人员从公开来源和监测数据中获得的BlackLotus样本数量很少，这证明只有很少的攻击者开始使用它。但是，在BlackLotus依赖的易受攻击的启动程序被取消之前，研究人员担心，如果这个bootkit落入知名的犯罪组织手中，情况会迅速发生变化，这是基于bootkit的易于部署和犯罪组织利用其僵尸网络传播恶意软件的能力。

**幕后组织是BlackLotus吗？**

BlackLotus属于一款相当全能的固件级 rootkit 恶意软件。特点是能够躲过各种删除操作，以及绕过先进的 Windows 防护措施。此前这类高级攻击能力，仅被拥有深厚背景的机构所拥有，比如情报威胁组织。

1.BlackLotus在黑客论坛上的宣称它具有集成的安全启动绕过。将易受攻击的驱动程序添加到UEFI取消列表目前是不可能的，因为该漏洞影响了数百个至今仍在使用的启动加载程序。

安全研究人员分析：它利用CVE-2022-21894来破坏安全启动，并在支持UEFI Secure Boot的系统上实现持久性。在撰写本文时，它使用的易受攻击的驱动程序仍然没有在最新的dbx中被取消。

2.BlackLotus在黑客论坛上宣称， bootkit具有内置的Ring0/Kernel保护，可以防止被删除。

安全研究人员分析：它的内核驱动程序保护属于EFI系统分区（ESP）上的文件句柄，可以不被关闭。作为额外的保护层，这些句柄会被持续监控，如果这些句柄中的任何一个被关闭，就会触发蓝屏死机（BSOD）。

3.BlackLotus在黑客论坛上宣称，它具有反虚拟机（anti-VM）、反调试和代码混淆功能，可以阻止被分析。

安全研究人员分析：它包含各种反虚拟机（anti-VM）、反调试和混淆技术，使其更难被复制或分析。

4.BlackLotus在黑客论坛上宣称其目的是充当HTTP下载器。

安全研究人员分析：它的最后一个组件充当HTTP下载器，如HTTP下载器部分所述。

5.BlackLotus在黑客论坛上宣称，HTTP下载器在一个合法的进程中以SYSTEM帐户运行。

安全研究人员分析：它的HTTP下载器在winlogon.exe进程上下文中运行。

6.BlackLotus在黑客论坛上的宣称，它是一个磁盘大小只有80kB的小型bootkit。

安全研究人员分析：能够获得的样本确实在80 kB左右。

7. BlackLotus在黑客论坛宣称，它可以禁用Windows内置的安全保护，如HVCI, Bitlocker, Windows Defender，并绕过用户帐户控制（UAC）。

安全研究人员分析：它可以禁用HVCI, Windows Defender, BitLocker并绕过UAC。

基于这些分析，研究人员可以肯定他们在野外发现的 bootkit是BlackLotus UEFI bootkit。

**攻击概述**

BlackLotus攻击链的简单步骤如下图所示。它由三个主要部分组成：

它首先执行安装程序（下图中的步骤1），该安装程序负责将bootkit的文件部署到EFI系统分区，禁用HVCI和BitLocker，然后重新启动计算机。

第一次重新启动后，利用CVE-2022-21894并随后记录攻击目标设备所有者的密钥（MOK），以便在启用UEFI Secure Boot的系统上实现持久性。然后重新启动设备（下图的步骤2- 4）。

在所有后续启动中，执行自签名的UEFI bootkit，并部署其内核驱动程序和用户模式有效负载（HTTP下载器）。这些组件能够一起从C&C服务器下载并执行额外的用户模式和驱动程序组件，并保护 bootkit不被删除（下图中的步骤5-9）。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230306/1678089618386192.png "1678089618386192.png")

BlackLotus的简单步骤

**工件分析**

尽管研究人员认为这是BlackLotus UEFI bootkit，但在分析的示例中没有发现任何引用此名称的内容。相反，该代码充满了对《暮蝉悲鸣时》（Higurashi When They Cry）动漫的引用，，例如，在单个组件名称中，例如Higurashi\_installer\_uac\_module.dll和Higurashi \_kernel.sys，以及用于签名bootkit二进制文件的自签名证书中（如下图所示）。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230306/1678089637204320.png "1678089637204320.png")

BlackLotus bootkit使用的自签名证书

此外，代码解密但从不使用包含来自BlackLotus开发者的消息的各种字符串（如下图所示），注意，hasherezade是一位著名的研究人员和各种恶意软件分析工具的开发者，或者只是一些来自各种歌曲、游戏或系列的随机引用。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230306/1678089645182852.png "1678089645182852.png")

BlackLotus开发者在代码中留下的消息示例

**安装过程**

研究人员首先分析了BlackLotus安装程序，bootkit似乎以安装程序的形式传播，有两个版本——离线和在线。这两者之间的区别在于它们获取合法（但易受攻击）的Windows二进制文件的方式，这些二进制文件后来被用于绕过安全启动。

在脱机版本中，Windows二进制文件嵌入在安装程序中；

在在线版本中，Windows二进制文件直接从Microsoft符号存储中下载。到目前为止，我们已经看到以下Windows二进制文件被BlackLotus bootkit滥用：

```
https://msdl.microsoft.com/download/symbols/bootmgfw.efi/7144BCD31C0000/bootmgfw.efi；https://msdl.microsoft.com/download/symbols/bootmgr.efi/98B063A61BC000/bootmgr.efi；https://msdl.microsoft.com/download/symbols/hvloader.efi/559F396411D000/hvloader.efi；
```

安装程序的目标很明确，它负责禁用Windows安全功能，如BitLocker磁盘加密和HVCI，并将多个文件（包括恶意bootkit）部署到ESP。完成后，它会重新启动受攻击的设备，让被释放的文件完成其工作，以确保每次系统启动时都会自动执行自签名的UEFIbootkit，无论UEFI Secure Boot保护状态如何。

**初始化步骤**

执行安装程序时，它会检查它是否有足够的权限（至少需要管理员）将其余文件部署到ESP，并执行其他需要提升进程的操作，如关闭HVCI或禁用BitLocker。如果不是这样的话，它会尝试通过使用此处详细描述的UAC绕过方法再次执行安装程序来提升，通过程序兼容性助手进行UAC绕过。

获得必要的权限后，它将继续，通过使用可用的Windows API函数读取SecureBoot UEFI变量的值来检查UEFI Secure Boot状态，并通过直接访问内存中的KUSER\_SHARED\_DATA结构字段NtMajorVersion和NtMinorVersion来确定Windows版本。它这样做是为了决定是否需要绕过UEFI Secure Boot来在受害者的系统上部署bootkit（因为安全启动支持最初是在Windows 8中添加的，并且可能不会在任何给定的设备上启用）。

在继续下一步之前，它将位于ESP:\EFI\Microsoft\Boot\目录中的合法Windows启动管理器（bootmgfw.efi）二进制文件重命名为winload.efi。此重命名的bootmgfw.exfi备份稍后将被bootkit用于启动操作系统，或者在从C&C服务器收到“卸载”命令时恢复原始启动链，详见C&C通信部分。

**步骤1——部署文件**

如果启用了UEFI Secure Boot，安装程序会将多个文件放入ESP:/EFI/Microsoft/Boot/和ESP:/system32/目录中。前者是Windows使用的标准目录，后者是安装程序创建的自定义文件夹。

表1提供了安装程序释放的文件列表，并简要说明了每个文件在执行链中的角色。稍后研究人员将详细解释执行链是如何工作的，现在只需注意，几个合法的Microsoft签名文件与恶意文件一起被释放。

表1：BlackLotus安装程序在启用UEFI Secure Boot的系统上部署的文件

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230306/1678089654503846.png "1678089654503846.png")

如果受害者正在运行不支持UEFI Secure Boot的Windows版本，或者在UEFI Secure Boot被禁用的情况下，部署非常简单。部署恶意 bootkit唯一需要做的...