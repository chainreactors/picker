---
title: OpenClaw：人工智能代理安全危机正在上演
url: https://mp.weixin.qq.com/s/piPOQF3vkw9ZVPW4gr1YBA
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:30:56.424750
---

# OpenClaw：人工智能代理安全危机正在上演

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7OM2wu8l5dIiaBibVMibQqxrQDYmia4VamXVITaJibbmnnsA5216XUibG9eMF0LTsX1uCQKgtAPCgU9u0wfHAOq0LsdPHG2nT0cXIWoI/0?wx_fmt=jpeg)

# OpenClaw：人工智能代理安全危机正在上演

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

您可能已经听说过 OpenClaw 了。这款开源 AI 代理迅速成为 GitHub 历史上增长最快的代码库之一，短短几周内就获得了超过 13.5 万颗星。然而，它也引发了 2026 年首个重大 AI 代理安全危机。Reco 可以帮助您识别您的环境中是否存在 OpenClaw。

‍

## **OpenClaw现象**

‍

OpenClaw（曾因商标纠纷而更名为 Clawdbot 和 Moltbot）是由开发者 Peter Steinberger 创建的开源人工智能代理。与只能回答问题的传统人工智能助手不同，OpenClaw 具有自主性。它可以执行 shell 命令、读写文件、浏览网页、发送电子邮件、管理日历，并在您的数字生活中执行各种操作。

‍

用户可以通过 WhatsApp、Slack、Telegram、Discord 和 iMessage 等即时通讯平台与 OpenClaw 进行交互。该代理程序在本地运行，并连接到 Claude 或 GPT 等大型语言模型。其“持久记忆”功能意味着它可以跨会话记住上下文，并随着时间的推移学习您的偏好和习惯。

‍

它的吸引力显而易见：一个能代表你采取行动的人工智能助手。人们甚至购买专用硬件，只为全天候运行 OpenClaw。然而，这种能力也带来了严重的后果，而且这些后果很快就显现出来。

‍

## **一系列安全漏洞**

‍

OpenClaw 在短短两周内迅速走红，随后便引发了一系列安全事件，这些事件的范围和严重程度都在不断升级。这些问题涵盖了从传统漏洞到暴露的管理接口，再到恶意技能的传播。单独来看，每一项都令人担忧。而综合起来，它们则表明，拥有广泛系统访问权限的人工智能代理构成了一种全新的风险类别。

‍

### **2026年1月27日至29日 - ClawHavoc**

‍

攻击者通过 OpenClaw 的公共市场 ClawHub 分发了 335 个恶意技能。这些技能使用专业的文档和诸如“solana-wallet-tracker”之类的无害名称来伪装成合法工具，然后指示用户运行外部代码，这些代码会在 Windows 系统上安装键盘记录器，或在 macOS 系统上安装 Atomic Stealer 恶意软件。研究人员随后确认，在 2857 个恶意技能中，共有 341 个受到攻击，这意味着大约 12% 的注册表遭到入侵。

‍

### **2026年1月30日 - 一片宁静之地**

‍

OpenClaw 发布了 2026.1.29 版本，在公开披露之前修复了CVE-2026-25253漏洞。该漏洞允许攻击者通过恶意链接一键执行远程代码。该漏洞利用了 Control UI 对 URL 参数的信任机制，攻击者无需验证即可利用该漏洞，从而通过跨站 WebSocket 劫持劫持实例——即使是那些配置为仅监听本地主机的实例也无法幸免。

‍

### **2026年1月31日 - 大规模曝光**

‍

Censys 发现 21,639 个暴露的实例可通过互联网公开访问，而几天前这一数字仅为约 1,000 个。美国暴露的部署实例数量最多，其次是中国，据估计，中国约有 30% 的实例运行在阿里云上。这些配置错误的实例被发现泄露了 API 密钥、OAuth 令牌和明文凭证。

‍

### **2026年1月31日 - Moltbook漏洞**

‍

就在同一周，专为OpenClaw代理商打造的社交网络Moltbook被发现存在数据库安全漏洞，泄露了3.5万个电子邮件地址和150万个代理商API令牌。该平台拥有超过77万活跃代理商，这表明未经审核的生态系统会如何迅速加剧风险。

‍

### **2026年2月3日 - 全面披露**

‍

CVE-2026-25253 已公开披露，CVSS 评分为 8.8。同一天，OpenClaw 发布了三项影响重大的安全公告：一键远程代码执行漏洞和两个命令注入漏洞。安全研究人员证实，受害者访问单个恶意网页后，攻击链只需“几毫秒”即可完成。

