---
title: 生成即安全?——基于hooks的coding agent代码生成安全审计实践
url: https://mp.weixin.qq.com/s/N_uPuJG9nnlMn0d1OTD7Ew
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:49:08.448438
---

# 生成即安全?——基于hooks的coding agent代码生成安全审计实践

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JpU6JH8dicqWww5vUIVibZGia56PlWnu9WmicwB4F3XhP5P2hiapEITgun2wMlp7JicNWqVXG4K5lWaYCkBEEhHXic7jndzpZhcCnkf04mC2QlpDicw/0?wx_fmt=jpeg)

# 生成即安全?——基于hooks的coding agent代码生成安全审计实践

赛博生存指南

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

本文作者信息如下：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/9kb0CP8mQPkibcib22jathc8xPNMeicffPOFVBnTMk2v2sNGXXRWASx2OLogCOMz33CKtQLw1LrQMt9xzQ4Ud55Fg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

P4nY0O

广州大学本科生，主要研究方向为利用大模型技术赋能程序静态分析

个人博客：

https://p4ny0o.top

***Part 0****1***

**背景与动机**

### 1.1 问题：AI 生成代码的安全一致性缺失

大语言模型（LLM）在安全编码能力上**参差不齐**——顶级模型在有明确安全 Prompt 时能写出较安全的代码，但中低端模型、以及在没有显式安全约束的对话中，往往会毫不犹豫地生成`exec(req.query.cmd)`这样的高危代码。即便是同一个强模型，在不同 Prompt 风格、不同上下文长度下，安全行为也会出现漂移。这种不稳定性使得”相信模型能自我保证安全”在工程实践中不可靠。

此外，传统的安全审计发生在 CI/CD 阶段，距离代码生成已经过去了数小时甚至数天，修复成本高、上下文丢失。

### 1.2 目标：“生成即安全”

我们提出一个核心理念：**每一行 AI 生成的代码，在落盘的时候就应完成安全审计**。如果存在漏洞，AI 应当在同一轮对话中自动修复，直到代码通过检测——用户无需介入。

***Part 0****2***

**前置知识**

### 2.1 Claude Code Hook 机制

Claude Code是现今最热门的 AI 编程 CLI 工具，允许 AI 在本地直接读写文件、执行命令。Hook 是其提供的扩展点——可以在 AI 执行特定操作的前后，自动运行用户定义的 shell 命令。这是实现”生成即审计”的关键基础设施。

Hook 通过`.claude/settings.json`（仓库级）或全局配置文件注册。格式如下：

```
{ “hooks”: {   “PostToolUse”: [    {       “matcher”: “Write|Edit”,       “hooks”: [        {           “type”: “command”,           “command”: “node scripts/yasa-hook.js”,           “timeout”: 15        }      ]    }  ],   “Stop”: [    {       “matcher”: “”,       “hooks”: [        {           “type”: “command”,           “command”: “node scripts/yasa-stop-hook.js”,           “timeout”: 30        }      ]    }  ]}}
```

2.2 Hook 事件点

Claude Code 目前支持四类 Hook 事件：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/TwPDxpULgKmykfwTLic49FCgfLReuYJgkicvrhKRokZZmst1T1ELiaCvyFSGiaHU6w92WQrnQPFSDib4WicBjaoseNONO6eJw4iaRQvvJKWPamODCw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

AICG-YASA 使用`PostToolUse`（写文件后立即扫描）和`Stop`（收集超时扫描结果）两个事件点。

### 2.3 Hook 的 I/O

Hook 程序通过**stdin**接收事件 JSON，通过**stdout**返回控制指令

**stdin 输入结构（PostToolUse）**

```
{  "hook_event_name": "PostToolUse",  "tool_name": "Write",  "tool_input": {    "file_path": "/path/to/generated.js",    "content": "..."  },  "tool_response": {},  "session_id": "abc123"}
```

**stdout 输出结构（阻断时）**

```
{  "decision": "block",  "reason": "人类可读的阻断说明",  "hookSpecificOutput": {    "hookEventName": "PostToolUse",    "additionalContext": "注入 Claude 上下文的详细信息"  }}
```

`decision: "block"`会让 Claude Code 终止当前工具调用，并将`additionalContext`注入 AI 的对话上下文——AI 能看到这段文字，并在下一轮自动根据它修复代码。如果 stdout 为空或不含`decision: "block"`，则视为放行。

### 2.4 YASA 静态分析引擎

YASA（Yet Another Static Analyzer）（https://github.com/antgroup/YASA-Engine/）是蚂蚁集团开源的多语言污点分析引擎：

