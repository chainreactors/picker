---
title: 大语言模型应用开发框架 —— Eino 正式开源！
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247513210&idx=1&sn=d73c42c5ee5a694a80854e7a8d02cbbf&chksm=e9d37f98dea4f68e253da00814ac6b5ef2a23b16f013db0cf0132cf59f459c9f2fa8c245b5ab&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2025-02-11
fetch_date: 2025-10-06T20:39:04.225162
---

# 大语言模型应用开发框架 —— Eino 正式开源！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOgmZwFx9nmOSibodEzk2QkVMsMWOuYPHByBdVUN6pXXZLYeOt1YcJ8mDS82iaG5M5NibiaEGN8VB8xSxw/0?wx_fmt=jpeg)

# 大语言模型应用开发框架 —— Eino 正式开源！

Eino 项目组

字节跳动技术团队

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/BvYvvlJIDbItvQwtrrib8HKL8wmkUvUibkhuwYGBM2rf1OKHmEiaZ6pg2RaRezJJVbPT1P1NwxBdEFkzeI9nnnLPw/640?wx_fmt=gif&from=appmsg)

作者｜Eino 项目组

经过字节跳动内部半年多的使用和迭代，基于 Golang 的大模型应用综合开发框架 —— Eino，已在 CloudWeGo 正式开源啦！

Eino 基于明确的“组件”定义，提供强大的流程“编排”，覆盖开发全流程，旨在帮助开发者以最快的速度实现最有深度的大模型应用。

你是否曾有这种感受：想要为自己的应用添加大模型的能力，但面对这个较新的领域，不知如何入手；想持续的站在研究的最前沿，应用最新的业界成果，但使用的应用开发框架却已经数月没有更新；想看懂项目里的用 Python 写的代码，想确定一个变量或者参数的类型，需要反复查看上下文确认；不确定模型生成的效果是否足够好，想用又不太敢用；在调试、追踪、评测等开发之外的必要环节，还需要额外探索学习其他配套的工具。如果是，欢迎了解和尝试 Eino，因为 Eino 作为旨在覆盖 devops 全流程的大模型应用开发框架，具有如下特点：

* 内核稳定，API 简单易懂，有明确的上手路径，平滑的学习曲线。
* 极致的扩展性，研发工作高度活跃，长期可持续。
* 基于强类型语言 Golang，代码能看懂，易维护，高可靠。
* 背靠字节跳动核心业务线的充分实践经验。
* 提供开箱即用的配套工具。

Eino 已成为字节跳动内部大模型应用的首选全代码开发框架，已有包括豆包、抖音、扣子等多条业务线、数百个服务接入使用。

项目地址：

https://github.com/cloudwego/eino

https://github.com/cloudwego/eino-ext

未来，我们将以 Eino 开源库为核心代码仓库，坚持**内外用一套代码**，与社区共建最优秀的大模型应用开发框架。

**0****1**

**快速认识 Eino**

Eino 是覆盖 devops 全流程的大模型应用开发框架，从最佳实践样例的 Eino Examples，到各环节的工具链，都是 Eino 的领域：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOgmZwFx9nmOSibodEzk2QkVMWHQ1TXQ4nI0VL9nnnELBfc82FOAIF2wzUOWyib0laWeALxZ32ibuLV3A/640?wx_fmt=png&from=appmsg)

Composition of Eino Framework from a devops perspective

那么 Eino 具体能做什么？首先，Eino 由一个个大模型领域的“组件”组成，比如最核心的是与大模型交互的 Chat Model：

```
model, _ := ark.NewChatModel(ctx, config) // 创建一个豆包大模型message, _ := model.Generate(ctx, []*Message{    SystemMessage("you are a helpful assistant."),    UserMessage("what does the future AI App look like?")}
```

像上面这样一个个的直接使用组件，当然没问题，Eino 提供了大量有用的组件实现供选择。但是，大模型应用有它们自身的特点和规律，比如：

