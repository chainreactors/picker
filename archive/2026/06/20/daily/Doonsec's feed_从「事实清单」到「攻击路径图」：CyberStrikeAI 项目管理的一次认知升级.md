---
title: 从「事实清单」到「攻击路径图」：CyberStrikeAI 项目管理的一次认知升级
url: https://mp.weixin.qq.com/s/Ak_uBoz9z6m8sRHCpGd78A
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:45:37.260906
---

# 从「事实清单」到「攻击路径图」：CyberStrikeAI 项目管理的一次认知升级

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ufQ2xnAD33sYAUaia5yEDzPZjwYUvEkubBd9s2ribKH0DAJPGicE9PQ8oqckwqib5nJ5iauSLYfTJewgibIINXl1z5CeIDJ5eoHWsOy8r7ictw8cfc/0?wx_fmt=jpeg)

# 从「事实清单」到「攻击路径图」：CyberStrikeAI 项目管理的一次认知升级

原创

学安全也就图一乐
学安全也就图一乐

低调学安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 当 AI 帮你扫端口、跑 POC、写报告的时候，真正决定渗透质量的不是「发现了多少条」，而是「这些发现之间，是否存在一条可验证、可复现、可交接的攻击路径」。

---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33t9LyZCrdzCibooYShJxEndvibicr5CbE1ZgibtG4kdKxRdbAuDQTcZVcQRmx5XIhTHIQ5BqUGaQ9jEmrTC4cA7IXpicQo3tHP3nJM8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33sZzSialHicKgBsURZ4VL2ItWVtQ7YcKH1ib7tqJ3SjzbLbF0b0icM0pHG5u29mEtXc5V7Cgz9BnMCTxkLm5W4IV1qicXibgI3fyqjIc/640?wx_fmt=png&from=appmsg)

## 一、我们遇到了什么问题？

CyberStrikeAI 的项目管理，从一开始就做对了一件事：**跨会话共享「事实黑板」**。

绑定项目后，Agent 会把目标域名、开放端口、认证特征、可利用点等认知，通过 `upsert_project_fact` 写入项目级存储；下一次开新对话，系统会自动注入「项目黑板索引」，Agent 不必从零开始。

但在这次更新之前，**人类操作者看到的，始终是一张表**——「事实黑板」页：Key、分类、摘要、关系列、Body 状态、置信度……一行一行往下排。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33sNKpbALY7zvDBiavwGzibfwk3oibMnUVaA5SZSFJzXZjHsIA9ceZ6kvKM9UXndHFpPGmcIA5xLvhPA6Vwrs1jxVZVzaPUoTdVaZQ/640?wx_fmt=png&from=appmsg)

这对「检索单条事实」很友好，却对渗透测试最核心的能力——**理解因果链与依赖关系**——几乎无能为力。

真实渗透从来不是：

```
发现 A
发现 B
发现 C
```

而是：

```
目标入口 → 信息泄露 → 认证绕过 → 后台上传 → RCE → 内网横移
```

列表能告诉你「有什么」，却很难回答：

* 这条 SQL 注入和那个文件上传，是不是同一条链上的前后步骤？
* 某个 exploit 依赖哪个 target/auth 前置条件？
* 哪些 finding 还是「待确认」的孤立点，尚未连入主路径？
* 换一个人接手项目，30 秒内能否建立全局图景？

**列表是存储友好的；攻击路径是认知友好的。** 这次更新，就是在两者之间补上了缺失的那一层。

---

## 二、新增了什么？「攻击路径」功能页

在项目管理详情中，Tab 栏新增 **「攻击路径」** 页（与「事实黑板」「关联对话」「关联漏洞」「设置」并列）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33sZzSialHicKgBsURZ4VL2ItWVtQ7YcKH1ib7tqJ3SjzbLbF0b0icM0pHG5u29mEtXc5V7Cgz9BnMCTxkLm5W4IV1qicXibgI3fyqjIc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33vRLyugXaleuJrNOh3yEKH2kAkzCias8ibmoYCN9Zdde03CVEmkP9Azb2nxIQK20W68G7Kic2bgUR1agopibvtM5lOfQkIMSic9U6BE/640?wx_fmt=png&from=appmsg)

