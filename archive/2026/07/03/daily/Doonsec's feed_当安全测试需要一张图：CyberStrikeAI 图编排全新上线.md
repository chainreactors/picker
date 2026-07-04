---
title: 当安全测试需要一张图：CyberStrikeAI 图编排全新上线
url: https://mp.weixin.qq.com/s/mCxc09AW5NhGRaYWvEuB0w
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:39:07.981736
---

# 当安全测试需要一张图：CyberStrikeAI 图编排全新上线

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ufQ2xnAD33vyYO8fxRHRaF5eSsqZsyjTPHHGFqBfBZtavTDzUQI0JHYewal9aZJJkwhxJFicH7eUWuCSOmjMtzdueBwtJwR6VNB3hjByvoJ8/0?wx_fmt=jpeg)

# 当安全测试需要一张图：CyberStrikeAI 图编排全新上线

原创

低调学安全
低调学安全

低调学安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 有些任务，交给 Agent 自己摸索就够了；有些任务，你必须先画好路线图。CyberStrikeAI 本次**新增图编排（Graph Orchestration）**，就是为后者准备的。

---

## 一、这次新增了什么？

CyberStrikeAI 的核心能力是：**用 AI + MCP 把 100+ 安全工具串起来，让渗透测试像对话一样发生。**

此前，平台已具备基于 Eino 的**Agent 编排**——单代理、Deep、Plan-Execute、Supervisor 等模式，让模型在运行时自主决策。这一次，我们**新增图编排**：在 Web 端用画布拖拽节点、连线，把步骤、分支、审批点固化成可保存、可绑角色、可重复执行的流程图。

两种编排方式，对应两种不同的工作方式：

| 路径 | 代表能力 | 本质 |
| --- | --- | --- |
| **Agent 编排** | Eino 单代理 / Deep / Plan-Execute / Supervisor | 模型**在运行时**决定下一步做什么 |
| **图编排** | 画布上的 Start → Agent → Tool → Condition → HITL → Output | 人**在运行前**把步骤、分支、审批点画清楚 |

* **探索型任务**：目标模糊、攻击面未知、需要临场换招——协调主代理带着子代理和 MCP 工具自由发挥，往往更合适。你描述意图，它拆任务、派单、汇总。
* **规程型任务**：SOP 已定、合规要留痕、高危步骤必须卡点、多角色要按固定顺序接力——你需要一张**可审计、可复现、可版本化**的流程图，而不是每次对话都重新「即兴演出」。

安全行业对此并不陌生：红队有 playbook，蓝队有 runbook，合规审计要的是「你**按什么顺序**做了什么」，而不只是「AI 最后说了什么」。

图编排承载的，是**显式流程契约**：步骤、分支、传参、审批点，全部落在一张图上。左侧导航**图编排** 入口、角色绑定`workflow_id`、完整使用文档，均已随本次更新一并提供。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33sibHOlVxjM1YZjqZjuy0tAKNmIWic9MBRB8hafblmQtUrkV5Kia5niaoqvxw5VLBkY5iaNEBrP6RqR6QkvlfDia4z67XBeLula5HWAU/640?wx_fmt=png&from=appmsg)

---

## 二、什么时候该画图，什么时候别画？

### 适合图编排的场景

1. **固定流水线**
   例如：子域枚举 → 端口扫描 → Web 指纹 → 按结果分支到 nuclei / sqlmap。步骤稳定，只是目标参数在变。
2. **条件分支必须确定**
   「扫到 443 且证书含某 SAN → 走路径 A，否则走路径 B。」这类逻辑写在图里，比写在 prompt 里可靠一个数量级。
3. **人机协同（HITL）卡点**
   利用链、C2 下发、批量 exploit 之前，流程必须在**指定节点**暂停等人点头。图编排把 HITL 嵌进拓扑，而不是靠模型「记得问一下」。
4. **多 Agent 分工但顺序固定**
   侦察 Agent 的输出命名写入`outputs.recon_summary`，验证 Agent 只读这个变量继续——**角色分工仍用 Agent，交接规则由图保证**。
5. **交付给团队的可复用资产**
   画布保存为`workflow_id`，绑到角色上，新人选角色即跑同一套流程。这是**组织知识**，不是个人聊天记录。

