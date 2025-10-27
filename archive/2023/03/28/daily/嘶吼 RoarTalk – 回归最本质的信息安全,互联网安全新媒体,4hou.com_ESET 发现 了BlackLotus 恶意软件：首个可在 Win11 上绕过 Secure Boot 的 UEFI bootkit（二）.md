---
title: ESET 发现 了BlackLotus 恶意软件：首个可在 Win11 上绕过 Secure Boot 的 UEFI bootkit（二）
url: https://www.4hou.com/posts/QLQl
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-28
fetch_date: 2025-10-04T10:49:50.921695
---

# ESET 发现 了BlackLotus 恶意软件：首个可在 Win11 上绕过 Secure Boot 的 UEFI bootkit（二）

ESET 发现 了BlackLotus 恶意软件：首个可在 Win11 上绕过 Secure Boot 的 UEFI bootkit（二） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# ESET 发现 了BlackLotus 恶意软件：首个可在 Win11 上绕过 Secure Boot 的 UEFI bootkit（二）

luochicun
[技术](https://www.4hou.com/category/technology)
2023-03-27 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)153724

收藏

导语：在本部分中，我们将详细了解BlackLotus如何在启用UEFI Secure Boot的系统上实现持久性。

**绕过安全启动并建立持久性**

在本部分中，我们将详细了解BlackLotus如何在启用UEFI Secure Boot的系统上实现持久性。由于我们将要描述的执行链非常复杂，我们将首先解释基本原理，然后深入了解技术细节。

简而言之，该过程包括两个关键步骤：

利用CVE-2022-21894绕过安全启动功能并安装 bootkit。这允许在早期启动阶段任意执行代码，此时平台仍然由固件拥有，UEFI启动服务功能仍然可用。这使得攻击者可以在没有物理访问权限的情况下，在启用了UEFI Secure Boot的设备上做许多不应该做的事情，例如修改仅用于启动服务的NVRAM变量。这就是攻击者在下一个步骤中为 bootkit设置持久性所利用的。通过将自己的MOK写入MokList来设置持久性，Boot仅服务NVRAM变量。这样，它可以使用合法的 Microsoft-signed shim加载其自签名（由写入MokList的密钥的私钥签名）UEFIbootkit，而不是在每次启动时利用该漏洞。有关这一点的更多信息，请参阅Bootkit持久性部分。

为了使下面两部分的分析更容易，研究人员将遵循执行图（下图）中所示的步骤。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230306/1678089923170025.png "1678089923170025.png")

绕过安全启动并使用MOK设置持久性

**利用CVE-2022-21894**

为了绕过安全启动，BlackLotus使用baton drop漏洞（CVE-2022-21894）：安全启动安全功能绕过漏洞。尽管这个漏洞对系统安全影响很大，但它并没有得到应有的重视。尽管微软在2022年1月的更新中修复了该漏洞，但由于受影响的二进制文件仍未添加到UEFI取消列表中，因此攻击者仍有可能利用该漏洞。因此，攻击者可以将他们自己的易受攻击的二进制文件副本带到受害者的设备上，以利用此漏洞并绕过最新UEFI系统上的安全启动。

此外，自2022年8月以来，针对该漏洞的概念证明（PoC）漏洞已公开可用。考虑到第一次BlackLotus VirusTotal提交的日期，恶意软件开发人员可能只是根据他们的需要调整了可用的PoC，而不需要深入了解此漏洞的工作原理。

让我们先简单介绍一下该漏洞，主要是与PoC一起发布在GitHub上的文章中的关键点：

受影响的Windows启动应用程序（如bootmgr.efi、hvloader.efi、winload.efi…）允许在应用程序加载序列化安全启动策略之前，使用truncatememory BCD启动选项从内存中删除该策略。

这允许攻击者使用其他危险的BCD选项，如bootdebug、testsigning或nointegridchecks，从而破坏安全启动。

有多种方法可以利用此漏洞——其中三种方法已发布在PoC存储库中。

例如，其中一个PoC显示了如何利用它使合法的hvloader.efi加载任意的自签名mcupdate\_

现在，我们继续介绍BlackLotus如何利用此漏洞：

1.安装程序重新启动机器后，UEFI固件将继续加载第一个启动选项。对于Windows系统，默认情况下，第一个启动选项是位于ESP上ESP:/efi/Microsoft/boot文件夹中的bootmgfw.efi。这一次，固件没有执行原始受害者的bootmgfw.efi（安装程序以前将其重命名为winload.efi），而是执行安装程序部署的易受攻击的启动。

