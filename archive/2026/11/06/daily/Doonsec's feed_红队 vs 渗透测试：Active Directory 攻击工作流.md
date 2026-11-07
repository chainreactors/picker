---
title: 红队 vs 渗透测试：Active Directory 攻击工作流
url: https://mp.weixin.qq.com/s/1dPLy-rh_bx7uTqB-XiaLg
source: Doonsec's feed
date: 2026-11-06
fetch_date: 2026-11-07T07:56:11.321685
---

# 红队 vs 渗透测试：Active Directory 攻击工作流

# 红队 vs 渗透测试：Active Directory 攻击工作流

网安之家-CyberHomestead

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 红队 vs 渗透测试：Active Directory 攻击工作流

> **同一条攻击链，打了两次。**一次从 Kali 打进来，一次从域内机器打进来。 结局一样——域控沦陷。 但你的 SIEM 只抓到了 4 条告警。

---

## 📌 导读：这篇文章到底讲了什么

同样一套 AD 攻击链，在同一个实验环境里跑了两遍：一遍是传统渗透测试（从 Kali 机器外部打），一遍是红队 C2（从已经拿下的一台域成员服务器内部打）。**两条路径都完成了从域成员服务器 → 子域 DC → 父域 DC 的完整域接管。**

但检测结果**天差地别**。

本文逐节对照每一条攻击技术的**渗透测试命令、C2 等价命令、OPSEC（行动安全）差异、以及对应的 Elastic 检测查询**。技术、检测查询与 OPSEC 分析适用于任意 Active Directory 环境。**GOAD-Light 只是演示用的靶场，不是本文的主题。**

> 全文所有 C2 命令均在一个活跃的 **Adaptix C2 Kharon agent** 会话中执行。 所有 Elastic 查询均在 Kibana Discover 或 KQL 输入栏中执行。
>
> 引用的 Extension-Kit BOF 模块：`AD-BOF`、`Creds-BOF`、`Elevation-BOF`、`Execution-BOF`、`Injection-BOF`、`LateralMovement-BOF`、`SAL-BOF`、`SAR-BOF`、`Process-BOF`、`Postex-BOF`、`Kerbeus-BOF`

---

## 🌳 项目成果树 / 全文章节索引

```
AD-ATTACK-WORKFLOW/
│
├── 【实验环境】Lab Environment
│   ├── 靶场：GOAD-Light（多域 AD + 故意配置缺陷）
│   ├── SIEM/EDR：Elastic Security（10.1.20.2）
│   └── C2：Adaptix（10.1.10.50, LXC）+ Kharon agent
│
├── 01 - 初始立足点 (Initial Foothold)
│   ├── 1.1 起点：castelblack 上的 samwell.tarly（低权限）
│   └── 1.2 Agent 配置降噪（sleep/jitter/blockdlls/mask/amsi/syscall/spawnto）
│
├── 02 - 侦察 (Reconnaissance)
│   ├── 2.1 主机发现        nmap -sn        → smartscan BOF
│   ├── 2.2 SMB 用户枚举   nxc --users     → ldapsearch BOF
│   ├── 2.3 共享枚举       nxc --shares    → SOCKS+nxc / net view
│   └── 2.4 BloodHound 采集 bloodhound-python → SharpHound / ldapsearch BOF
│
├── 03 - 凭据访问 (Credential Access)
│   ├── 3.1 AS-REP Roasting   GetNPUsers  → kerbeus asreproasting
│   ├── 3.2 Kerberoasting     GetUserSPNs → kerbeus asktgt + kerberoasting
│   ├── 3.3 LSASS 凭据转储    mimikatz    → nanodump / hashdump / lsadump
│   └── 3.4 DCSync            secretsdump  → dcsync single / lsadump_secrets
│
├── 04 - 权限提升 (Privilege Escalation)
│   ├── 4.1 GPO 滥用          pygpoabuse   → pygpoabuse over SOCKS
│   └── 4.2 本地提权到 SYSTEM  evil-winrm  → getsystem token / potato
│
├── 05 - SQL Server 漏洞利用
│   ├── 5.1 实例发现    nxc mssql       → mssql 1434udp BOF
│   ├── 5.2 服务器信息  mssqlclient.py  → SQLRecon execute-assembly
│   ├── 5.3 当前用户上下文
│   ├── 5.4 模拟枚举    EXECUTE AS LOGIN 链
│   ├── 5.5 数据库与用户枚举 (as sa)
│   ├── 5.6 链接服务器枚举 (as sa)
│   └── 5.7 xp_cmdshell 执行系统命令 (as sa)
│
├── 06 - 横向移动 (Lateral Movement)
│   ├── 6.1 WinRM        evil-winrm → invoke winrm BOF
│   ├── 6.2 PsExec       impacket-psexec → jump psexec BOF / SMB link
│   ├── 6.3 SCShell      smbexec.py → jump scshell BOF（免 7045）
│   └── 6.4 RDP          xfreerdp 直接 → xfreerdp over SOCKS
│
├── 07 - 域提权 (Domain Escalation)
│   ├── 7.1 受限委派滥用  findDelegation → kerbeus s4u (S4U2Self+S4U2Proxy)
│   └── 7.2 ExtraSids / 黄金票据  raiseChild.py → Rubeus golden + kerbeus ptt
│
├── 08 - 后渗透 (Post-Exploitation)
│   ├── 8.1 文件操作       smbclient get → fs ls / fs cat / download
│   ├── 8.2 NETLOGON 脚本发现 smbclient NETLOGON → fs cat
│   └── 8.3 态势感知       whoami/ipconfig/net → SAL-BOF（零子进程）
│
├── 09 - Shellcode 注入（新信标部署）
│   ├── 9.1 CreateRemoteThread  scinject
│   └── 9.2 Extension-Kit 注入 BOF  inject-sec / inject-cfg / inject-poolparty
│
├── 10 - 检测覆盖度总结 (Detection Coverage Summary)
│   ├── 10.1 各攻击阶段命中的预置规则表
│   ├── 10.2 检测盲区（无预置规则触发）清单
│   └── 10.3 补齐盲区的 5 条自定义规则
│
├── 11 - 完整攻击链映射 (Full Attack Chain Mapping)
│   ├── 11.1 路径 A（20 步完整表）
│   └── 11.2 路径 B（20 步完整表）
│
├── 附录 A - Extension-Kit BOF 速查表
│   ├── AD-BOF / Kerbeus-BOF / Creds-BOF / Execution-BOF
│   ├── Injection-BOF / LateralMovement-BOF / Elevation-BOF
│   └── SAL-BOF / SAR-BOF / Kharon 内置命令
│
├── 附录 B - Elastic 索引模式对照表
└── 附录 C - Sysmon Event ID 速查表
│
└── 【核心结论】Key Findings
    ├── 预置规则触发数：渗透 12+  vs  红队 4
    ├── 零检测技术数：  渗透 2   vs  红队 10
    ├── LSASS 相关告警： 渗透 5+  vs  红队 0
    └── 真正的缺口不是遥测，是规则覆盖度
```

