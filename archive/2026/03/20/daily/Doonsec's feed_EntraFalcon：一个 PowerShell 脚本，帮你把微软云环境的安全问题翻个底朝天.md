---
title: EntraFalcon：一个 PowerShell 脚本，帮你把微软云环境的安全问题翻个底朝天
url: https://mp.weixin.qq.com/s/ZokeVWflEs5CY4YixbFE2w
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:00:58.048999
---

# EntraFalcon：一个 PowerShell 脚本，帮你把微软云环境的安全问题翻个底朝天

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibfZQIVHSmbk3RxdXbGnZnZib0LWLdribaQNfts2EKTuL3Ribicicl9PVG82EffG29CfmtLedBpV2Sjx7ojAdJCTicRfgiaVnNWC9xpyicM/0?wx_fmt=jpeg)

# EntraFalcon：一个 PowerShell 脚本，帮你把微软云环境的安全问题翻个底朝天

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> EntraFalcon 是一款开源的 PowerShell 评估工具，专为检验 Microsoft Entra ID（原 Azure AD）环境安全而生。它无需额外依赖，能一键发现特权账号、风险配置和条件访问策略漏洞，并用交互式 HTML 报告呈现结果，是渗透测试和安全审计的实用帮手。

## 工具是干什么的

评估云环境安全，听起来就麻烦。你得有相应权限，还得搞清楚去哪里查、查什么。EntraFalcon 想解决的就是这个痛点。它是一个基于 PowerShell 的脚本，专门用来帮你快速评估 Microsoft Entra ID 环境的总体安全状况。

它的目标用户很明确：渗透测试人员、安全分析师和系统管理员。你不用安装额外的 PowerShell 模块，也不用为 Microsoft Graph API 专门申请授权。脚本兼容 PowerShell 5.1 和 7，在 Windows 和 Linux 上都能跑。

这个工具能帮你揪出那些容易被忽略的风险点，比如：

* 能控制高权限群组或应用的用户
* 权限过大（例如拥有 Microsoft Graph API 或 Azure 角色权限）的企业应用（无论来自外部还是内部）
* 直接在资源上被分配了 Azure IAM 角色的用户
* 从本地同步上来的特权账号
* 长期不活动的用户，或者没设置多因素认证（MFA）的用户
* 在敏感分配（例如条件访问策略排除项、订阅所有者、特权群组的合格成员）中使用的、未受保护的群组

最后，它会把所有发现整理成一份可交互的 HTML 报告，你可以筛选、排序、导出数据，分析起来方便多了。

## 核心功能一览

功能列出来不少，但核心就几点：简单、全面、可读性强。

* 一个 PowerShell 脚本搞定，支持 PowerShell 5.1 和 7，跨平台运行。
* 内置多种认证方式，适应不同环境。
* 利用微软官方应用预先同意的权限范围，省去手动授权 Graph API 的麻烦。
* 生成可导航的 HTML 报告，支持筛选、排序、数据导出。
* 执行超过 60 项自动化检查，并生成一份“安全发现报告”汇总结果。
* 检查内容涵盖租户的弱配置、对象的风险属性和权限。
* 对发现的问题提供严重等级、问题描述、潜在威胁和修复建议。
* 列出受影响的具体对象，并能直接链接到详细报告进一步分析。
* 进行基础的影响、可能性和风险评分，帮你高亮那些保护薄弱的高特权对象，并对数据进行排序。
* 为风险配置和过高权限显示警告。
* 枚举的 Entra ID 对象类型很全，包括用户、群组、企业应用、应用注册、托管标识等。
* 还能检查 PIM（Privileged Identity Management）分配：包括 Entra 角色、Entra 群组和 Azure 角色的 PIM。
* 检查条件访问策略、管理单元和 PIM 设置。

## 运行前要准备什么

想用这个工具，你手里得有相应的权限。说白了，你得能“看”到环境里的东西。

| 类型 | 所需权限 | 是否必须 | 缺少的后果 |
| --- | --- | --- | --- |
| Entra ID 角色 | 全局读取者（Global Reader） | 是 | 脚本根本跑不起来 |
| Azure 角色 | 读取者（Reader）：针对每个管理组或订阅 | 否 | 无法评估 Azure IAM 角色分配 |

