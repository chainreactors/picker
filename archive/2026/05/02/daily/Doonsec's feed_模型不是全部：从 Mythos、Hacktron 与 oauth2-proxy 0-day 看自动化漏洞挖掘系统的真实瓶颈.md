---
title: 模型不是全部：从 Mythos、Hacktron 与 oauth2-proxy 0-day 看自动化漏洞挖掘系统的真实瓶颈
url: https://mp.weixin.qq.com/s/_e332pf-qS04KPhu0O7Mcg
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:27:58.283966
---

# 模型不是全部：从 Mythos、Hacktron 与 oauth2-proxy 0-day 看自动化漏洞挖掘系统的真实瓶颈

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/VRdT0HGxjvAh7THgH4n18P3nRsz49bt3iaOXfyHoTtmibMANZiblwWVwVFSYqiaCD1ibwFRH3CO6X4ymbVDIeOVoRNeUu1BbWsCBJZx46h6dORz8/0?wx_fmt=jpeg)

# 模型不是全部：从 Mythos、Hacktron 与 oauth2-proxy 0-day 看自动化漏洞挖掘系统的真实瓶颈

做安全的小明同学
做安全的小明同学

大山子雪人

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 模型不是全部：从 Mythos、Hacktron 与 oauth2-proxy 0-day 看自动化漏洞挖掘系统的真实瓶颈

> 副标题：Hacktron《Why Mythos Doesn't Matter (for us)》深度对比学习笔记
> 核心主题：Mythos / Claude / Hacktron / oauth2-proxy / 上下文工程 / 成本-召回率 / 验证闭环 / 漏洞挖掘 Agent 架构
> 文档类型：多源合并、深度对比、架构学习
> 更新时间：2026-05-02

---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VRdT0HGxjvDuGfBibyJVBNSSzCQvEUsiaWX95IN91Lkn47iaMPTUGda77KBeQLlR0RiazWfPibrvYOPfLclSvcU83mxWUjMgWMw7yhafiaynxs9PE/640?wx_fmt=png&from=appmsg)

## 0. 阅读目标

这份文档不是对 Hacktron 原文做简单转载，也不是逐条摘录参考链接，而是把 Hacktron 原文及其引用资料合并为一套可学习、可复用的安全研究框架。

它重点回答四个问题：

1. 1. **Mythos / Claude 这类 frontier model 在漏洞发现中到底证明了什么？**
2. 2. **Hacktron 为什么认为“对它们而言 Mythos 不重要”？**
3. 3. **oauth2-proxy 两个认证绕过漏洞说明了什么样的上下文工程问题？**
4. 4. **对 OpenClaw 这类漏洞挖掘 Agent 来说，应该如何把这些材料转化为系统设计？**

一句话总结：

> 这些材料共同说明，未来的漏洞挖掘能力不只来自更强模型，而来自“模型能力 + 上下文构建 + 搜索覆盖 + 成本控制 + 证据验证 + 人类经验约束”的系统组合。

---

## 1. 资料来源总览