### 2.1 与「事实黑板」的关系

| 维度 | 事实黑板（原有） | 攻击路径（新增） |
| --- | --- | --- |
| 呈现形式 | 表格列表 | 交互式有向图 |
| 适合场景 | 搜索、编辑、批量管理单条事实 | 理解结构、梳理链条、交接复盘 |
| 数据来源 | 同一份 `project_facts` + `project_fact_edges` | 同一份，视图不同 |
| 关系表达 | 「关系」列显示入/出边计数与文本 | 箭头、颜色、分层布局直观展示 |

**不是两套数据，而是同一套结构化事实的两种读法。** 你在表格里改一条 fact 的 `links`，图会跟着变；在图里「连边」，表里的关系列也会更新。

### 2.2 前端展示形态（人读）

攻击路径页基于 **Cytoscape + ELK** 渲染，核心设计如下：

**① 节点 = 事实，边 = 关系**

* 每个节点对应一条 `fact_key`（如 `target/primary_domain`、`finding/sqli-login`、`exploit/upload-rce`）。
* 每条有向边对应数据库中的一条关系：`source → target`，类型如 `discovered_on`、`leads_to`、`exploits` 等。
* **箭头方向与存储方向严格一致**（source → target），避免「看图理解」与「Agent 写入语义」打架。

**② 节点卡片按类型分色分层**

节点按语义类型渲染为 SVG 卡片（目标 / 发现 / 利用 / 攻击链 / POC / 认证 / 基础设施 / 漏洞等），ELK 分层布局默认遵循：

```
target → infra → finding → exploit
```

让人一眼看到：**从哪进来、在哪发现问题、怎么打进去**。

**③ 两种视图模式**

* **攻击路径**（默认）：只展示与攻击链相关的 fact 类别（target、finding、chain、exploit、poc 等），以及作为依赖目标的 auth/infra 节点；过滤掉 note 等噪声，聚焦「能打的路径」。
* **完整关系**：展示项目内全部 fact 及其边，适合架构梳理与全量审计。

**④ 置信度可视化**

* `confirmed` 边：实线，高不透明度。
* `tentative` 边：**虚线**，表示待确认假设——鼓励「先连边、后验证」，而不是等一切定论才记录。
* 可勾选「隐藏废弃」，与事实黑板保持一致。

**⑤ 交互能力**

* 点击节点：侧栏展示摘要、分类、置信度、关联边列表，可跳转「详情 / 编辑」。
* **连边模式**：点选源节点 → 点选目标节点 → 选择边类型，手动补关系（适合人工复盘、纠正 Agent 遗漏）。
* 搜索节点、居中、刷新、图例（discovered\_on / leads\_to / exploits / 待确认）。
* 底部统计：节点数、边数。

**⑥ 与对话攻击链的衔接**

对话内的「攻击链可视化」是会话级的、由工具执行历史推导的图；项目攻击路径是**跨会话、可编辑、可沉淀**的项目级图。支持将某次对话的攻击链 **「沉淀攻击链」** 到项目——自动创建/更新 fact 与关系边，再进入攻击路径页统一治理。

---

## 三、Agent 侧是什么形态？（机读）

对人友好是图；对 Agent 友好，则是 **结构化 fact + links**，以及在 system prompt 中自动注入的 **黑板索引 + 攻击路径速览**。

### 3.1 写入：`upsert_project_fact` + `links`

Agent 通过 MCP 工具 `upsert_project_fact` 写入事实。关键字段：

* **`fact_key`**：项目内唯一键，建议 `category/slug` 命名（如 `finding/sqli-login`）。
* **`summary`**：索引用一行，须含「什么 + 在哪 + 如何验证」，禁止空泛结论。
* **`body`**：完整可复现上下文（HTTP 原文、命令、响应现象、步骤），**不进索引**，需要时 `get_project_fact` 按需拉取——控制 token，又保证可复现。
* **`links`**：关系边数组，语义为 **`from` → 当前 fact**（即来源指向本条事实）。

