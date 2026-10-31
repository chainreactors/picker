---
title: QECon北京2026｜小红书创新产品的 AI Native 质量工程实践
url: https://mp.weixin.qq.com/s/XqwFMK6zLC4ihzmLJFBxYw
source: Doonsec's feed
date: 2026-10-30
fetch_date: 2026-10-31T07:45:42.403513
---

# QECon北京2026｜小红书创新产品的 AI Native 质量工程实践

# QECon北京2026｜小红书创新产品的 AI Native 质量工程实践

原创

REDtech
REDtech

小红书技术REDtech

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/P9Hs04VFGRkQxqGfQroDjibJYKKnkYyapOjZhABZm6HgOrFicRQYicdtbB1j2FP6kWPCald8sniakyicgicOZlSvzxD8624Xj8G9icv1anKlcSq3Pc/640?wx_fmt=jpeg&from=appmsg)

**导读**

过去，AI 在测试中主要承担辅助角色，需求验证仍由测试人员主导。我们希望，Agent 能理解需求，自己决定该测什么、怎么测，根据现场变化推进测试，并判断实际测试结果是否符合业务预期。

围绕这一目标，小红书 Lab1327 打造了 QE Agent，目前已覆盖多个 App 和 PC 端产品，每月完成150余次完整测试。本文结合这些实践，分享从 AI 辅助测试走向 Agent 自主验证的探索，重点介绍上下文工程与多端质量知识图谱如何支撑测试决策，以及 Agent Loop、动态执行 DAG 和联合断言如何在测试执行与结果判断中协同工作。

**01**

**QE Agent：从 AI 辅助测试到自主验证**

过去，我们用 AI 生成用例，尝试用自然语言执行 E2E，也有接口、日志和数据准备工具。但 AI 本身并不了解我们的业务，也不知道一项需求具体该怎么测。测试人员仍要补充业务背景，写清入口、步骤和检查点，反复调试，把工具串起来推进整轮测试。单个环节快了一些，人却没有轻松多少。**为此，我们打造了 QE Agent，希望让 Agent 自主组织和推进完整的需求测试。**测试人员明确需求和业务预期后，Agent 据此设计用例、调用测试工具，根据现场执行反馈推进测试，并逐项判断实际结果是否符合预期。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRn7M9kRZjDRYU1dibG0YWiaWwms4RKWSEoIlQxeCGEw04Qjkeyj5yh7h2MZzZSNXRKYdE2bhROmH9xwicMYoBn0DzsHywDbheuLkg/640?wx_fmt=png&from=appmsg)

*图 1：QE Agent 整体架构。Agent 组织需求理解、测试设计、执行与结果判断，上下文工程、知识图谱和执行底座配合完成需求验证。*

**02**

**业务理解：测试上下文与跨端关系**

**2.1 以用例为单位的上下文工程**

Agent 要测试，首先需要明确当前测什么，预期是什么，以及已经完成了哪些操作。随着测试持续推进，用例、截图和日志不断累积，每步读取全部历史会增加耗时和 Token 消耗，也容易让 Agent 在执行中遗漏用例的前置条件、操作步骤和预期细节。

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRkuibAD8FFibfP6ich3TFr2utAr6O89HygA4S2ru7qpI7jgBXxicwySGjrmjAZbnYxRzxrHrPE9SSmialB9WhXlwbJa4U7G9DTgcugk/640?wx_fmt=png&from=appmsg)

*图 2：不断累积的测试记录。每一步都带上全部历史，会增加 Token 消耗，也容易让 Agent 忽略当前用例的前置条件和预期。*

上下文管理的常见方法包括上下文压缩、外置记忆、按需检索和上下文隔离。为减少重复读取，同时保留可回查的原始记录，我们结合后三种方法：需求、用例和执行记录完整保存在对话之外，Agent 按当前用例读取前置、步骤、预期和进度，截图与日志按需补读。

按用例读取后，Agent 还需要跟进执行中的变化。每次工具调用后，Agent 将新增操作、结果和进度补入当前上下文，未变化的信息继续复用，用于判断下一步。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRkdt2g9Vhb3IvJdWA070v6en9xmLft8kZTjFD6o0A92uyXRibHbFyOUGrsZpDJFhkxCf5kKBmpel0mkLknrwVibMicYIvCRZJvL28/640?wx_fmt=png&from=appmsg)

