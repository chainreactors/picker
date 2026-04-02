---
title: 登顶顶会 ｜ BlockSec 与浙江大学联合论文入选 FSE 2026：AI 审计，离真实安全研究更近了一步
url: https://mp.weixin.qq.com/s/KdFjZQjYQ4SshJGBF58Mwg
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:24:49.217758
---

# 登顶顶会 ｜ BlockSec 与浙江大学联合论文入选 FSE 2026：AI 审计，离真实安全研究更近了一步

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ibKZs4Hxyqtzxm5n3gFH9OSVWbicpNAeicpic0qyzhQ6Lfpts3P7GzqQjLOicpqPDVMW4rUegHsa8wpxMg4WXrGQPdGk6ZqU9k6OHm9nwdMrdXw/0?wx_fmt=jpeg)

# 登顶顶会 ｜ BlockSec 与浙江大学联合论文入选 FSE 2026：AI 审计，离真实安全研究更近了一步

原创

BlockSec
BlockSec

BlockSec

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2ibKZs4Hxyqsw9TNE6dA58o4kxGOwKgvH6KJiccfwbektvvCPmyl3Wb9E81EOtiaZU9mMUp9HIED13BGyluv3qicuYs09oia48xAgW2mM9ux0nl0/640?wx_fmt=gif&from=appmsg)

BlockSec 与浙江大学联合完成的研究论文 **《Thought is All You Need: Smart Contract Vulnerability Detection with Thought-Augmented Large Language Model》** 已被软件工程顶级会议 FSE 2026 收录。

这不仅代表我们的研究成果获得了顶级会议的认可，也说明 BlockSec 长期积累的审计经验，可以被整理成一套系统，在真实场景中跑出可验证、可复现的结果。

FSE（ACM International Conference on the Foundations of Software Engineering）是软件工程领域的顶级会议之一，本届会议将于 2026 年 7 月 5 日至 9 日 在加拿大蒙特利尔举行。

**现有 AI 审计卡在哪里**

先看一组论文中引用的已有研究数据，当前 AI 审计大致处于以下水平：

* GPT-4 和 Claude-1.3 做漏洞检测时，误报率曾高达 95%。也就是说，报出 100 个"漏洞"，95 个是假的。
* GPTScan 把 GPT 与静态分析结合，在大规模项目中的检测准确率约 57%。
* 一些号称用上了"漏洞知识库"的 RAG 方法，即便只做漏洞类型识别这种相对简单的任务，准确率也只有约 30%。
* 直接使用 GPT-4o、o3-mini、Claude 等最新模型做零样本检测，F1 分数仅在 0.241 至 0.311 之间。

这些结果放在一起，已经可以看出目前AI审计的主要问题。大模型当然有价值，但很多方案的做法仍然停留在同一个层面：把整份合约放进上下文里，让模型自行判断哪里可能有问题。

但真实审计并不是这样开展的。经验丰富的研究员通常不会平均扫描所有代码，而是会先判断哪些位置值得重点分析，再围绕关键函数、状态变量和业务流程向下展开。过去的 AI 审计，真正缺少的就是这套工作方式。

围绕这个问题，论文提出了 Synapse。它是一套面向智能合约漏洞检测的系统，目标是把安全研究员在真实审计中的关键步骤拆出来，交给系统分阶段完成。简单来说，Synapse 想让 AI 更接近安全研究真正的工作流程，而不只是再试一次让大模型读代码。

这也是 Synapse 试图解决的问题。在同样的测试条件下，Synapse 的 recall（真实漏洞找回率） 达到 71.9% 和 76.5%，约为已有 LLM 路线的 3 倍。进一步放到 BSC 链上的真实合约中测试，Synapse 发现了 117 个未知漏洞，而对照的 baseline 工具只识别出其中 8 个。其中一个关键漏洞，涉及约 3000 万美元的潜在资产损失。

**把真实的工作方式拆解成流程**

Synapse 的核心，是尽可能的把安全研究员在真实审计中的工作方式，拆解成一套系统能够执行的流程。

**一、把真正值得看的地方找出来**

真实的智能合约动辄几千行代码，但针对特定漏洞，真正需要看的可能只有几十行。Synapse 引入 Focal Context（焦点上下文），先定位高风险区域，再让模型集中分析。

这与真实审计的阅读方式是一致的。研究员分析代码时，通常会先关注关键函数、状态变量和核心业务逻辑。Synapse 只是把这一步前置了。实验结果显示，一旦去掉这个组件，recall（真实漏洞找回率）就会从 72.5% 下降到 52.8%。

**二、把审计经验转成可复用的判断框架**

