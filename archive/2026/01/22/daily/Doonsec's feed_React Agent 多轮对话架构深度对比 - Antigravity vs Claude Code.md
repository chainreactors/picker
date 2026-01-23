---
title: React Agent 多轮对话架构深度对比 - Antigravity vs Claude Code
url: https://mp.weixin.qq.com/s/QJHV_RQdWMSjxBeCBkGhtg
source: Doonsec's feed
date: 2026-01-22
fetch_date: 2026-01-23T03:30:23.598644
---

# React Agent 多轮对话架构深度对比 - Antigravity vs Claude Code

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Yhx2OWkuAzULic76Qs7MHlE1oicNrJ5BGCYCjz3z5AKRxzBRzF0V8X7DIFZffvibKtyV2y0MNI2Lf5NjDhZdicaqgw/0?wx_fmt=jpeg)

# React Agent 多轮对话架构深度对比 - Antigravity vs Claude Code

原创

xsser
xsser

xsser的博客

![]()

在小说阅读器中沉浸阅读

# React Agent 多轮对话架构深度对比

## 这是我最近研究agent架构的时候学习的资料，ai生成的，见谅。核心总结就是claude code是react，而antigravity是pdca agent，未来是哲学的天下，你懂的。

## Antigravity (Google DeepMind) vs Claude Code (Anthropic)

摘要

本文深入分析两个前沿 AI 编程助手的 React Agent 多轮对话实现架构：Google DeepMind 的 **Antigravity** 与 Anthropic 的 **Claude Code**。通过对实际 API 流量的逆向分析，揭示两者在请求封装、状态管理、工具调用、思考机制等维度的核心差异。

---

# 一、整体架构概览

## 1.1 核心定位对比

| 维度 | Antigravity (Google) | Claude Code (Anthropic) |
| --- | --- | --- |
| **产品形态** | 桌面应用 (Tauri + Rust) | CLI 工具 (Node.js) |
| **底层模型** | Gemini 系列 | Claude 系列 |
| **API 端点** | `cloudcode-pa.googleapis.com/v1internal` | `api.anthropic.com/v1/messages` |
| **协议风格** | 双层包装结构 | 扁平化直接请求 |
| **状态管理** | 服务端显式状态机 | 客户端隐式累积 |
| **设计哲学** | 「显式协调」 | 「模型智能」 |

## 1.2 架构图解

### Antigravity 请求流

```
```
12345678910111213141516171819flowchart LR    subgraph Client["客户端"]        A[用户输入] --> B[构建 Inner Request]    end
    subgraph Wrapper["包装层"]        B --> C[注入 project/requestId]        C --> D[添加 userAgent/requestType]    end
    subgraph API["v1internal API"]        D --> E[generateContent]        D --> F[streamGenerateContent]    end
    subgraph Response["响应处理"]        E --> G[解包 response 字段]        F --> G        G --> H[提取 candidates]
```
```

### Claude Code 请求流

```
```
202122232425262728293031323334353637flowchart LR    subgraph Client["客户端"]        A[用户输入] --> B[追加到 messages 数组]    end
    subgraph Request["直接请求"]        B --> C[构建扁平化 JSON]        C --> D[添加 metadata]    end
    subgraph API["/v1/messages API"]        D --> E[POST with beta headers]    end
    subgraph Response["SSE 流式响应"]        E --> F[content_block_start]        F --> G[content_block_delta]        G --> H[message_delta]
```
```

---

# 二、请求结构深度解析

## 2.1 Antigravity 双层包装结构

### 2.1.1 外层包装 (Wrapper Layer)

