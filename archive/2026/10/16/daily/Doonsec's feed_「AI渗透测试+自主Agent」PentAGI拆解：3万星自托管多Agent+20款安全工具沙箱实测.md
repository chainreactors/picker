---
title: 「AI渗透测试+自主Agent」PentAGI拆解：3万星自托管多Agent+20款安全工具沙箱实测
url: https://mp.weixin.qq.com/s/zlLXY_BwN-draqRSqXbQnA
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:32:23.920736
---

# 「AI渗透测试+自主Agent」PentAGI拆解：3万星自托管多Agent+20款安全工具沙箱实测

# 「AI渗透测试+自主Agent」PentAGI拆解：3万星自托管多Agent+20款安全工具沙箱实测

原创

句芒安全实验室
句芒安全实验室

句芒安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

上一期拆的是 AgentHound——把 AI Agent 基础设施拉成一张攻击图。这一期换个方向：如果干脆让 AI 自己去打靶，一整套渗透流程它能不能跑完？

AI 安全圈在这件事上吵了两年。多数工具停在"扫一遍给结论"：PentestAgent 出报告、Pentest Swarm 用信息素调度蜂群、CyberStrike 给 agent 配七千多个技能。真正把"一整支渗透团队"塞进 Docker、跑在自己服务器上的，是 `vxcontrol/pentagi`。

仓库自己的定位是一句话：你用自然语言描述目标和一个目的，一组专职 AI Agent 自己规划、在隔离 Docker 沙箱里跑 20+ 专业工具（nmap、Metasploit、sqlmap 等）、记住学到的东西，最后交给你一份报告。

硬数据：30512 star、4585 fork、33 个未关 issue、MIT、以 Go 为主（约 710 万字节 Go 加 415 万字节 TypeScript）、2025 年 1 月建仓、最新 release v2.2.0（2026-10-05），作者是迪拜的安全工程公司 VXControl。

