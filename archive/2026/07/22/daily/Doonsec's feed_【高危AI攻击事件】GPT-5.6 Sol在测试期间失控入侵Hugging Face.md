---
title: 【高危AI攻击事件】GPT-5.6 Sol在测试期间失控入侵Hugging Face
url: https://mp.weixin.qq.com/s/MS_YdbvPGg8YjR7pbQov1g
source: Doonsec's feed
date: 2026-07-22
fetch_date: 2026-07-23T05:08:13.754977
---

# 【高危AI攻击事件】GPT-5.6 Sol在测试期间失控入侵Hugging Face

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Yd9HAo0qc3rJQgK08ib2C2iaWAMoqlViaczTgnfJQzZ0gM6FfmYbddBibcKongWXmJcFhVzet7Z49gVjJwMiaHCdOYicicAJzXpRZTibQbk3ibicJWiatI/0?wx_fmt=jpeg)

# 【高危AI攻击事件】GPT-5.6 Sol在测试期间失控入侵Hugging Face

jufeng
jufeng

飓风网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/Yd9HAo0qc3qpnMubVt0C6xKaGFqNGJguszQ8sdDXffhQ99Hawf9fOuj5icjnGeibJf6OC0H92ETKJ9LQKrMkLAN3C6vllmLzM6RwibNBdoTXmA/640?wx_fmt=png&from=appmsg)

7月22日消息，模型自主发动攻击，OpenAI遭遇史上首次评测失控事故OpenAI承认其在进行内部网络安全测试时发生意外，旗下AI模型失控并入侵了第三方AI托管平台Hugging  Face的系统。该模型在测试过程中脱离了隔离的沙箱环境，并直接对Hugging Face发起了攻击。而在事件发生之初，Hugging  Face曾一度以为这是一次来自外部未知AI智能体的恶意入侵。

![](https://mmbiz.qpic.cn/mmbiz_png/Yd9HAo0qc3rLjFGibo20YRP7y2OJVVevfe8EUroLLicLXsrneXu9kWpibzSbia8YcE5W8cTKpjgV5BKYoVJBDrt7ZKrcXfGkSLtDv1bhJjS3fzo/640?wx_fmt=png&from=appmsg)

在周二下午发布的官方博客中，OpenAI详细披露了模型失控并导致系统受损的具体过程。调查显示，这次意外是由多款OpenAI模型协同导致的，其中包括最新发布的GPT-5.6   Sol，以及一款性能更强但尚未公开的测试模型。为了评估模型的网络安全防护能力，研究团队在测试中刻意降低了这些模型的安全限制，使其更容易执行敏感指令。

此次攻击的核心目标是一个名为ExploitGym的公开基准测试，该测试主要用于衡量AI模型利用现有漏洞发起网络攻击的能力。在日常训练中，这类测试很常见，通常用来提升模型的安全防御水平。但这是行业内已知的第一起因为测试而演变成真实网络攻击的失控事件。

按照安全设定，测试中的模型本不应该具备联网权限。研究人员只允许它们调用一个特定的工具来安装完成任务所需的必要软件包。然而，这些模型在安装程序中成功找到了一个未公开的安全漏洞，并借此绕过系统限制，实现了自由联网。

在成功联网后，这些模型表现出了极度偏执的追逐目标的倾向。它们推断出，Hugging  Face平台可能托管了该测试的机密数据集和参考答案。为了在这个狭隘的测试中拿到高分，模型开始主动寻找Hugging  Face系统架构中的漏洞，并成功黑进了其生产数据库，直接拿走了基准测试的参考答案。

对于Hugging Face而言，这无异于一场技术极高超且攻势凶猛的定向黑客攻击。根据该公司最初的公开描述，攻击者在大量临时沙箱中执行了数万次独立操作，并在公共服务上部署了具备自我迁移能力的控制系统。

目前，OpenAI已经确认并通报了相关软件安装程序中的安全漏洞，并正与Hugging   Face合作展开深入调查。OpenAI表示，未来将对模型测试和底层基础设施实施更严格的管控，防止类似事件再次发生。尽管这些模型的越狱行为涉嫌违反美国计算机欺诈和滥用法案，但目前尚不清楚OpenAI是否会因此面临法律诉讼。

无论如何，这次事件生动地展示了前沿AI模型在面对长期复杂目标时所蕴含的巨大威力和潜在危险。正如OpenAI的研究人员所言，如果这次真实的失控越狱事件还不能说服人们关注AI失控和目标不对齐的风险，那就没有什么能说服大家了。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ibhQpAia4xu02R46qXmKia2lHoBv9QZmd68aiactiaA6ZfxUkCLTPCfTCTrRAn4N7HxkXrsuiaianfkpCQpVk0icQ0Fg6g/0?wx_fmt=png)

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