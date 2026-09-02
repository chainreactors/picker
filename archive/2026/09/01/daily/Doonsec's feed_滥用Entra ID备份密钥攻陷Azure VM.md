---
title: 滥用Entra ID备份密钥攻陷Azure VM
url: https://mp.weixin.qq.com/s/z4kQPYyvR6_6TtIDt47NKA
source: Doonsec's feed
date: 2026-09-01
fetch_date: 2026-09-02T06:39:15.739274
---

# 滥用Entra ID备份密钥攻陷Azure VM

# 滥用Entra ID备份密钥攻陷Azure VM

Dubito
Dubito

云原生安全指北

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 注：本文翻译自 Altered Security 的文章《Abusing Azure VMs: BitLocker Recovery Key as an Attack Vector》[1]，可点击文末“阅读原文”按钮查看英文原文。

读者朋友们，大家好！

今天我们来探讨一个话题：**Entra ID 中备份的 BitLocker 密钥如何被滥用**。系好安全带，尽情享受这篇博客吧。

## 一、引言

在企业环境中，组织的终端和服务器通常存储着关键数据。为了满足静态数据加密策略，微软在 Windows 操作系统中引入了一项名为 **BitLocker** 的安全功能。BitLocker 用于对操作系统盘和固定数据盘实施对称加密保护，而加密密钥本身则通过恢复密钥（Recovery Key）进行保护。

在本地部署环境中，微软 Active Directory 支持借助组策略对象（GPO，Group Policy Object）存储 BitLocker 恢复密钥。众所周知，微软云生态中与 Active Directory 对应的服务是 Microsoft Entra ID。因此，对于任何 Entra ID 加入的设备，都可以将恢复密钥备份到 Entra ID。

虽然 Windows Server 并非原生支持，但可以通过 AADLoginForWindows VM 扩展将 Windows Server 加入 Entra ID。这最终将 Windows Server 的 BitLocker 恢复密钥备份覆盖范围扩大到了 Microsoft Entra ID。

## 二、背景

Azure 虚拟机（VM）作为一项服务，是 Microsoft Azure 提供的全托管的原生虚拟计算工作负载解决方案。相比之下，Azure Arc 通过 Azure Arc 代理（Connected Machine 代理），将本地和非 Azure 服务器作为 Azure Arc 启用的服务器接入，从而将其管理统一到同一个控制平面之下。

与传统数据中心一样，基于 Windows 的 Azure VM 和 Azure Arc 启用服务器的磁盘也会以快照形式进行备份。由于它们本质上仍是虚拟机，这些快照通常受 BitLocker 加密保护，在灾难恢复、迁移或作为安全备份时发挥着重要作用。

这些快照作为 Azure 的 ARM 托管资源存储，这意味着底层存储账户由 Azure 负责管理和维护，客户无法在自己的存储账户中看到它们。

> Azure 存储账户是 Microsoft Azure 提供的数据存储服务，支持多种存储服务，包括 Blob 存储（用于存储几乎所有类型的文件）、Azure 文件存储（Azure Files）、队列存储和表存储。

然而，托管磁盘快照仅适用于 Azure 原生的虚拟机服务。对于 Azure Arc 启用的服务器，管理员要么使用 Microsoft Azure 恢复服务（MARS）[2]（提供文件或文件夹级别以及卷级别的备份保护），要么依赖本地虚拟化解决方案自身来执行全磁盘快照备份。

## 三、观察发现

我们发现，在某些情况下，组织可能希望在 Azure 托管磁盘快照服务之外创建这些快照的独立副本。常见原因包括长期归档、在租户之间迁移工作负载，或为备份本身保留一份辅助副本。

为支持这些场景，Azure 允许客户将托管快照导出为 VHD（虚拟硬盘）文件，并复制到自己的 Azure 存储账户中。导出的 VHD 是磁盘数据的独立副本，不再作为 Azure 计算快照资源进行管理，而是受客户存储账户的权限、策略和访问控制约束。

我们同样发现，管理员通常会将这类非托管辅助备份保存在公司的 SharePoint 站点、NAS（网络附加存储）或专用备份解决方案中。

## 四、前提条件

本文展示的实验环境，是此前在 **Altered Security 的 2026 Azure 红队月（MoART）** 活动中首次演示成果的汇总。你可以在我们的 YouTube 频道上观看相关网络研讨会：https://www.youtube.com/watch?v=7dMXvxy3MUI。

我们将探讨以下场景：存放在不安全 SharePoint 站点上的磁盘快照非托管辅助备份，如何导致 BitLocker 加密磁盘中的数据被访问。

我们还将讨论如何通过对离线磁盘快照发动凭据窃取攻击，获取在线 Azure VM 的访问权限。

## 五、实验演示

