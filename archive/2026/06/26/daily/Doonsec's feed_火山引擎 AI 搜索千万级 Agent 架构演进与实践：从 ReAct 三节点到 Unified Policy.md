---
title: 火山引擎 AI 搜索千万级 Agent 架构演进与实践：从 ReAct 三节点到 Unified Policy
url: https://mp.weixin.qq.com/s/hol76ebv7-OB5TNUIWVVYA
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:48:30.936080
---

# 火山引擎 AI 搜索千万级 Agent 架构演进与实践：从 ReAct 三节点到 Unified Policy

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FGB4hYw9FeeaoxDrhp1DYX5ZEqMer5o4huQDC8VhmwLZKHxiaYgnibcVEjKBc3efd25FkmRKgkO8oO2dkdR3HbDiaDECbDAicrRDI8glzY7tRDM/0?wx_fmt=jpeg)

# 火山引擎 AI 搜索千万级 Agent 架构演进与实践：从 ReAct 三节点到 Unified Policy

字节跳动技术团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于VikingAI搜索
，作者Viking 工程师

![](http://wx.qlogo.cn/mmhead/hIz3ylFIYSibQpxAKIKEPiaW0ic0Vnlyubniazicibqaicyma3lQkeh3bNOYQUTuctzUgoQ5beWaVaoCjc/0)

**VikingAI搜索**
.

火山引擎 Viking AI 搜索，助力企业快速打造多模态检索、个性化推荐和对话 Agent 能力！

**导读：**

当 Agent 技术彻底跨越 Demo 玩具阶段，真正挺进千万级并发的企业级生产环境时，传统的 ReAct 架构开始暴露出节点臃肿、延迟极高、状态管理混乱的致命缺陷。本文深度拆解火山引擎 AI 搜索团队如何重新定义 Workflow 与 Agent 的系统边界，通过构建 **Unified Policy Agent （UP-ReAct）** 架构，在实现推荐与对话效果大幅提升的同时，将首字返回时间（TTFT）暴降 30%。这不仅是一次代码重构，更是对工业级 Agent 设计哲学的底层重塑。

**一、****工业级大考：为什么企业级 AI 搜索必须重构 Agent？**

过去一年，大模型应用赛道的竞争逻辑已经发生了根本性转移。评判一个 Agent 是否优秀的标准，不再是“它能不能通过复杂的 Prompt 调用外部工具”，而是“它能不能在真实、高并发的业务流水线里，以低延迟、高稳定、低成本的方式持续运转”。

随着模型在规划（Planning）、工具使用（Tool Use）和长上下文（Long Context）上的能力跃升，业界开始将越来越长的业务链路委托给 Agent 处理。然而，对火山引擎 AI 搜索而言，我们面临的工程挑战天然比单点聊天助手（Chatbot）高出几个数量级。

火山引擎 AI 搜索并不是一个简单的问答框，而是一套面向 ToB 企业的“搜、推、问一体化”智能引擎。它需要同时满足：

* **多模态检索：** 处理文本、图像、视频素材的混合召回。
* **个性化推荐**： 结合用户画像与实时偏好进行深度排序。
* **多轮对话交互**： 在电商导购、内容社区、企业知识库等数十种迥异的行业场景中，维持连贯的业务逻辑。

在这种极端复杂的场景下，ToB 用户不会为“看起来很聪明但经常超时”的系统买单。他们最在意的是：**系统的确定性够不够高？首字响应是不是极致的快？接入新业务线时架构会不会无限膨胀？**

这也引出了当前企业级 AI 搜索 Agent 最大的痛点：**上下文工程（Context Engineering）的失控**。上下文并不是越多越好的“垃圾桶”，而是一种极其昂贵且有限的计算资源。企业级系统真正的难点在于：谁来负责确定性流程？谁来负责开放式决策？哪些信息必须进入 Prompt？哪些信息应该被无情压缩或驱逐？

如果我们继续试图将所有的业务复杂性都揉进一个“无所不能”的 Agent 中，系统最终会被不可控的幻觉、高昂的 Token 成本和灾难性的延迟所拖垮。我们需要的是一套能**剥离确定性与不确定性、分离策略决策与上下文管理的现代 Agent 架构**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FedxSBU0EqPH84NfaOdfj7wqVWLn7VT78tWUHyj4NyBkB0oYiaoqPTaujicIhicD7nic0zYIhvCZfrlfEPvg48ibIxl0EohlvdQR0NjM/640?wx_fmt=png&from=appmsg)

