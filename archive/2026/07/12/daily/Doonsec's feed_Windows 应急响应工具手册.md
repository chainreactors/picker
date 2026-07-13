---
title: Windows 应急响应工具手册
url: https://mp.weixin.qq.com/s/FrLWdb5UjJ27mX05Noqa4w
source: Doonsec's feed
date: 2026-07-12
fetch_date: 2026-07-13T05:26:05.309528
---

# Windows 应急响应工具手册

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/txlz6HT4tF0pGSIOhdsQkuHyRa1mpDaP2rzn4GT1U7icEzkg8lvZ36Stdjibs2WBL5GWzEKqBic5XBGqFciaicO1DfFpCib0TCUwz3ibwDW5HYHodo/0?wx_fmt=jpeg)

# Windows 应急响应工具手册

原创

灰帽大于
灰帽大于

灰帽大于

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 前言：应急响应工具的重要性

在安全事件发生后，快速、准确地获取现场信息是应急响应的关键。Windows 系统作为企业最常见的操作系统，掌握其应急响应工具体系至关重要。

**应急响应核心目标：**

•🔍 **发现异常** - 识别入侵痕迹和异常行为•📊 **保留证据** - 收集日志、内存、文件等关键证据•🛡️ **控制影响** - 阻止威胁扩散，保护关键资产•🔎 **追溯溯源** - 分析攻击路径，定位攻击来源

---

## 第一章：工具分类总览

### 1.1 工具分类体系

Windows 应急响应工具按功能可分为以下几大类：

```
Windows 应急响应工具体系│├─ 📊 进程与行为分析│   ├─ Process Monitor│   ├─ Process Explorer│   ├─ Autoruns│   └─ ProcDump│├─ 🌐 网络分析│   ├─ Wireshark│   ├─ TCPView│   └─ 内置命令（netstat）│├─ 📁 文件分析│   ├─ VirusTotal│   ├─ Strings│   └─ Sigcheck│├─ 💾 内存取证│   ├─ Volatility│   ├─ DumpIt│   └─ WinPMEM│├─ 📝 日志分析│   ├─ Event Log Explorer│   ├─ LogParser│   └─ WELA│├─ 🔗 持久化检测│   ├─ Autoruns│   ├─ RegRipper│   └─ Persistence Ripper│├─ 🔬 恶意代码分析│   ├─ IDA Pro / Ghidra│   ├─ x64dbg│   └─ YARA│├─ 🧠 威胁情报│   ├─ 微步在线│   ├─ VirusTotal│   └─ MalwareBazaar│└─ 🎯 综合响应平台    ├─ Velociraptor    ├─ KAPE    ├─ Eric Zimmerman工具集    └─ CyLR
```

---

### 1.2 工具获取渠道

**官方与可信来源：**

| 来源 | 链接 | 说明 |
| --- | --- | --- |
| Sysinternals | https://learn.microsoft.com/sysinternals[1] | Microsoft官方工具集 |
| GitHub | https://github.com[2] | 开源工具主站 |
| VirusTotal | https://www.virustotal.com[3] | 在线恶意检测 |
| 微步在线 | https://x.threatbook.cn[4] | 国内威胁情报 |
| Eric Zimmerman | https://ericzimmerman.github.io[5] | Windows取证工具集 |

⚠️ **安全提示**：所有工具必须从官方渠道下载，避免使用来源不明的工具。

---

## 第二章：Sysinternals 工具集详解

Sysinternals 是 Microsoft 官方的 Windows 高级工具集，是应急响应的**必备工具包**。

### 2.1 Process Monitor（实时行为监控）

**功能**：实时监控文件系统、注册表、进程/线程活动

**下载地址**：https://learn.microsoft.com/sysinternals/downloads/processmonitor[6]

**核心用途**：

•🔍 恶意软件行为分析•🛠️ 软件问题排查•🔐 权限问题诊断•📊 应用程序行为审计

**常用命令行启动方式**：

```
# 后台监控并保存日志procmon.exe /Minimized /Capture /BackingFile C:\Logs\capture.pml
# 加载配置文件启动procmon.exe /LoadConfig filter.pmc /Capture
# 静默模式procmon.exe /Quiet /AcceptEula /Capture
```

**关键过滤条件**：

```
# 指定进程监控Process Name is malware.exe → Include
# 失败操作监控（权限问题）Result is ACCESS DENIED → Include
# 注册表监控Path begins with HKLM\Software → Include
# 文件写入监控Operation contains Write → Include
```

---

### 2.2 Process Explorer（进程分析）

**功能**：进程树、DLL、句柄、网络连接分析

**下载地址**：https://learn.microsoft.com/sysinternals/downloads/processexplorer[7]

**核心用途**：

