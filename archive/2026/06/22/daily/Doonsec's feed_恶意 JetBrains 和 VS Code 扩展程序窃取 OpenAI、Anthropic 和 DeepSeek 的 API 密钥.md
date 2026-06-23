---
title: 恶意 JetBrains 和 VS Code 扩展程序窃取 OpenAI、Anthropic 和 DeepSeek 的 API 密钥
url: https://mp.weixin.qq.com/s/P8t2xdoCbgRouhlhwzYMAA
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:03:54.890401
---

# 恶意 JetBrains 和 VS Code 扩展程序窃取 OpenAI、Anthropic 和 DeepSeek 的 API 密钥

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7Nt8KGHqz2eqhjzjP17aLpgnU5XIQgJKulyw2jwbE6TWTIBFiaDJnpc8klFhAJDbounOxcKopnVOEB89lFldnIhDTuGmp64oib38/0?wx_fmt=jpeg)

# 恶意 JetBrains 和 VS Code 扩展程序窃取 OpenAI、Anthropic 和 DeepSeek 的 API 密钥

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

依赖人工智能编码工具的开发者如今面临着一种严重的新威胁。JetBrains 应用市场被发现存在协同恶意软件攻击活动，至少有 15 个虚假的 IDE 插件悄悄窃取了数千名开发者的人工智能提供商 API 密钥。

这些插件伪装成基于 DeepSeek、OpenAI 和 SiliconFlow 构建的实用 AI 编码助手，但在其表面之下隐藏着危险的凭证窃取程序。

此次攻击持续了大约八个月，最早的恶意插件出现在 2025 年 10 月下旬，而新的插件直到 2026 年 6 月 10 日仍在发布。

在被发现之前，这15款插件在七个供应商账户中累计安装了近7万次。此次攻击活动的规模和持续时间凸显了开发者对应用市场生态系统的信任程度，以及这种信任极易被恶意利用。

Aikido Security 的研究人员率先发现并公开披露了此次攻击活动。云安全联盟 (CSAI) 在一份与网络安全新闻 (CSN) 分享的报告中指出，集成开发环境 (IDE) 插件生态系统已成为人工智能凭证窃取的主要攻击面，并强调供应链完整性控制措施尚未扩展到这些环境。

所有三起有记录的攻击活动都证实，开发者工具链现在已成为一个公认的、并被积极利用的目标。

除了 JetBrains 攻击活动之外，研究人员还追踪了同一时期发生的两个相关威胁。

GlassWorm蠕虫病毒的目标是Visual Studio Code Marketplace和OpenVSX注册表，而另一起Nx Console供应链入侵事件则攻击了GitHub的内部代码库。这两起事件共同反映了攻击者将开发者工具作为高价值攻击入口点的普遍趋势。

由于涉及巨大的经济利益，这些攻击尤其具有吸引力。人工智能推理成本高昂，企业客户每月需支付高额的模型使用费。

被盗的 API 密钥可以让攻击者零成本消耗该配额，而合法所有者却要继续支付费用，从而催生了不断增长的 AI 访问权限转售黑市。

## **恶意 JetBrains 和 VS Code 扩展**

所有 15 个恶意插件都使用了几乎相同的代码，只是重新打包并以不同的名称和供应商账户重新上架。

当开发者将 API 密钥输入到插件设置中并点击“应用”时，凭据会按预期存储在本地，但同时也会通过普通的 HTTP POST 请求转发到硬编码的攻击者控制的服务器。

界面上既没有出现任何通知，也没有出现任何同意屏幕。Aikido 的分析还揭示了一个货币化层面，这使得此次活动与普通的凭证盗窃有所不同。

有些插件提供付费版本，用户支付少量费用后，攻击者的服务器就会向客户端返回一个可用的 API 密钥。

研究人员认为，这些归还的密钥很可能是从免费套餐的受害者那里窃取的，这使得该攻击活动变成了凭证转售服务，攻击者从中既获得了金钱，又获得了免费的 AI 计算能力。

## **GlassWorm 和更广泛的 VS Code 风险**

GlassWorm 是一种技术先进的威胁，由 Koi Security 于 2025 年 10 月首次发现，它通过 OpenVSX 注册表上的恶意 VS Code 扩展程序传播。

它利用不可见的Unicode字符将恶意逻辑隐藏在扩展程序源文件中，使得代码对人工审核人员和自动化工具而言都显示为空行。这种技术使得恶意软件能够绕过大多数标准审核流程而不被发现。

GlassWorm一旦激活，就会窃取GitHub令牌、npm令牌、OpenVSX令牌和加密货币钱包数据。然后，它会将恶意提交强制推送到受害者账户可以访问的每个代码仓库，从而将感染传播给之后克隆这些代码仓库的任何开发者。

2026 年 5 月 26 日，CrowdStrike 与 Google 和 Shadowserver 基金会合作，摧毁了所有四个 GlassWorm 命令和控制通道。

开发人员应立即审核所有已安装的 JetBrains 插件和 VS Code 扩展，并将任何输入到未经审核的插件中的 API 密钥视为完全泄露。

OpenAI、Anthropic、DeepSeek 和 SiliconFlow 的密钥应立即在其各自的提供商控制面板中撤销和轮换。

网络团队应阻止流向攻击者服务器的出站流量，组织在批准新的 IDE 插件之前，应要求进行行为审查，而不仅仅是静态代码扫描。

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