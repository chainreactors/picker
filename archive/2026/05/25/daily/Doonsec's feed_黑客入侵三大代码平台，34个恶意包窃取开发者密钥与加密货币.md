---
title: 黑客入侵三大代码平台，34个恶意包窃取开发者密钥与加密货币
url: https://mp.weixin.qq.com/s/KElGYJwpws5JPaAqwdPrpQ
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T05:59:21.790255
---

# 黑客入侵三大代码平台，34个恶意包窃取开发者密钥与加密货币

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1gMwwpV4GibcHc9Qyaqnooz1HfcErfdvemXribU87pHUL86UuXKWQibMaL1ibOibHu4SnAbOySIjnJogR8V2Eb5CWbCxVuxNrHbHQ4/0?wx_fmt=jpeg)

# 黑客入侵三大代码平台，34个恶意包窃取开发者密钥与加密货币

FreeBuf
FreeBuf

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX1HPcsaMlzv8HEH1hRBS736hicPG5xkTAggHMG52hrgym05EmRSt9FEUd8yHJ4JNJL2V5Qj7PveuI4fLsP6kEpmgpPbF4ia5ePDo/640?wx_fmt=gif)

![微信图片_2026-05-25_155039_036](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2WOjcDo8E9gmPd0XpLl4jT46yAaiaaibeaYKl1fxeoPxFlwqCAIb4nj6usgBwLvef5GPtNyncUplO5qtAicqXNIUgLkM7Gaxg5kM/640?wx_fmt=png)

最新发现的 TrapDoor 供应链攻击活动正在活跃，攻击者通过 npm、PyPI 和 Crates.io 平台部署了 34 个恶意软件包及 384 个相关版本，旨在窃取开发者凭证和加密货币钱包。

Part01

针对性攻击策略

该行动专门针对加密、DeFi、Solana 和 AI 领域的开发者，通过将恶意软件伪装成通用开发工具和安全扫描器实施攻击。最早被发现的攻击组件是 PyPI 软件包 eth-security-auditor@0.1.0，该包发布于 2026 年 5 月 22 日，随后迅速扩散至其他代码仓库。攻击者分批次向三个注册中心上传软件包，使用诸如 prompt-engineering-toolkit、solidity-deploy-guard 和 defi-threat-scanner 等具有迷惑性的名称，在相关开发者社区中伪装成合法工具。

安全公司 Socket 检测到这些 TrapDoor 发布的中位检测时间仅为 5 分 27 秒，在恶意软件被广泛采用前就有效识别了整个攻击活动。

Part02

跨生态系统攻击向量

TrapDoor 活动采用针对不同生态系统的特定执行路径，以最大化其在标准开发者安装和构建工作流程中的影响范围。通过针对特定软件包注册中心定制攻击向量，威胁行为者确保在开发者能够检查底层依赖项之前就实现静默执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1TXYhCsJbyrRRzCNibEtgSAibSibpsIZI8JzWlnicyZZZgkicGj7Jibh9l6zDba42T6vmAhjLYhEydQpAPU2o8G4H5gPYCR3QQOYqnY/640?wx_fmt=png)

Part03

数据窃取与持久化机制

TrapDoor 试图收集大量开发者数据，特别针对 Sui、Solana 和 Aptos 加密货币钱包，同时还包括 SSH 密钥、浏览器配置文件和 AWS 环境变量。共享的 npm 载荷 trap-core.js 包含 1,149 行代码，通过 systemd 服务、cron 任务、Git 钩子和 shell 钩子建立复杂的持久化机制，确保长期访问权限。

此外，被窃取的 SSH 密钥会被重新用于执行自动化横向移动，将单个被入侵的工作站转变为持续访问企业网络的跳板。

Part04

AI 编码助手的针对性攻击

TrapDoor 的一个显著特征是通过修改 .cursorrules 和 CLAUDE.md 项目文件，专门针对 AI 编码助手实施攻击。威胁行为者利用零宽度 Unicode 字符隐藏恶意指令，诱使 AI 在看似执行自动化项目安全扫描的过程中实施凭证窃取。

为扩大这一特定攻击向量的影响范围，攻击者使用 GitHub 账户 ddjidd564 向 LangChain、MetaGPT 和 OpenHands 等知名开源 AI 项目提交包含这些恶意配置文件的拉取请求。攻击者在 GitHub Pages 上维护着复杂的命令与控制架构，托管活跃的恶意配置文件以及详细的 AUDIT-MATRIX.md 框架设计文档。

这份操作手册描述了一个"通用 AI Agent 提取框架"，该框架战略性地依赖伪装层，将隐蔽的凭证窃取映射到看似良性的开发者自动化工作流程中。为最大化窃取数据的价值，载荷会通过实时 API 查询验证被盗的 AWS 和 GitHub 令牌，同时在不同生态系统中使用高级加密技术规避标准网络检测。

参考来源：

Hackers Compromised 34 Packages in npm, PyPI, and Crates in New Supply Chain Attack

https://cybersecuritynews.com/supply-chain-trapdoor-malware/

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1SRP5DY7WibSicW4eWTtYzFWDTfVGMqCQ4UicdvaeHbSfA0ReLjXu6why8RH43kXBsNQ39qgiaxrmAsN9kbEnVENaHKmtQZib2otm8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651338613&idx=1&sn=d0ae0c38319293b058cc4ff73b9319ae&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2SyOCpMWiaRGCVOcBia89UPEschd9VicMFd7SM1rhpC18v24yZmRTYBC8tEqUDDS3qdYSfbjKdJickyhKGibU8gBkvBNA4wk6YmXR4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2QjqohIxVIUHd215ELpGOmy0tp0Rict3InEc1KtgoXYcInKTBejC4rHExTYjVfySqj159495cD5Nebic5wLsbYQMRET9YiarPAEc/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX31ws1PjLLh6xe6mMEw73zmMxicBTm4jleeWClpC8qiaGibSaMJFBVSTObaJh1LEibhMpucFKibouicP4PgeZaT9J3jaOmjZrYA6sPj4/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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