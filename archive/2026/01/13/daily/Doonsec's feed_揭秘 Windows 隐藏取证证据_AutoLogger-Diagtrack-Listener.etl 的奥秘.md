---
title: 揭秘 Windows 隐藏取证证据:AutoLogger-Diagtrack-Listener.etl 的奥秘
url: https://mp.weixin.qq.com/s/_NumB9RqhH7vIQ-aCe3P6w
source: Doonsec's feed
date: 2026-01-13
fetch_date: 2026-01-14T03:33:05.797533
---

# 揭秘 Windows 隐藏取证证据:AutoLogger-Diagtrack-Listener.etl 的奥秘

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hoiaQy7WhTCPykEBv4hqdHDejr9CQX4Q8SlkSbPaibtJeibmsJxyskIQgPGwACiaDlZL0bhWHTpaa71KjcTpyMbhjw/0?wx_fmt=jpeg)

# 揭秘 Windows 隐藏取证证据:AutoLogger-Diagtrack-Listener.etl 的奥秘

Faisal Qureshi

securitainment

![]()

在小说阅读器中沉浸阅读

**受影响平台：**Windows 10、Windows 11、Windows Server 2016 及更高版本

**影响用户：**分析 Windows 遥测和 ETW 产物的系统管理员、取证调查员和事件响应人员

**影响：**当依赖未记录或填充不一致的遥测文件 (如 *AutoLogger-Diagtrack-Listener.etl*) 时，进程执行数据的取证可见性受到影响

**严重程度：**低 (主动利用) / 中等 (取证或事件响应限制)

## 事件背景

在最近的一次事件响应任务中，FortiGuard IR 服务 (FGIR) 应对了一起勒索软件攻击。攻击者大量使用反取证技术来掩盖踪迹，避免其恶意软件落入研究人员手中。他们试图通过删除创建的文件和文件夹、清除日志以及混淆恶意软件来实现这一目标。

在分析被入侵的 Windows Server 2016 系统磁盘镜像时，FGIR 在一个名为 *AutoLogger-Diagtrack-Listener.etl*的隐蔽 ETL 文件中，发现了已删除恶意软件和攻击者使用工具的历史证据。ETL 文件由 Windows ETW (Event Tracing for Windows) 基础设施生成。

## Windows 事件跟踪 (ETW) 与 AutoLogger-Diagtrack-Listener.etl 文件

Event Tracing for Windows (ETW) 是一个内置的高性能日志记录框架，使 Windows 和应用程序能够以最小开销记录详细事件。ETW 不使用纯文本日志，而是通过提供程序 (如内核、TCP/IP 协议栈或注册表) 将结构化事件数据发送到 ETW 会话。这些会话可以缓冲数据供实时使用，或将其写入二进制事件跟踪日志 (ETL) 文件。

ETW 涉及三个主要角色：**提供程序**(事件源)、**控制器**(使用 *logman*或 *PerfMon*等工具启动、停止和管理会话),以及**消费者**(如调试器、事件查看器或 EDR，负责处理和解释数据)。

该框架的强大之处在于：它提供对底层 OS 活动的精细可见性 (如进程创建、注册表写入或 DNS 查询),通过在内核模式下运行优化速度，并且由于事件可以实时使用而无需写入磁盘，从而提供灵活性。现代 EDR 工具利用此功能，直接订阅 ETW 提供程序以实时监控行为，例如进程启动。

ETL 文件 **AutoLogger-Diagtrack-Listener.etl**通常位于：

%ProgramData%MicrosoftDiagnosisETLLogsAutoLogger

此 ETL 文件记录由 **Connected User Experiences and Telemetry (DiagTrack)**服务 (也称为 **Customer Experience Improvement Program (CEIP)**) 生成的遥测数据。它在 DiagTrack 服务启用并主动收集诊断数据时创建。

![DiagTrack Service](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCPykEBv4hqdHDejr9CQX4Q8OLBicGNuajibwiadCQkMDf2EahYt9iasic7ia9cHd1LFH8UEx7P4NOUO60eA/640?wx_fmt=png&from=appmsg)

DiagTrack 服务可通过设置注册表项 AllowTelemetry 的值来配置遥测日志记录的以下四个详细级别：

| 值 | 级别 | 描述 |
| --- | --- | --- |
| **0** | Security | 服务器默认值 (无 ETL 日志) |
| **1** | Basic | 最少数据收集 |
| **2** | Enhanced | 在较新版本中已弃用 |
| **3** | Full | 完整遥测捕获 |

默认情况下，遥测级别设置为 0x1，根据我们的经验，这**不会**导致 *AutoLogger-Diagtrack-Listener.etl*文件的创建。

![Default value for AllowTelemetry registry key](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCPykEBv4hqdHDejr9CQX4Q8OfsPaRqEcFqEt8Yv93GHtiaicSOoSgN9UlOpHRrkbkibsuTiagyNAQ3QxA/640?wx_fmt=png&from=appmsg)图 2: AllowTelemetry 注册表项的默认值

## 取证发现与分析

在 IR 任务期间分析被入侵的磁盘镜像时，FGIR 在 *AutoLogger-Diagtrack-Listener.etl*文件中发现了与攻击者活动相关的可疑字符串。对 ETL 文件内 ETW 负载的解析和深入分析显示，**KernelProcess → ProcessStarted**流中的进程创建事件可以保留有价值的历史数据，包括先前执行的二进制文件的命令行详细信息。

