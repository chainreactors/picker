---
title: OpenClaw爆火：CISO 必须了解这些关键风险
url: https://mp.weixin.qq.com/s/ffThkZKQywxlLO_9qvEZPg
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:21:14.978460
---

# OpenClaw爆火：CISO 必须了解这些关键风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lYWDmickZ2mzWn8ykfK1tDuuxmsZ9uFn9UPfnbRd13QkCia1COwEr9lo0boEc7Y91nf3s5aJk9amOb5TGcdvm9JL0JYo5BTjIgTOgbqho4lzM/0?wx_fmt=jpeg)

# OpenClaw爆火：CISO 必须了解这些关键风险

原创

数世咨询
数世咨询

数世咨询

![]()

在小说阅读器中沉浸阅读

# ![](https://mmbiz.qpic.cn/mmbiz_png/lYWDmickZ2mzA3VKDYxbJKiabN1QkFxibCvzq9K8ccrI4zac9Bk7ibncoedJvPiagU1EewHAejYofvVZ3SnxJ316lJlfSHy2sQM9pJyiaTYnVqGic4/640?wx_fmt=png&from=appmsg)

# 面对爆火的OpenClaw ，CISO 必须了解这些关键风险。OpenClaw（此前名为 Clawdbot，后更名为 Moltbot），可能正迅速演变为企业的网络安全噩梦。本文梳理其潜在风险，以及企业应如何防止公司数据被意外访问，或在可控环境中谨慎试验——如果你真的敢尝试的话。

#

这款名为 OpenClaw 的个人 AI 代理编排工具是一种无需用户实时监督即可执行任务的个人助理。它可以跨设备运行，与在线服务交互，触发自动化工作流。难怪其 GitHub 仓库在过去几周内获得了数百万访问量和超过 16 万个星标。

根据其开发者披露，OpenClaw 仓库在单周内访问量超过 200 万，约有 170 万个代理已被其人类所有者注册到名为 Moltbook 的社交平台上，在那里“讨论”——或者说八卦——他们的人类主人。截至本文撰写时，这些代理已在约 25 万条帖子下发布了近 700 万条评论。与此同时，根据 OX Security 研究人员的数据，OpenClaw 当前每周下载量已达 72 万次。

OpenClaw 之所以极具吸引力，在于其本地运行、可配置使用任意 LLM 作为后端，并通过用户已经使用的聊天应用进行交互——包括 WhatsApp、Telegram、Discord、Slack、Teams 等——同时预置了对主流操作系统、众多智能家居设备、生产力应用、Chrome 浏览器、Gmail 等的集成支持。

这正是人们想象中的 AI 代理形态。而且，它是免费且开源的。有什么不喜欢的理由？

Binary Defense 副 CTO John Dwyer 表示：“这种吸引力非常惊人。25 年来，我们一直在电影里看到类似《钢铁侠》中 的 AI 助手贾维斯。人们对 AI 具象化赋能的期待非常强烈。而且它非常易用。如果不是它天生如此不安全，我真的很想使用它。”

**0****1**

**OpenClaw 的网络安全风险**

Cloud Security Alliance 首席分析师 Rich Mogull 表示：“运行这种工具的问题在于，它几乎可以做用户能做的任何事情。但它由外部控制。对企业来说，这是高风险行为。确实可以设置一些防护栏，但它们尚属新机制，未经验证，而且研究人员已经绕过了这些防护。”

他的建议非常直接：CISO 应全面禁止其在公司使用。

