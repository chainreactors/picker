---
title: MPET——多协议安全测试与漏洞利用工具
url: https://mp.weixin.qq.com/s/9_Md2pl0FRemhx3LggWY0A
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:15:38.564630
---

# MPET——多协议安全测试与漏洞利用工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qqiaD4wiajgFz9eXaLOhUcnfXL1MgicKGkjaV0PtXkntyNm5sZjfEPp0vyVDpqiaOq5p80VcdEzF3DbLVCgTOx1b0uKdjN8hJosoKmmHuhTDzJE/0?wx_fmt=jpeg)

# MPET——多协议安全测试与漏洞利用工具

一个人挺好
一个人挺好

一个人挺好 wa

![]()

在小说阅读器中沉浸阅读

# 项目地址

https://github.com/onewinner/MPET

# MPET 技术文档

## 1. 项目概述

**MPET (Multi-Protocol Exploitation Toolkit)** 是一款专业的多协议安全测试与漏洞利用工具，专为安全研究人员和渗透测试工程师设计。该工具基于现代化的 Wails v2 框架构建，提供图形化桌面应用体验，支持对 25+ 种主流服务协议进行全面的安全测试。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFwfWEKhyfiaaTemTkeTOtZdKnSsfNSuu0KtBsP6zP9M35jFbQiaqCZSTrxPicL3icoZfRQ616zDVOzuU2UIiaNdoZjUVX60mG4mjJ3s/640?wx_fmt=png&from=appmsg)

### 1.1 核心定位

* **目标用户**：安全研究人员、渗透测试工程师、红队成员、安全运维人员
* **应用场景**：授权安全测试、企业内部安全审计、安全培训教学、漏洞研究
* **技术特色**：多协议支持、现代化 UI、高效并发测试

---

## 2. 技术架构

### 2.1 技术栈

表格

| 层级 | 技术选型 | 说明 |
| --- | --- | --- |
| **前端框架** | Wails v2 | 基于 Go + Web 技术的现代化桌面应用框架 |
| **后端语言** | Go (Golang) | 提供高性能并发处理能力 |
| **UI 技术** | Web 前端 (HTML/CSS/JS) | 现代化界面，支持响应式设计 |
| **架构模式** | 前后端分离 | 通过 Wails 桥接实现原生与 Web 交互 |

### 2.2 架构优势

1. **跨平台能力**：基于 Wails 构建，支持 Windows、macOS、Linux 三大主流平台
2. **高性能并发**：利用 Go 语言的 goroutine 实现高效的多协议并发测试
3. **现代化 UI**：相比传统安全工具（如 Metasploit 控制台），提供更友好的图形化操作界面
4. **轻量级部署**：单二进制文件分发，无需复杂依赖安装

---

## 3. 功能模块

### 3.1 核心功能

根据项目描述，MPET 提供以下核心安全测试能力：

#### 3.1.1 连接测试模块

* **协议支持**：覆盖 25+ 种主流服务协议

+ 远程连接：SSH、RDP、Telnet、VNC
+ 数据库：MySQL、PostgreSQL、MongoDB、Redis、Elasticsearch
+ Web 服务：HTTP/HTTPS、WebSocket
+ 消息队列：RabbitMQ、Kafka、MQTT
+ 云服务：AWS S3、阿里云 OSS、Azure Blob
+ 其他：FTP、SFTP、LDAP、SMTP、SNMP 等

* **连接验证**：检测目标服务的可达性和响应状态

#### 3.1.2 未授权访问检测

* **自动化扫描**：批量检测目标服务是否存在未授权访问漏洞
* **风险评级**：根据暴露程度进行风险等级分类
* **报告生成**：输出详细的未授权访问检测报告

#### 3.1.3 弱口令检测

* **字典支持**：内置常见弱口令字典，支持自定义扩展
* **多协议爆破**：针对各协议实现针对性的认证爆破
* **智能策略**：支持自定义线程数、超时时间、重试策略
* **结果筛选**：自动识别有效凭证并分类存储

#### 3.1.4 漏洞利用

* **EXP 框架**：提供可扩展的漏洞利用代码框架
* **内置 POC**：集成常见服务的已知漏洞利用代码
* **自定义扩展**：支持用户编写自定义漏洞利用模块

### 3.2 辅助功能

根据同类工具的功能推断，MPET 可能还包含：

* **文件浏览器**：支持远程服务的文件浏览和管理（如 FTP、SFTP、S3 等）
* **Docker Shell**：集成容器化环境的命令行操作能力
* **漏洞报告**：生成结构化的安全测试报告（HTML/PDF 格式）
* **任务管理**：支持多任务的并发执行和状态监控

---

## 4. 安装与部署

### 4.1 环境要求