### 不必图编排的场景

1. **开放式渗透 / CTF**
   路径未知，强行画图会束缚模型；用 Deep 或多代理模式更合适。
2. **一次性 ad-hoc 查询**
   「帮我用 fofa 查一下这个域」——单轮工具调用，图为它建流程是过度设计。
3. **强依赖上下文的连续博弈**
   与目标多轮交互、根据每一轮响应即时改策略——这恰恰是 Agent 编排的主场。

**一句话**：图编排适合「**我知道该怎么做**」；Agent 编排适合「**我不知道会碰到什么，但要做到底**」。按场景选即可。

---

## 三、技术实现：画布之下发生了什么？

图编排不是前端花架子，背后是一套完整的工作流引擎。保存时，画布上的 JSON 会经校验、编译，再交给**CloudWeGo Eino Compose** 执行。

### 3.1 从`graph_json` 到可运行图

用户在 Web 端拖拽的节点与边，持久化为`graph_json`。保存时引擎会：

* 解析图结构，检查至少一个**Start**、一个**Output**，禁止 Start 有入边、Output 有出边；
* **试编译（trial-compile）**：编译不过则无法保存，把配置错误拦在运行前；
* 编译结果按`workflow_id + version` 缓存，图未变则复用，减少重复编译开销。

核心编译逻辑在`internal/workflow/engine.go`：每个画布节点映射为 Eino`Workflow` 上的一个节点——普通节点是`LambdaNode`，**Agent 节点则编译为子图（GraphNode）**，内部仍可走`eino_single` 或`deep` /`plan_execute` /`supervisor` 等模式。图是外层调度骨架，Agent 是节点内的执行单元，二者可以嵌套使用。

### 3.2 执行模型：有向图 + 运行时状态机

执行从**Start** 出发，沿边遍历。引擎维护一份`WorkflowLocalState`，其中三块状态决定模板变量如何取值：

| 状态 | 模板前缀 | 含义 |
| --- | --- | --- |
| `inputs` | `{{inputs.message}}` 等 | 用户消息、会话 ID、项目 ID |
| `lastOutput` | `{{previous.xxx}}` | **执行顺序上** 上一节点的输出（不是画布上的「上游」） |
| `outputs` | `{{outputs.变量名}}` | 全局命名变量池，由节点的`output_key` 写入 |

这里有一个容易踩坑、但恰恰体现设计深度的点：

> `{{previous.output}}` 是「链式上一步」，不是「连线上游」。

若路径是`Agent A → 条件 → Agent B`，则 B 的`previous` 是条件节点的`true/false`，**不是** A 的扫描结果。跨条件、跨工具节点传参，应使用`{{outputs.agent_result1}}` 这类命名变量。

这是图编排与「简单管道」的本质区别：**拓扑是拓扑，数据流是数据流**；用`outputs` 注册表把二者解耦，才能画分支而不丢上下文。

### 3.3 节点类型与能力边界

| 节点 | 作用 |
| --- | --- |
| **Start** | 注入`inputs`，流程入口 |
| **Agent** | 调用 Eino 单代理或多代理，支持节点级`instruction` 与`input_source` 模板 |
| **Tool** | 直接调 MCP 工具，参数 JSON 支持`{{...}}` 模板 |
| **Condition** | 表达式求值，驱动是/否分支 |
| **HITL** | 人工审批检查点；编译时注册`InterruptBeforeNodes`，配合 checkpoint 可暂停恢复 |
| **Output** | 写入最终`outputs`，供对话摘要展示 |
| **End** | 可选结束摘要模板 |

工具节点走`ExecuteMCPToolForConversation`，与聊天里调工具同一套 MCP 桥接。

### 3.4 可靠性与审计

* **Checkpoint**：运行状态落盘`data/workflow-checkpoints`，长流程与 HITL 中断后可恢复。
* **运行记录**：`workflow_runs` 表记录每次执行的输入、输出、状态、pending HITL 节点，与平台审计日志、对话历史同轨。
* **进度事件**：对话页可订阅`workflow_start`、`workflow_node_start`、`workflow_tool_start` 等，图执行过程对用户可见，而非黑盒跑完才给结果。

---

