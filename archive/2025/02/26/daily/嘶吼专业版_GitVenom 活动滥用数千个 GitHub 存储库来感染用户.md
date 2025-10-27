---
title: GitVenom 活动滥用数千个 GitHub 存储库来感染用户
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247581299&idx=2&sn=3135c49c82bf03798f78bcd2d755a22f&chksm=e9146e49de63e75f9bb9e5bd1ebe872ea0d6fa467627d42bbd726280c3c8315cda53c487e172&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2025-02-26
fetch_date: 2025-10-06T20:38:21.962628
---

# GitVenom 活动滥用数千个 GitHub 存储库来感染用户

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibCxuxzrvJ6Td6eDfZiajluicIvicv0AUGMKm1dHIQ3fJzrPsdnC4cUXHiah0iasticLV6tNia5qIJc0eKGQ/0?wx_fmt=jpeg)

# GitVenom 活动滥用数千个 GitHub 存储库来感染用户

山卡拉

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

GitVenom 活动是一种复杂的网络威胁，利用 GitHub 存储库传播恶意软件并窃取加密货币。该活动通过创建数百个看似合法但包含恶意代码的虚假 GitHub 存储库来实施攻击，旨在诱骗开发人员下载和执行恶意代码，从而导致严重的财务损失。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibCxuxzrvJ6Td6eDfZiajluicCN7WCkssdAncKh5BiamyJX3x3rOSuuJibk5GgNWa6ng9qx1Be8WSOPaA/640?wx_fmt=png&from=appmsg)恶意代码部署

GitVenom 背后的攻击者使用多种编程语言（如 Python、JavaScript、C、C++ 和 C#）制作虚假项目。这些项目通常声称提供社交媒体或加密货币管理的自动化工具等功能，但实际上隐藏了恶意代码，执行恶意操作。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibCxuxzrvJ6Td6eDfZiajluics0aFfokkTeIrWk7twdxlZPz15xN5KpndpmVCcrJuu0JtJIDt5BWukw/640?wx_fmt=png&from=appmsg)

恶意存储库的示例结构

Python 项目：攻击者使用一种技术，在一长行制表符后隐藏解密并执行恶意 Python 脚本的代码。

JavaScript 项目：嵌入了恶意函数，用于解码并执行 Base64 编码的脚本。

C、C++ 和 C# 项目：恶意批处理脚本被隐藏在 Visual Studio 项目文件中，以便在构建过程中执行。

这些虚假项目部署的恶意负载会从攻击者控制的 GitHub 存储库下载其他恶意组件。这些组件包括一个 Node.js 窃取程序，用于收集凭证和加密货币钱包数据等敏感信息，并通过 Telegram 将其上传给攻击者。此外，攻击者还使用了开源工具如 AsyncRAT 和 Quasar 后门。

根据 SecureList 的报告，攻击者还使用了剪贴板劫持程序，将加密货币钱包地址替换为攻击者控制的地址，从而导致严重的财务盗窃。值得注意的是，一个攻击者控制的比特币钱包在 2024 年 11 月收到了约 5 BTC（当时价值约 485,000 美元）。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibCxuxzrvJ6Td6eDfZiajluicCN7WCkssdAncKh5BiamyJX3x3rOSuuJibk5GgNWa6ng9qx1Be8WSOPaA/640?wx_fmt=png&from=appmsg)影响与缓解

GitVenom 活动已经活跃多年，全球范围内都有感染尝试的报告，尤其是在俄罗斯、巴西和土耳其。这一活动凸显了盲目运行 GitHub 或其他开源平台代码所带来的风险。

为了降低风险，开发人员在执行或集成第三方代码之前必须彻底检查代码。这包括检查可疑的代码模式，并确保代码功能与描述一致。随着开源代码的广泛使用，类似攻击活动的可能性也在增加，这进一步强调了在处理第三方代码时保持警惕的必要性。

参考及来源：https://gbhackers.com/gitvenom-campaign-abuses-thousands-of-github-repositories/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibCxuxzrvJ6Td6eDfZiajluicVaq49YEK2f8U39ZZKHtTcPGpcT62iaIHCXibHGkej8MZDBjbnXoFuJfQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibCxuxzrvJ6Td6eDfZiajluicvLaGhw0QfebhUP9WKED1AuEsWGXia5laEggF5QW4XOYpibOqR1nRR9nA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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