Synapse 从 14,000+ 份真实审计报告中提炼出漏洞推理模板，形成 Thought Buffer（思维缓冲区）。它是一套结构化知识：遇到这种代码模式时，应该从哪几个角度分析风险。

例如面对一个提币函数，系统不会只做泛化阅读，而是会更有针对性地检查权限控制是否充分、重入保护是否完备、余额计算是否存在风险。这个过程依赖的是长期审计经验的沉淀，远超一次性的 prompt 技巧。

这一部分拿掉以后，recall（真实漏洞找回率）会从 72.5% 下降到 46.2%，影响非常明显。

**三、通过分工协作把结论做实**

Synapse 设计了 Developer（开发者）、Researcher（研究者）、Auditor（审计员）、Verifier （验证员）等多个角色，配合语义搜索、代码分析等工具完成检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ibKZs4Hxyqv4ZFLAwfiavKhIEdbvjOYLZFicdOed6qsmKYqg2PdDxQeib7PXiaic8ag1dcCMXrUAowqOJXa4T0I4dEyEusxnhtcw6rFtMBtQUQEQ/640?wx_fmt=jpeg)

Synapse 工作流

这里真正重要的是分工本身。理解代码、提出漏洞假设、交叉复核、确认结论，在真实审计里本来就是不同性质的工作。很多时候，难点并不在于发现线索，而在于确认这条线索是否成立。Verifier 角色的价值就在这里。

如果拿掉语义工具这一层，recall（真实漏洞找回率）会下降到 43.6%。这也说明，Synapse 的提升来自几个关键部分共同作用。

**基准测试**

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4HxyquqaZsHZ2BG7ECllyyQMnn1cibDhVvq1qqat4aPZAuaOiahibyKP9R1PJ57Tq6DThUPtQbCOtz01giaUsMyCFDvaoaiabw3I2j9qmyI/640?wx_fmt=png&from=appmsg)

Synapse 与现有工具主结果对比

在两个真实世界数据集上：

* Incidents 数据集：Synapse recall（真实漏洞找回率）71.9%，F1 73.1%；GPTScan 仅 10.8%
* DeFiHacks 数据集：Synapse recall（真实漏洞找回率）76.5%，F1 63.4%

与传统静态分析（Slither）、模糊测试工具（ItyFuzz）相比，平均也有大约 2 倍的提升。

消融实验

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4Hxyqtdx6icecgupt0d2uLYBVwZiaasWDK51ViakBzttsmzTfZZDR5s7soC2eaO6CB1vSr6wIEnISxzsE9KetOMAdbA1GUvM0qoWOR2bY/640?wx_fmt=png&from=appmsg)

关键组件消融实验（采用当时最新模型）

消融实验最能说明问题。直接使用 GPT-4o、o3-mini 或 Claude 做零样本检测，F1 基本都在 0.3 左右；加入 Synapse 的完整流程后，系统 F1 提升到 **0.723**。

**链上实测**

2025 年 2 到 3 月，我们在 BSC 链上测试 Synapse：

* 发现 117 个此前未被发现的漏洞，全部为 High 级别。
* 对照组 baseline 工具仅识别出其中 8 个。
* 其中一个关键漏洞涉及 约 3000 万美元 的潜在资产损失。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ibKZs4Hxyqv2aibLd5ia71ofoXpedmmqs2OiaJ5RskswjyvSzJxYCrw6nURoeTAkBsaY1rY2I6UjMTH1sAIaMuLsC4VkMbrKmnqeexoD1mKtIc/640?wx_fmt=jpeg)

BSC 真实链上检测结果

**这对 BlockSec 意味着什么**

Synapse 的Thought Buffer（思维缓冲区）来自 14,000 多份真实审计报告的蒸馏，Focal Context（焦点上下文） 的设计依赖对合约安全分析流程的深入理解，多角色架构的划分映射的也是我们在真实审计工作中的方法拆解。这些都不是纯粹的学术构造，而是我们长期积累的安全经验和工具链能力在研究层面的系统化表达。

换个角度说，这篇论文也证明了一件事：来自产业一线的安全理解，可以被组织成经得起顶级学术会议评审的方法论。模型 API 谁都能调，但把真实世界的审计经验转化成结构化、可验证、可复现的系统，门槛要高得多。

这也是我们一直在做的事情。从安全审计服务，到 Phalcon 等安全产品，再到这类研究工作，底层逻辑其实是一致的：把对真实攻击面和风险路径的理解，转化成可复用、可验证、可落地的能力。围绕 Synapse 形成的检测思路、工具能力和工作流设计，已经纳入 BlockSec 的整体审计流，用来提升真实项目中的审计覆盖、问题筛查效率和复杂逻辑漏洞的发现能力。

