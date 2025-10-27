---
title: Go语言开发AI智能体有多丝滑？字节重磅开源Eino框架，内含保姆级教程
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247513432&idx=1&sn=4b7c3096878e5fee05140f99b6256996&chksm=e9d37ebadea4f7ac599a7716399c57730b258d12e1d24550294bbe28d5f9a2a276e54c9f6028&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2025-02-20
fetch_date: 2025-10-06T20:36:16.572352
---

# Go语言开发AI智能体有多丝滑？字节重磅开源Eino框架，内含保姆级教程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOhwZxbA1VD5ibrUibkULbOdFAp4pGg30vpu90eMrXQXicoOFaV0PLtkVdOpiamicd3ib3WgakddlPtGxibDA/0?wx_fmt=jpeg)

# Go语言开发AI智能体有多丝滑？字节重磅开源Eino框架，内含保姆级教程

Eino项目组

字节跳动技术团队

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/BvYvvlJIDbItvQwtrrib8HKL8wmkUvUibkhuwYGBM2rf1OKHmEiaZ6pg2RaRezJJVbPT1P1NwxBdEFkzeI9nnnLPw/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

开发基于大模型的软件应用，就像指挥一支足球队：**组件**是能力各异的队员，**编排**是灵活多变的战术，**数据**是流转的足球。

Eino 是字节跳动开源的大模型应用开发框架，拥有稳定的内核，灵活的扩展性，完善的工具生态，可靠且易维护，背靠豆包、抖音等应用的丰富实践经验。初次使用 Eino，就像接手一支实力雄厚的足球队，即使教练是初出茅庐的潜力新人，也可以踢出高质量、有内容的比赛。

下面就让我们一起踏上新手上路之旅！

**认识队员**

Eino 应用的基本构成元素是功能各异的组件，就像足球队由不同位置角色的队员组成：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gWicBnh8bApkqXficjcia1XN8qBmpEsYTHiaByL45uu9dP1Jr9eONoicYwKfLgtqAsFwY1icgvyOnkES9xGw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

这些组件抽象代表了固定的输入输出类型、Option 类型和方法签名：

```
type ChatModel interface {    Generate(ctx context.Context, input []*schema.Message, opts ...Option) (*schema.Message, error)    Stream(ctx context.Context, input []*schema.Message, opts ...Option) (       *schema.StreamReader[*schema.Message], error)    BindTools(tools []*schema.ToolInfo) error}
```

真正的运行，需要的是具体的组件**实现**：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gWicBnh8bApkqXficjcia1XN8qB9k8kdN9Dv2oSGUtMlhqNA0q1B4eFmTk8Slk8oTBVGMDexOypmFnOibQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

Eino 的开发过程中，首先要做的是决定 “我需要使用哪个组件抽象”，再决定 “我需要使用哪个具体组件实现”。就像足球队先决定 “我要上 1 个前锋”，再挑选 “谁来担任这个前锋”。

组件可以像使用任何的 Go interface 一样单独使用。但要想发挥 Eino 这支球队真正的威力，需要多个组件协同编排，成为一个相互联结的整体。

**制定战术**

在 Eino 编排场景中，每个组件成为了 “节点”（Node），节点之间 1 对 1 的流转关系成为了 “边”（Edge），N 选 1 的流转关系成为了 “分支”（Branch）。基于 Eino 开发的应用，经过对各种组件的灵活编排，就像一支足球队可以采用各种阵型，能够支持无限丰富的业务场景。

足球队的战术千变万化，但却有迹可循，有的注重控球，有的简单直接。对 Eino 而言，针对不同的业务形态，也有更合适的编排方式：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gWicBnh8bApkqXficjcia1XN8qBQrIZpQ69ibm10PPZHCjChaPGmbo6btFOqqv8ktZxQHHqAIP4micGz6rg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

Chain，如简单的 ChatTemplate + ChatModel 的 Chain：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gW9F4uDZpE8I63LTGjPPssnKKziag2vzuS06D4Tq2hpqTQcP3De9ZsNWiaX7xKZbiaKvFCiaWEpibws5ZEg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

```
chain, _ := NewChain[map[string]any, *Message]().           AppendChatTemplate(prompt).           AppendChatModel(model).           Compile(ctx)chain.Invoke(ctx, map[string]any{"query": "what's your name?"})
```

