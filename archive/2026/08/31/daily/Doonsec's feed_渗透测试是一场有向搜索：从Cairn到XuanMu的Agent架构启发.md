---
title: 渗透测试是一场有向搜索：从Cairn到XuanMu的Agent架构启发
url: https://mp.weixin.qq.com/s/xKwWjPTIBO-HBWuGe6V68g
source: Doonsec's feed
date: 2026-08-31
fetch_date: 2026-09-01T06:55:57.820761
---

# 渗透测试是一场有向搜索：从Cairn到XuanMu的Agent架构启发

# 渗透测试是一场有向搜索：从Cairn到XuanMu的Agent架构启发

哈啰安全应急响应中心 HSRC

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

*渗透测试是一场有向搜索：*

*从 Cairn到 XuanMu*

*的Agent 架构启发*

**01**

渗透测试的本质，

其实是一场"有向搜索"

![](https://mmecoa.qpic.cn/sz_mmecoa_png/C0tk9icZjs9QD7yB9yN7MPibyC9t6EWt0ia1jVKL99N3j0HkxBUJIW2u8bIugXFIH9KWAKlbWUfdyV8awI0dUicaWNfiaic2FnuFgLR2UXXnAIgFY/640?wx_fmt=png&from=appmsg)

先问一个问题：渗透测试到底在做什么？

——**渗透测试是一次近乎无限状态空间中的有向搜索。**

![](https://mmecoa.qpic.cn/sz_mmecoa_png/C0tk9icZjs9Q08QjFGurTJVXMenoicopETgVXcS5ZJibJC7Rdrg3zqLqlib5VzrMAzpiaVLUU4NibtibMq4rKJriaN30utb5TlFUibtUaj7yafQLgtwk/640?wx_fmt=png&from=appmsg)

起点是已知、确定的：目标 IP。终点是明确的，但路径未知：拿到 Shell。中间是一片边界不明的雾区，你会不断遇到新节点（迷雾散开）、找到有价值的通路、也会一头撞进死胡同。

这片状态空间有两个特征：

* **无限：**事先无法完全枚举，每一个新发现都可能展开全新的维度；
* **有向：**你始终朝着目标前进，不是漫无目的地乱逛。

信息收集，就是你在这片空间里移动的方式——每一次收集，都是从已知迈向未知的一小步。渗透测试的结构，说到底就是一条从起点到终点的路径，穿过这片近乎无限的未知区域。

这个抽象很干净，也很关键。因为接下来要介绍的两个开源项目——**Cairn 和 XuanMu**，它们的整套架构设计，几乎都是从这句话直接推导出来的。

**02**

Cairn：用登山者垒石头的方式，

给 Agent 搭一块共享黑板

Cairn：https://github.com/oritera/Cairn（Github地址）

Cairn 这个名字本身就是一个隐喻——它是登山者用石头垒起的路标。

每一块石头，是前人留下的确认信息；

后来者沿着这些路标继续往前走，同时也为下一个人垒起新的路标。

这恰好对应了 Cairn 这套系统的核心设计：**一块所有 Agent 共享的黑板。**

黑板上只有三种东西：

![](https://mmecoa.qpic.cn/mmecoa_png/C0tk9icZjs9SGbUBhEBoJBfnQiaP2EEicSZdicwLe8aYdZTYBzIXz4fFWPtflTnCJhchdYCSxKdUdicRYcx3BsUicN3oTyN005uia2w4biaicibjfht2Q/640?wx_fmt=png&from=appmsg)

整张图从“目标 IP 已知”这个起点开始生长，一步步朝着“拿到 flag”这个终点靠近。每个新 Fact，都是一块已经踩实的石头；每条 Intent，都是踩向未知的下一步。

如果换成更具体的场景，这个生长过程大概是这样的：Fact 先落一条“目标 443 端口开放，Web 服务可访问”；据此长出一条 Intent“枚举 Web 目录，确认是否存在后台入口”；执行完之后写回新的 Fact“发现 /admin 路径，但需要登录”；再长出下一轮 Intent——“测试默认口令”“分析登录接口”“寻找未授权接口”。任务状态就这样一步步落进图里，不再飘在对话记录里。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/C0tk9icZjs9TVu2j2fncl5NbhKBXJS1sJWSDry85jwZuIvf54ldWOJw0yYicf4ibapxstzFDiaw8MVhMrR379okaicNAYxeJxScM9DAI9Yh8SAWA/640?wx_fmt=png&from=appmsg)

![](https://mmecoa.qpic.cn/sz_mmecoa_png/C0tk9icZjs9ScpzuzX40zDgiatMrmWau1ghojnJDdMRYUiba06R34pqLMB7yxNM9LLmJW0RSAiblDRsI2U3HAtfQtWumRnUgJzk7Mypl2QKMDpM/640?wx_fmt=png&from=appmsg)

**Agent 不是在“聊天”，是在跑一个 OODA 循环**

![](https://mmecoa.qpic.cn/sz_mmecoa_png/C0tk9icZjs9SHe1WEkJBBF7biczeIlo742Kad7dC6zlSbIuJJ6voplIJ12PV2pvO0NaXOyaKrWRsRBIckXa6ppricjL8laYtdugk7FUlzb4j6Q/640?wx_fmt=png&from=appmsg)

Cairn 里的每个 Agent Worker，工作方式非常经典——就是军事和管理学里常提的 **OODA**循环：

![](https://mmecoa.qpic.cn/mmecoa_png/C0tk9icZjs9QzTtm2NLs2VkQlClkrKwQJTRNPMXB72bF83XlKVrEP68DmBISVbYcQoiavQgjFyGPdWpqTz3Tj35glRDU0ibTwhXSctAgqPBknk/640?wx_fmt=png&from=appmsg)

对应到具体任务，Cairn 把整个流程收敛成了三类：

* **Bootstrap**：项目刚开始时，先直接尝试解决整个问题；
* **Reason**：读一遍完整的图，判断“完成了吗？下一步该往哪走？”；
* **Explore**：认领一条 Intent，去执行，产出一个新的 Fact。

这套逻辑跑起来是什么样子？

Cairn 提供了一个项目图的可视化界面：项目以 Origin → Bootstrap → Goal 的节点链路呈现，可以随时暂停 / 恢复，也可以导出快照，甚至按时间顺序**回放**整个探索过程——每一个 Fact 都能追溯到它的原始来源。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/C0tk9icZjs9TV9v9SjcMNcOMBWiaFcTgDH1jyQn8hwtayic7p1ib2jbPfGBKF6b7smWicWy5ZamILB290dB0xFXcgBLOIeBT7YfsYJWmUSf4kIIs/640?wx_fmt=png&from=appmsg)

**蚂蚁不聊天，但照样能找到最短路径**

![](https://mmecoa.qpic.cn/sz_mmecoa_png/C0tk9icZjs9QbY7W0fZIpeXWvc0iakduMtEt9riadqgicDkJYDE0CaTaRIuoQtA97dDcA88c1yYvddgxnvnyVg4F7PEXXtvTB35nCcfib9dbBU10/640?wx_fmt=png&from=appmsg)

Cairn 的多 Agent 协作方式，藏着一个很有意思的类比：**蚁群觅食。**

蚂蚁之间从来不直接通信。它们只是在路径上留下信息素——更优的路径上，信息素浓度更高；次优或无效的路径，浓度就低。群体智能，是从这种个体规则里“涌现”出来的，没有谁在中央指挥。

这个现象有个专门的名字，叫 **Stigmergy（间接协调）**：个体之间不互相通信，只通过改变共享环境来协调。

Cairn 的 Agent 之间也是这样：不直接对话，只通过在黑板上写 Fact 来间接协调。更有价值的 Fact 会引出更多的 Intent，整体的搜索策略，就从每个 Agent 各自的“读图—决策”循环里自然涌现出来。

放到架构图上看会更清楚：Cairn Server 只负责保证黑板（Facts / Intents / Hints）的一致性，不做任何推理和决策；Dispatcher 是唯一的协议写入者，负责调度和容器管理；真正执行任务的 Agent（比如 Claude Code、Codex），只接收 prompt、返回结构化结果，不直接碰协议接口。用一句话概括就是：**Server 管事实，Dispatcher 管推进，Worker 管执行**，这个边界切得比很多 demo 项目干净。

这套架构还有一个设计，读起来会让人会心一笑：**项目可以随时停止或恢复，系统状态完整保留；Intent 认领带心跳超时和自动释放机制；完整因果链永久保留，包括所有走过的死胡同；人类可以随时写入一条 Hint，注入判断，却不干预 Agent 自己的推理过程。**

这其实和军事理论里的“任务式指挥”（Mission Command）是一回事：指挥官只下达意图，下级根据现场态势自主决策。

![](https://mmecoa.qpic.cn/mmecoa_png/C0tk9icZjs9RUgTf12qka95RjEFoEGVo89H9sxmmvibbGQzeXJV7Kkna7UWpWuYCC4c1KyIBibrQduibUIZwP7M0Imibdlo7icFPA8RNMoGc5iaQ3M/640?wx_fmt=png&from=appmsg)

**为什么 Cairn 的 Agent 没有“角色”**

![](https://mmecoa.qpic.cn/mmecoa_png/C0tk9icZjs9QGoKxOibksg9A2TGTXJgiadHiakQRibayUqrckesKzxfaqbQawtIDXxwgJHcv7mxZQoChtJahTdeKHkH3drkWgBtfc3PPI6YSqKGA/640?wx_fmt=png&from=appmsg)

这里有个反直觉的设计选择，值得多说两句。

大部分多 Agent 系统，第一件事就是给 Agent 分配角色——侦察 Agent、渗透 Agent、报告 Agent……听起来很合理，对吧？

但 Cairn 偏偏反着来：它的 Worker **没有角色，只有任务。**

为什么？因为给 Agent 定义角色，本质上是人类组织方式的直觉延伸——人的记忆有限、注意力有限、上下文窗口极小，只能靠分工、专注一小块，再通过协作把结果拼起来。这是认知约束下的必然产物。

但 LLM 不是人类。它拥有超大的上下文窗口，完全可以容纳一整张完整的图，根本不需要靠分工来规避认知过载。

而分工从来不是免费的。它必然带来信息孤岛，代价体现在三个地方：**上下文残缺、翻译和过滤过程中的损耗、以及边界在设计阶段就被提前划死。**

Cairn 的做法是让每一次执行都基于完整图的上下文。一个 Agent 读到完整的 Fact + Intent 之后，能同时看到已有的凭证、已经排除的方向、当前的目标——于是从“探测 HTTP 服务”到“发现登录页”再到“直接用已有凭据尝试登录”直至“拿到 shell”，这类跨阶段的推理会自然发生，机会不会因为分工边界而被错过。

**分工的边界，不应该由人在设计时划定，而应该由图在运行时自己生成**。

这个判断没有停在 Cairn 最初的版本里。作者后来在 **Cairn\_Y 的迭代复盘** 里进一步把系统的运转拆成 Decide 和 Execute 两类活动——不是两个固定角色的 Sub-Agent，而是同一个运行器被注入了不同的提示词和工具：Decide 只负责读写图、评估和调整 Step（也就是升级版的 Intent），每次都从干净的上下文重新起一轮，不携带记忆；Execute 负责真正改变“世界状态”的动作，执行完提交一条 Fact。两类活动共享的唯一记忆，就是那张图本身。这进一步印证了同一个判断：**角色不是必需品，图才是**。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/C0tk9icZjs9TxXWVw2uGPoSx7953EiaglMQiaC2gTQnxV0MSBIjaC2Gg3RmWfic7e1lMQBxaGFiaWKiauLD7UryBibZYDxT1dBejK8nStCWTHEFAmc/640?wx_fmt=png&from=appmsg)

**越简单的架构，越难设计**

![](https://mmecoa.qpic.cn/mmecoa_png/C0tk9icZjs9Sia86icIIcCjGRUwVova2VNDDUvrOgmvBDA1QpdibDOKBu5l23KpQ1r52pGHibT81ZvMiberQpoO3rX7dk8knYhXia4TQpnNW1VdzP0/640?wx_fmt=png&from=appmsg)

Cairn 的实现里，有一个数字组合特别有意思：

**0 个渗透工具 MCP，0 个安全领域 RAG，0 个预定义的渗透流程，0 种预定义的 Agent 角色。**

这不是偷懒，而是一种刻意的克制。背后的判断是：**简单架构比复杂架构更难设计。**

大多数系统遇到问题的第一反应是“在问题外面堆解法”：缺什么能力就写个 Skill，遇到新场景就加一个 Sub-Agent。这种做法直觉、门槛低，但每多一层，系统就脆弱一分——本质上是在解决表面问题。

Cairn 走的是另一条路：**在问题内部找抽象。**先追问渗透测试的本质是什么——是状态空间搜索。再追问状态空间搜索的最小表达是什么——是 Fact + Intent。必须先看穿问题的本质，才知道什么东西可以被去掉；而去掉一个东西所需要的理解深度，远比加一个东西要大得多。

举两个具体的例子：不需要专门写一个 SQL 注入的 Skill，因为 LLM 本身就懂 SQL 注入；也不需要专门配一个内网渗透 Agent，因为 Agent 一旦在图上读到“拿到了 shell”这个 Fact，自然就会主动去探测内网。

这套思路听起来简洁，但它不是一个只能停留在审美层面的选择。Cairn 以及后续迭代出的 Cairn\_Y，在**Cybench、TsecBench v1、XBOW Validation Benchmarks** 等公开评测榜单 上都拿到了第一，而且没有针对题库定向优化提示词，所有大模型调用记录也公开接受监督。这从另一个角度说明，把探索过程外化成一张图，本身就是一条值得认真对待的工程路线。

![](https://mmecoa.qpic.cn/mmecoa_png/C0tk9icZjs9TS6VefDyH70LETo443rBbYNGgeVSBsnZcQDXEPWGYTXgVN41D2Sn8EibrhibUmW9UicDtQeYBJA3CXKuyHniczOuWrIOVMlcCFUxY/640?wx_fmt=png&from=appmsg)

**这套思路怎么迁移到日常的安全工作里**

![](https://mmecoa.qpic.cn/mmecoa_png/C0tk9icZjs9TTRJqajUVKhm7icn4C9qOgYpmWsO9blDYF4RwZnbYe40VOicqiczUfAcDy4Mej5GRBcQ0vXelhmB1HT76Z90ecHudoHBMAHy4Kyc/640?wx_fmt=png&from=appmsg)

这一整套逻辑，拿去看安全团队每天在做的事情，会发现映射相当直接。

拿漏洞审核来说，难点从来不是“发现漏洞”本身，而是后面的判断：这条告警是不是重复的？资产还在不在线？研发是不是已经修复了？业务方是不是有豁免？

信息往往分散在漏洞平台、CMDB、工单、日志、代码仓库和聊天记录里。单纯塞一个“会总结的模型”进去解决不了这个问题——模型的依据可能不透明，推断和事实容易混在一起，任务失败了也不知道该怎么恢复。

如果借用 Cairn 的思路，可以把这套判断过程拆成三层：

* **Fact（已经确认的事实），**比如“资产 A 属于业务线 B，当前状态运行中”。这里有一条硬规则：**模型的推断不能直接冒充 Fact，**候选结论必须能回指到具体的资产、扫描记录、日志或人工确认。
* **Intent（声明的探索方向）**，比如“核验资产是否仍在运行”。它解决的不是“模型会不会思考”，而是过程本身的可见性——为什么要做这个动作、谁在做、有没有别人已经在做了。
* **Hint（策略和约束），**比如“核心支付链路禁止自动执行验证动作”。这类信息不属于客观事实，但会影响处置策略。

这三层分开之后，一个很实际的好处是：不会再把“模型的一段回答”误当成整个系统的可用状态。

不过这里还留了一个问题：Fact 是一条一条的原子事实，那么“这确实是一个漏洞”这种结论，应该放在哪一层？Cairn 后续的迭代版本 Cairn\_Y 对这个问题给出了一个挺有意思的答案，引入了**Finding**这个概念——**作者的原话** 是，渗透测试、代码审计和 CTF 本质上都是搜索过程，但 CTF 的产物和最终目标是同一个东西（拿到 flag），渗透测试和代码审计不一样，它们真正要的产物是搜索过程中发现的漏洞，而不是“完成所有功能点测试”这种笼统的最终目标。

这个区分放到漏洞审核里格外贴切：**Fact 是过程中的原子事实，Goal 是任务的终止条件，Finding 才是搜索过程真正要交付的东西**——也就是这次审核最终确认下来的那个漏洞本身，连同它的证据链、影响范围和处置建议。三者分开之后，黑板负责记录“怎么查的”，Finding 负责承载“查到了什么该被上报”，不会再混在一起。

Cairn 里另一个值得借用的设计，是**任务租约**机制——claim / heartbeat / release / conclude。放到安全工具里，能直接减少几个常见的麻烦：多个任务重复审核同一个漏洞、一个任务卡死之后没人接手、重试导致重复写工单、中断之后状态无法恢复。

还有一点容易被忽略——**事实应该尽量只增不改**。“资产已修复”不应该粗暴地覆盖“曾经受影响”这段历史，而应该形成一条新的、带时间和证据的事实。这样做的好处是：能解释清楚为什么曾经判了高危、后来又关闭了；出问题时也方便复盘到底是哪一步误判了。

失败路径同样值得设计，而不是简单丢弃。接口超时、权限不足、模型输出格式不对、人工推翻结论，这些都是生产环境里的常态。Cairn 的思路是：执行阶段出异常时，先总结已经拿到的有效事实，确认真的没有有效结论了，才释放任务——这样有效的中间结果不会因为一次失败就整体丢掉。这一层设计也回应了一个更大的问题：多个 Agent 如果靠互相聊天协作，很容易变成“谁都说了点，但没人对状态负责”；Cairn 的做法简单很多——Worker 不需要聊天，只需要领取 Intent，做完写回 Fac...