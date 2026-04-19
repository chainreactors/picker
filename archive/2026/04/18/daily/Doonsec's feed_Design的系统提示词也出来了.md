---
title: Design的系统提示词也出来了
url: https://mp.weixin.qq.com/s/Ds3wLKLeVAJFg90SA29fIA
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:46:40.364984
---

# Design的系统提示词也出来了

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/cBGhzWwhSAggQVG98wia4DDjgqLfvnPCEa3ryGJHeIbwVZ74sf04uicT8PNfWkLNiaIhsUMTaTdRQtzoVOQk50eWKSPW1pNzbyEhZqmpT3nxVs/0?wx_fmt=jpeg)

# Design的系统提示词也出来了

原创

🅼🅰🆈
🅼🅰🆈

独眼情报

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAgEuBeU9qJ6icTBUuuFfLxGpFSREqdvHSx4pHUuXw39Eq1M9xCZjl1Bc6KfNWNxvFfyfy80icG2jYic31QQJ0NGiaoorJp7EGR0iaAc/640?wx_fmt=png&from=appmsg)

这是 Anthropic「Claude Design」（claude.ai 上的设计/原型产品，即 Artifacts 的进阶版）的系统提示词，核心是把 Claude 塑造成一个**在文件系统项目中用 HTML 产出设计稿的资深设计师**，而非普通聊天助手。

**角色定位**：HTML 是工具，但真正要扮演的角色随任务变化——动画师、UX 设计师、幻灯片设计师、原型师。除非真在做网页，否则要刻意避开「网页设计套路」。

**工作流严格**：理解需求→探索已有资源（设计系统/UI kit）→做 todo→建目录结构→产出→调用 `done` 自检→`fork_verifier_agent` 后台验证→极简收尾。提问环节权重很高，模糊需求必须先用 `questions_v2` 问一轮，且要求「至少问 10 个问题」，默认要问用户是否要变体、要几个、探索哪些维度。

**设计哲学明确**：

* 反 AI slop——禁用滥用渐变、emoji、圆角左边框强调条、SVG 画图标（宁用占位符）、Inter/Roboto 这类烂大街字体
* 禁止填充内容——「空了是设计问题，不是内容问题」，想加内容必须先问用户
* 高保真设计必须基于已有设计上下文，从零造是「最后手段且结果必然差」
* 给变体要跨多个维度（视觉/交互/色彩/动画），从保守到大胆铺开

**技术约束具体到死**：React 必须用钉死版本号和 integrity hash 的 CDN；多个 Babel 文件因作用域隔离必须手动 `Object.assign(window, {...})`；style 对象命名冲突是不可协商的红线必须叫 `terminalStyles` 不能叫 `styles`；禁用 `scrollIntoView`；slide 编号必须 1-indexed 对齐用户心智。

**有意思的几个信号**：

* 内置 `window.claude.complete()`，artifact 里可以直接调 Haiku 4.5，1024 token 上限，走访问者配额
* Tweaks 机制——工具栏可切换的「实时改设计」面板，有 `/*EDITMODE-BEGIN*/.../*EDITMODE-END*/` 标记块让宿主能改写磁盘
* Speaker notes、跨项目只读访问、GitHub 导入（强制要求真读代码不要凭记忆重建 UI）
* `snip` 工具管理上下文，明确说「悄悄 snip 别告诉用户」
* 版权条款——要求重建某公司 UI 时必须拒绝，除非用户邮箱域名匹配该公司

**一句话总结**：这是一个把「资深设计师的工作纪律」工程化的提示词——强制提问、强制基于既有系统、强制变体探索、强制验证闭环，用大量硬规则把 LLM 的偷懒倾向（从零编、加填充、用烂大街字体、猜而不查）挡在门外。

https://github.com/elder-plinius/CL4R1T4S/blob/main/ANTHROPIC/Claude-Design-Sys-Prompt.txt

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

独眼情报

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

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