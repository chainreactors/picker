---
title: 震惊安全圈！这款自动化 reconnaissance 神器让渗透测试效率提升 1000%
url: https://mp.weixin.qq.com/s/sceYwiKoT2t1XNC6S5N0Mg
source: Doonsec's feed
date: 2026-08-18
fetch_date: 2026-08-19T02:55:38.283924
---

# 震惊安全圈！这款自动化 reconnaissance 神器让渗透测试效率提升 1000%

![cover_image](http://mmbiz.qpic.cn/sz_mmbiz_jpg/x5l8unjI0UpIPLyJY68stoM4XjlKTyf5WEFxGib0ic8CoIeNxn5Se9WcnicbFvOsiar2RCyHjKGxRHicic3e0uAgpiajQG1WumPvYh2ibJAQfHE6LII/0?wx_fmt=jpeg)

# 震惊安全圈！这款自动化 reconnaissance 神器让渗透测试效率提升 1000%

棉花糖糖糖
棉花糖糖糖

棉花糖网络安全工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

郑重声明：本文仅作为技术分享，工具使用者需自行承担安全责任，请勿用于非法途径。

AutoRecon 是一款专为安全研究人员打造的多线程自动化网络侦察工具。该工具能够自动执行目标服务的枚举任务，大幅缩短信息收集阶段的时间成本。其设计初衷是服务于 CTF 竞赛环境以及渗透测试评估场景（如 OSCP 认证考试），同时亦适用于真实世界的安全审计项目。

## 重点导读核心能力

### PART 01智能侦察

AutoRecon 的工作流程采用两阶段设计。工具首先对目标执行端口扫描与服务识别，随后基于扫描结果自动触发针对各服务的深度枚举模块。例如，当系统检测到 HTTP 服务时，将自动调用 feroxbuster、nikto、whatweb 等多款工具进行联动扫描。整个过程无需人工干预，测试人员可专注于结果分析与漏洞利用环节。

### PART 02高并发架构

工具支持多目标并行扫描，可充分利用多核处理器资源。IPv4 与 IPv6 地址均在支持范围内，IP 地址、CIDR 网段、可解析主机名三种目标格式可混合使用。默认配置下最多同时运行 50 个并发扫描任务，端口扫描阶段约占总任务数的 20%。

### PART 03插件生态

AutoRecon 内置超过 70 个默认插件，涵盖以下服务类型：

* 端口扫描插件：TCP 全端口、UDP 高频端口、定制端口范围
* 服务扫描插件：HTTP、SMB、SSH、FTP、DNS、SNMP、MySQL、Oracle、Redis、MongoDB 等
* 暴力破解插件：FTP、SSH、SMB、RDP、HTTP 认证接口
* 报告生成插件：Markdown 格式、Cherrytree 格式

插件系统采用标签机制管理，支持通过 `--tags` 与 `--exclude-tags` 参数灵活筛选。高级用户可创建自定义插件并通过 `--add-plugins-dir` 参数加载。

## 重点导读配置体系

### PART 04扫描配置

默认配置严格遵循 OSCP 考试规范，不包含任何自动化漏洞利用模块。配置文件采用 TOML 格式，路径为 `~/.config/AutoRecon/config.toml`。用户可在个人配置文件中添加自动漏洞利用工具，但需自行承担风险。

### PART 05全局设置

全局配置文件 `~/.config/AutoRecon/global.toml` 用于存储跨任务通用参数，包括默认用户名/密码字典路径、域名称等。该设计确保多目标扫描场景下参数的一致性。

### PART 06结果组织

工具自动生成结构化输出目录，每个目标对应独立子目录：

```
results/
└── <target>/
    ├── exploit/       # 漏洞利用代码
    ├── loot/          # 敏感信息提取物
    ├── report/        # 报告文件
    │   ├── local.txt
    │   ├── notes.txt
    │   ├── proof.txt
    │   └── screenshots/
    └── scans/         # 扫描结果
        ├── _commands.log       # 执行命令日志
        ├── _manual_commands.txt # 需手动执行的命令
        ├── tcp80/
        ├── udp53/
        └── xml/                # Nmap XML 输出
```

`_commands.log` 文件记录所有执行的命令及其输出，便于复现与调试。`_manual_commands.txt` 列出因安全性或复杂性原因不适合自动运行的命令，供测试人员手动执行。

## 重点导读使用方式

### PART 07命令行接口

```
bashautorecon [targets ...] [options]
```

常用参数：

* `-t FILE`：从文件读取目标列表
* `-p PORTS`：指定扫描端口，支持 T:/U:/B: 前缀区分 TCP/UDP/两者
* `-m MAX_SCANS`：最大并发扫描数
* `-o OUTPUT`：输出目录路径
* `--timeout MINUTES`：全局超时时间
* `--target-timeout MINUTES`：单目标超时时间
* `-v/-vv/-vvv`：三级详细输出模式

### PART 08详细级别控制

工具提供四级输出详细程度，可通过命令行参数或扫描过程中按上下方向键实时调整。该功能使测试人员能够在详细信息与性能开销之间灵活切换。

### PART 09无端口扫描模式

当已通过其他渠道获知目标服务信息时，可使用 `--force-services` 参数直接指定服务类型，跳过端口扫描阶段。

## 重点导读技术架构

### PART 10核心模块

项目采用 Python 3.8+ 开发，主要模块包括：

* `autorecon.py`：命令行入口
* `autorecon/main.py`：主程序逻辑
* `autorecon/plugins.py`：插件加载与管理
* `autorecon/config.py`：配置解析
* `autorecon/targets.py`：目标管理
* `autorecon/io.py`：输入输出处理

### PART 11依赖工具

完整功能依赖以下外部工具：

nmap、curl、dnsrecon、enum4linux、feroxbuster、gobuster、impacket-scripts、nbtscan、nikto、onesixtyone、oscanner、redis-tools、smbclient、smbmap、snmpwalk、sslscan、svwar、tnscmd10g、whatweb

Kali Linux 用户可通过以下命令一键安装：

```
bashsudo apt install seclists curl dnsrecon enum4linux feroxbuster gobuster impacket-scripts nbtscan nikto nmap onesixtyone oscanner redis-tools smbclient smbmap snmp sslscan sipvicious tnscmd10g whatweb
```

### PART 12安装方式

支持三种安装途径：

1. **pipx（推荐）**：`pipx install git+https://github.com/Tib3rius/AutoRecon.git`
2. **pip**：`python3 -m pip install git+https://github.com/Tib3rius/AutoRecon.git`
3. **手动安装**：`python3 -m pip install -r requirements.txt` 后直接运行 `autorecon.py`

## 重点导读应用场景

### PART 13CTF 竞赛

在限时竞赛环境中，AutoRecon 可在后台自动执行信息收集，参赛者得以专注于漏洞利用与权限提升环节。工具生成的结构化报告便于团队成员快速共享发现。

### PART 14认证考试

OSCP 等渗透测试认证考试中，信息收集阶段的时间分配至关重要。AutoRecon 帮助考生在单目标上启动扫描后立即转向其他目标，实现时间的高效利用。

### PART 15渗透测试

真实渗透测试项目中，自动化侦察显著提升效率。工具的详细日志与输出结构为最终报告撰写提供了完整的证据链。

本文介绍的项目开源地址如下：

```
https://github.com/AutoRecon/AutoRecon
```

本公众号非项目作者，仅做技术分享。

## 广告时间

**低价考证包括但不限于CISP系列、PMP等等国内网安证书、网络安全交流群请关注公众号后点菜单栏的找棉花糖。**

**糖心会员站，网络安全必备网站，包括在线内网靶场、web靶场、src靶场、应急响应靶场，以及各种网安资料、教程、方案模版、以及超级多在线工具，99元包年！详细介绍：**[棉花糖会员站介绍(26年4月26日版本) ：在线内网靶场、网安资料方案、在线工具全能资源站](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493656&idx=1&sn=ef2aad19a122c739055604331f93f34c&scene=21#wechat_redirect)**，看完介绍百分百心动！**

![棉花糖会员站介绍图1](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0Ur4LlITe968UT5OHSWbiczj9jwlqS1XRq2o1UCb4QM4WgnpDlPeQCOlWFHmhcPV8h3Hr5icchCANibjYHVJ67JQpYKC97w5ygn0QE/640?from=appmsg)

![棉花糖会员站介绍图2](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UrS4NziccgInKID7b2nfqjBGTG8LVUy8y2gfnzQV7NAVNwKtgq4cicSsJzEeCKogbNPiaibZ0lreiaCCOlkfLbYpEZROOjTMiaeymHuk/640?from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UrCSxv33ws9W4q7NCsLZiaWAQPkO1Tr0E81AlzPiah3DzibhDxWLTTViaTb8BXvSoRhkkJ3hqFMlfrhIxlSZ8CWyBib5lyyLQyJ36Wo/0?wx_fmt=png)

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