**二、****旧日支配者：标准 ReAct 架构在深水区的工程原罪**

在技术探索早期，ReAct（Reason + Act）提供了一种极其优雅且符合直觉的范式：先思考（Thought），再行动（Action），最后根据观察结果判断是否继续（Iteration）。对于简单任务，这套逻辑无可挑剔。但当它被生搬硬套进包含搜推问多链路的千万级并发系统时，三大“工程原罪”开始显现。

**1、****极高的时间复杂度与调用惩罚**

在标准的三节点 ReAct DAG（有向无环图）中，模型每执行一次有效动作，都必须经历三次独立的决策流转。

我们可以用公式量化这种延迟代价。假设单次模型推理的平均耗时为 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5MTsCmIkR4aIdy1V0ZAz3piaMMLDsXbwnvV5OcDMrygWyfX7Ez6Ytfh1GJfBY1cxeLblbGBz4ApoBicKkKmoFiaaryqAe39putG28RibNs7pict1Q/640?wx_fmt=svg&from=appmsg)，工具执行耗时为 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4vVUuWtsNeEpek4YOFhltichCCaGmPE4b6tEC7UN6qFP00SRpsk4jdkibBia0zy4xDwZTopBgwPiaeQYCXib7sVJxViabb7fy3yk5gr2nkmDPKkTsw/640?wx_fmt=svg&from=appmsg)，网络 IO 与节点流转耗时为 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5Dic4bDEhKwibicDGTseFAOdibjJaO8LSAibehQXiboJhTkrtS8pTHaw8cyqPAYnq0Via6NJJR5LnQrjjcATcYn0da0WFfCOIC6Im48Vok4OT70O83A/640?wx_fmt=svg&from=appmsg)。在旧架构下，完成一次工具调用的全链路时间成本 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7icqpRJmmdb5nuiaDvJSFKiabj1KcgvWIiazdsSLvx3leyjJVmIxt8wAoia65XQABznx2J3aSBjZ8DOPMfbvesEO9yMtwjia0pjXCspmmdDKOibZDCA/640?wx_fmt=svg&from=appmsg) 为：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM79Id11Reic0zH3nDSO0jILbF9tEJcOH9cOQAThnULxbbJO418lLOm2v0fmHJH2yLQpTj7LwYfmibGp8RXEgbohicJXnuFViaxWKhxY7drRBjvdcg/640?wx_fmt=svg&from=appmsg)

在真实生产环境中，这不仅意味着原本 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7JJ4vwMibEstibkeianmyKiabGkfeC7EVsdVKYibVlavSYQN45Da5YMvXDjkm2AmwtpEw4GFHjQcl5te6JGrQ3UFuvE09bYXGWC4T2YMnmluc8h4A/640?wx_fmt=svg&from=appmsg) 的任务被强行拆成了 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7oCGm1sv05ibKGp7UXBrI06OPysw1dh8bdyWX5Wa4LHTrC2meEMpgr23dAknobAS8Mdib4ica11RUCNS2QscLribibv8f1t9RxwDrLVIBYFwELwBw/640?wx_fmt=svg&from=appmsg)，更导致了首字返回时间（TTFT）的急剧恶化。Token 的无谓消耗和并发压力的激增，使得这种架构在算力成本面前显得极为奢侈。

在真实生产环境中，这不仅意味着原本 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6qSAMLiaq3ib0kmhJumvicANIPY4jXyBtc25QPWl9GhIJ6Wp25KskPXtHUlk5aKtAgfbFddLicg0xicAo9ZfoNE7hPNuPiaWzXC5Dh5t0YOFs4gOnA/640?wx_fmt=svg&from=appmsg) 的任务被强行拆成了 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6ma7h5E3lvicAibGiaPtR6eiauOXJWYaicXmD61TgvRNOibT2QuSiaXghn39J0SS0W5WYJRoNDdD9DeiarlTKSxhZyIg1WgWboia9UaY4lrkBffEPpnLw/640?wx_fmt=svg&from=appmsg)，更导致了首字返回时间（TTFT）的急剧恶化。Token 的无谓消耗和并发压力的激增，使得这种架构在算力成本面前显得极为奢侈。