*图 3：按用例组织上下文。需求与执行记录完整保存；Agent 读取当前用例需要的内容，测试过程中再补上新的操作和结果。*

我们围绕“AI 页交互优化二期”需求做了一次上下文管理对比实验，覆盖 22 份双端设计、94 条预期和 94 个原始操作。与关闭上下文管理的基线相比，耗时下降 59.6%，累计总 Token 下降 65.1%，工具返回文本由 9.81 MB 降至 1.80 MB。

这样，上下文减少了重复内容，Agent 更容易看清当前要测什么，要测到哪一步，以及还缺哪些证据。

**2.2 为什么选择多端质量知识图谱**

除了用例和执行记录，Agent 还需要掌握业务关系，包括页面入口、数据前置和跨端调用。例如，QE Agent 在验证“采集图片审核通过才能分享”时，曾将“采集”理解为“收藏”，进入错误场景。找到入口后，Agent 只追到 RN 分享调用，没有查清后续的原生桥接和审核接口。把实际的分享链路展开，可以看到：Agent 需要先从个人页进入采集列表，并确保列表中已有采集数据。发起分享后打开 RN 分享页，分享页再通过 iOS 原生桥接请求后端审核接口。

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRkRKxTN3cjIoY0icNiaZiaDG5aicPeArcBsaKS5yY2cGGDaUJQmmicJL3xVzy9hUy87BRu8YGtTVlxDBCjic8HADNkJTphy7GkJfXYpA/640?wx_fmt=png&from=appmsg)

*图 4：采集图片的分享过程。Agent 需要找到采集入口、确认已有采集数据，再查清 RN 页面如何经 iOS 原生桥接调用审核接口。*

最直接的做法，就是把业务知识整理成文档，保存在代码仓库或文档库中，再通过文件或语义检索让 Agent 找到相关内容。但关系分散在多份材料中时，Agent 仍要从检索结果中提取、拼接。因此，我们采用多端质量知识图谱，显式保存已确认的入口、数据前置和跨端调用关系，供 Agent 在后续测试中沿关系查询页面、路由与接口，并追溯源码和版本。

**2.3 图谱构建与关系检索**

构建时，我们先提取各端、各语言的代码结构，统一表示页面、路由、接口及跳转、调用关系；以规范化路由连接原生入口与 RN、H5 页面，以 HTTP 方法和路径连接客户端与后端。在实际测试中，Agent 再用截图、UI 树、操作记录及接口日志核对实际行为，分开记录源码确认、真机观察和断言验证状态。每条关系保留来源、版本和证据，随代码变化核实更新。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRnMA8CA0Viceux2GhT2oDVb4hpSaroWV4IdicF2HdGibQEuMd0W952czgh83mKQ4UwbDqyajzE86X0TbTib6hVMycVN6zJX09OcOh0/640?wx_fmt=png&from=appmsg)

*图 5：图谱关系的来源。页面、路由与接口先从源码中提取，再用真机操作和接口日志核对，每条关系都能查到来源与版本。*

以“向已有内容中添加记录”为例，Agent 先用业务描述匹配知识库中的页面名称、入口路径和操作记录，找到相关场景。如果已有具体路由或接口标识，就直接定位关联场景；当前已选场景也会一并纳入。几路结果按场景合并去重，明确标识和已选场景优先，再按匹配程度排序。

接着，Agent 将匹配结果作为查询起点，沿跳转、依赖和调用关系做广度优先搜索（BFS），把关联页面、数据状态和接口串成路径，同时限制深度与路径数量。Agent 拿到路径及其来源、版本后，再核对当前平台与用例，确认从哪里进入、需要哪些数据前置，以及操作后应回查哪些接口。

在 200 题离线自评中，页面定位命中率为 95%，关系召回率和精确率（微平均）均为 97.02%。

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRkaCu0VFmLZLMic7EznkrgUQLwKicl3mJl1HChGFK73Q39qFbL3gJ5lb21w08unygDwco71086UfxNgcA7nGibKMEUXkhYvVwgbicw/640?wx_fmt=png&from=appmsg)

*图 6：添加记录会经过哪些页面和接口。Agent 沿图谱查找相关路径；右侧是 200 题离线自评的整体结果。*

**03**

**验证设计：从业务预期到测试结论**

**3.1 根据业务预期选择验证能力**

查清业务关系后，Agent 还要根据预期确定验证范围，再选择相应能力。

