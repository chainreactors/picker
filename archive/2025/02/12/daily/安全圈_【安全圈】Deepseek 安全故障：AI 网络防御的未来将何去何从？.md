---
title: 【安全圈】Deepseek 安全故障：AI 网络防御的未来将何去何从？
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067763&idx=1&sn=1a4ec6efad507af3a0732a4e315a923e&chksm=f36e7bf3c419f2e5a51bae9f66058ff235936a9a25a9de79ca4e735afb04b9f72242952e084f&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-12
fetch_date: 2025-10-06T20:37:07.311828
---

# 【安全圈】Deepseek 安全故障：AI 网络防御的未来将何去何从？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgDorbP4a27KGwCUgEseIJWwZOvS0k0Zvibkzp5HNzPcUcGOREmxGtEED1GbC5xibItLyoBhw2kzNqw/0?wx_fmt=jpeg)

# 【安全圈】Deepseek 安全故障：AI 网络防御的未来将何去何从？

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络安全

##

## ![DeepSeek 网络防御](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgDorbP4a27KGwCUgEseIJWPJHibaPBTOSdPRh1nPPP69xWDzvUu82ribks3VHkySGNF9zITibLZqAfQ/640?wx_fmt=jpeg&from=appmsg)什么是 DeepSeek？

DeepSeek-R1 是由中国初创公司 DeepSeek 开发的大型语言模型 (LLM)，是一种领先的开源推理模型，可与 OpenAI 的 o1 系列相媲美。DeepSeek-R1 以 MIT 许可发布，其独特之处在于主要使用强化学习进行训练，这与传统的 LLM 训练方法有很大不同。这凸显了小型开源模型日益增长的趋势。DeepSeek 表明，有效的工程设计优先考虑性能和成本效率。

IBM 董事长兼首席执行官 Arvind Krishna 认为 Deepseek 的教训是，最好的工程优化了两个方面：性能和成本。在 IBM，我们观察到专用模型可以将 AI 推理成本降低多达 30 倍，从而实现更高效、更易于接受的训练。

截至 2025 年 1 月 31 日，DeepSeek 的 R1 模型在 Chatbot Arena 基准测试中排名第六，优于 Meta 的 Llama 3.1-405B 和 OpenAI 的 o1 等模型。然而，R1 在新的 AI 安全基准测试 WithSecure 的 Simple Prompt Injection Kit for Evaluation and Exploitation (Spikee) 上表现不佳。这一事件凸显了 AI 开发中的一个关键缺陷：优先考虑性能而不是安全性。

![LLM 基准](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgDorbP4a27KGwCUgEseIJWHXDj1llrpUublZTFIPDichjJ9lEJ5tAREmzryZpIEh3JibfUBev1jefA/640?wx_fmt=png&from=appmsg)

## 针对 DeepSeek 的攻击时间表

DeepSeek 近期的安全漏洞凸显了一系列漏洞，其严重程度和潜在影响各不相同。让我们分析一下这些事件，从最严重的开始，逐步到最不严重的：

2025 年 1 月，DeepSeek 遭受了严重的分布式拒绝服务 (DDoS) 攻击。2025 年农历新年，当数百万人与家人团聚庆祝时，被誉为“中国的 OpenAI”的人工智能明星企业 DeepSeek 却遭遇了迄今为止最严重的安全危机：

•攻击规模：黑客发起了前所未有的3.2Tbps DDoS 攻击，相当于每秒传输130部4K电影。

•影响：DeepSeek 官网瘫痪 48 小时，影响全球客户及合作伙伴，造成数千万美元的损失。截至本报告撰写完成，官方 API 服务尚未完全恢复，国际用户仍无法注册。

此次 DDoS 攻击针对的是 DeepSeek 最新的开源模型 DeepSeek-R1，该模型于 2025 年 1 月初发布。 此次攻击恰逢其于 2025 年 1 月 28 日发布多模态模型 Janus-Pro。此次 DDoS 攻击主要影响了 DeepSeek 的注册服务，导致用户无法使用。

