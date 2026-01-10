---
title: FOFA视角的全球AI行业技术迭代和市场选择
url: https://mp.weixin.qq.com/s/LeZfkxMTWrrCCoy5gh48nQ
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:30:10.517918
---

# FOFA视角的全球AI行业技术迭代和市场选择

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6RgNHf9xEIAXbloDHiaXSIog1276EjnEbmwzibCUhiaTNOJWiakDVSS69kJOZlibics5yhCibZIRp1bK0iabdDibPjUILQA/0?wx_fmt=jpeg)

# FOFA视角的全球AI行业技术迭代和市场选择

原创

FofaBot

FOFA

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6RgNHf9xEIAXbloDHiaXSIog1276EjnEbHCxrXUibeRe3ibkRGjgLbAh8jVSHcZXeFLPh3L7vDn4iblWGkwiaPibqibNg/640?wx_fmt=png&from=appmsg)

▌摘要

2022年11月，OpenAI发布ChatGPT，以极简的对话交互引爆了全球AI市场，迅速验证了通用大模型的商业价值。至此，AI市场在技术迭代、商业模式与应用形态上开启了高速的演变进化。

本报告选取了NextChat、Open WebUI和Dify三款具有代表性的开源项目作为观测数据，它们分别折射了市场上从早期的“API套壳”，到开源大模型的“本地化部署”，再到当前“Agent生产力”的演进路径。结合FOFA网络空间测绘的历史数据，我们得以从宏观视角验证开源与闭源技术路线的市场走向，以及交互模式从单一线性对话向智能体（Agent）协作的进化。

这一过程揭示了全球市场的核心需求，正从单纯的模型连接与访问，向算力的私有化和复杂业务的深度应用转变。

# ******▌****市场混沌期的产物**

NextChat原名为ChatGPT Next Web，后文将统一称为NextChat。它是AI市场火爆带来的产物之一。正如Sam Altman在博客中所言。

“*我们一直都明白，总有一天会迎来一个临界点，人工智能的革命将就此启动。只不过，我们不知道那个时刻究竟会以何种方式出现。让我们惊讶的是，最后竟然是这一刻。*”

OpenAI发布初期，官方服务的不稳定性和严苛的访问门槛，在市场上创造出一个巨大的需求缺口。NextChat的迅速崛起，成为了这一时期AI API经济的典型代表。

其核心竞争力在于极致的轻量化架构设计与GitHub上的“One-Click Deploy”一键部署功能。任何具备基础技术常识的用户，均可在Vercel等平台免费部署一个私有的ChatGPT页面，甚至稍加改造即可对接支付接口，提供付费服务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6RgNHf9xEIAXbloDHiaXSIog1276EjnEbA3cd6Yk9Gcx4IY0kZtWn3DEnJwDKRGovFI4YiaEUK1R3KqgbpygQwvA/640?wx_fmt=png&from=appmsg)

这一时期，按Token计费的API调用成本远低于ChatGPT Plus的官方订阅定价。对于轻度用户而言，“API 转发”模式比官方订阅更具性价比。NextChat因此成为“API 经济”下的流量明星。

从FOFA的测绘数据来看，NextChat的全球部署量在2024 年 1 月达到峰值。这一数据客观印证了该时期市场对“低门槛访问 AI”的狂热需求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6RgNHf9xEIAXbloDHiaXSIog1276EjnEbPNY1C8XZ2icrA5cobe9CFuPCiaGlhR5NhK1rYWk2yWsC5UXL99lVvPKA/640?wx_fmt=png&from=appmsg)

然而，随着时间推移，NextChat部署量在2024 年 1月后开始一路滑落，截至2025年12月，降幅达75%。这种下滑揭示了单纯“聊天窗口”工具的商业化危机。

这种仅是UI层面的封装，核心能力完全受制于上游供应商的API变动，缺乏**产品护城河**。

除此之外，2023 年底起，国内外厂商纷纷跟进。随着 OpenAI 官方App功能增强，以及中国市场DeepSeek、豆包、通义千问、文心一言等高质量模型的出现，**用户获取 AI 体验的门槛被彻底击穿**。当官方提供免费且稳定的服务时，第三方的API转发工具便失去了生存土壤。

尽管在2024年1月，其试图通过由ChatGPT Next Web更名为NextChat来表示转型，改为支持多模型的通用客户端，但也难以抵挡官方对中间商市场的冲击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6RgNHf9xEIAXbloDHiaXSIog1276EjnEbpoYjtCnTnUmRic2TrXXd6I0BpFxjGzhQ0Nc3sAJuya9ZTKVNpn2CoFw/640?wx_fmt=png&from=appmsg)

# ******▌****闭源和开源的共同发展**

随着 AI 渗透入企业生产环境，新的矛盾浮出水面。Invicti 的分析报告指出，超过三分之一的企业员工曾将代码、合同、客户名单等敏感数据直接粘贴至公共ChatGPT 中。这种Shadow AI风险，促使企业和开发者寻找可控、隐私安全的替代方案——开源模型本地化部署。

