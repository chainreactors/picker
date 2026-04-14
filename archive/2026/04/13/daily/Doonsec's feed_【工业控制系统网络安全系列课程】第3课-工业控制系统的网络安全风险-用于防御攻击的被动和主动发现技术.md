---
title: 【工业控制系统网络安全系列课程】第3课-工业控制系统的网络安全风险-用于防御攻击的被动和主动发现技术
url: https://mp.weixin.qq.com/s/3RTFwPN-_eiML4AEJgr_Tg
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:40:29.938981
---

# 【工业控制系统网络安全系列课程】第3课-工业控制系统的网络安全风险-用于防御攻击的被动和主动发现技术

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icKb2wsWzy9OGY0zAl6wlkl0GcQRSZPbichCe9k6H8hEqnFVRkRic4aFl43bURKGZUWaI1PzAia5ibNWSk4LZFWJj3w/0?wx_fmt=jpeg)

# 【工业控制系统网络安全系列课程】第3课-工业控制系统的网络安全风险-用于防御攻击的被动和主动发现技术

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

2820字

阅读时间：

8分钟

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9PEjp9eSNQiaUOd1c6YqwgfmkPpdz6eLJ8DdlDNUBqveKtiacEVRcfsmdBFkicRIT6Jx5UjOKE0ia3ovA/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9PEjp9eSNQiaUOd1c6YqwgfmWXkibyqRGYwGCtfKsZVPyXib1Hnia07via66RuViaMOMicKXfLQeRKxgd9Ow/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/tE7RtngPUmic1MqVYB6nqZPgDKwGOuj07pAdzArsrJquyDPuFjqtEQoUibOP5KX7fCQI3Q6PNOQ0nSHSJEicYUjegLDXrDRfOqEYNfRq7R7TH8/640?wx_fmt=png&from=appmsg)

从计算机配置文件中可以学到很多东西，例如正在使用的服务、可能经常访问的主机、指定为域名服务器的 主机等。 历史文件提供有关用户使用哪些应用程序、发出的命令和启动的进程等的信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tE7RtngPUmibgvQ8GDw3E3dzn2vhhg42jLrvDd76qnV9tiaAEicAqqwOPwn7E0Z5CDcDTnT9vPYNPYmrbVxwjxMDG3cRWwMRPEovnAR6r5UNibU/640?wx_fmt=png&from=appmsg)

在网络被动发现阶段，查看 `.bash_history` 文件可以帮助安全分析人员**在不主动发送任何网络数据包的情况下**，了解到以下重要信息：

1. **识别其他主机和网络**：通过搜索 `ssh`、`ftp`、`telnet`、`ping` 等命令，可以发现该用户曾连接过哪些远程主机（IP 地址或主机名）。
2. **发现敏感信息**：某些命令可能直接包含用户名、明文密码、关键文件路径或数据库连接字符串。
3. **了解运维习惯**：可以观察到用户启动或停止了哪些服务、运行过哪些脚本、挂载过哪些 USB 设备等，从而构建出更完整的网络和系统活动图景。
4. **追溯攻击痕迹**：如果系统被入侵，攻击者输入的命令也可能留存在历史文件中，为溯源提供线索。

.bash\_history 文件是一个隐藏文件，位于 Linux 系统中每个用户的主目录下（路径为 ~/.bash\_history）。它会记录该用户在 Bash 命令行 shell 中执行过的所有命令历史。

![](https://mmbiz.qpic.cn/mmbiz_png/tE7RtngPUm9iabqonSDEnuxibibRLSnqfkuTZIoAVdA0cG3j8IKCGyfraryoEZ7yZRCDA5phmtPz5AJHvf3Fmqice2uPnUomiaQKD3I67jvEkHPo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tE7RtngPUm9J8GbgMUt7ljQibviatHVciaRKMgmYRZEibwgqygbibQj3t3z6GS7SghooD3PN1y6EcuDrpwefAXUkGHCbRzLM2mXLfAp2FU8jhrK4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tE7RtngPUmibeJkW55pHQxg9fEOPfJTWeXm5v5oB7Q15ue6LwJLrfCWGKqWcIk1YJoXcgbMTkMtpfNKnJW9guu5P1fJFANAkicTQleqN6cB20/640?wx_fmt=png&from=appmsg)

### 下面进入主动发现技术

### 什么是活动网络发现？

主动发现是一种通过向目标网络**主动发送探测数据包**（如 ARP 请求、ICMP Echo 请求、TCP SYN 数据包等），并根据收到的**响应信息**来识别网络中的活跃主机、开放端口、运行的服务以及操作系统类型的技术。它类似于声呐（SONAR）的工作原理——主动发出信号，然后分析反射回来的信号来绘制网络地图。

### 为什么要使用主动发现方法？

1. **获取更全面的信息**
   被动发现只能观察到已存在的通信流量，无法发现“沉默”的资产。主动发现可以探测到网络中**未主动通信但在线的主机**，并能识别出服务的具体版本、操作系统类型等详细信息。
2. **验证网络安全策略**
   通过模拟攻击者的扫描行为，可以检验防火墙规则、入侵检测系统（IDS）的配置是否生效，发现网络中的**薄弱环节**（如不应暴露的端口、过时的服务等）。
3. **资产盘点与变更管理**
   当网络规模较大或缺乏准确的资产清单时，主动扫描能够快速**建立完整的设备台账**，并发现未授权接入的非法设备。
4. **支持渗透测试与风险评估**
   在授权的测试环境中，主动发现是漏洞挖掘和漏洞利用（如使用 Metasploit）的前提步骤，能够帮助测试人员定位潜在的攻击入口点。

注：在真实的工业控制系统（ICS）环境中进行主动发现可能导致控制器崩溃、设备死机或配置丢失。建议仅在隔离的非生产网络中使用，并采用慢速扫描，避免使用操作系统检测等高危选项。

![](https://mmbiz.qpic.cn/mmbiz_png/tE7RtngPUm9iccT2YdZIaOyMkmx66hE1fNCnoaW4d6lmicNMictWqniaTUicLnu4lz2ibY90xtqjk2XP2n5cSPJWaKcXnMXiaHp6lpVbsGUXn6URHU/640?wx_fmt=png&from=appmsg)

ARP-Scan   ARP-Scan将ARP 数据包发送到本地网络上的主机，并显示收到的任何响应。

• ARP-Scan 工具是一种快速数据包扫描器，可显示本地子网上的每个活动IPv4 设备。ARP-Scan将 ARP 数据包发送到本地网络上的设备，并显示收到的任何响应。请注意，arp-scan命令不会填充ARP 缓存。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tE7RtngPUmicYItqyrDeWrwyd8moFEaiaL515xt42ejQbvpFfwxwUeB9fDFdYZoXWnxPH2qTeFzVt7vjuIBPwvfOBFsBqxPlQpJukUJaiaYxjU/640?wx_fmt=png&from=appmsg)

Nmap是一个免费的开源工具，对IT、SCADA和 PCS 系统可能很危险，主要用于1） 主机发现和 2） 端口扫描

### Nmap操作系统和版本检测

* **操作系统检测（OS Detection）**：Nmap 使用 **TCP/IP 堆栈指纹识别**技术，通过分析目标系统发送的数据包中的特定特征，来**远程推断目标主机运行的操作系统类型及版本**（如 Windows 10、Linux 3.x、iOS 等）。
* **版本检测（Version Detection）**：在发现开放端口后，Nmap 会进一步与这些端口上的服务进行交互，**识别具体运行的应用程序名称和版本号**（如 Apache httpd 2.4.41、OpenSSH 7.9 等）。

### 为什么要使用操作系统和版本检测？

1. **漏洞评估**：了解目标的操作系统和服务版本后，可以快速查找对应的已知漏洞（CVE），判断是否存在可被利用的安全风险。
2. **渗透测试规划**：攻击者或安全测试人员需要知道目标环境，才能选择合适的漏洞利用代码（Exploit）和有效载荷（Payload）。
3. **资产管理与合规**：帮助网络管理员发现网络中未授权的操作系统或过时的软件版本，确保符合安全基线要求。
4. **网络拓扑理解**：不同类型的设备（服务器、工作站、网络设备、ICS 控制器）通常运行不同的操作系统，识别它们有助于绘制更准确的网络地图。

### 操作系统检测如何工作？

1. **发送精心构造的探测包**：Nmap 向目标主机发送**一系列特制的 TCP、UDP 和 ICMP 数据包**，这些数据包在协议栈的边界行为上有特殊设计（例如，设置异常的标志位、分片方式、TCP 选项等）。
2. **分析响应特征**：不同的操作系统协议栈在处理这些“异常”数据包时，会产生**细微的差异**，例如：

* 初始 TTL 值
* TCP 窗口大小
* 分片重装行为
* 对某些标志位组合的响应方式
* ICMP 错误消息的格式

3. **指纹匹配**：Nmap 将收集到的响应特征与其内置的 **指纹数据库**（包含数千种操作系统和版本的签名）进行比对，输出最匹配的操作系统类型。

### 服务和版本检测如何工作？

1. **连接目标端口**：Nmap 首先通过端口扫描发现开放的 TCP/UDP 端口。
2. **发送探测查询**：对于每个开放端口，Nmap 会按照该端口常见服务的协议，发送**特定的探测字符串**。例如：

* 对端口 80 发送 `GET / HTTP/1.0` 请求
* 对端口 22 发送 SSH 协议版本协商请求

3. **分析响应内容**：Nmap 接收并分析目标返回的 **Banner 信息**或协议握手响应。这些响应中通常包含服务名称、版本号、操作系统信息等。
4. **匹配签名库**：将响应内容与 Nmap 的 **服务指纹签名库** 进行匹配，输出服务名称和版本信息。

### ICS 环境中的 Nmap 扫描挑战与注意事项

#### 一、主要风险

* **系统重启**：扫描可能导致计算机系统意外重新启动。
* **设备故障**：嵌入式设备（如 PLC、RTU）可能冻结或丢失配置，严重时需供应商介入修复。

#### 二、Nmap 安全扫描建议

1. **使用连接扫描**
   采用 `-sT`（TCP Connect 扫描）替代默认的 SYN 扫描，避免产生半开连接（悬空连接）导致设备异常。
2. **禁用高风险检测**
   **切勿**使用操作系统检测（`-O`）和版本检测（`-sV`），这两类探测极易触发设备崩溃。
3. **降低扫描速度**
   通过计时模板控制发包速率，推荐使用 `-T2`（Polite）或更慢的 `-T1`（Sneaky）、`-T0`（Paranoid），避免流量冲击。
4. **排除高风险目标**
   利用 `--exclude <IP>` 或 `--excludefile <文件名>` 跳过已知的不稳定主机（如老旧 PLC、无补丁的嵌入式设备），防止意外损坏。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tE7RtngPUm8GZic4WmXf3pKlre9PL6quE0bIRa1UazqSvMpRyKLgOFDN1LhFUGuKcDXxAMEkIWVcH8JMIicgjGP4eLN2nHnjdUA8mFBgxvBHw/640?wx_fmt=png&from=appmsg)

end

**往期内容**回顾****

|  |
| --- |
| [内网对抗穿透之隧道转发及突破系统防火墙限制](https://mp.weixin.qq.com/s?__biz=MzI0MzM3NTQ5MA==&mid=2247484737&idx=1&sn=0c2b2a3b8859c9129071bbf82436a3ff&scene=21#wechat_redirect) |
| [内网渗透测试之Responder工具](https://mp.weixin.qq.com/s?__biz=MzI0MzM3NTQ5MA==&mid=2247484328&idx=1&sn=07f021b08740d444a01b8fc22e29c5d8&scene=21#wechat_redirect) |
| [内网渗透之内网信息收集](https://mp.weixin.qq.com/s?__biz=MzI0MzM3NTQ5MA==&mid=2247484283&idx=1&sn=4d6fbc1ba1da56cab8e452c27ed4210b&scene=21#wechat_redirect) |
| [内网渗透工具mimikatz](https://mp.weixin.qq.com/s?__biz=MzI0MzM3NTQ5MA==&mid=2247484295&idx=1&sn=c1eae2e75a5a4eb6b660936435dbf6cb&scene=21#wechat_redirect) |

@请赐予我力量，关注和转发是最大的支持@

欢迎进群交流

![](https://mmbiz.qpic.cn/mmbiz_jpg/tE7RtngPUmibKtvbQMiaib2k0iaeM6T4DGPDht3cwzVVPg1aTEfqzAJoRBTzLoYITmU6ZrIYlUUvPQAdP1icnic8UaM09RaPL7k6NWibcib9ibUQXSPo/640?wx_fmt=jpeg)

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