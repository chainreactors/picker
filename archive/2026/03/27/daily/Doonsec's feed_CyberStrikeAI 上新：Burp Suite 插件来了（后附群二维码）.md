---
title: CyberStrikeAI 上新：Burp Suite 插件来了（后附群二维码）
url: https://mp.weixin.qq.com/s/d8d0QsGtGcG3ZNQqgmmLig
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:12:15.715926
---

# CyberStrikeAI 上新：Burp Suite 插件来了（后附群二维码）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ufQ2xnAD33ucWRhTcWiczicH4icC9S1X9JS5MHu1YU34kNNpn6sw1V7Lz9uYwxHxNm9hn7gtcNQugBNOvy9ZqjMXt3GS2M0poFunyRgyovtcNk/0?wx_fmt=jpeg)

# CyberStrikeAI 上新：Burp Suite 插件来了（后附群二维码）

原创

学安全也就图一乐
学安全也就图一乐

低调学安全

![]()

在小说阅读器中沉浸阅读

做 Web 渗透的同学都懂：**Burp 里的“这条流量”**，往往就是问题的起点。你想快速判断它有没有价值、该怎么改包验证、该抓什么证据、怎么把过程整理成可交付的结论——这些动作既需要经验，也很耗时间。

这次 CyberStrikeAI 带来一个更贴近实战的能力：**Burp Suite 插件**。它不是把 Burp 当“输入框”，而是把你最核心的资产——HTTP 流量——直接接入 CyberStrikeAI 的 Agent 流式测试能力，让你在 Burp 里就能完成“发包 → 推理 → 验证思路 → 记录结果”的闭环。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ufQ2xnAD33sOJISKUb847LTLPBDTh00XjEyHjNTb4CkYy3nSxv40jadIujibjIuXgTBZH9I8nqPibWficRvVVR13bup4uHt3Ig6aRvuMK6vh1I/640?wx_fmt=png&from=appmsg)

---

## 这个 Burp 插件能做什么？

### 1）右键一条流量，直接交给 CyberStrikeAI 做 Web 渗透测试

在 Burp 的 Proxy / HTTP history / Repeater 等位置，选中一条请求，右键发送到 CyberStrikeAI。
插件会把这条请求（可选带响应片段）发送到 CyberStrikeAI 的流式接口，让 AI **围绕该流量**给出渗透测试思路与可操作步骤。

我们把提示词刻意做得很“短”和“实战”：

> 针对该流量做web渗透测试

避免模型跑成泛化分析、Checklist、或无关的扫描建议。

### 2）可回看、可对比：测试历史侧边栏

很多时候你不是只测一次，而是要对比不同 payload、不同参数、不同响应。
插件内置**测试历史侧边栏（可搜索）**，每一次右键发送都会生成一条记录：

* 标题（`METHOD host/path`，方便定位）
* 单/多 Agent
* 状态（运行中 / 完成 / 错误 / 取消）

点开任意记录，就能回看当时的输出、请求与响应。

### 3）输出不再“刷屏”：Progress（可折叠）+ Final Response（主区域）

流式输出好用，但如果把“进度/调试/思考流”混在正文里，就会变得难读。
我们把 Output 拆成两段：

* **Progress（可折叠）**：只放进度、错误、取消等事件（开启 debug 时也会把思考流按行拼接后再展示，避免碎片化）
* **Final Response（主区域）**：只放最终正文与结论

### 4）可读性更强：Final 支持 Markdown 渲染

很多测试结论最终要沉淀为报告、工单、复测说明。
插件支持把 Final Response 的 Markdown 渲染成富文本（标题、列表、代码块、行内 code 等），阅读体验更像文档而不是日志。

### 5）可控制：Stop 一键取消当前会话任务

遇到跑偏/跑久/你已经确认结论时，可以直接 Stop。
插件会在会话创建后调用后端取消接口，避免浪费时间与资源。

---

## 为什么我们要做 Burp 插件？

因为“对话式安全测试”要真正落地，必须进入安全人员的日常工作流。
对很多人来说，Burp 就是 Web 渗透的主战场：请求在哪里、证据在哪里、复测怎么做，都在 Burp 里。

CyberStrikeAI 的目标不是替代 Burp，而是让 AI 在 Burp 的工作流里，帮助你更快完成：

* 判断这条流量有没有“可打点”
* 提供可验证的发包改法与证据点
* 保留可追溯的测试记录与输出
* 把结果更顺滑地沉淀成可交付内容

---

## 后续计划：持续改进 + 更多插件

Burp 插件只是开始。接下来我们会持续迭代“好用性”，包括但不限于：

* 更结构化的结果面板（Findings / Payloads / Evidence）
* 历史记录持久化与导出报告（Markdown/HTML）
* 一键复测 / 对比不同 payload 的差异
* 更丰富的集成插件：浏览器代理联动、CI/工单系统、IDE/MCP 等方向的插件与连接器

我们希望 CyberStrikeAI 不仅是一个平台，更是一套**可插拔的集成能力**：让 AI 安全测试能自然地融入你已有的工具链。

---

## 获取方式

插件已集成在 CyberStrikeAI 项目的 `plugins/` 目录下（Burp Suite extension），可编译成 jar 后在 Burp 里直接加载使用。文档与使用说明已提供中英文版本。

如果你已经在用 CyberStrikeAI，欢迎体验并反馈：
你最希望插件下一步补齐的能力是什么？我们会优先做“渗透现场最省时间”的那一批。

---

## 项目与交流

* **GitHub**：`https://github.com/Ed1s0nZ/CyberStrikeAI`
* **微信群**：

  ![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33te5KfMdlfXxeKMacdRsPia8Tnlu6QvXS7TE66NicmiaEwIbryS9kpBLTv9hyUCK7icgBJjF0F00UopQHo2TFWEe7uhs1bjn7iby9xc/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/KzNYA6icKe6ny3nDMkDelsYYnPJzRX2erWFEia2S7Bqqc7CjicEpJYQtId7a2jXKCial6Mw8ck8IFQEqmZnldrG2EQ/0?wx_fmt=png)

低调学安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/KzNYA6icKe6ny3nDMkDelsYYnPJzRX2erWFEia2S7Bqqc7CjicEpJYQtId7a2jXKCial6Mw8ck8IFQEqmZnldrG2EQ/0?wx_fmt=png)

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