2.执行bootmgfw.efi后，它将加载BCD启动选项，该选项先前由安装程序修改。下图显示了合法BCD和修改后BCD的比较。

3.如下图所示（路径以绿色划线），合法的Windows Boot Manager通常会将Windows OS加载程序（\Windows\system32\winload.efi）作为默认启动应用程序加载。但这一次，使用修改后的BCD，它继续加载易受攻击的ESP:\system32\bootmgr.efi，避免内存BCD元素设置为值0x10000000，并且custom:22000023 BCD指向另一个攻击者存储在ESP:\system32\BCD中的BCD。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230306/1678089935172566.png "1678089935172566.png")

合法BCD存储（BEFORE）与BlackLotus安装程序使用的存储（AFTER）的比较

4.在下一步中，执行的ESP:\system32\bootmgr.efi加载位于ESP:\system32\BCD中的附加BCD。这个附加BCD的解析内容如下图所示。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230306/1678089945205324.png "1678089945205324.png")

BlackLotus安装程序释放的第二个BCD——用于利用CVE-2022-21894

5.由于从上图所示的BCD文件加载了选项，bootmgr.efi将继续加载安装程序部署的另一个易受攻击的Windows启动应用程序ESP:\system32\hvloader.efi，即Windows Hypervisor Loader。更重要的是，在同一BCD文件中指定了其他BCD选项：

值设置为0x10000000的truncatememory；

nointegridchecks设置为Yes；

testsigning也设置为Yes；

此时就会发生意想不到的事情，由于序列化的安全启动策略应该在0x10000000以上的物理地址中加载（因为前面步骤中使用了avoidlowmemory），指定truncatmemory元素将有效地删除它。因此，中断安全启动并允许使用危险的BCD选项，如nointegritychecks或testsigning。通过使用这些选项，攻击者可以使hvloader.efi执行自己的自签名代码。

6.为此，使用此PoC中描述的技巧，即在执行过程中，合法的hvloader.efi从

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230306/1678089955103449.png "1678089955103449.png")

从合法的hvloader.efi反编译BtLoadUpdateDll函数，负责加载mcupdate\_\*.dll

7.现在，随着攻击者自己的自签名mcupdate\*.dll被加载和执行，它将继续执行这个链中的最后一个组件——一个嵌入式MokInstaller （UEFI应用程序）——参见图10了解它是如何完成的。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230306/1678089967139692.png "1678089967139692.png")

Hex-Rays反编译恶意自签名mcupdate\*.dll二进制代码

**Bootkit持久性**

现在，MokInstaller可以继续设置持久性，方法是将攻击者的MOK注册到NVRAM变量中，并将合法的Microsoft签名的shim二进制文件设置为默认启动加载程序来继续设置持久性。

shim是由Linux开发人员开发的第一阶段UEFI启动加载程序，用于使各种Linux发行版与UEFI Secure Boot一起工作。它是一个简单的应用程序，其目的是加载、验证和执行另一个应用程序，在Linux系统中，它通常是GRUB启动加载程序。它的工作方式是，微软只签署一个shim, shim负责其余的工作，它可以通过使用db UEFI变量中的密钥来验证第二阶段启动加载器的完整性，还可以嵌入自己的“允许”或“取消”项或哈希列表，以确保平台和shim开发人员（例如Canonical, RedHat等）都信任的组件被允许执行。除了这些列表之外，shim还允许使用用户管理的外部密钥数据库，即MOK列表。该MOK数据库存储在名为MokList的仅启动NVRAM变量中。在不利用上述漏洞的情况下，需要物理访问才能在启用UEFI Secure Boot的系统上对其进行修改（仅在启动期间，在系统加载程序调用UEFI启动服务函数ExitBootServices之前可用）。然而，通过利用此漏洞，攻击者能够绕过UEFI Secure Boot并在调用ExitBootServices之前执行自己的自签名代码，因此他们可以轻松注册自己的密钥（通过修改MokList NVRAM变量），使填充程序执行任何应用程序（由该注册密钥签名），而不会导致安全违规。

![12.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230306/1678089977578601.jpeg "1678089977578601.jpeg")

MOK启动过程

8.MokInstaller UEFI应用程序继续为BlackLotus UEFI bootkit设置持久性，并通过以下方式覆盖利用痕迹：