QE Agent 曾在一次消息中心测试中，用 Mock 数据验证消息展示和蓝点清除，测试结果都正常。但测试人员随后通过真实业务触发消息，发现 iOS 收不到消息。我们排查后发现，后端异步链路漏传了实验所需的版本信息。这次 QE Agent 只验证了客户端展示，漏测了真实消息送达链路。

这次漏测说明，Agent 在调用工具前，需要先确定验证哪些业务环节、每个环节需要什么证据。为此，我们采用先规划、再执行（Plan-and-Execute）的方式组织测试：Agent 先明确用例的前置条件、步骤、预期和平台，再复查需求覆盖与取证安排，补齐缺口后从业务预期倒推所需能力。

例如，需要检查页面交互和展示，Agent 就选择多端执行；需要核对服务端数据，就选择接口回查；需要验证异步送达或排查异常，就查询日志。同一条用例需要多类证据时，组合相应能力；前置数据不足，则先准备数据。

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRncgSCpDSYabbPmlwTYrphnGoTEhRI8p9CB1XcIF6IS00voPDyttOT4SzjyPnoibpWrEUNg8P82M94xpDFb3BuIYdzK6vbnn7kg/640?wx_fmt=png&from=appmsg)

*图 7：根据业务预期选择测试方法。Agent 检查用例能否覆盖需求，确定每项预期所需的操作和证据，再用逻辑 DAG 表达任务依赖。*

**3.2 逻辑 DAG 与动态执行 DAG**

选定能力后，Agent 还要明确操作顺序与依赖。例如，它完成数据准备后才能操作页面，操作产生的对象 ID 又是后续回查的输入。我们用逻辑 DAG（有向无环图）表达 Agent 的验证计划：节点表示准备、操作、取证等任务，边表示依赖。

执行中可能出现新的证据缺口，原计划也需要随实际结果调整。为跟踪计划在执行中的变化，我们用动态执行 DAG 记录任务依赖和执行状态。它根据保存的计划、实际调用和工作状态生成并更新，保留已完成结果。Agent 据此跟进进度，证据不足时追加取证并调整后续依赖，从当前进度继续。

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRnho3bfFYbXrggWOibwD477o6aHq13iaOmAcqRbz1byRK5WlzOB0FNcDhfvxHuCGhYibDkGRxWGCWQBnYruf5XUxjlhVaOaticpVIU/640?wx_fmt=png&from=appmsg)

*图 8：测试计划随执行变化。Agent 保留已经完成的工作，遇到新的取证需要时追加任务；动态执行 DAG 记录这些变化和实际进度。*

**3.3 联合断言与结果判断**

执行任务完成后，Agent 还要判断实际结果是否符合业务预期。有些预期需要同时核对页面表现、对象关系和服务端数据，因此 Agent 在规划取证（Planning）时就要明确证据来源和获取方式。以“复制内容 A 得到副本 B，再给 B 改名”为例，Agent 需要确认 A、B 的 ID 不同、B 的修改保留、A 的原数据不变。为此，Agent 在操作前留存 A 的初始数据，保存新名称后退出并重新进入 B 页面截图，再通过接口回查 A/B 的 ID 与数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRm9WCYPsX3DABXLFzCrAVFq3QwYOy6DpWwzJmPNSB82B8Gs0z2XuIh7Ow8lL5iaUrEqFdB6ovXeDs0QQZGkTKa1fJDeg8Q38MwM/640?wx_fmt=png&from=appmsg)

*图 9**：复制内容后的检查。**Agent 核对原内容与副本的 ID、改名后的页面和前后数据，检查副本是否独立、修改是否保留、原内容是否不变。*

取得证据后，Agent 进行联合断言，核对用例、账号和操作归属，逐项比较预期与实际结果。证据充分且符合预期则通过，明确不符则失败；不足或矛盾则记为待补证，再重新规划取证（Replanning）。

若缺少操作后 A 的回查结果，Agent 会选择接口能力，按 ID 补查 A 并与初始数据比较，再结合 B 的已有证据重新判断。新增补查任务保存后，动态执行 DAG 随记录更新，原业务预期不变。报告保留判断理由和所用证据。

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRkCzM2TDk2cuibhGC2LVcAug2VQU2qD4oMJEPPYGg2iclmqxiczYuv2UqZredib7ZQn9AdmCKYxuQWKiaVIYz1zdicGJ4sugswrKgwGQ/640?wx_fmt=png&from=appmsg)

