---
title: 一个项目带你入门AI应用开发05 - bamb00
url: https://www.cnblogs.com/goodhacker/p/22148759
source: 博客园 - bamb00
date: 2026-08-02
fetch_date: 2026-08-03T05:31:40.435656
---

# 一个项目带你入门AI应用开发05 - bamb00

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [周边](https://cnblogs.vip/store)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19316348)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://www.cnblogs.com/my "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://www.cnblogs.com/my)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/goodhacker/)

# [人怜直节生来瘦，自许高材老更刚。](https://www.cnblogs.com/goodhacker)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/goodhacker/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/bamb00)
* 订阅
* [管理](https://i.cnblogs.com/)

# [一个项目带你入门AI应用开发05](https://www.cnblogs.com/goodhacker/p/22148759 "发布于 2026-08-02 12:48")

# 第 5 课：用 LangGraph 编排多 Agent 协作

## 5.1 你的目标

把前 4 课的功能（意图分类、RAG、工具调用、投诉升级）拆成独立的 Agent，用 LangGraph 状态图来编排。

```
用户输入 → Router(分类) → Knowledge(RAG) ─→ Summary(汇总) → 回复
                       → Tool(工具)    ─→
                       → Escalation(升级)─→
```

## 5.2 回顾：if-else 的瓶颈

第 2 课的代码大概长这样：

```
def handle_by_intent(user_input, intent):
    if intent == "greeting": ...
    elif intent == "order_query": ...
    elif intent == "complaint": ...
    elif intent == "product_inquiry": ...
    else: ...
```

到第 4 课上完，每个分支内部都变得很复杂：

* `product_inquiry` → 调 Chroma 检索 → 调 LLM 生成
* `order_query` → 调 LLM 决策 → 执行工具 → 再调 LLM 推理
* `complaint` → 调 LLM 生成工单

`handle_by_intent` 已经 80 行了。而且有一个**更严重的问题**：所有分支最后都要经过 Summary 统一回复格式，但你只能在每个分支里分别处理。

### 更致命的问题：扩展性

假设要加一个新的 `recommend` 意图（推荐商品）：

```
# 新增一个 if 分支
elif intent == "recommend":
    return handle_recommend(user_input)
```

看似只加了一行。但如果 `handle_recommend` 也要走知识库检索呢？你要重复写检索逻辑。如果后面还要加一个 `price_inquiry` 也要检索呢？还要再重复。

**重复的逻辑需要被抽象。** 这就是从"if-else 分支"到"有向图"的转变。

## 5.3 LangGraph 的三个核心概念

### 1. State（状态）

```
class AgentState(TypedDict):
    user_message: str      # 用户输入
    intent: str            # 路由结果
    retrieved_docs: list   # 知识库检索结果
    tool_results: list     # 工具执行结果
    final_response: str    # 最终回复
    thought_chain: list    # 处理链路日志
```

State 是所有 Agent 共享的数据结构。每个 Agent 从 State 读取它需要的信息，写入它产生的信息。

### 2. Node（节点）

每个 Agent 是一个函数：`(state) → 新的 state 字段`

```
def router_node(state):
    intent = classify(state["user_message"])
    return {"intent": intent}
```

knowledge\_node 只关心 `user_message`，写入 `retrieved_docs`。tool\_node 只关心 `user_message`，写入 `tool_results`。每个节点只修改自己的字段，不碰别人的。

### 3. Edge（边）

```
# 固定边：A 执行完一定走 B
workflow.add_edge("knowledge", "summary")

# 条件边：根据 state 的字段决定走哪个分支
workflow.add_conditional_edges(
    "router",
    route_decision,          # 返回节点名的函数
    {"knowledge": "knowledge", "tool": "tool"}
)
```

条件边是 if-else 的替代品。`route_decision` 根据 `state["intent"]` 返回目标节点名，LangGraph 自动路由。

## 5.4 和第 2 课对比

**第 2 课的架构：**

```
main()
  └─ classify_intent()     ← 单次 LLM 调用
  └─ handle_by_intent()    ← if-else 分支
       ├─ handle_order()   ← 另一个 LLM 调用
       ├─ handle_product() ← 另一个 LLM 调用
       └─ handle_other()
```

if-else 的层级是扁平的，数据靠函数返回值传递。

**第 5 课的架构：**

```
StateGraph
  ├─ router_node        → 写入 intent
  ├─ knowledge_node     → 写入 retrieved_docs, final_response
  ├─ tool_node          → 写入 tool_results, final_response
  ├─ escalation_node    → 写入 escalation_ticket, final_response
  └─ summary_node       → 读取所有字段，写入 final_response
```

图结构的每个节点独立、可复用、可单独测试。

### 新增一个 Agent 要改几处？

**第 2 课（if-else）：**

1. 在 `INTENT_ROUTE` 加一行
2. 写新的处理函数
3. （如果要用到已有逻辑，可能会复制粘贴）

**第 5 课（LangGraph）：**

1. 写新的节点函数
2. `workflow.add_node("new", new_node)`
3. 在条件边的 mapping 里加一条
4. `workflow.add\_edge("new", "summary")"

第 1 步和第 2 步是必须的，第 3-4 步是"声明式"的——你只说你想要什么连接，LangGraph 负责执行。

## 5.5 为什么用 StateGraph(dict) 而不是 StateGraph(AgentState)？

```
# 本课使用的
workflow = StateGraph(dict)

# 严格类型化的版本
workflow = StateGraph(AgentState)
```

用 `dict` 更灵活——节点函数可以返回任意 key，不需要提前在 TypedDict 中声明。缺点是失去了类型检查。

对于课程来说，`dict` 更容易上手。生产环境建议用 TypedDict 获得 IDE 支持。

## 5.6 节点函数的共同模式

```
def xxx_node(state):
    # 1. 读取 state
    user_msg = state["user_message"]
    existing = state.get("thought_chain", [])

    # 2. 处理逻辑（调用 LLM、执行工具等）
    result = do_something(user_msg)

    # 3. 记录处理过程
    thought = {"agent": "xxx", "status": "completed", "output": result}

    # 4. 返回要更新的字段
    return {
        "xxx_result": result,
        "thought_chain": existing + [thought],
    }
```

**注意：** 每个节点都返回 `thought_chain: existing + [thought]`，而不是直接覆盖。这是为了保留所有节点的处理记录，不会因为后面节点的运行而丢失前面的记录。

## 5.7 对比运行

**第 2 课（if-else）：** 用户看不到处理过程，只能看到最终回复。

**第 5 课（LangGraph）：** 你可以查看 `result["thought_chain"]`，看到完整的处理链路：

```
→ router: order_query
→ tool: 您的订单已发货
→ summary: 已整合所有 Agent 输出
```

这为后续的流式输出和前端可视化打下了基础。

## 本课知识点

| 概念 | 你做了什么 | 为什么 |
| --- | --- | --- |
| StateGraph | 定义节点 + 边的图结构 | 替代 if-else，流程可视、易扩展 |
| 节点函数 | 每个节点只读写自己的字段 | 职责单一，不会互相干扰 |
| 条件边 | `add_conditional_edges` | 动态路由，新增意图只需加一条映射 |
| Thought Chain | 每个节点追加处理记录 | 可观测性——用户看到 Agent 的"思考过程" |

## 课后作业

1. 在图上加一个 `greeting` 节点（直接在节点中返回问候语，不调 LLM），并从条件边连过去
2. 把 `StateGraph(dict)` 改成 `StateGraph(AgentState)`，看看需要改动什么

## 面试可能会问

> "LangGraph 和手写 if-else 的本质区别是什么？"
> if-else 是"命令式"的——你写死每一步怎么走。LangGraph 是"声明式"的——你定义节点和连接方式，框架决定执行顺序。3 个节点以内没有区别，5 个以上后者优势明显。

> "State 的设计有什么需要注意的？"
> 每个节点只写自己的字段，不要覆盖别人的。如果两个节点都想写同一个字段，要明确谁有"最终解释权"。

posted @
2026-08-02 12:48
[bamb00](https://www.cnblogs.com/goodhacker)
阅读(94)
评论(0)

收藏
[举报](https://report.cnblogs.com?targetLink=https%3A%2F%2Fwww.cnblogs.com%2Fgoodhacker%2Fp%2F22148759&targetId=22148759&targetType=0)

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202512/35695-20251205182619157-1150461542.webp)](https://ais.cn/u/3Qf22e)

### 公告

[博客园](https://www.cnblogs.com/)
  ©  2004-2026

[![](//assets.cnblogs.com/images/ghs.png)浙公网安备 33010602011771号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)