---
title: 在 Mythic 中掌控紫队演练
url: https://mp.weixin.qq.com/s/vvTLhQI6_ZtRjndbdy70Xw
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:40:25.722010
---

# 在 Mythic 中掌控紫队演练

# 在 Mythic 中掌控紫队演练

原创

网安之家
网安之家

网安之家-CyberHomestead

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

Crucible：把原子测试编译成独立程序，在 Mythic 中掌控紫队演练

**面向 Mythic C2 的对手模拟代理——将 Atomic Red Team YAML 编译成可独立运行的 Windows 与 Linux 可执行文件，用于紫队演练。**

平台 · .NET · Mythic · 许可证

Crucible 是什么？

Crucible 是一款专为紫队对手模拟打造的 Mythic C2 代理。它将 Atomic Red Team 的 YAML 测试定义转换为可独立运行的 .NET 9 可执行文件，支持 Windows 和 Linux。

程序启动后，以 Mythic 回连会话（callback）的形式向服务端报到，等待操作员下发任务，再按指令执行演练，并将每项技术的执行结果实时回传至 Mythic 界面。

工作流程

1.

操作员在 Mythic 界面中配置演练任务：指定技术 ID、威胁组织、ATT&CK Navigator 图层，或上传 YAML。

2.

Mythic 容器编译出可独立运行的 .NET 9 可执行文件，将演练清单与 C2 配置嵌入其中。

3.

操作员将可执行文件部署到目标终端。

4.

代理向 Mythic 报到，然后保持空闲——**不会自动执行演练。**

5.

操作员通过 Mythic 回连会话界面下发 `run_campaign`。

6.

代理按攻击链顺序执行各项技术，将每项技术的结果以结构化 JSON 回传。

7.

执行过程中，操作员可以通过 `abort` 中止、通过 `skip_technique` 跳过技术，或通过 `campaign_status` 查询状态。

8.

浏览器脚本在 Mythic 任务输出中渲染以颜色区分状态的结果表格。

9.

JSON 日志、HTML 报告和 Markdown 报告写入目标终端的磁盘。

Crucible 同时提供独立 CLI，无需 Mythic 基础设施，也能构建和运行演练任务。

代理行为

回连代理：Mythic 模式

通过 Mythic 配合 C2 配置文件构建时，编译后的可执行文件会作为持续运行的回连代理工作：

■

通过 HTTP 向 Mythic 报到，并提交主机信息：主机名、用户、域、PID、IP 地址、操作系统和架构。

■

按配置的间隔发送带随机抖动的信标，轮询操作员任务。

■

演练执行结束后仍保持运行，可以再次接收任务。

■

**不自动执行：只有操作员明确发送 `run_campaign`，演练才会启动。**

■

演练在后台线程中运行，因此代理能够即时接收 `abort` 和 `skip_technique` 指令。

独立模式

如果可执行文件的清单中没有 C2 配置，也就是通过 CLI 构建的情况，程序会立即执行演练，将结果打印到控制台，把日志和报告写入磁盘，然后退出。

代理执行什么？

Windows 目标

■

PowerShell 测试使用 `powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -EncodedCommand`。

■

命令提示符测试使用 `cmd.exe /c`；多行命令通过临时 `.bat` 文件执行。

Linux 目标

■

Bash 测试使用 `/bin/bash -c`；多行命令通过临时 `.sh` 文件执行。

■

sh 测试以 `/bin/sh -c` 作为回退执行方式。

■

为支持跨平台 ART 测试，Linux 上会将 PowerShell/cmd 执行器名称映射为 bash/sh。

这些执行方式与 Atomic Red Team 框架使用的方式相同。代理会创建子进程，并在运行时自动检测平台。

运行要求与配置

目标终端要求