```
```
383940414243{  "project": "aerobic-surf-ss6dt",  "requestId": "agent/1768893140744/45527ef3-be65-47f3-8ca3-1986693dcfbf/3",  "model": "gemini-3-pro-low",  "userAgent": "antigravity",  "requestType": "agent"
```
```

字段解析

* **project**

  : 云项目标识，用于配额和计费隔离
* **requestId**

  : 复合标识符，编码了请求类型、时间戳、会话UUID和轮次号
* **model**

  : 模型选择，支持动态切换
* **userAgent**

  : 固定为 `antigravity`，用于服务端识别
* **requestType**

  : 请求类型 (`agent` / `autocomplete` 等)

### 2.1.2 requestId 结构深度解析

```
```
4445464748agent/1768893140744/45527ef3-be65-47f3-8ca3-1986693dcfbf/3  │        │                    │                         │  │        │                    │                         └── 轮次号 (Turn Number)  │        │                    └── 会话 UUID (Session Identifier)  │        └── Unix 时间戳 (毫秒)
```
```

**设计意图**：

1. **可追溯性**

   ：完整的请求链路可通过 requestId 重建
2. **幂等性**

   ：相同 requestId 可用于重试去重
3. **调试友好**

   ：时间戳和轮次号便于问题定位

### 2.1.3 内层请求 (Inner Request)

```
```
495051525354555657{  "request": {    "contents": [...],          // 多轮对话历史    "systemInstruction": {...}, // 系统指令    "tools": [...],             // 工具声明    "generationConfig": {...},  // 生成配置    "toolConfig": {...},        // 工具配置    "sessionId": "..."          // 会话标识  }
```
```

## 2.2 Claude Code 扁平化结构

### 2.2.1 完整请求示例

```
```
58596061626364656667686970717273{  "model": "claude-opus-4-5-20251101",  "messages": [    {"role": "user", "content": "..."},    {"role": "assistant", "content": "..."}  ],  "system": [    {"type": "text", "text": "You are Claude Code..."},    {"type": "text", "text": "...", "cache_control": {"type": "ephemeral"}}  ],  "tools": [...],  "metadata": {    "user_id": "user_xxx_account_xxx_session_xxx"  },  "max_tokens": 32000,  "stream": true
```
```

### 2.2.2 关键差异点

| 特性 | Antigravity | Claude Code |
| --- | --- | --- |
| 系统指令位置 | `systemInstruction` 对象 | `system` 数组 |
| 缓存控制 | 无显式支持 | `cache_control.type: ephemeral` |
| 用户追踪 | `project` + `requestId` | `metadata.user_id` |
| 流式标识 | URL 参数 `?alt=sse` | JSON 字段 `stream: true` |

---

# 三、多轮对话状态管理

## 3.1 Antigravity: Task Boundary 显式状态机

### 3.1.1 状态机模型

```
```
747576777879808182838485868788899091929394959697stateDiagram-v2    [*] --> NO_TASK: 初始状态    NO_TASK --> PLANNING: task_boundary(PLANNING)    PLANNING --> PLANNING: 更新计划    PLANNING --> EXECUTION: 计划批准    EXECUTION --> EXECUTION: 实现迭代    EXECUTION --> VERIFICATION: 实现完成    VERIFICATION --> EXECUTION: 发现bug    VERIFICATION --> PLANNING: 设计缺陷    VERIFICATION --> [*]: 验证通过
    note right of PLANNING        创建 implementation_plan.md        等待用户审批    end note
    note right of EXECUTION        更新 task.md        执行代码修改    end note
    note right of VERIFICATION        运行测试        创建 walkthrough.md
```
```

### 3.1.2 task\_boundary 工具定义

```
```
9899100101102103104105106107108109110111112113114115116117118119120121122123124125{  "name": "task_boundary",  "description": "Indicate the start of a task or make an update to the current task...",  "parameters": {    "type": "OBJECT",    "properties": {      "TaskName": {        "type": "STRING",        "description": "Name of the task boundary..."      },      "Mode": {        "type": "STRING",        "description": "PLANNING, EXECUTION, or VERIFICATION"      },      "TaskStatus": {        "type": "STRING",        "description": "Active status of the current action..."      },      "TaskSummary": {        "type": "STRING",        "description": "Concise summary of what has been accomplished..."      },      "PredictedTaskSize": {        "type": "INTEGER",        "description": "Estimated tool calls needed..."      }    }  }
```
```

### 3.1.3 Artifact 系统

| Artifact | 路径 | 用途 |
| --- | --- | --- |
| `task.md` | `<appDataDir>/brain/<conversation-id>/` | 任务分解和进度跟踪 |
| `implementation_plan.md` | 同上 | 技术方案设计文档 |
| `walkthrough.md` | 同上 | 完成后的工作总结 |

**task.md 格式示例**：

```
```
126127128129130131132## 用户认证模块实现
- [x] 研究现有认证代码- [/] 实现 JWT 验证中间件  - [x] 创建 middleware 文件  - [ ] 添加 token 解析逻辑- [ ] 编写单元测试
```
```

核心设计理念

Antigravity 将任务管理显式化，通过 artifact 文件和 task\_boundary 工具实现：

1. **可见性**

   ：用户可随时查看任务进度
2. **可控性**

   ：关键节点需要用户审批
3. **可追溯性**

   ：所有决策都有文档记录

## 3.2 Claude Code: 隐式上下文累积

### 3.2.1 对话历史管理

```
```
133134135136137138139140141142143144145146147148149150151152153{  "messages": [    // Turn 1    {"role": "user", "content": "创建一个登录页面"},    {"role": "assistant", "content": [      {"type": "text", "text": "我来帮你创建..."},      {"type": "tool_use", "id": "toolu_xxx", "name": "Write", "input": {...}}    ]},
    // Turn 2 (工具结果)    {"role": "user", "content": [      {"type": "tool_result", "tool_use_id": "toolu_xxx", "content": "文件已创建"}    ]},
    // Turn 3    {"role": "assistant", "content": [      {"type": "text", "text": "登录页面已创建完成..."}    ]},
    // ... 线性累积  ]
```
```

### 3.2.2 状态管理对比

```
```
154155156157158159160161162163164165166167168169170171172flowchart TB    subgraph Antigravity["Antigravity 状态管理"]        A1[用户请求] --> A2{task_boundary?}        A2 -->|是| A3[创建/更新 task.md]        A3 --> A4[执行工具调用]        A4 --> A5[更新 TaskStatus]        A5 --> A6{notify_user?}        A6 -->|是| A7[等待用户审批]        A6 -->|否| A4    end
    subgraph Claude["Claude Code 状态管理"]        C1[用户请求] --> C2[追加到 messages]        C2 --> C3[模型推理]        C3 --> C4{tool_use?}        C4 -->|是| C5[执行工具]        C5 --> C6[tool_result 追加]        C6 --> C3        C4 -->|否| C7[返回响应]
```
```

---

# 四、工具调用机制对比

## 4.1 工具声明格式

### 4.1.1 Antigravity: functionDeclarations

```
```
173174175176177178179180181182183184185186187188189190191192193194195196197198199200201202203{  "tools": [{    "functionDeclarations": [      {        "name": "view_file",        "description": "View the contents of a file...",        "parameters": {          "type": "OBJECT",          "properties": {            "AbsolutePath": {              "type": "STRING",              "description": "Path to file to view..."            },            "StartLine": {              "type": "INTEGER",              "description": "Optio...