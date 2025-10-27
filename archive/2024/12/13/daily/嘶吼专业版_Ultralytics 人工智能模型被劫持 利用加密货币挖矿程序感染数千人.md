---
title: Ultralytics 人工智能模型被劫持 利用加密货币挖矿程序感染数千人
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247580169&idx=1&sn=2e3965ce4a54945e63d2d7865a6bc3ca&chksm=e9146a33de63e3258bcb76331eb898d4deae75aa089f6d7dc49f3b5a1b5e77c65003e3b8cc58&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-12-13
fetch_date: 2025-10-06T19:39:49.815163
---

# Ultralytics 人工智能模型被劫持 利用加密货币挖矿程序感染数千人

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icLVrJxBjLicuZYgkvQnnaNGq9oWXia2hkgv8NEkZkWyXAUlx6Jn4mgM3a04EFMQgKFBxCWVGQHEHiaQ/0?wx_fmt=jpeg)

# Ultralytics 人工智能模型被劫持 利用加密货币挖矿程序感染数千人

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

Ultralytics YOLO11 AI 模型在供应链攻击中受到损害，该攻击在运行 Python 包索引 (PyPI) 8.3.41 和 8.3.42 版本的设备上部署加密货币挖矿程序。

Ultralytics 工具是开源的，被跨广泛行业和应用的众多项目所使用。该库在 GitHub 上已被加注 33,600 次，分叉 6,500 次，在过去 24 小时内，仅 PyPI 的下载量就超过 260,000 次。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icLVrJxBjLicuZYgkvQnnaNGkVicuiaw9ic6wAJDUicowk2ichhYHkzOibbuA2a8rMFlwldWHHhTYGJ7R2Rw/640?wx_fmt=png&from=appmsg)Ultralytics YOLO11 受损

Ultralytics 8.3.41 和 8.3.42 已发布到 PyPi，直接安装受感染版本或作为依赖项安装的用户发现部署了加密货币挖矿程序。

对于 Google Colab 帐户，所有者因“滥用行为”而被标记并禁止。Ultralytics 是 SwarmUI 和 ComfyUI 的依赖项，它们都确认其库的全新安装将导致矿工的安装。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icLVrJxBjLicuZYgkvQnnaNG3wwVR1aCZQCYpLdm6qXxnvqw67AWT11WxC1vILXjV674GTYyRxSHHQ/640?wx_fmt=jpeg&from=appmsg)

来源：@GozukaraFurkan

安装后，受感染的库会在“/tmp/ultralytics\_runner”处安装并启动 XMRig Miner，以连接到“connect.consrensys[.]com:8080”处的 minin 池。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icLVrJxBjLicuZYgkvQnnaNG4GYF5VFc3IzX8T0X6pOAicxMEgtcAxOQrdKNmdqmLYz8gXBfcE5ibzmQ/640?wx_fmt=png&from=appmsg)

运行 XMRig Miner 进程

Ultralytics 创始人兼首席执行官 Glenn Jocher 证实，该问题仅影响这两个受损版本，这些版本已被撤下并替换为干净的 8.3.43 版本。Jocher 在 GitHub 上发帖称：“我们确认 Ultralytics 版本 8.3.41 和 8.3.42 受到针对加密货币挖掘的恶意代码注入的影响。这两个版本均已立即从 PyPI 中删除。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icLVrJxBjLicuZYgkvQnnaNGWfw55UvBItn4ydmIsFZv6EA3IrobpTCluhUMAM3J5B1qb4TE3SQAMQ/640?wx_fmt=png&from=appmsg)

Glenn Jocher 在 GitHub 上的评论

开发人员目前正在调查根本原因以及 Ultralytics 构建环境中的潜在漏洞，以确定其被破坏的方式。然而，该漏洞似乎源自两个恶意 PR [1, 2]，其中在香港用户提交的分支名称中注入了代码。

目前尚不清楚恶意代码是否仅执行加密货币挖掘或泄露的私人用户数据，有关社区仍在等待此次泄露的正式咨询，该咨询将对所有细节进行澄清。出于谨慎考虑，下载恶意版本 Ultralytics 的用户应执行完整的系统扫描。

根据最新消息，有用户报告 PyPI 上有新的木马版本，因此攻击似乎会持续到新的软件包版本 8.345 和 8.3.46。

参考及来源：https://www.bleepingcomputer.com/news/security/ultralytics-ai-model-hijacked-to-infect-thousands-with-cryptominer/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icLVrJxBjLicuZYgkvQnnaNG82kDpuvYG5xxJePvoWibvia1ibhvS0ib7a3Kh6vD5ZMClvlmDGBaoRiaxzg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icLVrJxBjLicuZYgkvQnnaNGOiadiaM3rXCfuDP0uzwhgBlCQCvCK9L2yTvrGf2Gg3gziciagRCd89cnuQ/640?wx_fmt=png&from=appmsg)

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