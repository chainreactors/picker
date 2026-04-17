---
title: AI工作流自动化平台n8n正被大规模网络武器化
url: https://mp.weixin.qq.com/s/fR076c00nrJQFMkCmsAMSA
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:42:36.051757
---

# AI工作流自动化平台n8n正被大规模网络武器化

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDoXnp6snSxJPgYZU7riaoE2yzfDCKE5JAHialr1p9GfLpYC6vqOktX7eiauYgPAQ799ChnqoG3NQNH4sL5c9RPqPlSLnbCxehhQSQ/0?wx_fmt=jpeg)

# AI工作流自动化平台n8n正被大规模网络武器化

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

随着大语言模型和智能体 AI 技术的快速发展，低代码 AI 工作流自动化平台已经成为企业提升效率的核心工具。这类平台能够快速连接各类办公软件与 AI 模型，实现业务流程的自动化处理。

n8n 是全球最受欢迎的低代码工作流自动化平台之一。它支持连接所有基于 HTTP API 的网络应用和服务，包括 Slack、GitHub、Google Sheets 等常用工具。用户可以通过可视化界面搭建自定义自动化工作流，无需编写大量代码。平台同时提供可自行托管的社区许可版，以及托管于 n8n.io 的商业服务。商业服务内置 AI 驱动功能，能够创建智能体自动调用网络接口，从文档和各类数据源中提取数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrdHnusd0Vhn6MojRfnKkuhDsKQEKW2uA8xa6A3DOeVo573BQDKrmRrFqeFic8kzYAiaVc3ZN2gU0xVmQS6nnwgwy0hADQmAFA4M/640?wx_fmt=png&from=appmsg)

思科最新研究显示，这类合法生产力工具正被威胁行为者大规模武器化。2025 年 10 月至 2026 年 3 月期间，滥用主流平台 n8n 发起的网络攻击呈现爆发式增长。2026 年 3 月含 n8n 恶意链接的邮件总量，较 2025 年 1 月上涨约 686%。攻击者利用平台的可信基础设施绕过传统安全防护，将其转化为投递恶意软件和实施用户追踪的攻击载体。

n8n 的免费开发者账号机制是其被滥用的核心基础。用户无需支付任何费用即可注册账号，注册后会获得一个专属子域名，格式为 xxx.app.n8n [.] cloud。所有用户创建的工作流和应用都可以通过这个子域名访问。

n8n 平台最主要的滥用点是其通过 URL 暴露的 Webhook。Webhook 也被称为反向 API，它允许一个应用向另一个应用推送实时数据。这些 URL 会将对应的应用注册为监听器，接收外部请求并返回数据。返回的数据可以包含动态生成的 HTML 页面、文件流等任意内容。

 n8n Webhook URL 结构：

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDouqoibicVKXXsjTGZKQeYGJXfp8UfaiaJJ6sCjiczblyibIEGiaBpHm6PdYSSVs6QS9iaNJXKWyITzw15h8qqibk4TOItex1RHwUwa5CI/640?wx_fmt=png&from=appmsg)

https://[用户账号].app.n8n.cloud/webhook/[工作流唯一ID]

当用户访问一个 n8n Webhook URL 时，平台会自动触发预设的工作流步骤，并将执行结果作为 HTTP 数据流返回给用户的浏览器。

浏览器会将返回的内容直接渲染为网页。这种机制的核心特性使其成为完美的攻击跳板。

它能够完全掩盖数据的真实来源，让从恶意服务器拉取的内容看起来完全来自可信的 n8n 域名。

同时 Webhook 还能根据请求头信息动态返回不同内容，攻击者可以针对不同的浏览器和操作系统定制攻击载荷。

基于上述原理，攻击者发送伪装成 Microsoft OneDrive 共享文件夹的钓鱼邮件，邮件正文中嵌入 n8n Webhook 链接。邮件主题通常使用 “审核文档”“重要文件共享” 等具有迷惑性的标题，诱导收件人点击。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDo8qHymDiaM2GU6rDPDsLRSsMuiclU6pfh0ictHNAjxSnT1RbAo145kSoFBZ8IUUbAfTpH9ZnEbZOCxL1W2kFMSgEkwiavbnDQyp5Q/640?wx_fmt=png&from=appmsg)

受害者点击链接后，浏览器会跳转到 n8n 域名下的验证码页面。完成验证码验证后，页面会显示下载按钮和进度条。后台会从外部恶意服务器拉取恶意载荷。由于整个下载过程完全封装在 HTML 页面的 JavaScript 代码中，浏览器会认为文件来自 n8n 域名，从而绕过绝大多数静态安全检测。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrbrs740vnZeSTHgzm3Q8G3icgtEsXwOGsoosv0HKwjQ6ZjuliaOr8iadfdDUTj3gBoZB47w1dIfMLcPfyZ9dnZGMgh39j7avCias8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDohCwuChmwiaJbibOxMpZvD9sxCibtTXACiaxKLnhgiaIuFWNy15nzG4gcwoiacOApNZBQkt5tbFnhJzPgdwibJQia6Oaz2BTQbOkv5NTM/640?wx_fmt=png&from=appmsg)

