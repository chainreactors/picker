---
title: BinaryAI 全新升级：让二进制安全分析进入xa0AI-Nativexa0时代
url: https://mp.weixin.qq.com/s/bgv2DeBIA-PjoTOucxQ_gQ
source: Doonsec's feed
date: 2026-08-25
fetch_date: 2026-08-26T03:03:00.367035
---

# BinaryAI 全新升级：让二进制安全分析进入xa0AI-Nativexa0时代

# BinaryAI 全新升级：让二进制安全分析进入 AI-Native 时代

腾讯科恩实验室
腾讯科恩实验室

腾讯安全威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 让二进制安全分析 进入 AI-Native 时代

**恶意样本分析**是二进制安全工作中最高频、最关键的一环——从木马病毒、挖矿勒索到 APT 对抗，从漏洞挖掘到利用分析，每一起真实的安全事件背后，都是一次与二进制样本的正面对抗。我们打造了新一代二进制分析平台 **BinaryAI**，专为恶意样本分析而生，让分析更快、更准、更高效。

引言

## 二进制安全的技术困境

对于二进制安全从业人员来说，日常分析工作中始终绕不开两个核心痛点：

### 💰 使用成本高

高昂的授权费用让多数从业者望而却步。传统工具通常不支持云端部署，交互接口与产品形态也已明显无法跟上 Agent 时代的对接要求。

### 🧠 技术门槛太高

从字节码反向推导程序的原始行为逻辑，能熟练掌握这项技能的从业者凤毛麟角，但二进制分析在实际工作中的应用却无处不在。

借助 AI Agent 时代的种种突破，我们对 BinaryAI 进行了一次全面焕新：

BINARY QUERY

一款能与业界标杆正面对标的二进制安全分析工具，完全由 **AI Coding 驱动**。团队重心从逐行实现细节，转向架构设计和 Coding Loop 的深度优化。

BINARYAI AGENT

基于 **Workbuddy Managed Agents（WMA）** 的云端二进制分析 Agent，大幅降低使用门槛。用户通过对话与 Agent 交互，即可完成分析并获取结果。

PART 01

## Binary Query：AI Coding 的力量

Binary Query（简称 **BQ**）是整个 BinaryAI 体系的基石。它不只是一个反编译器，更是一个实验场——我们用 AI Coding 的方式，从头构建了一个能与业界标杆正面对标的二进制安全分析工具。

### 架构设计：更易于 AI 理解的反编译器架构

Binary Query 使用 Rust 的强类型特性来约束 AI；通过精简和调整传统反编译结构、保留 MIR 与 LIR，让整体架构对 AI 更易于理解、易于修改：

二进制文件 → loader → disasm → lift (MIR) → analysis (LIR) → lang + codegen → 源码

输入层

`bq-loader / bq-arch-*`：解析 ELF / PE / Mach-O，按架构反汇编，提升为机器无关的中间表示。支持 x86、ARM、RISC-V。

分析层

`bq-analysis / bq-pipeline`：控制流图重建、SSA 构造、数据流分析、类型推导。跨函数分析使用 Datalog 规则引擎。

输出层

`bq-lang-* / bq-db`：检测原始源代码语言（C、C++、Go、Rust、Zig），生成符合原始语言习惯的代码。

### AI Coding：减少人的介入，让 Agent 自己跑起来

研发的核心工作从写代码，变成了设计 Agent 指令和自迭代循环。真正要做的，是**把人从迭代循环里剥离出去**。

评测 用 Fuzz 替代人眼评测

反编译没有标准答案，但行为等价可量化——反编译结果重新编译、重新运行，输出跟原二进制一致就对。测试用例由 csmith 等 fuzzer 随机生成，数量充足，评测完全自动化。

![](https://mmbiz.qpic.cn/mmbiz_png/VnHqNyq3Ql96M30ZibDSvLbicMTfwBQZvCWwhaI7Fszyva7uOiaKSj2grtW7zTCPTXibMlK8HicTticJAmjCvq2zHksNqicHibNIkVjnQ4udGkQHrA8/640?wx_fmt=png&from=appmsg)

图 1 · Fuzz 驱动的自动化评测流程

定位 用 Interpreter 把"错了"变成"错在哪"

端到端测试只能说"对不上"，说不出哪个步骤出错。我们在 IR 层加了一个 interpreter，每个 pass 前后各执行一遍、比对语义，第一次对不上的 pass 就是根因。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VnHqNyq3Ql9IPY2vhGdp9RzIuibuzAErE8NAexjQ1icI7xLF6tVENR77YCDAGCHfhJ6IiamKMsBkiawKbQUc0BjHFFUmnzX1HuZCusDibrRm3M7Q/640?wx_fmt=png&from=appmsg)

图 2 · IR 层 Interpreter 精确定位失败 pass

Agent 获得的是精确定位到具体 pass 的失败信息，自主修复、自主验证——通过则一个 Bug 对应一次 Commit，未通过则继续迭代修复。人只做一件事：**确认最终结果**。

PART 02

## BinaryAI Agent：WMA 之上构建 Environment

直到出现了 **Workbuddy Managed Agents（WMA）** 这样的通用 Agent 控制面，BinaryAI NG 才有了可能。它承载了 Agent Loop、Runtime、调度、安全、隔离等复杂模块，BinaryAI 得以专注于"如何应用 Agent 解决用户的问题"。