| 要求 | 说明 |
| --- | --- |
| 操作系统 | Windows 10/11、Windows Server 2016+，或 Linux（内核 4.x+，x64） |
| 运行时 | 无需额外安装——二进制文件自包含，已打包 .NET 9；Windows 版本约 78 MB，Linux 版本约 81 MB |
| PowerShell | Windows 上基于 PowerShell 的原子测试需要 PowerShell，且必须位于 PATH 中 |
| 管理员权限 | 可选，但建议具备。未提升权限时，标记为 `elevation_required` 的测试会被跳过；Linux 上通过 `id -u == 0` 检查 |
| 网络 | 代理模式需要向 Mythic C2 服务器发起出站 HTTP/HTTPS 连接；独立模式不需要 |

终端准备：紫队演练

对于已获授权的紫队演练，通常需要在目标终端完成以下准备。

Windows Defender / 杀毒软件排除项

编译后的 Crucible 二进制文件会被大多数 AV/EDR 产品标记，因为它会通过编码命令启动 `powershell.exe`，并执行与已知攻击模式相关的技术。这是设计使然——在紫队演练中，需要平衡检测验证与演练执行。

**方案 A：完整排除，原文推荐用于初始验证。**

```
# 排除 Crucible 二进制文件路径
Add-MpPreference -ExclusionPath "C:\Temp\crucible.exe"

# 或排除部署目录
Add-MpPreference -ExclusionPath "C:\Temp\"
```

**方案 B：仅配置进程排除项。**

```
Add-MpPreference -ExclusionProcess "crucible.exe"
Add-MpPreference -ExclusionProcess "CrucibleRunner.exe"
```

**方案 C：不配置排除项，验证检测能力。**

不配置任何排除项运行，以验证蓝队检测规则能否正确触发。应预期二进制文件和/或子进程可能在演练中途被终止。JSON 日志采用写入即刷盘机制，能够保留进程终止前的执行结果。

Linux 终端准备

Linux 目标通常比 Windows 需要更少的准备工作：

■

大多数 Linux AV/EDR 产品，如 CrowdStrike Falcon、SentinelOne 和 Carbon Black，会标记携带编码命令或可疑命令的 `bash -c`。按需添加进程或路径排除项。

■

确保 `/bin/bash` 和/或 `/bin/sh` 可用；主流发行版通常均已提供。

■

对于需要 root 权限的测试，以 root 身份或通过 `sudo` 运行代理。非 root 代理会跳过需要提升权限的测试。

■

代理会将日志写入配置的 `log_path`，请确保该目录可写。

```
mkdir -p /opt/purpleteam
```

EDR 注意事项

如果部署了 CrowdStrike、SentinelOne、Defender for Endpoint 等 EDR：

■

**执行前通知 SOC**，提供演练名称、时间窗口和源主机。

■

在 EDR 控制台中，为 Crucible 二进制文件添加基于哈希或路径的排除项。

■

**不要排除 `powershell.exe` 或 `cmd.exe`**——它们应继续受到监控；演练的目的就是验证对其所执行战术、技术与程序（TTP）的检测能力。

■

代理 PID 和进程名 `CrucibleRunner.exe` 会出现在 EDR 遥测中。

■

演练结束后，移除所有排除项，再次运行演练，验证检测覆盖情况。

防火墙

在 Mythic 回连模式下，目标终端需要能够向 C2 服务器发起出站连接：

■

出站：TCP 连接至 `<callback_host>:<callback_port>`，默认使用 HTTP 端口 80。

■

无需开放入站端口——所有连接均由代理主动发起。

日志输出目录

代理会将 JSON 日志、HTML 报告和 Markdown 报告写入配置的 `log_path`。请确保目录已经存在，或代理有权限创建该目录。

```
mkdir C:\PurpleTeam
```

Mythic 服务端要求

| 要求 | 说明 |
| --- | --- |
| Mythic 版本 | 3.x，已在 3.4 上测试 |
| C2 配置文件 | `http` 配置文件必须处于运行状态 |
| 容器 | Crucible 容器镜像约 2.2 GB，包含 .NET 9 SDK、Python 3、STIX 数据和 Atomic Red Team 仓库 |
| 转换器 | `CrucibleTranslator` 在同一容器内运行，采用 JSON 透传 |

功能特性

■

**操作员控制执行**：Mythic C2 回连代理，由操作员控制演练启动。

■

**接入 Atomic Red Team YAML**：支持输入参数解析与测试选择。