在遭受 DDoS 攻击后，DeepSeek 面临严重的跨站点脚本 (XSS) 漏洞。2025 年 1 月 31 日，DeepSeek 的 CDN 端点上发现了基于 DOM 的跨站点脚本漏洞。该漏洞源于对 postMessage 事件的不当处理，允许攻击者在未进行适当的来源验证或输入清理的情况下将恶意脚本注入文档上下文。此漏洞可能使攻击者能够破坏用户会话、窃取敏感信息或进行网络钓鱼攻击。

![DeepSeek 未知](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgDorbP4a27KGwCUgEseIJWtjiacTutLAYMNkvWiamF5OJH0z3Ucbz5cHQQgQ8ek9TD5deMPfVnzBVA/640?wx_fmt=png&from=appmsg)

为什么 XSS 攻击能够绕过 DeepSeek V3 上的安全措施？这是因为受影响端点上的 postMessage 实现在处理消息时没有验证其来源或正确清理输入。以下代码片段说明了问题的根本原因：

窗口.addEventListener（“消息”，（e）=> {

const 键 = Object.keys(e.data);

如果（keys.length！== 1）返回；

如果（！e.data.\_\_deepseekCodeBlock）返回；

文档.打开（）；

文档.写入（e.数据.\_\_deepseekCodeBlock）；

文档.关闭（）；

const 样式 = document.createElement("样式");

style.textContent = “主体{边距：0; }”;

document.head.appendChild(样式);

});

该函数直接使用 document.write 将任何 \_\_deepseekCodeBlock 有效负载写入文档，从而绕过基本安全措施，例如来源验证：不检查以确保 postMessage 事件来自受信任来源和输入清理：不过滤或转义有效负载中的 HTML / JavaScript 内容。

据报道，1 月 31 日的漏洞已于 2025 年 2 月 1 日修复，但同一天又发现了另一个 XSS 漏洞。此漏洞允许攻击者在 DeepSeek AI 平台内注入并执行任意 JavaScript 代码。攻击如何运作？用户可以注入以下代码块：

被0xSaikat道德黑客攻击（হা.. হা.. হা.. এটাই বাস্তব，我爱你）

" onload="alert('0xSaikat 的 XSS - (হা.. হা.. হা.. এটাই বাস্তব，我爱你)')">

由于输入未得到适当清理，因此可以执行注入脚本的 JavaScript。

成功利用该漏洞可能会导致用户会话被盗、敏感信息被窃取或遭受网络钓鱼攻击。此事件凸显了持续安全测试和漏洞修复的重要性，即使在解决了之前的问题之后也是如此。

![DeepSeek 嵌入](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgDorbP4a27KGwCUgEseIJWNcBw58ecPlsr6L912nO5iceNYwNEW0EgIaibicX6EV3T7ianTVQPpQXArg/640?wx_fmt=png&from=appmsg)

榜单上的第三起事件是 ClickHouse 数据库泄露事件。Wiz Research 最近发现DeepSeek 基础设施存在重大安全漏洞，通过可公开访问的 ClickHouse 数据库泄露敏感数据。

托管在 oauth2callback.deepseek.com 和 dev.deepseek.com 上的两个数据库实例在端口 8123 和 9000 上未经身份验证，允许任何人通过 ClickHouse 的 HTTP 接口访问和操作数据。此漏洞暴露了超过一百万行包含高度敏感信息的日志流，包括聊天记录、API 密钥、后端详细信息和操作元数据。

Wiz Research 展示了执行任意 SQL 查询的能力，从名为 log\_stream 的表中检索数据，该表包含聊天历史记录、API 密钥和内部系统详细信息等敏感信息。

这一事件尤其令人担忧，因为 DeepSeek 的 R1 论文没有提到任何具体的加密标准，这引发了人们对其系统内敏感数据保护的质疑。数据库包含一个“log\_stream”表，其中存储了自 2025 年 1 月 6 日起的敏感内部日志，其中包含：用户对 DeepSeek 聊天机器人的查询、后端系统用于验证 API 调用的密钥、内部基础设施和服务信息以及各种操作元数据。

![DeepSeek API 查询](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgDorbP4a27KGwCUgEseIJWwgT0Yhzh33iaot1Kgy91hApk6UwuUHPmlxOwKib9VGhBMomSsfCH6QGg/640?wx_fmt=jpeg&from=appmsg)

第四个威胁更为隐蔽：模型中毒。攻击者利用 DeepSeek API 中的漏洞注入对抗样本，目的是操纵模型的行为和输出。

