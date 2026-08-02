---
title: 一个项目带你入门AI应用开发04 - bamb00
url: https://www.cnblogs.com/goodhacker/p/22139916
source: 博客园 - bamb00
date: 2026-08-01
fetch_date: 2026-08-02T05:10:33.991116
---

# 一个项目带你入门AI应用开发04 - bamb00

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

# [一个项目带你入门AI应用开发04](https://www.cnblogs.com/goodhacker/p/22139916 "发布于 2026-08-02 00:16")

# 第 4 课：让 Agent 调用工具

## 4.1 你的目标

用户说"查订单 ORD-001"，Agent 调用函数获取数据，再把结果组织成自然语言回复：

```
You: 查一下订单 ORD-001
[调用工具: query_order({"order_id": "ORD-001"})]
AI: 您的订单 ORD-001（智能蓝牙耳机 Pro，299元）已发货，正在配送中。
```

## 4.2 反例：硬编码分支

```
def handle_order(user_input):
    if "ORD-001" in user_input:
        return "您的订单 ORD-001 已发货"
    elif "ORD-002" in user_input:
        return "您的订单 ORD-002 正在处理中"
    else:
        return "请提供订单号"
```

### 这样为什么不行？

* 用户说"帮我查一下 001 那个订单"——没有 "ORD-"，匹配不到
* 新增订单要改代码
* 订单号多了 if-else 会变得非常长

### 本质问题是什么？

工具调用（查订单）的触发条件应该是 LLM 的判断，而不是写死的字符串匹配。LLM 能理解"查一下 001 那个订单"是在查什么，代码不行。

## 4.3 Function Calling 的原理

Function Calling 让 LLM 能看到你定义的工具列表，并且自主决定要不要调用、调用哪个、传什么参数。

### 工具定义

```
tools = [
    {
        "type": "function",
        "function": {
            "name": "query_order",
            "description": "查询订单状态和物流信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {"type": "string", "description": "订单编号"}
                },
                "required": ["order_id"],
            },
        },
    },
]
```

每个工具需要三样东西：

* **name**: 函数名，执行时用这个名字找到对应的 Python 函数
* **description**: LLM 靠这个描述来判断"当前场景要不要调用这个工具"
* **parameters**: JSON Schema 格式，告诉 LLM 需要什么参数

### LLM 的响应

如果不调工具，LLM 返回：

```
{"content": "直接回复用户", "tool_calls": None}
```

如果要调工具，LLM 返回：

```
{
    "content": None,
    "tool_calls": [
        {
            "id": "call_xxx",
            "function": {
                "name": "query_order",
                "arguments": '{"order_id": "ORD-001"}'
            }
        }
    ]
}
```

`content` 是 None，因为 LLM 没有直接回复——它决定由工具来提供信息。

## 4.4 为什么需要两轮 LLM 调用？

初学者最容易犯的错误：工具返回了 JSON 就直接拼接字符串返回给用户。

```
工具返回: {"found": true, "status": "shipped", "product": "智能蓝牙耳机 Pro"}
直接返回: "您的订单查询结果：{"found": true, "status": "shipped"}"
          ← 用户看到 JSON，体验很差
```

### 正确的流程

```
第一轮：LLM 决定调用 query_order
        → LLM 说"调 query_order，参数 order_id=ORD-001"
        → 我们执行 get_order("ORD-001")
        → 返回 {"found": true, "status": "shipped", "product": "智能蓝牙耳机 Pro"}

第二轮：把工具结果以 "tool" role 发回给 LLM
        → messages 变为：
          system: "你是电商客服系统的工具调用助手"
          user: "查一下订单 ORD-001"
          assistant: (tool_calls=...)
          tool: '{"found": true, "status": "shipped", "product": "智能蓝牙耳机 Pro"}'
        → LLM 看到结果后生成：
          "您的订单 ORD-001（智能蓝牙耳机 Pro）已发货，正在配送中。"
```

### 为什么不能直接拼接字符串？

工具返回的是 JSON 原始数据，LLM 需要：

