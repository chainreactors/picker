---
title: GYscan——综合渗透测试工具
url: https://mp.weixin.qq.com/s/ZtRQBPMgJ7LEaep6R8qEiw
source: Doonsec's feed
date: 2026-02-07
fetch_date: 2026-02-08T04:29:38.550176
---

# GYscan——综合渗透测试工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qqiaD4wiajgFzGicT80aNDWicNaR5hGYIXcBMhiceLibv0Aiatc03T5mgicYQhUumFzNUIxcQ4IianTQc6r5E63nH9DV3AzmgXY4ptxfoBcVpO9Qc6lI/0?wx_fmt=jpeg)

# GYscan——综合渗透测试工具

一个人挺好
一个人挺好

一个人挺好 wa

![]()

在小说阅读器中沉浸阅读

# 项目地址：

https://github.com/xiguayiqiu/GYscan

# GYscan 技术文档

## 一、项目概述

**GYscan** 是一款基于 Go 语言开发的现代化内网横向渗透测试工具，专为安全研究人员、渗透测试工程师和红队成员设计。该工具专注于内网横向移动和边界安全测试场景，提供高效、可靠的内网安全评估解决方案。

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFzyXXfqhaLnRCtCr1GmoKR1B9IianMpgI2licdibwCsV1n7aE2G8hiaFxWIefkgMwMTdYibgwPHic5gcZrLlpjianibGWic7H2ABica3c3nE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFwo7wibBksicmZIsGMYUhQjyKy2GwmlPicuTzY3kB3tmVzoo0qjmY30tia6NBI7oOqjpriabnnVKJ9klEwlSOQic4PW3Ql3DQ423jdyA/640?wx_fmt=png&from=appmsg)

### 1.1 基本信息

表格

| 项目属性 | 详情 |
| --- | --- |
| **项目名称** | GYscan |
| **开发语言** | Go 1.18+ |
| **最新版本** | v2.6.0 |
| **支持平台** | Windows 7+ / Linux / macOS / FreeBSD |
| **许可证** | Apache 2.0 |
| **项目地址** | https://github.com/xiguayiqiu/GYscan |

### 1.2 核心功能

* **端口扫描**：支持 TCP/UDP 端口扫描、服务识别和指纹采集
* **网络发现**：主机发现、网段扫描、操作系统识别
* **漏洞检测**：集成多种漏洞检测插件
* **弱口令爆破**：支持 SSH、FTP、数据库等协议的密码破解
* **远程执行**：PowerShell 远程执行、WMI 远程管理、DCOM 操作
* **协议操作**：SMB 共享枚举、RDP 会话管理、LDAP 查询
* **Web 安全**：目录扫描、CSRF/XSS 检测、WAF 识别、WebShell 生成
* **配置审计**：基于 CIS 基准的系统配置安全审计
* **网络包操作**：底层网络包构造和发送（类似 Scapy）

### 1.3 核心优势

1. **专注内网安全**：专门针对内网横向移动和边界安全测试场景优化
2. **功能丰富**：集成 20+ 种渗透测试功能模块
3. **跨平台支持**：原生支持 Windows、Linux、macOS 三大主流操作系统
4. **模块化设计**：采用插件化架构，支持功能扩展和自定义模块开发
5. **高性能**：基于 Go 语言原生并发，具备出色的并发处理能力
6. **易用性强**：提供简洁的命令行界面和详细的帮助文档

---

## 二、系统架构

### 项目结构

