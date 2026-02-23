---
title: Phantom TrojanWalker——AI 恶意软件自动化分析平台
url: https://mp.weixin.qq.com/s/hmxfMk-3uIohed4Jq8YHZQ
source: Doonsec's feed
date: 2026-02-22
fetch_date: 2026-02-23T04:15:38.772070
---

# Phantom TrojanWalker——AI 恶意软件自动化分析平台

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qqiaD4wiajgFxBHueHjlyoeDg2ao4FoUTRyKP0Kh4PdfG9EcVP5EAvOibpgic7JBdktSsNxsLG4jam3RG8iadzmGTZ84KmkwmlCPupB1ICaVwQL8/0?wx_fmt=jpeg)

# Phantom TrojanWalker——AI 恶意软件自动化分析平台

一个人挺好
一个人挺好

一个人挺好 wa

![]()

在小说阅读器中沉浸阅读

# 项目地址

https://github.com/MICHAEL-888/Phantom\_TrojanWalker

#

# Phantom TrojanWalker - AI 恶意软件自动化分析框架

Phantom TrojanWalker 是一个模块化的二进制分析与威胁检测平台，串联 Ghidra 静态分析、LLM 结构化研判与任务化后端，实现从样本上传到报告生成的自动化流水线。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFx0xlHOBvLhGCYUJCJTDYdfgfwRTVPaRk0hic9SFtcg9OoFUQFRzZ2kaIPoWaoicSwtgoliavMkJEqwvuL5A0JzbWxnrh7V5icrKc4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFwLYMaTRwEibeuMyEYVcb7wsPWUtFMicht8QhcrtFjgXgWeK5uSeF9FT99M9rp1X0CAAl9QtL73eOK24N73G9uf24beNriaIibAhjc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFxnrRlHYCo197XWSpehNNiarcXRLTsrx0PBzRcbN2GMTAq5ibZNOSXdx5wByejNoUXUUaMfR4UcKfia0aDfr4lrnlcUNAhmgKDZI4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFw7ibgeXkhKt7QklFiao2EQCluZKDJibg2q8icKnZmHspvcv6osnSMUU5QnQiaCXk5uoR9F4ml5oxohknzgUByDUXfZQRnxdFaQOWiaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFziaiaGd9QJSOJV46zc04Ircgovsjg830SA4Cvbs3TUEgQZYvLRUFe7JVE5QVPegkrk3UecAnmCFFVOMrgsfAa5hWibjNaBbvFx9M/640?wx_fmt=png&from=appmsg)

**Phantom\_TrojanWalker** 是一个模块化的二进制分析与威胁检测平台，专为恶意软件自动化分析而设计。该平台串联 Ghidra 静态分析引擎、大语言模型（LLM）结构化研判与任务化后端，实现从样本上传到报告生成的全流程自动化分析。

### 1.1 核心定位

* **目标**：自动化恶意软件分析与威胁检测
* **技术路线**：静态分析 + AI 研判 + 任务编排
* **应用场景**：安全研究、威胁情报、恶意软件样本分析

---

## 2. 系统架构

### 2.1 整体架构图

```
┌─────────────────────────────────────────────────────────────┐
│                        用户交互层                            │
│  (Web 界面 / API 接口 / 样本上传)                            │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                      任务调度层                              │
│  (任务队列 / 工作流编排 / 状态管理)                          │
└──────────────────────┬──────────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
┌───────▼──────┐ ┌────▼─────┐ ┌──────▼───────┐
│  静态分析引擎 │ │ LLM研判  │ │  报告生成    │
│  (Ghidra)   │ │  模块    │ │   引擎       │
└─────────────┘ └──────────┘ └──────────────┘
```

### 2.2 核心组件

表格

| 组件 | 功能 | 技术栈 |
| --- | --- | --- |
| **样本管理模块** | 接收、存储、预处理待分析样本 | Python / REST API |
| **Ghidra 分析引擎** | 二进制反编译、控制流分析、函数识别 | Ghidra / Java / SRE |
| **LLM 研判模块** | 恶意行为识别、威胁分类、风险评估 | GPT-4 / Claude / 本地模型 |
| **任务调度系统** | 异步任务队列、并发控制、状态追踪 | Celery / Redis / RabbitMQ |
| **报告生成器** | 结构化报告输出、IOC提取、可视化展示 | Markdown / JSON / PDF |

---

## 3. 核心功能模块

### 3.1 静态分析引擎（基于 Ghidra）

**功能特性：**

