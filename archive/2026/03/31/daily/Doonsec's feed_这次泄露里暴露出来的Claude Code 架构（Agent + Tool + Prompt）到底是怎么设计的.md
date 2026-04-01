---
title: 这次泄露里暴露出来的Claude Code 架构（Agent + Tool + Prompt）到底是怎么设计的
url: https://mp.weixin.qq.com/s/9zuBlFdJrSWB4q6yA6klcw
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:43:55.016103
---

# 这次泄露里暴露出来的Claude Code 架构（Agent + Tool + Prompt）到底是怎么设计的

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/316EM2ouicpyhX3iac7MJkpBVnuHXJMtHEcpIWuOd3WeBiaVIaTibDWJN4EhKIynAALIAEIO1XQbqEeLH1PVdgfLibqkwPANUYibo64YlSLibIMQcQ/0?wx_fmt=jpeg)

# 这次泄露里暴露出来的Claude Code 架构（Agent + Tool + Prompt）到底是怎么设计的

王慧敏
王慧敏

AI与代码安全

![]()

在小说阅读器中沉浸阅读

这部分才是这次事件真正“有含金量”的地方：**不是源码本身，而是它暴露了 Claude Code 的 Agent 架构范式**。我给你拆成一个比较清晰的工程视角来看。

# 一、整体架构一句话

Claude Code 的核心可以抽象为：

**LLM（Claude） + Agent Loop + Tool System + Prompt Scaffold**

也就是一个典型的「AI 编程代理（Coding Agent）」系统。

# 二、Agent 主循环（核心骨架）

泄露代码显示，它是一个非常标准的 **ReAct / Tool-using Agent Loop**：

### 2.1 核心流程大概是：

|  |
| --- |
| 用户输入     ↓  构造 Prompt（上下文 + 指令）     ↓  调用 Claude 模型     ↓  解析输出（判断是否调用工具）     ↓  执行 Tool（如读文件 / 写代码 / 执行命令）     ↓  把结果回填到上下文     ↓  继续下一轮 |

本质就是一个循环：

|  |
| --- |
| while (not\_done):      think → act → observe |

这其实和学术里的：

1）ReAct

2）Toolformer

是一脉相承的。

# 三、Tool 系统设计（重点）

Claude Code 的 Tool 设计是这次泄露里最值得看的部分之一。

## 3.1 Tool 抽象结构

每个工具基本是：

|  |
| --- |
| TypeScript  {    name: "read\_file",    description: "...",    input\_schema: {...},    execute: async () => {...}  } |

特点：

1）**强 schema（类似 JSON Schema）**

2）明确输入输出

3）可被模型调用

## 3.2 工具类型（从泄露内容推测）

主要分几类：

### 3.2.1 文件系统类

1）read\_file

2）write\_file

3）list\_directory

用于代码理解 / 修改

### 3.2.2 执行类

1）run\_command（执行 shell）

2）run\_tests

让 AI 能“验证代码”

### 3.2.3分析类

1）search

2）grep / symbol 查找

用于大项目导航

### 3，2，4任务类（高层）

1）plan\_task

2）apply\_patch

这类工具其实已经接近“子 Agent”

## 3.3 Tool 调用方式

模型不会直接输出自然语言，而是类似：

|  |
| --- |
| Josn  {    "tool": "read\_file",    "arguments": {      "path": "src/app.js"    }  } |

然后系统：

1）解析 JSON

2）调用工具

3）把结果喂回模型

# 四、Prompt Scaffold（真正的“灵魂”）

这是很多人低估的部分，但其实是核心竞争力之一。

Claude Code 的 Prompt 不是简单一句话，而是：

## 4.1多层结构 Prompt

大致结构：

|  |
| --- |
| [System Prompt]    - 你是一个代码助手    - 你可以使用工具    - 必须遵循格式     [Tool Definitions]    - 每个工具的说明 + schema     [User Input]     [Context]    - 当前文件    - 历史操作    - 命令输出     [Instructions]    - 输出必须是 JSON / Tool call |

## 4.2强约束输出格式

比如：

1）必须输出 JSON

2）不允许随便解释

3）必须选择 tool 或直接回答

这解决了 LLM 的两个问题：

1）幻觉

2）不可控输出

## 4.3 Planning 提示（关键）

泄露中一个很关键的点是：

模型会被引导：

1）先思考（plan）

2）再执行（act）

类似：

|  |
| --- |
| You should think step by step.  Decide whether to use a tool. |

# 五、上下文管理（Context Engineering）

这是工程上非常关键但容易被忽略的点。

Claude Code 做了几件事：

## 5.1滚动上下文（Sliding Window）

1）保留最近操作

2）丢弃过旧内容

## 5.2结构化上下文

不是简单拼接，而是：

|  |
| --- |
| [File Content]  [Previous Tool Output]  [Errors] |

让模型更容易理解

## 5.3关键状态注入

比如：

1）当前工作目录

2）Git 状态

3）失败日志

# 六、任务拆解（Mini-Agent 结构）

泄露中可以看到一种趋势：

Claude Code 不只是一个 Agent，而是：**Agent + 子任务执行器（pseudo multi-agent）**

例如：

## 6.1一个复杂任务：“修复测试失败”

会被拆成：

1.找失败测试

2.读代码

3.分析原因

4.修改代码

5.重新运行测试

每一步其实都像一个“小 Agent 行为”

# 七、错误恢复机制（很工程化）

Claude Code 有明显的“自愈能力”设计：

## 7.1 当出错时：

1）重新调用模型

2）注入错误信息：

|  |
| --- |
| The previous command failed with:  ...  Fix the issue. |

这就是 AI 能不断迭代修复代码的关键

# 八、和其它 Coding Agent 的对比

你可以把它和几个东西对标：

1）GitHub Copilot

2）OpenAI Codex

3）AutoGPT

Claude Code 的特点是：

**更工程化，而不是更“智能”**

具体表现：

1）Tool schema 很严格

2）Prompt 控制非常强

3）CLI 深度集成开发环境

# 九、核心洞察总结

这次泄露最重要的不是“代码”，而是验证了一件事：

## 9.1 AI Coding Agent 的标准范式已经收敛了：

**1. Agent Loop（ReAct）**

**2. Tool 调用（结构化）**

**3. Prompt Scaffold（强约束）**

**4. Context Engineering（上下文管理）**

**5. Error Recovery（自修复）**

# 十、总结

Claude Code 本质不是“更强的模型”，而是**把 LLM 包装成一个可执行的软件工程系统**。

  【AI代码助手、大模型智能体安全、AI代码静态分析工具、AI动态分析工具、AI渗透测试工具、AI模糊测试、AI恶意代码检测平台、AI软件漏洞挖掘平台、AI软件供应链安全平台。试用及合作请后台私信工程师13381155803（微信同步）】

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