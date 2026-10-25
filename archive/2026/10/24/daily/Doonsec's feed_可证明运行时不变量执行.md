---
title: 可证明运行时不变量执行
url: https://mp.weixin.qq.com/s/j5lWYMEMX_YuM3E2W4P3AQ
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:05:47.662629
---

# 可证明运行时不变量执行

# 可证明运行时不变量执行

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

1. 引言：经验护栏的局限
2. 形式化框架
3. 安全不变量规约语言
4. 迁移系统建模与模型检测
5. 抽象解释与 LLM 行为近似
6. 运行时验证混合方法
7. 基于类型系统的安全
8. 不变量完备性与覆盖度量
9. 评估框架
10. 前沿挑战
11. 参考文献

---

## 1. 引言：经验护栏的局限

当前 Agent 安全护栏主要采用经验性方法：prompt-based guardrails、output filtering、action blacklists。这些方法存在根本局限：

| 局限 | 表现 | 后果 |
| --- | --- | --- |
| 不完备 | 无法枚举所有危险动作 | 遗漏攻击面 |
| 不可组合 | 多个护栏的交互未经验证 | 组合漏洞 |
| 不可验证 | 无法证明"某事永不发生" | 安全信心不足 |
| 可绕过 | prompt injection 可操纵护栏 | 护栏本身成为攻击面 |

**核心问题**：能否为 Agent 运行时定义一组安全不变量，并给出其执行的数学证明？

**本文方法**：采用**形式化验证 + 运行时验证**的混合策略——形式化部分提供证明，运行时部分覆盖形式化无法覆盖的行为。

---

## 2. 形式化框架

### 2.1 Agent 运行时作为迁移系统

**定义 2.1（Agent 运行时迁移系统）**：Agent 运行时建模为迁移系统 ：

* ：状态空间（环境状态 + Agent 内部状态 + 记忆）
* ：动作空间（工具调用、文件操作、网络请求等）
* ：迁移关系
* ：初始状态

**执行轨迹**：

### 2.2 安全不变量

**定义 2.2（安全不变量）**：安全不变量  是一个在所有可达状态上必须成立的性质：

**典型 Agent 安全不变量**：

| 不变量 | 时态逻辑表达 | 含义 |
| --- | --- | --- |
| 路径限制 |  | 永不写入未授权路径 |
| 域限制 |  | 永不向未授权域发请求 |
| 权限限制 |  | 永不执行未授权命令 |
| 数据流 |  | 永不泄露秘密 |
| 资源限制 |  | 永不超资源限制 |
| 终止性 |  | 最终终止 |

### 2.3 证明义务

**证明义务**：对于每个安全不变量 ，证明：

即迁移系统  满足不变量 。

**挑战**：LLM 推理层使  的迁移关系  不可完全形式化——LLM 的输出是概率性的且内部计算不可符号化。

**解决方案**：分层验证——将  分解为可形式化层（动作执行、权限检查）与不可形式化层（LLM 推理），对可形式化层给出证明，对不可形式化层给出运行时验证。

---

## 3. 安全不变量规约语言

### 3.1 SIL 语言设计

**Safety Invariant Language (SIL)** 是面向 Agent 安全的规约语言：

```
// 路径访问不变量
invariant PathRestriction {
    forall action a:
        if a.type == "file_write"
        then a.path in AllowedWritePaths
}

// 网络域不变量
invariant NetworkRestriction {
    forall action a:
        if a.type == "http_request"
        then a.domain in AllowedDomains
}

// 数据流不变量（信息流控制）
invariant NoSecretLeak {
    forall state s:
        if s.contains(SecretData)
        then not s.output.contains(SecretData)
}

// 时态不变量：危险操作前需人类确认
invariant HumanInLoop {
    forall trace t:
        if t.last_action in DangerousActions
        then exists step s in t: s.type == "human_approval"
}

// 资源限制不变量
invariant ResourceLimit {
    forall state s:
        s.memory < MAX_MEMORY and s.cpu < MAX_CPU
}

// 组合不变量：数据外发需加密
invariant EncryptedEgress {
    forall action a:
        if a.type == "http_request" and a.body.contains(SensitiveData)
        then a.body.is_encrypted
}
```

### 3.2 时态逻辑表达

SIL 不变量翻译为 LTL/CTL 公式：

| SIL 构造 | LTL 翻译 |
| --- | --- |
| `forall action a: P(a)` |  |
| `if A then B` |  |
| `exists step s: Q(s)` |  |
| `before A, B` |  |
| `eventually A` |  |
| `always A` |  |

**示例翻译**：

```
invariant HumanInLoop {
    forall trace t:
        if t.last_action in DangerousActions
        then exists step s in t: s.type == "human_approval"
}
```

翻译为 LTL：

---

## 4. 迁移系统建模与模型检测

### 4.1 Agent 运行时的形式化建模

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