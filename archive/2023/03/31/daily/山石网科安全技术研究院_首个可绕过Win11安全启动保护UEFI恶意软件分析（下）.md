---
title: 首个可绕过Win11安全启动保护UEFI恶意软件分析（下）
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247500610&idx=1&sn=b8efd65fcd8a11f1c842b4f3bc04f9c7&chksm=fa5216fccd259fea887eb8201e123258b2f0452fa000700be1fdd809a29cee7a21904c662d7c&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2023-03-31
fetch_date: 2025-10-04T11:15:44.152961
---

# 首个可绕过Win11安全启动保护UEFI恶意软件分析（下）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnQiat2GGIZzoawndqrTIrMBQEMibDJXoRiaibna7l7icZUdfkkCokkfNUZNDDqpgN3iaU4uiazcKsGbiaWqlA/0?wx_fmt=jpeg)

# 首个可绕过Win11安全启动保护UEFI恶意软件分析（下）

原创

x1a0

山石网科安全技术研究院

**0****1**

**Bootkit持久化 ‍**

现在，MokInstaller可以通过将攻击者的 MOK 注册到 NVRAM 变量并将合法的 Microsoft 签名的shim二进制文件设置为默认引导加载程序来继续设置持久性。在继续讨论细节之前，先了解一下关于垫片和 MOK的理论。

shim是由Linux开发人员开发的第一阶段 UEFI 引导加载程序，用于使各种Linux 发行版与UEFI安全引导一起工作。它是一个简单的应用程序，其目的是加载、验证和执行另一个应用程序——对于 Linux系统，它通常是GRUB引导加载程序。它的工作方式是微软只签署一个垫片，垫片负责其余的工作——它可以通过使用来自db UEFI变量的密钥来验证第二阶段引导加载程序的完整性，并且还嵌入了它自己的“允许”列表或“撤销”密钥或散列，以确保平台和shim 开发人员（例如Canonical、RedHat等）都信任的组件被允许执行。除了这些列表之外，shim还允许使用由用户管理的外部密钥数据库，称为 MOK列表。图 11 很好地说明了UEFI安全启动与MOK的工作原理。

这个MOK数据库存储在一个名为MokList的Boot-only NVRAM变量中。在不利用上述漏洞的情况下，需要物理访问才能在启用了UEFI安全启动的系统上修改它（它仅在启动期间可用，在操作系统加载程序调用UEFI启动服务函数ExitBootServices之前）。然而，通过利用此漏洞，攻击者能够绕过UEFI安全启动并在调用ExitBootServices之前执行自己的自签名代码，因此他们可以轻松注册自己的密钥（通过修改MokList NVRAM变量）以使shim执行任何应用程序 - 由该注册密钥签名 - 而不会导致安全违规。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQiat2GGIZzoawndqrTIrMBQWteV2ibntiaCIbwiaiaFhG45kZSoXZCu54cOnPaO9F5FE6h0jXQ21zVcxg/640?wx_fmt=png)图11. MOK 引导过程概览

继续描述图 6 中的流程 - 第 8 步...... MokInstaller UEFI应用程序继续为BlackLotus UEFI bootkit设置持久性并覆盖利用的轨迹：

‍1.从安装程序创建的备份中恢复受害者的原始 BCD 存储，并将efi替换为合法的 Microsoft签名填充程序，之前由安装程序删除到ESP:\system32\bootload.efi 。

‍2.创建包含攻击者自签名公钥证书的MokList NVRAM变量。请注意，此变量的格式与任何其他UEFI签名数据库变量（例如db或db）相同，并且它可以包含零个或多个 EFI\_SIGNATURE\_LIST类型的签名列表——如UEFI规范中所定义。

‍3.从攻击者的ESP:\system32\文件夹中删除所有涉及利用的文件。

最后，它会重新启动机器，使部署的shim执行安装程序放置到\EFI\Microsoft\Boot\grubx64.efi 的自签名 bootkit（grubx64.efi通常是shim执行的默认第二阶段引导加载程序在 x86-64系统上）。

执行最后两个步骤中描述的操作的代码如图12 所示。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQiat2GGIZzoawndqrTIrMBQx5thyFZTbenfengg357dnrAkaoYQayRtweaiaA8pq6vJnYoLLZHHhkA/640?wx_fmt=png)图 12. Hex-Rays 反编译代码– MokInstaller UEFI 应用程序为 BlackLotus bootkit 设置持久性

