---
title: Jev Engineering：用分级 AI 把 Agent 账单砍掉 90%
url: https://mp.weixin.qq.com/s/EWLfzHm3HbhE7gWLl11FhA
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:55:37.912924
---

# Jev Engineering：用分级 AI 把 Agent 账单砍掉 90%

# Jev Engineering：用分级 AI 把 Agent 账单砍掉 90%

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6ObJnnqeEecdmh66MJlcVpLoSbJ1E9rGo3lKuLsbLhaWdNgqbE12BcsfCjctyVqWmqQ4U7TqXnswl1w73YSOA2okuXBJwY5bW4/640?from=appmsg)
> **导语**：AI Agent 圈最近有个朴素的痛点——大模型调用贵、慢、还不能全信。@polydao 这篇长文推的是 **Jev Engineering** 这种工程范式：别让 Kimi K3 直接拍板，先把决策按"代价×确定性"分进四个桶，再用 Jev 快速挡掉 70%，剩下的才丢给 K3 兜底。100 封欺诈邮件实测：1.42 秒、96 对、花 7 美分。本文翻译完整 13 节 + API + 框架集成 + 成本数学。

---

## 一、问题：AI Agent 账单里 90% 在付"决策"

随便翻开一段 Agent 运行记录，会发现大部分模型调用根本不是在"创作"。下一个该调哪个工具？这个资料来源相关吗？测试通过了吗？这个命令安全吗？任务做完了吗？这些小判断在循环里出现的次数往往超过真正的产出工作，每一次都按一次满血生成（Full Generation）计费。

TypeSafe AI 在 2026 年 9 月 15 日公开了一个专做这种判断的模型 **Jev**：你给它状态（State，即当前上下文的结构化数据）和类型化的问题，它返回带概率的答案——通常 100ms 左右，输入 $0.042/百万 token，输出免费。

TypeSafe 自己工作流评测里，Jev 比被对比的 LLM **快 193.6 倍、省 444.6 倍**。公司自己说这个数字是上限，但量级不会骗人。

**Jev Engineering** 就是用好它的手艺——找出隐藏的决策、写出模型答得出的问题、按置信度路由、知道哪里会断。下面的 playbook 拿 Kimi K3 当兜底模型。

---

## 二、为什么"不会写"的模型反而好用

Diogo Almeida 是 InstructGPT 的共同作者，RLHF（Reinforcement Learning from Human Feedback，基于人类反馈的强化学习）那篇让 GPT-3 变成 ChatGPT 的论文。他给 Jev 站台的开场是批评自己当年那套技术——RLHF 训出来的模型会"讨好人类评分员"，它们口头汇报的置信度早就不代表真实正确率。

> 一个模型做某件事 95% 的准确率，但没法告诉你剩下的 5% 错在哪，你就不能自动化这件事。

Jev 用 TypeSafe 叫 RLCD（Reinforcement Learning for Calibrated Decisions，校准决策强化学习）的目标训练。它要的是"诚实的概率"：在你数据上，标 90% 的答案应该大约 90% 真的对。**单条答案可能错，这正是置信度数值的用处**——它告诉你的代码"这条可以执行，那条得送别处"。

**真实跑分**：Hassan（@nutlope）筛 100 封邮件，一半正常一半欺诈。Jev 用 1.42 秒全部分完，置信度 <95% 的 31 封转 K3。整个流水线 16 秒完成，96/100 正确，总成本 $0.07。Jev 在这账单里的份额是**三分之一美分**。

![四层决策架构：代码 → Jev → Kimi K3 → 人类](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6MROA8CV78RJffoNVusXBswIgMhNMtfAicMib1BUIHg3gsfiaibh82PvribJXKAzmOHia581VbrmwEgUTA16r2KFYFxPAq5kj1LSmic90/640?from=appmsg "四层决策架构：代码 → Jev → Kimi K3 → 人类")

---

## 三、第一步：把 Agent 的每一步分进四个桶

把一段真实 transcript 拉出来，每一步放进四个桶之一：

* **第一桶（创造）** — 模型确实在生成新内容
* **第二桶（精确规则）** — 该写代码搞定，模型是浪费
* **第三桶（从已知答案里挑）** — 需要模糊判断但有结构
* **第四桶（不可逆）** — 必须人来

**第三桶总是比预想的大**，Jev Engineering 动的是它。其他桶别动。

![法师读信：Jev 的隐喻——只读不写](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PflZAgHYwRk6ZZ4sibgASypPCuVmfngoZF98yrtuuzDJgyKI2HIia7EK50OWca6AHbIPmCUMPictTqzicPrJOf9NTXwNsBamCUDuY/640?from=appmsg "法师读信：Jev 的隐喻——只读不写")

---

## 四、三种题型：Choice / Score / Noul

Jev 不写一段话，它只答结构化题。返回永远是数字或枚举，下游 `if score >= 0.95` 这种路由才好写：