接下来，我们以挑战实验的形式来演示该场景。本实验属于我们 Red Labs 平台（https://redlabs.enterprisesecurity.io/）的“高级实验室”类别，读者可以自行跟随操作。

1. 1. 在浏览器中，导航至 https://redlabs.enterprisesecurity.io/lab-exam/PremiumLabs/otLG8KHCe1bOHl1B7UHAL，使用你的 Google 账户进行身份验证。

![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5CAxuPrWdEh57FQqz0G22MTFrQT3fwJb59CCl0oiavVlun4EPuo4ibl1YNRFj4ZicmeU38XtKWGPXeT1xzHAbpppyptTpIV1SAsiaQ/640?from=appmsg "null")

1. 2. 建议在开始实验操作之前先下载 VHD 文件。你可以从以下链接下载：

https://redteamlabsus-my.sharepoint.com/:f:/g/personal/onedriveadmin\_redteamlabsus\_onmicrosoft\_com/IgDNqK2SPwbeSIC767pfGN3rAV91JiwsXD3PhayYyMlFtp4?e=3QE0Sa

1. 3. 下载并导入 Microburst PowerShell 模块，用于枚举实验关联的存储账户。你需要从系统中克隆该模块的目录中导入 `Invoke-EnumerateAzureBlobs.ps1`。

```
git clone https://github.com/NetSPI/MicroBurst

Import-Module "$pwd\MicroBurst\Misc\Invoke-EnumerateAzureBlobs.ps1"
```

![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5CjycFcSFt6rMf5CR5jmjh9T9NTUf3vNqQKnfxncR6Z7Fbbb3WRVnK9YpzFa48xcUtZmCALPkyYKy4uk4fU55McPcqjJVwNv28/640?from=appmsg "null")
> **注意：** 如果系统未安装 git，用户可以按照以下步骤下载、解压并将 Microburst 导入当前 PowerShell 会话。

```
$presentworkingdirectory = pwd

$presentworkingdirectory

$downloadfile = Join-Path $presentworkingdirectory "Microburst.zip"
$downloadfile

Invoke-WebRequest -UseBasicParsing -Uri 'https://github.com/NetSPI/MicroBurst/archive/refs/heads/master.zip' -OutFile $downloadfile

Expand-Archive $downloadfile -DestinationPath $presentworkingdirectory

$ps1path = Join-Path $presentworkingdirectory "MicroBurst-master\Misc\Invoke-EnumerateAzureBlobs.ps1"

$ps1path

Import-Module $ps1path
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5A4M3EOWib571IwiaXYqBc1DFmXTcKfIVmrZc2eLskFx4VxiaULrh7Lfu8zbB5icCvdcsib2ZlPpb2q0fVBcAticFZerVLicPrTQBA4l8/640?from=appmsg "null")

Microburst 的 `Invoke-EnumerateAzureBlobs` 用于查找目标组织的存储账户——我们正在合法地对其执行评估。在本案例中，目标环境是 Red Labs，因此我们在执行 `Invoke-EnumerateAzureBlobs` 时使用基础名称 redlabs。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5AJ0w7F2yM955316Km71KZj2Zh4qcibBDXq3tqC2KL2K99FicXa7dibXfayIeffialQvU4blpClvMPiaqvkZsa4JkvvoorO9rUBbwEc/640?from=appmsg "null")

```
Invoke-EnumerateAzureBlobs -Base redlabs
```

![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5DwSmnAib35YZibRhT32WSTibjErhTliaYhuFmbCTtyV5jM2Lc4icjFd6WnaXZsDyvbqFDz2K52skq9HEy3sKpttwJgWwcRu9wcnvlc/640?from=appmsg "null")
> **注意：** 你可以忽略调用 cmdlet 时 PowerShell 终端上显示的错误，它仅表示工具无法显示进度。

1. 4. 使用实验提供的凭据登录 Azure 门户。登录时，系统会提示你注册 MFA，你可以按照挑战实验页面上的“MFA 绕过”部分所述步骤进行操作。

![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5BiaVictsAoia8WKhuaibxmVo7JwOEDCJiaIRo1OOIWdHJwElyPV1qeYycNrVNgfjLCw5r1ichr6ZnK9Vv3dzqqTseiadTZxwVHykrwFY/640?from=appmsg "null")![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5CSPXRFmFUVbTAHNJ2yG0hHoiccAPaR2KsFL3Kicia76myzkXSiaztABWnOS0H77bThvAMdxS0d16sYJAvvjIzpdWhPgJzzWib7RQOM/640?from=appmsg "null")

或者，你也可以按照“MFA 绕过”部分列出的步骤，使用 Az PowerShell 模块登录。登录后，可以按如下方式验证上下文：

```
Get-AzContext
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5D2CPEiaGEIgV9KMcUYibtjdyarj1y2oYjVJFgZK4QjJMlWiaVfqT0PkuGNQAJ43IUNSSEaulAwtn8VibeDPeOabibib0lj0xT2mFOT8/640?from=appmsg "null")

