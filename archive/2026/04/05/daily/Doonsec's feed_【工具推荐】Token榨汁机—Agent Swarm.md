---
title: 【工具推荐】Token榨汁机—Agent Swarm
url: https://mp.weixin.qq.com/s/fL5g_33O1Jiw0y1H19OUTw
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:43:27.615505
---

# 【工具推荐】Token榨汁机—Agent Swarm

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JpU6JH8dicqUoo654bia30iadTDgUI5TUmat0gg2UTYiateW2jnVkn4MaTyCDn0T8oFPnxdpt0vkfzw28mt8ibAESUibciaiawC7F3sKaanJ2ujIhaw/0?wx_fmt=jpeg)

# 【工具推荐】Token榨汁机—Agent Swarm

原创

mimi3389
mimi3389

赛博生存指南

![]()

在小说阅读器中沉浸阅读

> 和很多朋友一样，我也有Token空闲焦虑症。怎么才能快速消耗Token 呢?调研了一些 Agent 框架和方案，毕竟Agent Swarm 是未来发展方向之一。

## Claude Code Agent Swarm 工具推荐(Grok生成)

### 01｜官方 Agent Teams

**怎么启用**：设置环境变量 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`（或写进 `settings.json`）。
**用法**：直接在 Claude Code 里说「Create an agent team...」或「用 swarm 模式帮我做...」，Lead 就会自动 spawn 多个 Teammate。

**亮点**

* • 内置任务列表（Task List）
* • Mailbox 互相发消息
* • Plan Approval 审批流程
* • Hooks 自定义流程

地址：官网文档 →

### 02｜ clnode（解决上下文爆炸神器）

**核心功能**：用 Claude Code 自己的 Hook 系统 + DuckDB 做共享内存层。子代理完成任务后自动总结存入 DB，其他代理自动拉取相关上下文，Leader 不会被中间结果淹没。
**安装**：超级简单，一行命令：

```
npx clnode init .
```

或让 Claude 自己安装。

* • Kanban 看板
* • Token 统计
* • Review Loop 防无限循环

**社区评价**：目前最受欢迎的 swarm 插件之一。地址：SierraDevsec/clnode

### 03｜【推荐】claude-flow / ruflo（企业级 swarm 编排平台）

**功能**：在 Claude Code 之上加一层智能协调，支持分布式 swarm、智能体 76+ 个、150+ 命令、RAG、MCP 深度集成。

**模式**

| 模式 | 特点 | 适用场景 |
| --- | --- | --- |
| swarm | 快速、单任务导向 | 短期任务 |
| hive-mind | 持续协作、复杂项目管理 | 长期项目 |

**安装**：npm 安装后几条命令就能跑。地址：ruvnet/ruflo。

### 04｜ClawTeam（开源多代理编排框架）

**功能**：兼容 Claude Code + Codex + 其他 CLI Agent，自动 spawn、任务分配、Git 集成。

**亮点**：

* • 支持 tmux
* • Docker 部署
* • 适合本地/团队部署

HKUDS/ClawTeam

### 05｜claude-sneakpeek（解锁隐藏 Swarm 高级功能）

解锁官方还没完全公开的动态子代理生成、更多 swarm 模式。
地址：mikekelly/claude-sneakpeek

### 06｜【推荐】oh-my-claudecode（解锁隐藏 Swarm 高级功能）

oh-my-claudecode（全称 Oh My Claude Code），它就是一个专为 Claude Code 打造的多代理编排框架（Multi-agent Orchestration Layer）。19+ 专业子代理（架构师、执行者、调试器、测试工程师、安全审查等）自动协作。零配置：自然语言驱动，不用学任何命令。

5 种执行模式（最推荐 Team Mode）：

* Team（推荐）：规划 → PRD → 执行 → 验证 → 自动修复循环（全自动）
* Autopilot：完全自主端到端开发
* Ralph：持久化 + 超强并行
* 支持 Claude + Codex + Gemini 混合团队

快速上手：

```
/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode/plugin install oh-my-claudecode/omc-setup
```

## 【好玩的 GUI 多 Agent 工具】 Golutra

在官方方案之外，**Golutra** 提供了有趣的Agent集群实现方式。

**核心特性**：支持多种平台 Gemini Cli\CodeX\Claude Code\opencode\Qwen Code\OpenClaw\Terminal 等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JpU6JH8dicqWzZic58QzlFN5JGBntG8ZOvE9bibtoibDJs9a5KARgibkvthpvxfSI3icibz82Ox9gstqQJHSfKbAydBvaibKSYAk0Ujaic8c7eumgMh8/640?wx_fmt=png&from=appmsg)

Golutra 目前处于活跃迭代期，GitHub 社区反馈积极。开发者SeekSky之前还在bilibili开展直播7\*24h直播，但是被官方封了（Orz）。

地址：https://github.com/golutra/golutra

![](https://mmbiz.qpic.cn/mmbiz_png/JpU6JH8dicqWPthLqDAoYDKs20BK8YbMFibNw1EaLiaP4ibX1w6chOiaQNIgK64e0Xvw51iatgmFh7ebAno7hDpqwDqkmBTOJ9kakhGJkIGLP3u34/640?wx_fmt=png&from=appmsg)

## 个人LLM模型实测感受

博主开了质谱、MiniMax、Kimi的Coding Plan，有朋友问我哪个好用，我个人使用习惯如下：

| 模型 | 优势场景 | 注意事项 |
| --- | --- | --- |
| **GLM 5.1** | 主力模型，春节买的很划算（Compose 1 基于 GLM ） | 老问题卡少，下午有点卡 |
| **Kimi-2.5** | 基于GLM和MinMax之间？可能是我主用GLM？（Compose 2 基于 Kimi） | Moderato 不够用 |
| **MiniMax-2.7** | 量大管饱 | 代码质量不如前两者 |

个人感觉，ClaudeCode 像3D打印机，然后 cursor 做美工刀，可以用来细化细节。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/W8BrFJicfTaicbd7kn2cZBgNIaLlk75yrMSYaKQVkia524P5J7BoEBsYWI1XEWOXqDdmMcIzOYWZAiaTaqoSuvZXfg/0?wx_fmt=png)

赛博生存指南

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/W8BrFJicfTaicbd7kn2cZBgNIaLlk75yrMSYaKQVkia524P5J7BoEBsYWI1XEWOXqDdmMcIzOYWZAiaTaqoSuvZXfg/0?wx_fmt=png)

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