**2、****上下文震荡（Context Thrashing）与注意力稀释**

三节点拆分导致了一个致命隐患：**状态的重复搬运**。Thought 节点需要读取历史对话，Action 节点需要读取 Thought 的输出，Iteration 节点又要重新理解前两者的状态以决定是否终止。

同一份业务状态在节点间反复序列化与反序列化，导致 Prompt 长度呈指数级膨胀。这不仅推高了显存占用，更引发了模型注意力的严重稀释（Attention Dilution）。模型在浩如烟海的中间推理步骤中，极易遗忘最初的用户真实意图。

**3、****控制流破碎与系统语义模糊**

在生产级 AI 搜索中，Agent 从来不是静态的。业务方今天要求接入“企微画像补全”，明天要求接入“实时库存查询”。

在 ReAct 架构下，这些新工具很难自然融入 Thought-Action 循环。例如，一个纯信息补充类的工具调用完毕后，并不需要 Iteration 节点去判断“是否退出”（因为它一定不退出）。为了绕开无效的 Iteration，工程师只能在 DAG 中硬编码各种 If-Else特判逻辑。久而久之，“优雅的智能架构”退化成了一座布满补丁的屎山代码。系统的控制权被撕裂：Thought 在规划，Action 在翻译，代码逻辑在强行路由。

**本质上，当业务规模突破阈值，继续在 ReAct 的尸体上打补丁是徒劳的。我们需要重新定义控制流。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9Fedibia5RibzbiabuYj5uYcXZ89PtaOeUjx3IMy8lt3z0tGz2rTU9WuGkichzWTh7KxhYPBV1IRhr0IozaOWFsOWjciccibAXsPia1ycGWs/640?wx_fmt=png&from=appmsg)

**三、****行业演进与共识：从 Prompt Engineering 到 System Engineering**

时间推移至 2025-2026 年，业界顶级 AI 团队（如 OpenAI、Anthropic）在生产级 Agent 的设计思路上达成了惊人的共识：**少谈些奇技淫巧的 Prompt，多讲点扎实的 System Engineering**。

* **共识一：****Workflow 与 Agent 必须严格分层**。 预定义路径、硬规则校验、权限控制必须留在传统 Workflow 代码中执行；Agent 只负责在环境反馈中做动态策略决策。不要用 LLM 去做普通的 switch-case。
* **共识二：****万物皆 Tool（Contract）**。 工具不再仅仅是 API 调用，而是 Agent 与外部世界的“强契约（Contract）”。工具的输入 Schema、输出质量、容错能力，比 Agent 自身的推理能力更决定系统的下限。
* **共识三**：**上下文管理的独立化**。 面对动辄千百个工具库，全量加载不仅昂贵且极其低效。按需加载（Progressive Exposure）和状态压缩（Compaction）成为长程任务的生命线。
* **共识四：****生产级工程评测（Eval）**。 仅靠“回答得好不好”已经无法衡量系统质量。代码判分、中间态阻断率、工具调用准确率构成了多维度的 Eval 体系。

火山引擎 AI 搜索团队高度认同并践行了这些共识。我们将系统彻底解耦，推出了全新的 **Workflow + Unified Policy Agent 架构**。

**四、火山引擎的破局重构：Workflow + Unified Policy Agent**

为了彻底解决“既要大模型聪明，又要系统轻快”的矛盾，我们将整个 AI 搜索链路一分为二：**确定性归 Workflow，动态决策归 Agent**。

**4.1 楚河汉界：明确分工体系**

* **Workflow 层（坚如磐石的确定性骨架）**：
* 负责接管所有无需 LLM 决策的前置工作。包括：风控校验、意图路由分类、用户画像预加载、基础倒排索引召回、本地配置读取等。例如，在电商搜索中，“必须先过滤无库存商品”这是一个绝对的业务红利规则，将它硬编码在 Workflow 中，远比指望 Agent 每次都“想起”调用过滤工具要可靠得多。

