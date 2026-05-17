---
title: 做了两个 Claude Code 插件，把一些重复劳动省了
url: https://mp.weixin.qq.com/s/vm9Db6zpD6xhjTcfGxGoxQ
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:47:19.793892
---

# 做了两个 Claude Code 插件，把一些重复劳动省了

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t9FpDdenMLUL1ItiaQlue8ZhckQPngYYnwVtapA0icj7eKtOUxqDsCWRRgUbcn5NTl4JFYBKmOUKYT3DPsCcguzMK1Vb9Qaq8ayGpvycIqKia8/0?wx_fmt=jpeg)

# 做了两个 Claude Code 插件，把一些重复劳动省了

chengable
chengable

安全产品人的赛博空间

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

最近搞了两个 Claude Code 的插件，本来只是自己用，后来想想，可能也会有人碰到类似的麻烦，索性整理了一下开源出来了。

agent-morph：

智能体做多了，发现有套路

最早没想着要做这个。就是前阵子事情比较多，我在 Claude Code 里做了十几个小agent。其实不管做什么类型的智能体，核心组件就那么几样：skill 负责编排，subagent 做专项处理和隔离上下文，MCP 负责接外部工具或数据源，hooks 负责事件拦截或者自动触发，再加上 scripts 做一些辅助处理和固定数据处理。

这些组件的职责是明确的，组合方式也基本是固定的模式。但每次新建一个智能体，还是得把这些东西重新搭一遍，很多是纯手工的重复劳动。

agent-morph 就是干这个的：

把“需求 → 调研 → 架构设计 → 构建 → 验证”这套流程自动化掉。

你给它一句话需求、一个 GitHub 仓库、一个本地项目或者一份 PDF 文档

它自己走完整条链路，最后产出一个结构完整、链式闭环的智能体包。

我对“链式闭环”这件事有点执念——就是主 skill 必须能一路追踪到每个 agent 和脚本，不允许有任何东西落单。

agent-morph 前置依赖superpowers和 plugin-dev，因为这俩太多东西可复用，不用重复造，README 里有写。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t9FpDdenMLVWTX3eIIUCZic1vfDXMQheMsHTwglKVibqQDxAPFJSqFs1z6KN9dkiawoWfbnZnFPGTzBCgsqpsMh2eEeYvpcicicANnYkOltxdxGM/640?wx_fmt=jpeg)

claude-evol：

Hermes 太火了，碰巧我自己也需要

这个的起因比较具体。

一个是最近到处都能看到人在讨论 Hermes，尤其是它那个“自主进化”的能力，大概就是自动检测重复模式、学习错误经验、积累知识这一套。我看了下觉得思路确实有意思，但 Hermes 是另一套体系的东西，我日常工作在 Claude Code里 。

另一个是我自己平时工作中的真实情况：skill 写完了，但有些地方其实不够好，用着用着发现要调整纠正，或者同一个事情我跟 Claude Code 说过好几遍，它在那个会话里是记住了，但重开会话就又回到原样。当然你可以手动让它写进 CLAUDE.md，但总觉得不够系统化，也不知道哪些东西真的值得持久化，哪些只是临时的。

于是我就让 AI 自己去读 Hermes 的代码，把里面关键的提示词和触发条件提取出来，然后做了个适配，移植成了 Claude Code 的插件。

claude-evol 做的事情就是：

后台 Hook 自动统计你对话里的重复模式和错误经验，达标了就在下一次会话提醒你审查。

你敲一个 /claude-evol，它会用审查 Agent 自动判断这些经验应该存成什么：

是 Skill（怎么做）、CLAUDE.md（记住什么）、还是 .claude/rule/（必须/禁止的硬性约束）。

默认需要你确认才会写入，怕它自己瞎改。

![](https://mmbiz.qpic.cn/mmbiz_jpg/t9FpDdenMLXiccVE3yL3BpLjicRVPWd9RyAvMgK4xo1icuwwIm9icUPPAf9w9icGCc5lPHXjlnAFQpKQEAtibkjjMKTb1IgOphA096eA7Dx0FReU0/640?wx_fmt=jpeg)

朋友们用得上可以给个star

> agent-morph
>
> https://github.com/chengable/agent-morph

> claude-evol
>
> https://github.com/chengable/claude-evol

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/8ZOMF5yvSF5BRA7aM7EBdGSSNibwLuRP5tJLXzZdwhCQMBF5RgIAyGK3k8u90GMZ9icP8koxamC5K54yIcVMgqsw/0?wx_fmt=png)

安全产品人的赛博空间

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8ZOMF5yvSF5BRA7aM7EBdGSSNibwLuRP5tJLXzZdwhCQMBF5RgIAyGK3k8u90GMZ9icP8koxamC5K54yIcVMgqsw/0?wx_fmt=png)

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