另外，你用来运行工具的电脑，必须能成功认证到 Microsoft Graph API，如果还想评估 Azure 部分，也得能连上 Azure ARM API。记得确认条件访问策略不会把你登录的请求给拦了。

## 怎么把它用起来

### 下载脚本

第一步是把代码弄到本地。打开终端，执行：

git clone https://github.com/CompassSecurity/EntraFalcon
cd EntraFalcon

注意：运行脚本前，你可能需要临时改一下 PowerShell 的执行策略。只对信任的脚本这么干！

Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process

### 选择认证方式并运行

EntraFalcon 内置了好几种认证流程，用来应对不同环境（比如有没有图形界面）和限制。

| 认证流程 | Windows | Linux/macOS | 交互登录次数 | 便利性 | 参数 | 说明 |
| --- | --- | --- | --- | --- | --- | --- |
| BroCi（默认） | 是 | 否 | 1 | 高 | -AuthFlow BroCi | 避开对旧客户端（如 Azure AD PowerShell）的依赖，仅限 Windows。 |
| 授权码流程 | 是 | 否 | 4 | 一般 | -AuthFlow AuthCode | 标准的非 BroCi 授权码流程，仅限 Windows。 |
| 设备代码流程 | 是 | 是 | 3 | 一般 | -AuthFlow DeviceCode | 认证可在另一台设备完成，但有两个安全检查会降低深度。 |
| 授权码 + 手动代码 | 是 | 是 | 4 | 低-一般 | -AuthFlow ManualCode | 认证可在不同设备或浏览器会话完成。 |
| BroCi + 手动代码 | 是 | 是 | 1 | 低 | -AuthFlow BroCiManualCode | 需要手动从浏览器开发者工具提取授权码。 |
| BroCi + Token | 是 | 是 | 0 | 低 | -AuthFlow BroCiToken -BroCiToken “令牌” | 直接使用已有的 Azure 门户刷新令牌。 |

如果你在 Windows 上，直接用默认的 BroCi 流程最省事：

.\run\_EntraFalcon.ps1

或者在非 Windows 环境下用设备代码流：

.\run\_EntraFalcon.ps1 -AuthFlow DeviceCode

> 使用 `DeviceCode` 时，如果环境加固过，可能会被条件访问策略拦截。另外，这会使得两个安全检查（`CAP-004`和`CAP-005`）的深度降低。

### 其他有用的参数

脚本还支持一些可选参数来调整行为：

* **包含微软官方应用**

  ：默认为了减少干扰，会排除官方的微软企业应用。用 `-IncludeMsApps` 参数可以把它们也纳入评估。

  .\run\_EntraFalcon.ps1 -IncludeMsApps
* **跳过群组 PIM 评估**

  ：如果你不想检查群组的 PIM 分配，可以用 `-SkipPimForGroups` 跳过，这样能省掉一次额外的认证。

  .\run\_EntraFalcon.ps1 -SkipPimForGroups
* **其他参数**

  ：比如 `-Tenant` 指定要评估的租户（不是当前账号的主租户时有用），`-OutputFolder` 自定义报告输出目录，`-Csv` 同时生成 CSV 报告文件等。

## 报告长什么样？

说再多不如看看实际产出。EntraFalcon 会生成一系列 HTML 文件，每个文件对应一个对象类型的详细视图。报告是交互式的，你可以直接在上面操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibcgBKux7Ej1lYbQefxuBrkiaicF1ZibqGMM01I6aUA4T3vlUCjWcRBqiciaFtfM5icaLgML2wHtpujPXeiaFONxv8pMWPW3foamvdtdWA/640?wx_fmt=png&from=appmsg)