**02****‍**

**BlackLotus UEFI 启动套件‍**

一旦配置了持久性，BlackLotus bootkit就会在每次系统启动时执行。bootkit的目标是部署一个内核驱动程序和一个最终的用户模式组件——HTTP 下载器。在执行期间，它会尝试禁用其他Windows安全功能——基于虚拟化的安全 (VBS) 和Windows Defender——以提高成功部署和秘密操作的机会。在跳转到有关如何完成的详细信息之前，让我们总结一下有关内核驱动程序和HTTP下载程序的基础知识：

·内核驱动负责

o部署链的下一个组件——HTTP下载器。

o在终止的情况下保持加载程序活动。

o保护 bootkit文件不被从ESP中删除。

o执行额外的内核有效负载，如果HTTP下载程序如此指示。

o卸载 bootkit，如果HTTP下载程序如此指示。

·HTTP下载器负责：

o与其C&C通信。

o执行从C&C接收到的命令。

o下载并执行从C&C接收到的有效载荷（支持内核有效载荷和用户模式有效载荷）。

从安装程序到HTTP下载程序的完整执行流程（简化）如图 13 所示。我们将在下一节中更详细地描述这些单独的步骤。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQiat2GGIZzoawndqrTIrMBQ9zHE2UJuJWKOheKY9rMW9kz9lHlicMD1rCu1SSGEx7OdmLNA15zJ8bw/640?wx_fmt=png)图 13. 显示 BlackLotus UEFI bootkit 执行的图表

**03****‍**

**BlackLotus 执行流程 ‍**

执行步骤如下（这些步骤如图 13 所示）：

1.作为第一步，UEFI固件执行默认的Windows引导选项，该文件通常存储在\EFI\Microsoft\Boot\bootmgfw.efi中。正如我们之前描述的（Bootkit 持久性部分，8.a），MokInstaller二进制文件用合法签名的shim替换了这个文件。

2.执行shim时，它会读取MokList NVRAM变量，并使用攻击者先前存储在其中的证书来验证第二阶段引导加载程序——位于\EFI\Microsoft\Boot\grubx64.efi中的自签名 BlackLotus UEFI bootkit .

3.验证后，shim将执行 bootkit。

4.bootkit从创建 Boot-only VbsPolicyDisable NVRAM变量开始。如此处所述，此变量在启动期间由 Windows操作系统加载程序评估，如果已定义，则不会初始化核心 VBS 功能，例如 HVCI 和 Credential Guard。

5.在以下步骤 (5.a–e) 中，bootkit继续使用 UEFI bootkit使用的通用模式。它拦截典型 Windows启动流程中包含的组件的执行，例如Windows启动管理器、Windows操作系统加载程序和 Windows操作系统内核，并在内存中挂钩它们的一些功能。作为奖励，它还尝试通过修补其某些驱动程序来禁用Windows Defender。所有这些都是为了在操作系统启动过程的早期阶段实现其有效负载的执行，并避免被发现。以下功能已挂钩或修补：

a.bootmgfw.ef或bootmgr.efi中的ImgArchStartBootApplication：此函数通常被bootkits 挂钩，以捕捉Windows操作系统加载程序 ( winload.efi ) 加载到内存但仍未执行的时刻 - 这是正确的时刻执行更多的内存修补。

b.winload.efi中的BlImgAllocateImageBuffer：用于为恶意内核驱动程序分配额外的内存缓冲区。

c.winload.efi中的OslArchTransferToKernel：钩住操作系统内核和一些系统驱动程序已经加载到内存中但仍未执行的时刻 - 这是执行更多内存中修补的完美时刻。下面提到的驱动程序在此挂钩中进行了修补。来自此挂钩的代码负责在内存中查找合适的驱动程序，如图 14 所示。

d.WdBoot.sys和WdFilter.sys： BlackLotus 修补了WdBoot.sys和WdFilter.sys的入口点——分别是 Windows Defender ELAM 驱动程序和 Windows Defender 文件系统过滤驱动程序——以立即返回。

e.disk.sys： bootkit 挂钩disk.sys驱动程序 的入口点，以在系统初始化的早期阶段执行 BlackLotus 内核驱动程序。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQiat2GGIZzoawndqrTIrMBQl8S4tSoBesTcrkSIF3OVRW9YndVw3d0Ij8ibQfcWZW00w0HBpqL3HRw/640?wx_fmt=png)图 14. OslArchTransferToKernel挂钩的 Hex-Rays 反编译代码——修补 Windows Defender 驱动程序并搜索disk.sys入口点