■

**多种输入方式**：技术 ID 列表、ATT&CK Navigator 图层、威胁组织名称（STIX），或演练 YAML。

■

**编译为自包含二进制文件**：基于 .NET 9 单文件发布，支持 Windows `.exe` 或 Linux，目标端零依赖。

■

**按攻击链顺序执行**：按战术阶段对技术分组并排序。

■

**逐项实时回传**：每项技术的结果以结构化 JSON 提交至 Mythic。

■

**浏览器脚本展示结果**：在 Mythic 界面中以颜色区分通过、失败、跳过和超时状态。

■

**可配置延迟与随机抖动**：使执行节奏更贴近实际。

■

**多种清理模式**：自动清理、手动清理（延后至演练结束），或跳过清理。

■

**试运行模式（dry-run）**：记录所有命令，但不实际执行。

■

**逐项控制与范围筛选**：单独启用或禁用技术，并按演练范围筛选阶段。

■

**技术依赖图**：通过 `depends_on` 定义技术依赖关系。

■

**JSON Lines 日志**：便于接入 SIEM，写入即刷盘。

■

**实时转发**：支持 UDP syslog 和 HTTP webhook。

■

**自动生成报告**：每次演练自动生成 HTML 和 Markdown 报告。

■

**结果对比**：通过 `crucible compare` 比较两次运行结果，查看检测差异。

■

**8 个预置演练模板**：包括 APT29、Lazarus、FIN7、勒索软件、凭据访问和发现类场景。

■

**安全控制**：执行提示横幅、中止并清理、权限提升检查。

Mythic 命令

| 命令 | 说明 |
| --- | --- |
| `run_campaign` | 执行内嵌演练；浏览器脚本将结果渲染为表格 |
| `campaign_status` | 查询当前阶段、技术索引和测试数量 |
| `abort` | 立即中止执行；停止前运行尚未完成的清理操作 |
| `skip_technique` | 跳过当前或下一项技术 |
| `get_log` | 从目标终端获取 JSON 执行日志 |

演练模板

`campaigns/` 中提供 **14 个开箱即用的模板**。

威胁组织模拟

| 模板 | 说明 |
| --- | --- |
| APT29 — Cozy Bear | 俄罗斯对外情报局（SVR）：PowerShell、计划任务、凭据转储、WMI 发现 |
| FIN7 — Carbanak | 金融行业：多语言脚本、屏幕截图、数据暂存 |
| Lazarus Group | 朝鲜国家支持的组织：进程发现、防御规避、时间戳篡改 |

场景型演练

| 模板 | 说明 |
| --- | --- |
| 勒索软件模拟（Ransomware Simulation） | 覆盖至影响阶段的通用勒索软件攻击链；影响类技术默认禁用 |
| 发现与侦察（Discovery Recon） | 包含 12 项技术的安全只读侦察扫描 |
| 凭据访问（Credential Access） | LSASS、SAM、NTDS、Kerberoasting、密码喷洒；转储操作默认禁用 |

2025—2026 年威胁趋势演练

| 模板 | 趋势来源 | 说明 |
| --- | --- | --- |
| 2026 勒索软件敲诈（Ransomware Extortion 2026） | Qilin/Akira、阻止恢复、数据外传量增长 275% | 包含 24 项技术的完整攻击链：侦察、凭据访问、横向移动、数据暂存、数据外传、阻止恢复 |
| 2026 AiTM 身份窃取（Identity Theft AiTM 2026） | AiTM 绕过、33 亿枚被盗令牌、OAuth 滥用 | 包含 12 项技术的会话与令牌窃取链 |
| LOTL 隐蔽链（LOTL Stealth Chain） | 56% 的渗透测试使用 WinRM，LOTL 占据主导地位 | 包含 18 项技术，全部使用系统原生二进制程序，不投放任何工具 |
| 供应链失陷后活动（Supply Chain Post-Compromise） | npm 翻倍、SaaS 令牌滥用、2,865 万条秘密信息 | 包含 22 项技术：取得立足点后的侦察、令牌收集、数据外传 |
| 快速突破：29 分钟（Rapid Breakout (29min)） | CrowdStrike 所述突破时间减半至 29 分钟 | 包含 13 项技术的速度测试，延迟设为 5 秒，用于验证 SOC 响应 |
| ICS/OT 初始访问（ICS/OT Initial Access） | 119 个组织、3,300 多家 OT 机构成为目标 | 包含 28 项技术，开展 IT 侧侦察及面向 OT 网段的横向移动 |