示例（finding 连到 target）：

```
{
  "fact_key": "finding/sqli-login",
  "category": "finding",
  "summary": "登录框 id 参数存在布尔盲注，/login.php，sqlmap --technique=B 可验证",
  "body": "…完整请求响应与步骤…",
  "links": [
    { "from": "target/primary_domain", "type": "discovered_on", "confidence": "confirmed" }
  ]
}
```

**写入 finding / chain / exploit / poc 时，必须提供 `links`**——这是攻击路径图有「边」可画的前提。Agent 指令中明确：

* finding 至少 1 条 `from=target/*` + `type=discovered_on`
* 在 finding 上挂 exploit 用 `from=exploit/*` + `type=exploits`
* 更新时省略 `links` 保留已有边；传 `[]` 清空；传新数组则**替换**全部入边

### 3.2 支持的边类型（完整列表）

| 类型 | 含义（Agent 写入时的语义） |
| --- | --- |
| `discovered_on` | 在某目标/资产上发现 |
| `depends_on` | 复现前置依赖 |
| `leads_to` | 认知/步骤推进到下一步 |
| `enables` | 扩大攻击面 |
| `exploits` | 利用关系（如 exploit → finding） |
| `contains` | 资产包含关系 |
| `part_of` | 属于某链/组 |
| `supports` | 证据支撑 |

另有合成边 `links_vuln`：当 fact 关联 `related_vulnerability_id` 时，自动生成 fact → `vuln:<id>` 的边，打通「事实黑板」与「漏洞管理」。

### 3.3 读取：黑板索引里的「攻击路径（事实关系）」

对话绑定项目后，系统自动向 Agent 注入 **「项目黑板索引」** 块，包含：

1. **事实列表**（仅 key + category + summary + confidence + 行内关系边摘要）
2. **`### 攻击路径（事实关系）`** 速览段——列出 `source → target · type` 关系边（与图/库方向一致）
3. 页脚提示：详情必须 `get_project_fact`；写入时 links 用 `from` 声明来源

索引有 rune 预算（`fact_index_max_runes`），事实列表与攻击路径速览分区占用，避免上下文爆炸。Agent 不必一次加载全部 body，却能**先看见图的骨架**，再按需下钻。

### 3.4 行为约束：边渗透边记录

各 Agent（orchestrator、recon、penetration 等）共享同一节奏：

> 每确认一条新认知，**立即**`upsert_project_fact`；每验证一条漏洞，**立即**`record_vulnerability`；勿等会话结束批量写入。

原因很现实：多轮对话会触发 **上下文压缩 / 摘要**，晚写 = 丢细节。攻击路径图如果只有节点没有边，往往是「写 fact 了但没写 links」——所以 links 被设为 finding 类 fact 的硬约束。

### 3.5 与漏洞记录的分工

* **`record_vulnerability`**：可交付的正式 finding（标题、严重度、POC、修复建议）。
* **`upsert_project_fact`**：复现所需的**全部上下文**（失败尝试、绕过、会话 cookie、依赖关系）。

同一发现常常**各记一次**：漏洞管「报告」，事实管「复现与路径」。攻击路径图画的是后者之间的结构，并可经 `links_vuln` 指向前者。

---

## 四、为什么要这样做？设计背后的几条原则

### 4.1 渗透知识本质是图，不是表

BloodHound 用图讲 AD 攻击路径，ATT&CK 用矩阵讲战术技术——行业共识是：**关系与顺序和发现本身一样重要**。项目黑板如果只存 flat facts，Agent 和人类都容易陷入「点状记忆」，漏掉组合利用与横向逻辑。

把 links 提升为一等公民，并让前端默认提供路径视图，是在产品层面对这一共识的回应。

### 4.2 索引与正文分离：省 token，不省证据

黑板索引 deliberately **不含 body**，只给摘要 + 关系骨架；完整 POC 在 body，按需 `get_project_fact`。

