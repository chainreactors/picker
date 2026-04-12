---
title: Storm-1175 高频勒索攻击全链路：从 N-day 漏洞到 Medusa 部署最快仅 24 小时
url: https://mp.weixin.qq.com/s/pgtf9R-smm085Jsi3BwbZA
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:43:59.480505
---

# Storm-1175 高频勒索攻击全链路：从 N-day 漏洞到 Medusa 部署最快仅 24 小时

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/PO9bjOzlHYDz7NgmYU9CUuONCT31EyEY3zbvePuoy8s0pDUnaS49BLPG1ossicMicoHGiaCSqcEAMYA0D16ib9fUY01Eruic9JdEmZERfrNFYAaY/0?wx_fmt=jpeg)

# Storm-1175 高频勒索攻击全链路：从 N-day 漏洞到 Medusa 部署最快仅 24 小时

bitbot
bitbot

Desync InfoSec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

微软威胁情报团队最新披露：一个名为 **Storm-1175** 的高活跃度勒索软件组织，正持续利用已公开的 N-day 漏洞（甚至零日漏洞）攻击暴露在公网的系统。从初始入侵到部署 **Medusa 勒索软件**，整个攻击链最快仅需 **24 小时**。

该组织近期重点打击医疗、教育、金融等行业，覆盖澳大利亚、英国和美国。以下是完整攻击链深度剖析与防御建议。

────────────────

一、攻击者画像：Storm-1175

Storm-1175 是微软追踪的一个以经济利益为驱动的网络犯罪组织，专注于高频率勒索软件攻击。其核心特征：

**⚡ 极速武器化 N-day 漏洞**：在漏洞公开披露后极短时间内即发起攻击，最快仅 1 天。
**⚡ 零日漏洞能力**：已观察到至少 3 次零日漏洞利用，包括在公开披露前一周即发起攻击。
**⚡ 快速横向移动**：从初始访问到勒索软件部署，通常 5-6 天，极端情况仅 24 小时。

────────────────

二、漏洞利用武器库（2023-2026）

自 2023 年以来，微软已观测到 Storm-1175 利用超过 **16 个漏洞**进行初始访问，覆盖以下产品：

|  |  |
| --- | --- |
| CVE 编号 | 受影响产品 |
| CVE-2023-21529 | Microsoft Exchange |
| CVE-2023-27350 / CVE-2023-27351 | PaperCut |
| CVE-2023-46805 / CVE-2024-21887 | Ivanti Connect Secure |
| CVE-2024-1709 / CVE-2024-1708 | ConnectWise ScreenConnect |
| CVE-2024-27198 / CVE-2024-27199 | JetBrains TeamCity |
| CVE-2024-57726/27/28 | SimpleHelp |
| CVE-2025-31161 | CrushFTP |
| CVE-2025-10035 ⚠️ 零日 | GoAnywhere MFT |
| CVE-2025-52691 / CVE-2026-23760 ⚠️ 零日 | SmarterMail |
| CVE-2026-1731 | BeyondTrust |

**⚠️ 关键发现：**Storm-1175 曾在 CVE-2025-31324（SAP NetWeaver）披露后仅 **1 天**即发动攻击。此外，该组织还展示了利用零日漏洞的能力，在公开披露前一周即完成武器化。

图1：Storm-1175 漏洞利用时间线（披露 vs 实际利用日期）

────────────────

三、完整攻击链解析

图2：Storm-1175 完整攻击链

阶段 1：初始访问 — 利用暴露的 Web 资产

Storm-1175 专门瞄准暴露在公网的 Web 应用和服务。该组织还会将多个漏洞串联利用以实现更深层次的攻击。例如，在 2023 年 7 月的攻击中，攻击者先利用 CVE-2022-41080 通过 OWA 获取 Exchange PowerShell 访问权限，再利用 CVE-2022-41082 实现远程代码执行（即 "OWASSRF" 攻击链）。

该组织还展示了攻击 Linux 系统的能力：2024 年底，微软发现其利用 Oracle WebLogic 漏洞攻击了多个组织。

阶段 2：持久化与横向移动

在入侵成功后，Storm-1175 通常会部署 Web shell 或远程访问载荷建立立足点。随后：

**1. 创建管理员账户** — 在被入侵设备上新建用户并加入管理员组
**2. 使用 LOLBins 横向移动** — 主要使用 PowerShell 和 PsExec
**3. Cloudflare 隧道** — 将隧道工具重命名为 conhost.exe 等合法程序名，通过 RDP 横向移动
**4. 修改防火墙** — 如果 RDP 被禁用，直接修改 Windows 防火墙策略启用远程桌面

图3：Storm-1175 修改防火墙并启用远程桌面以实现横向移动

Storm-1175 大量使用远程监控和管理（RMM）工具，自 2023 年以来使用过的 RMM 工具包括：

• Atera RMM  • Level RMM  • N-able  • DWAgent
• MeshAgent  • ConnectWise ScreenConnect  • AnyDesk  • SimpleHelp