*图 10：联合断言的判断过程。Agent 把实际证据与业务预期逐项核对；证据不够或相互矛盾时，补查后再作判断。*

**04**

**持续执行：现场决策与任务恢复**

**4.1 测试数据准备与清理**

验证计划明确后，Agent 需要先满足用例的前置条件，才能执行相应操作。例如，要验证分组内的记录操作，分组中就需要先有指定记录。

因此，QE Agent 先核实用例的数据前置，查询已有数据，满足则复用；有缺口时，规划如何补足数据（Planning）。Agent 对照目标状态与能力目录，组合已有 UI/API 操作，确定参数与顺序，再调用工具执行并独立回查，未满足则调整规划。确需新增能力时，Agent 依据代码或 API 实现，经测试、清理验证和注册后使用。Agent 保留对象 ID 与回执，测试后据此清理并确认。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRmVgrXibaM51eZSPPEjXodqYy2mibp0lEgsib9ibQo9ASjfC86aevYWULTVZYSWDfWiafCPEzLHQANrxY7ibNXaTUcWkJfXS6BicfGBKM/640?wx_fmt=png&from=appmsg)

*图 11：为用例准备数据。Agent 检查现有数据能否满足条件，有缺口时补齐并独立核对，测试结束后再清理本次创建的数据。*

**4.2 Agent Loop 与现场执行**

前置条件满足后，Agent 要将用例步骤转成设备可执行的动作。我们先解决动作落地（Action Grounding）问题：Agent 结合页面知识、当前截图和必要的 UI 树，通过多模态理解定位目标、确定动作和参数，再交给执行器。点击、输入、滑动等操作由设备自动化工具完成：iOS 使用 WebDriverAgent（WDA）；Android 优先使用 uiautomator2，必要时通过 ADB 执行基础操作。

动作发出后，Agent 还要通过页面反馈确认操作是否生效。例如，关闭侧栏时，Agent 先尝试系统返回。工具调用没有报错，但操作后的截图显示侧栏仍然打开，说明关闭目标尚未达成。Agent 据此调整动作，改为点击灰色遮罩，随后确认侧栏关闭。

![](https://mmbiz.qpic.cn/mmbiz_png/P9Hs04VFGRlliaoqDWjQWTaflGGO2ErdB9SNkgkTk01I8jIEDKOXTJ1NibHPxOg9Ejl9TvHib6BTpDXkP6Bv1ib2NbPwMSx5iaz59YH35eiaxBia64/640?wx_fmt=png&from=appmsg)

*图 12：系统返回后，侧栏仍然打开。工具没有报错，页面却没有达到预期，Agent 需要根据截图继续处理。*

为处理这类现场变化，我们采用 ReAct 式 Agent Loop，让 Agent 在“观察—判断—执行—再观察”中持续推进：目标达成后进入下一步，操作未奏效时调整动作，发现疑似业务异常则保留证据、核对预期；无法继续时，由 Harness 保存阻塞与恢复状态。动态执行 DAG 跟踪任务依赖与进度，Agent Loop 处理每步操作的现场反馈。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P9Hs04VFGRnjiaVMlicxJym25syNqYxYFbndD5huY57LHdqGiatWa0S0WGwicgzrISQO5ke9q5CrcwFDBGnfZqR77FHnKahV3UxzOSp8x5bjGdc/640?wx_fmt=png&from=appmsg)

*图 13：Agent Loop 如何推进测试。Agent 根据当前页面确定动作，操作后确认实际变化，再决定继续执行、调整操作或核查异常。*

**4.3 Quality Harness 的进度管理与中断恢复**

Agent 在处理现场变化的同时，还要持续跟进整项需求的未测项。我们曾遇到 Agent 明知还有未测项，却释放设备并结束执行。

为此，我们明确了 Agent 与 Quality Harness 的分工：Agent 专注于测试决策，包括测什么、如何验证、下一步做什么，以及结果是否符合预期；Harness 将用例、计划、操作与证据关联起来，按场景和平台跟踪完成、失败、阻塞和未执行状态，并管理账号、设备的申请、占用、释放与异常清理。

有了这些记录，Agent 就能核对剩余任务和缺少的证据，继续推进可执行项。这些记录也用于中断恢复：Agent 重新读取原需求、计划、已确认结果和未完成项，核验设备、账号等实时状态后，从原进度继续。整轮结束时，Agent 再汇总结论、证据、阻塞与未执行项，交付报告。

![](https://mmbiz.qp...