这样 Agent 在长项目中仍能看见「攻击路径速览」，又不会被 megabyte 级 HTTP 原文撑爆 context——这是 **RAG 式渐进披露** 在渗透记忆里的变体。

### 4.3 单一事实源：图由结构化边生成，而非 LLM 现画

对话内的攻击链图，是从工具执行与 LLM 分析**推导**出来的；项目攻击路径图，是从 **`project_fact_edges` 表** 确定性构建的。

好处：

* 可审计：每条边有来源会话、类型、置信度。
* 可编辑：人可以在 UI 删边、连边，纠正 Agent。
* 可同步：Agent 写 links → 人看图；人改 links → 下次 Agent 读索引时看到同一结构。

避免「聊天里说得头头是道，项目里却一盘散沙」。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33sJcPU07aJo61MsicMia25Njcic33ETB1D5cuzciagJjuVHQ2k9Gbia0h13ce09lJgcVtkAnxvPUibOPxWnFiceOFK1uQjL6SHPzgcMLM/640?wx_fmt=png&from=appmsg)

### 4.4 待确认边（tentative）降低记录摩擦

渗透中大量关系先是假设：「这个 SSRF 可能打内网，还没验证」。若只允许 confirmed，Agent 和用户都会推迟写入，路径图长期稀疏。

**虚线 tentative 边** 表达「已纳入假设结构，尚未闭环」，推动「先结构化、再验证」，与「边渗透边记录」一致。

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33tl2oWQn53jPVpJ51nFIpx9iaUicUaIWjQpQYfpHGNtiaiajBVvczfjQtjUYMKYhRo6eVCsrjJ6ibANPgRhTiacrFDvf4vqggytPPUbw/640?wx_fmt=png&from=appmsg)

### 4.5 跨会话协作：把个人会话记忆变成团队项目记忆

项目攻击路径不绑定单次 conversation。新人绑定同一项目，打开攻击路径 Tab，看到的不是某次聊天的 scrollback，而是**团队累积的可视化战役地图**——这是 AI 原生渗透平台区别于「一次性 ChatGPT 对话」的关键。

---

## 五、带来的具体好处

**对安全工程师**

* 30 秒建立项目全局：目标、发现、利用是否成链，哪里还是孤岛。
* 写报告 / 汇报时，路径图即叙事骨架，减少漏写关键步骤。
* 手动连边、改置信度、废弃误报，与 Agent 协同而不是盲信。

**对 Agent**

* 索引中的关系边 + 攻击路径速览，提供**结构化先验**，减少重复扫描与重复提问。
* 编排指令强调「将低影响问题串联成高影响攻击路径」——有图可依，串联才有落点。
* `get_project_fact` 按需加载 body，支持长周期项目而不丢复现细节。

**对组织**

* 事实 + 边 + 置信度 + 来源会话，审计可追溯。
* 对话攻击链可沉淀到项目，会话级探索升级为资产级知识。
* 与漏洞管理通过 `related_vulnerability_id` / `links_vuln` 打通，事实—漏洞—路径三角闭环。

---

## 六、如何用起来？（建议工作流）

1. **建项目**，对话绑定项目。
2. Agent 渗透过程中自动（或你提示它）写入 target / finding / exploit，**finding 类务必带 links**。
3. 在「事实黑板」检查 summary、body 完整度（待补全 badge）。
4. 切换到 **「攻击路径」**，默认「攻击路径」视图，检查是否成链、是否有 tentative 虚线待验证。
5. 缺边时用「连边」或编辑 fact 的 links 文本（`type: source_fact_key` 每行一条）。
6. 某次对话已有攻击链时，使用 **「沉淀攻击链」** 批量导入，再在图中修剪、确认。
7. 需要看 auth/infra/note 全量关系时，切 **「完整关系」** 视图。

---

## 七、与「对话攻击链」的区别（易混点）

|  | 对话攻击链 | 项目攻击路径 |
| --- | --- | --- |
| 范围 | 单次会话 | 整个项目，跨会话 |
| 生成方式 | 分析工具执行历史 + LLM 构建 | fact + links 结构化存储 |
| 入口 | 聊天侧栏 / 模...