---
title: 【工业控制系统网络安全系列课程】第4课-工业控制系统的网络安全风险-Metasploit攻击框架基础（二）
url: https://mp.weixin.qq.com/s/5vTS_1iCXgnqs9X4nxvHgg
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:53:08.812194
---

# 【工业控制系统网络安全系列课程】第4课-工业控制系统的网络安全风险-Metasploit攻击框架基础（二）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icKb2wsWzy9OGY0zAl6wlkl0GcQRSZPbichCe9k6H8hEqnFVRkRic4aFl43bURKGZUWaI1PzAia5ibNWSk4LZFWJj3w/0?wx_fmt=jpeg)

# 【工业控制系统网络安全系列课程】第4课-工业控制系统的网络安全风险-Metasploit攻击框架基础（二）

原创

老付话安全
老付话安全

老付话安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/7UnMUNqGIz071DWbJdrzpdJpDxlHDFtnMDlvK8TeibfibdovgH3vMKfIloQibicL6TTiaXQib28nacKJv8qx7AJNnm8g/640?wx_fmt=gif)

**点击蓝字**

**关注我们**

关注我，带给你不一样的精彩

世界因你的沉淀而出彩

**始于理论，源于实践，终于实战**

**老付话安全，每天一点点**

**激情永无限，进步看得见**

![](https://mmbiz.qpic.cn/mmbiz_png/lB1oaPhdMNvxZ67rEjeQWUFqwCxiacBblWHRAxzuoMfYPQXETZ7Y5bsGSLBPy2QGDKIbia74ruAWgJXhWkMlGgkA/640?wx_fmt=png)

**严正声明**

本号所写文章方法和工具只用于学习和交流，严禁使用文章所述内容中的方法未经许可的情况下对生产系统进行方法验证实施，发生一切问题由相关个人承担法律责任，其与本号无关。

特此声明！！！

本文字数：4503

字

阅读时间：

14分钟

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9PEjp9eSNQiaUOd1c6YqwgfmkPpdz6eLJ8DdlDNUBqveKtiacEVRcfsmdBFkicRIT6Jx5UjOKE0ia3ovA/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9PEjp9eSNQiaUOd1c6YqwgfmWXkibyqRGYwGCtfKsZVPyXib1Hnia07via66RuViaMOMicKXfLQeRKxgd9Ow/640?from=appmsg)

## MSF 有效负载概述

有效负载是漏洞利用成功后在目标系统上执行的代码。

Metasploit 有效负载涵盖五个核心维度：操作系统目标、通信选项、操作类型、修饰符 以及 Meterpreter。

## 1、操作系统目标

有效负载必须与目标系统的**操作系统**和**系统架构**相匹配，否则无法执行。

| 操作系统 | 常见架构 | 示例 Payload |
| --- | --- | --- |
| Windows | x86, x64 | `windows/meterpreter/reverse_tcp` `windows/x64/meterpreter/reverse_tcp` |
| Linux | x86, x64, armle | `linux/x86/meterpreter/reverse_tcp` `linux/x64/meterpreter/reverse_tcp` |
| macOS | x64, arm64 | `osx/x64/meterpreter/reverse_tcp` |
| Android | armle, dalvik | `android/meterpreter/reverse_tcp` |
| iOS | armle | `apple_ios/meterpreter/reverse_tcp` |

> **选择原则**：先确认目标操作系统版本及位数（32/64 位），再选择对应 payload。错误选择会导致攻击失败或目标进程崩溃。

---

## 2、通信选项

定义有效负载如何与攻击者建立网络连接。主要分为两大类：

| 通信方向 | 说明 | 典型 Payload 后缀 | 适用场景 |
| --- | --- | --- | --- |
| **Bind（绑定）** | 目标系统开放一个端口，等待攻击者主动连接。 | `bind_tcp` 、`bind_ipv6_tcp` | 目标可直接访问、无入站防火墙限制；横向移动中通过跳板机连接内网目标。 |
| **Reverse（反向）** | 目标系统主动连接攻击者监听的端口。 | `reverse_tcp` 、`reverse_https`、`reverse_udp` | 目标有出网能力、入站防火墙严格；最常见方式。 |

### 通信协议

* **TCP**：稳定可靠，最常用。
* **UDP**：可用于 TCP 被过滤的环境，但不可靠。
* **HTTP/HTTPS**：流量伪装成正常网页访问，穿透能力强，不易被检测。
* **DNS**：极隐蔽，用于极端受限网络（需专用模块）。

---

## 3、操作类型

根据有效负载执行后的**行为与功能**进行分类。

| 类型 | 说明 | 示例 Payload |
| --- | --- | --- |
| **Shell** | 提供传统命令行 shell（cmd 或 /bin/sh）。 | `windows/shell/reverse_tcp` `linux/x86/shell/bind_tcp` |
| **Meterpreter** | 高级交互式 payload，支持文件操作、进程迁移、键盘记录、提权等丰富功能。 | `windows/meterpreter/reverse_tcp` |
| **VNC Inject** | 向目标进程注入 VNC 服务器，实现远程桌面控制。 | `windows/vncinject/reverse_tcp` |
| **Adduser** | 在目标系统上添加新用户（常用于后渗透）。 | `windows/adduser` |
| **Exec** | 执行一条指定命令后退出（一次性）。 | `linux/x86/exec` |
| **Download/Upload** | 仅用于文件传输（较少单独使用）。 | `windows/download_exec` |

