---
title: 一个项目带你入门AI应用开发06 - bamb00
url: https://www.cnblogs.com/goodhacker/p/22167488
source: 博客园 - bamb00
date: 2026-08-03
fetch_date: 2026-08-04T04:56:32.518887
---

# 一个项目带你入门AI应用开发06 - bamb00

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

# [一个项目带你入门AI应用开发06](https://www.cnblogs.com/goodhacker/p/22167488 "发布于 2026-08-03 11:29")

# 第 6 课：让 Agent 记住对话

## 6.1 你的目标

多轮对话中，AI 能记住前面说了什么：

```
You: 查一下订单 ORD-001
AI: 您的订单 ORD-001（智能蓝牙耳机 Pro）已发货

You: 这个保修多久？     ← 用户期望 AI 知道说的是"耳机"
AI: 智能蓝牙耳机 Pro 提供 12 个月质保。  ← 没忘！
```

## 6.2 问题和解决方案

### 为什么 AI 会忘？

每次请求的 `state["messages"]` 都是空列表。Agent 没有上下文，每次都是"第一次见到用户"。

### 解法：把历史消息传进去

```
# main.py 中
sessions: dict[str, list] = defaultdict(list)
conv_id = req.conversation_id or str(uuid.uuid4())
history = sessions[conv_id]

initial_state = {
    "user_message": req.message,
    "messages": history,         # ← 把历史传进去！
    ...
}

result = agent_graph.invoke(initial_state)

# 保存本轮对话
history.append({"role": "user", "content": req.message})
history.append({"role": "assistant", "content": result["final_response"]})
```

### 为什么不能存所有历史？

聊 50 轮后，history 会有 100 条消息，几千个 token。LLM 的上下文窗口是有限的。

### 解法：滑动窗口

```
MAX_HISTORY = 10  # 最多保留 10 轮

def save_history(conv_id, user_msg, reply):
    history = sessions[conv_id]
    history.append({"role": "user", "content": user_msg})
    history.append({"role": "assistant", "content": reply})
    # 只保留最近 10 轮
    if len(history) > MAX_HISTORY * 2:
        sessions[conv_id] = history[-MAX_HISTORY * 2:]
```

**为什么是 10 轮？** 这不是一个固定的答案。取决于你的业务场景：

* 客服对话通常 3-5 轮解决问题，10 轮足够
* 如果是长周期跟进（如售后多次沟通），可能需要更多

## 6.3 Agents 怎么使用历史

之前每个 Agent 的 LLM 调用只传 `user_message`，现在加上历史：

```
def tool_node(state):
    history = state.get("messages", [])      # ← 拿到历史
    msg = call_llm(
        messages=[
            {"role": "system", "content": TOOL_PROMPT},
            *history,                        # ← 展开到 prompt 中
            {"role": "user", "content": state["user_message"]},
        ],
        tools=TOOLS,
    )
```

Router Agent 看到历史后，能理解"这个"指的是什么。Tool Agent 看到历史后，知道用户之前已经提供过订单号。

## 6.4 内存存储的局限

当前会话存在 Python 进程的内存里。服务重启后所有会话丢失。

生产环境应该用 Redis 或数据库存储会话：

```
# 当前（内存）
sessions: dict[str, list] = defaultdict(list)

# 生产（Redis）
import redis
r = redis.Redis()
history = json.loads(r.get(f"session:{conv_id}") or "[]")
```

但第 6 课的重点是理解"有状态"这个模式，而不是具体的存储方案。

## 6.5 三种记忆策略对比

| 方案 | 实现复杂度 | 信息保留 | Token消耗 | 适用场景 |
| --- | --- | --- | --- | --- |
| 滑动窗口 | 低 | 丢失早期信息 | 可控 | 短对话（<20轮） |
| 摘要压缩 | 中 | 保留核心信息 | 低 | 中等长度对话 |
| 向量检索记忆 | 高 | 几乎不丢失 | 中 | 超长对话、知识型对话 |

本课使用滑动窗口，因为简单且适配电商客服的场景。

## 本课知识点

| 概念 | 你做了什么 | 为什么 |
| --- | --- | --- |
| 有状态 | conversation\_id + 历史存储 | LLM 无状态，上下文全靠 messages 传 |
| 滑动窗口 | 保留最近 N 轮 | Token 消耗有上限，不会撑爆窗口 |
| 历史注入 | history 展开到 messages 里 | 每个 Agent 都能参考上文 |

## 课后作业

1. 把 MAX\_HISTORY 改成 2，看第 3 轮还能不能记住第 1 轮的信息
2. 给 sessions 加一个过期时间（比如 30 分钟不活跃就删除）

## 面试可能会问

> "Agent 系统的会话管理和传统 Web 应用的 Session 有什么不同？"
> Web Session 存的是用户登录状态。Agent 存的是对话历史（messages 数组），而且影响 LLM 的推理质量。管理不好 Agent 就会"失忆"。

posted @
2026-08-03 11:29
[bamb00](https://www.cnblogs.com/goodhacker)
阅读(294)
评论(0)

收藏
[举报](https://report.cnblogs.com?targetLink=https%3A%2F%2Fwww.cnblogs.com%2Fgoodhacker%2Fp%2F22167488&targetId=22167488&targetType=0)

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202607/35695-20260715081632770-1485313413.webp)](https://www.trae.com.cn/?utm_source=advertising&utm_medium=cnblogs_ug_cpa&utm_term=hw_trae_cnblogs)

### 公告

[博客园](https://www.cnblogs.com/)
  ©  2004-2026

[![](//assets.cnblogs.com/images/ghs.png)浙公网安备 33010602011771号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)