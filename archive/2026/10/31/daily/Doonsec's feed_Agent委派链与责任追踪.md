---
title: Agent委派链与责任追踪
url: https://mp.weixin.qq.com/s/BUYKG7ioUEAsbVRAnQKyOg
source: Doonsec's feed
date: 2026-10-31
fetch_date: 2026-11-01T08:18:24.004847
---

# Agent委派链与责任追踪

# Agent委派链与责任追踪

原创

pandazhengzheng
pandazhengzheng

安全分析与研究

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 目录

1. 引言：Agent 委派的责任黑洞
2. 委派链的形式化模型
3. 能力令牌与委派令牌设计
4. 委派图与责任路径算法
5. 权限衰减与深度限制
6. 密码学完整性：签名链与可验证凭证
7. 动态子 Agent 的即时身份签发
8. 跨组织委派的信任建立
9. 委派链中的攻陷与隔离
10. 工程实现：委派引擎架构
11. 审计与责任归因系统
12. 评估框架与实验
13. 前沿挑战与开放问题
14. 参考文献

---

## 1. 引言：Agent 委派的责任黑洞

### 1.1 问题的本质

传统 IAM（身份与访问管理）的委派模型相对简单：

```
User → Application → Database
```

委派深度有限（通常 1-2 跳），且每个节点都是人类管理的静态实体。

但 Agent 系统的委派链完全不同：

```
User A
  → Agent B (用户 A 的个人助手)
    → Agent C (Agent B 动态创建的子 Agent)
      → Agent D (Agent C 调用的云服务 Agent)
        → API E (企业 SaaS API)
          → Database F (敏感数据)
```

这条链有 5 跳，且包含**动态生成的子 Agent**。当 API E 被调用并访问 Database F 中的敏感数据时：

* **谁授权了这次访问？** → 沿委派链回溯到 User A
* **谁应对过度授权负责？** → 可能是 Agent B（签发了过宽委派）或 Agent C（请求了过宽权限）
* **如果 Agent D 被攻陷呢？** → 责任如何分割？
* **如何防止权限在委派中放大？** → 每跳权限应 ⊆ 上跳权限

### 1.2 当前系统的缺陷

| 缺陷 | 后果 |
| --- | --- |
| Agent 使用共享服务账号 | 无法区分哪个 Agent 执行了操作 |
| 委派深度无限制 | 权限可无限传递，难以追踪 |
| 委派无密码学签名 | 委派链可被篡改或伪造 |
| 动态子 Agent 无身份 | 动态创建的 Agent 无法追责 |
| 跨组织委派无信任机制 | Agent 无法安全跨域操作 |
| 委派链无权限衰减检查 | 权限可能在委派中放大 |

### 1.3 本文贡献

本文提出**可验证委派链框架（VDCF）**，核心贡献包括：

1. **委派链形式化模型**：基于能力安全理论的委派链形式化，支持任意深度
2. **委派令牌设计**：每跳签发包含签发者、主体、范围、过期、证明的可验证令牌
3. **委派图与责任路径算法**：构建委派图并支持图上责任路径查询与归因
4. **权限衰减保证**：形式化并强制执行每跳权限 ⊆ 上跳权限
5. **密码学完整性**：基于 SPKI/SDSI 扩展的非人类身份签名链
6. **动态身份签发**：动态生成子 Agent 的即时身份签发与吊销
7. **跨组织信任**：基于可验证凭证的跨域委派信任建立

---

## 2. 委派链的形式化模型

### 2.1 基本定义

**定义（实体）**：系统中的实体集合 `E = H ∪ A ∪ S`，其中：

* `H`：人类用户集合
* `A`：Agent 集合（包括静态 Agent 与动态生成的子 Agent）
* `S`：服务/API 集合

**定义（能力）**：能力 `c = (resource, action, constraints)`，其中：

* `resource`：目标资源标识
* `action`：允许的操作（read/write/exec/...）
* `constraints`：附加约束（时间、条件、参数限制等）

**定义（能力集合）**：`C = {c₁, c₂, ..., cₙ}`，能力的集合。

**定义（委派）**：委派 `d = (issuer, subject, capabilities, conditions, proof)`，其中：

* `issuer ∈ E`：委派方
* `subject ∈ E`：被委派方
* `capabilities ⊆ C`：委派的能力集合
* `conditions`：委派条件（过期时间、使用次数、上下文限制等）
* `proof`：委派的密码学证明（签名）

### 2.2 委派链

**定义（委派链）**：委派链 `χ = (d₁, d₂, ..., dₖ)` 是委派的序列，满足：

```
∀ i ∈ [1, k-1]: dᵢ.subject = dᵢ₊₁.issuer
```

即每条委派的被委派方是下一条委派的委派方。

**委派链的起点**：`d₁.issuer ∈ H`（委派链必须始于人类用户）。

**委派链的终点**：`dₖ.subject` 执行实际操作。

### 2.3 权限衰减公理

**公理（权限衰减）**：对于合法委派链 `χ = (d₁, d₂, ..., dₖ)`：

```
∀ i ∈ [2, k]: dᵢ.capabilities ⊆ dᵢ₋₁.capabilities
```

即每跳委派的能力集合是上跳的子集。这保证了权限在委派中不会放大。

**推论**：`dₖ.capabilities ⊆ d₁.capabilities`，最终执行操作的能力是初始委派能力的子集。

### 2.4 责任归因

**定义（责任归因）**：对于委派链 `χ` 导致的操作 `op`：

```
Accountability(χ, op) = {
    originator: d₁.issuer,          # 原始委托者（人类）
    delegators: [d₁.issuer, ..., dₖ₋₁.issuer],  # 各级委派方
    executor: dₖ.subject,           # 实际执行者
    over_delegator: argmax_{dᵢ} (|dᵢ.capabilities| - |dᵢ₊₁.capabilities|),  # 过度委派方
    capability_used: op.required_capability,
    capability_source: dⱼ where op.required_capability ∈ dⱼ.capabilities,
}
```

---

## 3. 能力令牌与委派令牌设计

### 3.1 能力令牌（Capability Token）

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

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