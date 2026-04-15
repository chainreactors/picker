---
title: RedTeam-Agent：让 AI 直接化身黑客的自动化红队框架来了
url: https://mp.weixin.qq.com/s/_1mJ2iFi7OE1S6UiDnn6Hw
source: Doonsec's feed
date: 2026-04-14
fetch_date: 2026-04-15T04:40:52.861765
---

# RedTeam-Agent：让 AI 直接化身黑客的自动化红队框架来了

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4T1PVwJicwkicqDehKTJIaXIh3ia1bSLgouab6QkNbibVxfURQUjbdBQayCyYhNPhmkcpsdXXZibaxlV83wzIETicaSahz0ribiaTdKOrb5Ho5lKXhM/0?wx_fmt=jpeg)

# RedTeam-Agent：让 AI 直接化身黑客的自动化红队框架来了

原创

ktol1
ktol1

泷羽Sec-Norsea

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以前做渗透，最累人的不是想攻击思路，而是反复敲命令、切工具、看输出、拼结果。

现在，有一个工具能让你把这些繁琐执行工作直接甩给 AI —— 你只需要给出目标和最终需求，它会自主完成信息收集、漏洞扫描、内网穿透、域渗透、权限提升等全流程。

## 🎯 项目简介

RedTeam-Agent 是一个采用 **Skill-first 终端工作流** 的 AI 红队渗透测试框架。AI 读取项目 Skill 后，会自动识别工具并 能够自主执行内网渗透测试、活动目录攻击、漏洞利用等红队任务。

> ❝
>
> **核心理念**：无需手动操作，AI 接管所有渗透工具，让安全测试真正自动化。

### ✨ 核心特性

| 特性 | 说明 |
| --- | --- |
| 🚀 **开箱即用** | 15+ 渗透工具自动安装，Windows 一键部署 |
| 🤖 **AI 驱动** | 通过 Skill + 终端，AI 直接调用渗透工具 |
| 💰 **Token 优化** | 智能输出压缩，节省 80% Token 消耗 |
| 🛡️ **域渗透完整** | BloodHound + impacket + Responder 全链路 |
| 🌐 **多客户端支持** | Cursor、Claude Desktop、VS Code Cline |

---

## 🛠️ 工具矩阵

### 网络扫描

| 工具 | 功能 | 场景 |
| --- | --- | --- |
| gogo | 极速资产发现 | 内网主机探测 |
| fscan | 综合扫描 | 端口/漏洞/弱口令 |

### Web 安全

| 工具 | 功能 | 场景 |
| --- | --- | --- |
| httpx | Web 指纹识别 | 网站技术栈识别 |
| nuclei | POC 批量扫描 | 已知漏洞检测 |
| ffuf | 目录 fuzzing | Web 目录爆破 |

### 活动目录攻击 🏆

| 工具 | 功能 | 场景 |
| --- | --- | --- |
| SharpHound | Windows 收集器 | 域内数据采集 |
| bloodhound-python | 跨平台收集器 | Linux/macOS 数据采集 |
| GetNPUsers | AS-REP Roast | 枚举不需要预认证的用户 |
| GetUserSPNs | Kerberoasting | 请求 SPN 票据破解 |
| secretsdump | LSASS Dump | 提取明文和哈希 |
| ntlmrelayx | NTLM Relay | 中继攻击 |
| pywerview | 域信息枚举 | 用户/计算机/组 |
| ldapdomaindump | LDAP 转储 | 域信息快照 |

### 横向移动

| 工具 | 功能 | 场景 |
| --- | --- | --- |
| nxc | NetExec | SMB/WinRM/SSH |
| wmiexec | WMI 执行 | 无文件横向 |
| psexec | PSEXEC | 服务执行 |

### 代理与凭据

| 工具 | 功能 | 场景 |
| --- | --- | --- |
| chisel | HTTP 隧道 | 端口转发 |
| responder | LLMNR 欺骗 | 哈希收集 |

---

## 🚀 快速开始

### 1. 环境要求

```
Python 3.8+
Windows 10/11 或 Linux/macOS
8GB+ RAM (推荐)
```

### 2. 安装部署

```
# 克隆仓库
git clone https://github.com/ktol1/RedTeam-Agent.git
cd RedTeam-Agent

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# Linux/macOS
source venv/bin/activate

# 下载二进制工具 (自动下载 gogo, fscan, httpx, nuclei 等)
python scripts/install_tools.py
```

### 3. 启用 Skills 终端模式

无需额外服务端配置。只需要：

```
# 进入仓库根目录（确保 .github/skills/redteam/SKILL.md 可见）
cd RedTeam-Agent

# 确认工具目录存在
dir .\tools
```

AI 会根仓库内的 Skill 与 `copilot-instructions.md`，直接在终端执行命令并读取输出。

### 4. 开始使用

对 AI 说：

```
🎯 先加载 redteam skill，然后用终端扫描 192.168.1.0/24，输出写入 scan.txt 并总结高价值结果

🎯 扫描 192.168.1.0/24 网段，发现所有 Windows 主机并识别开放服务

🎯 使用 SharpHound 收集 corp.local 域信息，分析攻击路径

🎯 在 192.168.1.100 上搭建 chisel 代理，访问 10.10.10.0/24 网段

🎯 对 192.168.1.50 执行 Kerberoasting 攻击
```

---

