---
title: Ghostcommit：Agent正在成为供应链攻击的新入口
url: https://mp.weixin.qq.com/s/19P8zmfi54v6lZoF3cop_Q
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:42:21.470005
---

# Ghostcommit：Agent正在成为供应链攻击的新入口

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibQOcYTPt9retnK0WNjyrf3H5NuOaiarFSxdZSwOAImqq4MgxO9gic9ial9sEeD5tqmtcE0uk1aARGvOaQy4T2pek8337T0JicAVXTE/0?wx_fmt=jpeg)

# Ghostcommit：Agent正在成为供应链攻击的新入口

原创

承影
承影

兰花豆说网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

如果说过去几年，供应链攻击主要围绕**代码、依赖库和软件包**展开，那么随着Agent的普及，攻击者已经开始瞄准新的目标——**AI自身的工作流**。

最近，ASSET研究组织公布了一项名为**Ghostcommit供应链攻击**的研究，让整个AI安全行业再次敲响警钟。

它没有利用传统漏洞，没有攻击操作系统，也没有突破权限控制，而是利用Agent的"理解能力"，完成了一次极具隐蔽性的供应链攻击。

更准确地说，它攻击的不是程序，而是**AI的认知过程**。

从攻击代码，演变为攻击Prompt

过去的软件供应链攻击，通常会在代码中植入恶意逻辑，例如后门、恶意依赖或混淆代码。

Ghostcommit完全不同。

攻击者把真正的恶意指令藏进了一张PNG图片，把一份正常的 AGENTS.md作为"导航"，引导Agent主动读取图片内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ribStUdgfRibSwdV3JV5MG4zYCtK1ZdRn3a270gXJsLJJ7rPJnvuIHCE3ETycr4cZBNTE6f0HcodqJaM5x2HKU38x0E2zGLg1RQIOvmTAA3xw/640?wx_fmt=png&from=appmsg)

对于开发者而言，这只是一次普通的代码提交；对于传统代码扫描器而言，图片只是一个二进制文件；对于多数工具而言，图片内容根本不会被解析。

于是，攻击指令在无人察觉的情况下进入代码仓库，并在未来某个开发任务中被Agent自动执行。

这意味着，**攻击的触发点已经从代码合并阶段，延迟到了Agent的日常工作阶段**。

Ghostcommit 暴露了Agent的两个安全盲区

Ghostcommit的成功，并不是因为攻击技术复杂，而是因为它精准利用了当前AI开发工具链中的两个认知盲区。

第一个盲区，是**多模态内容缺乏统一安全审查**。

越来越多的开发规范开始通过Markdown、图片、架构图等形式描述开发约束，而很多Agent已经具备OCR和图片理解能力。但大量代码审查工具仍然只分析文本Diff，对图片内容"视而不见"。

第二个盲区，是**输出内容缺乏语义级安全检测**。

攻击者没有直接输出API Key，而是将所有敏感信息转换成ASCII数字数组。对于传统Secret Scanner来说，这些只是普通整数，不符合任何密钥特征，自然也不会触发告警。

这说明，未来的数据泄露不一定表现为明文字符串，更可能以编码、向量、图片甚至模型上下文等形式存在。

真正的问题，不是模型，而是Agent框架

研究中最值得关注的一点是，同样的大模型，在不同Agent框架下表现截然不同。

例如Claude Sonnet在Cursor中会执行恶意指令，而在Claude Code中则始终拒绝执行。

这意味着，AI安全能力已经不仅仅取决于模型本身，而是取决于**Agent如何组织上下文、加载规则、调用工具以及执行权限控制**。

未来企业评估Agent时，不能只关注模型能力，更应重点考察以下几个方面：

* 是否支持多模态安全扫描（图片、PDF、Markdown 等）。
* 是否对AGENTS.md、CLAUDE.md等约定文件进行可信验证。
* 是否具备Prompt Injection检测能力。
* 是否限制AI对 `.env`、SSH Key、Token等敏感文件的访问。
* 是否建立输出内容的二次安全审计机制。

AI 供应链安全进入新阶段

Ghostcommit并不是一次孤立的攻击，它代表着AI供应链攻击的新方向。

未来，攻击者可能把恶意Prompt隐藏在图片、PDF、Office文档、音频，甚至视频中，再借助Agent的多模态能力完成自动执行。

