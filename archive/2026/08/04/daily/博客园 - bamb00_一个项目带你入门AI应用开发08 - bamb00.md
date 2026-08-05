---
title: 一个项目带你入门AI应用开发08 - bamb00
url: https://www.cnblogs.com/goodhacker/p/22202653
source: 博客园 - bamb00
date: 2026-08-04
fetch_date: 2026-08-05T04:58:16.163047
---

# 一个项目带你入门AI应用开发08 - bamb00

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

# [一个项目带你入门AI应用开发08](https://www.cnblogs.com/goodhacker/p/22202653 "发布于 2026-08-04 11:31")

# 第 8 课：工程化——让系统可靠、可观测、可测试

## 8.1 你的目标

给 Agent 系统加上生产级能力：

* **错误处理**：不同异常返回不同的 HTTP 状态码
* **日志**：每个 Agent 的执行耗时、异常记录
* **测试**：mock LLM，不依赖真实 API Key 也能跑

## 8.2 错误处理

### 反例：所有错误返回 500

```
try:
    result = agent_graph.invoke(state)
except Exception as e:
    raise HTTPException(500, f"处理失败: {e}")
```

这样做的问题：

| 实际发生的错误 | 返回的 HTTP 状态码 | 用户看到的 |
| --- | --- | --- |
| LLM API 超时 | 500 | "处理失败" |
| LLM 返回格式不对 | 500 | "处理失败" |
| 用户输入太短 | 500 | "处理失败" |
| 数据库连不上 | 500 | "处理失败" |

运维完全不知道哪里出了问题。

### 正解：分层异常

```
class LLMTimeoutError(Exception):
    """LLM 请求超时"""
    pass

class LLMFormatError(Exception):
    """LLM 返回格式不符合预期"""
    pass
```

然后在 API 层区分处理：

```
@app.post("/api/chat")
async def chat(req: ChatRequest):
    try:
        result = agent_graph.invoke(state)
        return result
    except LLMTimeoutError:
        # 503 = 服务暂时不可用，客户端可以重试
        raise HTTPException(503, "AI 服务暂时不可用，请稍后重试")
    except LLMFormatError:
        # 502 = 上游服务（LLM）返回异常
        raise HTTPException(502, "AI 返回格式异常")
    except ValidationError:
        # 400 = 客户端请求有问题
        raise HTTPException(400, "请求参数不合法")
    except Exception:
        # 500 = 服务器内部错误
        logger.exception("未预期的错误")
        raise HTTPException(500, "系统内部错误")
```

### 为什么异常分层很重要？

**给不同的人看不同的信息：**

* 用户看到友好的"服务暂时不可用"
* 前端看到明确的 HTTP 状态码（503 触发自动重试，400 不做重试）
* 运维从日志看到详细的 stack trace
* 开发者从"502"知道是 LLM 格式问题，去调整 prompt

### 重试机制

LLM API 经常因为网络波动或限流而失败。一次失败就抛异常太脆弱：

```
def call_llm(messages, max_retries=3):
    for attempt in range(max_retries):
        try:
            resp = session.post(url, json=body, timeout=60)
            return resp.json()["choices"][0]["message"]
        except requests.exceptions.Timeout:
            if attempt == max_retries - 1:
                raise LLMTimeoutError("请求超时")
            time.sleep(2 ** attempt)  # 1s → 2s → 4s
```

**为什么是指数退避？** 第一次失败可能是网络抖动，第二次可能是瞬时负载高，第三次如果还失败说明真的出了问题。每次重试等待时间加倍，避免对已过载的服务造成更大压力。

## 8.3 可观测性

### 节点耗时追踪

```
import time

def timed_node(name):
    def decorator(node_func):
        def wrapper(state):
            start = time.perf_counter()
            try:
                result = node_func(state)
                elapsed = time.perf_counter() - start
                logger.info(f"[{name}] 完成，耗时 {elapsed:.2f}s")
                return result
            except Exception:
                elapsed = time.perf_counter() - start
                logger.exception(f"[{name}] 在 {elapsed:.2f}s 后失败")
                raise
        return wrapper
    return decorator
```

这样每次请求都会记录：

```
2026-07-31 10:23:45 [INFO] [router] 完成，耗时 0.32s
2026-07-31 10:23:46 [INFO] [tool] 完成，耗时 1.87s
2026-07-31 10:23:46 [INFO] [summary] 完成，耗时 0.41s
```

**从日志中你能看到什么？**

