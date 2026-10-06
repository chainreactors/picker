---
title: Agent Harness 实战：上下文压缩
url: https://mp.weixin.qq.com/s/BJag0bta6CXxs8fg2DG9Og
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:23:15.305981
---

# Agent Harness 实战：上下文压缩

# Agent Harness 实战：上下文压缩

原创

Z
Z

威胁情报Z分析

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0LGiaGIrzXunEAvbPNPkhSOMXaYTCno5UXFBIZhnWBOTfMkSaS029NM5hbXq9yFLabFRIn1Q2AIZGlK7Ua8DMhBtXnpGohTDgibxjOo097VsM/640?wx_fmt=png&from=appmsg)

## 1. 背景与痛点

##

Agent Harness 是一套标准化 Agent 执行框架，负责调度 LLM、工具调用、会话状态维护、多轮迭代。 Agent 多轮执行会持续累积：用户提问、LLM 思考、工具入参、工具返回结果、历史思考链。

**痛点：**

1. Token 持续暴涨，超出模型上下文窗口，直接报错截断
2. 大量冗余历史占据输入，LLM 容易上下文漂移、幻觉上升
3. API 成本随轮次线性上涨，长会话调用成本极高
4. 直接粗暴截断：丢失关键信息，Agent 任务直接失败

> 上下文压缩目标：**在尽可能保留任务关键信息前提下，降低上下文 Token 数量，不破坏 Agent 推理链路。**

##

## 2. Agent Harness 核心主循环

##

![](https://mmbiz.qpic.cn/mmbiz_png/0LGiaGIrzXuliaoNHnzvF7n0IZAZQqDC9ZSkVvHaT8dRwjOdMMhhF4S0I98ffsPf3gNMjDeuMiaw2MMxCobEdMkaMhSicgRlrHRXhXQnSWiaEVVw/640?wx_fmt=png&from=appmsg)

**循环说明：**

1. 每一轮迭代前，把用户 prompt、system prompt、全部历史会话、工具记录组装完整上下文
2. 做 Token 计数，到达阈值后执行上下文压缩
3. 压缩后的上下文交给 LLM 输出思考与工具 Action
4. 执行工具，工具结果追加进历史，回到循环起点

> 关键：**压缩发生在每轮 LLM 调用之前，不是事后清理。**

##

## 3. 什么是上下文压缩

##

上下文压缩不是简单截断字符串，分为几大类思路：

1. **摘要压缩 (Rolling Summary)**

   对久远会话做滚动摘要，原始历史丢弃，保留摘要文本
2. **窗口滑动 (Sliding Window)**

   保留最近 N 轮完整对话，更早历史全部摘要 / 丢弃
3. **选择性保留 (Sparse Compress)**

   过滤低价值消息，保留关键工具输出、关键决策，丢弃冗余日志
4. **分层记忆**

   短期记忆完整保存，中长期记忆做摘要向量检索召回
5. **工具结果专项压缩**

   大体积工具返回（文件读取、搜索结果）只保留头部 + 尾部 + 关键路径，丢弃中间冗余

> Agent Harness 设计：将压缩逻辑封装为独立组件`ContextManager`，和 Agent 主逻辑解耦，可插拔切换不同压缩策略。

##

## 4. 自动压缩决策流程

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0LGiaGIrzXukSLMH29eg6hV1etYnfdibdS6KFnSSuq8otsicuumHSu6Eic3mRn1taRKIBeQOoTGVKPNXBdI7KLh1UD7L4346Qua88IIeQ7LCeFw/640?wx_fmt=png&from=appmsg)

### 参数甜区（生产实测）

###

* 触发阈值：**上下文总 Token 达到窗口 70% 触发压缩**，不要等到 100% 再处理
* Sanity 校验两点：

1. 压缩后 Token 必须明显下降
2. 不能丢弃最近 N 轮完整交互（一般保留最近 6‑8 轮原始消息，不做摘要）

