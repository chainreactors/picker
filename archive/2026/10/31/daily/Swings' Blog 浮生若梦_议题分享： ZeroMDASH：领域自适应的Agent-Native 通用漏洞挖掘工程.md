---
title: 议题分享： ZeroMDASH：领域自适应的Agent-Native 通用漏洞挖掘工程
url: https://bestwing.me/zeromdash-agent-native-vulnerability-mining.html
source: Swings' Blog 浮生若梦
date: 2026-10-31
fetch_date: 2026-11-01T08:17:53.159040
---

# 议题分享： ZeroMDASH：领域自适应的Agent-Native 通用漏洞挖掘工程

[SKIP\_TO\_CONTENT](#main-content)

[SECURITY RESEARCH LOG
·
Swings' Blog 浮生若梦](/)

BESTWING.ME

[[SWING/]](/)

MENU
[+]

[./INDEX](/)
[./ARCHIVE](/archives/)
[./CATEGORIES](/categories/)
[./TAGS](/tags/)
[./ABOUT](/about/)
[./LINKS](/link/)

⌘K
SEARCH

// RESEARCH\_TRANSMISSION
ID: ZEROMDASH\_AGENT\_NATIVE\_VUL

# 议题分享： ZeroMDASH：领域自适应的Agent-Native 通用漏洞挖掘工程

PUBLISHED2026.11.01

READ\_TIME**2 MIN**

PAYLOAD**778 CHAR**

CHANNEL[Writeup](/categories/Writeup/)

// INDICATORS
[ZeroMDASH](/tags/ZeroMDASH/)[Agent-Native](/tags/Agent-Native/)[AI Agent](/tags/AI-Agent/)[vulnerability-mining](/tags/vulnerability-mining/)[kanxue-sdc-2026](/tags/kanxue-sdc-2026/)

// CONTENT\_MAP

1. [前言](#%E5%89%8D%E8%A8%80)
2. [议题介绍](#%E8%AE%AE%E9%A2%98%E4%BB%8B%E7%BB%8D)
3. [议题亮点](#%E8%AE%AE%E9%A2%98%E4%BA%AE%E7%82%B9)
4. [公开 slide](#%E5%85%AC%E5%BC%80-slide)
5. [开源代码](#%E5%BC%80%E6%BA%90%E4%BB%A3%E7%A0%81)

[↑ RETURN\_TO\_HEADER](#main-content)

BEGIN\_PAYLOAD20261101

…

## 前言

这个议题于2026年10月23日在看雪 SDC 2026 上分享。

## 议题介绍

AI Agent已经能够阅读代码、调用工具并自主执行安全分析，但当目标从单一函数扩展到 Linux 内核、虚拟化系统、网络协议栈等复杂软件时，为什么它仍会遗漏真正重要的漏洞？问题往往不只是上下文长度不足，而是模型缺少对目标软件特有安全机制的理解：它不知道哪些对象属于核心资产，哪些权限关系和状态转换必须满足特定的安全约束，也难以判断散落在不同模块中的局部缺陷能否组合成一条真实可利用的攻击链。

本议题将介绍 ZeroMDASH，一套面向源码漏洞挖掘的领域自适应 Agent-Native 分析框架。它不依赖预设的漏洞类型清单，而是从目标代码出发，自主识别其中的关键对象、权限关系、信任边界、状态转换及其安全约束，并将潜在攻击面转化为可追踪的分析范围和漏洞假设。随后，由调查 Agent 与审查 Agent 围绕源码证据、反例和未解决条件展开多轮对抗式验证。系统还会关联分析分散在不同模块中的风险线索，识别单点分析难以发现的复杂漏洞与攻击路径。

当每一个局部行为看起来都“不是漏洞”时，它们组合起来是否可能导致权限提升、信息泄露？当 Agent 声称“没有发现问题”时，我们又如何判断它确实完成了必要的安全分析，而不是因为分析范围不足而提前停止？本议题将围绕这些问题，分享 ZeroMDASH 在目标领域安全建模、假设集推理、对抗式证据复核以及跨原语攻击链验证方面的设计与实践，并讨论 AI 漏洞挖掘如何从生成潜在issue，进一步发展为构建可追踪和复核的安全证据。

## 议题亮点

**Agent时代的漏洞挖掘，怎么才能挖得又全又准。**

## 公开 slide

这里公开 slide，感兴趣的同学可以自行阅读。

[在线阅读 slide](https://cossack9989.github.io/slides/2026/10/23/zeromdash-agent-native-vulnerability-mining.html)

## 开源代码

ZeroMDASH 已开源，代码仓库：

<https://github.com/JANUS-SEC/ZeroMDASH>

EOFCHECKSUM\_OK

← PREVIOUS\_LOG // NULL
[NEXT\_LOG →
**议题分享： Pwn2OwNothing: When a KVM Full-Chain Escapes to Emptiness**](/hitcon-2026-pwn2ownothing-when-a-kvm-full-chain-escapes-to-emptiness.html)

// EXTERNAL\_CHANNEL

## 评论

请启用 JavaScript 查看评论。

$ contact --channel secure

## 关于漏洞、系统与攻防，欢迎交流。

// RESPONSE\_TIME: WHEN\_THE\_SIGNAL\_IS\_CLEAR

ask@mail.exp.sh↗

© 2016—2026 Swing · BUILT\_WITH\_HEXO · SIGNAL\_THEME

[GITHUB](https://github.com/WinMin)
[X](https://twitter.com/bestswngs)
MAIL
[RSS](/atom.xml)

[↑ TOP](#top)

SEARCH\_PROTOCOL // LOCAL\_INDEX

[ESC]

$ query --all-posts

>

TYPE\_TO\_SCAN\_THE\_ARCHIVE