* **自动反编译**：支持 x86/x64/ARM 架构的二进制文件
* **控制流图（CFG）生成**：提取程序执行路径
* **函数识别与标注**：自动识别入口点、导出函数、回调函数
* **字符串提取**：扫描硬编码的 IP、URL、文件路径、注册表项
* **导入表分析**：识别 API 调用模式（文件操作、网络通信、注册表操作）

**分析流程：**

1. 样本上传 → 格式识别（PE/ELF/Mach-O）
2. Ghidra Headless 模式启动分析
3. 生成反编译代码与中间表示（P-Code）
4. 提取特征向量供 LLM 研判

### 3.2 LLM 结构化研判模块

**研判维度：**

* **恶意行为分类**：木马、勒索软件、间谍软件、挖矿程序等
* **攻击技术映射**：MITRE ATT&CK 框架映射
* **威胁等级评估**：Critical / High / Medium / Low
* **IOC 提取**：C2 地址、文件名、互斥体、注册表键值

## 目录结构

```
├── agents/             # AI 编排层（Coordinator / GhidraClient / Prompts）
├── backend/            # API + 任务系统 + SQLite
├── frontend/           # React 前端看板
├── module/             # ghidra_pipe + ghidra_mcp
├── data/               # 上传文件与任务数据
└── docker-compose.yml  # 一键启动
```

## 环境准备

* **Python**

  : 3.10+
* **Node.js**

  : 18+
* **Ghidra**

  : 12.0+（Docker 内置或本地安装）
* **JDK**

  : 21+

## 配置

1. 复制配置模板：

```
cd agentscp config.yaml.example config.yaml
```

2. 编辑 `agents/config.yaml`，至少配置 LLM 与 Ghidra 地址：

```
plugins:  ghidra:    base_url: "http://ph_ghidra:8000"    endpoints:      health_check: "/health_check"      upload: "/upload"      analyze: "/analyze"      metadata: "/metadata"      functions: "/functions"      strings: "/strings"      callgraph: "/callgraph"      decompile: "/decompile"      decompile_batch: "/decompile_batch"      xrefs: "/xrefs"      xrefs_batch: "/xrefs_batch"  mcp:    base_url: "http://ph_ghidra:9000/mcp"    endpoints: {}FunctionAnalysisAgent:  system_prompt: ""  system_prompt_path: "prompt/FunctionAnalysisAgent.md"  llm:    model_name: deepseek-reasoner    temperature: 0    api_key: "YOUR_API_KEY_HERE"    base_url: "https://api.deepseek.com/chat/completions"    extra_body: {}    max_retries: 3    timeout: 120    max_completion_tokens: 32768    max_input_tokens: 131072  rate_limit:    requests_per_second: 10    check_every_n_seconds: 0.1    max_bucket_size: 10MalwareAnalysisAgent:  system_prompt: ""  system_prompt_path: "prompt/MalwareAnalysisAgent.md"  llm:    model_name: deepseek-reasoner    temperature: 0    api_key: "YOUR_API_KEY_HERE"    base_url: "https://api.deepseek.com/chat/completions"    extra_body: {}    max_retries: 3    timeout: 600    max_completion_tokens: 32768    max_input_tokens: 131072  rate_limit:    requests_per_second: 10    check_every_n_seconds: 0.1    max_bucket_size: 10
```

修改 prompt 或 config 后，需要重启 backend/worker 生效。

## 快速启动

### 方式 A：Docker Compose（推荐）

```
docker compose up --build
```

默认端口：Ghidra `127.0.0.1:8000`、Backend `127.0.0.1:8001`（`/api`）、Frontend `127.0.0.1:8080`、Ghidra MCP `127.0.0.1:9000`

### 方式 B：纯本地（开发调试）

按顺序启动：

```
# Step 1: Ghidra 引擎export GHIDRA_INSTALL_DIR=/path/to/ghidrapython module/ghidra_pipe/main.py# Step 2: Backend + Workerpython backend/main.py# Step 3: Frontendcd frontendnpm installnpm run dev
```

访问：`http://localhost:5173`

## 常用环境变量

* `PTW_GHIDRA_BASE_URL`

  ：覆盖 `agents/config.yaml` 中的 `plugins.ghidra.base_url`
* `PTW_MCP_BASE_URL`

  ：覆盖 MCP 地址
* `PTW_MAX_UPLOAD_BYTES`

  ：最大上传大小（默认 200MB）
* `PTW_CORS_ORIGINS`

  ：后端允许的跨域来源（逗号分隔）
* `BACKEND_HOST`

  / `BACKEND_PORT`：后端监听地址与端口
* `GHIDRA_INSTALL_DIR`

  ：本地 Ghidra 安装目录

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