•📊 查看进程父子关系•🔍 查看进程加载的DLL•📌 检测DLL注入•🌐 查看进程网络连接

**关键功能**：

| 功能 | 用途 |
| --- | --- |
| Process Tree | 进程父子关系追踪 |
| DLL View | DLL加载检测 |
| Handles View | 句柄分析 |
| Properties | 进程详细信息 |
| VirusTotal Check | 快速恶意检测 |

**与 Procmon 配合使用**：

```
Process Explorer → 找到可疑进程Process Monitor → 过滤该PID，分析行为
```

---

### 2.3 Autoruns（自启动项分析）

**功能**：全面扫描 Windows 所有自启动位置

**下载地址**：https://learn.microsoft.com/sysinternals/downloads/autoruns[8]

**核心用途**：

•🔍 检测恶意持久化项目•📊 审计合法启动项•🛡️ 发现隐藏的启动项

**扫描位置（超过50个）**：

```
启动项位置├─ 注册表│   ├─ HKLM\Software\Microsoft\Windows\CurrentVersion\Run│   ├─ HKCU\Software\Microsoft\Windows\CurrentVersion\Run│   ├─ HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce│   ├─ HKLM\System\CurrentControlSet\Services│   └─ WMI事件订阅│├─ 文件系统│   ├─ Startup文件夹（用户/公用）│   ├─ C:\Windows\Tasks│   ├─ C:\Windows\System32\Tasks│   └─ 浏览器扩展│├─ 其他│   ├─ 计划任务│   ├─ 服务│   ├─ 驱动│   ├─ Boot Execute│   ├─ Image File Execution Options│   └─ AppInit DLLs
```

**使用要点**：

```
# 以管理员身份运行autoruns.exe -a
# 验证文件签名View → Verify Code Signatures
# 隐藏合法Microsoft条目Options → Hide Microsoft Entries
# VirusTotal检测右键条目 → Check VirusTotal
```

---

### 2.4 ProcDump（进程内存dump）

**功能**：捕获进程内存dump

**下载地址**：https://learn.microsoft.com/sysinternals/downloads/procdump[9]

**核心用途**：

•💾 捕获崩溃进程内存•🔍 恶意进程内存分析•📊 应用程序问题诊断

**常用命令**：

```
# 按PID dumpprocdump.exe -ma 1234 output.dmp
# 按进程名dumpprocdump.exe -ma malware.exe output.dmp
# CPU异常时dump（CPU超过80%触发）procdump.exe -ma -c 80 malware.exe output.dmp
# 持续dump（每5秒一次）procdump.exe -ma -s 5 malware.exe output.dmp
```

---

### 2.5 TCPView（网络连接监控）

**功能**：实时监控TCP/UDP连接

**下载地址**：https://learn.microsoft.com/sysinternals/downloads/tcpview[10]

**核心用途**：

•🌐 实时查看网络连接•🔍 查看连接对应的进程•📊 监控异常网络活动

**关键信息**：

| 列 | 说明 |
| --- | --- |
| Process | 进程名 |
| PID | 进程ID |
| Protocol | TCP/UDP |
| Local Address | 本地地址端口 |
| Remote Address | 远程地址端口 |
| State | 连接状态 |

---

### 2.6 Strings（字符串提取）

**功能**：从文件中提取可打印字符串

**下载地址**：https://learn.microsoft.com/sysinternals/downloads/strings[11]

**核心用途**：

•🔍 从恶意文件提取关键信息•📌 发现隐藏的URL、IP、命令•📊 分析未知文件类型

**常用命令**：

```
# 提取所有字符串（默认4字符以上）strings.exe malware.exe
# 指定最小字符长度strings.exe -n 8 malware.exe
# 输出到文件strings.exe -n 8 malware.exe > strings_output.txt
# 提取Unicode字符串strings.exe -u malware.exe
```

---

### 2.7 Sigcheck（文件签名验证）

**功能**：验证文件数字签名，查询VirusTotal

**下载地址**：https://learn.microsoft.com/sysinternals/downloads/sigcheck[12]

**核心用途**：

•🔐 验证文件是否被篡改•🔍 检测恶意文件签名状态•📊 批量文件签名检查

**常用命令**：

```
# 检查单个文件签名sigcheck.exe malware.exe
# VirusTotal检测sigcheck.exe -vt malware.exe
# 批量检查目录sigcheck.exe -vt -s C:\Windows\System32
# 查找未签名文件sigcheck.exe -u C:\Program Files
```

---

## 第三章：网络分析工具

### 3.1 Wireshark（流量抓包分析）

**功能**：网络流量捕获与分析

**下载地址**：https://www.wireshark.org/download.html[13]

**核心用途**：