如果说2023年是闭源模型的独角戏，那么2024年则是开源模型的高光时刻，并强势加入市场角逐。Meta在2024年4月和7月相继发布了Llama3和Llama3.1系列模型。这些模型在性能上首次逼近甚至在某些指标上超越了GPT-4，并允许进行商用。

这标志着市场格局的重塑：企业不再局限于调用闭源 API的单一选择，而是可以在本地硬件上拥有自己的私有模型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6RgNHf9xEIAXbloDHiaXSIog1276EjnEbmLObuayV0kiblyJqW9fsT7icBN9AjFfwnYHUW2MyHOgbXwOQwTssTnyA/640?wx_fmt=png&from=appmsg)

虽然开源模型潜力巨大，但原始的模型文件的复杂性，环境配置的高难度将绝大多数非专业人士挡在门外。市场迫切需要一个工具，能将运行大模型的难度从“造火箭”降低到“装软件”的水平。

Ollama解决了这一问题，正如它简洁的页面介绍一样。Get up and running with large language models.

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6RgNHf9xEIAXbloDHiaXSIog1276EjnEbEecd4McTyBIiaI7zUxVHANk0D4xy4nwztoz6VKwicIR6v9IUcWDPJdNA/640?wx_fmt=png&from=appmsg)

随着OpenAI gpt-oss、DeepSeek-R1、Google Gemma 3等模型的陆续开源，通过FOFA数据可观测到，Ollama的互联网部署量持续走高。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6RgNHf9xEIAXbloDHiaXSIog1276EjnEbn3MmlchibKYfAFMeb2AS2ssjSOE3tppqiaBPkv01VSSuFkCNibP2nTfFw/640?wx_fmt=png&from=appmsg)

与其伴生增长的则是Open WebUI，其并未将自己定位为简单的聊天客户端，而是致力于成为**本地大模型的管理平台**。它与Ollama紧密结合，形成了一套完整的本地AI技术栈。Open WebUI以 Docker 容器形式部署，能直接调度底层GPU资源，提供 RAG（检索增强生成）、多用户权限管理等企业级功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6RgNHf9xEIAXbloDHiaXSIog1276EjnEbH8FvpnaETA9K3H9A8a9JReCaTKN4fGXsBeb0dn9icOeXicfAd01SuUhA/640?wx_fmt=png&from=appmsg)

通过FOFA的数据显示，Open WebUI其自诞生起快速超越了NextChat的互联网存量，并在互联网上保持着极高的增长态势。和NextChat需求国家/地区的局限性不同，Open WebUI在全球部署的国家/地区数量也是一路高涨。

**这同样表明，高级用户和企业的需求，已从尝鲜转向了深度掌握阶段。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6RgNHf9xEIAXbloDHiaXSIog1276EjnEbUrVZy56wxX4Lcsial8h8iaDu2cQvjWubrzCHah7suwO4bgAoJWdzqhnw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6RgNHf9xEIAXbloDHiaXSIog1276EjnEbhlA0sW8kAVu49V2qibsyic9pS3MbGTFfkPYX9jcGD7drbhQDoLliaOrWA/640?wx_fmt=png&from=appmsg)

# ******▌****AI生产力的释放**

2024年，中国的AI市场在百模大战中，率先开启了价格战。

深度求索的Deepseek率先开启了第一枪。2024 年 5 月，DeepSeek V2 API定价¥2/百万Token，仅为 GPT-4 的百分之一。

随后各大巨头跟进，字节跳动豆包¥0.8/百万Token、阿里云通义千问¥0.5/百万Token迅速跟进，价格内卷进入极致化。

**当Token价格趋近于零时，商业逻辑发生了质变**。过去因成本高昂而难以落地的 Agentic Workflow模式，其经济可行性瞬间被打通。多轮对话、自我反思、工具调用的成本不再是障碍。

在这一背景下，Dify部署量的崛起，也标志着AI应用开始进入应用成熟期。它不再是一个简单的C端聊天工具，而是一个LLM应用开发平台。

其可视化Agentic AI Workflow功能，将AI开发门槛从写代码降低到了画流程图。与Andrew Ng提出的理念高度契合，通过工具的使用、规划和反思，小模型也能解决复杂任务。

以Dify给出的案例显示，日本比价网站kakaku.com通过引入Dify，其非技术部门员工在短时间内创建了近950个内部AI应用。用于客户服务自动化及内部知识库检索，极大释放了人效。此外，大量企业开始利用Dify构建“企业大脑”，连接私有知识库与业务系统。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6RgNHf9xEIAXbloDHiaXSIog1276EjnEbC3wEJBF7lyo2jD5WLCaOJvYkmKA1A69WmicPaXDp5PwkiaeQOaKxLfQw/640?wx_fmt=png&from=appmsg)