* **Agent 层（纯粹的动态决策中枢）**：
* 当复杂请求穿透 Workflow 进入 Agent 后，它不再承担任何“干脏活”的静态任务。此时的 Agent 被剥离得极其纯粹——它只基于当前收敛后的上下文，决定下一步采取什么动作（检索、计算、推荐、总结或直接抛出答案）。

**4.2 Unified Policy：重聚破碎的控制权**

如果说内外分层解决了“谁干什么”的问题，那么**Unified Policy** 则解决了 Agent 内部“如何控制”的问题。

我们无情地砍掉了 Thought、Action、Iteration 三个散装节点，将其统一收敛为单一的 **Policy 节点**。这个全能中枢单次前向传递即可完成三件事：

1. **全局规划（Planning）**： 基于目标分析当前缺失的信息。
2. 动作选择（Action Selection）：直接输出结构化（JSON Schema）的决策指令，而非先输出自然语言再由正则提取。
3. 终止判定（Termination）： 判断目标是否满足，满足则生成最终态输出。

通过这种架构，我们将前文提到的时间复杂度由 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5V4Ikic5ibA6bEpd933ibv78lDkZXCqiaVqH3yiaAUEmjL6AZrqkpzd1XjRlyQtt8CptwHXic9O3fwia4pGszrQ7bmxEE3F1etHHpbdZXtXPWwvJicJw/640?wx_fmt=svg&from=appmsg) 降维打击至 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5VhmxVZdtXtZoXJXCuGpT41kO2xDPjibmK3F21AUg7GHeLemmS3wjoRZoGXBHTBucq30fNiadJYQ0lQAJgorIdic7QYX6JIQP95LiccP6xLuibL3A/640?wx_fmt=svg&from=appmsg)：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6jBTasV1tV2kj5NInVhsrBECK4F3FFic8XxvHLWV1iblsMr36gzXs1qR6aXCC4ra7Fs35LHxtHnzPULn7y73tnORfJThRmIcnfpgWqPScDM46g/640?wx_fmt=svg&from=appmsg)

系统不仅少跑了冗余节点，更在语义层面明确了“大脑”的唯一性，彻底消灭了控制逻辑在多个 Prompt 中打架的乱象。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FefK1lzFUTwrQrL4bk2zh2sIQjanhRdy6tPWwjTeIvlxQZibB4C3e1nySREUMy0gSJmPMvoibObgcx33LqUd6n4x6NfbT0E07zDhI/640?wx_fmt=png&from=appmsg)

**五、架构深度解剖：支撑千万级调用的「三个统一」**

表面看，合并节点只是工程重构；但在系统抽象层面，火山引擎 AI 搜索完成了一次哲学级别的重塑。我们将 Agent 内部运转的三大核心要素——**控制、行为、状态**——完美收敛为“三个统一”。

**5.1 统一控制：Policy 独裁中心**

如前所述，Policy 取代了松散的议会制，成为了独裁的决策中心。它使得链路监控变得极度清晰：如果 Agent 抽风了，不用再排查是翻译错了还是理解错了，直接 Dump 当前的 Policy 状态日志即可定责。它大幅降低了二次开发的认知负担。

**5.2 统一行为：万物皆 Tool 的泛化抽象**

在旧系统中，系统的“行为”是割裂的：查天气是 Tool 调用，退出思考是特殊的字符串标记，进行深度总结是 DAG 分支里的隐式流转。这种设定让系统的动作空间（Action Space）难以被穷举和优化。

在 Unified Policy 中，我们强制规定：**所有系统级别的主动行为，必须被抽象封装为标准的 Tool**。

* search\_database\_tool：常规的外部数据获取。
* exit\_and\_reply\_tool：显式的终止动作，携带最终要发给用户的 Payload。
* deep\_think\_tool：当面临财报分析等需要复杂推理的节点时，主动调用自身的高级推理算力。
* load\_tenant\_config\_tool：按需拉取特定租户的业务说明文档。

**架构红利**： 当“退出”和“思考”都变成了标准 API，大模型的动作空间变得完全可枚举且可校验。接入新能力再也不用修改任何核心 DAG 代码，只需注册一个新 Tool 即可。

**5.3 统一状态：Context Manager 捍卫内存防线**

这是...