表格

| 组件 | 最低要求 | 推荐配置 |
| --- | --- | --- |
| 操作系统 | Windows 10 / macOS 10.15 / Ubuntu 18.04 | Windows 11 / macOS 13 / Ubuntu 22.04 |
| 内存 | 4 GB | 8 GB+ |
| 磁盘空间 | 500 MB | 1 GB+ |
| 网络 | 可访问目标测试网络 | 千兆以太网 |

### 4.2 安装方式

#### 方式一：预编译二进制文件（推荐）

1. 访问 GitHub Releases 页面：https://github.com/onewinner/MPET/releases
2. 下载对应平台的安装包（`.exe`、`.dmg` 或 `.AppImage`）
3. 运行安装程序或直接执行二进制文件

#### 方式二：源码编译

bash

```
# 1. 克隆仓库
git clone https://github.com/onewinner/MPET.git
cd MPET

# 2. 安装 Wails CLI
go install github.com/wailsapp/wails/v2/cmd/wails@latest

# 3. 安装前端依赖（进入 frontend 目录）
cd frontend
npminstall
cd..

# 4. 编译应用
wails build

# 5. 运行
./build/bin/MPET
```

### 4.3 开发模式运行

bash

```
# 进入项目目录
cd MPET

# 启动开发服务器（支持热重载）
wails dev
```

---

## 5. 使用指南

### 5.1 界面布局

MPET 采用典型的安全工具布局设计：

plain

```
┌─────────────────────────────────────────────────────────┐
│  工具栏 (新建任务/导入/导出/设置)                        │
├──────────┬──────────────────────────────────────────────┤
│          │                                              │
│  协议    │              主工作区                        │
│  导航    │         (连接配置/扫描结果/报告)              │
│  面板    │                                              │
│          │                                              │
├──────────┴──────────────────────────────────────────────┤
│  状态栏 (任务进度/日志输出/系统状态)                      │
└─────────────────────────────────────────────────────────┘
```

### 5.2 基本操作流程

#### 步骤 1：创建测试任务

1. 点击「新建任务」按钮
2. 选择目标协议类型（如 SSH、MySQL 等）
3. 配置目标地址（支持单 IP、IP 段、CIDR 格式）

#### 步骤 2：配置测试参数

* **连接配置**：端口、超时时间、重试次数
* **认证配置**：选择弱口令字典或指定测试凭证
* **高级选项**：线程数、代理设置、SSL/TLS 配置

#### 步骤 3：执行测试

* 点击「开始测试」启动扫描
* 实时查看进度和中间结果
* 支持任务暂停/恢复/终止

#### 步骤 4：查看与导出报告

* 在「结果」面板查看详细发现
* 筛选高风险/中风险/低风险项目
* 导出为 HTML/PDF/JSON 格式报告

### 5.3 典型使用场景

#### 场景一：内网服务弱口令审计

yaml

```
目标: 192.168.1.0/24
协议: SSH, MySQL, Redis, PostgreSQL
模式: 弱口令检测
字典: top1000-common-passwords.txt
线程:50
```

#### 场景二：云存储未授权访问检测

yaml

```
目标: 对象存储服务域名
协议: AWS S3 / 阿里云 OSS
模式: 未授权访问 +  Bucket 枚举
策略: 检测公开读写权限配置
```

---

## 6. 配置说明

### 6.1 全局配置

配置文件路径（根据操作系统）：

* Windows: `%APPDATA%/MPET/config.json`
* macOS: `~/Library/Application Support/MPET/config.json`
* Linux: `~/.config/MPET/config.json`

JSON

```
{
"general":{
"theme":"dark",
"language":"zh-CN",
"auto_update":true
},
"network":{
"default_timeout":5000,
"max_threads":100,
"user_agent":"MPET/1.0"
},
"security":{
"verify_ssl":true,
"proxy_enabled":false,
"proxy_address":""
},
"dictionaries":{
"username_dict":"dicts/usernames.txt",
"password_dict":"dicts/passwords.txt"
}
}
```

### 6.2 字典管理

MPET 支持多层级字典配置：

* **系统字典**：内置常用弱口令组合
* **用户字典**：自定义字典文件路径
* **动态生成**：基于规则的密码变异（如添加后缀、大小写变换）

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zyTvSBegohhPkdl4ZiaID39hGjT55M6GNVWWYfpt8Q146OaDEU4xQ0E4VtxLO4zfGia16VE6qHb001g/0?wx_fmt=png)

一个人挺好 wa

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zyTvSBegohhPkdl4ZiaID39hGjT55M6GNVWWYfpt8Q146OaDEU4xQ0E4VtxLO4zfGia16VE6qHb001g/0?wx_fmt=png)

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