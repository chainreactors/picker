---
title: Lazarus 利用带有后门的编码测试引诱开发者
url: https://mp.weixin.qq.com/s/Stjq9b8VzREZhplg0yRyHQ
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:51:32.022782
---

# Lazarus 利用带有后门的编码测试引诱开发者

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7Psia5AyhRqtXzZicx9gnKdNhbndPibg15sy4gEk0QKOSgz49776y2EepcnRyB5kNaNc8qjn9L8WkByu9B5gQNIOAosKia8Ipzg3Ag/0?wx_fmt=jpeg)

# Lazarus 利用带有后门的编码测试引诱开发者

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

与朝鲜有关联的黑客正在利用人工智能辅助恶意软件和带有后门的编码挑战，悄悄地从 Web3 开发人员那里窃取数百万美元的加密货币。

Expel 高度确信 HexagonalRodent 是一个由朝鲜民主主义人民共和国政府支持的子组织，该组织很可能是从欺诈性 IT 工作者运作演变而来，之后才完全转向恶意软件驱动的盗窃活动。

短短三个月内，该组织就从 2726 个受感染的开发者系统的 26584 个加密货币钱包中窃取了数据，导致高达 1200 万美元的资产暴露，不过硬件安全代币似乎限制了损失。

虽然出于经济动机，但这些运营者与其他与 Lazarus 结盟的 APT 组织（例如 Famous Chollima）共享工具、技术技巧和基础设施模式。

该活动集群被追踪为 Expel‑TA‑0001，昵称为 HexagonalRodent，似乎是更大的 Lazarus 生态系统的一个子群，其重点是窃取数字资产，而不是传统的间谍活动。

该组织主要依赖三个恶意软件家族：BeaverTail 和 OtterCookie，它们都是基于 NodeJS 的多用途工具包，具有窃取密码、文件访问和反向 shell 功能；以及 InvisibleFerret，一个基于 Python 的反向 shell。

## **后门编码测试**

HexagonalRodent 的主要攻击手段是通过在LinkedIn 等平台和加密货币小众招聘网站上发布虚假的高薪工作信息，来诱骗 Web3 开发人员进行社会工程攻击。

一旦目标人物参与进来，“招募者”就会发送一份托管在 Git 平台上或以项目存档形式存在的居家编程评估，它看起来像是一份普通的技能测试，但实际上却隐藏着后门。

一种关键技术是滥用 VS Code 的 tasks.json 配置文件，预加载一个带有 runOn: “folderOpen” 的恶意任务，这样当受害者在 VS Code 中打开项目文件夹时，恶意软件就会自动执行。

对于使用其他编辑器或安全模式的开发者，额外的后门会直接嵌入到挑战代码中，在构建或执行项目时触发。

一旦激活，该恶意软件就会连接到基于 NodeJS 的命令与控制 (C2) 基础架构，从而实现凭证窃取、钱包窃取和完全远程控制。

与 Stardust Chollima 或 Pressure Chollima 等更精准的朝鲜组织不同，这些组织主要渗透大型交易所和金融科技公司，而 HexagonalRodent 则专注于对个人开发者和小型 Web3 项目进行大规模的攻击。

Expel 没有发现企业网络内部横向移动的证据；相反，攻击者专注于直接从开发者终端窃取浏览器保存的密码、助记词和钱包数据。

2026 年 3 月，该组织通过破坏Open VSX 生态系统中的“快速草稿”扩展程序，并利用该程序分发 OtterCookie 恶意软件，从而进入了供应链领域。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7PaKztSwJcHMzGJc691uah9NibUH5RibPJSkZTvUqmoqAbEPufbCjUyLHtd5rbAetOEiaMBnVhZ61pR9e0uM4luiagnaZxvq3YSnJw/640?wx_fmt=png&from=appmsg)

遥测数据将该扩展程序的 C2 服务器 195.201.104[.]53 与 OtterCookie 基础设施关联起来，而该基础设施此前已被归咎于 HexagonalRodent。Expel 确认，在恶意更新上线前几天，与扩展程序作者匹配的帐户已被感染。

Expel 的调查显示，HexagonalRodent 在其运营的各个方面都深度投入了生成式人工智能，从编写恶意软件加载程序到完善网络钓鱼诱饵和构建虚假公司网站。

这些虚假的高管名单会列在公司的 LinkedIn 页面上，而且通常也会列在公司的网站上。

遥测数据将该组织与 ChatGPT 和 Cursor 的使用联系起来，两家供应商均证实，他们在收到通知后阻止了已识别的帐户，并且发现的主要是“双重用途”的安全和开发查询，而不是大规模的自动化恶意软件生成。

2025 年人类学报告还记录了与朝鲜民主主义人民共和国有关联的人员试图注册 Claude 帐户，据称是为了改进 BeaverTail、OtterCookie 和 InvisibleFerret，尽管这些帐户在提交任何提示之前就被封禁了。

## **团队规模的工业化钱包盗窃**

通过逆向工程多个基于 ReactJS 的 C2 和管理面板，Expel 重建了 HexagonalRodent 的内部结构和工作流程。

我们发现的下一个面板是一个基于浏览器的远程控制实用程序。它为攻击者提供了类似 VNC 的功能（能够查看受害者的屏幕，以及控制其键盘、鼠标和剪贴板）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7N1N6se83ngvoNmGUZw2DCSbV5xBY8X85mBg1V9w56ag9yAHPibM93Po0Oic6h4nQprsU84MjTpYUpAiaEtpga7nRyT4yiaKj6d36w/640?wx_fmt=png&from=appmsg)

Expel 还观察到，一些行为者促使商业 AI 模型“审核”他们自己的后门编码评估，这很可能是为了使其他使用AI 辅助代码审查的开发人员更难发现这些评估。

这些面板包括实时信息窃取视图、类似远程桌面的控制、基于浏览器的文件资源管理器，以及一个“工作流”仪表板，用于跟踪每个操作员和团队的加密钱包和余额。

OtterCookie 示例中的硬编码字段（例如 t（团队 ID）和 userKey（成员标识符））与面板逻辑一致，该逻辑按团队和系统主机名对钱包进行分组，表明至少有 6 个活跃团队和 31 个不同的活动 ID。

有趣的是，其中一个面板的功能似乎与其说是 C2，不如说是劳动力跟踪器，它按钱包收入对“6team”、“7team”和“101team”等团队进行排名，并显示所有运营商的“管理员”视图，这与有关朝鲜民主主义人民共和国更广泛地使用绩效仪表板来监控欺诈性 IT 工作者的报道相呼应。

2026 年 1 月 1 日至 3 月 31 日期间，这些团队窃取了价值高达 1200 万美元的钱包公钥，并确认至少有 13 个受害钱包的资金流入一个已知的朝鲜控制的以太坊地址，该地址自 2023 年以来已收到超过 110 万美元。

目前来看，HexagonalRodent 的人工智能辅助 Lazarus 攻击手段表明，相对简单、嘈杂的恶意软件，如果能够实现工业化、自动化，并结合令人信服的社会工程手段，仍然可以对 Web3 生态系统造成重大的经济损失。

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