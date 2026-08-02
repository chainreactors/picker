---
title: 一个项目带你 入门AI应用开发02 - bamb00
url: https://www.cnblogs.com/goodhacker/p/22137472
source: 博客园 - bamb00
date: 2026-08-01
fetch_date: 2026-08-02T05:10:36.567526
---

# 一个项目带你 入门AI应用开发02 - bamb00

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

# [一个项目带你 入门AI应用开发02](https://www.cnblogs.com/goodhacker/p/22137472 "发布于 2026-08-01 19:45")

# 第 2 课：让程序理解用户的意图

## 2.1 你的目标

用户输入不同的内容，程序自动判断意图并做出对应的回应：

```
You: 帮我查一下快递
[意图识别: order_query]
AI: 正在查询您的订单...

You: 你们的产品太差了
[意图识别: complaint]
AI: 非常抱歉，我已记录您的问题...

You: 你好
[意图识别: greeting]
AI: 你好！有什么可以帮你的？
```

## 2.2 反例：关键词匹配为什么不行？

你可能第一反应是写 if-else：

```
if "订单" in user_input or "物流" in user_input:
    handle_order()
elif "退货" in user_input or "投诉" in user_input:
    handle_complaint()
elif "产品" in user_input or "价格" in user_input:
    handle_product()
```

跑一下看看：

| 用户输入 | 期望 | 实际结果 |
| --- | --- | --- |
| "查一下我的快递到哪了" | 查订单 | ❌ 走了 else——没有"订单"关键词 |
| "我要退了这个耳机" | 投诉/退货 | ❌ 走了 else——虽然有"退"，但条件匹配不精确 |
| "这个订单我要投诉" | 投诉 | ⚠️ 同时包含"订单"和"投诉"，取决于 if 顺序 |

**为什么不行？** 语言是灵活的。"我的快递到哪了"明明是在查订单，但关键词匹配无法理解"快递"="查订单"这种语义关系。人类能理解，代码不行。

### 这个问题的本质是什么？

关键词匹配是在**字符层面**工作，而意图识别需要在**语义层面**工作。LLM 恰好擅长后者。

## 2.3 正解：让 LLM 做分类器

把分类规则写进 system prompt，让 LLM 来判断：

```
def classify_intent(user_input):
    prompt = """你是一个电商客服意图分类器。判断用户消息属于以下哪一类：
- order_query: 查询订单、物流、配送状态
- complaint: 投诉、不满、要求售后
- product_inquiry: 询问产品信息、功能、价格
- greeting: 问候、闲聊
- other: 其他

只返回 JSON 格式：{"intent": "<分类>", "reason": "<理由>"}"""

    reply = call_llm([
        {"role": "system", "content": prompt},
        {"role": "user", "content": user_input},
    ])

    import json
    try:
        parsed = json.loads(reply)
        return parsed.get("intent", "other")
    except json.JSONDecodeError:
        return "other"  # 解析失败时走最安全的路径
```

### 为什么 JSON mode 很重要？

你看 prompt 的最后一句："只返回 JSON 格式"。这是告诉 LLM 输出结构化的数据，而不是自然语言。

如果不加这句话，LLM 可能会回复：

```
我认为用户的问题是 order_query，因为他在查询订单状态。
```

加了之后，它会回复：

```
{"intent": "order_query", "reason": "用户在查询订单状态"}
```

结构化输出让下游代码可以直接 `parsed["intent"]`，不需要做文本解析。**这是 Agent 系统中反复出现的模式——LLM 负责理解，代码负责执行。**

### 为什么需要 try/except？

LLM 的输出没有 100% 的保证。即使你说了"只返回 JSON"，它偶尔也会输出别的。所以：

```
try:
    parsed = json.loads(reply)
    return parsed.get("intent", "other")
except:
    return "other"  # 兜底：走最安全的路径
```

这不是"偷懒"，而是**防御性编程**——承认 LLM 不可靠，并为不可靠做好准备。

## 2.4 路由表：替代 if-else

传统的 if-else：

```
def handle(user_input, intent):
    if intent == "greeting":
        return "你好！"
    elif intent == "complaint":
        return "已记录投诉..."
    elif intent == "order_query":
        return call_llm([...订单客服...])
    ...
```

改用路由表（dict）：

```
INTENT_ROUTE = {
    "order_query": handle_order,
    "complaint": handle_complaint,
    "product_inquiry": handle_product,
    "greeting": handle_greeting,
}

def handle_by_intent(user_input, intent):
    handler = INTENT_ROUTE.get(intent, handle_other)
    return handler(user_input)
```

**用 dict 代替 if-else 的好处：**

1. 新增意图：在 dict 里加一行，不用改 if-else 结构
2. 动态路由：dict 可以在运行时修改
3. 可配置：路由表可以放在配置文件里

### 更重要的：容错

```
handler = INTENT_ROUTE.get(intent, handle_other)
```

如果 LLM 返回了一个 `INTENT_ROUTE` 里不存在的意图（比如 `"return_request"`），程序不会崩溃，而是走 `handle_other` 兜底。

## 2.5 完整代码的结构

```
├── Settings              # 配置管理（第1课的内容）
├── call_llm()            # LLM 调用（第1课的内容）
├── classify_intent()     # ★ 本课新增：意图分类
├── handle_order()        # 订单处理
├── handle_product()      # 产品咨询
├── handle_other()        # 兜底处理
├── INTENT_ROUTE          # ★ 本课新增：路由表
├── handle_by_intent()    # ★ 本课新增：按意图路由
└── main()                # 主循环
```

**从第1课到第2课的变化：** 代码结构从"问→答"变成了"问→分类→按类回答"。只加了一层抽象，但系统的行为从"统一回复"变成了"按需响应"。

## 本课知识点

| 概念 | 你做了什么 | 为什么 |
| --- | --- | --- |
| 意图分类 | 用 LLM 替代关键词匹配 | LLM 理解语义，"快递到哪了"也能识别为 order\_query |
| System Prompt | 在 system 消息中定义分类规则 | 规则独立于具体对话，可单独优化 |
| JSON mode | 要求 LLM 输出 JSON + try/except | 结构化输出方便下游处理；异常时走兜底路径 |
| 路由表 | dict 替代 if-else | 新增意图只需加一行，不会破坏现有逻辑 |
| 容错 | route.get(intent, default) | LLM 输出未定义意图时，程序不会崩溃 |

## 课后作业

1. 在 prompt 里加一个 `price_inquiry` 意图，并在路由表中注册对应的处理函数
2. 把 `INTENT_ROUTE` 改成从 JSON 文件读取，体验"配置驱动"的思路

## 面试可能会问

> "System Prompt 和 User Prompt 的区别是什么？为什么分类规则放在 System 里？"
>
> "如果 LLM 返回了一个未定义的意图名称，你的系统会怎么处理？"

posted @
2026-08-01 19:45
[bamb00](https://www.cnblogs.com/goodhacker)
阅读(4)
评论(0)

收藏
[举报](https://report.cnblogs.com?targetLink=https%3A%2F%2Fwww.cnblogs.com%2Fgoodhacker%2Fp%2F22137472&targetId=22137472&targetType=0)

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202606/35695-20260609221536870-1777800795.webp)](https://www.volcengine.com/activity/codingplan?utm_campaign=hw&utm_content=hw&utm_medium=devrel_tool_web&utm_source=OWO&utm_term=cnblogs)

### 公告

[博客园](https://www.cnblogs.com/)
  ©  2004-2026

[![](//assets.cnblogs.com/images/ghs.png)浙公网安备 33010602011771号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)