![](https://mmbiz.qpic.cn/mmbiz_png/VnHqNyq3Ql8CGXLnHvpksrTSh9cYeShkMHJU8pbcfgAnLf74fgzuSnAqxV7RgfeVEvicNVMt2ibMCZF8nWHwQ52Hic8OOTWMsIsdW5icqwfUlrQ/640?wx_fmt=png&from=appmsg)

图 3 · BinaryAI Agent 整体架构

### 抽象分析操作：连接 Agent 与二进制文件

传统二进制安全分析工具是为人类分析师设计的：交互式界面、多级菜单、手动标注。**Agent 不需要这些**——它需要确定性的输入输出、简单的命令行接口、明确的退出码和超时机制。我们为 Agent 重新设计了一套 CLI：

Agent 可用的原子操作

📄 文件概览 `bq info`

这个文件是什么格式、什么架构

📋 函数列表 `bq functions`

有哪些函数可以分析

🔤 反编译 `bq decompile <fn>`

把这个函数还原成 C / Rust / Go 源码

⚙️ 反汇编 `bq disasm <addr>`

看看这个地址的汇编指令

🔗 交叉引用 `bq xrefs <addr>`

谁调用了这个函数，这个函数调用了谁

🔍 字符串提取 `bq strings`

文件里有哪些可疑字符串

💾 十六进制 `bq hex <addr>`

看一下这块内存区域

光有命令行还不够。这套编排知识被编码在 Binary Query 的 `SKILL.md` 中——一份 103 行的 Agent 操作手册：

# 端到端示例：一次典型的样本分析
bq create /path/to/binary
bq info --target /path/to/binary
bq functions --target /path/to/binary --filter "read|write"
bq decompile main --target /path/to/binary
bq strings --target /path/to/binary --min-length 8 --filter "http"
bq xrefs main --target /path/to/binary

Skill 还会告诉 Agent：`--filter` 要逐步收紧，不要一次 dump 所有函数；disasm 找不到函数时用 decode 代替；反编译前必须先 `bq create` 建立分析数据库。这些本来需要人类分析师积累的经验，现在被编码进 Skill——**Agent 装上去就会**。

### Prompt 提示与约束：连接 Agent 与用户输入

**System Prompt：边界和约束。** Agent 在没有明确指令时会遍历文件系统、反复重试失败的 API、用 shell 直接调 HTTP 接口。System Prompt 用最少的文字划出最硬的边界：工作区在哪、分析工具怎么调、哪些事不能做。每条都是硬约束，都对应一次 Agent 曾浪费 Token 的教训。

**预置 Skill：让 Agent 知道怎么做二进制安全分析。** 通用代码 Agent 拿到二进制文件，第一反应是 `file` 看一下，然后就卡住了。我们预置的 skill 内置了三条工作流：

① 恶意行为分析

识别文件格式 → 搜索可疑字符串 → 定位敏感 API → 反编译关键函数 → 输出行为摘要

② 关键 Payload 解析

解析文件结构 → 定位加密 / 压缩数据段 → 追踪解密函数 → 反编译解密逻辑 → 提取并还原 Payload

③ 漏洞利用分析

反编译目标函数 → 追踪输入到漏洞触发点的数据流 → 定位缺失的边界检查 → 分析利用原语

用户不需要说"先看字符串，再看导入表，然后反编译"——一句 **"分析这个样本的恶意行为"**，Agent 按 Skill 走，每一步都知道该干什么、结果怎么解读。

QUICK START

## 一分钟快速上手

直接上传样本，用一句话开始分析——完整体验请看下面这段演示视频。

ROADMAP

## 下一步：Dream Big, Build Solid

在将 BinaryAI 投入生产使用的过程中，我们发现了非常多的优化改进空间。经过反复思考，我们确定了三个最重要的目标，需要依次达成：

1 更精确的评测基准

基于真实业务场景，发布一套面向二进制安全分析的自有 Benchmark，准确评估 BinaryAI Agent 的能力。

2 更先进的分析工具

实现从汇编指令到 Rust、Golang 等现代编译型语言的原生反编译能力，应对日益复杂的真实分析场景。

3 更高效的模型

针对二进制分析这一垂直任务做专项模型优化，在保证分析质量的前提下，提供更低延迟、更低成本的体验。

— 内测开放中 —

## 加入 BinaryAI 内测

我们已开放邀请内测，欢迎二进制安全从业者与我们一起共建

💬 加入交流群获取内测方式

📱 扫码加入 BinaryAI 交流群

![](https://mmbiz.qpic.cn/mmbiz_png/VnHqNyq3QliblXibW2L9YwHTBsvEzsrHiaQqdqvpLbLsF9RxLSc3TNTdfMtjyzL1nWAUT21uVsQCBia4YZWUe8V66DbjDLGuGcnfDdftqpp19ew/640?wx_fmt=png&from=appmsg)

若群已满，微信搜索添加 `keenlab` 为好友，发送 **"BinaryAI 交流群"**，小助手会拉你入群。

与我们一起探索 AI-Native 的
二进制安全分析工作流

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6AoQM3RKCWUu1j1TYiaYRU8wWVGpaHhqaEDCiah9eDwNn00ncbMsWBQwBbd41N9WNYEvp7neMHMksDS9dScCZ2aQ/0?wx_fmt=png)

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