---
title: Hermes Agent：会成长的AI助手
url: https://mp.weixin.qq.com/s/YcXZQkPcUlJmdasO3SlebQ
source: Doonsec's feed
date: 2026-04-08
fetch_date: 2026-04-09T04:27:21.951363
---

# Hermes Agent：会成长的AI助手

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/CBe66ugaImlPWUfIUjgricr5FvFa9lNicAiau6xiamaC4euvaiba16EXnCPLibeJibk9A2v79zg8445OTI3iaY0EQeF9v9u4h2vGCicXyGQY0cg7gLdU/0?wx_fmt=jpeg)

# Hermes Agent：会成长的AI助手

AI助手
AI助手

爱唠叨的Nil

![]()

在小说阅读器中沉浸阅读

#

> 「不是被束缚在 IDE 里的编程助手，也不是某个 API 的聊天外壳。这是一个真正自主的 Agent，它住在你的服务器上，记住它学到的一切，并且运行越久越强大。」

---

## 什么是 Hermes Agent？

   由 **Nous Research** 团队打造的 Hermes Agent，是一款真正意义上的**自我进化型 AI Agent**。

   它不是那种用完即走的聊天机器人，而是一个可以长期运行、持续学习、不断成长的智能助手。就像一位越相处越了解你的伙伴，Hermes 会在每次对话中加深对你的理解，逐步构建起属于你们的协作默契。

---

## 六大核心特性，重新定义 AI 助手

### 1    真正的学习闭环

   Hermes 是目前唯一具备**内置学习循环**的 Agent：

* **自主技能创建** —— 完成复杂任务后，自动提炼为可复用技能
* **技能自我优化** —— 在使用过程中不断改进技能效果
* **智能记忆管理** —— 主动提醒自己持久化重要知识
* **跨会话搜索** —— 基于 FTS5 全文检索，快速找回过往对话
* **用户画像建模** —— 建立深度用户理解模型

### 2    多平台无缝切换

   无论你习惯用哪个平台，Hermes 都能随时响应：

**Telegram** · **Discord** · **Slack** · **WhatsApp** · **Signal** · **Email** · **CLI**

   在一个平台开始对话，在另一个平台继续，全程无缝衔接。还支持语音消息转录，让沟通更加自然。

### 3    模型自由选择，拒绝锁定

   Hermes 支持接入几乎所有主流大模型：

**Nous Portal** · **OpenRouter** (200+ 模型) · **Kimi/Moonshot** · **MiniMax** · **GLM** · **OpenAI** · **Anthropic**

   一条命令切换模型：`hermes model`，无需修改任何代码。

### 4    定时自动化任务

   用自然语言设置定时任务，就像和朋友聊天一样简单：

> "每天早上 9 点给我发送昨日新闻摘要"
>
> "每周五下午生成本周工作报告"
>
> "每月 1 号备份项目数据"

   内置 Cron 调度器，任务会在后台自动运行，并通过你选择的平台推送结果。

### 5    子代理并行处理

   遇到复杂任务？Hermes 可以**生成隔离子代理**，每个子代理拥有独立的对话、终端和 Python RPC 脚本。

   多步骤流水线被压缩为零上下文成本的单次调用，效率倍增。

### 6    真正的沙箱环境

   提供五种运行后端，满足不同安全需求：

| 后端 | 适用场景 |
| --- | --- |
| Local | 本地快速测试 |
| Docker | 容器化隔离 |
| SSH | 远程服务器 |
| Singularity | HPC 环境 |
| Modal | 无服务器，按需计费 |

   Daytona 和 Modal 还支持**无服务器持久化**——空闲时休眠，唤醒时恢复，成本极低。

---

## 一分钟快速上手

   安装只需一条命令：

`curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash`

   支持 Linux、macOS 和 WSL2，安装器会自动处理 Python、Node.js 和所有依赖。

   安装完成后：

`source ~/.bashrc # 重新加载 shell`
   `hermes # 开始对话！`

   常用命令速查：

`hermes setup` — 完整配置向导

`hermes model` — 选择模型

`hermes tools` — 配置工具

`hermes gateway` — 启动消息网关

---

## 适用场景

#### 个人用户

* 智能日程管理助手
* 个性化知识库问答
* 自动化信息收集与整理

#### 开发者

* 代码审查与优化建议
* API 文档智能查询
* 自动化测试与部署

#### 团队/企业

* 多平台统一客服入口
* 定时报告自动生成
* 跨平台协作流程自动化

---

## 开源与社区

   Hermes Agent 采用 **MIT 协议**完全开源：

🔗 **GitHub**: github.com/NousResearch/hermes-agent

📖 **文档**: hermes-agent.nousresearch.com/docs

💬 **Discord**: discord.gg/NousResearch

   无论你是想深度定制，还是只想开箱即用，Hermes 都能满足你的需求。

---

## 写在最后

   在 AI 工具层出不穷的今天，Hermes Agent 选择了一条不同的路——**不是做最强大的模型，而是做最懂你的 Agent**。

   它不会用完即走，而是会记住你的偏好、理解你的项目、积累你们的共同经验。每一次对话，都是在为下一次更好的协作做准备。

   如果你也在寻找一个真正**会成长**的 AI 助手，不妨试试 Hermes。

> 因为最好的工具，应该越用越顺手。

---

本文部分内容参考 Hermes Agent 官方文档

项目由 Nous Research 团队开发维护

预览时标签不可点

阅读原文

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