* **基于 UAST 的跨语言 IR**：JavaScript / Java / Go / Python 统一中间表示，分析逻辑与语言语法解耦
* **规则驱动的 Source-Sink 匹配**：规则文件定义哪些是污点源（如`req.query`）、哪些是危险汇聚点（如`child_process.exec`），YASA 在调用图上追踪污点流动路径
* **两种扫描模式**：

+ `--single`：单文件模式，跳过调用图构建，适合对独立文件做快速审计
+ 目录模式（不加`--single`）：构建全局函数调用图（CG），能追踪跨文件的 source→sink 路径

* **SARIF 标准输出**：`report.sarif`符合 SARIF 2.1 规范，包含完整的`codeFlows`（污点传播链）

规则配置示例：

```
[    {      "checkerIds": ["taint_flow_js_input", "taint_flow_express_input"],      "sources": {        "TaintSource": [          { "path": "req.query", "scopeFile": "all", "scopeFunc": "all" },          { "path": "req.body",  "scopeFile": "all", "scopeFunc": "all" }        ]      },      "sinks": {        "FuncCallTaintSink": [          { "args": ["0"], "attribute": "NodejsExec",         "fsig": "child_process.exec" },          { "args": ["0"], "attribute": "NodejsSqlInjection", "fsig": "mysql.query" }        ]      }    }  ]
```

##

***Part 0****3***

**系统架构**

## 3.1 整体流程