•🌐 抓取网络流量•🔍 分析恶意通信内容•📊 解密协议通信

**应急响应场景**：

```
场景一：分析恶意软件通信1. 抓取流量：Capture → Start2. 过滤IP：ip.addr == malicious_ip3. 分析内容：右键 → Follow TCP Stream4. 提取恶意数据
场景二：分析C2通信1. 过滤端口：tcp.port == 44442. 查看通信模式3. 分析心跳包特征
场景三：DNS异常分析1. 过滤DNS：dns2. 查看查询域名3. 检测DNS隧道
```

**常用过滤规则**：

```
# 按IP过滤ip.addr == 192.168.1.100
# 按端口过滤tcp.port == 443
# 按协议过滤http || dns || ftp
# 按进程过滤（需配合其他工具）# 通过TCPView找到PID和端口，Wireshark过滤端口
```

---

### 3.2 内置网络命令

**netstat**：网络连接状态

```
# 显示所有连接netstat -ano
# 只显示已建立连接netstat -ano | findstr ESTABLISHED
# 显示监听端口netstat -ano | findstr LISTENING
# 查看特定端口netstat -ano | findstr :443
# 持续刷新显示netstat -ano 1
```

**关键信息解读**：

```
Proto  Local Address      Foreign Address     State       PIDTCP    0.0.0.0:443        192.168.1.1:80      ESTABLISHED 1234│      │                  │                   │           ││      本地端口           远程地址端口         连接状态    进程ID
```

---

## 第四章：文件分析工具

### 4.1 VirusTotal（多引擎恶意检测）

**功能**：使用数十个杀毒引擎检测文件

**网址**：https://www.virustotal.com[14]

**核心用途**：

•🔍 快速检测恶意文件•📊 查看文件基本信息（Hash、签名）•📌 查看文件行为报告•🌐 检测URL、IP、域名

**使用方式**：

| 方式 | 说明 |
| --- | --- |
| 上传文件 | 上传可疑文件检测 |
| 输入Hash | 搜索已检测的样本 |
| 输入URL | 检测恶意链接 |
| 输入IP | 检测恶意IP |

**检测结果解读**：

```
Detection: 15/70│          ││          15个引擎报毒 / 70个总引擎数│判定标准：  0/70 → 安全  1-3/70 → 可能误报，需人工确认  4+/70 → 确认恶意
```

---

### 4.2 PE-bear（PE文件结构分析）

**功能**：PE文件（exe、dll）结构可视化分析

**下载地址**：https://github.com/hasherezade/pe-bear-releases[15]

**核心用途**：

•🔍 查看PE文件结构•📌 分析导入/导出表•📊 检测PE异常（注入、加壳）

**关键PE结构**：

```
PE文件结构├─ DOS Header├─ PE Header│   ├─ Signature│   ├─ File Header│   └─ Optional Header├─ Section Headers│   ├─ .text（代码段）│   ├─ .data（数据段）│   ├─ .rdata（只读数据）│   └─ .rsrc（资源）├─ Import Table（导入函数）├─ Export Table（导出函数）└─ Resource Section（资源）
```

---

### 4.3 Hash计算工具

**内置命令计算Hash**：

```
# CertUtil计算MD5certutil -hashfile malware.exe MD5
# CertUtil计算SHA1certutil -hashfile malware.exe SHA1
# CertUtil计算SHA256certutil -hashfile malware.exe SHA256
# PowerShell计算HashGet-FileHash malware.exe -Algorithm SHA256
```

---

## 第五章：内存取证工具

### 5.1 Volatility（内存分析框架）

**功能**：分析内存dump文件，提取关键信息

**下载地址**：https://github.com/volatilityfoundation/volatility[16]

**核心用途**：

•💾 提取进程、网络连接•🔍 检测恶意代码、DLL注入•📊 分析注册表、密码哈希•🦠 发现隐藏进程、Rootkit

**关键命令**：

```
# 查看进程列表volatility -f memory.dmp --profile=Win10x64_19041 pslist
# 查看进程树volatility -f memory.dmp --profile=Win10x64_19041 pstree
# 查看网络连接volatility -f memory.dmp --profile=Win10x64_19041 netscan
# 查看DLL加载volatility -f memory.dmp --profile=Win10x64_19041 dlllist
# 查看命令行历史volatility -f memory.dmp --profile=Win10x64_19041 cmdscan
# 查看注册表volatility -f memory.dmp --profile=Win10x64_19041 hivelist
# 查看密码哈希volatility -f memory.dmp --profile=Win10x64_19041 hashdump
# 检测恶意代码volatility -f memory.dmp --profile=Win10x64_19041 malfind
# 检测隐藏进程volatility -f memory.dmp --profile=Win10x64_19041 psxview
`...