▲ 安全发现总览报告，汇总了所有风险项和评分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibc53ibg3vBa8VNI0cnvick0Qe0eJscW1CB6Q8r6IxHFXqiccbDQHHyibyicicxlRsXz1BEAQs7KLXyKBsu0ib6K6UTswzBcibewnx1KibJI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibez6JrAvDYpuQnibY0RE5XNgH9KOzwDnu81DnRQGrlsK5ibaiciay42oumccticyhqse3kGVlgjsSa8fIkrTFC0icLvnibC8lBBzoG7tI/640?wx_fmt=png&from=appmsg)

▲ 用户列表报告，可以按风险排序。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcmAhdg7ahuZ43UyFiaGLGnDvJh1VLlCYscntBTsVGUKzTMMBdpTa2kXhfvF8keVmWbwcSeXibEfwDTHR55dVFPRW9DMiblnv33Ok/640?wx_fmt=png&from=appmsg)

▲ 单个用户的详细信息页。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibeRQlfibOYp4885EWa8pX7FoIv4zZt8mT8hDko4wEQoB7Mq81r3gRUsHWbeibDI4tbvCGH7Jld6r7OicENkOLfmDma0MuXjkH1zwU/640?wx_fmt=png&from=appmsg)

▲ Entra ID 角色分配情况。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibdD2WiacIHTymvLpRtsxiacn5W5ibgBkD06GicicOUnlXkVf9wMEpAwwlNC3EE5q79J13C3Py0RIwJhX2s58yfog939QHjrKrLBKmCU/640?wx_fmt=png&from=appmsg)

▲ Azure 角色分配情况。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibf0UugEADibZP52LUAp3xNcxR0YjwBWP0y7HDibM12DVsjro7gOS2iaiajz5icKv3vU7UHJObCsu2aOB0sdsBIqXgrz5MPBflwSGI4s/640?wx_fmt=png&from=appmsg)

▲ 企业应用的详细信息。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfQZPpRmhSWb958oG9aJNicyLJf3ZZYZLydBSkFSZ9tqTpFB8na8u0x5HzIbQFchvbX1G7RotP3D9VuBoSIGC8PTQr89GMJxehc/640?wx_fmt=png&from=appmsg)

▲ 条件访问策略列表。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdHUTLJlCQOichqMNIMp06tBbDuvqS3K5j8uZyyT2YOEk49zAQHkwjoM5I4P7OqjM8KB4Tuz5769Zab5M6icC3mp04ah0JQsoH6M/640?wx_fmt=png&from=appmsg)

▲ 单个条件访问策略的详细配置。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcsibUkk7tice4XwicFJ8x8ctLC3Lckyqibj0oFuVoqjMgroCsNDzqeHHLQ1XWZorcBECnibHBLTQeoA5uuyp2aeG6F9bicUxaKVia2RQ/640?wx_fmt=png&from=appmsg)

▲ PIM 角色设置情况。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcqvNakEGr0DibvetJCftOONJibLV2kDsbALmmx2pKA8icMeAPFqy2sdusmjEXdeWTrJKsE6TW39bjI6xxuRTcHm0Bib7swcClRicxo/640?wx_fmt=png&from=appmsg)

▲ 枚举结果摘要，包含各类对象的统计。

### 报告互动小技巧

生成的 HTML 报告不只是用来看的：

* 点 ⚙️ 按钮可以显示或隐藏列。
* 点 💾 可以把当前看到的数据导出成 CSV。
* 点 👁 可以复制当前的筛选、排序和列选择，生成一个可分享的链接。
* 点 🧰 可以应用预设的视图。
* 点对象名称可以跳转到该对象的详细信息，甚至能跨报告跳转。
* 可以通过在 URL 后加 GET 参数直接应用筛选、选择列或排序，比如 `?EntraRoles=>1&Enabled=true`。

## 它背后的评分逻辑

报告里会给对象打“影响”、“可能性”和“风险”分。这是什么意思？

* **影响**

  ：代表对象拥有的权限量或严重程度。
* **可能性**

  ：代表这个对象被攻陷或影响的难易程度，也反映了它的保护水平。
* **风险**

  ：算出来的分数，公式是 影响 × 可能性 = 风险。

> 这个评分只是一个基础的评估，目的是帮你给表格里的条目排序和确定优先级。不同类型的对象或报告之间的风险分数不能直接比较。它**不能替代完整的风险评估**。

