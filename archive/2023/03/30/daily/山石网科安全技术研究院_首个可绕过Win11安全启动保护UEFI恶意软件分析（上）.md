---
title: 首个可绕过Win11安全启动保护UEFI恶意软件分析（上）
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247500592&idx=1&sn=fdc2df77370717652cafbd8b3ad37bde&chksm=fa52168ecd259f9828999742410ecc8f716951edb332afee5f620a2fe5655163f8c2a3e9342a&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2023-03-30
fetch_date: 2025-10-04T11:08:06.567390
---

# 首个可绕过Win11安全启动保护UEFI恶意软件分析（上）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnSwFGRd2elAPXT5vhib3YRq2BRsvqZ4GumRHFIdHTuG0gqcjJNI4Wz6icpicib2jomeEMpiasmR5gF3pVg/0?wx_fmt=jpeg)

# 首个可绕过Win11安全启动保护UEFI恶意软件分析（上）

原创

x1a0

山石网科安全技术研究院

近年来发现的UEFI 漏洞数量以及未能在合理的时间窗口内修补或撤销易受攻击的二进制文件并没有被威胁者忽视。因此，第一个绕过基本平台安全功能（UEFI 安全启动）的公开 UEFI bootkit 现已成为现实。在这篇博文中，我们首次公开分析了这个 UEFI bootkit，它甚至能够在启用了 UEFI 安全启动的最新 Windows 11 系统上运行。

UEFI bootkit是非常强大的威胁，可以完全控制操作系统启动过程，因此能够禁用各种操作系统安全机制并在早期操作系统启动阶段部署自己的内核模式或用户模式有效负载。这使他们能够非常隐蔽地操作并享有很高的特权。到目前为止，只有少数在野外被发现并公开描述（例如，在 2020 年发现的多个恶意 EFI 样本，或功能齐全的 UEFI bootkit，例如我们去年发现的ESPecter bootkit，或研究人员发现的FinSpy bootkit来自卡巴斯基）。

与固件植入相比，UEFI bootkit可能会失去隐蔽性——例如LoJax; 国外团队在 2018 年发现了第一个野外 UEFI 固件植入——因为 bootkit 位于一个易于访问的 FAT32 磁盘分区上。然而，作为引导加载程序运行赋予它们几乎与固件植入相同的功能，但无需克服多级 SPI 闪存防御，例如 BWE、BLE 和 PRx 保护位，或硬件提供的保护（如 Intel Boot Guard ). 当然，UEFI 安全启动阻碍了 UEFI bootkit，但是有不可忽略的已知漏洞数量可以绕过这种基本的安全机制。

以下是关于BlackLotus 的要点以及总结与之相关的一系列事件的时间表：

·它能够在启用了 UEFI 安全启动的最新、完全修补的 Windows 11 系统上运行。

·它利用一年多前的漏洞 ( CVE-2022-21894 ) 绕过 UEFI 安全启动并为 bootkit 设置持久性。这是此漏洞的首次公开滥用。

·尽管该漏洞已在 Microsoft 2022 年 1 月的更新中得到修复，但由于受影响的**有效签名**二进制文件仍未添加到UEFI 吊销列表中，因此仍有可能利用该漏洞。BlackLotus 利用了这一点，将自己的合法但易受攻击的二进制文件副本带到系统中，以利用该漏洞。

·它能够禁用 BitLocker、HVCI 和 Windows Defender 等操作系统安全机制。

·安装后，bootkit 的主要目标是部署一个内核驱动程序（其中包括保护 bootkit 不被删除）和一个 HTTP 下载程序，负责与 C&C 通信并能够加载额外的用户模式或内核模式有效负载.

·至少从 2022 年 10 月 6 日起，BlackLotus 就开始在地下论坛上做广告和销售。

·有趣的是，如果受感染的主机使用以下语言环境之一，我们分析的一些 BlackLotus 安装程序不会继续安装 bootkit：

o罗马尼亚语（摩尔多瓦），ro-MD

o俄语（摩尔多瓦），ru-MD

o俄语（俄罗斯），ru-RU

o乌克兰语 (Ukraine) , uk-UA

o白俄罗斯语（白俄罗斯语），be-BY

o亚美尼亚语（亚美尼亚），hy-AM

o哈萨克语（哈萨克斯坦），kk-KZ