![图片](https://mmbiz.qpic.cn/mmbiz_png/TwPDxpULgKloGEMeYVdribia2K8JYkWhYkEleDuaoib4Oy9IBlA4FoXLIJ595ZxD1QBACAbC1hxW4lvBesVYGpRjM0hDVGpTFE7j30j1Wibz8oo/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

### 3.2 核心组件

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/TwPDxpULgKkCZQQJpHmpS4kSXORbWaRAOJFG886FgGPEV7R5KhiaXFfEE03unRSfkEPhEH6VeYbZgicKmjKbpsXWFeFiaf7nMRuRtbpicT7nWxw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

### 3.3 扫描策略决策引擎

`decideScanStrategy()`在 YASA 调用前分析文件特征，选择最合适的扫描策略：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/TwPDxpULgKnqiaNYgh24Bd3zBBAeX0PwYYibAnL6d7t2Awupic9ghuXoaUAO8jMGeBOJsGkkQ3j5uxRJRccYXlkpv8AaXa2TDH2icLiaKNzbm5Xk/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

设计这一分层的原因：带路由的文件（controller 层）本身就是完整的source→sink 路径起点，单文件扫描足够；而纯 service/util 层文件只有 sink，没有 source，单文件扫描会漏报，必须构建跨文件调用图才能追溯到上游路由的用户输入。

### 3.4 超时策略：同步超时转后台异步

在 Claude Code 的交互链路里，`PostToolUse`是用户可感知延迟的一部分。若每次都强制同步等待扫描完成，目录级分析（尤其是 reverse 模式的全局调用图构建）会让 AI 写文件后的响应明显卡顿，甚至中断连续对话体验。

但如果简单地“超时即跳过”，又会丢失本应被检出的漏洞。为同时满足**交互实时性**与**扫描完整性**，系统采用“双通道”策略：

* **前台通道（低延迟）**：同步扫描设置 8 秒上限，确保主交互可控
* **后台通道（保完整）**：超时任务转后台继续执行，结果在后续轮次补报

后台异步流程如下：

1. `PostToolUse`启动同步扫描，并设置 8 秒超时阈值。
2. 若在阈值内完成：直接解析 findings，`0`个问题放行，`>0`个问题立即`decision:block`。
3. 若超过阈值：将同一扫描任务转为后台进程继续运行，并把任务元数据写入`pending-scans.json`；当前 hook 立即`exit 0`，不阻塞本轮生成。
4. Claude 本轮回复结束后触发`Stop`hook：

+ 进程仍在运行：任务保留在队列，等待下一轮
+ 进程已结束且无问题：从队列移除
+ 进程已结束且有问题：输出`decision:block`+`additionalContext`，并移除任务

5. Claude 在下一轮读到补报漏洞后进入自动修复，再次触发同一闭环。

该机制的本质是：**把“是否阻断当前轮”与“是否最终给出安全结论”解耦**。当前轮优先保证可用性，后续轮保证安全性不丢失。

***Part 0****4***

**关键实现代码解析**

## 这一章不再讨论参数细节，而是直接从代码入口看系统如何闭环运行。

### 4.1 PostToolUse 主流程（`scripts/yasa-hook.js`）

主入口是`main()`，核心调用链如下：

```
main├─ readStdin├─ validateFilePath / sanitizeSessionId├─ decideScanStrategy├─ runYasaSync│   ├─ 超时 -> runYasaAsync + enqueuePending│   └─ 完成 -> parseSarif└─ formatFindings -> decision:block(JSON)
```

对应的控制逻辑可以概括为四段：

1. **事件过滤**：只处理`Write`/`Edit`，其他工具事件直接`exit 0`。
2. **策略决策**：`decideScanStrategy()`返回`forward`/`reverse`/`skip`。
3. **扫描执行**：`runYasaSync()`先走同步路径，超时再切`runYasaAsync()`。
4. **结果回注**：`parseSarif()`取 findings，`formatFindings()`组装上下文，返回`decision:block`。

### 4.2 策略引擎代码（`decideScanStrategy`）

`decideScanStrategy(filePath, ruleConfigFile)`是整个闭环的分流器：

* 命中路由特征

  （`app.get`/`router.post`/`@Controller`）→`forward`
* 命中 sink 特征（`exec`/`query`/`eval`等）且无路由 →`reverse`
* 两者都不命中，或属于测试/声明/Hook 脚本 →`skip`

`reverse`分支会调用`findProjectRoot()`向上查找`package.json`，把扫描目标从**当前文件**提升为**项目目录**，让 YASA 在目录级构建完整调用图，再回溯 source→sink 跨文件路径。

从代码结构上看，这是一个典型的**快速路径优先**实现：

* 绝大多数普通文件直接`skip`（零成本）
* 路由文件走`forward`（低成本）
* 只有“疑似危险且缺上下文”的文件才走`reverse`（高成本但高收益）

### 4.3 异步补报代码（`scripts/yasa-stop-hook.js`）

`Stop`hook 对应的主链路是：

```
main├─ readStdin├─ 读取 pending-scans.json├─ isProcessAlive(pid)├─ parseSarif(reportDir)├─ formatFindings└─ decision:block(JSON)
```

它做的事情很纯粹：

1. 遍历`pending-scans.json`队列。
2. 对每个任务先判定进程是否仍在运行：

+ 在运行：继续保留在队列
+ 已结束：解析 SARIF

3. 有 findings 的任务聚合成报告，统一输出一次`decision:block`。
4. 无 findings 的已完成任务直接清理。

这段代码把“超时后扫描结果丢失”的问题补上了：前台没来得及阻断的漏洞，会在后续`Stop`周期里补发给 Claude，并重新进入修复闭环。

### 4.4 两个 Hook 的协作关系

从实现上，`yasa-hook.js`与`yasa-stop-hook.js`形成了一个状态机：

```
[Write/Edit]  ↓PostToolUse(yasa-hook.js)  ├─ findings>0 -> 立即 block  ├─ findings=0 -> 放行  └─ timeout   -> 入队 pending-scans.json                    ↓              Stop(yasa-stop-hook.js)                  ├─ 进程未结束 -> 保留队列                  ├─ 已结束且0问题 -> 清理队列                  └─ 已结束且有问题 -> 补发 block
```

这保证了两个目标同时成立：

* **即时性**：不把所有长扫描都阻塞在当前交互
* **完整性**：超时任务不会被忽略，最终一定被消费并回注结果

### 4.5 代码层面的闭环边界

从这套实现可以看出，闭环边界非常清晰：

* `PostToolUse`负责写入瞬间的首轮判定
* `Stop`负责超时任务的延迟判定
* 两者共同通过
  `decision:block + additionalContext`
  驱动 Claude 自动修复

也就是说，闭环并不依赖模型的自觉，而是依赖 Hook 协议把静态分析结果强制并入模型上下文，形成可重复的工程约束。

***Part 0****5***

**实测：端到端触发验证**

### 5.1 测试用例

我们构造了 4 个典型漏洞场景，由 Claude Code 直接写入磁盘：

![图片](https://mmbiz.qpic.cn/mmbiz_png/TwPDxpULgKnYTkMR2zNo6h1nOYHSPpYaRkcoE2fryMYFtwOfBRF6FOpRDwRfGibKXIQYmTmOPsyV7G4huVAAXw9gqr7F1ibduG5Huib11xZdfk/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

### 5.2 Hook 日志

```
[2026-04-20T15:09:18] STRATEGY: vuln-cmd-injection.js → mode=forward (检测到路由注册，正向扫描)  [2026-04-20T15:09:18] SCAN: vuln-cmd-injection.js [javascript] mode=forward  [2026-04-20T15:09:22] DONE: vuln-cmd-injection.js → 2 个问题
...