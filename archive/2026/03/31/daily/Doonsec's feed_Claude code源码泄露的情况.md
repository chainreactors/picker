---
title: Claude code源码泄露的情况
url: https://mp.weixin.qq.com/s/zgUQQb4ssErhVg7pPGd8vA
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:43:51.495043
---

# Claude code源码泄露的情况

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/316EM2ouicpzT3ricHPOoeG9iaS9J9AR4hibyNvRJTNNsq5FoDvtojRvBsQicylIM4xFxoLDwvrics8HcwFfjZScXOugKPgZH9CwKJia7qfhibxHu4w/0?wx_fmt=jpeg)

# Claude code源码泄露的情况

王慧敏
王慧敏

AI与代码安全

![]()

在小说阅读器中沉浸阅读

这次所谓“Claude Code 源码泄露”其实不是传统意义上的“黑客入侵”，而是一次**工程发布失误导致的“可逆源码暴露”事件**。我给你按关键点梳理一下（比较重要）：

# 一、事件核心：Source Map 泄露源码

这次主角是 Anthropic 的开发工具 **Claude Code（CLI 编程助手）**。

发生了什么：在 **v2.1.88 版本发布到 NPM** 时，误把 `cli.js.map`**（Source Map 文件）一起发布了****。**

而 Source Map 的作用是：把压缩后的 JS ↔ 原始源码一一映射（方便调试）

结果就是：本来“混淆后的代码”，可以被**完全还原成原始源码结构****。**

# 二、 泄露程度：几乎“全量还原”

根据社区分析：

1）Source Map 里包含：

1.完整源码路径

2.函数名 / 变量名

3.模块结构

2）开发者只需：

Bash

npm install
+ reverse-sourcemap

就能恢复源码

甚至有说法称：包含数千个源文件（社区提到约 4000+ 文件）

本质：**不是“部分泄露”，而是接近“源码公开级别”**

# 三、 泄露了哪些内容？

目前整理下来，主要包括：

## 3.1 CLI 工具核心逻辑

1）Agent 调度流程

2）任务执行逻辑

3）插件 / 工具调用方式

## 3.2 内部 API 调用细节

1）请求结构

2）调用链设计

3）权限/执行流程

## 3.3 Prompt / Agent 设计（可能）

1）系统提示词结构（部分被提取到 GitHub）

注意：

1）**模型权重没有泄露**

2）**训练数据没有泄露**

所以不是“模型泄露”，而是：**产品工程实现泄露**

# 四、 为什么这件事很严重？

这类泄露在 AI 行业其实挺敏感，原因有几个：

## 4.1 AI 工程“护城河”暴露

Claude Code 本质是：

LLM + Agent系统 + 工具链

泄露后别人可以：

1）直接学习 Anthropic 的 Agent 架构

2）复制 CLI 设计

3）分析 prompt engineering

## 4.2潜在安全风险

源码中可能包含：

1）API 调用逻辑

2）权限机制

3）安全策略

攻击者可以：

1）找漏洞

2）逆向调用链

（类似之前的漏洞：Claude Code 曾出现 API key 提前泄露问题）

## 4.3 行业影响

这类事件会引发一个更大的问题：**AI 产品到底算不算“软件资产”？**

1）传统软件：源码 = 核心资产

2）AI 产品：prompt + orchestration 同样重要

# 五、 本质原因：DevOps 失误（不是黑客）

这次很典型：

问题点：

1）打包流程没去掉 `.map`

2）CI/CD 没做安全检查

3）NPM 发布未过滤敏感文件

一句话总结：**不是被攻破，是自己“带着源码上线”**

# 六、 和其它“Claude泄露事件”的区别

顺便区分一下，最近 Claude 相关“泄露”其实不止一个：

## 6.1 本次（最火）

1）类型：源码可逆泄露

2）原因：Source Map

3）影响：工程实现暴露

## 6.2 模型/内部信息泄露（另一条线）

1）未发布模型信息被泄露（如 Mythos）

2）内部文档/活动信息外泄

属于“数据管理问题”

## 6.3 安全漏洞

1）API Key 被提前发送

属于“产品逻辑漏洞”

# 七、 总结

这次事件可以这样理解：**Claude Code 没被黑，是 Anthropic 把“带源码的调试文件”直接发到 npm，导致任何人都能还原其完整工程实现。**

**【AI代码助手、大模型智能体安全、AI代码静态分析工具、AI动态分析工具、AI渗透测试工具、AI模糊测试、AI恶意代码检测平台、AI软件漏洞挖掘平台、AI软件供应链安全平台。试用及合作请后台私信工程师13381155803（微信同步）】**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/gbFHCWYSgF4dWsMlOVnEDAzyugosHQFicRvViccFWcTR87YWA0ZVg0p2tXglgnXEQElwnIhhmpEwulCbzCbzKb1A/0?wx_fmt=png)

AI与代码安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/gbFHCWYSgF4dWsMlOVnEDAzyugosHQFicRvViccFWcTR87YWA0ZVg0p2tXglgnXEQElwnIhhmpEwulCbzCbzKb1A/0?wx_fmt=png)

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