```
GYscan/
├── C2/                          # C2 服务器端（命令与控制）
│   ├── Linux/                   # Linux 版本 C2 服务器
│   │   ├── cmd/                 # 命令行入口程序
│   │   ├── internal/            # 内部实现模块
│   │   ├── pkg/                 # 公共包（扫描器、工具等）
│   │   └── tools/               # 集成工具（Lynis、Trivy 等）
│   └── Windows/                 # Windows 版本 C2 服务器
│       ├── cmd/                 # 命令行入口程序
│       ├── internal/            # 内部实现模块
│       ├── pkg/                 # 公共包（审计、扫描器等）
│       └── tools/               # 集成工具（Goss 等）
├── Client/                      # 客户端主程序（渗透测试工具）
│   ├── internal/                # 内部功能模块
│   │   ├── cli/                 # 命令行界面和命令注册
│   │   ├── network/             # 网络扫描和主机发现
│   │   ├── nmap/                # Nmap 集成功能
│   │   ├── powershell/          # PowerShell 远程执行
│   │   ├── smb/                 # SMB 协议操作
│   │   ├── ssh/                 # SSH 密码爆破
│   │   ├── rdp/                 # RDP 远程桌面
│   │   ├── wmi/                 # WMI 远程管理
│   │   ├── dcom/                # DCOM 远程执行
│   │   ├── dirscan/             # 网站目录扫描
│   │   ├── csrf/                # CSRF 漏洞检测
│   │   ├── xss/                 # XSS 漏洞检测
│   │   ├── waf/                 # WAF 检测工具
│   │   ├── webshell/            # WebShell 生成工具
│   │   ├── database/            # 数据库密码破解
│   │   ├── ftp/                 # FTP 密码破解
│   │   ├── ldap/                # LDAP 枚举
│   │   ├── weakpass/            # 弱口令检测框架
│   │   ├── scapy/               # 网络包操作
│   │   ├── reports/             # 报告生成模块
│   │   └── utils/               # 工具函数和辅助方法
│   ├── config/                  # 配置文件目录
│   ├── dirmap/                  # 目录扫描字典文件
│   └── reports/                 # 报告输出目录
├── PSTools/                     # 微软 PSTools 套件
├── build.ps1                    # Windows 构建脚本
└── build_linux.sh               # Linux 构建脚本
```

---

## 三、安装与部署

### 3.1 环境要求

* **操作系统**：Windows 7+ / Linux / macOS
* **Go 版本**：1.18+（编译需要）
* **内存**：至少 512MB 可用内存
* **网络**：稳定的网络连接（扫描功能需要）
* **权限**：部分功能需要 root/Administrator 权限

### 3.2 源码编译安装

#### 3.2.1 获取源码

bash

```
# 从 GitHub 克隆
git clone https://github.com/xiguayiqiu/GYscan.git

# 或从 Gitee 克隆（国内镜像）
git clone https://gitee.com/bzhanyiqiua/GYscan.git

cd GYscan
```

### 3.3 一键构建脚本

**Windows 平台：**

powershell

```
.\build.ps1
```

**Linux 平台：**

bash

```
chmod +x build_linux.sh
./build_linux.sh
```

### 3.4 Linux 依赖安装

不同发行版的依赖安装命令：

**Debian/Ubuntu/Kali：**

bash

```
sudoapt update
sudoaptinstall-y\
    libx11-dev \
    libxcursor-dev \
    libxrandr-dev \
    libxinerama-dev \
    libxi-dev \
    libxxf86vm-dev \
    libgl1-mesa-dev \
    libglu1-mesa-dev \
    mesa-common-dev \
    build-essential \
    pkg-config \
    dbus-x11 \
    libdbus-1-dev \
    libpcap-dev
```

**RedHat/CentOS/Fedora：**

bash

```
sudo yum install-y\
    libX11-devel \
    libXcursor-devel \
    libXrandr-devel \
    libXinerama-devel \
    libXi-devel \
    libXxf86vm-devel \
    mesa-libGL-devel \
    mesa-libGLU-devel \
    gcc-c++ \
    pkgconfig \
    dbus-devel \
    libpcap-devel
```

## 四、使用指南

### 4.1 基础命令

#### 4.1.1 查看版本信息

bash

```
./GYscan.exe --version
```

#### 4.1.2 查看帮助信息

bash

```
./GYscan.exe --help
```

### 4.2 网络扫描功能

#### 4.2.1 端口扫描（scan）

bash

```
# 扫描单个 IP 地址
./GYscan.exe scan --target192.168.1.100

# 扫描 IP 段（CIDR 格式）
./GYscan.exe scan --target192.168.1.0/24

# 扫描指定端口范围
./GYscan.exe scan --target192.168.1.100 --ports80,443,22,21

# 设置并发线程数
./GYscan.exe scan --target192.168.1.0/24 --threads50

# 设置超时时间（秒）
./GYscan.exe scan --target192.168.1.100 --timeout3

# 指定扫描速度等级（1-5，5 最快）
./GYscan.exe scan --target192.168.1.0/24 -T3

# 静默模式（仅输出关键结果）
./GYscan.exe scan --target192.168.1.100 --silent

# 详细输出模式
./GYscan.exe scan --target192.168.1.100 --verbose
```