与BlackLotus 相关的个别事件的时间线如图 1 所示。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSwFGRd2elAPXT5vhib3YRq2Ty14BCEIicNNqKRstMSrD5n6RaZezyxasONUQLpz8LlQRnbIiaZjIMBQ/640?wx_fmt=png)图 1. 与 BlackLotus UEFI bootkit 相关的主要事件的时间表

**0****1**

**攻击概述   ‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍**

BlackLotus 妥协链的简化方案如图 2 所示。它由三个主要部分组成：

1.它从执行安装程序（图 2 中的步骤 1）开始，负责将 bootkit 的文件部署到 EFI 系统分区，禁用 HVCI 和BitLocker，然后重新启动机器。

2.第一次重启后，利用 CVE-2022-21894 并随后注册攻击者的机器所有者密钥(MOK)，即使在启用了 UEFI 安全启动的系统上也能实现持久性。然后机器再次重新启动（图 2 中的步骤 2-4）。

3.在所有后续引导中，自签名 UEFI bootkit 被执行并部署其内核驱动程序和用户模式有效负载，即 HTTP 下载程序。这些组件一起能够从 C&C 服务器下载和执行额外的用户模式和驱动程序组件，并保护 Bootkit 不被删除（图 2 中的步骤 5-9）。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSwFGRd2elAPXT5vhib3YRq2mj9IwobKIvBAVMriacVGjVGTCXuyGaZJPhBQRWpzCcAuZuCG1qUFpxQ/640?wx_fmt=png)图 2. BlackLotus 简化执行概述

**02****‍**

**有趣的事情 ‍‍‍‍‍‍‍‍‍‍**

##

尽管我们认为这是 BlackLotus UEFI bootkit，但我们在分析的样本中没有发现任何对此名称的引用。相反，代码中充满了对Higurashi When They Cry动漫系列的引用，例如在单独的组件名称中，例如higurashi\_installer\_uac\_module.dll和higurashi\_kernel.sys，以及用于签署 bootkit 二进制文件的自签名证书（如图所示）在图 3 中）。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSwFGRd2elAPXT5vhib3YRq2TUgdfPN8JVhOy0Cib3gribJlOScjRsibdoUyh6A3TOgib3HHS0OgCA7LPA/640?wx_fmt=png)图 3. BlackLotus bootkit 使用的自签名证书

此外，代码解密但从不使用包含来自 BlackLotus 作者的消息的各种字符串（如图 4 所示），或者只是来自各种恶意软件分析工具的一些随机引用歌曲、游戏或系列。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSwFGRd2elAPXT5vhib3YRq2fX1wP36gHUONKjBoukicCyQ7AC9EUKpQVhSZibiatvlZ8xFHRDeg2utDA/640?wx_fmt=png)图4. BlackLotus 作者在代码中留下的消息示例

**03****‍**

**安装过程 ‍**

我们从分析BlackLotus 安装程序开始。bootkit 似乎以安装程序的形式分发，有两个版本——离线和在线。这两者之间的区别在于它们获取合法（但易受攻击）Windows 二进制文件的方式，后来用于绕过安全启动。

·在离线版本中，Windows 二进制文件嵌入在安装程序中

·在在线版本中，Windows 二进制文件直接从 Microsoft 符号商店下载。到目前为止，我们已经看到以下 Windows 二进制文件被 BlackLotus bootkit 滥用：

ohttps://msdl.microsoft.com/download/symbols/bootmgfw.efi/7144BCD31C0000/bootmgfw.efi

ohttps://msdl.microsoft.com/download/symbols/bootmgr.efi/98B063A61BC000/bootmgr.efi

ohttps://msdl.microsoft.com/download/symbols/hvloader.efi/559F396411D000/hvloader.efi

安装程序的目标很明确——它负责禁用 Windows 安全功能，例如 BitLocker 磁盘加密和HVCI，以及将多个文件（包括恶意 bootkit）部署到 ESP。完成后，它会重新启动受感染的机器，让丢失的文件发挥作用——确保自签名 UEFI bootkit 将在每次系统启动时静默执行，无论UEFI 安全启动保护状态如何。

### **第 0 步****– 初始化和（潜在的）提升**

### 当安装程序被执行时，它会检查它是否有足够的权限（至少需要管理员权限）来将其余文件部署到ESP 并执行其他需要提升进程的操作——比如关闭 HVCI 或禁用 BitLocker。如果不是这种情况，它会尝试通过使用此处详细描述的 UAC 绕过方法再次执行安装程序来提升：UAC 绕过程序兼容性助手。

