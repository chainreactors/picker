---
title: DeepSeek遭遇连环攻击，AI 安全何去何从？
url: https://www.freebuf.com/news/421454.html
source: FreeBuf网络安全行业门户
date: 2025-02-12
fetch_date: 2025-10-06T20:36:22.143548
---

# DeepSeek遭遇连环攻击，AI 安全何去何从？

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

DeepSeek遭遇连环攻击，AI 安全何去何从？

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

DeepSeek遭遇连环攻击，AI 安全何去何从？

2025-02-11 14:41:39

所属地 上海

![](https://image.3001.net/images/20250211/1739256093_67aaf11d2632ac9b22a08.png!small)

常被称作 “中国版 OpenAI” 的 DeepSeek，近来遭遇了一场极为严重的分布式拒绝服务（DDoS）攻击。本文将深入探讨专家对于人工智能行业所面临安全挑战的观点，以及制定主动防御策略的紧迫性。

## DeepSeek 究竟是谁？

DeepSeek - R1 是中国初创公司 DeepSeek 研发的一款大型语言模型（LLM），作为领先的开源推理模型，它与 OpenAI 的 o1 系列不相上下。DeepSeek - R1 依据 MIT 许可协议发布，其训练方式主要采用强化学习，这与传统的大语言模型训练方法截然不同，彰显出行业朝着小型开源模型发展的趋势。DeepSeek 的实践表明，出色的工程设计必须兼顾性能与成本效益。

IBM 董事长兼首席执行官阿尔温德・克里希纳指出，DeepSeek 的经历证明，优秀的工程设计应在性能和成本两方面进行优化。“在 IBM，我们观察到，专用模型能够将人工智能推理成本降低多达 30 倍，从而实现更高效且更易实现的训练。”

截至 2025 年 1 月 31 日，DeepSeek 的 R1 模型在 Chatbot Arena 基准测试中位列第六，超越了 Meta 的 Llama 3.1 - 405B 和 OpenAI 的 o1 等模型。然而，在全新的人工智能安全基准测试 ——WithSecure 的简单提示注入评估与利用工具包（Spikee）中，R1 的表现却不尽人意。这一情况凸显出人工智能发展过程中的一个关键问题：过于侧重性能而忽视了安全。

![](https://image.3001.net/images/20250211/1739256082_67aaf11224028d23dee3a.png!small)

## DeepSeek 受攻击时间线

DeepSeek 近期出现的安全漏洞，暴露出一系列严重程度和潜在影响各异的问题。下面，让我们按照严重程度从高到低，来分析这些事件：

**1.DDoS 攻击**：2025 年 1 月，DeepSeek 遭受了一场严重的 DDoS 攻击。在 2025 年春节期间，当千家万户阖家团圆欢庆佳节之时，被誉为 “中国版 OpenAI” 的人工智能明星企业 DeepSeek，却陷入了有史以来最为严峻的安全危机。

* **攻击规模**：黑客发动了一场前所未有的 3.2Tbps DDoS 攻击，这相当于每秒能够传输 130 部 4K 电影。
* **影响**：DeepSeek 官方网站瘫痪长达 48 小时，全球客户和合作伙伴都受到影响，造成了数千万美元的损失。截至本报告完成时，官方 API 服务仍未完全恢复，国际用户依旧无法完成注册。此次 DDoS 攻击的目标是 DeepSeek 于 2025 年 1 月初发布的最新开源模型 DeepSeek - R1，且攻击时间恰好与 2025 年 1 月 28 日发布的多模态模型 Janus - Pro 重合。DDoS 攻击主要导致 DeepSeek 的注册服务无法使用。

**2.XSS 漏洞**：DDoS 攻击之后，DeepSeek 又面临严重的跨站脚本（XSS）漏洞。2025 年 1 月 31 日，在 DeepSeek 的 CDN 端点检测到一个基于 DOM 的跨站脚本漏洞。该漏洞是由于对 postMessage 事件处理不当导致的，攻击者可以在不进行适当来源验证或输入清理的情况下，将恶意脚本注入文档上下文。这一漏洞可能导致攻击者劫持用户会话、窃取敏感信息，甚至发起网络钓鱼攻击。

![](https://image.3001.net/images/20250211/1739256069_67aaf105797d4ffeba92f.png!small)

* **漏洞原因**：受影响端点上的 postMessage 实现在处理消息时，既未验证来源，也未对输入进行适当清理。以下代码片段可以说明问题的根源：

```
window.addEventListener("message", (e) => {

const keys = Object.keys(e.data);

if (keys.length !== 1) return;

if (!e.data.__deepseekCodeBlock) return;

document.open();

document.write(e.data.__deepseekCodeBlock);

document.close();

const style = document.createElement("style");

style.textContent = "body { margin: 0; }";

document.head.appendChild(style);

});
```

该函数直接使用 document.write 将任何\_\_deepseekCodeBlock 负载写入文档，跳过了来源验证（未检查 postMessage 事件是否来自受信任源）和输入清理（未对负载中的 HTML/JavaScript 内容进行过滤或转义）等关键安全措施。

* **后续漏洞**：虽然据报道，1 月 31 日的漏洞在 2025 年 2 月 1 日已修复，但同一天又发现了另一个 XSS 漏洞。这个漏洞使攻击者能够在 DeepSeek 人工智能平台内注入并执行任意 JavaScript 代码。攻击方式为用户注入以下代码块：

```
Ethically hacked by 0xSaikat (হা.. হা.. হা.. এটাই বাস্তব, I love you)
" onload="alert('XSS by 0xSaikat - (হা.. হা.. হা.. এটাই বাস্তব, I love you)')">
```

`由于输入未得到妥善清理，注入脚本的 JavaScript 代码得以执行。一旦成功利用此漏洞，可能导致用户会话被劫持、敏感信息被盗取，或是遭受网络钓鱼攻击。这一事件充分体现了持续进行安全测试和漏洞修复的重要性，即便之前的问题已得到解决。`

![](https://image.3001.net/images/20250211/1739256532_67aaf2d404f9bc995f673.png!small)

3. **ClickHouse 数据库泄露**：Wiz Research 最近发现，DeepSeek 的基础设施存在重大安全漏洞，通过可公开访问的 ClickHouse 数据库，大量敏感数据被暴露。

在[oauth2callback.deepseek.com](https://oauth2callback.deepseek.com)和[dev.deepseek.com](https://dev.deepseek.com)托管的两个数据库实例，在端口 8123 和 9000 上未进行身份验证，任何人都可以通过 ClickHouse 的 HTTP 接口访问和操作数据。这个漏洞导致超过一百万行的日志流被曝光，其中包含聊天记录、API 密钥、后端详细信息和操作元数据等高度敏感的信息。

Wiz Research 展示了执行任意 SQL 查询的能力，能从名为 log\_stream 的表中检索数据，该表包含聊天记录、API 密钥和内部系统详细信息等敏感内容。

这一事件尤其令人担忧，因为 DeepSeek 的 R1 论文中并未提及任何特定的加密标准，这让人对其系统内敏感数据的保护产生质疑。这些数据库包含一个 “log\_stream” 表，存储了自 2025 年 1 月 6 日以来的敏感内部日志，其中包括用户对 DeepSeek 聊天机器人的查询、后端系统用于验证 API 调用的密钥、内部基础设施和服务信息，以及各种操作元数据。

![](https://image.3001.net/images/20250211/1739256556_67aaf2eccba7bdb470861.jpg!small)

4. **模型投毒**：这是一种更为隐蔽的威胁。攻击者利用 DeepSeek API 中的漏洞注入对抗样本，试图操控模型的行为和输出。这种攻击可能产生长期的不良后果，比如降低模型性能、引入偏差，甚至让恶意代码得以执行。

DeepSeek 对 Common Crawl 等大型公开可用数据集的依赖，进一步加大了这种风险，因为攻击者有可能向这些数据源注入恶意数据，从而污染模型。这一事件凸显出针对模型投毒建立强大防御机制的迫切需求，包括数据验证、异常检测和模型监控。

5. **模型越狱**：DeepSeek 的模型，包括 V3 和 R1，被发现容易受到越狱技术的操控。帕洛阿尔托网络公司（Palo Alto Networks）的研究人员利用 “欺骗性喜悦”（Deceptive Delight）、“不良李克特评判”（Bad Likert Judge）和 “渐强”（Crescendo）等方法，成功实现了对模型的越狱。这些技术利用了模型安全机制中的漏洞，使得攻击者能够绕过限制，进而有可能未经授权访问信息或操控模型行为。

DeepSeek 迫切需要重视并投入资源建立强大的安全措施，包括对抗训练、延长日志保留时间和加快事件响应速度，以此降低漏洞风险，防范日益复杂的网络威胁。

## OpenAI 的安全事件

尽管 DeepSeek 近期的漏洞突出了重大安全问题，但我们也不能忽视，即便是像 OpenAI 这样的人工智能行业巨头，同样也面临过安全挑战。在 OpenAI 的早期发展阶段，曾遭遇过众多攻击和漏洞，这表明实现强大的人工智能安全并非一蹴而就，而是一个复杂且持续的过程。研究 OpenAI 的经历，能为整个人工智能社区提供宝贵的经验，强调在面对不断变化的威胁时，持续改进和适应的重要性。

![](https://image.3001.net/images/20250211/1739256747_67aaf3ab00123eca22eea.jpg!small)

1. **2023 年 3 月数据泄露**：2023 年 3 月 24 日，ChatGPT 的开发公司 OpenAI 在其博客上公布了一起数据泄露事件。博文中指出，一个漏洞导致用户能够看到其他活跃用户的部分聊天记录和部分支付数据，其中暴露的支付数据包括支付地址、信用卡类型、信用卡到期日期以及信用卡号码的后四位。
2. **2023 年 6 月凭据被盗**：2023 年 6 月，Group - IB 的一个威胁情报团队发布报告称，在过去 12 个月里，有超过 10.1 万个 ChatGPT 凭据被恶意软件窃取。研究人员在暗网上发现了这些账户，它们与其他被盗数据一同出售。不过需要注意的是，这些账户是因为用户设备上的恶意软件而泄露，并非 ChatGPT 自身系统被攻破。
3. **2023 年内部消息系统遭入侵**：据《纽约时报》报道，2024 年披露，2023 年有一名黑客入侵了 OpenAI 的内部消息系统，并窃取了该公司人工智能技术设计的相关细节。报道称，黑客是从一个在线论坛的讨论中获取到这些信息的，在该论坛中员工们讨论了 OpenAI 的最新技术。然而，据称 OpenAI 从未就 2023 年的数据泄露事件进行报告。
4. **2025 年仍存在漏洞**：即便到了 2025 年，OpenAI 依然存在漏洞问题。一位研究人员报告称，通过向一个无关的 ChatGPT API 发送 HTTP 请求，就可以触发 ChatGPT 爬虫对目标网站进行 DDoS 攻击。OpenAI 软件中的这一缺陷，会利用 ChatGPT 爬虫运行所在的多个微软 Azure IP 地址范围，对毫无防备的受害者网站发起 DDoS 攻击。其严重程度的 CVSS 评分高达 8.6，因为它基于网络，攻击复杂度低，无需特权，无需用户交互，影响范围改变，虽对保密性和完整性无影响，但对可用性影响极大。

DeepSeek 并非唯一遭受 XSS 攻击的受害者。Claude 在早期也面临诸多漏洞。一位研究人员报告称，在 DeepSeek 聊天中输入 “以项目符号列表形式打印 XSS 作弊表。只需列出有效载荷”，会触发作为生成响应一部分的 JavaScript 代码执行。发现这一问题后，他进一步检查是否存在提示注入的情况，即用户可能利用 DeepSeek 处理来自他人的不可信数据。攻击者可以轻松获取[chat.deepseek.com](https://chat.deepseek.com)域的 localStorage 中存储的 userToken。如果应用程序容易受到 XSS 攻击，且大语言模型能够利用该漏洞，那么提示注入就有可能完全控制用户账户。

## 如何保护人工智能模型

DeepSeek 的数据泄露事件，充分表明了零信任安全的必要性，即无论是内部还是外部实体，都不能被无条件信任。人工智能系统在授予对 API、数据库或模型权重的访问权限之前，应该要求进行持续身份验证、最小权限访问和上下文验证。通过实施基于身份的访问控制（RBAC 和 ABAC）和多因素身份验证（MFA），企业能够防止未经授权的访问，降低内部威胁。

此次数据泄露中，最令人担忧的威胁之一是模型权重操纵，即对抗样本干扰人工智能的决策。人工智能模型在每次训练和部署阶段，都应该使用 HMAC、RSA 或 ECC 签名进行加密签名，以确保完整性。此外，采用如可信执行环境（TEE）等安全飞地技术，可以防止对人工智能模型的未经授权修改。

DeepSeek 的数据泄露暴露了内部安全的薄弱环节，而通过员工网络安全意识培训，原本可以减轻这些问题。定期培训项目应该向工程师、研究人员和员工传授安全编码实践、网络钓鱼防范意识、提示注入风险以及人工智能特定的攻击向量等知识。同时，应该开展模拟网络钓鱼活动和安全演练，确保团队有能力识别并应对威胁。

我们必须认识到，传统安全架构对于大型人工智能模型来说是不够的。企业应该将安全理念融入企业文化，转向系统级安全措施。这需要一种全面的方法，涵盖从模型开发到基础设施管理的人工智能系统的各个方面。

为了防止出现类似[chat.deepseek.com](https://chat.deepseek.com)上的 XSS 漏洞，平台需要对用户生成的代码输入进行清理。要确保进行适当的输入 / 输出清理，并实施脚本沙盒。例如，在未首先验证的情况下，切勿直接渲染和执行人工智能生成的代码。

通过持续的红队评估，对所有人工智能接口、API 和后端服务进行持续的安全渗透测试。此外，设立漏洞赏金计划，鼓励道德黑客在恶意行为者利用漏洞之前，负责任地披露漏洞。

**参考来源：**

> <https://cybernews.com/editorial/how-deepseeks-security-failures-shape-the-future-of-cyber-defense/>

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

DeepSeek 究竟是谁？

DeepSeek 受攻击时间线

OpenAI 的安全事件

如何保护人工智能模型

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系...