为了打分，工具内部对 Entra ID 和 Azure 的角色做了大致的分级。比如，“全局管理员”比“全局读取者”的影响分要高得多，即使微软都把两者算作特权角色。

对于 Azure 角色，这个分级就没那么精确了，因为实际影响很大程度上取决于角色分配的范围。比如，一个“所有者”角色分配在一台虚拟机上，和分配在整个订阅上，影响力天差地别。

应用权限也被分了级。有些 API 权限（比如 `RoleManagement.ReadWrite.Directory`）能让应用直接升级成全局管理员，这类权限被标记为“危险”，拥有它们的应用影响分就高。

## 蓝队注意：这东西能被发现吗？

能，而且很容易。EntraFalcon 并不隐秘。在那些记录并监控 Microsoft Graph API 和 Azure 登录活动的环境里，它的行踪会被发现。

默认情况下（使用非 BroCi 流程），工具通常会发起 4 次交互式登录和 1 次非交互式登录。蓝队可以在登录日志里监视下面这些应用 ID，或者留意异常的 Graph API 流量、令牌刷新和批量请求行为。

### 默认（非BroCi）认证使用的应用

| 应用 ID | 类型 | 资源 ID | 目的 |
| --- | --- | --- | --- |
| 1b730954-1685-4b74-9bfd-dac224a7b894 | 交互式 | 00000003-0000-0000-c000-000000000000 | 获取群组 PIM 数据 |
| 04b07795-8ddb-461a-bbee-02f9e1bf7b46 | 交互式 | 00000003-0000-0000-c000-000000000000 | 获取通用租户对象数据 |
| 51f81489-12ee-4a9e-aaae-a2591f45987d | 交互式 | 00000003-0000-0000-c000-000000000000 | 获取 Entra / Azure 角色 PIM 数据 |
| 80ccca67-54bd-44ab-8625-4b79c4dc7775 | 交互式 | 00000003-0000-0000-c000-000000000000 | 获取安全检查策略上下文 |
| 04b07795-8ddb-461a-bbee-02f9e1bf7b46 | 非交互 | 797f4846-ba00-4fd7-ba43-dac1f8f63013 | 获取 Azure IAM 角色分配数据 |

### BroCi 认证使用的应用

| 应用 ID | 类型 | 资源 ID | 目的 |
| --- | --- | --- | --- |
| c44b4083-3bb0-49c1-b47d-974e53cbdf3c | 交互式 | 00000003-0000-0000-c000-000000000000 | 初始认证，为 BroCi 获取刷新令牌 |
| 50aaa389-5a33-4f1a-91d7-2c45ecd8dac8 | 非交互 | 00000003-0000-0000-c000-000000000000 | 获取群组 PIM 数据 |
| 50aaa389-5a33-4f1a-91d7-2c45ecd8dac8 | 非交互 | 01fc33a7-78ba-4d2f-a4b7-768e336e890e | 获取群组 PIM 数据 |
| 74658136-14ec-4630-ad9b-26e160ff0fc6 | 非交互 | 00000003-0000-0000-c000-000000000000 | 获取通用租户对象数据 |
| 74658136-14ec-4630-ad9b-26e160ff0fc6 | 非交互 | 797f4846-ba00-4fd7-ba43-dac1f8f63013 | 获取 Azure IAM 角色分配数据 |

## 有什么局限性？

工具虽好，但别把它当万能钥匙。它现在不评估 M365 RBAC、Defender for Endpoint RBAC 和 Intune RBAC。

云平台变化快，有些检测逻辑可能会过时。租户配置越来越复杂，某些特定的设置组合可能导致结果不准确。所以，永远建议你独立验证重要的发现，别光靠工具做关键决策。

另外，生成的 HTML 报告没有做防跨站脚本（XSS）的保护，别把它放在公开可访问的地方。

## 适用场景与一句话总结

EntraFalcon 适合那些需要对微软 Entra ID 环境做快速安全体检的场景，比如内部红队评估、渗透测试的初期信息搜集、云安全审计的辅助工具...