* Tool Agent 最慢（1.87s）——因为它调了两次 LLM
* 如果某天 Tool Agent 突然变成 5s，说明 LLM API 变慢了
* 如果 Router 经常失败，说明 prompt 可能有问题

## 8.4 测试

### 为什么测试 Agent 很困难？

Agent 依赖 LLM，而 LLM 调用需要 API Key、需要网络、需要花钱。

### 解法：Mock LLM

```
# conftest.py
def mock_call_llm(messages, **kwargs):
    """不调真实 LLM，根据 prompt 关键词返回固定 JSON"""
    combined = " ".join(m.get("content", "") or "" for m in messages)

    if "意图分类" in combined:
        # 根据最后一条 user 消息判断返回什么意图
        last_user = [m["content"] for m in messages if m["role"] == "user"]
        text = last_user[-1] if last_user else ""
        if "投诉" in text:
            return {"content": '{"intent": "complaint", "reason": "mock"}'}
        elif "订单" in text or "物流" in text:
            return {"content": '{"intent": "order_query", "reason": "mock"}'}
        else:
            return {"content": '{"intent": "general", "reason": "mock"}'}

    return {"content": "mock 回复"}
```

### 这样测试有什么用？

不需要 API Key、不需要网络、测试秒级完成。测试的是 Agent 的逻辑（"意图为 complaint 时是否生成了工单"），而不是 LLM 的分类能力。

```
def test_complaint_creates_ticket():
    result = agent_graph.invoke({"user_message": "我要投诉", ...})
    assert result["escalation_ticket"] is not None
    assert "ticket_id" in result["escalation_ticket"]
```

### 那 LLM 的分类能力怎么测？

这是两个不同的问题：

1. **Agent 的逻辑是否正确** → 用 mock 测试（本课的内容）
2. **LLM 的分类能力是否满足需求** → 用评测集测试（不在本课范围内）

## 8.5 从第 1 课到第 8 课

```
第 1 课: 30 行 — 一个能聊天的终端程序
第 2 课: 80 行 — 加上意图分类和路由
第 3 课: 150 行 — 加上 Chroma 向量检索 RAG
第 4 课: 250 行 — 加上 Function Calling
第 5 课: 400 行 — 拆成 LangGraph 多 Agent
第 6 课: 500 行 — 加上会话管理
第 7 课: 600 行 — 加上可插拔数据源
第 8 课: 800 行 — 加上错误处理、日志、测试
```

**每一步增加的代码都对应一个真实遇到的问题。** 不是预先设计了一个大架构，而是问题驱动架构演进。

## 本课知识点

| 概念 | 你做了什么 | 为什么 |
| --- | --- | --- |
| 分层异常 | LLMTimeoutError / LLMFormatError | 不同问题返回不同 HTTP 状态码 |
| 指数退避 | 失败后等 1s/2s/4s | 避免对已过载的服务造成更大压力 |
| Mock 测试 | 固定 JSON 替换真实 LLM | 不消耗 API Key，离线可跑 |
| 节点耗时 | timed\_node 装饰器 | 性能瓶颈一目了然 |

## 课后作业

1. 给 `knowledge_agent.py` 也加上 try/except，当 Chroma 查询失败时返回降级回复
2. 在 conftest.py 中加一个 fixture，模拟 Chroma 查询失败的情况

## 面试可能会问

> "Agent 系统的测试和传统 Web 系统的测试有什么不同？"
> 传统 Web 测试依赖数据库/API，Agent 测试依赖 LLM。LLM 不可控、不可重复，所以需要 mock。难点在于 mock 的返回值要"像真的"——否则测不出逻辑缺陷。

> "为什么节点耗时日志对 Agent 系统特别重要？"
> Agent 系统比传统 Web 系统多了一层不确定性（LLM 响应时间波动大）。如果 Router 突然从 0.3s 变成 3s，不一定是你代码有问题，可能是 LLM API 变慢了。没有耗时日志，你无法区分"代码 bug"和"上游变慢"。

posted @
2026-08-04 11:31
[bamb00](https://www.cnblogs.com/goodhacker)
阅读(225)
评论(0)

收藏
[举报](https://report.cnblogs.com?targetLink=https%3A%2F%2Fwww.cnblogs.com%2Fgoodhacker%2Fp%2F22202653&targetId=22202653&targetType=0)

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202512/35695-20251205182619157-1150461542.webp)](https://ais.cn/u/3Qf22e)

### 公告

[博客园](https://www.cnblogs.com/)
  ©  2004-2026

[![](//assets.cnblogs.com/images/ghs.png)浙公网安备 33010602011771号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)