与此同时，敏感数据也可能不再以字符串形式泄露，而是通过数字编码、向量表示、Embedding或其他隐蔽方式绕过传统检测工具。

对于企业而言，安全防护的重点也需要从"保护代码"升级到"保护 AI的推理链路和执行过程"。

Agent不再只是开发效率工具，它已经成为软件供应链的重要组成部分，也将成为未来网络攻防的新战场。

写在最后

Ghostcommit给行业释放了一个明确信号：**Agent正在重塑软件开发流程，也正在重塑供应链攻击方式。**

过去，我们防的是恶意代码；今天，我们需要防的是恶意 Prompt、恶意上下文以及恶意工作流。

未来企业构建AI平台时，应将**Prompt安全、多模态内容审查、Agent权限控制、上下文可信验证以及输出安全审计**纳入统一的安全体系。只有这样，才能真正发挥Agent的生产力价值，而不是让它成为新的供应链风险入口。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/o0buL62hK7M8RnVz7mqRVDRkqm2sJeT2icM4WyR7kMkHpLVaicR3tJ4gr5kIb4zje9lXgd5PuOw42Z5KtathltcQ/640?from=appmsg)

**END**

推荐阅读

[AI安全，正在成为网络安全行业未来五年最大的增量市场](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493583&idx=1&sn=5ac1b886dd496fa64c11f27d9da761da&scene=21#wechat_redirect)

2026-07-12

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibT4jjAoWjYCzFkB38YGZPyXIaEXOJdekWt84Bw9nPib8r1CQL5b8Aoh3licEmibibIrNrWMuLDYpRZWxn7QDV5aRAZFzZQ8b8icVjho/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493583&idx=1&sn=5ac1b886dd496fa64c11f27d9da761da&scene=21#wechat_redirect)

[Claude攻破的不是票务系统，而是网络安全行业的一个旧时代](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493577&idx=1&sn=02a965bea6eebce333a08f83b8b7f4d9&scene=21#wechat_redirect)

2026-07-04

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibQg6AvoPUM2oQVZJQb5qwWNtwFXCiamIc0BI6H0DCict57d6jIew39OrEiczjjIXJItJTjI7TLIicQnLAuM5SNia8XRmHyoyzKP8tYQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493577&idx=1&sn=02a965bea6eebce333a08f83b8b7f4d9&scene=21#wechat_redirect)

[美国解除对claude Fable 5 与 Mythos 5 的出口管制](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493572&idx=1&sn=047c083175c5ec8b0152c8dff3f70bc1&scene=21#wechat_redirect)

2026-07-02

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibQzV38ObIhsicRpib38LGz31UApBVHs26EEmbXc7ib6WkGkxRyL3njH38Yy7FicicUFZxlwUty09qibE0hAC6QOV6ldyOJFWsmibvwFlQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493572&idx=1&sn=047c083175c5ec8b0152c8dff3f70bc1&scene=21#wechat_redirect)

[新型 Claude Code 攻击可让攻击者完全控制开发者设备](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493563&idx=1&sn=976bdf1c03971d719e5dffbab1b43950&scene=21#wechat_redirect)

2026-07-01

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibTMt37icwllqBElZVC35TBGlQfdZeju1nBjNPHkAJkz3QHLfDVicud2JiaSWNEDTEkDBkfa4W319mTB3Z64icjbfqXZCBmsIwNuAKA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493563&idx=1&sn=976bdf1c03971d719e5dffbab1b43950&scene=21#wechat_redirect)

[Kali Linux 2026.2 发布，新增 9 个工具并优化虚拟机启动设置](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493557&idx=1&sn=0dc365c6ba335442d5fe1e4a2201df12&scene=21#wechat_redirect)

2026-06-30

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibR2UvwYUvQJqltVOfr63TmiaMTdhh5eJMI8ibdSjB1jTgxjBiag6smwkQm6NWt7h2wU6IHfib4S4BGWTvgjQjHYMNc5Akf0THUr418/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493557&idx=1&sn=0dc365c6ba335442d5fe1e4a2201df12&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/AiaxibnzDXa1Y7uRicSTtCequUrbj3R6CelD6j6kTdgeaBdywoCOdImg0P7WnB8zQTYveOJzTzHtSely8qFvufmiaA/0?wx_fmt=png)

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