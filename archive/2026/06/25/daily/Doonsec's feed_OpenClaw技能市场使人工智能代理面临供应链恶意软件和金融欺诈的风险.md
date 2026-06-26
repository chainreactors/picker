---
title: OpenClaw技能市场使人工智能代理面临供应链恶意软件和金融欺诈的风险
url: https://mp.weixin.qq.com/s/oTLr6_s5kWBfoN16dVi6Dw
source: Doonsec's feed
date: 2026-06-25
fetch_date: 2026-06-26T06:06:03.847024
---

# OpenClaw技能市场使人工智能代理面临供应链恶意软件和金融欺诈的风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7MvWHmGzePibrcxLs3uBZ9sWC0K2C8Ciaibahl5pLeooO4aYYD8WW0yyuJm6AlPgwnLDYKvvDqBjRTK0aU56bRnpQ1md9IXngcib5U/0?wx_fmt=jpeg)

# OpenClaw技能市场使人工智能代理面临供应链恶意软件和金融欺诈的风险

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

针对 OpenClaw AI 代理市场的恶意技能浪潮暴露了软件供应链安全领域一个危险的新前沿。

攻击者利用 ClawHub 技能市场将有害代码推送到 AI 代理环境中，窃取数据并实施金融欺诈计划，而传统的安全工具未能发现这些计划。

OpenClaw 是一款人工智能代理，它运行来自第三方技能库 ClawHub（一个专门的技能交易平台）的技能。这些技能是以 Markdown 为基础的软件包，拥有对本地系统的深度访问权限。

当恶意技能被安装后，它可以完全控制代理的身份，并通过代理自身的已认证会话执行未经授权的操作，而无需传统的漏洞利用。

Unit 42 的研究人员在一份与网络安全新闻 (CSN) 分享的报告中表示，他们在 2026 年 2 月至 5 月期间的分析发现了五种恶意技能，这些技能绕过了 ClawHub 集成的 VirusTotal 和 ClawScan 筛查。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7N5t0Aqf1X15icV9gQWpvqM8MSeFKaJFkm21ticDnIJFnVQ0oXbZLaE6k2ibzswCCNJ0q6VvPqoR6xU0ibHdNDQeodnl62NhxTtsxs/640?wx_fmt=png&from=appmsg)

这五起事件均被举报处理，相关账号随后被封禁。

这五种技能分为三类威胁：与命令和控制基础设施相连的信息窃取者、旨在突破扫描器阈值的文件填充规避工具，以及两种为获取经济利益而构建的新型代理威胁。

Bitdefender Labs 此前曾指出，该平台上约 17% 的技能携带恶意载荷，而 Koi Security 的 ClawHavoc 披露记录了市场上的 341 个恶意技能。

即使在引入自动筛选之后，这些威胁仍然存在，这表明人工智能代理生态系统面临的风险远未得到解决。

核心问题是恶意技能利用自然语言劫持人工智能自身的指令遵循行为，绕过了保护更传统软件环境的防护措施。

## **OpenClaw技能市场公开人工智能代理**

五项威胁中有两项是伪装成 TradingView macOS 生产力助手的技能。

两者都嵌入了一个恶意的前提条件块，该块将代理程序引导至 rentry[.]co/openclaw-code 上的粘贴站点重定向诱饵，该站点上有一个 Base64 编码的命令，等待在终端窗口中运行。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7PmMcHWn4LuZOFZl2sZZ1aE9rA7eOK23icnT4VXibJRuPoIezyvoic3wVj1WvicMjEtOaJFuIxia9Sb6udQT4yOBYdeb9LZUoGhIyQ4/640?wx_fmt=png&from=appmsg)

然后该命令从 2.26.75[.]16 的远程服务器拉取了一个名为 cluw 的 macOS 信息窃取程序。

一个名为 omnicogg 的独立技能将 AMOS 恶意软件投放器嵌入到 README.md 文件中，然后用 22 MB 的垃圾字符填充该文件，以超过大多数扫描管道强制执行的文件大小限制。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7PN11dn7QWBz7346AicTtfTOnF8uldlIEQsY8UiaiasODDsr8ZaAzxkaXcnic6I1R9qDaBX6uMtZSjOoZPGIrQ53dxVsKknTHAicTtk/640?wx_fmt=png&from=appmsg)

VirusTotal 和 ClawScan 都给出了干净的判定结果，这意味着该技能在隐藏恶意代码的同时仍然可以自由使用。

这些技能都模仿了某种合法工具。TradingView 的技能看起来像是交易员效率提升工具，而 omnicogg 则伪装成通用实用程序。

攻击者利用用户对精选市场的信任，使得自动化工具和人工审核人员都难以检测到攻击者的行为。

## **代理人金融欺诈和新型剥削**

除了数据窃取之外，研究人员还发现了两种滥用人工智能代理的咨询权限以谋取经济利益的技能。其中一种名为“金钱雷达”的技能伪装成金融产品顾问，服务于中国大陆、香港和新加坡的用户。

每次调用时，它都会默默地从 laosji[.]net 获取有效载荷，并将联盟跟踪链接嵌入到它生成的每个推荐中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7NOwzU90SmDTXhqxScXjCHWyZX4MhA8sQ0XVfqvF9wXbyqjCSsRzhPsNaZPwRu3QSP911jhO1313qduVBd5kPE2vq2eQQ4BUSo/640?wx_fmt=png&from=appmsg)

运营商可以在用户不知情的情况下随时更换推荐产品。letssendit 技能更进一步，在 Solana 区块链上运行了拉高出货骗局。

安装的代理将 SOL 加密货币汇入运营商的钱包，之后运营商以最低可用价格购买了 SENDIT 模因代币，然后在 pump[.]fun 上推出。

外部买家可能会将人工智能协调活动误认为是自然需求，从而使运营商能够以低价将持仓抛售给二级买家并从中获利。

这些案例是首次有记录的利用自主人工智能代理进行协同金融欺诈的案例。

研究人员建议验证发布者的来源，逐行审核技能源文件，并监控出站网络流量，以查找与未记录的端点的连接。

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