**人仍然不可替代**

71.9% 的 recall（真实漏洞找回率）和 117 个真实漏洞是很强的结果，但在安全领域，71.9%还远远谈不上万无一失，安全需要的是100%，只要误判一次、漏判一次，代价都可能非常高。

LLM 仍然存在 hallucination 问题，在事实一致性和推理忠实性上有天然风险。Synapse 更擅长的是依赖语义理解的复杂逻辑漏洞，并不能替代传统工具处理所有 machine-auditable bugs。

真实的安全审计远不止模式识别。理解协议设计中的隐含假设，判断攻击者最可能走哪条路径，在不完整信息下排列风险优先级，在多个看起来都有问题的发现中决定哪些值得上报。这些判断，今天仍然只能由人来完成。

我们认为AI审计的方向是 human-in-the-loop：AI 负责更广的覆盖面、更快的初筛和更低的边际成本；人负责最终的判断、复核与决策。Synapse 把 AI 能做到的事情往前推了一大步，也让我们在 AI 安全审计这条路上的方法论轮廓变得更清晰。这套能力的价值，也在我们与客户的长期合作中得到验证。

BlockSec 审计客户反馈

Manta：BlockSec 的监控体系覆盖链上合约监控、Token 余额变化、关键事件触发等常见风险点，也支持异常触发后自动执行预设动作。Manta 的 CeDeFi 产品和 Sequencer 均已接入这套监控体系。在生态项目遭遇攻击时，BlockSec 能够第一时间捕捉异常交易，协助快速冻结相关黑客地址。Manta 也提到，BlockSec 的审计能够深入到合约实现细节和具体业务逻辑，问题定位和修改建议都比较清晰、可执行。

DeltaPrime：协议在 2022 到 2024 年间已经做过 9 次审计，但在 2024 年底仍然连续遭遇攻击。此后，团队与 BlockSec 启动了一次持续数月的深度审计，最终识别出 39 个潜在安全问题，并收到 32 条代码修改建议。这一次审计带来的发现数量，已经接近此前 9 次审计结果的总和。

如果您正在寻找更专业的智能合约审计与安全防护支持，欢迎点击【阅读原文】，进一步了解 BlockSec 的审计服务与安全产品能力。

**论文作者：**

彭超源 (浙江大学)

姜木慧 (BlockSec)

周亚金 (BlockSec)

吴磊 (浙江大学 & BlockSec)

---

关于BlockSec

BlockSec 是全球领先的区块链安全和合规公司，于 2021 年由多位业内知名专家联合创立。BlockSec 致力于提升 Web3 世界的安全性和易用性，提供一站式安全服务，包括智能合约/链/钱包安全审计服务、协议安全和数字货币合规(AML/CFT)平台 Phalcon Security / Phalcon Compliance / Phalcon Network、资金追踪调查平台 MetaSleuth和区块链交易分析工具 Phalcon Explorer 等。

目前，BlockSec 已服务全球逾 500 家客户，既涵盖 Web3 知名公司 Coinbase、Cobo、Uniswap、Compound、MetaMask、Bybit、Mantle、Puffer、FBTC、Manta、Merlin、PancakeSwap 等，也包括了权威监管机构及咨询机构，如联合国、SFC、PwC、FTI Consulting 等。

官网：https://blocksec.com/

Twitter：https://twitter.com/BlockSecTeam

推荐阅读👇

[![](https://mmbiz.qpic.cn/mmbiz_jpg/icl4OTbk4icTJKnQAjhicg47N8sLY3SKzqlEcnuEf3pYzPTIqpar2ibkeSeCvjqQsKrLwZwWyTcAXIazKXLQIXEchQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyMzI2NzIyMw==&mid=2247490504&idx=1&sn=ed76941ba8ee144bdd12cb0ddb7df70c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/icl4OTbk4icTIje0g9kj9ic4b9GEzwpo1TCWq94NdL91n7Yt1FYkWUmPEXrkGzHKNvuQbOlu36LFXShpNOTklWvKw/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyMzI2NzIyMw==&mid=2247491200&idx=1&sn=f0a133511ca63c3deb086c51654e4157&scene=21#wechat_redirect)

#BlockSec

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTKWV4NZYNjUicibdl9UQ4HibVfGa4a6ypSMKArRmWBI3Nibibicuo7YJbQibOC8XKvSMJXYGRFWIz3hsvvfA/0?wx_fmt=png)

BlockSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTKWV4NZYNjUicibdl9UQ4HibVfGa4a6ypSMKArRmWBI3Nibibicuo7YJbQibOC8XKvSMJXYGRFWIz3hsvvfA/0?wx_fmt=png)

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