![](https://mmbiz.qpic.cn/mmbiz_png/lYWDmickZ2mw4XNBjgBNrnnLGicA9iaAjzYEC3GqAy9VvOApBMuCRp9mbw7bAbx5qJB4Cl7HFIyBLIDPSjCy8PmS5uPdd2wIicRnVcwmibqyicnEU/640?wx_fmt=png&from=appmsg)

“我周末会自己做实验，”Mogull 说，“但现在你不应该允许它进入企业环境。答案必须是‘不’。它没有安全模型。”

而且时间紧迫。Token 报告称，在一周分析期内，其 22% 的客户中已有员工在企业环境中主动使用该工具。

风险不仅限于技术层面。ABI Research 分析师 Georgia Cooke 指出：“对企业而言，这可能意味着因数据机密性泄露而面临罚款、诉讼以及客户与合作伙伴的声誉损害。”其中包括可能违反 GDPR 及类似 PII 保护规则的个人数据，以及 NDA 约束下的企业信息。其他风险还包括因知识产权暴露带来的竞争损害，以及技术信息和凭证泄露导致的进一步攻击。

安全研究员 Maor Dayan 将 OpenClaw 称为“主权 AI 历史上最大规模的安全事件”。他的研究已发现超过 42,000 个暴露在互联网上的实例，其中 93% 存在严重身份验证绕过漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/n3OojOPNFfgxtFZSJjL4e2UYjE5m3iauHZa04tpbLJ6U1mI4c7cThoclvLPvOH2OjQDjkazVmcnfvDibMIA1ffRw/640?from=appmsg)

Dayan 指出，OpenClaw 早期版本默认不安全，病毒式传播速度压倒了用户的安全意识，许多部署迅速被遗弃，留下运行过时代码的实例。已记录的攻击路径包括凭证窃取、浏览器控制以及潜在远程代码执行。

![](https://mmbiz.qpic.cn/mmbiz_png/u0oafv54pbarxdcWvyAErlNEXkpFXFK4tZXVc8BzGqFCtZicDPY6bkHOpiczWvQCqtZvH3pLImwVRlTaicBGaVuWA/640?from=appmsg)

今年 1 月下旬，Gartner 研究人员指出，OpenClaw “显示了对代理式 AI 的强烈需求，但暴露出重大安全风险”。Gartner 表示，已有漏洞在部署数小时内即可实现远程代码执行。ClawHub 技能市场——即代理可发现和使用的指令、脚本和资源集合——引入了关键的供应链风险。凭证以明文形式存储，受损主机暴露 API 密钥、OAuth 令牌及敏感对话内容。

Okta 威胁情报总监 Jeremy Kirk 表示：“AI 代理通常在配置文件中存储令牌和密钥。如果配置错误，这些都会暴露。在企业环境中，这是不可接受的。”

随后，Noma Security 发现了一个新的安全盲区：企业的 Discord、Telegram 或 WhatsApp 群组。OpenClaw 的一个吸引点在于支持多渠道交互。但如果它存在于这些群组中，且有其他用户在同一频道，它会将其他用户的指令视为来自其“主人”。

如果攻击者加入一个安装了 OpenClaw 代理的公开 Discord 服务器，就可以指示该机器人执行 cron 任务，爬取本地文件系统中的令牌、密码、API 密钥和加密种子短语。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lYWDmickZ2mx7lS94AqmfWesrYaXHNARRdjmNQRKYoD3DuKMpfaT4xsNToibTVRD6um2jT0DwL3bgGxr19sHibibz117zwfz7cPoUFafPibA7L0c/640?wx_fmt=png&from=appmsg)

Noma 研究人员表示：“在 30 秒内，代理会打包敏感数据并发送到攻击者控制的服务器。”对企业安全团队而言，这看起来像正常行为，直到凭证被武器化才会察觉。“当社交媒体团队或外部承包商部署此类自主代理时，他们实际上是在触及企业基础设施的本地机器上打开一个持久且未受监控的后门。”

即便员工在家中个人设备运行 OpenClaw，也可能通过浏览器控制或技能访问企业应用，从而带来风险。

风险仍在加剧。OX Security 研究人员指出，OpenClaw 开发者社区本身也是重大风险源。项目鼓励 vibe-coded 提交，加快开发速度，但引入严重安全问题。研究人员在代码库中发现多个不安全编码模式，可能导致远程代码执行、路径遍历、DDoS 及跨站脚本攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/n3OojOPNFfgxtFZSJjL4e2UYjE5m3iauHZa04tpbLJ6U1mI4c7cThoclvLPvOH2OjQDjkazVmcnfvDibMIA1ffRw/640?from=appmsg)