### 4.3 远程执行功能

#### 4.3.1 PowerShell 远程执行

bash

```
# 执行远程 PowerShell 命令（HTTP 5985 端口）
./GYscan.exe powershell exec\
--target192.168.1.100 \
--user Administrator \
--password"Password123"\
--command"whoami"

# 使用 HTTPS 连接（5986 端口）
./GYscan.exe powershell exec\
--target192.168.1.100 \
--user Administrator \
--password"Password123"\
--command"whoami"\
--https

# 测试 WinRM 端口连通性
./GYscan.exe powershell test\
--target192.168.1.100 \
--port5985
```

### 4.4 弱口令爆破功能

#### 4.4.1 SSH 密码爆破

bash

```
# 对单个目标进行 SSH 爆破
./GYscan.exe ssh brute \
--target192.168.1.100 \
--user root \
--wordlist passwords.txt

# 指定端口
./GYscan.exe ssh brute \
--target192.168.1.100 \
--port2222\
--user admin \
--wordlist passwords.txt
```

#### 4.4.2 FTP 密码爆破

bash

```
# FTP 密码爆破
./GYscan.exe ftp brute \
--target192.168.1.100 \
--user ftpuser \
--wordlist passwords.txt

# 检测匿名登录
./GYscan.exe ftp anonymous --target192.168.1.100
```

#### 4.4.3 数据库密码爆破

bash

```
# MySQL 密码爆破
./GYscan.exe database mysql \
--target192.168.1.100 \
--user root \
--wordlist passwords.txt

# MSSQL 密码爆破
./GYscan.exe database mssql \
--target192.168.1.100 \
--user sa \
--wordlist passwords.txt

# PostgreSQL 密码爆破
./GYscan.exe database postgres \
--target192.168.1.100 \
--user postgres \
--wordlist passwords.txt
```

### 4.5 协议操作功能

#### 4.5.1 SMB 操作

bash

```
# SMB 版本检测
./GYscan.exe smb version --target192.168.1.100

# 枚举 SMB 共享
./GYscan.exe smb shares --target192.168.1.100

# 使用凭据访问共享
./GYscan.exe smb shares \
--target192.168.1.100 \
--user Administrator \
--password"Password123"
```

#### 4.5.2 RDP 操作

bash

```
# 查看 RDP 会话
./GYscan.exe rdp sessions --target192.168.1.100

# 查看 RDP 进程
./GYscan.exe rdp processes --target192.168.1.100
```

#### 4.5.3 WMI 远程管理

bash

```
# 执行 WMI 查询
./GYscan.exe wmi query \
--target192.168.1.100 \
--user Administrator \
--password"Password123"\
--query"SELECT * FROM Win32_Process"

# 远程创建进程
./GYscan.exe wmi process \
--target192.168.1.100 \
--user Administrator \
--password"Password123"\
--command"cmd.exe /c whoami"
```

### 4.6 Web 安全功能

#### 4.6.1 目录扫描

bash

```
# 使用默认字典扫描
./GYscan.exe dirscan --target http://192.168.1.100

# 指定自定义字典
./GYscan.exe dirscan \
--target http://192.168.1.100 \
--wordlist custom.txt

# 指定文件扩展名
./GYscan.exe dirscan \
--target http://192.168.1.100 \
--extensions php,asp,aspx,jsp
```

#### 4.6.2 CSRF 检测

bash

```
# 检测 CSRF 漏洞
./GYscan.exe csrf scan --target http://192.168.1.100/form.php

# 带参数的 POST 请求检测
./GYscan.exe csrf scan \
--target http://192.168.1.100/api/user \
--data"username=admin&password=123"
```

#### 4.6.3 XSS 检测

bash

```
# 检测 XSS 漏洞
./GYscan.exe xss scan --target http://192.168.1...