目前有两类主要的恶意载荷。第一类是伪装成自解压归档文件的 NSIS 可执行文件，文件名为 DownloadedOneDriveDocument.exe。用户运行后，它会安装篡改版的 Datto 远程监控与管理工具，并执行一系列 PowerShell 命令。这些命令会将 RMM 工具配置为系统计划任务，实现开机自动运行。随后工具会连接到攻击者控制的中继服务器，建立持久化远程访问。最后脚本会自毁并删除所有载荷文件，清除攻击痕迹。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDq8DEDG5c7T6IaqxEqGel0p1lKaVx1ahSm9JI5OAXM6gicu1NlKocTIb6AhbXrdodpOAG0Z38Nbqib0dtJUnYzn2zJpibJ61GtK3M/640?wx_fmt=png&from=appmsg)

第二类载荷是加壳的 MSI 安装包，文件名为 OneDrive\_Document\_Reader\_pHFNwtka\_installer.msi。该文件采用 Armadillo 反分析加壳保护，部署的是篡改版的 ITarian 端点管理 RMM 工具。当系统执行该安装包时，前台会显示虚假的安装进度条。后台则会安装 RMM 后门并运行 Python 模块，窃取系统信息。安装完成后进度条会重置为 0% 并自动退出，制造安装失败的假象迷惑用户。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqRODCGyykF5NEodjicpPDUlW8dS2MyRUAZZRE5oqXw5Kic5sMbMFaCs3fubicC8UiatdMUPT6LDqoBssIxsK6sT9nFJA8DBIPOickI/640?wx_fmt=jpeg&from=appmsg)

除了投递恶意软件，n8n Webhook 还被广泛用于邮件打开追踪和设备指纹识别。攻击者的实现方式非常隐蔽。他们会在邮件中嵌入一个 1x1 像素的透明图片，将图片的源地址指向 n8n Webhook URL。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpRonuQ2XY0iatibc7POAQaHxEnOFzo8EjEc9gng7maLoVP5KK3aiaQCfBiashicISeibSjmSRZMfgovG5wCicZBqpnLTVQ8ZB4FumHCg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDqeib0zx4HkHABe3WFNeMeKrh0m1b8WAPTUebcAkicJBJfIgQs5rcTKJbM2GYicITOqX1kuolE4Pt6q5q2uEdicFtuk5IRBwzIKocs/640?wx_fmt=jpeg&from=appmsg)

当邮件客户端自动加载图片时，会向 n8n Webhook 发送一个 HTTP GET 请求。Webhook URL 中会携带受害者的邮箱地址等唯一追踪参数。攻击者可以通过这些参数精确知道哪个用户打开了邮件。同时请求头中包含的浏览器版本、操作系统类型、IP 地址等信息，会被攻击者收集用于构建设备指纹。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrtxv2hbr2icFGSJRjsliarN5MpwpjiaqfricTcW8XgHo8n2dlfwzZYH0VfHew9G76PRf1ZC5fxSqxUiajpHQiaoHm5k3XFFcIBX5Gko/640?wx_fmt=png&from=appmsg)

攻击者通过 CSS 属性将追踪图片设置为完全不可见。用户在阅读邮件时完全无法察觉自己已经被追踪。Talos 已监测到西班牙语、英语等多语言垃圾邮件使用该技术，诱饵内容涵盖礼品卡促销、日常问候等多种类型。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDohPMHu3DEiaGTbKhiaChqNqr5h36iaUKcXlWeBxCpmG0x8Y0PicQyXA7sPvtaTZjOelicYm8o0pR13dRSWJ0eaDV7GGpwmUC1dh7Yo/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpRsavUa5zZMIkczrgqYVicBOWicto5RO5q7VCjM644SGxib3UFkJ5n5rehr0USJ8Rs9Zjpvlc9E0IImpw2Lc9DIj4zzgFGTpial80/640?wx_fmt=png&from=appmsg)

由于 AI 工作流自动化平台已经被广泛应用于合法业务流程，单纯拦截整个平台域名会严重影响企业正常运营。传统的静态特征匹配也无法有效检测这类利用可信基础设施的攻击。

可以部署基于行为的检测规则来应对这类攻击。安全团队应重点监控以下异常行为。内部非授权 IP 向 n8n 平台发送大量流量。端点尝试与未纳入企业白名单的 n8n 子域名通信。从 n8n 域名下载可执行文件或安装包。一旦发现上述行为，应立即触发告警并进行人工核查。

原本旨在为开发者和企业节省时间的自动化工作流技术，如今因其灵活性和易集成性，成为威胁行为者手中的攻击利器。

合法工具被武器化已经成为当前网络安全领域的重要趋势。

随着 AI 自动化技术的进一步普及，类似的攻击还会不断涌现。安全团队必须转变防护思路，从传统的静态防御转向动态的行为检测。同时加强员工安全培训，构建多层次的安全防护体系，才能有效应对这类新型威胁。

IOCs可见：

https://github.com/Cisco-Talos/IOCs/tree/main/2026/04

https://blog.talosintelligence.com/the-n8n-n8mare/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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