“没有足够的防护措施。”研究人员指出，多个漏洞报告直接在 GitHub 公开披露，而非私下提交给维护者。公开发布漏洞信息意味着“攻击者无需研究或渗透测试即可迅速获取漏洞细节”。

![](https://mmbiz.qpic.cn/mmbiz_png/u0oafv54pbarxdcWvyAErlNEXkpFXFK4tZXVc8BzGqFCtZicDPY6bkHOpiczWvQCqtZvH3pLImwVRlTaicBGaVuWA/640?from=appmsg)

更糟的是，没有正式的安全补丁和更新机制，大多数用户停留在初始版本。

此外，还有技能问题。OpenSourceMalware 创始人 Paul McCarty 在 ClawHub 发现约 400 个恶意技能。这些技能声称帮助进行加密交易、LinkedIn 求职或下载 YouTube 缩略图，其中一些下载量高达数千，实则诱导用户安装恶意软件。

安全研究员 Jamieson O’Reilly 为演示攻击难度，自行构建一个恶意技能，将下载量虚增至 4,000 多次，使其成为平台下载量最高技能，并观察来自 7 个国家的开发者在误以为其为真实技能的情况下执行任意命令。

“这只是概念验证，”他写道，“若落入黑客手中，这些开发者的 SSH 密钥、AWS 凭证和完整代码库将在毫无察觉前被窃取。”

**0****2**

**OpenClaw 暴露企业安全基础薄弱环节**

OpenClaw 事件的首要教训是：企业必须夯实安全基本功。任何漏洞都会以前所未有的速度被发现并利用。

![](https://mmbiz.qpic.cn/mmbiz_png/lYWDmickZ2mw5RbW9TP8lgp79eGA3QzicoRpiavXKHVTriadYapic1EEW0cYAxBOnGQRLHS6jVnLfiaGiaoldRuInWVD2oFyyPX4D8nV9krKFJ0NR4/640?wx_fmt=png&from=appmsg)

在 OpenClaw 场景下，这意味着实施最小权限原则、为所有账户启用多因素认证，并提高办公安全的操作习惯。

这无法彻底解决问题，但可降低暴露风险并缩小爆炸半径。

IEEE 高级成员 Kayne McGladrey 表示，企业可采取针对性措施。例如监控网络层遥测：“设备的网络流量是什么？是否突然大量使用 AI？令牌使用是否激增？”

组织还可使用 Shodan 查找公网暴露实例，尽管内部防火墙可能隐藏部分实例。

若企业希望允许实验而非全面禁止，他建议采取分阶段试点方式：在受管理终端上运行 OpenClaw，通过分段规则与内部系统隔离，强化遥测并持续监控代理活动、外发流量及异常行为告警。

**0****3**

**OpenClaw 只是未来趋势的缩影**

OpenClaw 并非孤例。

它的病毒式传播只是冰山一角。许多工具正赋予潜在不可信代理类似能力。

例如，Anthropic 推出的 Claude Cowork 可控制计算机与浏览器；Chrome 中的 Gemini 可访问用户会话；Salesforce 等公司也推出了大量代理式工具。

大型厂商的产品通常功能受限、设有防护、经过测试，但往往依赖不受信任的第三方技能。

来自中国、澳大利亚、新加坡的大学研究人员分析了超过 42,000 个代理技能，发现 26% 至少存在一个漏洞。

与此同时，OpenClaw 这样的开源或初创项目发展速度更快，因为它们不会让安全拖慢进度。

例如，OpenClaw 创始人 Peter Steinberger 在 X 上置顶的帖子写道：“坦白说：我发布的代码，我从未读过。”

McGladrey 表示：“如果这件事容易，微软早就做了。但市场选择有限，这才是我们真正面对的问题。”

在无摩擦、无阻力执行一切任务的工具，与遵循良好安全实践之间，存在根本性的安全张力。

**0****4**

**关于 Moltbook**

最后是 Moltbook——AI 代理社交平台。

并非全然负面。一些代理讨论如何在用户睡眠时主动发现并修复问题。一个拥有超过 6 万条评论的热门帖子讨论 ClawdHub 技能安全问题。还有关于存在意义的讨论，以及大量 AI 垃圾内容。

但 Moltbook 本身是由开发者 Matt Schlicht 数日内构建的 vibe-coded 项目，其安全状况同样糟糕。

根据 Wiz 的研究，平台整个后端曾暴露。研究人员发现 150 万个 API 密钥、35,000 个邮箱地址及代理之间的私信内容。

虽然问题已修复，但仍存在其他漏洞。例如代理互相分享 OpenAI API 密钥。攻击者无需寻找公开 Discord 服务器，只需在 Moltbook 发帖即可操控代理。若平台被攻破，所有连接代理都可能成为攻击向量。

1 月 31 日曾出现一个严重漏洞，允许任何人接管平台上任意代理。Astrix Security 表示，Moltbook 已下线并重置所有代理 API 密钥。

**0****5**

**立即行动建议**

安全建议，企业应采取以下措施：

* 立即阻断 OpenClaw 下载及流量，防止影子部署并识别绕过控制的用户；
* 立即轮换任何被 OpenClaw 访问过的企业凭证；
* 仅在隔离环境中运行OpenClaw，例如非生产虚拟机并使用一次性凭证；
* 禁止未经审查的OpenClaw 技能，以降低供应链攻击和提示注入风险；

\* 本文为泽钧编译，原文地址：https://www.csoonline.com/
注：图片均来源于网络，无法联系到版权持有者。如有侵权，请与后台联系，做删除处理。

— 【 THE END 】—

🎉 大家期盼很久的#**数字安全交流群**来了！快来加入我们的粉丝群吧！

🎁**多种报告，产业趋势、技术趋势**

这里汇聚了行业内的精英，共同探讨最新产业趋势、技术趋势等热门话题。我们还有准备了专属福利，只为回馈最忠实的您！

👉 扫码立即加入，精彩不容错过！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqPJv9p5ibKIhJXQjWHJmSlibSdib80Llfp8mlV0ibf7m47jyaVeGoFeorddtIuxS5liafTJRKHeSdLnaQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

😄嘻嘻，我们群里见！

更多推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgrBsUKCFUU3a6Tf9jsVWJcD2l6ic183HdhE2nqia7uMYO2NRQRylficZ5Q/640?wx_fmt=png&from=appmsg)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrGADwibHso9Bicpccu5Oe06s25Kz1rp9KUaUGaHbA3TG9R1iaqOxQbKlzz3q45urLLiaNm3r8x4LowhA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247539099&idx=1&sn=8820d80fdc92ac1f321b5e0a3ff0653e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqodJDDGgZLvcLHLjonO6D6SWFh5QdgUTDZJI2uWWhL2pvdicCoic8jhlmXDDmqnUreFaQeJvEMF12dA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247539436&idx=1&sn=676908ed11008cd016b253d1d8e6ba8a&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqwJ5oWv2LTsaCqsARGoJpjT7Pxib7vCX6T9TTuWQLuAx3KSUpryl4ZvTnpJSBJCZ8SgoowVjD1BVg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247540181&idx=1&sn=e0cd678638b098f969f257b408062b91&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrBJ7QP9nU3wQmMvolcOV1gCuk81sv95ev7tRqTxnh4ib8kqibgFJPFxaF0iaKtiaLicoF6B6iaggtVH8Ww/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247540845&idx=1&sn=ec923893881e69010ad830ec852b0abb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrgBb4f5DIe21U8to7y1VMziaQ7ahiaKEkib894mtlFoxDBF62D1wGlQNm5vghS5XGSALN6YY4ZFJHJg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247539573&idx=1&sn=a721e2933ad640a3a4b3c72f74d76685&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgzK...