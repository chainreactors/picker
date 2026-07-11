---
title: 【揭秘】如何打造一支凌晨3点还在交付的AI军团
url: https://mp.weixin.qq.com/s/OV2OqbaDj0hIrBvX1pV_qQ
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:59:18.122080
---

# 【揭秘】如何打造一支凌晨3点还在交付的AI军团

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/KVER9adz905gVWR6icezvGibqD5PvyqJF8ZjjiaMQBxLIibAqClvmhjOArAPCDzKc490Rb8cHBJhRXRJevg4iaXsetfeKicibQnJViaGlBfefYsIVXQ/0?wx_fmt=jpeg)

# 【揭秘】如何打造一支凌晨3点还在交付的AI军团

腾讯程序员
腾讯程序员

腾讯技术工程

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/j3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj79H3xfgvsqK9TDxOBlcUa6W0EE5KBdxacd2Ql6QBmuhBJKIUS4PSZQ/640?wx_fmt=gif&from=appmsg)

作者：胡峻玮&姚广龙

> AI 已经让很多人成为”超级个体”，但一件完整工作并没有因此自动变快。AI 帮我写完了需求草稿、帮我定位了 Bug、帮我生成了一批用例、帮我整理了一份配置——AI 让每个人都成为了"超级个体"，却依然需要由“人”来作为主导推动。一件完整的工作仍要靠人一步步看、一步步转、一步步推：需求等人评审，Bug 等人接手，上下文在一次次转述里丢失。我们意识到，真正的瓶颈不在"每个人会不会用 AI"，而在“没有为 AI 的模式去设计一套新的工作方式”。这次基于 Multica，我们搭出了这支 AI 协作军团的雏形——这是我们对"组织级 Loop Engineering” 的一次思考实践。

![](https://mmbiz.qpic.cn/mmbiz_jpg/KVER9adz906vvytXqxCzDBNNQgDRt28EnnpDBK6YAPFyvTsVu3EwPBXa6vh02ykNu5kNMpL09icFeJsza4k0ibIWUCDQJ1ko8Z942cwVzAibsE/640?wx_fmt=other&from=appmsg)

凌晨三点，没有人在群里催进度，也没有人在电脑前等结果。

但第二天早上当你打开平台，已经能看到一些工作进度发生了变化：一条需求走完了评审和分发，进入实现和验收入口；一个测试提的 Bug 被接手处理，修完后回到测试侧继续验收；平台自己的一个能力改进项，也跑完了分析、修改和验证，等人确认；历史问题池里那些过去总是排不上期的小问题，也开始被定期捞出来处理。

这些事情当然是 Agent 在做。

但真正的变化不在于某个 Agent 半夜多跑了一次，而在于一件事进入系统后，不需要再等人逐步叫醒下一个角色。系统会继续找到下一步、找到合适的 Agent、带着上下文往下推，直到走到通知、验收或返工的位置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz9044fnExbFiadbNkic4TKBuUE9dAtfrHVyev8NsCOuEtibWvQZUMtTbTOZdvTJtx3ntzPPXdiaJaj8SLg7UwEKDCxy7bmcOgjh29sd0/640?wx_fmt=png&from=appmsg)

过去这一年，我们其实已经攒了不少 Agent。有的能评审需求，有的能分发任务，有的能改配置，有的能修 Bug，有的能写代码。

它们的单点能力都已经不弱——像是一群刚入职的优秀实习生：让他们做手上这一摊事，做得不错；但你不能指望他们自己知道这件事什么时候该开始、做完之后该交给谁、卡住了该找谁兜底。

更现实的是，这些"实习生"还分散在不同的角色手里。产品用自己的 AI，研发用自己的 AI，测试用自己的 AI，运营用自己的 AI。每个角色都变强了，但一件事从开始到完成，仍然要靠人一步步看、一步步转、一步步推。

所以这次我们真正想试的，不是再训练一个更强的"实习生"，而是看看能不能**教这群实习生一起把一件事做成**——一条需求进来，不再只是等人看到后才去调用评审 Agent；一个 Bug 被提交，不再只是等研发逐单接手；一个平台待办出现，也不一定要先等人排期、拆解、推动。只要这件事边界清楚、目标明确、结果可验收，就让它进入这套机制，由不同 Agent 围绕同一个目标协作推进，最后把结果交给人确认。

这件事如果说到底是什么，我们的判断是这样：

> **AI 转型的下半场，不是让每个人都用上 AI，而是教 AI 怎么真正学会“工作”。**