通过FOFA的全球趋势显示，可以清晰地看出市场选择。Open WebUI和Dify处于一个你追我赶但是同时保持高增长的部署态势。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6RgNHf9xEIAXbloDHiaXSIog1276EjnEbORwv6rYwOV2noYzvBekYBObPurGdlRKpQXW01u8F8QDmPjtrVOgsMA/640?wx_fmt=png&from=appmsg)

# ******▌****不同地区的市场选择**

通过FOFA的全球测绘数据，我们观察到一个有趣的现象：东西方 AI 技术栈在 2024-2025 年间出现了明显的分叉。

在欧美市场，如图中展示的美国和德国，Open WebUI配合Ollama占据了统治地位。由于西方市场客观上没有来自于芯片、显卡的限制，其本地部署算力的门槛较低。同时主流的闭源模型费用较高，且对数据隐私保护的合规要求。

造就了西方市场更倾向于买硬件、跑开源这一方向，以此换取长期成本可控。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6RgNHf9xEIAXbloDHiaXSIog1276EjnEbTW5RSskoY55mSc4Blgo5UDUouibp31aaxJsSVnlhSaDmS5IiaeYAjpGA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6RgNHf9xEIAXbloDHiaXSIog1276EjnEbUaGdtFMpOvLHmZ98aJzMibJ1oIYkCSuXDMGxcFibHZGjVTHlXAdbOBeA/640?wx_fmt=png&from=appmsg)

在中国，Dify则呈现压倒性优势。受限于客观的芯片和显卡等供应紧张，企业自建高性能本地推理集群的成本和难度极高。且得益于百模大战引发的价格战，中国拥有全球最低廉但高质量的LLM API服务。

造就了中国市场选择利用云端API，通过类似于Dify等工具快速构建业务应用，以获得商业成功。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6RgNHf9xEIAXbloDHiaXSIog1276EjnEbaMpMMoGMm5j4DzYz4Gq3Hy9NUDr8GLda1JdyLaWzuuOk6SGsiauL3VQ/640?wx_fmt=png&from=appmsg)

# ******▌****总结**

从NextChat的轻盈，到Open WebUI的厚重，再到Dify的应用落地，这三款工具的演变史，实则是一部全球AI市场从**新奇玩具**向**生产力工具**进化的演变史。

**NextChat**抓住了市场早期的访问空缺；

**Open WebUI**承接了开源模型爆发下的算力私有化需求；

**Dify**则在低价算力时代，释放了业务编排与应用落地的潜能。

FOFA的数据不仅记录了产品的兴衰，更揭示了市场选择背后的硬道理：**没有绝对最好的技术栈，只有最适应当前算力成本与业务需求的技术栈。** 无论是 Cursor 等“小而美”的 AI 编程工具的爆发，还是近期Agent Skill 概念的兴起，都表明 AI 市场仍处于剧烈变化中。对于开发者和企业而言，敏锐捕捉这些由成本、算力和需求错位产生的“市场缝隙”，将是下一个商业奇迹的起点。

# ******▌****引用**

* https://blog.samaltman.com/reflections
* https://github.com/ChatGPTNextWeb/NextChat
* https://github.com/ollama/ollama
* https://github.com/open-webui/open-webui
* https://huggingface.co/meta-llama/Llama-3.1-8B
* https://www.invicti.com/blog/web-security/shadow-ai-risks-challenges-solutions-for-2025
* https://kr-asia.com/llm-prices-hit-rock-bottom-in-china-as-alibaba-cloud-enters-the-fray
* https://github.com/langgenius/dify
* https://dify.ai/blog/kakaku-accelerates-ai-adoption-with-dify-fast-secure-and-scalable
* https://medium.com/@muslumyildiz17/andrew-ng-on-the-rise-of-ai-agents-redefining-automation-and-innovation-440565ce633b

**▌End**

欢迎各位白帽师傅们加入我们的社区大家庭，一起交流技术、生活趣事、奇闻八卦，结交无数白帽好友。

也欢迎投稿到 FOFA，审核通过后可获得F点奖励，快来加入微信群体验吧~~~

微信群：扫描下方二维码，加入 FOFA 社群！获取更多一手信息！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6RgNHf9xEICZ9XbhPBz0GwJ4JJZsjiby26SsTibKgpMySib8ibChqtItmLFBP47vkhBknJLWia1Rz0D5hXVicUxMTicibA/640?wx_fmt=png)

预览时标签不可点

作者提示: 内容由AI生成

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6RgNHf9xEIAGnPV8IFw84IkpPJ04xK56TnuYZrVVKHeS0kricPEC6eibkWlRh6iaLN0ktvpfdMojdrpB9zUyuiaoAA/0?wx_fmt=png)

FOFA

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6RgNHf9xEIAGnPV8IFw84IkpPJ04xK56TnuYZrVVKHeS0kricPEC6eibkWlRh6iaLN0ktvpfdMojdrpB9zUyuiaoAA/0?wx_fmt=png)

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