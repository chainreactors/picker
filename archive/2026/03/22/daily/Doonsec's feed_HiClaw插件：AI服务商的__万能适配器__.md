---
title: HiClaw插件：AI服务商的\"万能适配器\"
url: https://mp.weixin.qq.com/s/0f_H3QWDNUeCSuhweXCHpA
source: Doonsec's feed
date: 2026-03-22
fetch_date: 2026-03-23T04:19:55.500755
---

# HiClaw插件：AI服务商的\"万能适配器\"

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CBe66ugaImkx12v8FgyBWlX2eAZ6YQh6loPVKV1fnPibcficWqEKxzcOHWKSVnb9ISLApMYbYKZFLE8NVCCjxBXlh7KWOeSaDyic2L9RCS8Zbk/0?wx_fmt=jpeg)

# HiClaw插件：AI服务商的"万能适配器"

原创

Agent-阿刁
Agent-阿刁

爱唠叨的Nil

![]()

在小说阅读器中沉浸阅读

# 项目简介

HiClaw 是一个企业级 AI Agent 协作平台，基于 Apache 2.0 协议开源，由 Higress 团队构建。它通过集成 Matrix 即时通讯协议、Higress AI Gateway、OpenClaw 智能体框架以及 MinIO 共享文件系统，实现了多 AI 智能体 (Agents) 在人工监督下的安全、透明与高效协同工作。

## 核心架构与组件

HiClaw 系统主要由 Manager 容器 和多个 Worker 容器 构成。

### Manager 容器

作为系统的控制中心，集成了以下核心服务：

• Higress AI Gateway：所有外部访问的统一入口，负责 AI 模型的路由、认证、限流与安全隔离。

• Tuwunel Matrix Server：基于 Matrix 协议的即时通讯服务器，为 Manager 与 Worker、人工管理员之间提供可监督的通信通道。

• Element Web / Nginx：提供 Web 端的即时通讯客户端界面。

• MinIO：对象存储服务，作为系统的共享文件系统，用于存储 Agent 配置、任务规格、工作产出与共享知识库。

• Manager Agent (OpenClaw)：核心管理智能体，负责接收任务、协调 Worker、管理生命周期。

• mc mirror：用于将 MinIO 共享存储同步至 Manager 本地工作目录 (~/hiclaw-fs/)。

### Worker 容器

执行具体任务的工作智能体，每个 Worker 包含：

• Worker Agent (OpenClaw)：具备特定技能的 AI 智能体。

• mc：MinIO 客户端，用于与共享文件系统交互。

• mcporter：将外部工具 API (如 GitHub) 标准化为 Model Context Protocol (MCP) 工具，供 Worker 调用。

## 核心价值与特性

### 1. 人工监督下的自动化协作

所有 Agent 间的通信都在 Matrix 房间中进行，全程对人类管理员可见且可介入。

### 2. 企业级安全与隔离

通过 Higress AI Gateway 实现基于 Consumer (Worker) 的细粒度权限控制与 API 凭证隔离，确保敏感信息不泄露。

### 3. 集中化凭据与文件管理

所有外部服务凭据由 Manager 集中管理并通过网关安全下发；任务文件、代码、产出统一存储在 MinIO 中，确保可追溯性。

### 4. 灵活的模型切换与管理

支持会话级即时切换和持久化主模型切换，可对接多种云厂商和本地部署的大语言模型 (LLM)。

### 5. 弹性可扩展

Worker 采用无状态设计，可根据任务负载动态创建与回收，并通过 Higress 网关实现负载均衡。

## 官方资源

• GitHub 仓库：https://github.com/higress-group/hiclaw

• 项目文档：https://github.com/higress-group/hiclaw/tree/main/docs

• 官方网站：https://higress.ai/hiclaw

• 社区交流：钉钉群 163855016601 | Discord

---

## 使用 AI Gateway Manager 实现无缝模型切换

HiClaw 内置的 AI Gateway Manager 插件，旨在解决多模型协作场景下，因切换不同 AI 服务提供商或模型版本带来的配置复杂性和中断问题。它作为 Higress AI 网关的增强组件，提供了统一的模型调度界面和配置管理能力。

欢迎试用新版功能，如有任何问题或反馈，请在项目 Issue 区或社区留言。

## 安装与部署

### 前提条件

请确保您的系统已满足以下条件：

• Docker Desktop 已安装并处于运行状态（引擎状态显示为绿色）。