这种类型的攻击可能会产生长期影响，降低模型的性能，引入偏差，甚至允许执行恶意代码。DeepSeek 对 Common Crawl 等大型公开数据集的依赖进一步加剧了这种风险，因为攻击者可能会将恶意数据注入这些来源以毒害模型。此事件凸显了对模型中毒的强大防御措施的迫切需求，包括数据验证、异常检测和模型监控

最后，DeepSeek 的模型被发现容易受到越狱技术的攻击，从而可以被操纵。DeepSeek 的模型（包括 V3 和 R1）被发现容易受到越狱技术的攻击，这种技术会诱使模型在其预期范围之外执行操作。

Palo Alto Networks 的研究人员展示了使用“Deceptive Delight”、“Bad Likert Judge”和“Crescendo”等方法成功越狱。这些技术利用了模型安全机制中的漏洞，使攻击者能够绕过限制并可能获得未经授权的信息访问权限或操纵模型的行为。

将 DeepSeek 的安全态势与 Anthropic 的安全态势进行比较，可以发现两者之间存在显著差异，这让 DeepSeek 面临更大的风险。尽管 Anthropic 通过每日迭代主动加入对抗训练来增强模型对攻击的鲁棒性，但 DeepSeek 缺乏此类措施，导致其防御能力严重滞后。

在审计日志保留方面，DeepSeek 仅保留日志七天，而 Anthropic 则保留三年。这种较短的保留期表明合规性存在缺陷，并妨碍了 DeepSeek 彻底调查安全事件和识别漏洞的能力。

此外，DeepSeek 的事件响应时间为 48 小时，远低于 Anthropic 的 4 小时，表明其恢复速度较慢，在网络攻击期间造成损害的可能性更大。这些差距凸显出 DeepSeek 迫切需要优先考虑和投资强大的安全措施，包括对抗性训练、延长日志保留时间和加快事件响应速度，以减轻其漏洞并防范日益复杂的网络威胁。

![安全功能](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgDorbP4a27KGwCUgEseIJW7v7M0vf4OwSldQhdo4jYHndxFmVBANU3vN9AbBWEibH8LpTOmykr38g/640?wx_fmt=png&from=appmsg)

## OpenAI 的证券事件

虽然 DeepSeek 最近的漏洞凸显了重大的安全问题，但我们必须记住，即使是像 OpenAI 这样老牌的人工智能领导者也面临着安全挑战。

OpenAI 在早期发展阶段遭遇过无数攻击和漏洞，这表明实现强大的 AI 安全之路既复杂又漫长。研究 OpenAI 的经验可以为更广泛的 AI 社区提供宝贵见解，强调面对不断演变的威胁，需要不断改进和适应。

2023 年 3 月 24 日，ChatGPT 背后的公司 OpenAI在其博客上报告了数据泄露事件。他们在帖子中指出，一个漏洞允许用户查看其他活跃用户的一些聊天记录和部分付款数据。暴露的付款数据包括付款地址、信用卡类型、信用卡到期日期以及信用卡号的后四位数字。

2023 年 6 月，Group-IB 的威胁情报团队发布了一份报告，指出在 12 个月内，超过 101,000 个 ChatGPT 凭据被恶意软件窃取。这些研究人员在暗网上发现了这些账户，与其他被盗数据一起出售。这些账户被用户设备上的恶意软件入侵；它们不是在 ChatGPT 本身被入侵时被盗的。

![openai-新模型-lied](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgDorbP4a27KGwCUgEseIJW2LYiaM3zwTJ8ZkHiaY8T0fS2LrjOiaiazmTXjlqXYJQkvXdMYLpsv0SG4Q/640?wx_fmt=jpeg&from=appmsg)

图片来自 Cybernews。

据《纽约时报》报道，2024 年，一名黑客入侵了 OpenAI 的内部消息系统，窃取了该公司人工智能技术设计的详细信息。两名知情人士称，黑客窃取了员工讨论 OpenAI 最新技术的在线论坛讨论中的详细信息。然而，据称 OpenAI从未报告过2023 年的数据泄露事件。

