---
title: 逆向万物！REA打通AI编码与逆向工具，支持多类目标无源码分析
url: https://mp.weixin.qq.com/s/HEQXX6KaJ6VdMoV3nHWFDQ
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T07:59:51.769066
---

# 逆向万物！REA打通AI编码与逆向工具，支持多类目标无源码分析

# 逆向万物！REA打通AI编码与逆向工具，支持多类目标无源码分析

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX2UBa7x9ibubR5gT2R3JFGWWBUtPDwtUyPzCKMzhFvo8iciaEyaSMFDfsctUkHtUxwevkbJaE3SmjNgH4OsmMx5mZNKGxQoCbxLbI/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1vZexyDicbLN9KQrHCnian5GLs6O1WUO3zL3Pgrn43pPy69nibqukxM7bcpVqI2icVtcNqYIIkx26cDIlRue9H2Btkg2zvRibyoKy8/640?wx_fmt=png&from=appmsg)

REA全称为Reverse Engineer Anything（逆向万物），可将Claude Code、Cursor等AI编码Agent，连接至各类无需源码即可检测软件内部结构的工具。

这一开源项目将Ghidra、IDA Pro、Hopper接入Agent驱动的工作流，帮助安全研究人员追踪程序行为，结合支撑证据解释分析结论。

REA不会替代反汇编工具，而是充当Agent与分析工具之间的桥梁。其支持范围除原生二进制文件外，还覆盖JavaScript、Electron应用、.NET程序集、Android安装包、固件、网站及部分运行时活动。偏好脚本操作的研究人员，也可通过终端命令调用全套工作流。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1WX3KJIuoh2CeOLFc2B9KJ7dAX7HmXeeGuphMXE6BQXULEODdiaGop9LEqE1oaKqYu2jVD83hCCCVyS4ia0NJmicxEpf7l8sJOnI/640?wx_fmt=png&from=appmsg)

Part01

REA覆盖多类软件逆向分析场景

REA采用模型上下文协议（MCP），允许Agent通过本地服务器发起分析请求。Agent可调用工具检测目标、追踪相关代码路径，接收附带证据与适用边界说明的分析结果。基于返回结果，Agent还可进一步提问，或编写、测试对应的实现方案。

针对原生二进制文件，REA可返回伪代码、汇编指令、字符串、符号、函数调用及引用关系。这些结果能帮助研究人员将软件的可见功能，与背后的代码逻辑直接关联。用户要开展深度原生分析，需预先在设备上安装Ghidra、IDA Pro或Hopper；安装流程可在获得用户许可后，自动部署Hopper。

这种实现思路延续了此前Ghidra逆向相关报道中提到的工具定位。REA是在现有分析流程上新增Agent交互接口，并不会替代底层代码检测环节的价值。

基于JavaScript与Electron目标，该工具可映射模块、导入项、源码映射、路由及应用进程间的通信逻辑。静态.NET检测可提取元数据、中间语言指令及声明的原生依赖项，这两类工作流均不需要原生分析引擎支持。

Part02

REA支持多款主流AI编码客户端

用户安装对应版本的Node.js与npm后，可通过npx rea-agents setup命令启动安装流程。安装程序会引导用户选择要对接的Agent，查看配置变更并确认注册操作。

确认后流程会自动安装匹配的工作流指令，备份现有配置。部署完成后用户需重启对应Agent，配置就可以生效。

目前支持一键配置的客户端包括Claude Code、Cursor、Codex、Gemini CLI、Grok Build。其他支持本地MCP服务器的客户端，可通过手动方式完成注册。REA官方代码仓库提供了详细安装说明，并注明平台支持范围取决于用户选择的分析提供商。

Part03

REA公布多场景还原案例

该项目的公开示例展示了基于证据的还原流程实际效果。在DX-Ball案例研究中，工具还原的声音定位计算逻辑，与原始x86代码比对通过了3205项测试，完整复现了全部63个编译函数字节。另一项示例追踪了Notion的剪贴板处理逻辑，覆盖Electron渲染层、预加载层与主进程全链路。

这些都是项目方自行公布的演示效果，并不代表所有目标都能被完全还原。相关案例可作为此前AI辅助XLoader恶意软件分析报道的补充，此前研究人员开展同类分析时，会将模型输出与运行时检测结果结合验证。

REA在本地完成目标分析，但分析结果会传输给对接的Agent。这些结果的处理仍需遵循模型服务商的数据政策，因此本地执行不代表所有分析数据都会留存于本地设备。

静态JavaScript与.NET检测模式只会读取文件，不会运行应用。但运行时捕获模式会以用户权限启动目标程序或与其交互，研究人员分析可疑软件前，必须先明确两种模式的差异。

尽管REA的命名意为“逆向万物”，但它仍存在目标、平台与依赖层面的限制。其核心价值在于打通分析提问与可检测代码、可验证结论之间的链路，同时始终将证据留存、操作授权与人工审核作为工作核心。

参考来源：

REA Tool Connects Claude Code and Cursor to Ghidra and IDA Pro to Reverse Engineer Anything

https://cybersecuritynews.com/reverse-engineer-anything-tool/

###

### **推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0YicFBBV16wQdPW4H8cTibDhNEfda7XWQYxJejxMQXMkmUHx6wDDLARUIbdeicO6WQyTRZN8jBRKSbL2bT8srvaRb0FMGv7DXJU8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651348384&idx=1&sn=b0d043fbf6f272983df964e3f249232e&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3mETrvTp1xSWg4nsaY8jdaRdeta9l692aSBiaWUg95sD0gVn7BiaQ6bng5NuFFmERdoTibOtYlCXD4z0Fsus60Vbx1ExXibLicvq4s/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

预览时标签不可点

阅读原文

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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