8.1 从安装程序创建的备份中恢复受害者的原始BCD存储，并将efi替换为合法的microsoft签名shim，该shim先前由安装程序放置到ESP:\system32\bootload.efi中。

8.2创建包含攻击者自签名公钥证书的MokList NVRAM变量。请注意，此变量的格式与任何其他UEFI签名数据库变量（如db或dbx）的格式相同，它可以由零个或多个EFI\_signature\_LIST类型的签名列表组成，如UEFI规范中所定义。

8.3 从攻击者的ESP:\system32\文件夹中删除涉及攻击的所有文件。

最后，它会重新启动计算机，使部署的shim执行安装程序从\EFI\Microsoft\Boot\grub64.EFI中删除自签名bootkit，grub64.EFI通常是x86-64系统上shim执行的默认第二阶段启动加载程序。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230306/1678089986153359.png "1678089986153359.png")

Hex Rays反编译代码——MokInstaller UEFI应用程序为BlackLotus bootkit设置持久性

**BlackLotus UEFI bootkit**

一旦配置了持久性，就会在每次系统启动时执行BlackLotus bootkit。 bootkit的目标是部署一个内核驱动程序和一个最终的用户模式组件——HTTP下载器。在执行过程中，它试图禁用其他Windows安全功能——基于虚拟化的安全（VBS）和Windows Defender——以提高成功部署和隐形操作的机会。在详细介绍如何实现之前，让我们先了解一下内核驱动程序和HTTP下载器的基本知识：

内核驱动程序负责：

部署链的下一个组件—HTTP下载器；

在被终止运行的情况下保持加载器不被关闭；

防止从ESP中删除 bootkit文件；

如果HTTP下载器指示的话，执行额外的内核有效负载；

根据HTTP下载器的指示，卸载 bootkit。

HTTP下载器负责：

与C&C通信；

执行从C&C收到的命令；

下载并执行从C&C接收到的有效负载（支持内核有效负载和用户模式有效负载）。

从安装程序到HTTP下载器的完整执行流程（简化后）如下图所示。我们将在下一节中更详细地描述这些步骤。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230306/1678089996130928.png "1678089996130928.png")

BlackLotus UEFIbootkit执行示意图

**BlackLotus执行流程**

执行步骤如下（这些步骤如下图所示）：

1.UEFI固件执行默认的Windows启动选项，该选项通常存储在\EFI\Microsoft\boot\bootmgfw.EFI中的文件。正上所述，MokInstaller二进制文件用一个合法的签名shim替换了这个文件。

2.执行shim时，它读取MokList NVRAM变量，并使用攻击者先前存储在其中的证书来验证第二阶段启动加载程序——位于\EFI\Microsoft\Boot\grubx64.efi中的自签名BlackLotus UEFI启动程序。

3.验证后，shim执行 bootkit。

4.bootkit从创建仅启动VbsPolicyDisable NVRAM变量开始。如本文所述，此变量在启动期间由Windows OS加载程序评估，如果已定义，则不会初始化核心VBS功能，如HVCI和凭据保护。

5.在以下步骤中，bootkit继续使用UEFIbootkit使用的通用模式。它拦截典型Windows启动流中包含的组件的执行，例如Windows启动管理器、Windows OS加载器和Windows OS内核，并将它们的一些功能挂钩到内存中。另外，它还尝试通过修复某些驱动程序来禁用Windows Defender。所有这些都是为了在系统启动过程的早期阶段实现有效负载的执行，并避免检测。以下函数已挂钩或修复：

5.1 bootmgfw.efi或bootmgr.efi中的ImgArchStartBootApplication：该函数通常由bootkit挂钩，以捕捉Windows OS加载程序（winload.efi）加载到内存中但尚未执行的时刻——这是执行更多内存修复的正确时刻。

5.2 winload.efi中的BlImgAllocateImageBuffer：用于为恶意内核驱动程序分配额外的内存缓冲区。

5.3 winload.efi中的OslArchTransferToKernel：连接以捕捉系统内核和某些系统驱动程序已加载到内存中但尚未执行的时刻，这是执行更多内存修复的最佳时刻。下面提到的驱动程序在此挂钩中进行了修复。下图显示了这个挂钩中负责在内存中查找适当驱动程序的代码。

5.4 WdBoot.sys和WdFilter.sys：BlackLotus修复了WdBoot.sys和WdFilter.sys（分别是Windows Defender ELAM驱动程序和Windows Defender文件系统筛选器...