---

## 4、修饰符

修饰符用于进一步定制 payload 的行为，以绕过防护或适应特殊环境。

| 修饰符 | 含义 | 示例 Payload | 说明 |
| --- | --- | --- | --- |
| `_staged` / `_stageless` | 分阶段 / 单一体 | `windows/meterpreter/reverse_tcp` （staged） `windows/meterpreter_reverse_tcp`（stageless，注意下划线位置） | Staged 先传小 stager，再下载主体，适合空间受限；Stageless 全功能一体，更稳定但体积大。 |
| `_nonx` | 绕过 NX（数据执行保护） | `linux/meterpreter/reverse_nonx_tcp` | 针对启用了内存执行保护的目标。 |
| `_allports` | 尝试所有端口 | `windows/meterpreter/reverse_tcp_allports` | 用于端口限制严格或动态变化的环境，提高成功率。 |
| `_ipv6` | 使用 IPv6 协议 | `windows/x64/meterpreter/bind_ipv6_tcp` | 用于纯 IPv6 网络或绕过仅过滤 IPv4 的防火墙。 |
| `_https` | 使用 HTTPS 加密通信 | `windows/meterpreter/reverse_https` | 流量加密，更难检测。 |
| `_rc4` | 使用 RC4 加密 | `windows/meterpreter/reverse_rc4` | 简单加密，绕过基础检测。 |

> **命名规律**：修饰符通常放在连接方式之后、协议之前或末尾，具体以实际模块名称为准。

---

## 5、Meterpreter

**Meterpreter**（Metasploit Interpreter）是 Metasploit 框架中最强大、最常用的 payload，运行在目标进程内存中，**不写入磁盘**，具有极高的隐蔽性和扩展性。

### 核心特性

| 特性 | 说明 |
| --- | --- |
| **内存运行** | 不创建磁盘文件，难以被传统杀毒软件查杀。 |
| **进程迁移** | 可迁移至其他稳定进程（如 `explorer.exe`），避免因原进程退出而断开连接。 |
| **丰富命令** | 支持文件上传/下载、屏幕截图、键盘记录、密码哈希导出、提权、端口转发等。 |
| **扩展加载** | 可动态加载扩展模块（如 `mimikatz`、`powershell`、`python`）。 |
| **多会话管理** | 同时管理多个目标会话，支持后台切换。 |
| **流量加密** | 支持 HTTPS、RC4 等加密通信方式。 |

### 常用 Meterpreter 命令分类

| 类别 | 命令示例 | 功能 |
| --- | --- | --- |
| 系统信息 | `sysinfo` , `getuid`, `getpid` | 查看目标系统信息、当前权限、进程 ID |
| 进程操作 | `ps` , `migrate <PID>`, `kill <PID>` | 列出进程、迁移会话、终止进程 |
| 文件操作 | `ls` , `cd`, `upload`, `download`, `cat` | 浏览目录、上传下载文件、查看文件内容 |
| 网络操作 | `ifconfig` , `netstat`, `arp`, `route`, `portfwd` | 查看网络配置、连接、ARP 表、路由、端口转发 |
| 用户交互 | `shell` , `execute` | 进入系统 shell、执行程序 |
| 权限提升 | `getsystem` | 尝试提升至 SYSTEM 权限 |
| 信息收集 | `hashdump` , `screenshot`, `keyscan_start/dump` | 导出密码哈希、截屏、键盘记录 |
| 日志清理 | `clearev` | 清除 Windows 事件日志 |
| 扩展加载 | `load mimikatz` , `load powershell` | 加载第三方扩展 |
| 会话管理 | `background` , `exit` | 后台挂起、退出会话 |

Metasploit 将有效负载分为三类：

### 1. 独立（Staged）与内联（Inline）

* **Staged**（分阶段）：先发送一个小型 stager 下载主体，适合空间受限环境。
  示例：`windows/meterpreter/reverse_tcp`
* **Inline**（单一体）：所有功能集成在一个 payload 中，体积较大，更稳定。
  示例：`windows/shell_reverse_tcp`（注意下划线）

### 2. 常用有效负载类型

| 类型 | 说明 | 示例 |
| --- | --- | --- |
| `shell` | 提供命令行 shell（cmd 或 /bin/sh） | `windows/shell/bind_tcp` |
| `meterpreter` | 高级交互式 payload，支持文件上传下载、屏幕截图、提权等 | `windows/meterpreter/reverse_https` |
| `vnc` | 注入 VNC 服务器，远程控制桌面 | `windows/vncinject/reverse_tcp` |
| `adduser` | 在目标系统上添加用户 | `windows/adduser` |
| `exec` | 执行指定命令 | `linux/x86/exec` |