* 核心是大模型，业务逻辑围绕“如何给大模型充分、有效的上下文”以及“如何让大模型的输出可靠的影响环境”，核心的组件类型、数据类型和交互模式是可以枚举的，整体可以由有向图来描述。
* 大模型输出的特点是流式输出，意味着模型的下游都需要有效的处理流式数据，包括流的实时处理、流的复制、多个流的合并、单个流的拼接等。
* 以有向图为基础，衍生出并发处理、扇入扇出、通用横切面、option 分配等一系列子问题。

Eino 的编排能力，是上述通用问题的充分解决方案。

以 ReAct Agent 为例：一个 ChatModel（大模型），“绑定”了 Tool（工具），接收输入的 Message，由 ChatModel 自主判断是否调用 Tool 或输出最终结果。Tool 执行结果会再次成为给到 ChatModel 的 Message，并作为下一轮自主判断的上下文。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOgmZwFx9nmOSibodEzk2QkVMygibVPdpkA6oibJlXX9pU6zmWKuGhOzxicBmOyjYoJauHz5qcsyWXibjEA/640?wx_fmt=png&from=appmsg)

上述基于 ChatModel 进行自主决策和选路的 ReAct Agent，便是基于 Eino 的 组件 和 Graph 编排 来实现， 代码清晰简洁，可与流程图清晰对应。

* 代码实现详见：「flow/agent/react 」的实现
* ReAct Agent 用户手册详见：「react\_agent\_manual」

「flow/agent/react」https://github.com/cloudwego/eino/blob/main/flow/agent/react/react.go

「react\_agent\_manual」https://www.cloudwego.io/zh/docs/eino/core\_modules/flow\_integration\_components/react\_agent\_manual/

在 Eino 中，这是几十行代码的图编排：

```
// 构建一个 ReAct Agent，编译为一个输入为 []*Message，输出为 *Message 的 Runnable
// 创建包含 state 的 Graph，用户存储请求维度的 Message 上下文graph = NewGraph[[]*Message, *Message](   WithGenLocalState(func(ctx context.Context) *state {      return &state{Messages: make([]*Message, 0, config.MaxStep+1)}   }))
// 将一个轮次中的上下文和响应，存储到 Graph 的临时状态中modelPreHandle = func(ctx context.Context, input []*Message, state *state) ([]*Message, error) {    state.Messages = append(state.Messages, input...)    return state.Messages, nil}
_ = graph.AddChatModelNode(nodeKeyModel, chatModel, WithStatePreHandler(modelPreHandle))
_ = graph.AddEdge(START, nodeKeyModel)
_ = graph.AddToolsNode(nodeKeyTools, toolsNode)
// chatModel 的输出可能是多个 Message 的流// 这个 StreamGraphBranch 根据流的首个包即可完成判断，降低延迟modelPostBranch = NewStreamGraphBranch(   func(_ context.Context, sr *schema.StreamReader[*Message]) (endNode string, err error) {      defer sr.Close()
      if msg, err := sr.Recv(); err != nil {         return "", err      } else if len(msg.ToolCalls) == 0 {         return END, nil      }
      return nodeKeyTools, nil   }, map[string]bool{nodeKeyTools: true, END: true})
_ =  graph.AddBranch(nodeKeyModel, modelPostBranch)
// toolsNode 执行结果反馈给 chatModel_ = graph.AddEdge(nodeKeyTools, nodeKeyModel)
// 编译 Graph：类型检查、callback 注入、自动流式转换、生成执行器agent, _ := graph.Compile(ctx, WithMaxRunSteps(config.MaxStep))
```

在上面这几十行代码的背后，Eino 自动做了一些事情：

* 类型检查，在 compile 时确保相邻的节点的类型对齐。
* 流式封装，编译出的 Runnable 既可以 Invoke 调用，也可以 Stream 调用，无论内部的 Tool 是否支持流。
* 并发管理，对 state 这个公共状态的读写是并发安全的。
* 横切面注入，如果某个组件（比如一个 tool）没有实现 callbacks 注入，则 Eino 自动注入。
* Option 分配，编译出的 Runnable 可以灵活接收并把 option 分配给指定的节点。