Graph，如 ReAct Agent：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gW80MOH7pK8rYBH5FTLFlE2aj4R8yIEztQweBeOTj6SIQUQPaNhDCJWxltIwndQJoOAOiaxzmd9yzlw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

```
graph := NewGraph[map[string]any, *schema.Message]()
_ = graph.AddChatTemplateNode("node_template", chatTpl)_ = graph.AddChatModelNode("node_model", chatModel)_ = graph.AddToolsNode("node_tools", toolsNode)_ = graph.AddLambdaNode("node_converter", takeOne)
_ = graph.AddEdge(START, "node_template")_ = graph.AddEdge("node_template", "node_model")_ = graph.AddBranch("node_model", branch)_ = graph.AddEdge("node_tools", "node_converter")_ = graph.AddEdge("node_converter", END)
compiledGraph, err := graph.Compile(ctx)if err != nil {    return err}out, err := r.Invoke(ctx, map[string]any{"query":"Beijing's weather this weekend"})
```

**了解工具**

现在想象下你接手的足球队用了一些黑科技，比如：在每个队员接球和出球的瞬间，身上的球衣可以自动的记录接球和出球的速度、角度并传递给场边的服务器，这样比赛结束后，就可以统计出每个队员触球的情况和处理球的时间。

在 Eino 中，每个组件运行的开始和结束，也可以通过 Callbacks 机制拿到输入输出及一些额外信息，处理横切面需求。比如一个简单的打日志能力：

```
handler := NewHandlerBuilder().    OnStartFn(       func (ctx context.Context, info *RunInfo, input CallbackInput) context.Context {           log.Printf("onStart, runInfo: % v, input: % v", info, input)           return ctx    }).    OnEndFn(        func (ctx context.Context, info *RunInfo, output CallbackOutput) context.Context {           log.Printf("onEnd, runInfo: % v, out: % v", info, output)           return ctx    }).    Build()
// 注入到 graph 运行中compiledGraph.Invoke(ctx, input, WithCallbacks(handler))
```

再想象一下，这个足球队的黑科技不止一种，还可以让教练在比赛前制作 “锦囊” 并藏在球衣里，当队员接球时，这个锦囊就会播放教练事先录制好的妙计，比如 “别犹豫，直接射门！”。

听上去很有趣，但有一个难点：有的锦囊是给全队所有队员的，有的锦囊是只给一类队员（比如所有前锋）的，而有的锦囊甚至是只给单个队员的。如何有效的做到锦囊妙计的分发？

在 Eino 中，类似的问题是 graph 运行过程中 call option 的分发：

```
// 所有节点都生效的 call optioncompiledGraph.Invoke(ctx, input, WithCallbacks(handler))
// 只对特定类型节点生效的 call optioncompiledGraph.Invoke(ctx, input, WithChatModelOption(model.WithTemperature(0.5)))
// 只对特定节点生效的 call optioncompiledGraph.Invoke(ctx, input, WithCallbacks(handler).DesignateNode("node_1"))
```

**发现独门秘笈**

现在，想象一下你的球队里有一些明星球员（中场大脑 ChatModel 和锋线尖刀 StreamableTool）身怀绝技，他们踢出的球速度如此之快，甚至出现了残影，看上去就像是把一个完整的足球切成了很多片！

面对这样的 “流式” 足球，对手球员手足无措，不知道该如何接球，但是你的球队的所有队员，都能够完美的接球，要么直接一个片一个片的接收 “流式” 足球并第一时间处理，要么自动的把所有片拼接成完整的足球后再处理。身怀这样的独门秘笈，你的球队具备了面对其他球队的降维打击能力！

在 Eino 中，开发者只需要关注一个组件在 “真实业务场景” 中，是否可以处理流式的输入，以及是否可以生成流式的输出。根据这个真实的场景，具体的组件实现（包括 Lambda Function）就去实现符合这个流式范式的方法：