过去，AI 更多是在帮助每个人成为"超级个体"。

这一次，我们想再往前走一步：看看一组 Agent 被组织起来之后，能不能长出"超级组织"的雏形。

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz905VRegYzmCAruuaiak3YibTJiad3RsUSwtpOsAsjNhOic9MxRLWurymVYHrWnPfhewKSmZ4VhXfX2wSb8w3zk4KBy8nYzJYtHUfrpI/640?wx_fmt=png&from=appmsg)

---

### 一、AI 进了岗位，但还没有进入协作链路

每个角色都配上 AI 之后，组织效率却没有因此发生质变——卡点到底在哪里？

先回到那条最常见的工作流转链路：

```
产品理解需求
→ 评审判断合理性
→ 负责人分发任务
→ 研发实现
→ 测试验证
→ 负责人验收
→ 发布或关闭
```

AI 出现后，最自然的做法，是给链路上的每个角色都配上 AI。这当然有效，但改变的只是**每个节点的效率**，并没有改变整条链路的协作方式——工作仍然要等人看到、等人判断、等人分发、等人转述、等人验收。很多时候真正消耗时间的，不是某一步执行本身，而是中间的等待、交接、确认和返工。

具体来看，旧模式下有三处典型卡点。

**第一，工作推进仍然依赖人的在线状态。** 过去 Agent 会干活，但要等人叫它。需求来了，要有人看到；评审完了，要有人转述；该谁执行，要有人分发；做完以后，还要有人通知负责人验收。只要人不在，这条链路就容易停住。

这也是"人下班，Agent 也下班"的本质：不是 Agent 没有能力，而是旧模式里，Agent 的启动、衔接、推进和验收都依赖人。

**第二，旧角色边界限制了 AI 扩大的能力边界。** AI 已经扩大了每个人能做的事。一个研发可以借助 AI 更快理解需求；一个测试可以借助 AI 判断问题可能出在哪里；一个运营可以借助 AI 分析配置规则；一个产品也可以借助 AI 补充验收标准。

但如果组织协作仍然严格按照过去的角色边界推进，那么 AI 放大的个人能力又会被旧流程重新压回原来的格子里。

> **AI 扩大了个体能力，但旧流程仍然要求每个人只接自己那一段。**

**第三，很多关键上下文丢在角色交接里。** 旧流程里，很多信息并不稳定地存在于系统里，而是散落在角色之间的转述中。比如评审时真正担心的风险、分发时为什么判断给这个模块、执行时发现的边界条件、Agent 输出里哪些内容可信、验收不通过的真实原因，以及返工时应该重点改哪里。

这些信息在一次次交接中会丢失。但 Agent 要连续完成一件事，最需要的恰恰是这些上下文。如果上下文仍然靠人来读、来解释、来转述，那么 Agent 就很难真正接力——它们只是各自完成一小段任务，链路仍然要靠人粘起来。

回到那个"实习生"的比喻：我们给每个角色都配了能力不弱的实习生，但**没有人教过他们怎么和别人一起工作**。所以哪怕每个实习生都比过去更利索了，整条链路并不会因此自动变快。

> **AI 只提效了节点，没有提效整条协作链路。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KVER9adz9052DicJjSQngcK6iaHRPnOUkac4fPIU6ktj5BhxMwed3F4ZS3AG1KJkaQqtCfgiaC2RIuglcibx1fFZXF3ibowWELu2soSGSlxaPaAI/640?wx_fmt=png&from=appmsg)

---

### 二、所以我们想验证的，是另一件事

这次实践想验证的，不是"某个 Agent 能不能做某一步"，而是更进一步的问题：

> 一段边界清晰、可验证的组织工作，能不能不再按照人类角色接力的方式推进，而是由一组 Agent 在系统里围绕同一个目标协作完成？

### 我们考虑过的几条路

要让这件事发生，路径并不止一条。动手之前，我们在三个方向上权衡过：

**路径 A：造一个更强的"超级 Agent"。** 让一个端到端的 Agent 自己看懂需求、自己拆解、自己执行、自己验收。这条路看起来最酷，但问题也最直接：单一 Agent 的可控性、可观测性、责任边界都不好处理；一旦它中间错了，几乎没有干预点。对一件涉及多个角色、多个外部系统的真实工作来说，这一步迈得太大。