## 四、怎么用：从画布到角色对话

### 4.1 搭建流程

1. 登录 Web 控制台 → 左侧**图编排**
2. 新建或选择流程，在画布添加节点、连线
3. 填写流程**ID**、**名称**、**描述** →**保存**（触发校验与编译）

画布操作：添加节点、连线模式、右侧属性面板、自动布局、删除选中。建议每个需被下游引用的 Agent/工具节点都设好**`output_key`**（如`scan_result`、`parsed_targets`）。

### 4.2 绑定角色

**角色管理** 中为角色选择绑定的`workflow_id`，策略设为`auto`：

```
name: 外网资产巡检
workflow_id: asset-scan-v1
workflow_version: latest
workflow_policy: auto
```

用户选择该角色发消息后，对话入口会加载对应图并自动执行。

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33tpLaeA2IE8NxXs48XRL7VkAnreYWaSBIyhc0Udu5iax4rcCF4oevK5mpJg25LvkHkvFJpHeCMHHLmpwibHmvRZPibn5ajcuEg8Zw/640?wx_fmt=png&from=appmsg)

### 4.3 模板传参口诀

* **直连两步**：`{{previous.output}}` 最简
* **中间有条件/工具/审批**：上游写`output_key`，下游用`{{outputs.xxx}}`
* **读用户原始输入**：`{{inputs.message}}`
* **条件判断**：优先基于`{{outputs.xxx}}`，避免误用`previous` 拿到`true/false`

### 4.4 示例：跨条件传递 Agent 结果

```
开始 → Agent（侦察，output_key: recon）→ 条件（{{outputs.recon}} != ""） ├─ 是 → Agent（验证，输入: {{outputs.recon}}）→ 输出 └─ 否 → 输出（静态说明「无结果」）
```

若 Agent（验证）误写`{{previous.output}}`，拿到的是条件的布尔值——这是文档里最高频的排错点，也是理解执行模型的钥匙。

更完整的节点字段说明、连线条件、排错表，见项目内文档：docs/workflow-graph.md

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33sMyWlUJqcWPBYj3HPZTFylt8chcibRQVYYK4ch3zaIMQWBLqG9dIr1Vn9icw2VUvq7g5V62XQvrE3JOtbvq1naT9XSmiaJ7xNmmM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33s7ib3pbxrztBqxayZPTEwtFoPUhZ2oa6VCab2CvcU9BQq3lGghh1JaSUL28q6YXaYRbeAElciaF5cbibQfRp8hqialv21Laicz8OHQ/640?wx_fmt=png&from=appmsg)

---

## 五、一张图背后的设计取舍

这次做图编排，背后有几条清晰的产品判断：

1. **模型的不确定性在探索任务里是优势**——开放场景应交给 Agent 编排。
2. **规程与合规需要确定性**——关键路径可以外置为人可读的图。
3. **图与 Agent 可以组合**——图里的 Agent 节点照样可以 Deep 编排；图管调度，节点管智能。
4. **安全测试的可复现性**——同一`workflow_id`、同一版本，团队得到的是同一拓扑；这比「上次 prompt 大概这么写的」更接近工程实践。

如果你手头有一份跑过无数次的巡检 SOP、一份必须留痕的授权测试检查表、一条「扫到高危必须先审批再继续」的纪律——**值得画一张图。**

---

## 六、快速上手清单

* [ ] 拉取 / 升级到最新 CyberStrikeAI，在左侧导航找到**图编排**
* [ ] 图编排页：Start + Output 各至少一个，试跑一条线性流程
* [ ] 为一个 Agent 节点配置`output_key`，下游用`{{outputs.xxx}}` 验证跨节点传参
* [ ] 角色管理绑定`workflow_id`，`workflow_policy: auto`
* [ ] 用该角色发一条测试消息，在对话页观察 workflow 进度事件
* [ ] 阅读 图编排使用说明 中的条件分支与 HITL 章节

---

欢迎在社区交流你的 playbook 是怎么画成图的。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/KzNYA6icKe6ny3nDMkDelsYYnPJzRX2erWFEia2S7Bqqc7CjicEpJYQtId7a2jXKCial6Mw8ck8IFQEqmZnldrG2EQ/0?wx_fmt=png)

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