1. **理解** JSON 的含义（"shipped" 对用户应该说"已发货"）
2. **翻译** 成自然语言（"智能蓝牙耳机 Pro, 299元" 比原始 JSON 更容易阅读）
3. **添加上下文**（"正在配送中"补充了用户关心的信息）

这叫"推理"（reasoning），不是简单的字符串拼接。

### 什么时候可以省略第二轮？

如果工具返回的已经是可以直接展示的内容（比如查百科返回了一段文字），那可以省略。但多数情况下，工具返回的是结构化数据，建议走两轮。

## 4.5 执行工具

```
def _execute_tool(name, args):
    if name == "query_order":
        order = get_order(args["order_id"])
        if order:
            return json.dumps({"found": True, "order": asdict(order)})
        return json.dumps({"found": False, "message": "未找到"})
    # ... 其他工具
```

注意结果统一用 `json.dumps` 序列化成字符串。因为 `tool` role 的 `content` 字段是字符串类型。

## 4.6 完整调用流程

```
def handle_with_tools(user_input):
    messages = [
        {"role": "system", "content": "根据用户问题调用合适的工具获取信息。"},
        {"role": "user", "content": user_input},
    ]

    # 第一轮：LLM 决定是否调用工具
    msg = call_llm(messages, tools=tools, tool_choice="auto")
    tool_calls = msg.get("tool_calls")

    if not tool_calls:
        return msg.get("content", "")

    # 第二轮：执行工具 + 结果回传
    messages.append({"role": "assistant", "content": None, "tool_calls": tool_calls})
    for tc in tool_calls:
        name = tc["function"]["name"]
        args = json.loads(tc["function"]["arguments"])
        result = _execute_tool(name, args)
        messages.append({"role": "tool", "tool_call_id": tc["id"], "content": result})

    final_msg = call_llm(messages, temperature=0.3)
    return final_msg.get("content", "")
```

### tool\_choice 参数

* `"auto"`: LLM 自主决定要不要调工具（默认）
* `"required"`: 强制 LLM 必须调一个工具（用于"先查再说"的场景）
* `{"type": "function", "function": {"name": "query_order"}}`: 强制调指定工具

第 4 课用 `"auto"` 就够了。

## 本课知识点

| 概念 | 你做了什么 | 为什么 |
| --- | --- | --- |
| Function Calling | 定义 tools schema + tool\_choice | LLM 自主决定调用，不靠关键词匹配 |
| 工具描述 | name + description + parameters | LLM 靠 description 判断何时调用 |
| 两轮调用 | 决策 → 执行 → 推理 | 工具返回 JSON，需要 LLM 翻译成自然语言 |
| tool role | 把工具结果按 role 传回 | 符合 OpenAI 标准，LLM 能理解这是"工具说的" |

## 课后作业

1. 加一个 `get_discount` 工具，根据用户等级（vip/normal）返回折扣信息
2. 把 `tool_choice` 改成 `"required"`，观察 LLM 的行为变化

## 面试可能会问

> "Function Calling 的 tool\_choice=auto 和 tool\_choice=required 有什么区别？分别用于什么场景？"
> auto: LLM 自主决定（多数场景）。required: 强制调用工具（如"必须先查数据库再回答"的场景）。
>
> "工具执行后为什么要把结果以 tool role 发回给 LLM？直接拼接字符串不行吗？"
> 工具返回的是原始数据，LLM 需要推理后生成自然语言。而且 tool role 的消息在后续对话中可以作为上下文，方便用户追问。

posted @
2026-08-02 00:16
[bamb00](https://www.cnblogs.com/goodhacker)
阅读(8)
评论(0)

收藏
[举报](https://report.cnblogs.com?targetLink=https%3A%2F%2Fwww.cnblogs.com%2Fgoodhacker%2Fp%2F22139916&targetId=22139916&targetType=0)

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202606/35695-20260609221536870-1777800795.webp)](https://www.volcengine.com/activity/codingplan?utm_campaign=hw&utm_content=hw&utm_medium=devrel_tool_web&utm_source=OWO&utm_term=cnblogs)

### 公告

[博客园](https://www.cnblogs.com/)
  ©  2004-2026

[![](//assets.cnblogs.com/images/ghs.png)浙公网安备 33010602011771号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)