1.接下来，当 OS 内核执行disk.sys驱动程序的入口点时，已安装的挂钩会跳转到恶意内核驱动程序的入口点。恶意代码依次恢复原来的disk.sys让系统正常运行，等待winlogon.exe进程启动。

2.当恶意驱动程序检测到winlogon.exe进程已启动时，它会向其中注入并执行最终的用户模式组件——HTTP 下载程序。

**04****‍**

**内核驱动 ‍‍‍‍‍‍‍‍‍**

内核驱动程序负责四个主要任务：

·将 HTTP 下载程序注入winlogon.exe并在线程终止时重新注入它。

·保护部署在 ESP 上的 bootkit 文件不被删除。

·解除用户模式 Windows Defender 进程MsMpEngine.exe。

·与 HTTP 下载程序通信，并在必要时执行任何命令。

让我们一一看看。

**05****‍**

**HTTP下载器持久化‍**

内核驱动程序负责部署HTTP 下载程序。当驱动程序启动时，它会等到名为winlogon.exe的进程启动，然后再执行任何其他操作。进程启动后，驱动程序会解密 HTTP 下载程序二进制文件，将其注入winlogon.exe的地址空间，并在新线程中执行。然后，驱动程序会定期检查线程是否仍在运行，并在必要时重复注入。如果驱动程序检测到内核调试器，则不会部署 HTTP 下载器。

**06****‍**

**保护ESP上的bootkit文件不被删除‍**

为了保护位于ESP 上的 bootkit 文件，内核驱动程序使用了一个简单的技巧。它打开它想要保护的所有文件，复制并保存它们的句柄，并使用ObSetHandleAttributes内核函数将HandleFlags ( OBJECT\_HANDLE\_FLAG\_INFORMATION )参数中的ProtectFromClose标志指定为 1——从而保护句柄不被任何其他进程关闭。这将阻止任何删除或修改受保护文件的尝试。以下文件受到保护：

·ESP:\EFI\Microsoft\Boot\winload.efi

·ESP:\EFI\Microsoft\Boot\bootmgfw.efi

·ESP:\EFI\Microsoft\Boot\grubx64.efi

如果用户尝试删除这些受保护的文件，将会发生如图15 所示的情况。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQiat2GGIZzoawndqrTIrMBQZ2IwdBQPSArcPAd83FmIjqu5iaY5kyV0WuheKwzKOiaEHX39aZrGhO9w/640?wx_fmt=png)图15. 尝试删除受 BlackLotus 驱动程序保护的文件

作为另一层保护，以防用户或安全软件能够取消设置保护标志并关闭句柄，内核驱动程序会持续监视它们，如果有任何句柄，则通过调用 KeBugCheck(INVALID\_KERNEL\_HANDLE) 函数导致BSOD不存在了。

**07****‍**

**解除主 Windows Defender 进程‍‍‍‍‍**

内核驱动程序还尝试解除主 Windows Defender 进程——MsMpEng.exe。它通过为每个进程设置SE\_PRIVILEGE\_REMOVED属性来删除所有进程的令牌特权。因此，Defender 进程应该无法正常执行其工作（例如扫描文件）。但是，由于此功能实现不佳，可以通过重新启动MsMpEng.exe进程使其失效。

**08****‍**

**与HTTP下载器通信**

内核驱动程序能够通过使用命名的事件和部分与HTTP 下载程序进行通信。使用的命名对象的名称是根据受害者的网络适配器 MAC 地址（以太网）生成的。如果八位位组的值小于 16，则向其添加 16。生成的对象名称的格式可能因样本不同而不同。例如，在我们分析的一个样本中，对于 MAC 地址00-1c-0b-cd-ef-34，生成的名称将是：

·\BaseNamedObjects\101c1b：用于命名部分（仅使用 MAC 的前三个八位字节）

·\BaseNamedObjects\ **Z** 01c1b：对于命名事件——与 Section 相同，但 MAC 地址的第一位数字被替换为Z

如果HTTP 下载器想要将一些命令传递给内核驱动程序，它只需创建一个命名部分，在其中写入一个带有相关数据的命令，然后通过创建一个命名事件等待驱动程序处理该命令并等待直到驱动程序触发（或发出信号）它。

驱动程序支持以下不言自明的命令：