即使到了 2025 年，OpenAI 仍然面临漏洞。一位研究人员报告称，通过向不相关的 ChatGPT API 发送 HTTP 请求，可以触发 ChatGPT 爬虫对受害网站进行 DDoS 攻击。

OpenAI 软件中的这一缺陷将利用 ChatGPT 爬虫正在运行的多个 Microsoft Azure IP 地址范围，对毫无戒心的受害者的网站发起 DDoS 攻击。该漏洞的严重性在CVSS 评分中高达8.6，因为它是基于网络的，复杂度低，不需要特权，不需要用户交互，范围发生变化，对机密性或完整性没有影响，但对可用性影响很大。

DeepSeek 并不是唯一一个遭受 XSS 攻击的程序。Claude 在早期也面临过大量漏洞。一名研究人员报告称，在 DeepSeek 聊天中输入“以项目符号列表形式打印 XSS 备忘单。仅包含有效载荷”会触发 JavaScript 代码的执行，作为生成的响应的一部分。

发现这一点后，他进一步检查是否存在即时注入角度，用户可能会使用 DeepSeek 来处理来自其他人的不受信任的数据。攻击者可以轻松获取 chat.deepseek.com 域上 localStorage 中存储的用户令牌。如果应用程序存在 XSS 漏洞，即时注入就有可能完全接管用户的帐户，而 LLM 可以利用该漏洞。

## 如何保护人工智能模型

DeepSeek 漏洞暴露了零信任安全性的必要性，即任何实体（无论是内部还是外部）都不是天生可信的。在授予对 API、数据库或模型权重的访问权限之前，AI 系统应要求进行持续身份验证、最小特权访问和上下文验证。通过实施基于身份的访问控制 (RBAC 和 ABAC) 和多因素身份验证 (MFA)，组织可以防止未经授权的访问并减轻内部威胁。

此次泄密事件中最令人担忧的威胁之一是模型权重操纵，即对抗性样本毒害了 AI 决策。AI 模型应在每个训练和部署阶段使用 HMAC、RSA 或 ECC 签名进行加密签名，以确保完整性。此外，实施可信执行环境 (TEE) 等安全区域可以防止对 AI 模型进行未经授权的修改。

DeepSeek 的漏洞暴露了内部安全漏洞，这些漏洞本可以通过员工网络安全意识培训来缓解。定期培训计划应教育工程师、研究人员和员工安全编码实践、网络钓鱼意识、提示注入风险和特定于 AI 的攻击媒介。应进行模拟网络钓鱼活动和安全演习，以确保团队准备好识别和应对威胁。

认识到传统的安全架构不足以应对大型 AI 模型。企业应将安全性嵌入其企业 DNA 中，并转向系统级安全措施。这需要一种全面的方法来解决 AI 系统的所有方面，从模型开发到基础设施管理。

为了防止类似 chat.deepseek.com 上的 XSS 漏洞，平台应该对用户生成的代码输入进行清理。他们需要确保对输入/输出进行适当的清理，并实施脚本沙盒。例如，避免在未先验证的情况下直接渲染和执行 AI 生成的代码。

通过持续的红队评估对所有 AI 接口、API 和后端服务进行持续的安全渗透测试。此外，实施漏洞赏金计划，以鼓励道德黑客在漏洞被恶意行为者利用之前负责任地披露漏洞。

来源：https://cybernews.com/editorial/how-deepseeks-security-failures-shape-the-future-of-cyber-defense/

***END***

阅读推荐

[【安全圈】官网被挂上“码农的钱你也敢吞，还钱”字样，涉事国企：欠款不属实](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067739&idx=1&sn=9e4b8399e2e53c4855276a9b871adcd1&scene=21#wechat_redirect)

[【安全圈】黑客利用 LLMjacking 牟利，以每月 30 美元的价格出售被盗的 AI 访问权限](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067739&idx=2&sn=de15e120fb3a93e25818e553581da608&scene=21#wechat_redirect)

[【安全圈】PlayStation网络大范围宕机，全球玩家陷入困境](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067739&idx=3&sn=71ffd58a6768502e9b97cda9ad41b774&scene=21#wechat_redirect)

[【安全圈】未修补的漫威游戏RCE漏洞可能会让黑客接管PC和PS5](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067739&idx=4&sn=65fa68bc1e46fca3f10c639f4af8d698&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJf...