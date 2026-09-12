---
title: 黑客借助ClickFix投放新型SloppyRAT，支撑勒索软件横向移动
url: https://mp.weixin.qq.com/s/7OZXhNzlSR1eoAJa0qDD2A
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:42:50.261326
---

# 黑客借助ClickFix投放新型SloppyRAT，支撑勒索软件横向移动

# 黑客借助ClickFix投放新型SloppyRAT，支撑勒索软件横向移动

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

一款名为 SloppyRAT 的新型Windows远程访问木马，定位为勒索软件攻击的入侵辅助工具。
该恶意软件最早于2026年6月被观测到，通过多阶段ClickFix攻击链进行投递，具备主机侦察、隐蔽命令执行、反向代理以及高韧性命令控制能力，用于完成入侵后操作与内网横向移动。

该攻击不会直接释放传统可执行程序，而是调用Windows系统自带老旧工具 finger.exe ，从攻击者控制的服务器下载批处理脚本。
Finger协议默认使用TCP 79端口，现代企业环境几乎不会用到该端口；因此终端日志中一旦出现该协议行为，是非常有价值的告警检测信号。

下载得到的脚本会把系统合法程序 curl.exe 复制到用户AppData目录，重命名为数字后缀的 .com 文件，并用它从GitHub获取IronPython运行环境。
IronPython随后加载经过压缩与Base64编码的Python载荷，继续执行多阶段攻击链。

ThreatLabz团队发现，后续攻击会使用特征User‑Agent字符串 K8VGmQTrzX ，从域名 skipraid[.]com 下载CastleLoader与CastleRAT组件。
CastleLoader常见于各类欺骗式投放活动，负责拉取更多恶意载荷；CastleRAT则提供远程控制、命令执行能力。

Python执行的最后阶段，会从Azure云Blob存储拉取 config.py 配置文件，并以此通过DLL文件 hostfxr.dll 反射加载SloppyRAT木马。
该加载器使用请求头User‑Agent： Mozilla/5.0 (compatible; DLLMemLoader/1.0) ，防御人员可以在代理日志、云存储访问日志中检索该特征。

SloppyRAT功能丰富，能够充分服务勒索软件团伙拿到初始访问权限之后的各类操作：
可采集主机信息、安全软件信息，枚举进程、服务、用户、本地组成员、文件、注册表项、环境变量与网络连接状态。
同时支持文件下载、创建进程、执行WMI查询、篡改微软Defender配置，并且有多条执行渠道来运行系统命令。

值得关注的是：该木马直接使用C++原生实现了47条类PowerShell命令，并非每次任务都调用真实PowerShell进程。
诸如 whoami 、 Get‑Process 、 Get‑Service 、 Get‑LocalUser 、 Resolve‑DnsName 、 Test‑NetConnection 、 Get‑MpComputerStatus 这类常用命令，都被映射调用Windows原生API。
该手段大幅减少可被监控的PowerShell行为，同时攻击者依然可以使用熟悉的命令交互。
如果确实需要执行原生PowerShell代码，SloppyRAT可以加载.NET CLR，通过内部名为PSInline的处理函数，在进程内调用 System.Management.Automation 组件。

Zscaler向GBhackers提供的报告称，整套攻击始于ClickFix社会工程诱饵，诱导受害者运行经过混淆处理的系统命令。

如果该方式失败，木马会启动 powershell.exe ，并且伪造父进程为 explorer.exe ，以此干扰进程树排查。
它尝试通过Run注册表项配置 rundll32.exe 实现开机自启，但代码中缺少指向SloppyRAT DLL的完整路径与导出函数调用，该持久化方式存在缺陷。

木马的 cmd 模式通过WMI接口 Win32\_Process::Create 执行命令，进一步让攻击者行为混在正常管理员运维活动中，难以区分。

该木马最关键的能力是反向SOCKS代理功能：
恶意软件接收来自接口 /api/poll 下发的代理指令，启动反向SOCKS工作通道。攻击者就可以以被感染主机为跳板，把流量路由进入企业内网。
只拿到普通用户权限的一台沦陷主机，就变成侦察、横向移动的支点。
攻击者利用受害终端访问内网业务系统，定位文件服务器、管理服务，逐步靠近高价值资产，而不用把这些内网系统直接暴露在外网。

SloppyRAT使用字符串异或混淆、加密代码段、垃圾代码、API哈希、Hell’s Gate风格间接系统调用等多种手段对抗静态与行为分析。
它通过DJB2哈希算法定位Windows原生API，直接发起系统调用，试图绕过用户态安全钩子。

C2通信基于HTTPS并且启用证书锁定：木马会将服务器TLS证书与硬编码的SHA‑256哈希比对，不匹配就直接断开连接。该特性可以抵御网络监控工具使用TLS中间人技术解析恶意流量。

该恶意软件还设计了EtherHiding备选方案，可以借助Polygon JSON‑RPC区块链基础设施解析C2服务器配置。
ThreatLabz尚未在样本中发现启用的智能合约地址，但该实现允许攻击者将C2配置托管在区块链上，会增加传统封禁域名、IP的处置难度。

SloppyRAT持久化逻辑存在漏洞以及其他程序缺陷，说明该恶意家族还处于开发迭代阶段。但现有功能已经足以完成侦察、代理转发、命令执行以及勒索软件相关入侵活动。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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