‍

## **这对您的组织为何重要**

‍

这些技术问题本身就令人担忧，但更深层次的问题是，当员工将个人人工智能工具连接到企业系统时会发生什么，而安全团队往往对此毫不知情。

‍

OpenClaw 可与电子邮件、日历、文档和即时通讯平台集成。连接到企业级 SaaS 应用（例如 Slack 或 Google Workspace）后，代理可以访问 Slack 消息和文件、电子邮件、日历条目、云端存储的文档、来自集成应用的数据以及用于横向移动的 OAuth 令牌。

‍

更糟糕的是，代理的持久内存意味着它访问的任何数据都会在会话之间保持可用状态。如果代理随后被攻破（通过恶意技能、提示注入或漏洞利用），攻击者将继承所有这些访问权限。

‍

这本质上是一种拥有更高权限的影子人工智能。员工在未经安全团队知情或批准的情况下，授予人工智能代理访问企业系统的权限，而每次新的集成都会扩大攻击面。

‍

## **在您的环境中识别 OpenClaw**

‍

传统安全工具难以检测人工智能代理的活动。端点安全工具能够检测到进程运行，但无法理解代理的行为。网络工具能够检测到 API 调用，但无法区分合法的自动化操作和恶意入侵。身份系统能够检测到 OAuth 授权，但不会将人工智能代理的连接标记为异常。

‍

**Reco 是少数几个能够检测环境中 OpenClaw 集成的 SaaS 安全平台之一。**

‍

通过 Reco 的插件页面，您可以搜索所有与 OpenClaw 关联的插件。如下所示，如果应用程序与近期真实世界中出现的风险模式升高案例相关，则会被标记为“新兴风险”。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7Nxzlkg88972UGowaNA0f5kPbSADicuHtMcUUqCaibngiaXdYeGtiaQAFk7dricYNVeBX7Wm5tQRqf2aJRPWCwSaJfePUbPfnyQ7npo/640?wx_fmt=png&from=appmsg)

推荐平台：OpenClaw 插件检测

SaaS到 SaaS页面以图表形式直观地展示了 OpenClaw 与企业 SaaS 应用的集成情况。在我们的示例中，您可以看到 OpenClaw 同时被应用于 Google Workspace 和 Slack。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7MehicFzwhW218DibPCLKBhEIzb5tfTibAAtjtpO9aI3dicLD3oGaIHRVCIGjh0QFtOVdyAyH53mkicybQkBNP6ssx11ltiaAZIksXWY/640?wx_fmt=jpeg&from=appmsg)

Reco平台：SaaS到SaaS可视化

将鼠标悬停在虚线上，即可查看授予 OpenClaw 的确切权限和角色。Reco 会自动识别并标记高风险权限，例如 gmail.modify、gmail.settings.basic 和 gmail.settings.sharing，以便安全团队能够快速评估哪些集成对敏感数据构成最大风险：

![](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7PALicEhZcAskFj2Aj6rZOollZEb5AGLh5riaMjnyATYkeJKg9Y4ibibuVbnHSN8BhIsjs7uiaC1rkPlEPCL0ayS9NgRIVpCcukInuA/640?wx_fmt=jpeg&from=appmsg)

Reco平台：OpenClaw权限细分

如果您想获取与相关应用程序相关的更多详细信息，可以使用“事件”窗格：

![](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7OMWic1ae1oPiclicYmhbS3mtSol8qAVvrGtV41llAkFswiaPnbvgDJGSbCYYN31479icRsVhk18Y4ahZ8WEbkApVDC5LpTLBotHWy8/640?wx_fmt=jpeg&from=appmsg)

Reco平台：应用关联事件

这种可见性使安全团队能够识别 AI 代理连接、审核哪些用户已授予访问权限，并在事件发生之前调查潜在的风险敞口。

‍

在调查过程中，Reco 安全研究团队还发现了一个与 Slack 中 OpenClaw 活动相关的特定用户代理字符串：

ApiApp/<SlackAppID> @slack:socket-mode/2.0.5 @slack:bolt/4.6.0 @slack:web-api/7.13.0 openclaw/22.22.0 <操作系统标识符>

‍

可以使用此用户代理直接在 Slack 访问日志中搜索 OpenClaw 连接。具体字符串可能有所不同，但对于希望识别环境中 OpenClaw 使用情况的安全团队来说，这是一个有用的信号。

‍

OpenClaw 不会消失——即使它消失了，对自主人工智能代理的需求也意味着会有另一个项目取而代之。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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