有了必要的权限，它会继续检查 UEFI 安全启动状态，方法是使用可用的 Windows API 函数读取 SecureBoot UEFI 变量的值，并通过直接访问内存中的 KUSER\_SHARED\_DATA 结构字段 NtMajorVersion 和NtMinorVersion来确定Windows版本。它这样做是为了决定是否有必要绕过UEFI 安全启动以在受害者的系统上部署 bootkit（因为安全启动支持首先在 Windows 8 中添加，并且可能不会在任何给定的机器上启用）。

在继续下一步之前，它将位于ESP:\EFI\Microsoft\Boot\目录中的合法 Windows 启动管理器 ( bootmgfw.efi ) 二进制文件重命名为winload.efi。这个重命名的bootmgfw.efi备份随后被 bootkit 用来启动操作系统，或者如果从 C&C 服务器接收到“卸载”命令则恢复原始引导链——更多内容在C&C 通信部分。

### **第 1 步****– 部署文件**

如果启用了 UEFI 安全启动，安装程序会继续将多个文件放入ESP:/EFI/Microsoft/Boot/和ESP:/system32/目录。前者是 Windows 使用的标准目录，而后者是安装程序创建的自定义文件夹。

表1 提供了安装程序丢弃的文件列表以及每个文件在执行链中的作用的简短说明。稍后我们将详细解释执行链的工作原理；现在请注意，几个合法的 Microsoft 签名文件与恶意文件一起被丢弃。

*表 1. BlackLotus 安装程序在启用了 UEFI 安全引导的系统上部署的文件*

|  |  |  |
| --- | --- | --- |
| 文件夹 | 文件名 | 描述 |
| ESP:\EFI\Microsoft\Boot | grubx64.efi | BlackLotus bootkit，恶意自签名 UEFI 应用程序。 |
| 引导加载文件 | 合法的 Microsoft 签名shim二进制文件（临时名称，在CVE-2022-21894  漏洞利用后替换bootmgfw.efi）。 |
| bootmgfw.efi | 合法但易受攻击 ( CVE-2022-21894  ) Windows 启动管理器二进制文件，嵌入在安装程序中或直接从 Microsoft Symbol Store 下载。 |
| BCD | CVE-2022-21894  开发链中使用的攻击者自定义 启动配置数据  (BCD) 存储 。 |
| BCDR | 受害者原始 BCD 存储的备份。 |
| ESP:\system32 | hvloader.efi文件 | 合法但易受攻击 ( CVE-2022-21894  ) Windows Hypervisor Loader 二进制文件，嵌入在安装程序中或直接从 Microsoft Symbol Store 下载。 |
| 启动管理器文件 | 合法但易受攻击 ( CVE-2022-21894  ) Windows 启动管理器二进制文件，嵌入在安装程序中或直接从 Microsoft Symbol Store 下载。 |
| mcupdate\_AuthenticAMD.dll | 恶意自签名本机 PE 二进制文件。该文件在成功利用 CVE-2022-21894 后由hvloader.efi执行（在使用 AMD CPU 的系统上）。 |
| mcupdate\_GenuineIntel.dll | 恶意自签名本机 PE 二进制文件。该文件在成功利用CVE-2022-21894后由  hvloader.efi执行（在使用 Intel CPU 的系统上）。 |
| BCD | CVE-2022-21894  利用链中使用的攻击者自定义BCD 。 |

如果受害者运行的 Windows 版本不支持 UEFI 安全启动，或者在它被禁用的情况下，部署就非常简单。部署恶意 bootkit 唯一需要做的就是用攻击者自己的自签名恶意 UEFI 应用程序替换ESP:\EFI\Microsoft\Boot\目录中现有的 Windows 启动管理器 ( bootmgfw.efi ) 二进制文件。由于禁用了 UEFI 安全引导（因此在引导期间不执行完整性验证），因此不需要利用，UEFI 固件只是执行恶意引导管理器而不会导致任何安全违规。

### **第 2 步****– 禁用受管理程序保护的代码完整性 (HVCI)**

为了能够在以后运行自定义的未签名内核代码，安装程序必须确保系统上禁用了HVCI 。

基于虚拟化的安全性(VBS) 提供多种保护功能，其中最突出的是虚拟机监控程序保护的代码完整性 (HVCI)，它也是一个独立的功能。HVCI 在内核中强制执行代码完整性，并且只允许执行已签名的代码。它有效地防止易受攻击的驱动程序被滥用来执行未签名的内核代码或加载恶意驱动程序（无论使用何种利用方法）并且似乎恶意软件滥用易受攻击的驱动程序加载恶意代码是微软实现此功能的主要动机之一。