**路径 B：直接设计一套 AI 原生的协作流程。** 不参考人类现有的流程，从 AI 协作的特性出发，重新组织"目标 → 计划 → 执行 → 验证 → 验收"。这条路是我们真正认为更有想象空间的方向，但它有一个现实问题：没有人能拍脑袋设计出最优的 AI 原生流程。如果没有第一阶段的真实运行数据，所谓的"AI 原生"很容易变成另一种凭直觉的设计。

**路径 C：先把人类已经验证过的流程 Agent 化。** 选择一类边界清晰、已经被人类协作跑通过的工作，把其中每个角色背后的执行者换成 Agent，让工作流来组织它们接力。它不是终局，但它能最快跑起来，能最快暴露真实问题，也能为后面任何方向积累数据。

我们最后选了路径 C，作为第一阶段的策略：**先把人类流程 Agent 化**。

不是因为它最理想，而是因为它最务实——它**足够接近原有流程**，容易落地，容易对齐责任边界，也容易被业务验收；同时它又**真的把多个 Agent 串了起来**，会逼出协作系统该有的所有边界问题。

第一阶段的目标不是一上来就设计一个终局式的 AI 原生流程，而是先把一个更基础的问题回答清楚：

> 一条原本需要多人接力的链路，能不能被一组 Agent 接起来跑？

---

### 三、技术底座：把 Multica 改造成 AI 军团的指挥中枢

策略定了，接下来要选起点。我们没有从零搭一个新平台，而是选择了 [Multica](https://github.com/multica-ai/multica) 这个开源项目的能力作为技术底座。

Multica 不是最终答案，而是一个比较合适的起点。它已经具备 Agent、Issue、Runtime / Daemon、Agent Task、工作空间、基础任务分发和执行链路等能力，能比较自然地表达一个基础模式：

```
Issue → 分配给 Agent → Agent 执行 → 回写结果
```

这对单个 Agent 执行任务是够用的。 但当我们想承接一条真实工作链路时，它还不够。

真实工作不是"一个 Issue 交给一个 Agent"就结束。它可能要先评审，再分发，再执行，再通知，再验收；有时要并行处理；有时 Agent 会 blocked；有时执行完成后还要外部系统验收；有时验收不通过，要回退到中间节点重做。

所以第一阶段二次开发的核心，不是给 Multica 加几个页面，而是把它从一个偏 **Agent 任务管理** 的系统，扩展成一个能支撑 **多 Agent 协作工作流** 的底座。

Multica 项目链接：https://github.com/multica-ai/multica

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz906bztg5sgXUurB4icYzdSBzboGSDK2f1HVARmkRL1ibveftEicNNV0LAX786gDiblVMeoZP7ZXqkicCgLMDdYibq8WKiaILqEUKQCymS4/640?wx_fmt=png&from=appmsg)

要让一组 Agent 在系统里协作起来，不是加几个工作流页面就能完成的。它要先回答三个最基础的问题：

```
平台能不能调得动 Agent？
平台能不能表达一条工作流？
平台能不能和外部系统完成交接？
```

这三件事构成了 Agent 协作系统的基础骨架。下面分别展开。

---

#### 3.1 第一根骨架：把分散 Agent 变成平台可调度的能力池

第一阶段之前，我们已经有不少 Agent，但它们是分散的。有的在个人电脑上，有的在云主机上，有的在外部平台上，有的是某个业务方向的专项 Agent。

这些 Agent 各自有能力，但平台并不知道：有哪些 Agent、它们能做什么、现在能不能用、该怎么调用、这一步该派谁。

如果平台不知道这些，Agent 再多也只是散点能力。

所以第一步不是先画工作流，而是让 Agent 进入平台视野，变成平台可调度的能力池。

第一阶段，我们把平台内 Agent、本地 Agent、云主机 Agent、KNot、CodeBuddy 等不同来源的 Agent 接入到统一管理视图中。调度策略覆盖了"指定 Agent / 上一步指定 / 能力匹配 / 兜底解析"四种方式，从静态到动态都能落。

这一步不是单纯做一个 Agent 列表，而是把分散在个人和外部平台里的 AI 能力，变成平台可调度的执行能力。

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz907wGuehnKIc1pgwSgvhAiaJgTRdtGia1IoMkXqYWbGzic5qjCMc3GcwNre85kCxqnt2QMVy5XiaiahU8EbHGHAYXfl01MRa6OEvYKKA/640?wx_fmt=png&from=appmsg)

---

#### 3.2 第二根骨架：把人的流程经验变成可运行工作流

光有 Agent 还不够。