| 题型 | 问什么 | 返回 | 适用场景 |
| --- | --- | --- | --- |
| **Choice** | "发件人想从我们这儿要啥？" | 候选项 + 概率分布 | 队列路由、分类 |
| **Score** | "证据对论点支撑多强？" | 0-3 整数 | 质量评分、紧急度、相关性 |
| **Noul** | "这邮件是不是要付款或登录？" | 0-1 浮点（0.5=说不准） | 风险判定、完成判定 |

Noul 名字有意思——本质是"二元决策 + 显式 unsure"。0.5 不是默认值，是个信号值，意味着"我不确定，给我更多上下文"。下游代码看到 0.5 立刻升级到 K3 或者人去重看。

![三种题型：Choice / Score / Noul](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NgaAh4M1QelAaBCsZDONDewv1xENyBnFRxSwunLBaqiclv0AnOLoy9IuOvgVoNC6D89GLrOtZbibn2hibcudCkTk3plRvr2CuKbk/640?from=appmsg "三种题型：Choice / Score / Noul")

---

## 五、API 速查（TypeSafe SystemOne）

实操必知：

* **Endpoint**: `POST https://api.typesafe.ai/v1/systemone`，body 带 state、model、questions
* **Python SDK**: `pip install typesafe-sdk`，然后 `client.system_one(...)`
* **Model**: 调好阈值之后钉死 `jev-1.13.0`；`jev-latest` 会变
* **Size**: state + 所有 questions 总和 ≤ 64K tokens；state + 最长的单个 question ≤ 32K tokens（约 15 万字符英文）
* **Input**: 仅文本。字符串、JSON 对象、数组都行，不收图片
* **Rate Limits**: `jev-1.13` 上 1200 RPS / 250K TPS（TypeSafe 说会随容量调整）
* **Speed and Price**: 端到端 70-500ms，输入 百万，输出免费。条的决策0.42

---

## 六、Spec Fan-out：13 个问题只发一次文档

同一次请求里的所有问题**并行**对同一份 state 评估。TypeSafe 把它叫 **Speculative Fan-out（推测性扇出）**，这是你能控制的最大成本杠杆。

> 一组测试里，53,777 字符的文档、13 个问题，打包成一个调用比拆成 13 次调用**便宜 12.2 倍、快 10 倍**——主要因为 state 只发了一次。

两个硬边界：

1. 同一调用里的问题不能互相看答案——如果某决策需要新证据，先 fetch 再问
2. fan-out 只在问题共享 state 时才划算，不相关的问题分开发

![Spec Fan-out：一次调用并行 13 个问题](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6Mc7GiasL3ZAq8Vbg0VM625BYNe3KjbNrxLCibcHKk4pDZT38iaK2fOfWgmicVicZ9tNogXdgoycM4kDuvKRicXCdZGfpW9bDKr0MVPk/640?from=appmsg "Spec Fan-out：一次调用并行 13 个问题")

---

## 七、写问题才是真手艺

Jev 答得烂 90% 是问题写得烂。下面九条来自 TypeSafe 文档和已经在用 Jev 的团队：

1. **问题 ID 不会传给模型**——`is_fraud` 这种字段名 Jev 看不见，意思全得写在 instructions 和 criteria 里
2. **一道问题只问一个判断**——"这个紧急吗、是不是付费用户发的"是两个问题，拆开再在代码里组合
3. **描述场景，别描述程度**——"提到取消或拒付"是能勾的对错题，"非常生气"是情绪，裸数字当等级也是
4. **每个等级写成立得住的句子**——等级独立打分，"比上一级更严重"模型读不懂
5. **每个 Noul 都要让高分=是**——真的意思是"不安全"的 Noul 是埋着的 bug
6. **每个 Choice 加出口**——`other` 或 `none`，因为模型总得选一个，入口给不确定留位
7. **指准字段**——反引号路径如 `` `order.charges` `` 告诉 Jev state 的哪一块
8. **先发证据，代码层先过滤**——不相关的 state 堆多了准确率就掉。七条带 claim 的资料 > "研究看着差不多了"，裁剪到相关行的搜索结果 > 整页
9. **抽取改成选择**——Jev 不能产出 schema 之外的值。要从发票里抓供应商名？给它一个已知供应商列表让它挑

**强问/弱问对比**：

```
# 弱问
"is_fraud": Noul(instructions="Suspicious?")
"severity": Score(criteria=["Low", "medium", "high"])
"team": Choice(criteria={"billing": None, "support": None})

# 强问
"is_fraud": Noul(instructions=
"Does `email` ask for a payment, a bank change "
"or a login the sender never asked for before?")

"severity": Score(criteria=[
"Cosmetic, nobody is blocked",
"One customer blocked, a workaround exists",
"Several customers blocked, no workaround"])

"team": Choice(criteria={
"billing": "Charges, invoices, plan changes",
"support": "Product questions and bugs",
"other": "None of the above fits"})
```

![同一组问题，两种写法](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6PPLN4xU6CXnvEyRXGV5QpibvbVrCcDgibTSP4ozMhbawUkGoMKHdQoDaExhcWOytn7icyibmEjU2OsAGEPgxoEbea9mKAsPXwich1I/640?from=appmsg "同一组问题，两种写法")