| 编号 | 来源 | 主题 | 在本文中的作用 |
| --- | --- | --- | --- |
| S0 | Hacktron, Why Mythos doesn't matter (for us) | 小模型多次运行、成本-召回率、Hacktron workflow、oauth2-proxy benchmark | 主线材料 |
| S1 | Mozilla Security Blog, The zero-days are numbered | Mythos Preview 在 Firefox 150 中发现 271 个漏洞 | Frontier model 能力上限案例 |
| S2 | LinkedIn, oauth2-proxy 0-days post | Hacktron Review / oauth2-proxy 0-day 对外叙事 | 产品化与 PR review 场景 |
| S3 | Trail of Bits, Audit context-building skill | 审计任务中的上下文构建方法 | 人类经验转为 Agent skill 的例子 |
| S4 | Anthropic Claude Code Review docs | 多 Agent PR review、验证、去重、分级 | 工程化代码审查参考 |
| S5 | oauth2-proxy v7.15.0 source | benchmark 目标版本 | 漏洞 ground truth 对照基础 |
| S6 | GitHub Advisory GHSA-5hvv-m4w4-gf6v | Health Check User-Agent auth bypass | Finding A 事实依据 |
| S7 | GitHub Advisory GHSA-7x63-xv5r-3p2x | X-Forwarded-Uri spoofing auth bypass | Finding B 事实依据 |
| S8 | Wikipedia, Precision and Recall | precision / recall 定义 | 评价指标基础 |
| S9 | OpenRouter AI Model Rankings | 模型使用、榜单与成本选择参考 | 模型选择背景 |
| S10 | oauth2-proxy README | OAuth2 Proxy 项目定位和部署模式 | 上下文语义来源 |
| S11 | Anthropic, Mozilla and Firefox security | Claude Opus 4.6 与 Firefox 安全合作 | Mythos 前序案例 |

---

## 2. 事件时间线

| 时间 | 事件 | 关键含义 |
| --- | --- | --- |
| 2026-03-06 | Anthropic 发布 Mozilla / Firefox 合作文章，称 Claude Opus 4.6 两周内发现 22 个 Firefox 漏洞，其中 14 个被 Mozilla 评为 high severity | 证明 frontier model 已经能在复杂浏览器代码库中发现高价值漏洞 |
| 2026-04-14 | oauth2-proxy 发布 v7.15.2，修复多个安全问题，包括两个 critical 认证绕过 | Hacktron benchmark 的两个 ground truth 漏洞进入公开 advisory |
| 2026-04-21 | Mozilla 发布 The zero-days are numbered，称 Firefox 150 包含 271 个 Mythos Preview 初始评估发现的漏洞修复 | Mythos 进一步提升了 AI-assisted vulnerability discovery 的规模感 |
| 2026-04-29 | Hacktron 发布 Why Mythos doesn't matter (for us) | 从产品化、无人值守、成本-召回率角度重新定义模型选择问题 |

---

## 3. 三条主线：Mozilla / Anthropic / Hacktron

### 3.1 Mozilla 主线：AI 让防守方有机会系统性清空历史漏洞库存

Mozilla 文章的核心叙事是：Firefox 团队自 2026 年 2 月起使用 frontier AI models 查找并修复浏览器中的潜在安全漏洞。Mozilla 表示，Firefox 150 中包含 271 个由 Claude Mythos Preview 初始评估发现的漏洞修复；在更早的合作中，Opus 4.6 对 Firefox 148 的扫描促成了 22 个 security-sensitive bugs 的修复。

Mozilla 的重要观点包括：

* • 传统安全长期处于攻防拉锯状态。
* • 攻击者只需要找到一个薄弱点，而防守者需要覆盖大量攻击面。
* • fuzzing 很有效，但覆盖不均衡。
* • 顶级安全研究员能通过源码推理找到 fuzzing 难以覆盖的问题，但这种能力稀缺且昂贵。
* • frontier AI models 开始具备接近 elite human researcher 的源码推理能力。
* • Mozilla 没有看到“人类顶级研究员能发现而模型不能发现”的漏洞类别或复杂度。

这里的学习重点不是“AI 无所不能”，而是：

> 当模型足够强，并且目标代码库、维护团队、修复流程和验证能力都具备时，AI 可以显著压缩漏洞发现时间。

### 3.2 Anthropic 主线：从历史 CVE 复现到真实复杂代码库发现

Anthropic 的 Firefox 安全合作文章强调了几个事实：

* • Claude Opus 4.6 在两周内发现 22 个 Firefox 漏洞。
* • Mozilla 将其中 14 个评为 high severity。
* • Firefox 被选作目标，是因为它是复杂、经过长期测试、用户规模巨大的开源软件。
* • Anthropic 先用历史 Firefox CVE 构建评测集，测试模型是否能复现既有漏洞，再进入真实未知漏洞发现。
* • Mozilla 在合作中帮助判断哪些 findings 值得提交 bug report，并最终修复问题。