### 3. 连接方式修饰符

* **bind\_tcp**：目标开启端口等待攻击者连接（需能直接访问目标）。
* **reverse\_tcp**：目标主动连接攻击者（常用，可绕过入站防火墙）。
* **reverse\_https**：使用 HTTPS 加密回连，更难检测。

### 4. 选择有效负载的原则

* 目标操作系统与架构（x86 / x64）
* 通信方向（反向更通用）
* 功能需求（仅 shell 或 meterpreter）
* 网络环境（是否允许出站 HTTPS）

## Meterpreter 常用命令

Meterpreter 是 Metasploit 中最强大的交互式 payload，运行在目标进程内存中，不写入磁盘。

### 系统信息与文件操作

| 命令 | 说明 | 示例 |
| --- | --- | --- |
| `sysinfo` | 显示目标系统信息（OS、主机名等） | `sysinfo` |
| `getuid` | 显示当前权限（用户/系统） | `getuid` |
| `getpid` | 显示当前 meterpreter 进程 ID | `getpid` |
| `ps` | 列出目标上所有进程 | `ps` |
| `migrate <PID>` | 将 meterpreter 迁移到其他进程（更稳定） | `migrate 688` |
| `pwd` / `getwd` | 显示当前工作目录 | `pwd` |
| `ls` | 列出目录内容 | `ls C:\\` |
| `cd` | 切换目录 | `cd C:\\Users` |
| `cat` | 显示文件内容 | `cat secret.txt` |
| `upload` / `download` | 上传/下载文件 | `upload /root/tool.exe C:\\temp` |

### 网络与权限

| 命令 | 说明 | 示例 |
| --- | --- | --- |
| `ifconfig` | 显示网络接口配置 | `ifconfig` |
| `netstat` | 显示网络连接 | `netstat -an` |
| `arp` | 显示 ARP 缓存 | `arp` |
| `route` | 查看或添加路由 | `route add 10.0.0.0 255.255.255.0 1` |
| `portfwd` | 端口转发（本地<->目标） | `portfwd add -L 0.0.0.0 -l 8080 -p 80 -r 127.0.0.1` |
| `execute` | 在目标上执行程序 | `execute -f cmd.exe -i -H` |
| `shell` | 进入传统系统 shell（exit 返回 meterpreter） | `shell` |
| `getsystem` | 尝试提升权限至 SYSTEM | `getsystem` |

### 信息收集与后渗透

| 命令 | 说明 | 示例 |
| --- | --- | --- |
| `hashdump` | 导出 SAM 哈希（需要管理员权限） | `hashdump` |
| `screenshot` | 截取目标桌面 | `screenshot` |
| `keyscan_start` / `keyscan_dump` | 键盘记录 | `keyscan_start` 然后 `keyscan_dump` |
| `clearev` | 清除 Windows 事件日志 | `clearev` |
| `load` | 加载扩展（如 mimikatz、powershell） | `load mimikatz` |
| `help` | 显示所有 meterpreter 命令 | `help` |

### 会话管理

| 命令 | 说明 |
| --- | --- |
| `background` | 将当前 meterpreter 会话放到后台，返回 msfconsole |
| `sessions -i <ID>` | 从 msfconsole 重新进入指定会话 |
| `exit` | 终止当前会话（目标上 meterpreter 退出） |

##

end

**往期内容**回顾****

|  |
| --- |
| [【工业控制系统网络安全系列课程】第2课-工业控制系统的网络安全风险-过程控制漏洞利用过程](https://mp.weixin.qq.com/s?__biz=MzI0MzM3NTQ5MA==&mid=2247486037&idx=1&sn=611a127747a9b05e02a2ef4bf1114e0c&scene=21#wechat_redirect) |
| [【工业控制系统网络安全系列课程】第2课-工业控制系统的网络安全风险-过程控制漏洞利用（一）ICS过程控制漏洞概述](https://mp.weixin.qq.com/s?__biz=MzI0MzM3NTQ5MA==&mid=2247486039&idx=1&sn=9da3debdeee21e4d6eca9efc0838d3cd&scene=21#wechat_redirect) |
| [【工业控制系统网络安全系列课程】第2课-工业控制系统的网络安全风险-过程控制漏洞利用（二）典型漏洞利用路径](https://mp.weixin.qq.com/s?__biz=MzI0MzM3NTQ5MA==&mid=2247486040&idx=1&sn=500f7e115c7abb2e44d3ee9326382085&scene=21#wechat_redirect) |

@请赐予我力量，关注和转发是最大的支持@

欢迎扫码进群交流

![](https://mmbiz.qpic.cn/mmbiz_jpg/tE7RtngPUm85FtZKuNRCbqvutVXOSqIphpS43hcaArSJeUjiaWxOLoibkPBlQbE6FdlN2wic4Lf7tqq7ibouYzjfzQcnRkWBGYhp9ZMVOP71PVI/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9MFl1LCgCibJeCV...