---

## 🎯 关键指标速览（先看结论，再看过程）

| 指标 | 渗透测试（来自 Kali） | 红队 C2（来自域内主机） |
| --- | --- | --- |
| 触发的 Elastic 预置规则数 | **12+** | **4** |
| 完全零检测的技术数量 | **2** （AS-REP Roasting、Kerberoasting） | **10** （见第 10.2 节） |
| LSASS 相关告警 | **5+** 条规则 | **0** （改用 SAM 方案，全程未碰 lsass.exe） |
| 进程创建事件（Event ID 1） | 频繁（cmd、net、whoami） | **接近于零** （BOF 全程进程内执行） |
| 源 IP 异常特征 | 外部 IP 极其扎眼 | 域成员服务器 IP，与正常流量混同 |

---

## 1 - 初始立足点（Initial Foothold）

### 1.1 - 起点（Starting Point）

这套工作流从一个以 `samwell.tarly` 身份运行在 castelblack（SRV02，10.1.10.22）上的 Kharon agent 开始。

活跃 agent 状态：

| 字段 | 值 |
| --- | --- |
| 主机 | castelblack (SRV02) |
| IP | 10.1.10.22 |
| 用户 | NORTH\samwell.tarly |
| 权限 | 低（普通域用户，无本地管理员） |
| Agent | Kharon HTTP |

`samwell.tarly` 是一个没有任何本地管理员权限的普通域用户。**所有的侦察、凭据获取、权限提升和横向移动都从这个低权限立足点开始。** 整个行动从工作站一路打到域控制器，靠的是权限提升与横向移动。

### 1.2 - Agent 配置（Agent Configuration）

**MITRE ATT&CK**：T1562.001（削弱防御：禁用或修改工具）、T1027（混淆文件或信息）、T1134.004（父进程 ID 欺骗）、T1036.005（伪装：匹配合法名称或位置）、T1106（原生 API）

agent 上线之后，先把配置调低以减少暴露面。在 castelblack 的 agent 会话中执行以下命令。

**C2 命令（在 castelblack agent 上执行，每个新 agent 上线时重复一遍）：**

```
config sleep 5000
config jitter 30
config ppid 0
config blockdlls true
config mask.beacon timer
config mask.heap true
config amsi_etw_bypass all
config syscall spoof_indirect
config bof_api_proxy true
config spawnto C:\Windows\System32\RuntimeBroker.exe
```

