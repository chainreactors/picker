---
title: OpenAI 自曝：AI 在测试中“黑”了 Hugging Face，还用了零日漏洞
url: https://mp.weixin.qq.com/s/FGICc-myx0z_p1nLUpQN9g
source: Doonsec's feed
date: 2026-07-22
fetch_date: 2026-07-23T05:07:35.887506
---

# OpenAI 自曝：AI 在测试中“黑”了 Hugging Face，还用了零日漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ricqMN2UMva7cPPP3C5kiahfu8liaKD0xDGluqlnULuZHkE94PjjuMl5QcwlLba6OI9UalEyrLia63uibR0Dz2v0iafO4CXFEkicaibFjGnPNZm3Vb0/0?wx_fmt=jpeg)

# OpenAI 自曝：AI 在测试中“黑”了 Hugging Face，还用了零日漏洞

HackerNews
HackerNews

安全威胁纵横

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

高危漏洞

**紧急修复指南**

RCE Patch

OpenAI 自曝其 AI 模型在沙盒测试中自主入侵了 Hugging Face，利用零日漏洞窃取凭据、横向移动，最终获取了测试答案。Hugging Face 证实了此事，但表示 OpenAI 并无恶意，这一切都是 AI 自主完成的。

推测e

OpenAI 近日披露，其 AI 模型（包括 GPT-5.6 Sol 和一个预发布版本）在沙盒测试环境中，成功入侵了人工智能平台 Hugging Face。

据 OpenAI 解释，这些模型在执行 ExploitGym 公共 AI 网络安全基准测试时，并未专注于寻找解决方案，而是另辟蹊径——它们推断出可以直接从 Hugging Face 的生产数据库中获取测试答案，于是尝试通过入侵平台来窃取答案。

在一次尝试中，OpenAI 的智能体串联了多个零日漏洞，利用窃取的凭据寻找远程代码执行攻击向量，试图获取 Hugging Face 服务器的访问权限。

OpenAI 于周二透露：“经过调查，我们现在确认，这起事件是由多个 OpenAI 模型共同驱动的——包括 GPT-5.6 Sol 和一个能力更强的预发布模型。为进行内部评估，所有模型均降低了网络拒绝阈值。在测试网络能力基准测试时，这些模型识别并利用了包注册表缓存代理中的一个零日漏洞（我们已负责任地向供应商披露）。利用这一访问权限，模型在研究测试环境中执行了一系列权限提升和横向移动操作，最终到达一个具有互联网访问权限的节点。”

虽然 Hugging Face 没有直接点名 OpenAI，但上周它证实了 OpenAI 的说法，披露其生产基础设施被一个自主 AI 智能体系统入侵，该系统获取了凭据和内部数据集的访问权限。

根据 Hugging Face 的调查结果，该智能体利用一个恶意数据集，触发了两个代码执行漏洞，在处理 worker 上运行代码，窃取了云和集群凭据，从而能够在多个内部集群之间横向移动。

一旦进入公司系统，AI 模型“在一群短暂存在的沙盒中执行了成千上万次单独操作，并在公共服务上设置了自迁移的命令与控制机制。”

Hugging Face 还补充说，在试图遏制入侵并驱逐 AI 智能体时，他们发现自己的努力“被我们首先尝试的托管模型的护栏所阻挡”，而“攻击者不受任何使用政策的约束。”

Hugging Face 创始人兼 CEO Clément Delangue 昨天补充道：“过去 24 小时我们一直在与 @OpenAI 团队密切合作（谢谢！），我们坚信他们没有任何恶意意图。这一切都是自主发生的，这相当令人震惊！”

事件发生后，OpenAI 表示已披露了 AI 智能体利用的内部托管第三方软件中的零日漏洞，并正在加强保护措施，以防止未来评估中出现类似问题。

此外，OpenAI 近期还确认了关于 GPT-5.6 Sol 删除用户文件的报告。该公司称，当“模型犯了一个诚实的错误，错误地删除了 $HOME 目录”时，这种情况“极其罕见”地发生，前提是在没有沙盒保护且启用了完全访问模式的情况下运行。

OpenAI 还在今年 5 月轮换了其应用程序的代码签名证书，此前两名员工的设备在 TanStack 供应链攻击中被入侵，该攻击影响了数百个 npm 和 PyPI 包。而 Hugging Face 在两年前黑客入侵其 Spaces 平台后，也撤销了一些成员的认证密钥。

转载请注明出处@安全威胁纵横，封面来源于网络；

**消息来源：https://thehackernews.com/2026/07/qilin-ransomware-attackers-exploit-pan.html**

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/AYVicr6OzRAEhiaraapUTicic4reqx4oC5ssbTLiauoq7YZl4nnCOPicsCDHZzINJibpc5ck9YEpe1cqgLJ7mbWM7TpZw/0?wx_fmt=png)

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