完整的结构定义参考见 `CAMPAIGN_SCHEMA.md`。

许可证

采用 BSD 2-Clause 许可证，详情见 `LICENSE`。

作者

Whispergate — @Lavender-exe

---

项目结构与 info 索引

以下依据附件中的仓库页面整理；目录仅展开附件可见层级，统计值及相对时间均为附件快照信息。

仓库目录树

```
Whispergate/Crucible
├── C2_Profiles/
│   └── 提交说明：新增 Windows 支持 · 昨天
├── Payload_Type/
│   └── 提交说明：新增 Linux 支持，已在 Kali 26 上测试 · 昨天
├── documentation-c2/
│   └── 提交说明：新增 Windows 支持 · 昨天
├── documentation-payload/
│   └── 提交说明：新增 Windows 支持 · 昨天
├── documentation-wrapper/
│   └── 提交说明：新增 Windows 支持 · 昨天
├── .gitignore
│   └── 提交说明：新增 Windows 支持 · 昨天
├── LICENSE
│   └── 提交说明：初始提交 · 昨天
├── README.md
│   └── 提交说明：更新 README.md · 昨天
└── config.json
    └── 提交说明：新增 Windows 支持 · 昨天
```

项目 info

```
Crucible / info
├── 项目定位：对手模拟 Mythic 代理
├── 所有者：Whispergate
├── 仓库名称：Crucible
├── 可见性：公开
├── 作者：Whispergate — @Lavender-exe
├── 最近提交
│   ├── 提交者：Lavender-exe
│   ├── 提交说明：更新 README.md
│   ├── 提交标识：4631ffe
│   └── 页面显示时间：昨天
├── 许可证：BSD-2-Clause
├── Stars：26
├── Watchers：0
├── Forks：3
├── 发布版本：尚未发布
├── 软件包：尚未发布
├── 贡献者：1
│   └── @Lavender-exe · 显示名称：Lav
└── 语言占比
    ├── Python：59%
    ├── C#：38.7%
    ├── JavaScript：1.7%
    └── Dockerfile：0.6%
```

文章内容与结果索引

```
Crucible / 内容索引
├── 项目介绍
│   ├── Atomic Red Team YAML → 自包含 .NET 9 可执行文件
│   └── Windows / Linux
├── 运行方式
│   ├── Mythic 模式：回连 → 等待指令 → 执行 → 继续接收任务
│   └── 独立模式：立即执行 → 输出结果 → 退出
├── 环境准备
│   ├── 目标终端要求
│   ├── Windows / Linux 终端准备
│   ├── EDR 注意事项
│   ├── 防火墙与日志目录
│   └── Mythic 服务端要求
├── 功能与控制
│   ├── 多种输入方式、参数解析与测试选择
│   ├── 攻击链排序、依赖关系与阶段筛选
│   ├── 延迟、随机抖动、试运行与清理
│   └── run_campaign / campaign_status / abort / skip_technique / get_log
├── 演练模板
│   ├── 威胁组织模拟
│   ├── 场景型演练
│   └── 2025—2026 年威胁趋势演练
├── 结果输出
│   ├── Mythic：每项技术的结构化 JSON 结果
│   ├── 界面表格：通过 / 失败 / 跳过 / 超时
│   ├── 目标磁盘：JSON 日志 / HTML 报告 / Markdown 报告
│   ├── 实时转发：UDP syslog / HTTP webhook
│   └── 两次运行结果对比：crucible compare
└── 参考入口
    ├── campaigns/：原文提及的模板目录，附件未展开其位置与内容
    ├── CAMPAIGN_SCHEMA.md：原文提及的结构定义参考
    ...