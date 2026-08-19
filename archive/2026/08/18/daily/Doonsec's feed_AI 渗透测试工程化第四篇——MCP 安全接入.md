---
title: AI 渗透测试工程化第四篇——MCP 安全接入
url: https://mp.weixin.qq.com/s/Q2mLrKpiYa09MPUGpsyREg
source: Doonsec's feed
date: 2026-08-18
fetch_date: 2026-08-19T02:55:00.758528
---

# AI 渗透测试工程化第四篇——MCP 安全接入

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/VIJdfjNCVs4wBulS8mgsEfcGxlicNXKFpsDKctMIQu7LOpD2VTcEgAah2sgicJ8fDF0JpYHKnqa2RvT41I4EbdRBjzhiaxs0wlRCq8sibIe7UA0/0?wx_fmt=jpeg)

# AI 渗透测试工程化第四篇——MCP 安全接入

孔方兄
孔方兄

知微守望

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![公众号封面：AI 渗透测试工程化第四篇——MCP 安全接入](https://mmbiz.qpic.cn/sz_mmbiz_png/VIJdfjNCVs6e19u4OYIzaZ18rApiajF2XAanjI7MIUM6o0nLDvR8Jfl3EYBZYibC5Aa5SHc4WThAqpgUFfPzxmtxhPiaFYmib1ARdQI4HS3Fvyw/640?wx_fmt=png&from=appmsg)
> 接通工具只是第一步。真正的生产化，是把身份、权限、项目 Scope、审批状态、证据标准和审计记录绑定到每一次调用上。

前三篇，我们依次完成了三层能力建设：

1. 用 **Skills** 固化高级渗透测试工程师的工作方法与安全边界；
2. 把 Skill 写成可触发、可执行、可审计的能力包；
3. 把历史 PoC 整理成可检索、可校验、带安全等级的 YAML 规则库。

到了第四篇，系统已经具备“方法”和“知识”，接下来要解决的是连接问题：

> **怎样让 Agent 读取资产平台、查询扫描器、检索 PoC 规则库，并在需要时发起受控任务？**

很多团队会想到 MCP。

确实，MCP 可以把外部数据与工具以标准接口暴露给 Agent。但在安全场景中，最容易出现的误判也是：

> MCP Server 已经连通，工具能被模型调用，所以系统可以上线了。

这中间还差得很远。

一个能执行 `scan.create`、`validation.execute` 或 `report.export` 的 MCP Server，本质上已经进入企业生产权限边界。工具描述写错、Token 范围过大、审批只弹一个“是否允许”、后端返回内容夹带恶意指令，都会让一次看似正常的 Agent 调用演变成越权扫描、敏感信息外发，甚至跨系统权限升级。

所以这一篇不讲“如何跑通一个 Hello World MCP Server”，而是从生产安全架构出发，讲清楚：

* 资产、扫描器和 PoC 库应该怎样拆分；
* MCP Tool 的契约应该包含哪些内容；
* 如何实现工具级最小权限；
* 怎样绑定用户、项目、资产与授权窗口；
* 哪些动作必须进入人工审批；
* 如何防御工具投毒、结果注入和混淆代理；
* 怎样让每次调用留下完整证据链。

---

## 先给结论：MCP 接通了，不等于安全能力上线了

![图1：MCP 接通与生产安全上线的区别](https://mmbiz.qpic.cn/sz_mmbiz_png/VIJdfjNCVs5VNFsPav288FD16E2b6bOrBKu20V2BlwaPGRTsjsoBpf5trQMvVibTpbUzJ2oq1BYGn7lcPjR9TNtmFPybz3C4aPWibCBTicR2Os/640?wx_fmt=png&from=appmsg)

图1：MCP 接通与生产安全上线的区别

MCP 解决的是**标准化连接**问题，不会自动替你解决所有安全问题。

按照 MCP 2026-07-28 规范，MCP 为 LLM 应用与外部数据、工具提供统一协议，支持 Resources、Prompts 和 Tools 等能力；与此同时，官方规范也明确指出，MCP 会带来数据访问和代码执行路径，实施方必须建设用户同意、访问控制、数据保护和工具安全机制。MCP 2026-07-28 规范

从工程角度看，可以把成熟度分成四层：

| 层级 | 能力 | 典型表现 |
| --- | --- | --- |
| L1 连通 | Agent 能发现 MCP Server | 可以列出工具和资源 |
| L2 可调用 | 参数可以传入并返回结果 | 演示环境能够跑通 |
| L3 可控制 | 身份、Scope、审批与限流生效 | 越权调用被服务器拒绝 |
| L4 可审计 | 决策、执行、证据和版本可回溯 | 能回答谁在何时为何调用了什么 |

多数演示停留在 L1 或 L2，而企业生产至少要达到 L3 和 L4。

因此，本文所说的生产级 MCP，不只是一个协议适配器，而是：

```
标准协议接口
+ 权限代理
+ 策略执行点
+ 审批门禁
+ 证据与审计边界
```

---

## 先理解最新版 MCP 的几个关键变化

截至本文写作时，最新正式版本为 **MCP 2026-07-28**。这一版本将核心协议调整为无状态、自描述请求，并强化了路由、缓存、授权和扩展机制。2026-07-28 版本说明

对于安全工程师，最值得关注的是以下变化。

### 1. 请求从“依赖会话”转向“每次自描述”

新版核心不再依赖旧式初始化会话，每个请求都携带协议版本、客户端身份与能力信息。

这意味着安全网关不应假设“连接建立时验证过一次，后面都可信”，而应该对**每个请求**重新执行：

* 身份认证；
* Token 受众校验；
* 工具权限判断；
* 项目与资产 Scope 判断；
* 限流、审批和审计策略。

无状态不等于无上下文，而是要求上下文必须能够被明确携带、校验和重建。

### 2. 网关可以更清楚地识别调用对象

新版请求可以在 HTTP 头中携带 MCP 方法和工具名称，便于网关基于方法、工具和部分非敏感参数进行路由、限流和授权。

但不要把密码、Token、个人信息或敏感业务数据映射到可被中间设备记录的请求头。官方工具规范也明确提醒，敏感参数不应通过 `x-mcp-header` 暴露给网络中间层。MCP Tools 规范

### 3. 工具输入输出可以使用完整 Schema

MCP Tool 可以定义 `inputSchema` 和 `outputSchema`。输入 Schema 用于限制参数，输出 Schema 用于验证结构化结果。

这对安全系统十分重要：模型不能自由拼接任意参数，服务器也不能随意返回一段无法校验的自然语言，再由模型猜测执行状态。

### 4. 工具目录可以按授权动态收敛

服务器返回的工具集合可以根据当前请求携带的授权信息变化。例如，只拥有查询权限的用户，只能看到 `asset.search` 和 `finding.query`，不应该看到 `scan.create` 或 `validation.execute`。

这比“所有人看到全部工具，调用时再报 403”更符合最小暴露原则。

---

## Resources、Prompts、Tools，不要混着设计

MCP 服务器可以提供三类主要能力：

| 能力 | 主要用途 | 安全场景中的建议 |
| --- | --- | --- |
| Resources | 提供上下文和数据 | 资产快照、规则说明、报告模板、只读证据 |
| Prompts | 提供用户选择的模板化工作流 | 复测模板、报告框架、研判提纲 |
| Tools | 执行查询、计算或外部系统动作 | 搜索资产、创建扫描任务、导出报告 |

官方规范将 Resources 定位为应用驱动的上下文数据，将 Tools 定位为可由模型发现和调用的功能。MCP Resources｜MCP Tools

设计时可以遵循一个简单原则：

> **能用只读 Resource 解决的，不要包装成高权限 Tool；能拆成查询和执行两步的，不要做成一个万能 Tool。**

例如：

* 读取某条 PoC 的元数据，可以是 Resource 或只读查询工具；
* 建立 PoC 候选列表，可以是 `poc.match`；
* 执行主动验证，则必须是单独的 `validation.execute`，并设置更高权限与审批门槛。

如果把“匹配规则、选择目标、执行验证、导出证据”全部封装在一个 `run_poc` 工具里，服务器就失去了对各阶段分别授权和审计的能力。

---

## 不要建设“万能 MCP Server”

![图2：资产平台、扫描器与 PoC 规则库的安全隔离架构](https://mmbiz.qpic.cn/sz_mmbiz_png/VIJdfjNCVs6MXuSUl6EP4T8jSKI7TKDuibEcbY68BrQILOfF6Ubl9u170NwB3mEZuFzVxT2KyhSquCCO2qdIdMxpOdrfibzl6dGVWJuGRicjia4/640?wx_fmt=png&from=appmsg)

图2：资产平台、扫描器与 PoC 规则库的安全隔离架构

安全平台常见的错误架构，是建设一个 `security-mcp-server`，同时持有 CMDB、漏洞扫描器、工单系统、PoC 库、报告平台和凭据系统的高权限账号。

这样做虽然接入快，但会形成权限聚合点：

* 任意一个工具实现存在漏洞，都可能影响全部后端；
* 工具描述或返回结果被污染，可能诱导 Agent 跨系统调用；
* 一个宽权限 Token 被窃取，影响面横跨多个业务域；
* 很难对某一类动作单独限流、停用或回滚。

更合理的做法是按**数据域和风险域**拆分。

### 资产平台 MCP

只提供当前授权范围需要的资产能力：

```
asset.search
asset.get_snapshot
asset.get_service_facts
```

默认只读，返回脱敏摘要，并保留数据来源和采集时间。

### 扫描器 MCP

将查询和创建任务拆开：

```
finding.query
scan.profile.list
scan.create
scan.status
scan.cancel
```

其中 `finding.query` 可以是只读能力，`scan.create` 则必须校验项目、目标、扫描模板、并发、速率和授权窗口。

### PoC 规则库 MCP

默认只暴露规则元数据，不直接获得执行权限：

```
poc.search
poc.get_metadata
poc.validate_schema
poc.get_evidence_requirements
```

真正的验证执行应由独立执行器负责，并根据上一篇定义的 S0—S3 安全等级进入不同门禁。

### 报告与证据服务

如果涉及证据查询和报告导出，最好再次拆分：

```
evidence.get_redacted
report.preview
report.export
```

导出能力需要独立的数据外发策略，不应与普通查询共享权限。

拆分以后，Agent 不直接持有后端长期高权限凭据，只向相应 MCP Server 提交受约束意图。后端凭据留在服务端，由服务端依据当前身份和请求策略完成最小范围操作。

---

## 一个生产级 MCP Tool，至少要定义八件事

![图3：生产级 MCP Tool 的八项契约](https://mmbiz.qpic.cn/mmbiz_png/VIJdfjNCVs5yzV5ZX3UFxp5Kpr6qeddwnqOSFpKdfWopiahHeDCM3o1LPCibia2G5bslib1kdS6iblruZVibPIJPe5icEcQfia5nXFcE1zwiacvSDODg/640?wx_fmt=png&from=appmsg)

图3：生产级 MCP Tool 的八项契约

### 1. 单一职责

工具名称要表达清晰动作，例如：

```
asset.search
finding.query
poc.match
scan.create
validation.request
report.export
```

不推荐：

```
security.execute
do_everything
run_command
auto_pentest
```

一个 Tool 做的事情越多，权限就越难拆分，审批页面也越难让用户理解。

### 2. 严格输入 Schema

输入 Schema 至少要约束：

* 必填字段；
* 类型与枚举；
* 字符串长度；
* 数组数量；
* 格式与模式；
* 是否允许未知字段；
* 互斥和依赖关系。

安全工具通常应该设置：

```
"additionalProperties":false
```

避免模型额外传入服务器没有预期的字段。

### 3. 结构化输出契约

输出不能只有一句：

```
扫描已完成，发现 3 个高危漏洞。
```

应该返回可以验证的结构化结果：

```
{
"status":"completed",
"decision":"candidate_only",
"task_id":"task-placeholder",
"finding_count":3,
"evidence_refs":["evidence://placeholder/001"],
"warnings":[],
"policy":{
"decision_id":"policy-placeholder",
"rule_version":"2.1.0"
}
}
```

服务器必须按 `outputSchema` 生成结果，客户端也应再次验证。输出不符合 Schema 时，不应交给模型继续推理，更不能自动触发下一个高风险工具。

### 4. 授权上下文

每次调用至少需要绑定：

```
用户或工作负载身份
组织 / 租户
项目编号 engagement_id
授权资产范围
测试时间窗口
允许动作集合
审批或策略决策引用
```

其中身份与权限应来自可信认证上下文，而不是让模型在普通参数中声明“我是管理员”。

### 5. 风险级别

工具要明确属于：

* 只读查询；
* 受控写入；
* 数据导出；
* 主动验证；
* 高风险或不可逆操作。

风险级别决定是否允许自动调用、是否需要二次认证、是否需要人工审批，以及能否在生产环境执行。

### 6. 执行约束

至少包括：

* 幂等键；
* 请求超时；
* 总执行时限；
* 并发和速率；
* 重试上限；
* 取消能力；
* 结果保留时间。

特别是 `scan.create` 这类工具，如果没有幂等键，模型重试可能创建多个重复任务。

### 7. 审批策略

审批不是简单的布尔字段，而是绑定具体动作的一次性授权。

它应包含目标摘要、动作、风险、影响、参数哈希、有效期和审批人。只要调用参数变化，原审批就应失效。

### 8. 审计与证据

Tool 必须定义哪些信息进入审计：

* 调用链 `trace_id`；
* 用户、租户和项目；
* MCP Server 与 Tool 版本；
* 输入参数的脱敏摘要与哈希；
* 策略判断和审批引用；
* 执行状态、耗时、重试与错误；
* 输出结构哈希与证据索引。

---

## 安全工具示例：不要让模型直接传目标地址

下面以 `scan.create` 为例展示一种更安全的设计思路。示例只体现契约和权限边界，不包含任何攻击载荷。

```
{
"name":"scan.create",
"title":"创建授权范围内的受限扫描任务",
"description":"根据已批准的项目、资产引用和扫描配置创建受限任务。不得接收任意目标地址。",
"inputSchema":{
"$schema":"https://json-schema.org/draft/2020-12/schema",
"type":"object",
"required":[
"engagement_id",
"asset_refs",
"profile_id",
"idempotency_key"
],
"properties":{
"engagement_id":{
"type":"string",
"pattern":"^PT-[0-9]{4}-[0-9]{4}$"
},
"asset_refs":{
"type":"array",
"minItems":1,
"maxItems":20,
"uniqueItems":true,
"items":{
"type":"string",
"pattern":"^asset-[a-z0-9-]+$"
}
},
"profile_id":{
"enum":["safe-web-baseline","safe-service-baseline"]
},
"idempotency_key":{
"type":"string",
"minLength":16,
"maxLength":64
}
},
"additionalProperties":false
},
"outputSchema":{
"type":"object",
"required":["status","task_id","scope_snapshot","policy_decision"],
"properties":{
"status":{
"enum":["queued","denied","input_required"]
},
"task_id":{"type":["string","null"]},
"scope_snapshot":{"type":"string"},
"policy_decision":{"type":"string"}
},
"additionalProperties":false
}
}
```

这里没有让模型提交 `target_url`、`cidr` 或任意扫描参数，而是提交：

* 经过资产平台解析的 `asset_refs`；
* 经过安全团队审核的 `profile_id`；
* 用于防止重复创建的 `idempotency_key`。

服务器收到请求后，还必须再次完成：

1. 根据 `engagement_id` 获取授权快照；
2. 将 `asset_refs` 解析为服务器端资产记录；
3. 校验每项资产属于当前项目；
4. 确认当前时间位于授权窗口；
5. 检查扫描配置、速率和并发；
6. 根据风险策略判断是否需要审批；
7. 创建任务并写入审计链。

**模型提交的是意图，不是最终执行命令。**

---

## 最小权限要做到“按工具授权”

![图4：MCP Tool 最小权限矩阵](https://mmbiz.qpic.cn/sz_mmbiz_png/VIJdfjNCVs6vQp2kKGp6icaWBMBkaibC4iccgrwic4T6GXkmCj2IRFpBQRTPVsJ90HzGpUjHNn...