**02**

**Eino 的独特优势**

基于大语言模型的软件应用正处于快速发展阶段，新技术、新思路、新实践不断涌现，我们作为应用开发者，一方面需要高效、可靠的把业界共识的最佳实践应用起来，另一方面需要不断学习和提升认知，从而能够整体理解这个新领域的可能性。因此，一个优秀的大模型应用开发框架，既需要**封装领域内“不变”的通用核心要素**，又需要基于最新进展**敏捷的横向和纵向扩展**。

另一方面，目前较为主流的框架如 LangChain，LlamaIndex 等，都基于 Python，虽然能借助 Python 较为丰富的生态快速实现多样的功能，但是同时也继承了 Python 作为动态语言所带来的“弱类型检验”和“长期维护成本高”等问题。在大模型应用快速进入大规模线上运行阶段的当下，基于 Golang 这一强类型语言而实现的**高可靠性**和**高可维护性**，逐渐具有更大的价值。

基于大模型的应用开发是相对较新的领域，有时需要摸着石头过河，靠实践来检验认知。依托字节跳动高频应用豆包、抖音等的多样场景、快速迭代和海量反馈，Eino 在**实践驱动设计**方面有独特的优势。

最后，生产级的框架需要面对真实、复杂的业务场景，因此，除了直观易用的 API 设计之外，提供有针对性设计的开发**工具**可以有效的帮助开发者理解和应对复杂性、加速开发过程。

**内核稳定**

我们认为，存在一个常见的组件列表，共同构成了大模型应用的常见组成部分。每类组件作为一个 interface，有完善、稳定的定义：具体的输入输出类型，明确的运行时 option，以及明确的流处理范式。

在明确的组件定义基础之上，我们认为，大模型应用开发存在通用的基座性质的能力，包括但不限于：处理模型输出的流式编程能力；支持横切面功能以及透出组件内部状态的 Callback 能力；组件具体实现超出组件 interface 定义范围的 option 扩展能力。

在组件定义和通用基座能力的基础上，我们认为，大模型应用开发存在相对固定的数据流转和流程编排范式：以 ChatModel（大模型）为核心，通过 ChatTemplate 注入用户输入和系统 prompt，通过 Retriever、Document Loader & Transformer 等注入上下文，经过 ChatModel 生成，输出 Tool Call 并执行，或输出最终结果。基于此，Eino 提供了上述组件的不同编排范式：Chain，链式有向无环图；Graph，有向图或有向无环图；Workflow，有字段映射能力的有向无环图。

上述设计和功能共同构成了 Eino 的稳定内核：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOgmZwFx9nmOSibodEzk2QkVMCTwjkOkR0sv9NDyDc3TWCvCWBWibIf0hXHqzCvbAmNN6BnmIEFVH6XA/640?wx_fmt=png&from=appmsg)

**敏捷扩展**

每类组件都可以横向扩展出不同的实现，比如 ChatModel 组件可以有 OpenAI、Gemini、Claude 等不同的实现等。这些具体的实现，在实现组件 interface 从而可作为组件参与编排的基础上，可以实现和持续扩展自身的特殊功能。

当实际业务场景中，出现需要进入编排但是不对应任何组件定义的功能时，Eino 支持将自定义 function 声明为 Lambda 类型。Lambda 有用户声明的输入输出以及 option 类型，可支持全部的流处理范式，具备完整的 Callback 能力，在编排视角等价于官方组件。

在大模型应用开发领域，存在并且持续会涌现多个组件的特定编排范式，这些范式封装了验证有效的研究成果或实践经验，比如 ReAct Agent，Host Multi-Agent 等。这些开箱即用的封装，浓缩了大模型应用开发领域的最佳实践，会随着我们认知的提升持续纵向扩展。

