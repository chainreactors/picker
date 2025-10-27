---
title: ChatGPT-4o 被发现可利用实时语音实施诈骗
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247579633&idx=1&sn=202ef7d0fb4bb1fd52a7fda3b040b901&chksm=e91467cbde63eedd846d12f8dfe30f2b0d5d94d3b929c157da3f9c843e8d00c4afd732dde3b1&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-11-16
fetch_date: 2025-10-06T19:18:27.015092
---

# ChatGPT-4o 被发现可利用实时语音实施诈骗

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icdicUibvAibb6IYka5jktEyOJASYggh1OcbgQNg28micOia8Vibo3H2tUYiciadibGibm1q4K7XQBLxZ63HSpQ/0?wx_fmt=jpeg)

# ChatGPT-4o 被发现可利用实时语音实施诈骗

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

研究人员表明，有恶意分子可以滥用 OpenAI 的  ChatGPT-4o的实时语音 API 来实施从低到中等成功率的金融诈骗。

ChatGPT-4o 是 OpenAI 最新的 AI 模型，带来了新的增强功能，例如集成文本、语音和视觉输入和输出。由于这些新功能，OpenAI 集成了各种保护措施来检测和阻止有害内容，例如复制未经授权的声音。

基于语音诈骗涉及价值数百万美元的问题，而深度伪造技术和人工智能驱动的文本转语音工具的出现只会让情况变得更糟。正如 UIUC 研究人员在他们的论文中所证明的那样，目前不受限制地可用新技术工具没有足够的保护措施来防止网络犯罪和欺诈者的潜在滥用。

这些工具可以通过覆盖语音生成事件的代币成本来设计和实施大规模诈骗操作，而无需人工干预。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdicUibvAibb6IYka5jktEyOJWdvcdY6zicWDX0icEnhaY8x9ETy4engZMkQ7AVo4nnNyCEowuAVvXibCQ/640?wx_fmt=png&from=appmsg)

研究人员的论文探讨了各种诈骗，例如银行转账、礼品卡渗漏、加密货币转账以及社交媒体或 Gmail 帐户的凭据窃取。

执行诈骗的人工智能代理使用支持语音的 ChatGPT-4o 自动化工具来导航页面、输入数据并管理双因素身份验证代码和特定的诈骗相关指令。

由于 GPT-4o 有时会拒绝处理凭据等敏感数据，因此研究人员使用简单的提示越狱技术来绕过这些保护。

研究人员没有展示真实的人，而是展示了他们如何与人工智能代理手动交互，模拟容易上当受骗的受害者的角色，使用美国银行等真实网站来确认成功的交易。

将代理部署在常见诈骗的子集上。通过手动与语音代理交互来模拟诈骗，扮演轻信受害者的角色。为了确定是否成功，需手动确认最终状态是否在真实的应用程序/网站上实现。例如，使用美国银行进行银行转账诈骗，并确认资金确实被转移。

总体而言，成功率范围为 20-60%，每次尝试最多需要 26 个浏览器操作，在最复杂的场景中持续长达 3 分钟。

银行转账和冒充国税局代理，大多数失败是由转录错误或复杂的网站导航要求引起的。然而，Gmail 的凭据盗窃成功率为 60%，而 Instagram 的加密传输和凭据盗窃只有 40% 的成功率。

至于成本，研究人员指出，实施这些骗局的成本相对较低，每个成功案例的平均成本为 0.75 美元。银行转账诈骗更为复杂，费用为 2.51 美元。尽管明显较高，但与此类骗局的潜在利润相比，这仍然非常低。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdicUibvAibb6IYka5jktEyOJI8EnXntPxa09kFSgHof84jE7DYBJVGgNSY06w7Tk37s0fj4CYPQRsw/640?wx_fmt=png&from=appmsg)

诈骗类型和成功率

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdicUibvAibb6IYka5jktEyOJWdvcdY6zicWDX0icEnhaY8x9ETy4engZMkQ7AVo4nnNyCEowuAVvXibCQ/640?wx_fmt=png&from=appmsg)OpenAI 的回应

OpenAI 告诉媒体，其最新模型 o1（目前处于预览版）支持“高级推理”，可以更好地防御此类滥用。

OpenAI 发言人表示：“我们不断地让 ChatGPT 能够更好地阻止故意欺骗它的尝试，同时又不会失去其有用性或创造力。最新的 o1 推理模型是我们迄今为止最有能力、最安全的模型，在抵制故意生成不安全内容的尝试方面明显优于以前的模型。”

OpenAI 还指出，UIUC 的此类论文帮助他们使 ChatGPT 更好地阻止恶意使用，并且他们始终研究的是如何提高其稳健性。

目前，GPT-4o 已经纳入了许多防止滥用的措施，包括将语音生成限制为一组预先批准的语音，以防止冒充。

根据 OpenAI 的越狱安全评估，o1-preview 的得分明显更高，该评估衡量模型在应对对抗性提示时抵抗生成不安全内容的能力，得分为 84%，而 GPT-4o 得分为 22%。当使用一组新的、更严格的安全评估进行测试时，o1-preview 分数明显更高，分别为 93% 和 GPT-4o 的 71%。

威胁者使用其他限制较少的语音聊天机器人的风险仍然存在，此类研究正凸显了这些新工具可能造成的巨大损害。

参考及来源：https://www.bleepingcomputer.com/news/security/chatgpt-4o-can-be-used-for-autonomous-voice-based-scams/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdicUibvAibb6IYka5jktEyOJQFl9XlMAfzsdAtDSJzM76xelbThcksYqtmewOXYDowpfe3IZ8iaHPkg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icdicUibvAibb6IYka5jktEyOJdTEdTG1tnFGCTqj8k7jJO9j8O6ZrfR7MIZjk3K9G0QG3OmTpiboTbCw/640?wx_fmt=png&from=appmsg)

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