·安装内核驱动

·卸载黑莲花

细心的读者可能会注意到这里的BlackLotus 弱点——即使 bootkit 保护其组件不被删除，内核驱动程序也可以通过创建上述命名对象并向其发送卸载命令来欺骗以完全卸载 bootkit。

**09****‍**

**HTTP下载器**

最后一个组件负责与C&C 服务器通信并执行从它接收到的任何 C&C 命令。我们能够发现的所有有效载荷都包含三个命令。这些命令非常简单，正如部分名称所暗示的那样，它主要是关于使用各种技术下载和执行额外的有效负载。

**10**

**C&C通信**

为了与其C&C 通信，HTTP 加载程序使用 HTTPS 协议。通信所需的所有信息都直接嵌入到下载程序二进制文件中——包括 C&C 域和使用的 HTTP 资源路径。与 C&C 服务器通信的默认间隔设置为一分钟，但可以根据来自 C&C 的数据进行更改。与 C&C 的每个通信会话都以向其发送信标 HTTP POST 消息开始。在我们分析的示例中，可以在 HTTP POST 标头中指定以下 HTTP 资源路径：

·/network/API/hpb\_gate[.]php

·/API/hpb\_gate[.]php

·/gate[.]php

·/hpb\_gate[.]php

信标消息数据以checkin = string 为前缀，包含有关受感染机器的基本信息——包括自定义机器标识符（称为HWID）、UEFI 安全启动状态、各种硬件信息，以及一个似乎是 BlackLotus 的值内部版本号。HWID由机器 MAC 地址（以太网）和系统卷序列号生成。加密前的消息格式如下所示

{
    "HWID":"%s",
    "Session":"%lu",
    "Owner":"%s",
    "IP":"%s",
    "OS":"%s",
    "Edition":"%s",
    "CPU":"%s",
    "GPU":"%s",
    "RAM":"%lu",
    "Integrity":"%lu",
    "SecureBoot":"%i",
    "Build":"%lu"
}

在将消息发送到C&C 之前，首先使用嵌入式 RSA 密钥对数据进行加密，然后进行 URL 安全的base64 编码。在分析过程中，我们发现样本中使用了两个不同的 RSA 密钥。图 17 显示了此类 HTTP 信标请求的示例。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQiat2GGIZzoawndqrTIrMBQSO3DKYDsGpvFUdxh2bqKmR0PIoLXjSf3I7b4qUtVmrIcWEX2hqs06g/640?wx_fmt=png)图17. 信标 HTTP POST 消息示例（由来自 VirusTotal 的示例生成——具有本地 IP 而不是真实 C&C 地址的示例）

作为对信标消息的响应，从C&C 接收的数据应以两字节的魔法值 HP 开头；否则，不会进一步处理响应。如果magic值正确，则以上述HWID字符串为密钥，使用CBC模式的256位AES对magic值后面的数据进行解密。

解密后的消息类似于信标，是一个JSON格式的字符串，并指定了一个命令标识符（简称Type）和各种附加参数，例如：

·C&C通信间隔

·使用的执行方法

·负载文件名

·基于文件扩展名的负载类型（支持.sys、.exe或.dll ）

·应该用于请求下载有效负载数据的身份验证令牌

·用于解密有效负载数据的 AES 密钥

表2 中列出了所有受支持的命令及其说明。

*表 2. C&C 命令*

|  |  |
| --- | --- |
| 命令类型 | 命令说明 |
| 1个 | 下载并执行内核驱动程序、DLL 或常规可执行文件 |
| 2个 | 下载有效载荷，卸载 bootkit，然后执行有效载荷——可能用于更新 bootkit |
| 3个 | 卸载bootkit并退出 |

在这些命令中，C&C可以指定有效载荷是应该在执行之前先放到磁盘上，还是直接在内存中执行。在涉及将文件拖放到磁盘的情况下，操作系统卷上的ProgramData文件夹用作目标文件夹，文件名和扩展名由C&C服务器指定。在直接在内存中执行文件的情况下，svchost.exe被用作注入目标。当 C&C 发送要求内核驱动程序协作的命令，或者操作员想要在内核模式下执行代码时，将使用与 HTTP 下载程序通信部分中描述的机制。

**11**

**反分析技巧
‍‍‍‍‍‍‍‍‍**

为了更难检测和分析这种恶意软件，它的作者试图将标准文件工件（例如文本字符串、导...