![KernelProcess -> ProcessStarted Events](https://mmbiz.qpic.cn/mmbiz_jpg/hoiaQy7WhTCPykEBv4hqdHDejr9CQX4Q8H7IS3PulHI96xKdszT91OlR4yxt6mpJeIXdZXAJibKOYgNLlkEBlEPQ/640?wx_fmt=jpeg&from=appmsg)图 3: KernelProcess -> ProcessStarted 事件

![Ransomware Binary svhost.exe executed to encrypt drives on remote systems](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCPykEBv4hqdHDejr9CQX4Q8QviagJg1GwncADrUVBvue9xnvaPu256XMe0vItZ97qZ9xsyrT2cAGCw/640?wx_fmt=png&from=appmsg)图 4: 勒索软件二进制文件 svhost.exe 被执行以加密远程系统上的驱动器

这些 ETW 事件中记录的其他相关字段 (此提供程序的事件 ID **1**) 如下所示：

| **字段** | **描述** |
| --- | --- |
| **ProcessID** | Windows 分配的进程 ID (PID)。 |
| **ParentProcessID** | 父进程的 PID。 |
| **SessionID** | Windows 会话 ID (0 = 服务，>1 = 用户会话)。 |
| **ImageName** | 可执行文件的完整路径 (例如 C:\Windows\System32\notepad.exe)。 |
| **CommandLine** | 用于启动进程的命令行字符串 (如果由标志启用)。 |
| **UserSID** | 启动进程的用户帐户的安全标识符 (SID)。 |
| **PackageFullName** | (在现代 Windows 上) 如果是 AppX 进程，则为 UWP 应用包名称。 |
| **Flags** | 有关进程创建方式的内部标志。 |
| **Reserved** | 保留供系统使用。 |

*表 1: 进程执行详细信息*

FGIR 还提取了已被攻击者删除的二进制文件的执行证据，包括工具 **GMER**(重命名为 *gomer.exe*) 和多个恶意批处理文件。

![Evidence of Execution of GMER and Malicious Batch Files](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCPykEBv4hqdHDejr9CQX4Q8RrlDMMyO6hNiagNLTAuhJ17XPqian5kprhialnsvSXZGMXl0GEYTic9S8w/640?wx_fmt=png&from=appmsg)图 5: GMER 和恶意批处理文件的执行证据

## 受控测试与观察结果

为了确定导致 *AutoLogger-Diagtrack-Listener.etl*文件创建和填充的确切配置和状态，我们在 Windows Server 2022 和 Windows 11 系统上进行了配置更改和系统状态实验。我们将遥测详细级别值更改为 **3**,并执行以下命令将 ETL 文件写入指定位置。这导致了目标 ETL 文件的创建，但文件仍未填充任何遥测数据。

```
New-ItemProperty-Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\DataCollection" -Name AllowTelemetry -Value 3 -PropertyType DWord -Force

logman start "AutoLogger-Diagtrack-Listener" -ets

logman update "AutoLogger-Diagtrack-Listener" -o "C:\ProgramData\Microsoft\Diagnosis\ETLLogs\AutoLogger\AutoLogger-Diagtrack-Listener.etl" -ets
```

第一个命令修改 **AllowTelemetry**注册表项，将详细级别提高到最大值 (**3 – Full**)。第二个命令启动 **AutoLogger-Diagtrack-Listener**ETW 会话。第三个命令更新会话，明确将输出写入指定的 ETL 文件。这些命令共同尝试手动激活和捕获通常由 DiagTrack 服务生成的遥测数据。

尽管执行成功，但生成的文件仍为空。这表明文件的填充可能依赖于 DiagTrack 服务内部或未记录的条件。

在测试期间，FGIR 观察到，虽然可以创建 *AutoLogger-Diagtrack-Listener.etl*文件，但它并未记录任何遥测数据。进一步调查显示，该文件的填充行为可能依赖于 DiagTrack 服务的内部触发器，而这些触发器并未公开记录。

## 未解行为与研究意义

尽管进行了测试，但 *AutoLogger-Diagtrack-Listener.etl*文件在何种确切条件下被填充仍不清楚。将 **AllowTelemetry**注册表项调整为 **3 (Full)**并使用 *logman update*命令显式重新配置会话，并未导致任何事件写入文件。自动记录器会话保持可见和活动状态，但 ETL 文件仍为空。

这表明此产物的填充由 **Connected User Experiences and Telemetry (DiagTrack)**服务在内部控制，并且可能取决于未公开记录的触发器。

需要进一步研究以揭示导致 *AutoLogger-Diagtrack-Listener.etl*填充的特定条件或系统触发器。了解此文件何时以及如何记录遥测数据，可以将其转变为有价值的取证产物——特别是在进程创建和执行跟踪至关重要的事件响应调查中。我们鼓励研究人员在不同的 Windows 版本、遥测级别和服务状态下进行实验，以帮助确定此日志的证据价值。

---

> Uncovering Hidden Forensic Evidence in Windows: The Mystery of AutoLogger-Diagtrack-Listener.etl
>
> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

securitainment

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

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