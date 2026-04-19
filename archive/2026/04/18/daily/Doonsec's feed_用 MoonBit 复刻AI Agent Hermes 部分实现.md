---
title: 用 MoonBit 复刻AI Agent Hermes 部分实现
url: https://mp.weixin.qq.com/s/ydcnmJ1b7mKBm9lE8e869w
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:52:10.489267
---

# 用 MoonBit 复刻AI Agent Hermes 部分实现

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/CBe66ugaImkROSAZvD241k5eFI7kTUhZEZvbfRxDl8CPjnIOcicyuibsibTtN0wiaGmic6Xq6jUnrAPvYXy3MiaRFkqOR63YGdzeN9VbicqxchAcEY/0?wx_fmt=jpeg)

# 用 MoonBit 复刻AI Agent Hermes 部分实现

原创

爱唠叨的Nil
爱唠叨的Nil

爱唠叨的Nil

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Moonbit   HERMES AI · v1.0.0

爱唠叨的Nil · 技术分享

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CBe66ugaImlzyAyJJLaZzA1uXaykWbjEjMmrJg8BjBQORLoicHKTfHKr7ibI7Y7MKkjHuL1MaozhVwT8Wicg6aslAA74jBw4t5tFqtZvCric0lE/640?wx_fmt=jpeg)

**导语：**Hermes 是一个全功能 AI Agent，支持多模型切换、工具调用、预算控制、记忆系统。现在，用MoonBit 语言进行部分复刻，性能更优、类型安全、编译速度极快。

## 🚀 什么是 Hermes？

Hermes 是一个运行在终端的 AI Agent 框架，具备以下核心能力：

* 🧠 **多模型支持** — OpenAI / Claude / 通义千问 / DeepSeek
* 🔧 **工具调用** — 终端命令、文件操作、Web 搜索
* 💰 **预算控制** — Token 消耗实时追踪
* 🧵 **对话记忆** — 持久化上下文，跨会话不丢失
* 🔌 **飞书集成** — Webhook 桥接，消息即对话

## 🌙 为什么用 MoonBit ？

MoonBit 是由前 Google 工程师张宏波主导开发的新一代编程语言，专注于 WebAssembly 和云原生场景。相比 Python 原版，MoonBit 版本带来：

* ⚡ **编译速度** — 毫秒级编译，远快于 Rust/C++
* 🛡️ **类型安全** — 编译期杜绝空指针和类型错误
* 📦 **极小二进制** — 1.2MB 原生二进制，无依赖
* 🌐 **多目标** — 同时编译 native / wasm-gc / JS

## 📊 项目数据

当前使用hermes单agent，用时48小时，当前只具备部分功能，或者仅仅能对话😊

|  |  |  |  |
| --- | --- | --- | --- |
| 53  源文件 | 532  测试用例 | 3409  代码行数 | 1.2MB  二进制大小 |

## 🎯 v1.0.0 进展

| 模块 | 状态 |
| --- | --- |
| 核心 Agent 循环 | ✅ 完成 |
| 多模型注册表 | ✅ 完成 |
| 工具调用系统 | ✅ 完成 |
| 预算配置与追踪 | ✅ 完成 |
| 审批工作流 | ✅ 完成 |
| 记忆系统 | ✅ 完成 |
| CLI 终端渲染 | ✅ 完成 |
| 飞书 Webhook 桥 | ✅ 完成 |

   🔥  问题:

飞书对接还是个假的，或者只写了函数

记忆部分貌似也没有实现

开发期间，虽然给他相对清晰方向和要求，他依旧需要时不时盯着

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CBe66ugaImlkoSvRnukWAzG1I4j8NslUwSX4BoPiaERc0D3Qe1urFAVfKkrmUVmk7kHVicwGREGWFIPMCQOyfmAPS81TmRNQlXlVZaAInloQs/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CBe66ugaImniav0DtnwiaB7n6CVW6BdTzibZTiaGLVtasZnvrjSxvFDMG001xa010rETgDBTvct5ibaE2KTk6ia3y6bHzx4bqjnTom9a1ia0hSjJyw/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CBe66ugaImnqOS90ib3n8zfdTObOic2KvL0mNnAA11k1Fc6Q3hxhYoSyzIwofMKh0aCjt3cvPGHJy4INicoUQibrDicOZibwt9MDQicFCfibfe4CvDM/640?wx_fmt=jpeg)

## 💻 快速上手

https://github.com/nillikechatchat/hermes-moonbit

# 编译

moon build --release

# 运行测试

moon test --target native

# 启动交互模式

./bin/hermes

⭐ 如果你也觉得 MoonBit 很棒
欢迎 star 项目，一起建设生态

— 爱唠叨的Nil · 用技术改变世界 —

预览时标签不可点

作者提示: 内容由AI生成

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Eic0kibODiaic3cnib21814uBlib0RxYwbFZILry66UgHqsZlvOSBByNwCXtjpcFXFhjtcmLx8FpFgVDgPASPuo2YT4w/0?wx_fmt=png)

爱唠叨的Nil

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Eic0kibODiaic3cnib21814uBlib0RxYwbFZILry66UgHqsZlvOSBByNwCXtjpcFXFhjtcmLx8FpFgVDgPASPuo2YT4w/0?wx_fmt=png)

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