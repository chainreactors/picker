---
title: 安全工具丨一个轻量 C2 框架覆盖「生成载荷 → 会话管理 → 任务执行」的完整链路。红队演练、渗透测试开箱即用。
url: https://mp.weixin.qq.com/s/bNJoqHvPYkVwB4hCba8bUA
source: Doonsec's feed
date: 2026-09-15
fetch_date: 2026-09-16T07:03:54.866390
---

# 安全工具丨一个轻量 C2 框架覆盖「生成载荷 → 会话管理 → 任务执行」的完整链路。红队演练、渗透测试开箱即用。

# 安全工具丨一个轻量 C2 框架覆盖「生成载荷 → 会话管理 → 任务执行」的完整链路。红队演练、渗透测试开箱即用。

原创

蓝星安全
蓝星安全

蓝星安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**点击上方****蓝星安全****关注我**

**免责声明：本公众号分享的任何资料仅限用于安全学习，严禁用于其他用途，请严格遵守中华人民共和国法律法规，对因不遵守国家法律法规而产生的任何后果，均由个人自行承担，本公众号不承担任何责任！**

**获取资料，请扫码下方二维码加入知识星球**

![](https://mmbiz.qpic.cn/mmbiz_png/opKHaHXLxcmxg12rU33pwcICNRkiaof5YSUAGfWPApU7M1BfdsTTOyvREw0gKD42g4U8eefG4n0XuYETEtbxSIN2drACnNVz3UeicCcldM5AA/640?wx_fmt=png&from=appmsg)

## 一、简介

  ToShell 是一个自托管的 C2 远程管理平台，明确面向“授权红队演练、渗透测试与安全研究”场景，并在 README 中强调仅限获得授权后使用。

架构上，ToShell 由三部分组成：

* **服务端（Team Server）** ：核心控制节点，负责会话管理、任务调度和载荷生成；
* **Web 控制台**：可视化操作界面，集成仪表盘、会话管理、文件操作等功能；
* **多平台植入端**：覆盖 Windows / Linux / macOS，支持 exe / dll / raw / shellcode 多种载荷格式。

这套架构覆盖了从“生成载荷”到“会话管理”再到“任务执行”的完整链路，而最值得关注的设计是**单二进制部署**——整个服务端就是一个可执行文件，无需安装任何依赖服务，直接运行即可启动。

![](https://mmbiz.qpic.cn/mmbiz_png/opKHaHXLxcl5WyeOf5p34rOo2m8DAOV8dzz2ow92iaT4njSk0xvfObhH8IwibFZUKurjCJIIyoya6Jv723I1FmibcXz6yvZxw56qRN5JnEr2H8/640?wx_fmt=png&from=appmsg)

## 二、核心功能

### 2.1 多通道回连与跨平台载荷

C2 框架的生命力首先取决于通信通道的多样性与隐蔽性。ToShell 提供了四种回连通道：TCP、HTTP(S)、WebSocket 和 MQTT。其中 HTTP(S) 通道支持域前置和 TLS 拟态，适合模拟正常流量以提升隐蔽性。植入端覆盖 Windows、Linux、macOS 三大平台，并支持 `full` 和 `light` 两种载荷档案，兼容较老的操作系统（基于 Go 1.20 工具链）。

![](https://mmbiz.qpic.cn/mmbiz_png/opKHaHXLxcmaW2IGBTYQHEuNWzvcqrpvxJS0ibJa8ibAnQiciaOTqLFnskkJaqRiaQ3fXX7HAVyrXzOdJdTfoungACNZRnosLfmIWyJYNpqxYKWI/640?wx_fmt=png&from=appmsg)

### 2.2 全功能会话操作

会话建立之后，ToShell 提供了一套完整的操作能力：交互式 Shell、目录与文件管理（上传、下载、删除、在线预览，支持断点续传）、进程枚举/注入/杀死。此外还集成了截图、实时屏幕流、凭据收集、UAC 提权、持久化，以及文件无落地执行和 BOF/DLL/EXE 插件加载。这些能力基本覆盖了红队日常作业中对目标主机的主要操控需求。

![](https://mmbiz.qpic.cn/mmbiz_png/opKHaHXLxckR74SDGuutYe6WUqibVyUHRSxlrWcAAzEWHSDMoIQkXrtSyRWrXsAySorQWnA92t92EiagrhITazXspdfvKtOMUvcKvlJOPyxLo/640?wx_fmt=png&from=appmsg)

### 2.3 组网与隧道

在横向移动和内网渗透场景中，ToShell 支持 **Beacon Mesh 多跳中继**和 **SOCKS5 隧道代理**，中继链路全程加密。这意味着即使目标网络存在多层隔离，也可以通过中继节点建立稳定的访问通道。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/opKHaHXLxcmHotibfVTiaKN6raa5bV7UxmayDslql2csH2cabCBIWZHoWEST9roHFp4JmqLnMvwUH1CibETBJl4N3VMouEw2z78XDsxicmeKLWA/640?wx_fmt=png&from=appmsg)

### 2.4 AI 副驾驶与自主 Agent

这是 ToShell 区别于传统 C2 框架的核心差异化能力。**AI 副驾驶**支持联网搜索、远程下载工具、按用途进行插件/内存加载、任务结果分析并给出下一步建议，同时对影响会话的操作设置了权限审批机制。**自主 Agent** 则更进一步：支持异步自主执行（不阻塞对话）、SSE 流式思考过程可见、连续上下文记忆，能够在授权范围内自主完成提权或横向移动的闭环操作，失败时自动恢复，最终只输出结论与建议。从设计思路上看，ToShell 试图将 AI 从“辅助查询工具”升级为“可委托的执行主体”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/opKHaHXLxcm5p0FKOJcu5Tl8ic5hzib09WrkjkIFrZTmicloh1HYjByQCtDhmLyl6VuYqLQLtaUzTCMcicfgu8eJA3sywDPX8hDbWxxgk10RU3A/640?wx_fmt=png&from=appmsg)

### 2.5 免杀与隐蔽设计

在对抗检测方面，ToShell 采取了多层策略：每次构建时随机化配置块魔数、密钥和 API 哈希种子，编译期进行字符串混淆，运行时通过 apihash 和 PEB 动态解析 API，并内置反沙箱机制和启动随机延迟。进程注入时随机选择良性宿主进程，进一步降低被识别的概率。

![](https://mmbiz.qpic.cn/mmbiz_png/opKHaHXLxclibNSt8c1dHXzlwSibv1iaZ1ibuxeTBsVJOgASFNDQrV434cWGmSMD29j34YOkPjzxCab0KmibADE23a9BQ3szF8hrEpT9A37hScUQ/640?wx_fmt=png&from=appmsg)

三、立即获取

https://github.com/iQingshan/Toshell

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/s3lScxtIeTuH1icn4iaremWj4s4jciasuCyiaXXFyGvyWN1E2jVRhP7B10QsXqSPkwnjYrrguSxpj0QKV4sD7fZmBw/0?wx_fmt=png)

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