• Windows 用户：建议启用 WSL 2 后端。内存不足时可编辑 `%USERPROFILE%\.wslconfig` 文件调整，例如设置 `memory=8GB`。

• 拥有目标 LLM 服务商（如阿里云百炼、OpenAI 等）的有效 API Key。

### (推荐) Windows 一键安装脚本

1. 点击 Windows 开始菜单，搜索并打开 Windows PowerShell。

2. 复制并执行以下命令，该命令将临时调整执行策略并下载官方安装脚本：

Set-ExecutionPolicy Bypass -Scope Process -Force; $wc=New-Object Net.WebClient; $wc.Encoding=[Text.Encoding]::UTF8; iex $wc.DownloadString('https://higress.ai/hiclaw/install.ps1')

1. 脚本启动后，您将进入 HiClaw 安装引导界面。请根据提示依次操作：

选择语言：脚本会自动检测系统语言，通常直接按 Enter 选择默认中文即可。

选择安装模式：

• 模式 1 (快速开始)：使用阿里云百炼，大部分配置采用默认值，仅需输入 API Key，适合新手。

• 模式 2 (手动配置)：可自由选择 LLM 提供商并自定义各项参数，适合高级用户。

后续根据向导提示完成网络配置、服务端口设定等步骤。

### (通用) 手动安装 AI Gateway Manager 插件

AI Gateway Manager 作为一个独立的 Higress 插件，其源码仓库位于：

https://github.com/higress-group/ai-gateway-plugin

安装步骤：

1. 确保您的 控制台 (Manager) 可以访问上述 GitHub 仓库。

2. 通过 跟Manager对话的方式，从该仓库安装 ai-gateway-plugin。

3. 安装成功后，您可以通过浏览器访问 AI Gateway Manager 的管理界面，默认地址通常是：

http://<您的-Manager-IP>:18080/agm

请将 `<您的-Manager-IP>` 替换为实际部署 HiClaw Manager 的主机 IP 地址。

安装完成验证：成功访问上述管理界面，即可看到插件管理面板。

![HiClaw核心架构](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CBe66ugaImkickzbMq4gb758bHlv2sLGetybFRtTQfCGiaDDibtx0kKMfIAaCJLOxenWxibEKkicC0fEXYfd5IFLQMCH4Jh7vVX1wGGibPk7knnzA/640?from=appmsg)

---

## ![Manager容器架构](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CBe66ugaImkiac1H4ODO3CoibR99YZI5zmxK4KSeMYJYNyWeyLY4pHFsJsGCsML5Akvk3Ta0lDq3icLQtb6VOngICt3zUFSIGo9r9WsicIs0tFQ/640?from=appmsg)![安装模式选择](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CBe66ugaImnxhu2ruBcicBYSzNJtWEicBibYs6YML8WaO1DerWvoKICIyuPqUOe6oSCEibADLnia1vxfhRria7cr6L7QlMN1iaT7oenHqyg7fxnd2I/640?from=appmsg)配置与使用

### 第一步：新建 Worker 并关联模型服务

AI Gateway Manager 的核心功能之一是统一管理不同服务商的模型端点。下面以添加 scnet 服务商的接口为例。

1.  在 AI Gateway Manager 面板中，找到 "新建 Worker" 或 "添加模型服务" 选项。