在组件和图执行过程中，开发者可以在固定的时机嵌入自定义的回调逻辑，用于注入横切面功能。

综上所述，Eino 框架具备充分的可扩展性：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOgmZwFx9nmOSibodEzk2QkVMmnpqBib7oDz8RialtSW9IV0dQB7samZCia9gK8CibzzzrmN69y3Iib3j05A/640?wx_fmt=png&from=appmsg)

**高可靠易维护**

基于 Golang 写 Eino 代码时，开发者可以充分利用 Golang 的强类型特性，为所有的组件、Lambda、编排产物等声明具体类型。这像是为代码绘制了一幅精确的地图，开发者可以沿着清晰的路径进行维护和扩展，即使在项目规模不断扩大、功能持续迭代的情况下，依然能够保有较高的可维护性。

同时，Eino 编排能力也充分利用了强类型系统的编译时校验能力，尽可能将类型匹配问题暴露的时机提前到 graph 的编译时，而不是 graph 的运行时。尽早并明确的暴露类型匹配问题，有助于开发者迅速定位和修复，减少因类型错误在运行时引发的难以排查的故障和性能问题。

另一方面，Eino 遵循模块化设计，核心库以及各组件实现是单独的 go module，每个 go module 做到依赖最小化。同时，API 设计以“精简”、"直观"和“同构性”为原则，辅以由浅入深的全面文档，尽可能让学习曲线更平滑。最重要的是，Eino 采用清晰的分层设计，每层职责明确、功能内聚，在提升维护性的同时能更好的保证稳定性。

Eino 框架结构图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOgmZwFx9nmOSibodEzk2QkVM8FKiaicGPSl214kPGSWRQqg7YOyj4BFLrfTznbiaEicxaQrkXDc1JonJ8Q/640?wx_fmt=png&from=appmsg)

**实践驱动**

Eino 框架的设计开发过程，扎根于 “满足真实需求” 与 “实践驱动设计” 这两大基石之上。功能的演进过程与字节跳动各业务线的接入过程紧密结合，始终倾听开发者的声音，并通过实际使用效果来检验设计的合理性。比如我们收到来自抖音的“希望能够以字段为粒度在图中映射和传递数据”的需求，以此为基础设计了 Workflow；倾听来自豆包的使用痛点，增强作为模型输入输出类型的 Message 结构体。在未来的开源生态共建过程中，我们会继续坚持上述原则，满足更广大的用户和开发者的真实需求，并在更大的范围内认真实践和精进。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOgmZwFx9nmOSibodEzk2QkVMmqqxYZLxl3uzgbVvia4STKTjPMYuxCUscPhOc7A9K0bibSUdZ1qic7dtg/640?wx_fmt=png&from=appmsg)

**工具生态**

链路追踪、调试、可视化，是编排引擎的三个重要辅助工具。Eino 内置了 tracing callback，并与 Langfuse 平台做了集成。同时提供了 IDE 插件，可以在写代码的过程中随时可视化查看编排出的 graph，并进行调试运行，甚至可以通过 UI 拖拽的方式快速构建 graph 并导出为 Eino 代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5EcwYhllQOgmZwFx9nmOSibodEzk2QkVMpibypoKm4cJ1QSpLDJTuNLxVRvLniaz3OOsibh3TZuZW4ruGicoy9dOsLw/640?wx_fmt=png&from=appmsg)

**03**

**快速上手**

针对 Eino 的学习和使用，我们提供了完善的 Eino 用户手册，帮助大家快速理解 Eino 中的概念，掌握基于 Eino 开发设计 AI 应用的技能，赶快通过「Eino: 快速开始」尝试使用吧~

如有任何问题，可通过下方的飞书群或者「Eino Issues」和我们沟通、反馈~

「Eino: 快速开始」https://www.cloudwego.io/zh/docs/eino/quick\_start/

「Eino Issues」https://github.com/cloudwego/eino/issues

**相关链接**

项目地址：

https://github.com/cloudwego...