* 兜底降级：摘要策略失效时直接切滑动窗口，避免任务直接崩溃

##

## 5. 主流压缩策略实战

##

### 策略 1：Rolling Summary 滚动摘要

> 把旧的多轮对话交给 LLM 生成简短摘要，原始消息丢弃；最近 N 轮完整保留。

![](https://mmbiz.qpic.cn/mmbiz_png/0LGiaGIrzXum6RqVRcDqHQu4GJibzv0iaYWGTpkdXicbviakUyfiauM2jpW0ZlOFAqD6HkqlfxKXzy9hbuCh96hNZEGld21IqnVXiamMXwFDdkjibHw/640?wx_fmt=png&from=appmsg)

✅优点：Token 下降幅度大； ❌缺点：摘要会丢失细节，复杂工具任务容易丢失参数、路径信息；适合闲聊、简单任务，不适合重度工具 Agent。

### 策略 2：Sliding Window 滑动窗口

###

只保留最近 N 轮完整会话，更早历史全部丢弃。

* 优点：不会丢失最近细节，逻辑最稳定
* 缺点：过早历史全部丢失，长任务跨多轮后遗忘早期目标

###

### 策略 3：Sparse 选择性压缩（Agent Harness 推荐）

###

1. 最近 8 轮消息：**完全原样保留，不压缩**
2. 8 轮之前：过滤纯日志、重复报错；工具返回巨大 payload 只保留 head+tail，中间截断
3. 重要决策、用户原始目标、关键工具参数强制标记为不可删除
4. 久远部分做轻量摘要，不全部丢弃

> 实测甜区：成本压到原来 1/4，任务成功率 71%，优于粗暴截断与纯 Rolling Summary。

###

### 策略 4：向量记忆召回

###

久远会话转为向量存入向量库，不全部塞进 prompt；运行时根据当前 query 做相似度召回少量历史片段。

* 适合超长期会话；缺点增加向量库依赖，有召回失败风险。

## 6. 五层上下文压缩模型

##

| 层级 | 存储位置 | 处理策略 | 生命周期 |
| --- | --- | --- | --- |
| L0 System Prompt | 输入最顶层 | 永远保留，禁止压缩 | 全程 |
| L1 当前任务目标 | 用户原始请求 | 标记不可删除，强制保留 | 全程 |
| L2 短期记忆（最近 6‑8 轮） | Prompt 上下文 | 原始完整，不摘要 | 窗口内完整保存 |
| L3 中期记忆（8 轮之前） | Prompt 上下文 | 选择性压缩，工具结果裁剪、轻摘要 | 部分留在 prompt |
| L4 长期记忆 | 向量数据库 / 外部存储 | 摘要 + 向量，不塞进 prompt，按需召回 | 持久化 |

##

## 7. ContextManager 核心伪代码实现（Agent Harness）

##

```
"""Agent Harness ContextManager 上下文压缩组件"""from typing import Listimport tiktokenclass Message:    role: str    content: str    meta: dict  # meta["keep"]=True标记不可删除消息class ContextManager:    def __init__(        self,        window_max: int = 128000,        trigger_ratio: float = 0.7,        keep_recent_rounds: int = 8    ):        self.window_max = window_max        self.trigger_threshold = int(window_max * trigger_ratio)        self.keep_recent = keep_recent_rounds        self.history: List[Message] = []    def count_tokens(self, messages: List[Message]) -> int:        """统计上下文token数量"""        enc = tiktoken.get_encoding("cl100k_base")        total = 0        for m in messages:            total += len(enc.encode(m.content))        return total    def compress(self) -> List[Message]:        """对外暴露压缩入口"""        current_token = self.count_tokens(self.history)        if current_token < self.trigger_threshold:            return self.history.copy()        # 拆分：最近N轮完整保留；更早部分待压缩        keep_part = self.history[-self.keep_recent:]        old_part = self.history[:-self.keep_recent]        # 过滤标记强制keep的消息（system、原始用户目标）        must_keep = [m for m in old_part if m.meta.get("keep") is True]        compress_candidate = [m for m in old_part if not m.meta.get("keep")]        # 工具大结果裁剪：只保留头部+尾部        compressed_old = self._sparse_compress(compress_candidate)        final_ctx = must_keep + compressed_old + keep_part        # Sanity校验        after_token = self.count_tokens(final_ctx)        if after_token >= current_token:            # 压缩无效，降级滑动窗口兜底            return must_keep + keep_part        return final_ctx    def _sparse_compress(self, msg_list:List[Message]) -> List[Message]:        """选择性压缩，工具返回裁剪，可替换为RollingSummary"""        out = []        for m in msg_list:            if len(m.content) > 3000:                # 超长工具结果保留头500 + 尾500                head = m.content[:500]                tail = m.content[-500:]                m.content = f"[large output truncated]\n{head}\n...\n{tail}"            out.append(m)        return out
```

调用位置：Agent Harness 每轮循环，组装完历史之后，调用`ContextManager.compress()`拿到处理后的上下文，再传给 LLM。

> 工具结果落盘建议：超长工具返回不要全部塞 prompt，原始完整结果写入本地 / 缓存，上下文只放裁剪片段。

##

## 8. 性能对比：4 种方案实测

```

```

| 方案 | 相对 Token 成本 | 任务成功率 | 备注 |
| --- | --- | --- | --- |
| 无压缩 | 100% | 82% | Token 持续暴涨，极易超限报错 |
| 粗暴截断 | 32% | 41% | 直接砍掉尾部，丢失关键工具返回，大量失败 |
| 选择性稀疏压缩（推荐） | 24% | 71% | 生产甜区，保留最近轮次，裁剪大工具输出 |
| 过度 Rolling 摘要 | 18% | 53% | Token 最低，但细节丢失严重，复杂任务幻觉高 |

> 结论：不要追求极致低 Token，压缩的底线是保证 Agent 推理信息完整。

##

## 9. 常见反模式 Checklist

##

❌ 错误 1：等到 Token 占比 98% 才触发压缩，没有预留余量

❌ 错误 2：对最近 2‑3 轮交互做摘要压缩，破坏 Agent 思考链路

❌ 错误 3：直接截断 system prompt、用户原始目标 prompt

❌ 错误 4：过度依赖 Rolling Summary 处理重度工具调用 Agent

❌ 错误 5：压缩后不做 sanity 校验，越压缩 token 越大

❌ 错误 6：超长工具返回全部塞进上下文，不做裁剪落盘

✅ 正确：标记核心消息不可删除；优先压缩久远历史；设置降级兜底逻辑。

## 10. 落地实施路线

```

```

![](https://mmbiz.qpic.cn/mmbiz_png/0LGiaGIrzXun8ibCKibK3LhQfN0sd6SaGjhOtibVh7REtFJ7Rdfyo53LofTRZgXzGQ3Q4ot4wxurS8CM2GgpXl2icCzjehvZibiaK7VR6ruWpPWCsE/640?wx_fmt=png&from=appmsg)

**阶段 1**

给 Agent Harness 增加 token 统计埋点，观察真实业务会话 token 分布，确定触发阈值。

**阶段 2**

实现滑动窗口兜底，解决直接超限崩溃问题，优先保障可用性。

**阶段 3**

实现选择性稀疏压缩；对大工具返回做头 + 尾裁剪，关键消息标记不可删除；增加 sanity 校验降级。

**阶段 4**

可选，叠加 Rolling 摘要、向量长期记忆，适配超长会话场景

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0wJVoTDXBBkc5vFwntXsAd8nDxmDyBf0Z76ENz1lEx3EmN3upgBOvJOHKylGVwXH7KCZSXduJAuoib2MvH9Hyww/0?wx_fmt=png)

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