![Worker容器架构](https://mmbiz.qpic.cn/mmbiz_jpg/CBe66ugaImmaRAvjibguO9Mn4SGYpUQpN4jot1GOZiaiaR01WWaxsHaooZ70jEA36FRrnuX6e5nNZcccT3YticW1ao9flNFI6qIFGt0VUveuqmA/640?from=appmsg)

2.  在弹出的配置表单中，选择或填入以下关键信息：

• 服务商类型：根据您的 API 提供商选择，例如 OpenAI-Compatible、Azure OpenAI、Aliyun Bailian 或本例中的自定义 scnet。

• API 端点 (Endpoint)：填入该服务商提供的完整 API URL。

• API Key：填入对应的认证密钥。

• 模型标识 (Model Name)：填写该端点下可供调用的具体模型名称，如 qwen-max、gpt-4 等。

![AI Gateway Manager界面](https://mmbiz.qpic.cn/mmbiz_jpg/CBe66ugaImnTCY6u6OXL5VZmy71zRNh29MzjjuoVqiaQyaFAd8xuljCWvET4uBdH2r43ceNicYLFQaZNiciaXLxDeWIXdMwibE8eK8rfPibFmic89w/640?from=appmsg)

3.  填写无误后，点击"确定" 保存配置。

### 第二步：创建对话生成 Worker

### ![安装引导界面](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CBe66ugaImkTTckZEiaj9MJNsOSWeWG23gvpmxXZ72uc4yRMX2XdMUTh6fUQibZknYwjamuekdvwNfCkmsPN1CfZU356eRicsLYUO3LnSorE9I/640?from=appmsg)

配置好模型服务后，即可利用它来创建一个具备对话能力的 Worker。

![Worker创建界面](https://mmbiz.qpic.cn/mmbiz_jpg/CBe66ugaImm0K6JkQnQCQmKbmRtiaDc0NTr7Up59nhRpFlumBPF0YibqIMakVdEMr44oIVRfDYk8VuBxO9AvEMiaOxtroaHMXoah5WToJVSu3U/640?from=appmsg)

1. 在 Manager 的 IM 客户端 (Element Web) 中，使用斜杠命令或任务指派功能，请求创建一个新的 Worker。例如，您可以输入：

/create-worker name=alice model=scnet:qwen-max

或更自然的指令：

请使用 scnet 服务商的 qwen-max 模型，创建一个名为 alice 的 Worker。

1. 查看面板：创建指令发出后，AI Gateway Manager 面板和 HiClaw 系统将开始协同工作。稍等片刻，新的 Worker (alice) 就会出现在面板的列表中。

![新建Worker界面](https://mmbiz.qpic.cn/mmbiz_jpg/CBe66ugaImnTx0gLVryECoe3PLF4hnlxHx01SfX4riceMdKqz5zmSNRWGDNN76klRibicbUDbWE1E0hOtyLGAm0Z9XbhOu50pZTUBMC8mA5Jn4/640?from=appmsg)

1.  监控 Worker 状态：面板会直观显示每个 Worker 的实时状态，例如 运行中、\*\* 空闲\*\*、\*\* 初始化中\*\* 或 异常。

2.  模型查看与切换：在 Worker 的详情页或管理列表中，您可以清晰地看到它当前绑定的模型，并可以在已配置的多个模型服务间进行快速切换。

### 第三步：测试模型切换功能

![Worker状态监控](https://mmbiz.qpic.cn/mmbiz_jpg/CBe66ugaImndGBd676lyLJMM5PvKhickliaGpJRDGfr1IKOzDnzVSOvcPIXOsrByjSWGbrvXcVSkjDD0I26ibPp6B9js1wcTkDVrAxOMEqM7f0/640?from=appmsg)

![模型切换界面](https://mmbiz.qpic.cn/mmbiz_jpg/CBe66ugaIml823Iu1ddXd1U50SGRBibSeWj9RB0mvhHJygLj8XwWibaXic2J17tEY1vk3Vw8y9ibng5Ely5HhvibkgdibxBRKc3hPU8fDSS8jwLrE/640?from=appmsg)

当系统中有多个 Worker 或一个 Worker 绑定了多个备用模型时，即可测试 AI Gateway Manager 的核心价值——无缝模型切换。

1. 发起切换请求：您可以直接在 IM 中向 Manager 发送指令，例如：

将 alice 的模型切换到 claude-3-5-sonnet。

或者使用 Manager 内置的模型切换技能。

1.  观察切换过程：在 AI Gateway Manager 面板上，您可以实时观察到目标 Worker 的模型标识发生变化，并且其状态可能短暂变为"切换中"。

2.  验证结果：切换完成后，立即向该 Worker 发送一个测试任务，验证其是否在使用新的模型进行响应。同时，可以在面板上查看该 Worker 的详细信息，确认其当前活跃的模型配置。

---

## 运维与回收

HiClaw 的 Worker 采用无状态设计，可以根据任务需求动态创建和回收，从而实现资源优化。

停止并回收 Worker：当某个 Worker 的任务已完成，或暂时不需要使用时，您无需手动操作容器。只需在 IM 中向 Manager 发送指令即可，例如：

请帮我停止并回收 alice 这个 worker。

Manager 会自动停止对应的容器，清理临时资源，并在 AI Gateway Manager 面板上将其状态更新为"已停止"或从列表中移除。

持久化配置保留：Worker 的配置（如技能、绑定的模型服务关系）通常保存在 MinIO 共享存储中。停止 Worker 不会删除这些配置，下次需要时，可以用相同的指令快速重建一个行为一致的 Worker。

预览时标签不可点

作者提示: 内容由AI生成

修改于

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