---
title: DeepAudit——代码漏洞挖掘多智能体ai系统
url: https://mp.weixin.qq.com/s/wXYL-QvkaZHnKKfDxUUOgQ
source: Doonsec's feed
date: 2026-01-20
fetch_date: 2026-01-21T03:31:13.585828
---

# DeepAudit——代码漏洞挖掘多智能体ai系统

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AGUhPQZ04zxjcPMwAR6h5xiacWdZZzoo5X8ywgZORy91PB4RXP6GQLxZ2WWWaXTduu0C9dDJIwCZOO35OfGEMMQ/0?wx_fmt=jpeg)

# DeepAudit——代码漏洞挖掘多智能体ai系统

原创

一个人挺好
一个人挺好

一个人挺好 wa

![]()

在小说阅读器中沉浸阅读

# 项目地址

https://github.com/lintsinghua/DeepAudit

# 项目概述

DeepAudit是一个基于 Multi-Agent 协作架构的下一代代码安全审计平台，旨在通过人工智能自动化漏洞挖掘流程。该项目是国内首个开源的代码漏洞挖掘多智能体系统，已成功发现 48 个 CVE 漏洞，覆盖 16 个知名开源项目。

![Agent审计入口](https://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zxjcPMwAR6h5xiacWdZZzoo5QOuzxXNFYR3gbL5ibYiaOBgbOdkquggvA2ibVibWcCl3ia0ajiaA0aciaK8EA/640?wx_fmt=png&from=appmsg)

![审计流日志](https://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zxjcPMwAR6h5xiacWdZZzoo5A6quib8VdYdQHNjGZwVDuEPl1xTUhiah4LibjWye3NAF3f8iaHFg0Vj6pg/640?wx_fmt=png&from=appmsg)

![仪表盘](https://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zxjcPMwAR6h5xiacWdZZzoo5H0VH8riaSgfqQ0vTbgugDC1e4xdXMbrJ3xZxzgHyytKK419qVRgnVtw/640?wx_fmt=png&from=appmsg)

![即时分析](https://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zxjcPMwAR6h5xiacWdZZzoo5jic5pOxp5gP26CA5DxwLcsVVFicT7tsujN4uGkEiatMfOKbd1d51chGjQ/640?wx_fmt=png&from=appmsg)

![项目管理](https://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zxjcPMwAR6h5xiacWdZZzoo512CfIlloTJuI5tOhkmaP2CMa1Hdn84pQhiboIw8UwQ2xDGzRBVV4wzg/640?wx_fmt=png&from=appmsg)

项目核心理念是"让 AI 像黑客一样攻击，像专家一样防御"，通过模拟安全专家的思维方式，解决传统 SAST 工具的三大痛点：

高误报率（缺乏语义理解）

业务逻辑盲点（无法理解跨文件调用）

缺乏验证手段（无法确认漏洞可利用性）

---

# 核心架构

## 系统架构图

DeepAudit 采用微服务架构，核心由 Multi-Agent 引擎驱动，包含四个专用智能体：

┌─────────────────────────────────────────────────────────────┐

│                     User Interface                          │

│                    (React + TypeScript)                     │

└─────────────────────────────────────────────────────────────┘

│

▼

┌─────────────────────────────────────────────────────────────┐

│                    FastAPI Backend                          │

│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐ │

│  │Orchestrat│  │  Recon   │  │ Analysis │  │Verification│ │

│  │  or Agent│◄─┤  Agent   │◄─┤  Agent   │◄─┤   Agent  │ │

│  │          │  │          │  │          │  │          │ │

│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘ │

│       │             │             │             │        │

│       └─────────────┴─────────────┴─────────────┘        │

│                     RAG + LLM Service                     │

│                      (ChromaDB)                           │

└─────────────────────────────────────────────────────────────┘

│

▼

┌─────────────────────────────────────────────────────────────┐

│               Docker Sandbox Environment                    │

│            (Automated PoC Testing & Validation)             │

└─────────────────────────────────────────────────────────────┘

# Multi-Agent 工作流

## 表格

| 步骤 | 阶段 | 负责 Agent | 主要动作 |
| --- | --- | --- | --- |
| 1 | 策略规划 | **Orchestrator** | 分析项目类型，制定审计计划，分发任务 |
| 2 | 信息收集 | **Recon Agent** | 扫描项目结构，识别技术栈，提取攻击面 |
| 3 | 漏洞挖掘 | **Analysis Agent** | 结合 RAG 知识库与 AST 分析，深度审查代码 |
| 4 | PoC 验证 | **Verification Agent** | 编写并执行 PoC 脚本，Docker 沙箱中验证 |
| 5 | 报告生成 | **Orchestrator** | 汇总结果，剔除误报，生成专业审计报告 |

---

# 技术栈

## 后端技术栈

框架: Python FastAPI + Uvicorn

Multi-Agent: LangGraph + LangChain

向量数据库: ChromaDB (RAG 知识库)

AST 解析: Tree-sitter (支持 10+ 语言)

任务队列: Celery + Redis

数据库: PostgreSQL 15+

## 前端技术栈

框架: React 18 + TypeScript

构建工具: Vite

样式: TailwindCSS + shadcn/ui

状态管理: Zustand

图表: Recharts

## 部署技术

容器化: Docker + Compose

沙箱: 隔离 Docker 容器

镜像仓库: GitHub Container Registry (ghcr.io)

---

# 支持的漏洞类型

## 表格

| 类型 | 描述 | 危害等级 |
| --- | --- | --- |
| `sql_injection` | SQL 注入 | 严重 |
| `xss` | 跨站脚本攻击 | 中等 |
| `command_injection` | 命令注入 | 严重 |
| `path_traversal` | 路径遍历 | 中等 |
| `ssrf` | 服务端请求伪造 | 严重 |
| `xxe` | XML 外部实体注入 | 严重 |
| `insecure_deserialization` | 不安全反序列化 | 严重 |
| `hardcoded_secret` | 硬编码密钥 | 中等 |
| `weak_crypto` | 弱加密算法 | 中等 |
| `authentication_bypass` | 认证绕过 | 严重 |
| `authorization_bypass` | 授权绕过 | 严重 |
| `idor` | 不安全直接对象引用 | 中等 |

---

# LLM 平台支持

## 国际平台

OpenAI: GPT-4o / GPT-4 / GPT-3.5

Anthropic: Claude 3.5 Sonnet / Opus

Google: Gemini Pro

## 国内平台

阿里: 通义千问 Qwen

智谱: GLM-4

月之暗面: Kimi

百度: 文心一言

字节: 豆包

## 本地部署（支持 Ollama）

Llama3(8B/70B)

Qwen2.5(7B/14B/32B)

DeepSeek-Coder(6.7B/33B)

CodeLlama(7B/13B)

API 中转支持: 支持自定义 API Base URL，解决网络访问限制

---

# 部署方案

## 方案一：生产环境一键部署（推荐）

bash

# 标准部署

curl-fsSLhttps://raw.githubusercontent.com/lintsinghua/DeepAudit/v3.0.0/docker-compose.prod.yml|dockercompose-f- up-d

# 国内加速（南京大学镜像站）

curl-fsSLhttps://raw.githubusercontent.com/lintsinghua/DeepAudit/v3.0.0/docker-compose.prod.cn.yml|dockercompose-f- up-d

访问地址:http://localhost:3000

## 方案二：源码开发部署

bash

# 1. 克隆代码

gitclone https://github.com/lintsinghua/DeepAudit.git&&cdDeepAudit

# 2. 配置环境变量

cpbackend/env.example backend/.env

# 编辑 .env 文件，配置 LLM API Key

# 3. 启动服务

dockercompose up-d

## 方案三：源码本地开发

环境要求:

Python 3.11+

Node.js 20+

PostgreSQL 15+

Docker (用于沙箱)

启动步骤:

bash

# 启动数据库

dockercompose up-dredis db adminer

# 后端开发

cdbackend

uvsync

source.venv/bin/activate

uvicorn app.main:app--reload

# 前端开发

cdfrontend

pnpminstall

pnpmdev

# 沙箱镜像

dockerpull ghcr.io/lintsinghua/deepaudit-sandbox:latest

---

# 核心功能矩阵

## 表格

| 功能模块 | 技术实现 | 描述 |
| --- | --- | --- |
| **Multi-Agent 审计** | LangGraph 状态机 | 自主编排审计策略，Agent 间协作 |
| **RAG 知识增强** | ChromaDB + Embeddings | 代码语义理解，CWE/CVE 知识检索 |
| **沙箱 PoC 验证** | Docker 隔离 + 动态执行 | 自动生成并执行攻击脚本 |
| **项目管理** | Git/API/ZIP 导入 | 支持 GitHub/GitLab/Gitea |
| **即时分析** | 代码片段快速扫描 | 粘贴代码秒级分析 |
| **五维检测** | 规则引擎 + AI | Bug/安全/性能/风格/可维护性 |
| **What-Why-How** | LLM 解释生成 | 漏洞定位 + 原因分析 + 修复建议 |
| **报告导出** | PDF/Markdown/JSON | 一键生成专业审计报告 |
| **运行时配置** | Web UI 动态配置 | 无需重启服务切换 LLM |

---

# 配置说明

## 环境变量配置 (backend/.env)

bash

# LLM API 配置

OPENAI\_API\_KEY=sk-xxx

ANTHROPIC\_API\_KEY=sk-ant-xxx

DEEPSEEK\_API\_KEY=sk-xxx

# 数据库配置

DATABASE\_URL=postgresql://user:pass@localhost:5432/deepaudit

# 沙箱配置

SANDBOX\_IMAGE=ghcr.io/lintsinghua/deepaudit-sandbox:latest

SANDBOX\_TIMEOUT=300

# RAG 配置

CHROMA\_PERSIST\_DIR=./chroma\_db

EMBEDDINGS\_MODEL=text-embedding-3-small

## 前端配置 (frontend/.env)

bash

VITE\_API\_URL=http://localhost:3000

VITE\_WS\_URL=ws://localhost:3000

---

# API 接口参考

## 核心 REST API 端点

http

# 项目管理

POST   /api/projects

# 创建项目

GET    /api/projects/{id}

# 获取项目详情

POST   /api/projects/{id}/scan

# 启动审计任务

# Agent 审计

POST   /api/agent/audit

# 启动 Multi-Agent 审计

GET    /api/agent/status/{task\_id}

# 获取审计状态

GET    /api/agent/logs/{task\_id}

# 获取审计日志

# 即时分析

POST   /api/analysis/code

# 代码片段分析

POST   /api/analysis/file

# 文件上传分析

# 报告

GET    /api/reports/{project\_id}

# 获取审计报告

POST   /api/reports/export

# 导出报告 (PDF/MD/JSON)

## WebSocket 实时通信

JavaScript

// 连接审计日志实时推送

constws=newWebSocket('ws://localhost:8000/ws/agent/{task\_id}');

ws.onmessage=(event)=>{

constlog=JSON.parse(event.data);

console.log(`[${log.agent}]${log.message}`);

};

---

# 沙箱安全机制

## 隔离策略

Docker 容器隔离: 每个 PoC 在独立容器中运行

资源限制: CPU/Memory 配额限制

网络隔离: 沙箱内禁止外网访问（SSRF 测试除外）

文件系统: 只读挂载，防止逃逸

## 验证流程

Verification Agent 生成 PoC 脚本

沙箱动态构建目标应用环境

在隔离环境中执行攻击脚本

捕获响应/异常，验证漏洞存在性

失败时自动修正 PoC 并重试（最多 3 次）

---

# 性能指标

并发审计: 支持多项目并行扫描

响应时间: 代码片段分析 < 5 秒

Agent 循环: 平均 3-5 轮完成深度审计

PoC 成功率: > 85%（常见漏洞类型）

误报率: < 15%（相比传统 SAST 降低 60%）

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zyTvSBegohhPkdl4ZiaID39hGjT55M6GNVWWYfpt8Q146OaDEU4xQ0E4VtxLO4zfGia16VE6qHb001g/0?wx_fmt=png)

一个人挺好 wa

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zyTvSBegohhPkdl4ZiaID39hGjT55M6GNVWWYfpt8Q146OaDEU4xQ0E4VtxLO4zfGia16VE6qHb001g/0?wx_fmt=png)

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