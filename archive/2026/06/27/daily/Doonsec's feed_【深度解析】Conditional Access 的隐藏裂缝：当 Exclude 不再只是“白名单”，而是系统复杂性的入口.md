---
title: 【深度解析】Conditional Access 的隐藏裂缝：当 Exclude 不再只是“白名单”，而是系统复杂性的入口
url: https://mp.weixin.qq.com/s/Ohsm1LyTDyENx7DeBbxjhQ
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:10:35.379877
---

# 【深度解析】Conditional Access 的隐藏裂缝：当 Exclude 不再只是“白名单”，而是系统复杂性的入口

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Ft77EUEUqotcI5RicWbHdlPa63zia3pUbNMQyZftmNUHEuumGjsSVGU6XicE9XqliaYVsavtdYr6rAZ0hcdIsFljFG9NnsavNDFsJmnK2EkJmSY/0?wx_fmt=jpeg)

# 【深度解析】Conditional Access 的隐藏裂缝：当 Exclude 不再只是“白名单”，而是系统复杂性的入口

云梦DC
云梦DC

云梦安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 在 Entra ID 的安全体系里，Conditional Access（条件访问）一直被视为零信任落地的核心控制点。
> 但最近安全社区围绕“resource exclusion（资源排除）”展开的一系列讨论，让很多管理员开始重新审视一个问题：
> **我们以为的“例外”，真的只是例外吗？**

---

![](https://mmbiz.qpic.cn/mmbiz_png/Ft77EUEUqoshySmVBOdQwOhNibNkzO7rLlKRpQ45icnpboMQOIWJj3GSMyJniamqS6CcaphOT25B7uzFwicCPrAtA6oBiabibD2vD3hvibyny3cjHY/640?wx_fmt=png&from=appmsg)

在企业落地 Microsoft Entra ID 的过程中，条件访问策略几乎是标配能力：

* 强制 MFA
* 限制登录位置
* 控制设备合规性
* 统一访问策略

为了兼顾业务兼容性，一个非常常见的配置就是：

> **“All cloud apps + 排除某个业务应用”**

看起来很合理，但问题恰恰就出现在这里。

---

# 01 一个被长期忽视的现实：CA 并不是“单点决策引擎”

很多人默认认为：

> 只要命中了 CA policy，就一定统一执行 MFA 或阻断

但实际情况要复杂得多。

在 Microsoft Entra ID 内部，CA evaluation 是一个**多路径决策系统**：

* OIDC 登录路径
* OAuth token 颁发路径
* Resource token minting 路径
* First-party 应用特殊路径

这些路径在某些历史兼容场景下，并不是完全统一执行的。

---

# 02 复杂性来源：Graph token 是“第二条隐式路径”

在现代 SaaS 登录中，一个应用通常不会只请求一个资源：

* 登录本身（OIDC / openid）
* 用户基础信息（User.Read）
* 组织数据访问（Microsoft Graph）

而 Microsoft Graph API 在这里扮演了一个特殊角色：

> 它既是资源 API，也是几乎所有微软服务的“数据总入口”。

问题就在于：

> Graph token 的获取，往往发生在“主登录流程之外”。

---

# 03 真正的风险点：CA policy 评估上下文丢失

在“All apps + exclusion”配置下，问题不是简单的绕过，而是：

> **部分 Graph token 请求没有完整继承主 CA policy 上下文**

换句话说：

* 主登录流程是被 CA 控制的
* 但附带的 Graph token 请求可能进入不同评估路径

这会导致一种现象：

> 同一个登录会话中，不同 token 的策略执行结果可能不一致

---

# 04 public client 与 low-privilege scope 的特殊行为

![](https://mmbiz.qpic.cn/mmbiz_png/Ft77EUEUqos1U6FfkyT0bTBM3AWiaqzaqM4xeXEsiaW4bZUHttT3wYumZRviclD6qicXSBhHblnh6mw4E0MMibc4L2XCyWpu8RSj2bWiaIuZamia20/640?wx_fmt=png&from=appmsg)

#

在现实攻击面分析中，有一个关键因素经常被忽略：

### public client（公共客户端）

例如移动端或微软自家应用：

* 无 client secret
* 完全依赖用户交互登录
* 更依赖系统级 trust model

在某些 legacy 兼容逻辑中：

> low-privilege scope（如 openid、profile、User.Read）可能被视为“低风险访问”

这就引出了一个安全设计权衡：

> **为了避免业务中断，系统可能对低风险 Graph token 采用不同的 CA enforcement 逻辑**

---

# 05 更真实的问题：不是“绕过 MFA”，而是“策略不一致”

需要强调一点：

网络上流传的“绕过 MFA”说法往往过于简化。

更准确的描述是：

> 在特定 resource exclusion 场景下，CA enforcement 在 Graph token issuance 上存在一致性差异。

表现为：

* 某些 low privilege token 不触发预期的 CA control
* 部分 first-party client 行为更“宽松”
* 策略日志可能显示 Not Applied

---

# 06 Microsoft 的应对：从 legacy behavior 到统一 enforcement

微软实际上已经意识到这一类“路径不一致问题”，并在逐步推进新的模型：

* 统一 token issuance evaluation
* 强化 Continuous Access Evaluation（CAE）
* 收紧 Graph token 与 CA policy 的绑定关系
* 减少 legacy compatibility 分支

在部分租户中，已经可以看到所谓：

> “baseline enforcement / modern CA evaluation behavior”

---

# 07 对企业的真实影响：不是漏洞，而是“配置风险放大器”

对于企业管理员来说，这类问题真正的风险不在于攻击技巧，而在于：

### ❗ CA 复杂性被低估

常见误区包括：

* 认为 Exclude 只是业务例外
* 认为 MFA 是全局一致执行
* 认为 Graph API 不受 CA 影响

但现实是：

> CA 是一个跨登录链路的分布式策略系统，而不是单点开关

---

# 08 企业建议（实战向）

如果你在管理 Entra ID 环境，可以重点关注：

### ✔ 1. 最小化 Exclude 使用范围

避免 “All apps + 大范围 exclusion”

### ✔ 2. 检查 Graph 相关登录行为

重点关注：

* User.Read
* profile / openid flow
* third-party + first-party 混合 token

### ✔ 3. 启用现代 CA evaluation 行为

逐步迁移到新策略模型（CAE / unified evaluation）

### ✔ 4. 审计 sign-in logs

关注：

* “policy not applied”
* token issued without expected control

---

# 结语

在零信任体系里，最危险的从来不是某一个“漏洞点”，而是：

> **看似合理的例外配置，在复杂系统中逐渐演变成不可预期的信任路径差异**

Microsoft Entra ID 的 CA 体系并没有“失效”，但它提醒我们：

> 安全策略的复杂度一旦超过理解能力，配置本身就可能成为风险来源。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ndxZsFvkmpznJ7eICiaSkulHmla8V8RPVeTQ5z2uI5iaV9FniaMzXYbodGk9qNSBY6ccvbiaW5XxvKJNp7zLicxwSEQ/0?wx_fmt=png)

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