1. 5. 枚举资源组及其下的所有资源。我们发现了 1 台 Azure Arc 启用服务器和 3 个存储账户。

![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5CGEHJGvIf9M7Tm4PAkrKoXjiblD3ceMSUQQzxsxPXCUIoStN9gibN62GlSVo6WFW68xC2MXicj9sg6ibicrJq9zrV7llQLiaJkaRVf4/640?from=appmsg "null")![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5C8ulbATHWEw0Js1Ric3icQswCicyYLgLWWuic2GtxK0XeWZc6fLXMnaQ08ro2KibPUNAYnPaibJuuKr3jeiaBFCe1H5K29GSzI7miaWvs/640?from=appmsg "null")

或者，也可以使用以下 Az PowerShell cmdlet 通过 PowerShell 进行发现。

```
Get-AzResourceGroup

Get-AzResource -ResourceGroupName ((Get-AzResourceGroup).ResourceGroupName)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5B46YH8C3bckHKA3dVRzddKhyFCTYUjuZRdEB9X5P7tbNbpxicrgPcQwVSoQUGtITJFnuhPibRZndhXt72V6GeOsu8GT07a72BCA/640?from=appmsg "null")

1. 6. 为了了解我们拥有的权限，必须首先检查 IAM 下的 RBAC 角色分配，以确认我们的用户在资源组上的权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5AI6iaicj6EQyVWibicXTeWib2YuZajrstmRfeED5yIwibuIWXNksfW8VUujwZU8CvYB0qluJc6an1nfx8yWGq8JTkhppREU9XJCiao1s/640?from=appmsg "null")

或者，也可以使用以下 Az PowerShell cmdlet 来收集我们用户的角色分配信息。

```
$resourcegroupname = ((Get-AzResourceGroup).ResourceGroupName)

$Accountcontext = Get-AzContext

$accountId = $Accountcontext.Account.Id

Get-AzRoleAssignment -SignInName $accountId -ResourceGroupName

$resourcegroupname | Select RoleDefinitionName, Scope
```

![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5C3ibRBUX0wgSJbmQ3V6xLNKUUFQIgveSgUWnmM8AX1k0k4GX9Uulibq5VPib21FawyTicmkPtaCKiaEQEzibzFv30exJrJaxrMIuSXE/640?from=appmsg "null")

1. 7. 既然我们拥有存储 Blob 数据读取者角色，让我们探索在外部枚举期间发现的两个存储账户。

![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5BUqIj4ibq8Z4O1HXRIyJZlkSxr8IZIF5tDrkcrzS6icy8RlowGNEnYPf9ialu0ObN2NoY2UOW7CLqfbn1e7kUmWRcuR7M26pJXIs/640?from=appmsg "null")![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5CVAQezLLFcPzBMbEUDKFGj21yfMENaIprOcbKKugsT0oiaEbSXB9njrc1ibf4DUI8sJYiaDKZqQ7FdzEQKscaodDztYtBO8MIANI/640?from=appmsg "null")![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5D95LHgBDiaTPBL4VfXblJAJkVn99Y9IDuF5TF1OWLY13AKZfgUvT8oPQMicBRNKqCM3wvdYibibMc2Pmibw0OJSYUQkjfUwghhTibfQ/640?from=appmsg "null")![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5AE4mGBhoLQu63Rh1lMfaib69O1gWHo02o0IPtaeuU9Y8LYLFrR0TqU0W1hxhEiaNy5EF1NWiaRyeGAG4bXiac4p6CY1SKOibvwyOU0/640?from=appmsg "null")![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5AnU3frKQ8jKxOysiaTB7JFicibF6aeAO0OogaNlVTVKkiahbE3BOR2sHha9IATmTBIunTBUKSqdjjyHIncuZL4PF5M1n2wmMf2Zu8/640?from=appmsg "null")![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5BKEZYqI9Ztg1pxuO9bMFPgnQpyDCQzcoNicWQRPDN73HnK9OiapQJVHaiaxElC2CF6yCIE8BAZicajE9ibdpBHiceT2MgmzRkDeHdVc/640?from=appmsg "null")

或者，使用 Az PowerShell，我们也可以确认第一个存储账户确实为空，而第二个存储账户中的 Blob 指向 SharePoint 链接。

```
$ctx = (Get-AzStorageAccount -Name "redlabsinternal" -ResourceGroupName $resourcegroupname).context

$ContainerName = (Get-AzRmStorageContainer -ResourceGroupName

$resourcegroupname -StorageAccountName "redlabsinternal"); $ContainerName

$FileShareName = (Get-AzRmStorageShare -ResourceGroupName

$r...