**工具亮点：**Storm-1175 还频繁使用 **PDQ Deployer**（合法软件部署工具）进行横向移动和载荷分发，包括最终的勒索软件部署。此外，该组织还利用 **Impacket** 进行横向移动。

阶段 3：凭据窃取

凭据窃取是 Storm-1175 攻击链中的关键环节：

**LSASS 转储** — 通过 Impacket 和 Mimikatz 进行凭据转储，或利用 LOLBins 技术（修改注册表启用 WDigest 凭据缓存、使用 Task Manager 导出 LSASS 凭据）

**Veeam 备份密码恢复** — 获取管理员凭据后，使用脚本从 Veeam 备份软件中恢复密码，用于连接远程主机

**NTDS.dit 提取** — 使用 PsExec 跳转到域控制器，提取 Active Directory 数据库（含用户数据和密码），可离线破解

**SAM 数据库访问** — 获取安全账户管理器数据，全面了解和操控系统环境

阶段 4：安全防御绕过

在部署勒索软件前，Storm-1175 会系统性地削弱安全防护：

• 修改注册表中的 **Microsoft Defender** 设置，阻止其拦截勒索软件载荷
• 使用编码的 PowerShell 命令将 C:\ 盘添加到杀毒软件**排除路径**
• 需要高度特权账户才能完成这些操作 — 这正是凭据窃取如此关键的原因

阶段 5：数据外传与勒索部署

Storm-1175 实施**双重勒索**策略 — 不仅加密数据，还窃取数据威胁公开泄露：

**数据打包** — 使用 Bandizip 收集文件
**数据外传** — 使用 Rclone 将数据同步到攻击者控制的云端资源，支持实时持续外传
**勒索部署** — 通过 PDQ Deployer 执行 RunFileCopy.cmd 脚本投放 Medusa 勒索软件，或通过组策略（GPO）大范围部署

────────────────

四、IoC 情报指标

|  |  |  |
| --- | --- | --- |
| 类型 | 值 | 描述 |
| SHA-256 | 0cefeb6210b7103fd32b996beff518c9b6e1691a97bb1cda7f5fb57905c4be96 | Gaze.exe（Medusa 勒索软件） |
| SHA-256 | 9632d7e4a87ec12fdd05ed3532f7564526016b78972b2cd49a610354d672523c | lsp.exe（Rclone） |
| SHA-256 | e57ba1a4e323094ca9d747bfb3304bd12f3ea3be5e2ee785a3e656c3ab1e8086 | main.exe（SimpleHelp） |
| SHA-256 | 5ba7de7d5115789b952d9b1c6cff440c9128f438de933ff9044a68fff8496d19 | moon.exe（SimpleHelp） |
| C2 IP | 185.135.86[.]149 | SimpleHelp C2（活跃至 2026-03-15） |
| C2 IP | 134.195.91[.]224 | SimpleHelp C2（活跃至 2026-02-26） |
| C2 IP | 85.155.186[.]121 | SimpleHelp C2（活跃至 2026-02-12） |

────────────────

五、防御建议

微软针对 Storm-1175 的 TTPs 提出了以下关键防御措施：

**1. 攻击面管理** — 使用外部攻击面管理工具（如 Microsoft Defender EASM）了解组织的数字足迹，尤其是暴露在公网的系统

**2. 网络边界加固** — Web 面向系统应与公网隔离，必须暴露的服务应放在 WAF 或反向代理后方

**3. 凭据防护** — 启用 Credential Guard（Windows 11 默认开启），限制本地管理员权限使用，不共享本地管理员密码

**4. 防篡改保护** — 全租户开启 Tamper Protection，配置 DisableLocalAdminMerge 阻止通过 GPO 修改杀毒排除

**5. RMM 管控** — 对批准的 RMM 工具强制 MFA，发现未批准的 RMM 安装立即重置相关账户密码

**6. 攻击面缩减规则** — 启用 ASR 规则阻止凭据窃取、混淆脚本执行、Webshell 创建、PsExec/WMI 进程创建

**💡 核心防御逻辑：**Storm-1175 的攻击链中，凭据窃取是关键转折点。优先处理与凭据窃取相关的告警（通常意味着环境中存在活跃攻击者），可有效阻止后续的勒索软件部署。

────────────────

**来源：**Microsoft Threat Intelligence Blog
**原文链接：**microsoft.com/security/blog
**发布日期：**2026 年 4 月 6 日

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeFpGrKMFU4NyWgYxhTTtARibcgd8y7msMIlZEicN5zxiahgsxzNcOurtGuBkTJYdp1ZFEN1lDF8EbDw/0?wx_fmt=png)

Desync InfoSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeFpGrKMFU4NyWgYxhTTtARibcgd8y7msMIlZEicN5zxiahgsxzNcOurtGuBkTJYdp1ZFEN1lDF8EbDw/0?wx_fmt=png)

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