如图 5 所示，要禁用此功能，安装程序将HypervisorEnforcedCodeIntegrity注册表项下的 Enabled 注册表值设置为零。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSwFGRd2elAPXT5vhib3YRq241zQBXNu3AxfLcrC9Jibp9y9icZup8YiaGpox4eoI1Yt5wIFjAeHHBdJQ/640?wx_fmt=png)图 5. 负责禁用 HVCI 的 BlackLotus 安装程序函数的 Hex-Rays 反编译代码

### **第 3 步****– 禁用 BitLocker**

安装程序停用的下一个功能是BitLocker 驱动器加密。这样做的原因是 BitLocker 可以与可信平台模块 (TPM)结合使用，以确保自系统上配置 BitLocker 驱动器加密以来，各种启动文件和配置（包括安全启动）未被篡改。考虑到安装程序会修改受感染计算机上的 Windows 启动链，为支持 TPM 的系统保持 BitLocker 开启将导致在下次启动时出现 BitLocker 恢复屏幕，并提示受害者系统已被入侵。

要禁用此保护，BlackLotus 安装程序：

·遍历Root\CIMV2\Security\MicrosoftVolumeEncryption WMI 命名空间下的所有卷，并通过调用Win32\_EncryptableVolume WMI 类的GetProtectionStatus方法检查它们的保护状态

·对于那些受 BitLocker 保护的对象，它会调用DisableCount参数设置为零的DisableKeyProtectors方法，这意味着保护将被暂停，直到它被手动启用

在禁用必要的保护并部署所有文件的情况下，安装程序会在下次系统重启时注册自己以将其删除，并重启机器以继续利用CVE-2022-21894。

## **绕过安全启动并建立持久性**

在这一部分中，我们将仔细研究BlackLotus 如何在启用了 UEFI 安全启动的系统上实现持久化。由于我们即将描述的执行链相当复杂，我们将首先解释基本原理，然后深入挖掘技术细节。

简而言之，这个过程包括两个关键步骤：

1.利用 CVE-2022-21894 绕过安全启动功能并安装 bootkit。这允许在早期引导阶段执行任意代码，此时平台仍由固件拥有，并且 UEFI 引导服务功能仍然可用。这允许攻击者在没有物理访问权限的情况下在启用了 UEFI 安全引导的机器上做很多他们不应该做的事情，例如修改仅引导服务的 NVRAM 变量。这就是攻击者在下一步中为 bootkit 设置持久性所利用的。有关利用的更多信息，请参阅利用 CVE-2022-21894部分。

2.通过将自己的 MOK 写入 MokList ，仅限引导服务的 NVRAM 变量来设置持久性。通过这样做，它可以使用合法的 Microsoft 签名填充程序来加载其自签名（由属于写入MokList 的密钥的私钥签名）UEFI bootkit，而不是在每次启动时都利用该漏洞。在Bootkit 持久性部分中有更多相关信息。

为了使接下来两节中的详细分析更容易，我们将按照执行图（图6）中所示的步骤进行操作。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSwFGRd2elAPXT5vhib3YRq26a4N8EgkBNyXHTibMUIFuUU8c1vVS9iawcXHnmd3ejJDW1H4iaLKiaQksg/640?wx_fmt=png)图6. 绕过安全启动并使用 MOK 设置持久性

**04****‍**

**利用CVE-2022-21894**

为了绕过安全启动，BlackLotus使用接力棒 (CVE-2022-21894)：安全启动安全功能绕过漏洞。尽管它对系统安全有很大的影响，但这个漏洞并没有得到应有的公众关注。尽管该漏洞已在微软 2022 年 1 月的更新中得到修复，但由于受影响的二进制文件仍未添加到UEFI 吊销列表中，因此仍有可能被利用。因此，攻击者可以将他们自己的易受攻击二进制文件的副本带到受害者的机器上，以利用此漏洞并绕过最新 UEFI 系统上的安全启动。

此外，自2022 年 8 月以来，针对此漏洞的概念证明 (PoC) 漏洞已公开。考虑到首次提交BlackLotus VirusTotal 的日期（见图 1），恶意软件开发人员可能只是根据他们的需要调整了可用的 PoC，而没有是否需要...