| 设置项 | 作用 |
| --- | --- |
| `sleep 5000` / `jitter 30` | 回连间隔设为 5 秒，带 30% 随机性。信标间隔实际在 3500ms–6500ms 之间浮动。 |
| `blockdlls true` | 阻止非微软签名的 DLL 在派生的子进程中加载。这会让 EDR 的注入钩子失效。 |
| `mask.beacon timer` | 睡眠期间加密信标内存区域。使用定时器队列回调配合 ROP 链，把内存翻转为 RW，加密，睡眠，解密，再翻回 RX。 |
| `mask.heap true` | 睡眠期间加密堆内存分配。防止内存扫描器找到字符串和配置数据。 |
| `amsi_etw_bypass all` | 在 `execute-assembly` 或 `dotnet` 命令执行前对 AMSI 与 ETW 打补丁。阻止 .NET 遥测触达 Defender 与 Elastic。 |
| `syscall spoof_indirect` | 使用带栈欺骗的间接系统调用。所有 `Nt*` API 调用都通过 ntdll.dll 指令地址发起，并伪造调用栈。 |
| `bof_api_proxy true` | 将 BOF 的 API 调用路由到信标内部代理。这样 BOF 模块同样享有栈欺骗和间接系统调用的能力。 |
| `spawnto RuntimeBroker.exe` | 将 fork-and-run 操作的牺牲进程设为 `RuntimeBroker.exe`。这是一个在用户会话中经常运行的合法 Windows 进程。 |

**Elastic 查询 - 检测信标睡眠混淆：**

无直接检测手段。睡眠混淆属于内存内技术。最佳检测方式是借助 Elastic Defend 行为告警进行内存扫描：

```
event.module:"endpoint" AND event.action:"Memory Threat Detection Alert"
```

---

## 2 - 侦察（从 castelblack 立足点出发）

本节所有枚举都在 castelblack（SRV02）上的低权限 `samwell.tarly` agent 中执行。**这正是与渗透测试路线的关键差异：不是从外部 Kali 主机扫描，而是每一条查询都从一台已加入域的成员服务器发起。** 这些流量与正常的 Active Directory 运维流量混同。这些操作**不需要任何本地管理员权限**。

### 2.1 - 主机发现（Host Discovery）

**MITRE ATT&CK**：T1046（网络服务发现）

**渗透测试命令（来自 Kali）：**

```
nmap -sn -n -v 10.1.10.0/24
```

**C2 命令（来自 castelblack agent）：**

```
smartscan 10.1.10.0/24 -p standart
```

这会运行 SAR-BOF 的 smartscan 模块。它是一个单线程的静默端口扫描器。`-p standart` 模式（注意拼写错误是 BOF 源码里就有的）会扫描约 20 个端口，包括 135、139、445、3389、5985、5986、22、21、25、53。想更窄地扫描，直接指定端口：

```
smartscan 10.1.10.0/24 -p 445
```

**OPSEC 对比：**

| 因素 | 渗透测试（nmap） | 红队（smartscan BOF） |
| --- | --- | --- |
| 流量来源 | 外部（Kali IP） | 内部（SRV02 IP） |
| 协议 | ICMP echo | TCP connect |
| 流量量级 | 256 台主机 × 全部端口 | 256 台主机 × 指定端口 |
| 特征 | nmap user-agent / TTL 异常 | 来自域内主机的一次正常 TCP 连接 |

**Elastic 查询 - 检测内网端口扫描：**

预置规则：

```
rule.name:"Potential Network Scan Executed From Host"
```

自定义高连接量查询（单一源）：

```
event.category:"network" AND destination.port:445 AND source.ip:"10.1.10.22"
```

> smartscan 的输出表明它其实**相对嘈杂**。一个更安静的替代方案：列出 castelblack 的 ARP 表来发现邻居，无需产生网络扫描遥测。
>
> 这样可以完全避免 smartscan 产生的检测信号与遥测。

### 2.2 - SMB 用户枚举（SMB User Enumeration）

**MITRE ATT&CK**：T1087.002（账户发现：域账户）

**渗透测试命令（来自 Kali）：**

```
# 允许匿名认证
nxc smb 10.1.10.11 --users
```

**C2 命令（来自 castelblack agent）：**

以 `samwell.tarly` 身份执行定向的 ldapsearch 查询：

```
ldapsearch (objectClass=user) -a sAMAccountName,description,memberOf,lastLogon
```

这会运行 AD-BOF 的 ldapsearch 模块。**它使用信标当前的令牌上下文发送 LDAP 查询。** 来自域内机器的 LDAP 查询是标准的 Active Directory 流量。

完整语法参考：

```
ldapsearch <query> [-a attributes] [-c count] [-s scope] [--dc dc] [--dn dn] [--ldaps]
```

**OPSEC 对比：**

| 因素 | 渗透测试（nxc --users） | 红队（ldapsearch BOF） |
| --- | --- | --- |
| 协议 | SMB + SAMR RPC | LDAP（389 端口） |
| 认证 | 明文凭据上线 | 当前 Kerberos 令牌 |
| 可见性 | SAMR 枚举被记录 | 标准 LDAP 查询，正常 AD 流量 |
| Sysmon 覆盖 | 针对 samr 的命名管道事件（Event ID 17/18） | LDAP 无 Sysmon 事件 |

**Elastic 查询 - 检测 LDAP 枚举：**

预置规则 —— 该预置规则**只在访问敏感属性**（userPassword、unicodePwd、msDS-ManagedPassword）时触发。`sAMAccountName`、`member...