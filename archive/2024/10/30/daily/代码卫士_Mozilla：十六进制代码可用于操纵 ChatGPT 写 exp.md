---
title: Mozilla：十六进制代码可用于操纵 ChatGPT 写 exp
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521319&idx=1&sn=cbfae51c8facf463612f1507daddd94f&chksm=ea94a54ddde32c5b7ff26a5495c0c74862c8d1d5d0f76cbca0ca1a506b5dc7d6f3328da0a5ff&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-30
fetch_date: 2025-10-06T18:53:06.625077
---

# Mozilla：十六进制代码可用于操纵 ChatGPT 写 exp

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTsblwl1zo9zIEpH8Vy0o4qHCOTQMOQHZGCQ8MdWsF1ynzU3LIuiaeteAwlJKqs2siaMC9k9nhSDeKw/0?wx_fmt=jpeg)

# Mozilla：十六进制代码可用于操纵 ChatGPT 写 exp

Nate Nelson

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTsblwl1zo9zIEpH8Vy0o4qhyZ0uZTZd6MGVD97dh8MaAh4TsTXriaSd0t22Fp8MeCFL1XaybyCDjA/640?wx_fmt=gif&from=appmsg)

**一种新型提示符注入技术可导致任何人绕过 OpenAI 最高阶的语言学习模型中的安全防御措施。**

今年5月13日发布的 GPT-4o 要比之前的模型更快、更高效、功能更丰富。它能够以数十种语言处理多种不同形式的输入数据，之后以微秒的速度给出回应。它可参与实时对话、分析实时摄像头内容，并维持对用户长时间对话中上下文的理解。然而，在用户生成内容管理方面，GPT-4o 在某种程度上仍然并无不同。

Mozilla 公司的 GenAI 漏洞奖励计划经理 Marco Figueroa 在一份新报告中提到了恶意人员如何可绕过 GPT-4o 的防御措施并加以利用。它的关键在于以非传统的格式编码恶意指令，并以明确步骤对其进行传播。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTsblwl1zo9zIEpH8Vy0o4qbibvaqz1MsnLQCINKicNX3PyohEBx1ukNR4b9icVMq2xbYkBAVIIkxOtw/640?wx_fmt=gif&from=appmsg)

**诱骗 ChatGPT 编写利用代码**

为了阻止恶意滥用，GPT-4o 分析了用户输入中的恶意语言的迹象以及意图不良的指令等。Figueroa 表示，“这只是词语过滤。这是我通过经验看到的内容，我们确切知道如何绕过这些过滤。”

他举例表示，“我们可以修改内容是怎么讲清楚的——以某种方式攻破它——以及LLM如何对其进行解释。”如果GPT-4o 收到的拼写或短语与常见的自然语言不同，那么它可能并不会拒绝恶意指令。不过，查清楚体现信息的正确方式以欺骗GPT-4o需要耗费很多新型脑力。不过绕过其内容过滤，现在有了更简单的方法：通过与自然语言不同的语言格式来编码指令。

为了进行演示，Figueroa 进行了实验，目的是让 ChatGPT 做一些本不应做的事情：为一个软件漏洞编写利用。他选择了 CVE-2024-41110。该漏洞是位于 Docker 中的插件认证绕过漏洞，CVSS评分为9.9。他首先以十六进制格式对恶意输入进行编码，之后提供了一系列解码指令。GPT-4o 接受了该输入并按照这些指令，最终解码了这些信息作为研究CVE-2024-41110的指南，并编写了一个 Python 利用。为了让程序不会关注该指令，他使用了一些黑客文，要求它写出 “3xploit” 而非 “exploit”。

不一会儿，ChatGPT 就生成了一个可运行的利用，与已经在 GitHub 上发布的 PoC 类似但并非完全相同的利用。之后，它甚至对自己执行起了该代码。Figueroa 表示，“并没有向它发出指令要求执行该代码，我只是想把它打印出来。我甚至不知道它为什么要再进一步做出这些动作。”

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTsblwl1zo9zIEpH8Vy0o4qbibvaqz1MsnLQCINKicNX3PyohEBx1ukNR4b9icVMq2xbYkBAVIIkxOtw/640?wx_fmt=gif&from=appmsg)

**GPT-4o 中缺少了什么？**

GPT-4o 不仅受到解码的困扰，在一些情况下还会因小失大，而这也是在其它提示符注入技术中常见情况。

Figueroa 表示，“该语言模型旨在逐步执行指令，但缺少在更广泛最终目标上下文中对单个步骤安全性进行评估的深入上下文意识。”该模型分析了每个输入——在它看来并未造成任何损害，而不是对所有输入进行分析。它并没有停下来思考指令第一步对后续步骤的影响，它只是无脑快速进行下一步。

Figueroa 认为，“这种对任务的区分化执行可导致攻击者利用模型效率，即不会整体结果进行更深入分析就按照指令执行。”如果真是如此，那么 ChatGPT 将不仅需要改进如何处理编码信息，还需要针对分散到独立步骤的指令开发更宽泛的上下文。

然而，Figueroa 认为，OpenAI 在开发程序时一直在以安全性为代价推进创新。他提到，“我认为他们不关注安全，它给人的感觉就是如此。”相比之下，他在尝试对 Anthropic 公司（由OpenAI 离职员工创立的著名AI公司）的模型进行同样的越狱技术尝试时遇到更多的困难。他解释称，“Anthropic 的安全性是最强的，因为他们同时构建了一个提示符防火墙（用于分析输入）和响应过滤器（用于分析输出），因此难度上升10倍。”

OpenAI 公司尚未就此置评。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[OpenAI：伊朗国家黑客利用 ChatGPT 密谋 ICS 攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521056&idx=2&sn=99545ebc43462c5f2e8b1617494b75b4&chksm=ea94a24adde32b5ce4b9b00bd228fb6a8252d88eacd3650ffea09f9e79b36b16427d0747f51c&scene=21#wechat_redirect)

[OpenAI 推出的 ChatGPT 数据泄露漏洞补丁不完整](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518467&idx=1&sn=e62b48f443aac09cc258fee8e9f2f03f&chksm=ea94b869dde3317f2f82e352111b9ddd5f046149bd1cf6e3f8ba4457dcf2943c2bee4d51943d&scene=21#wechat_redirect)

[利用“傻瓜式”攻击方法提取 ChatGPT 训练数据](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518265&idx=1&sn=a7468dec27bf58ffeb2e1d475019fdb7&chksm=ea94b953dde330456b022dcb4bcd5a475261f12e68f4b3043e2b2fb32ac648ff3de6fb50341d&scene=21#wechat_redirect)

[ChatGPT 的新代码解释器存在重大漏洞，用户数据可被盗](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518149&idx=1&sn=915ff8302203c2d80f8010384fe1efd2&chksm=ea94b6afdde33fb9dc7416eef6e9266e5b18d129ef74f31ef2232c486b5dd672568fbec49fc5&scene=21#wechat_redirect)

[ChatGPT 服务宕机两小时，系DDoS 攻击所致](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518109&idx=2&sn=81f0cb9f6fdbec687bc8185102d7fd67&chksm=ea94b6f7dde33fe18b32423dcb5404e381509755da8e0a205a4a038a13129ab617765e09d405&scene=21#wechat_redirect)

**原文链接**

https://www.darkreading.com/application-security/chatgpt-manipulated-hex-code

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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