这条主线说明：

> 高质量 AI 漏洞研究不是“模型直接输出漏洞”这么简单，而是包含历史 CVE benchmark、真实代码扫描、维护者 triage、漏洞报告、修复发布等完整协作流程。

### 3.3 Hacktron 主线：无人值守商业化扫描的核心指标不是单次模型能力，而是 cost-to-signal

Hacktron 原文承认 frontier model 非常强，尤其是在 expert human operator 参与、目标明确、harness 设计良好、研究员能中途纠偏的场景中。

但 Hacktron 关注的是另一个场景：

* • 没有熟练 operator。
* • 没有人告诉 Agent 应该看哪里。
* • 没有人动态纠偏。
* • 需要面向大量普通代码库、PR 或 Web 应用持续运行。
* • 成本会随着规模迅速放大。

因此 Hacktron 提出：

> 对 99% 的应用而言，较小模型重复运行，在成本-召回率上可能比一次性运行 frontier model 更合理。

这个观点的本质不是否定大模型，而是把评价指标从“单次最强能力”切换为：

```
单位成本下发现真实漏洞的概率 × 单位时间可覆盖代码范围 × 后续验证成本 × 用户可接受的信号质量
```

---

## 4. 核心对比：三类漏洞挖掘模式

| 维度 | Mozilla / Mythos 模式 | Anthropic / Claude 安全合作模式 | Hacktron 自动扫描模式 |
| --- | --- | --- | --- |
| 目标 | 清理 Firefox 这类高复杂度代码库的潜在漏洞 | 证明 Claude 可在复杂真实软件中发现高危漏洞 | 面向多数应用、PR 和代码库持续发现 critical bugs |
| 人类角色 | 维护团队深度参与、修复和验证 | 研究团队 + Mozilla maintainer 协作 | 尽量 human-out-of-the-loop，只保留最小 triage |
| 模型侧重点 | frontier model 上限 | frontier model + 安全评测 | 成本可控模型 + 多次运行 + workflow 优化 |
| 目标代码复杂度 | 浏览器、C++、sandbox、legacy code | Firefox / open-source security benchmark | Web app、auth proxy、业务应用、PR changes |
| 成本敏感度 | 相对较低，安全收益极高 | 研究合作成本可接受 | 极高，商业化扫描必须控制单位成本 |
| 关键瓶颈 | 大规模发现后的修复和优先级管理 | 如何判断 findings 是否值得报告 | 如何提高 recall，同时控制 false positives 和 token cost |
| 适合场景 | 高价值核心软件、浏览器、内核、基础设施 | 研究验证、模型能力评估、重大开源项目合作 | SaaS 安全扫描、PR review、CI/CD、普通企业代码库 |

---

## 5. Hacktron 原文的关键论证链

Hacktron 的论证可以拆成 7 步：

```
1. Mythos / Claude 在 Firefox 等复杂目标中的成果是真实且重要的。
2. 但这些成果背后通常有熟练 operator 或高质量维护团队参与。
3. Hacktron 目标是无人值守、持续化、产品化漏洞扫描。
4. 在这种场景中，frontier model 的成本会快速放大。
5. LLM 漏洞发现本身具有非确定性，强模型也不是 100% 命中。
6. 如果小模型足够便宜，可以通过多次运行提升覆盖率和召回率。
7. 因此，对大多数应用而言，优化 workflow + 多次运行小模型，可能比依赖 Mythos 更有性价比。
```

这条论证的关键转折点在第 5 步：

> 只要大模型也不是确定性命中，那么“多次运行 + 多策略搜索”就具有工程价值。

---

## 6. oauth2-proxy benchmark：为什么这个案例很重要