如果仍然靠人决定什么时候评审、评审完找谁、分发完谁执行、执行完谁验收、失败后回哪里，那协作模式没有变化。

所以第二根骨架是 **工作可编排**。

我们补出了工作流运行时能力：Workflow Template、Node、Edge、Step Instance、Issue / Agent Task、节点状态流转、End Node、Acceptance 等。它们负责把过去人脑里的流程经验，变成系统可以运行、追踪和恢复的流程结构。

比如一类复杂流程的工作，可以表达为：

```
评审 → 技术方案 → 配置变更 → 模板变更 → 代码变更 → 通知完成
```

更简单的标准流程则只需要其中几个节点的子集。它们复用的是同一套模板、节点、边和 Step Instance 机制。节点被激活后，系统创建对应 Issue / Agent Task，并分配给合适 Agent 执行；Agent 提交结果后，工作流根据状态推进下一步。

这一步让"人知道下一步怎么走"，变成"系统知道下一步怎么走"。

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz9061SHCqlf3A6jBQNzpGTj58ohTl65qzoMW61J6gic5thAAseODLNusOjjvCzbg1WsOMe7xnm1RmaAVeHsSKKYonxGVSic6eydic4Y/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz904icSnBeibVpblm7wqqknkrbAKIgLNp6TD351icNmfbNmy5l8AxdHoYViaibagoBs81db6zsA3xxbltIzz1v4eaQYuZtMF0ToxlbObc/640?wx_fmt=png&from=appmsg)

#### 3.3 第三根骨架：让真实工作进来，完成状态能出去

平台不能替代所有外部系统。

需求、缺陷、验收、发布系统已经存在。我们要做的不是把所有工作搬进一个新平台，而是让外部系统在合适的状态把工作交给平台，平台组织 Agent 执行，执行完成后再把结果或状态交回去。

所以第三根骨架是 **外部可交接**。它要回答四件事：外部工作如何进入平台、平台完成后如何通知负责人、外部验收结果如何回到平台、外部系统如何理解当前进度。

以需求系统为例，当需求进入可执行状态后，外部系统触发 Hook，把需求标题、描述、负责人、来源链接和 `template_key` 推给平台。平台创建工作对象并启动对应工作流。工作流完成后，负责人收到通知，并在平台或外部系统完成验收；验收通过则关闭，驳回则回到指定节点返工。

这一步让平台成为 Agent 执行层，而不是另一个孤立工单系统。

**走到这里，Multica 不再只是分发任务的看板，而是一支 AI 军团可以在其上排兵、接力、验收和返工的指挥中枢。**

---

### 四、从能跑到可用：真实运行里补出的复杂能力

有了 Agent 可调度、工作可编排、外部可交接这三根骨架，系统就具备了跑起来的基础。

但跑起来只是第一步。真实场景很快会暴露出 AI 工作流和传统工作流不一样的地方：Agent 输出不稳定，复杂工作不一定是线性的，Agent 完成不等于业务完成，流程可能静默卡住，验收不通过不能靠人重新解释一遍，跑完一批后还要知道哪里应该优化。

> 正向链路跑通只证明"能跑"，失败路径能处理才证明"可用"。

下面六类能力不是为了让系统“看起来”更完整，而是真实运行中被一个个找到的必要能力。

---

#### 4.1 Agent 输出不稳定：准出字段和 Verdict

传统程序节点的输入输出通常比较稳定，但 Agent 节点不是这样。

它可能输出格式不稳定，漏掉下游需要的信息；也可能自然语言里说了很多，但系统无法稳定消费；它可能失败了但表达得很模糊，也可能 blocked 了但没有形成明确状态。

所以 AI 工作流不能假设每个节点天然可靠。我们用一组结构化字段约束 Agent 输出：**业务产物**承载真正要交付的内容，**流程裁定**（pass fail blocked）告诉系统下一步该往哪里走，**根因解释**和**置信度**则把"为什么这么判断"留在链路里，让下游不必重新猜测。

![](https://mmbiz.qpic.cn/mmbiz_png/KVER9adz907WkraxqRS0MJ6rYibx87X4zBONWDSAtv1fWEazVTSZrgQTcuC34844Lnqibwtp1JwKWicEkAmgyObsTJphRQRHOQP5neWGr5jTko/640?wx_fmt=png&from=appmsg)

在这套字段之上，每一次 Agent 执行都会落成一次 Submission，并由系统派生出统一的 Verdict 状态。下游节点不再去解析自然语言，...