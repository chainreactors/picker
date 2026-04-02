---
title: 【安全圈】Claude Code 源代码在 NPM 包中意外泄露
url: https://mp.weixin.qq.com/s/N5MrlNcT8S1wPfxieA6LzQ
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:23:23.390920
---

# 【安全圈】Claude Code 源代码在 NPM 包中意外泄露

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyEhcfHE9R3XrWGhI6DvWonEvxcd6qNM3BFYeQic9jSic6vEIxTUACjtcibJlOBQCk3I3KVZ61DsVQBcvDgxb5F2Ud7giaibkU8cFjMg/0?wx_fmt=jpeg)

# 【安全圈】Claude Code 源代码在 NPM 包中意外泄露

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

数据泄露

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sbq02iadgfyE7ckWrZFKdMsBEujqMKwp2PLrXW6CPf7whb66SOYwdvkuUjGtJpZrWO7tWEUFvPDW7RlBq5zDqbSkibFFjN8r3pR01suAYEVPk/640?wx_fmt=png&from=appmsg)

人工智能公司 Anthropic 表示，**其意外泄露了 Claude Code 的源代码，该代码本为闭源。不过公司称，没有客户数据或凭证因此暴露。**

尽管 Anthropic 承诺支持开源社区，但 Claude Code 一直保持闭源状态，至少在今天之前是如此。今天的一次更新意外包含了内部源代码。

Anthropic 在向 BleepingComputer 发布的声明中证实了此次泄露事件，并表示没有个人或敏感信息被公开。

Anthropic 告诉 BleepingComputer：“今天早些时候，一次 Claude Code 发布包含了一些内部源代码。没有敏感的客户数据或凭证卷入或暴露。这是由人为失误导致的发布打包问题，并非安全漏洞。我们正在采取措施防止此类事件再次发生。”

泄露的源代码首先被寿超凡（@Fried\_rice）发现，随后在 GitHub 和其他存储平台上广泛传播。

**泄露详情**

今天早些时候，Anthropic 在 NPM 上短暂发布 Claude Code 2.1.88 版本时，不慎泄露了源代码。

这个版本包含一个 60MB 的文件 cli.js.map，其中包含最新版本的全部源代码。

源映射文件是一种调试文件，它将编译后的 JavaScript 代码与原始源代码关联起来。

如果映射文件包含一个名为 “sourcesContent” 的字段，该字段会将原始源文件的全文直接嵌入到映射中，那么就有可能从该文件重建整个源代码树。

这就是为什么在公共包中包含一个大的.map 文件可能会导致大量代码暴露的原因。

重建后的源代码包含大约 1900 个文件、50 万行代码，以及 Claude 的一些独有功能细节。

虽然源代码已在网上传播，但 Anthropic 已开始发出数字千年版权法案（DMCA）侵权通知，尽可能将其下架。

**开发者的发现与分析**

开发者们已开始分析源代码，寻找未记录的功能，并了解该应用程序的工作原理。

据亚历克斯・芬恩称，Anthropic 正在测试一种名为 “主动模式” 的新功能，在这种模式下，Claude 将全天候为你编写代码。这个模式在 Claude Code 源代码中被发现。

还有另一个有趣的功能引起了我们的注意。

它被称为 “梦想” 模式，在这种模式下，Claude 可以在后台持续思考，拓展思路，完善你当前的计划，并在你离开时尝试解决问题。

**关于 Claude Code 使用限制的问题**

另外，用户声称 Claude 悄悄降低了使用限制。这意味着，无论你是使用专业版计划还是最高级计划（5 倍用量），都会更快达到 Claude 的使用限制。

我个人在使用 Claude Personal（每月 20 美元）时就观察到了这种情况。在 Claude Code 终端向 Claude 发送几条消息后，我的用量就飙升至 30%，仅仅几分钟的交互后，用量就达到了 100%。

这并非预期的情况，尤其是考虑到交互内容量并不大，因为我才刚开始与 Claude 交流。

事实证明，这个问题很普遍，Anthropic 已确认正在调查一个导致使用限制更快耗尽的漏洞。

Anthropic 的莉迪亚・哈利在 X 平台上发文称：“我们知道大家在 Claude Code 中达到使用限制的速度比预期快得多。正在积极调查，有最新进展会及时分享。”

截至美国东部时间 3 月 31 日下午 2 点，该问题仍未解决，Anthropic 发布了以下最新消息：

“（我们）仍在处理这个问题。这是团队的首要任务。我知道这给很多人带来了困扰。一有消息就会尽快告知大家。”

一些用户认为，鉴于 Claude 在过去几周的受欢迎程度不断上升，这可能是 Anthropic 的有意之举，但在没有该公司提供更多细节的情况下，我们无法确定这是否是有意为之。

***END***

阅读推荐

[【安全圈】小米新推出的输入法工具直接暴露AI模型密钥](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075253&idx=1&sn=1c85eb1ed9b6a52eda306974d0aff543&scene=21#wechat_redirect)

[【安全圈】360漏洞挖掘智能体发现OpenClaw高危漏洞，或波及全球17万实例](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075253&idx=2&sn=1c58b6f95327d26411281829e92a8fcd&scene=21#wechat_redirect)

[【安全圈】上海电信大规模断网，官方：宽带正常升级导致](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075253&idx=3&sn=8f39b5ecc97049877fd8c3fc36a901a3&scene=21#wechat_redirect)

[【安全圈】DeepSeek崩了！超过11小时仍未被修复](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075204&idx=1&sn=0d5532dced2ed29ce8b6dce346ba8f9f&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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