![PentAGI 分析仪表盘：Flows 活动、工具调用、Token 用量、成本四条曲线随时间变化，下方是 Flow 执行明细](https://mmbiz.qpic.cn/mmbiz_png/J2hBCjr4LfucZQkf5GazHzvzXOkJAg30icHiaRsUXqll2yQFThWNOT2I7GgF3TfW7DeaHBEibyMgAjmEU9WdsXicQrbeTDkYxZeDc0ErWACticgA/640?wx_fmt=png "PentAGI 分析仪表盘：Flows 活动、工具调用、Token 用量、成本四条曲线随时间变化，下方是 Flow 执行明细")

### 它是什么

两件事分得很清楚：

* **谁来用**：安全工程师、渗透测试人员、研究者、红队。前提是跑在自己的基础设施上，只做授权测试——仓库在 EULA 里写明只测自己拥有或明确授权的系统。
* **跑在哪**：自己的服务器加自己选的模型——10+ 云厂商 LLM、任何 OpenAI 兼容端点，或者 Ollama/vLLM 本地模型。

架构分六块：

1. **核心服务**：React+TypeScript 前端、Go 的 REST+GraphQL 后端、PostgreSQL+pgvector 向量库、异步任务队列、多 Agent 系统。
2. **可选知识图谱**：Graphiti（Neo4j），beta、默认关。
3. **监控栈**：OpenTelemetry、Grafana、VictoriaMetrics、Jaeger、Loki。
4. **分析平台**：Langfuse、ClickHouse、Redis、MinIO。
5. **安全工具**：隔离浏览器 scraper、20+ 渗透工具、沙箱执行。
6. **记忆系统**：长期记忆、工作记忆、情景记忆、知识库，外加一套上下文管理（chain summarization）。

### 亮点一：Agent 分工不是"一个 prompt 打天下"

编排层是 Orchestrator，下面挂三个专职 Agent：Researcher（分析目标、查相似案例）、Developer（规划攻击、查 exploit）、Executor（执行计划、查工具手册）。再横向加一批角色：Adviser（顾问/导师）、Planner（规划）、Enricher（补上下文）、Memorist（记忆）、Generator（生成）、Reporter（报告）、Reflector（纠偏）、Searcher（检索）。

数据模型是 Flow → Task → SubTask → Action → Artifact / Memory。一次 flow 是一整个任务，task 是一阶段，subtask 挂 `agent_type`（researcher/developer/executor），action 是具体命令或检索，产出 artifact 和带向量 embedding 的 memory。这个分层值得抄：它把"agent 到底干了什么"变成可查的记录。

### 亮点二：模型自由，包括完全本地

官方支持的 provider 覆盖 OpenAI、Anthropic、Google AI/Gemini、AWS Bedrock、Ollama、DeepSeek、GLM、Kimi、Qwen、MiniMax、Mistral、xAI，以及任何 OpenAI 兼容端点（含 Azure OpenAI）和 OpenRouter 这类聚合器。

要完全脱离云厂商，官方给了一条 vLLM + Qwen3.5-27B-FP8 的自托管路线：4×RTX 5090 上 prompt 处理约 13000 TPS、生成约 650 TPS，支持 12+ 并发 flow。对"目标数据不能出内网"的安全团队，这条比多接一家 API 更有意义。

搜索侧可选 DuckDuckGo、Google、Tavily、Firecrawl、Traversaal、Perplexity、Sploitus、SearXNG，另有一个默认关闭的内置浏览器兜底引擎。

### 亮点三：给小模型装"监理"

这是它最有工程价值的一块，三个机制都带明确开关和阈值：

**Execution Monitoring（默认关）**：盯执行模式。同一个工具调用超过 5 次（`EXECUTION_MONITOR_SAME_TOOL_LIMIT`）、或总调用超过 10 次（`EXECUTION_MONITOR_TOTAL_TOOL_LIMIT`），自动叫顾问（mentor）介入；工具返回里同时带 `<original_result>` 和 `<mentor_analysis>` 两段，判断 agent 是不是真在推进子任务、有没有在打转。

**Intelligent Task Planning（默认关）**：动手前先让 Planner 把任务拆成 3-7 个具体步骤，由 Enricher 看过完整上下文再落计划，原始请求被包进 `<task_assignment>`，防止范围蔓延。

**Tool Call Limits（常开）**：通用 agent 100 次，受限 agent（检索、记忆、报告、顾问这类）20 次；接近上限时由 Reflector 引导收尾。Reflector 还有一条常开规则：LLM 连续 3 次没生成工具调用就介入。

官方在 Qwen3.5-27B-FP8 上给的数字很直接：两个都开，结果质量 2 倍，代价是时间和 token 2-3 倍。他们甚至建议顾问用更强的模型或最高推理档——也就是说，监督层自己也得够聪明。这条对"用 27B 小模型跑自主渗透"的团队是真正的分水岭。

### 亮点四：沙箱与网络边界写得很细

* 默认所有服务只绑 `127.0.0.1`。要外部访问得改 `PENTAGI_LISTEN_IP`、`PUBLIC_URL`、`CORS_ORIGINS`，而且不能拿 `0.0.0.0` 当 `PUBLIC_URL`。
* 生产推荐两节点：worker 跑在独立服务器上，跟主系统分开；用 Docker-in-Docker over TLS（`DOCKER_INSIDE=true`、`DOCKER_INSIDE_HOST=tcp://…:3376`、`DOCKER_INSIDE_TLS_VERIFY=1`），把宿主 Docker API 留在另一台机器上。
* 明确**不推荐** bind-mount Docker socket（`DOCKER_SOCKET`）。两种翻车方式写得很清楚：一是启动顺序竞态——挂载源还不存在时 Docker 会把它建成目录，重启后 dind 起不来，得手工删；二是爆炸半径——挂宿主 socket 等于把宿主 Docker API 交给一个自主 agent，它能起特权容器、挂 `/`、接管整台机器，PentAGI 自己也在里面。只在单机开发环境用。
* `PROXY_URL` 只代理后端自己的 HTTP 调用（LLM、embedding、搜索引擎，含自建 Ollama/SearXNG，没有 `NO_PROXY` 豁免），沙箱容器、scraper、Graphiti、OAuth 登录、Langfuse/OTel 导出都不走它。要隔离就在网络层做。
* flow 沙箱不绑 localhost：每个 flow 会发布两个 TCP 端口做带外回调（reverse shell 之类），取自 `DOCKER_PORTS_BASE` 起 2000 个端口的窗口（默认 28000-29999），绑在 `DOCKER_PUBLIC_IP`（默认 `0.0.0.0`）。Docker 会绕过 ufw 规则，firewalld 走自己的 docker zone——要么在宿主前放防火墙，要么用 iptables 的 `DOCKER-USER` 链限制这段端口。

### 亮点五：多实例与 flow 级文件

多个 PentAGI 实例共用一套外部资源（一个 PostgreSQL、一个 worker 节点、一个 Neo4j/Graphiti、一个 Langfuse）时，设 `TENANT_ID` 会把所有会撞名字的东西命名空间化：PostgreSQL 建在自己的 schema 里、worker 容器名变成 `acme-pentagi-terminal-<flow>`、知识图谱 group id 变成 `acme-flow-<id>`、cookie 和 API token 的签名 key 跟着变，连 session cookie 名字都换掉。值严格校验 `^[a-z][a-z0-9_]{0,31}$`，非法直接启动失败，而不是悄悄归一化。

不命名空间化的是宿主资源，得自己分配：`DATA_DIR`（两个实例共用会互相覆盖 flow 数据）、`DOCKER_PORTS_BASE`、发布端口、`INSTALLATION_ID`。启动时会打印在 `Instance identity` 下，值得对一遍。

flow 级文件也是隔离的：每个 flow 有自己的 Files 页，文件落在 `{dataDir}/flow-{id}-data/`，三个来源是上传（`uploads/`）、资源库附件（`resources/`）、容器快照（`container/`）。上传和资源会镜像进运行中的容器 `/work/uploads/`、`/work/resources/`，并且自动列进 agent 系统提示的 `{{.UserFiles}}` 变量（渲染成 `<task_files>` XML 块）——这也是一处容易忽略的注入面：你放进 flow 的文件名和路径会直接进模型上下文。

![PentAGI Flows 列表：ID/Title/Status/Provider/Terminals/Created/Updated 七列，Running 状态与 E2E Provider](https://mmbiz.qpic.cn/sz_mmbiz_png/J2hBCjr4LfsUqoFdhNwXO95QDiaViasqbhibyCqOWOUYbZosIbX7e24AEArN7AGicbjfg7OGohBdZENFI0OJsekdt0u6ncxx2vujCS3hAQ2nqk0/640?wx_fmt=png "PentAGI Flows 列表：ID/Title/Status/Provider/Terminals/Created/Updated 七列，Running 状态与 E2E Provider")

### 上手

官方推荐用交互式 installer（Linux amd64/arm64、Windows amd64、macOS Intel/M 系列都有对应包），它会做系统检查、生成 `.env`、配 provider、配搜索引擎、生成凭据与 SSL，最后 docker compose 起来。

Linux amd64 最短路径：

```
mkdir -p pentagi && cd pentagi
wget -O installer.zip https://pentagi.com/downloads/linux/amd64/installer-latest.zip
unzip installer.zip
sudo ./installer
```

手工装的话：建目录 → 复制 `.env.example` → 下载三个 provider 示例配置（compose 会挂载，源不存在时 Docker 会建成目录）→ 填 key → `docker compose up -d`。

起来后访问 `https://localhost:8443`，默认账号 `admin@pentagi.com` / `admin`。首登先改密码；忘了可以用 installer 的维护菜单重置。多用户由管理员走 Users REST API 管。

第一次跑 flow 建议窄范围：一个目标、一个目的。也可以在 flow 表单里选模板（比如 `examples/prompts/base_web_pentest.md`）预填。跑完在 flow 页的 Report 菜单里可以网页看、复制、下 Markdown、下 PDF。

### 避坑

* 默认密码 `admin` 必须首登改掉；PentAGI 没有公开自助注册。
* installer 默认用 `/var/run/docker.sock`：要么 `sudo` 跑，要么把用户加进 `docker` 组——后者等于给这个用户 root 等价权限，别在不受控环境这么干。
* `docker-compose.yml` 里 PentAGI 服务是以 root 跑的（要访问 docker.sock）。如果你用 TCP 连 Docker 而不是 socket 文件，就可以去掉 root、用默认 `pentagi` 用户。
* `PROXY_URL` 不是全局代理：沙箱、scraper、Graphiti、OAuth 登录、Langfuse/OTel 导出都不走它。需要隔离就在网络层做。
* Graphiti 是 beta 且默认关：捆绑的 HTTP API **没有鉴权层**，默认只绑 `127.0.0.1`；搜索默认只在本 flow 内，跨 flow 复用要额外隔离设计，别在多租户或共享部署上开。Graphiti 起不来时 PentAGI 会记一条失败的健康检查，然后退回主记忆和向量库；要显式关掉就设 `GRAPHITI_ENABLED=false`。
* `LLM_SERVER_*` 是实验性变量，官方说未来会改。
* 它今天**不是** CALDERA 式的 BAS 或对手仿真产品，没有预置攻击战役；"agent 自己写攻击脚本"官方明确写成概念和未来工作，别拿它当对手仿真替代品。
* flow 报告 UI 今天只有网页、剪贴板、Markdown、PDF 四种，没有 JSON 导出。
* 删 flow 会删记录和长期记忆条目，但**不会**删磁盘上的 `flow-{id}-data/`，空间要自己回收。
* 上传限制：单文件 300MB、单次上传最多 1000 个文件 / 2GB、文件名 255 字节。容器快照是时点快照，在 UI 里改了不会写回运行中的容器。

### 适合谁

三类人：一是做授权红队评估、又不想把目标数据交给云厂商的安全团队——自托管加本地模型，两节点隔离；二是手里只有小模型（<32B）但想让 agent 真跑完渗透流程的团队——开 Agent Supervision，用 2-3 倍时间换 2 倍质量；三是做 AI 安全研究、想看一个自主 agent 系统怎么做工具调用上限、执行监理、上下文治理和沙箱网络边界的人。

回到开头那个问题。PentAGI 真正值得看的不是它接了多少家模型，而是它把"自主 agent 跑渗透"拆成了一串可配置的工程件：工具调用有硬上限、执行有监理、规划有前置、上下文有摘要、沙箱有网络边界、多实例有命名空间。这些边界能不能守住，比 agent 能不能打通一个靶机重要得多。

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hHXiayYmia1LqLl6UmtMH3DtucaIaicr9HY5ffO5ckGVia3LvuCPCDNRNAX9fEmhicdmtRshennOyOqtPic6GTeASRNg/0?wx_fmt=png)

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