## 📊 系统架构（Skills + Terminal）

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│    ██████╗ ██████╗ ███████╗███╗   ███╗███████╗ ██████╗ ██╗    │
│    ██╔══██╗██╔══██╗██╔════╝████╗ ████║██╔════╝██╔═══██╗██║    │
│    ██████╔╝██████╔╝███████╗██╔████╔██║█████╗  ██║   ██║██║    │
│    ██╔═══╝ ██╔══██╗╚════██║██║╚██╔╝██║██╔══╝  ██║   ██║╚═╝    │
│    ██║     ██║  ██║███████║██║ ╚═╝ ██║███████╗╚██████╔╝██╗    │
│    ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═╝    │
│                                                                 │
│                 Skill-first Terminal Execution                   │
│                                                                 │
└─────────────────────────────┬───────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
              ▼               ▼               ▼
       ┌──────────┐   ┌──────────┐   ┌──────────┐
       │  Cursor   │   │  Claude  │   │  Cline   │
       │    IDE    │   │  Desktop │   │ (VS Code)│
       └──────────┘   └──────────┘   └──────────┘
              │               │               │
              └───────────────┼───────────────┘
                              │
              ┌───────────────┴───────────────┐
              │                               │
              ▼                               ▼
    ┌─────────────────────────────────────────────────────────────┐
    │                    Skill Layer                              │
    │                                                             │
    │  .github/copilot-instructions.md                            │
    │  .github/skills/redteam/SKILL.md                            │
    │                                                             │
    │  约束: 非交互命令 / 长输出写文件 / 只提取高价值结果          │
    └─────────────────────────────────────────────────────────────┘
              │
              ▼
    ┌─────────────────────────────────────────────────────────────┐
    │                     Tool Layer                              │
    │  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐  │
    │  │  gogo  │ │  fscan  │ │  httpx  │ │ nuclei  │ │ Sharp  │  │
    │  └────────┘ └────────┘ └────────┘ └────────┘ │Hound.exe│  │
    │  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ └────────┘  │
    │  │ nxc    │ │ chisel  │ │impacket │ │responder│            │
    │  └────────┘ └────────┘ └────────┘ └────────┘               │
    └─────────────────────────────────────────────────────────────┘
```

---

## 🎯 AD 攻击链路

```
     ┌─────────────────────────────────────────────────────────────────┐
     │                      攻击阶段流程图                              │
     └─────────────────────────────────────────────────────────────────┘

  ┌───────────────┐      ┌───────────────┐      ┌───────────────┐
  │    侦察阶段    │ ───► │    收集阶段    │ ───► │    分析阶段    │
  └───────────────┘      └───────────────┘      └───────┬───────┘
         │                                               │
         ▼                                               ▼
  ┌───────────────┐                            ┌───────────────┐
  │ gogo/fscan    │                            │ BloodHound GUI│
  │ kerbrute      │                            │ attack_paths  │
  │ pywerview     │                            │ analysis.py  │
  └───────────────┘                            └───────────────┘
                                                        │
  ┌───────────────┐      ┌───────────────┐            │
  │    攻击阶段    │ ◄─── │    移动阶段    │ ◄─────────┘
  └───────────────┘      └───────────────┘
         │                       │
         ▼                       ▼
  ┌───────────────┐      ┌───────────────┐
  │ Kerberoast    │      │ nxc smb       │
  │ AS-REP Roast  │      │ wmiexec       │
  │ secretsdump   │      │ psexec        │
  │ ntlmrelayx    │      │ getST         │
  └───────────────┘      └───────────────┘
```

---

## 📦 终端命令清单（Skill 调用）

| # | 工具名称 | 功能 | 核心命令 |
| --- | --- | --- | --- |
| 1 | `gogo` | 极速资产探针 | `gogo -t 100 -l hosts.txt -q -f gogo.txt` |
| 2 | `fscan` | 内网综合扫描 | `fscan -h 192.168.1.0/24 -np -silent -nocolor -o fscan.txt` |
| 3 | `httpx` | Web 指纹探测 | `httpx -l urls.txt -sc -title -server -td -silent -o httpx.txt` |
| 4 | `nuclei` | 漏洞 POC 扫描 | `nuclei -l urls.txt -tags cve,rce -s high,critical -nc -o nuclei.txt` |
| 5 | `ffuf` | 目录 fuzzing | `ffuf -u http://target/FUZZ -w wordlist.txt -mc 200,301,302 -s -o ffuf.txt` |
| 6 | `nxc` | 内网横向渗透 | `nxc smb 192.168.1.0/24 -u user -p pass --shares` |
| 7 | `kerbrute` | Kerberos 用户枚举 | `kerbrute userenum -d corp.local --dc 192.168.1.10 users.txt -o valid_users.txt` |
| 8 | `SharpHound` | BloodHound 数据采集 | `SharpHound.exe -c Default -d corp.local` |
| 9 | `pywerview` | 域信息枚举 | `pywerview.py get-domain-user -d corp.local --dc-ip 192.168.1.10 -u user -p pass` |
| 10 | `ldapdomaindump` | LDAP 信息转储 | `ldapdomaindump ldap://192.168.1.10 -u 'corp\\user' -p 'password' -o .\\ldapdump` |
| 11 | `responder` | LLMNR 欺骗 | `responder -I eth0 -v` |
| 12 | `wmiexec` | WMI 执行 | `impacket-wmiexec domain/user:pass@target 'whoami'` |
| 13 | `psexec` | PSEXEC | `impacket-psexec domain/user:pass@target cmd.exe` |
| 14 | `secretsdump` | LSASS Dump | `impacket...