Hacktron 使用 oauth2-proxy v7.15.0 作为 benchmark 目标，并用两个真实 0-day 作为 ground truth：

1. 1. **Finding A / CVE-2026-34457 / GHSA-5hvv-m4w4-gf6v**
   Health Check User-Agent Matching Bypasses Authentication in auth\_request Mode
2. 2. **Finding B / CVE-2026-40575 / GHSA-7x63-xv5r-3p2x**
   Authentication Bypass via X-Forwarded-Uri Header Spoofing

这个 benchmark 的价值在于：

* • 两个漏洞都不是简单语法 bug。
* • 都依赖部署配置。
* • 都发生在 OAuth2 Proxy 与反向代理 / 上游服务的信任边界处。
* • 都需要理解“认证代理组件在整体架构中的角色”。
* • 都是 security semantics bug，而不是单纯的内存安全 bug。

因此它特别适合作为漏洞挖掘 Agent 的测试目标：

> 它要求 Agent 不只是看代码，还要理解配置、部署模式、HTTP header 信任边界、auth\_request 语义和攻击者可控输入。

---

## 7. Finding A 深入学习：Health Check User-Agent 认证绕过

### 7.1 漏洞事实

GitHub Advisory 对 GHSA-5hvv-m4w4-gf6v 的描述是：OAuth2 Proxy 存在配置依赖型认证绕过。受影响条件包括：

* • OAuth2 Proxy 使用 `auth_request` 风格集成，例如 nginx `auth_request`。
* • 配置了 `--ping-user-agent`，或启用了 `--gcp-healthchecks`。

在受影响配置中，OAuth2 Proxy 会把带有特定 health check `User-Agent` 的请求当成成功健康检查，而不考虑请求路径。攻击者可以构造相同 `User-Agent`，使 OAuth2 Proxy 返回成功，从而在 `auth_request` 模式下绕过认证并访问受保护上游资源。

### 7.2 漏洞成立的语义链

这个漏洞不是看到 `User-Agent == GoogleHC/1.0` 就能得出结论。它需要下面的语义链：

```
攻击者可控请求
  ↓
攻击者设置 User-Agent 为健康检查 UA
  ↓
OAuth2 Proxy 在 health check 分支返回成功
  ↓
在 standalone reverse proxy 模式下，这可能只是健康检查行为
  ↓
但在 nginx auth_request / middleware 模式下，2xx/200 被上游反向代理解释为“认证通过”
  ↓
上游反向代理允许原始请求访问受保护资源
  ↓
形成认证绕过
```

### 7.3 为什么上下文决定能否发现

Hacktron 原文特别强调 Finding A：如果 prompt 中没有部署模式上下文，模型很容易把 health check 逻辑判断为 harmless dead end。因为在 standalone mode 下，健康检查返回成功并不一定构成漏洞。

只有当上下文中出现以下信息时，漏洞才容易被模型理解：

```
component_role:
  value:OAuth2Proxymayrunasmiddlewareinexistinginfrastructure
required_for_vulnerability:true

delegated_auth_semantics:
value:reverseproxymaytreat2xxresponsefromauth_requestasauthsuccess
required_for_vulnerability:true

attacker_control:
value:clientcaninfluenceUser-Agentunlessupstreamoverwritesit
required_for_vulnerability:true

configuration_condition:
value:
    ---ping-user-agentconfigured
    -or--gcp-healthchecksenabled
required_for_vulnerability:true

impact:
value:unauthenticatedaccesstoprotectedupstreamresources
required_for_vulnerability: true
```

### 7.4 对 Agent 的学习点

Finding A 说明：

> 漏洞发现 Agent 必须区分“代码局部行为”和“部署组合后的安全语义”。

如果 Agent 只分析函数局部，它可能看到的是：

```
健康检查返回 200，正常。
```

如果 Agent 能看到系统语义，它应该看到的是：

```
健康检查返回 200 被另一个组件当作认证成功信号，且攻击者...