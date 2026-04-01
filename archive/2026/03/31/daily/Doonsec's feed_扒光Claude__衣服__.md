---
title: 扒光Claude\"衣服\"
url: https://mp.weixin.qq.com/s/4KHX_oI4_GHgsuSsR-6WOQ
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:42:50.513334
---

# 扒光Claude\"衣服\"

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Yvub5gSYgRibYcXg07mGosFGqDocicx7muYDKQ2hvBD10S5JD6YK5R95rbshGsuLcGTWKcwQB7YsLibMgN6Gbr4piaA00IuNYEYB5hCf8e57Mk0/0?wx_fmt=jpeg)

# 扒光Claude"衣服"

原创

Ghost Wolf Lab
Ghost Wolf Lab

Ghost Wolf Lab

![]()

在小说阅读器中沉浸阅读

## 写在前面

拿到Claude源代码的那一刻，我对代码仓库做了一次完整的架构扫描。本文不聊体验，不聊评测，只聊代码。我会按模块边界拆解这套系统的真实设计——它的入口、大脑、工具链和通信层长什么样，以及为什么这样设计。

## 入口层

代码入口分布在 cli.tsx 和 main.tsx，但真正的启动逻辑藏在 setup.ts 里。

先说结论：Claude的启动流程做了非常精细的分层解耦。

* `cli.tsx`只做两件事：解析命令行参数，走快速路径（--version、--help 这类指令直接返回，不加载任何重模块）
* `main.tsx`负责全局装配，包含明显的启动性能优化——提前并行预取、延迟加载、条件引入
* `setup.ts`负责环境落地：当前工作目录、会话快照、hook快照、工作树状态、终端恢复等

![](https://mmbiz.qpic.cn/mmbiz_png/Yvub5gSYgR941lCDNcD7X0yUmgFkt9SXBSGwomfgswRqtxKu2zWEckiawE7kciaKunvGWA6chuMZpHhcnJMkv5vJma8IKPvDFSx21qWV8Okaw/640?wx_fmt=png&from=appmsg&quot)

这个分层的好处是职责清晰，代价是三个文件之间的调用关系需要花点时间理清。但客观来说，这种设计对后续维护是有利的。

**值得注意的一点**：`setup.ts`里对会话状态的初始化做了memoize，意味着会话启动时的环境快照是一次性抓取的，避免了后续每轮对话重复读取文件系统带来的开销。

## 上下文与会话层

`context.ts`是整条链路上最关键的一环。

它的职责是构建注入给模型的system context和user context。我重点看了它的几个设计决策：

1. Git状态快照 会话开始时一次性抓取git状态并缓存，后续对话不再重复读取。这是一个典型的“读一次、用多次”模式，在长时间会话中能有效降低IO开销。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Yvub5gSYgRib2NfCnhgDZHicVxxDnWcUtG4ZNaL2EiaTJLuQHu3x6JhJIq8KyrNR0sJ9lX07H9K9IfLuvicRdiaEXbsVGUictdBFAapsKxzdia0NHA/640?wx_fmt=png&from=appmsg&quot)

2. 上下文缓存清理 代码里实现了cache breaker机制。当某些关键文件变更时，可以主动清空缓存，保证下一轮对话能拿到最新状态。这个设计在诊断日志里埋点也很完整，方便排障。
3. 降级策略 在bare模式下，user context会按规则降级——比如不读取Claude.md文件。这说明系统对不同运行环境有明确的契约约束，不是所有场景都追求“全功能”。

## 命令系统

命令注册中心在 `commands.ts`。

这是一个典型的**集中注册 + feature gate条件加载**的模式。所有命令的入口都在同一个文件里，枚举能力强，便于统一管理。

但代价也很明显：这个文件体量很大，多人协作时冲突概率高。新增命令时，所有人都要改同一个聚合点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Yvub5gSYgR9kTAEvoF9F9VAJiaMnbKfYuEpVHt986mlBG7zdx6aR8ThNhB0USnkzZM2Q5eC0ljWnSaFRuJNichl8hI285ZwVib4ibHemlS7hv8s/640?wx_fmt=png&from=appmsg&quot)

不过话说回来，这种模式对产品形态切换是有好处的。通过feature gate，同一套代码可以编译出不同能力集的版本，这是工程化成熟度的体现。

## 核心对话引擎

`QueryEngine.ts`和`query.ts`是整条链路上最复杂的区域。

`QueryEngine`扮演的是会话编排器的角色，实际执行循环在`query.ts` 里。它的职责涵盖：

* **用户输入处理**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Yvub5gSYgRicrMajibqJUrUBPk1S8udOY7HEM5dOrTKxhHVHQQ8iavHXnxlpd8MiaSXjibVFGoib5OfScWZqicwgKy85XOvgmIviafz8cV48x3ywam8/640?wx_fmt=png&from=appmsg&quot)

* **多模态调度器**:根据用户意图，智能调度不同的处理引擎，如普通对话引擎、代码解释器或外部工具调用。
* **命令与工具调用**:负责解析并执行命令，或调用注册的外部工具（Tools），并处理其输入输出。
* **权限判定**:在执行敏感操作或调用特定工具前，进行严格的权限检查，确保操作符合安全策略
* **预算与token控制**:实时计算和监控输入输出的Token数量，确保不超出模型上下文窗口限制，并为计费提供依据。
* **消息持久化**
* **维护可变消息状态与跨轮会话状态**

通过feature gate，这里可以拼接不同能力——比如snip、coordinator、compact等模块是按条件装配的。