![智者之塔：写作问题需要阅历](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6N3DaMrLJU0Boiaeo3515hd3qlZ1SXE8ww8ord7dEP8XbHdOgEM4thSxk0IRwgWLQuNETAFOiaxoJttynHlONnKuQhQkKZZFSEyg/640?from=appmsg "智者之塔：写作问题需要阅历")

---

## 八、Jev 的边界在哪

TypeSafe 公开了 `jev-1.13` 的 jaggedness 页（描述模型能力断层的页面）——每一项都有 harness 层的应对方案。

> 类型安全（Type Safety）意味着 Jev 不会返回 schema 之外的值，但它会返回**错误的合法值**。置信度阈值 + 第二模型才是最后一道防线。

---

## 九、Cascade：Jev 兜底 K3 的四层架构

把所有东西拼起来，每个决策过四层，在第一个有把握的那层停下来：

* **第 1 层（CODE）** — 硬规则：正则、白名单、字段比对
* **第 2 层（JEV）** — 模糊判断：~~$0.04/百万、~~100ms
* **第 3 层（KIMI K3）** — 难例：1M context、开放权重、可自托管
* **第 4 层（YOU）** — 不可逆动作

K3 适合放在第二位置有实际原因：升级上来的 case 经常需要整个 thread 和历史，K3 的 1M context 长度都一个价。它能读截图和扫描 PDF——Jev 不能。它的权重是开放的，同一段代码能跑 Moonshot API、Together 平台（Hassan 的方案）、或者你自己托管。

`other` 不会单独路由——K3 拿到的是 Jev 的猜测作为上下文。**两个都不确定时，两个答案并排给你，这是最快的复审**。

---

## 十、框架集成：LangChain / Pydantic AI / Vercel AI SDK

不用换框架，Jev 已经塞进三个最常见的：

**LangChain（langchain-typesafe）** 有两个中间件：

* `ModelRouterMiddleware` —— 让 Jev 按你写的 criteria 挑最便宜的能处理的模型
* `AutoModeMiddleware` —— 每次工具调用前先过一遍风险检查，这种危险动作分类器以前各 coding harness 一直藏着

**Pydantic AI（pydantic-ai-slim[typesafe]）** 把你的输出类型直接变问题：`Agent("typesafe:jev-latest", output_type=Triage)`。

* `bool` → yes/no
* `Literal` → Choice
* `IntEnum`（每个成员带 docstring）→ Score
* `X | None` → 加一个 "None of these" 选项
* `FallbackModel` 模式把不确定的答案丢给 LLM——两行写完 cascade

**Vercel AI SDK** 通过 `experimental_evaluate` 暴露 Jev，配 `@ai-sdk/typesafe-ai` provider；也能走 AI Gateway 用 `typesafe-ai/jev` 同样价格。

---

## 十一、Agent Swarm：Jev 掌舵，K3 群打工

同样的思路放大。当任务很大时，K3 的 Agent Swarm 干执行——最多 300 个子 agent 并行，Jev 处理 turn 之间的判断：下一个跑哪个角色、保留哪些 return、目标是不是达成了。

> 每个 turn 三次 Jev 调用花不到一美分，循环就能每轮检查"做完了吗"然后自停。done-check 落在中间带时，一次 K3 调用带着完整 state 拍板。

![Jev 调度 K3 Agent Swarm 的架构](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PibX87ic9lnsof5saxWZHSITJwRnhqK6mIlq7HMf1MzftCzMicricLRKkiax86dreh1oHvsbcyL1C9U9IrvbOzyRrvp4QKicQLWGqtA/640?from=appmsg "Jev 调度 K3 Agent Swarm 的架构")

---

## 十二、阈值和上线流程

阈值按动作定，不是按模型定。TypeSafe 文档给两个例子：人类审核的下限 0.5，破坏性动作的下限 0.9——但明说是"例子不是默认值"。归档 newsletter 可以比标欺诈邮件低很多。

**Shadow Week 灰度周**——让 Jev 同时打标签，老路径做决策。然后按置信度段对比：0.9+ 的答案几乎每次跟你一致，这一段就先自动化。

**钉版本 + 全量日志**：Model ID、完整分布、阈值、哪一层答的、之后发生了什么。日志就是你的评测集，钉版本意味着下个月阈值含义还是一样的。

**把问题当代码对待**——改 criteria 改的是线上行为。要版本化、在标注集上测、漂了就回滚。

![不同操作的置信度阈值（自生成）](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PgVr6O8nyPUPHfsIa7ichLnnzYh4B0K8Vt6WsPD2sjMaia93iaM6ibPIcTV7ia5AYuQUn0TgL4yZIN3C19bvyPNOg70ub48P50OIjU/640?from=appmsg "不同操作的置信度阈值（自生成）")

---

## 十三、The Math：10000 邮件账单对比

**每月 10000 封邮件**。假设 Jev 每次 1000 input token；全模型调用 1500 in / 300 out；10% 升级。

| 方案 | 单价 | 10000 封邮件总成本 |
| --- | --- | --- |
| 全 Kimi K3 | 15 每百万 token | **$450** |
| ...