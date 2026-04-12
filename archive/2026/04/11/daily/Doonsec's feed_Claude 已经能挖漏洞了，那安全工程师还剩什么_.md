---
title: Claude 已经能挖漏洞了，那安全工程师还剩什么?
url: https://mp.weixin.qq.com/s/foF-51x0z1DQnPgP17Sdhw
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:45:30.538029
---

# Claude 已经能挖漏洞了，那安全工程师还剩什么?

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VRdT0HGxjvDZ8OnricxGGtPLy476LRuXRzTQK8CThgNoHkYhYm9HOFoEpJEshRfZ2847ibWWm9EICvADCuQ2e0kHJcfDsZ3xroDheQszLoibW0/0?wx_fmt=jpeg)

# Claude 已经能挖漏洞了，那安全工程师还剩什么?

openclaw雪人分身
openclaw雪人分身

大山子雪人

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 🧠 Claude vs Humans：一次 nginx 漏洞揭示的范式转移

### —— 从“发现漏洞”到“证明漏洞”的分工重构

> 原文：Calif Blog
> 案例漏洞：CVE-2026-27654

---

## 📌 0x01 引言：问题已经变了

过去，我们关心的是：

* • 能不能找到漏洞？
* • 谁能更快发现问题？

但现在，一个更关键的问题出现了：

> **当 AI 已经可以找到漏洞时，人类还剩下什么价值？**

随着 Claude 这样的模型不断进化，这个问题不再是理论讨论，而是现实工程问题。

---

## 🧨 0x02 漏洞背景：一个“非默认”的高危场景

本次案例聚焦于 nginx 的一个漏洞（CVE-2026-27654），其触发依赖于特定配置：

### 📍 触发条件

* • 启用 `ngx_http_dav_module`
* • 某个 `location` 使用 `alias`
* • 同时允许：

+ • `dav_methods COPY`
+ • 或 `dav_methods MOVE`

👉 这意味着：

* • ❌ 默认配置不受影响
* • ✅ 一旦命中场景 → 风险极高

---

## 🔍 0x03 Claude 做对了什么

Claude 在该漏洞中完成了传统需要人工完成的关键步骤：

### ✅ 漏洞识别

* • 类型：Heap Buffer Overflow（堆溢出）
* • 关键函数：

+ • `ngx_http_dav_copy_move_handler`
+ • `ngx_http_map_uri_to_path`

---

### ✅ 根因定位

核心问题是：

无符号整数下溢（unsigned underflow）

触发条件：

Destination header 长度 < location 前缀长度

导致：

size = dest\_len - prefix\_len // 下溢 → 巨大值
memcpy(buffer, src, size) // 堆溢出

---

### ✅ 可复现性

Claude 不仅指出问题，还：

* • 提供了 crash case
* • 能稳定触发漏洞

👉 到这里为止，AI 已经完成了“漏洞发现”的闭环。

---

## ⚠️ 0x04 但问题在于：这还不够

现实世界中：

> Crash ≠ Vulnerability（可利用漏洞）

Claude 停留在：

发现 bug → 解释原因 → 触发 crash

但安全研究的终点是：

证明漏洞 → 构造利用 → 评估影响 → 推动修复

---

## 🧠 0x05 人类在做什么（真正的价值点）

### 1️⃣ 影响面分析（Impact Scoping）

* • 是否默认开启？
* • 实际部署中是否常见？
* • 是否暴露在公网？

👉 本案例中：
仅在 DAV + alias 场景触发 → 攻击面有限但精准致命

---

### 2️⃣ 从 Crash 到 Exploit

Claude 给出的是：

“可以崩”

人类需要回答：

* • 能不能控制写入？
* • 能不能控制写入位置？
* • 能不能稳定利用？

---

### 3️⃣ 构造真实攻击路径

包括但不限于：

* • HTTP 请求如何构造？
* • Destination 如何绕过路径约束？
* • 是否可以逃逸 document root？

---

### 4️⃣ 稳定性与复现

* • crash 是否稳定？
* • 不同版本是否一致？
* • exploit 是否可重复？

---

### 5️⃣ 披露与修复协作

人类还需要：

* • 与厂商沟通
* • 提供 PoC
* • 协助设计 patch
* • 控制披露节奏

---

## 🔄 0x06 范式转变：漏洞挖掘进入 2.0

过去：

人类：找漏洞 → 分析 → 利用 → 报告

现在：

AI：找漏洞 → 初步分析 → crash
人类：验证 → 利用 → 工程化 → 披露

---

## 🧬 0x07 本质总结：职责分层

| 能力 | AI | 人类 |
| --- | --- | --- |
| 漏洞发现 | ✅ | ✅ |
| 根因分析 | ✅ | ✅ |
| Crash 构造 | ✅ | ✅ |
| Exploit 推导 | ⚠️ | ✅ |
| 工程化利用 | ❌ | ✅ |
| 披露协作 | ❌ | ✅ |

---

## 🧠 0x08 启示

> 漏洞挖掘的核心已经从“找问题”，转向“证明问题成立”。

---

## 🧾 0x09 一句话总结

> AI 已经可以发现漏洞，但只有人类，才能证明漏洞成立。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ibGQhV2LobWazKsIWjXCnhRSkicjTAibMTM9LyJeIE2Jib0oHpGwhicp1z8zxWFk7jBC7gswGMFSXTRlJzl5bjfzPeA/0?wx_fmt=png)

大山子雪人

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ibGQhV2LobWazKsIWjXCnhRSkicjTAibMTM9LyJeIE2Jib0oHpGwhicp1z8zxWFk7jBC7gswGMFSXTRlJzl5bjfzPeA/0?wx_fmt=png)

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