```
// ChatModel 实现了 Invoke（输入输出均非流）和 Stream（输入非流，输出流）两个范式type ChatModel interface {    Generate(ctx context.Context, input []*Message, opts ...Option) (*Message, error)    Stream(ctx context.Context, input []*Message, opts ...Option) (       *schema.StreamReader[*Message], error)}
// Lambda 可以实现任意四种流式范式
// Invoke is the type of the invokable lambda function.type Invoke[I, O, TOption any] func(ctx context.Context, input I, opts ...TOption) (    output O, err error)
// Stream is the type of the streamable lambda function.type Stream[I, O, TOption any] func(ctx context.Context,    input I, opts ...TOption) (output *schema.StreamReader[O], err error)
// Collect is the type of the collectable lambda function.type Collect[I, O, TOption any] func(ctx context.Context,    input *schema.StreamReader[I], opts ...TOption) (output O, err error)
// Transform is the type of the transformable lambda function.type Transform[I, O, TOption any] func(ctx context.Context,    input *schema.StreamReader[I], opts ...TOption) (output *schema.StreamReader[O], err error)
```

Eino 编排能力会自动做两个重要的事情：

1. 上游是流，但是下游只能接收非流时，自动拼接（Concat）。

2. 上游是非流，但是下游只能接收流时，自动流化（T -> StreamReader [T]）。

除此之外，Eino 编排能力还会自动处理流的合并、复制等各种细节，把大模型应用的核心 —— 流处理做到了极致。

**一场训练赛 -- Eino 智能助手**

好了，现在你已经初步了解了 Eino 这支明星球队的主要能力，是时候通过队员 (组件)、战术 (编排)、工具 (切面、可视化) 来一场训练赛，去亲自体验一下它的强大。

**场景设定**

Eino 智能助手：根据用户请求，从知识库检索必要的信息并按需调用多种工具，以完成对用户的请求的处理。工具列表如下：

* DuckDuckGo：从 DuckDuckGo 搜索互联网信息
* EinoTool：获取 Eino 的工程信息，比如仓库链接、文档链接等
* GitClone：克隆指定仓库到本地
* 任务管理 (TaskManager)：添加、查看、删除 任务
* OpenURL：使用系统的默认应用打开文件、Web 等类型的链接

这里呈现一个 Demo 样例，大家可根据自己的场景，更换自己的知识库和工具，以搭建自己所需的智能助手。

先来一起看看**基于 Eino 搭建起来**的 Agent 助手能实现什么效果：

构建这个 Eino 智能助手分两步：

* Knowledge Indexing（索引知识库）：将我们在特定领域沉淀的知识，以分词、向量化等多种手段，构建成索引，以便在接收用户请求时，索引出合适的上下文。本文采用向量化索引来构建知识库。
* Eino Agent（Eino 智能助手）：根据用户的请求信息以及我们预先构建好的可调用的工具，让 ChatModel 帮我们决策下一步应该执行什么动作或输出最终结果。Tool 的执行结果会再次输入给 ChatModel，让 ChatModel 再一次判断下一步的动作，直至完成用户的请求。

**任务工作流**

**索引知识库 (Knowledge Indexing)**

将 Markdown 格式的 Eino 用户手册，以合适的策略进行拆分和向量化，存入到 RedisSearch 的 VectorStore 中，作为 Eino 知识库。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gW9F4uDZpE8I63LTGjPPssnK15UB8gK36nzMyvrtoKf31EQPiccNiaicNfawvfibuLs05td0f5M6Jkh31g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**Eino 智能体 (Eino Agent)**

根据用户请求，从 Eino 知识库召回信息，采用 ChatTemplate 构建消息，请求 React Agent，视需求循环调用对应工具，直至完成处理用户的请求。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gW9F4uDZpE8I63LTGjPPssnK88cJ9pdDbqiaPjv8H2sq2a4KIPicFpVjnkdATD8uRnQFXricveMZa1icBQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**所需工具**

在从零开始构建「Eino 智能助手」这个实践场景中，需要下列工具：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gWicBnh8bApkqXficjcia1XN8qBPLoX1AJDiaYq4AXvG2sRCISbYZaak2IuWjdlOw7HaEONWVGE1vs7C9g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**索引知识库**

> 示例的仓库路径：https://github.com/cloudwego/eino-examples/tree/main/quickstart/eino\_assistant
>
> 下文中，采用相对于此目录的相对路径来标识资源位置

构建一个命令行工具，递归遍历指定目录下的所有 Markdown 文件。按照标题将 Markdown 文件内容分成不同的片段，并采用火山云的豆包向量化模型逐个将文本片段进行向量化，存储到 ...