**一个值得关注的设计点**：token预算控制不是简单的硬截断，而是通过compact机制做智能压缩。这意味着Claude在处理长上下文时，有明确的策略选择，而不是粗暴地丢掉历史。

## 工具与任务执行层

工具注册总表在`tools.ts`。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Yvub5gSYgR8OZ88DpoTpEsULbQAmPxw6lqc4iace3PRFrKRaVALYoruZVwtxXONia3TLAPQTnVtv8kPfNEG8Sxlr3L6zyxMYpFOicL2xe3Su5U/640?wx_fmt=png&from=appmsg&quot)

这里定义了所有可供模型调用的Tool集合，并在运行时做可用性过滤——环境、权限、feature gate都会影响哪些工具最终暴露给模型。

任务模型定义在`Task.ts`，任务分发在`tasks.ts`。

这套模式的优点很明显：声明式注册 + 运行时过滤 + 条件装配。想要新增一个工具能力，只需要在`tools.ts`里增加定义，不需要改动核心引擎。这种设计对持续迭代非常友好。

## 远程桥接层

`bridgeMain.ts`是远程桥接的主循环。

它的职责包括：

* 轮询与心跳
* 重试退避算法
* session生命周期管理
* 超时清理
* 多会话并发控制

这部分代码的工程化程度明显高于其他模块。大量细节考虑到位——比如心跳超时后如何处理、网络抖动时如何退避重试、多会话场景下如何隔离资源。

这说明Claude的设计从一开始就考虑了远程/多会话场景，而不是事后打补丁。

## 整体架构特征

扫描完整个代码库，可以看到几个关键特征：

1. 重度使用feature gate

通过编译时开关做死代码消除和产品形态切换。这意味着不同用户看到的Claude能力集可能不同，而代码库是同一套。

2. 大量lazy require

主要用于规避循环依赖和降低启动成本。这是Node.js生态里处理大型项目的成熟手段。

3. 日志与诊断埋点密集

每个关键路径都有埋点，线上排障时能快速定位问题。这是生产级系统的标配。

4. 模块边界清晰，但聚合文件较重

启动、环境、大脑、工具、桥接这几层分得清楚，但commands.ts这类聚合入口文件确实偏大，是后续可优化的点。

## 建议分析文件顺序

如果想查看源码，我建议按这个顺序：

* cli.tsx —— 理解入口
* main.tsx —— 理解装配
* setup.ts —— 理解环境初始化
* context.ts —— 理解上下文构建
* QueryEngine.ts + query.ts —— 理解核心对话循环
* tools.ts + Task.ts + tasks.ts —— 理解工具与任务
* bridgeMain.ts —— 理解远程通信

这个顺序遵循了“从外到内、从启动到执行”的原则，能最快建立全局认知。

调用链时序图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Yvub5gSYgRibLhiaUMoTIQx8lU2aHN0J4XSQWDEJHVAQOpATUoWnNG88rw8aEN7Bjv0jehXhLI3CnCtLlYTiaTXxNCUpNbwuDqC79a3QDH5rzk/640?wx_fmt=png&from=appmsg&quot)

代码：

```
sequenceDiagram
autonumber
participant U as 用户输入
participant M as main.tsx
participant P as print.ts runHeadless
participant RS as runHeadlessStreaming
participant A as QueryEngine.ask
participant QE as QueryEngine.submitMessage
participant Q as query.ts query loop
participant TE as ToolExecutor
participant T as 具体工具
participant O as StructuredIO/stdout
U->>M: CLI 参数/stdin prompt
M->>P: 调用 runHeadless(...)
P->>P: 初始化 structuredIO、权限回调、tools/mcp
P->>RS: for-await runHeadlessStreaming(...)
RS->>A: 调用 ask({...})
A->>QE: new QueryEngine + submitMessage(prompt)

QE->>QE: fetchSystemPromptParts + processUserInput
QE->>Q: 进入 query({...}) 主循环
Q->>Q: prependUserContext/appendSystemContext，发起模型流式响应
Q->>Q: 收集 assistant 中的 tool_use blocks

alt 流式工具执行开启
    Q->>TE: StreamingToolExecutor.getRemainingResults()
else 普通工具执行
    Q->>TE: runTools(toolUseBlocks,...)
end

TE->>T: runToolUse（逐个/并发）
T-->>TE: tool_result / progress / attachment
TE-->>Q: MessageUpdate(newContext/message)

Q-->>QE: yield assistant/user/system/result
QE-->>RS: 规范化并持续回放消息
RS-->>P: 流式产出 StdoutMessage
P->>O: structuredIO.write(...) 或最终 stdout 输出
```

## 最后

这套系统的强大不在于某个模块的“炫技”，而在于整体架构的克制与工程化。

课程：

[突破防御极限！《APT攻击原理深度刨析》第二批课程](https://mp.weixin.qq.com/s?__biz=MzI3OTM3OTAyNw==&mid=2247486221&idx=1&sn=8adf32e4826134cb076efc2981230b09&scene=21#wechat_redirect)

---

关注 Ghost Wolf Lab，获取更多前沿技术干货.

公开QQ群：`816112115`

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5F1cGSkUffMjPelmXP6PVz3ggEh1icEAF87iaeIb4TlVN9ZPSUCrNXlBqYYNIT7EjRhT5QBTZawC4Iro4ia1MZFEw/0?wx_fmt=png)

Ghost Wolf Lab

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5F1cGSkUffMjPelmXP6PVz3ggEh1icEAF87iaeIb4TlVN9ZPSUCrNXlBqYYNIT7EjRhT5QBTZawC4Iro4ia1MZFEw/0?wx_fmt=png)

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