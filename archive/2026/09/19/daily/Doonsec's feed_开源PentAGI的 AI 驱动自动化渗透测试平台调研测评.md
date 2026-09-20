---
title: 开源PentAGI的 AI 驱动自动化渗透测试平台调研测评
url: https://mp.weixin.qq.com/s/6XhP5mmhYsuc5NxfXaRgXw
source: Doonsec's feed
date: 2026-09-19
fetch_date: 2026-09-20T07:14:54.601817
---

# 开源PentAGI的 AI 驱动自动化渗透测试平台调研测评

# 开源PentAGI的 AI 驱动自动化渗透测试平台调研测评

原创

AI分析师
AI分析师

开源情报技术研究院

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

俺捏个看网上说的是俄罗斯网安巨头，这个和俺分析的不太一样，不去纠结。

报告性质： 开源情报调研 + 架构/产品测评（非实战攻击演练）

评估对象： vxcontrol/pentagi

评估时点： 2026年9月19日

一、公司主体：VXControl L.L.C-FZ

类型：阿联酋迪拜 Meydan 自由区注册的有限责任公司（Free Zone LLC）

成立：官网写 2025 年 10 月注册，执照号 2538161.01

注册地址：Meydan Grandstand, 6th floor, Meydan Road, Nad Al Sheba, Dubai, UAE

创始人：Dmitry / Dmitrii Nagibin

规模：小团队工作室（LinkedIn 写 2–10 人；官网自称分布式团队在迪拜、普吉、布加勒斯特）

根据项目仓库、官网与公司页：

项目公开事实产品名PentAGI（Penetration testing Artificial General Intelligence）开发主体VXControl L.L.C-FZ，迪拜 Meydan 自由区注册的安全工程工作室创始人Dmitrii / Dmitry Nagibin（GitHub @asdek）团队分布官方自称 Dubai / Phuket / Bucharest开源仓库github.com/vxcontrol/pentagi，MIT最新正式版v2.1.0（2026-05-29）；main 之后仍持续提交社区规模约 2.47 万 Star / 0.32 万 Fork（2026-09）语言栈后端 Go，前端 React + TypeScript，执行层 Docker

VXControl 官方把自己定位为“agentic-AI 时代的进攻性安全工程工作室”：本体开源、自托管，同时另售 VXControl Cloud（威胁情报、增强 AI 支持等），云服务需单独密钥，不在 MIT 代码许可范围内。

# 二、它到底是什么

PentAGI 不是通用 Agent 框架（LangChain / CrewAI / AutoGPT），也不是传统漏扫（Nessus / OpenVAS），更不是 CALDERA 那种预设剧本的 BAS。官方自己划的边界很清楚：

它是一套自主 + 可人工督导的渗透测试平台，不是带预置战役剧本的 Breach and Attack Simulation 产品。

工作方式可以概括成一句话：

用户给出授权范围内的目标与任务 → Orchestrator 拆解 Flow/Task/Subtask → Researcher / Developer / Executor 等专职 Agent 协作 → 在隔离容器里调用专业安全工具 → 结果写入 PostgreSQL + 向量库，并生成报告。

产品形态更接近“自托管的红队控制台 + 多智能体编排器 + Kali 工具沙箱”，而不是聊天机器人。

## 2.1 架构分层

text用户 / REST / GraphQL

│

Web UI (React)

│

Backend (Go) ── Orchestrator

│

┌────┼─────────────┐

Researcher Developer Executor (+ pentester/coder/reflector 等)

│

Docker 沙箱（默认 Kali 镜像 + 20+ 工具）

│

PostgreSQL+pgvector / 可选 Graphiti+Neo4j

Langfuse + Grafana/OTel 可观测性栈

公开文档里能看到两类“智能体划分”，不要被媒体文章搞混：

对外叙事的四角色： Orchestrator、Researcher、Developer、Executor。

实现对内的细粒度 Agent 类型： primary\_agent、assistant、generator、refiner、adviser、reflector、searcher、enricher、coder、installer、pentester、simple、simple\_json 等。不同角色可绑定不同模型与推理强度。

中文二次传播里“13 个专项 Agent”基本来自对上述内部角色的归纳，不是官方对外产品名。

## 2.2 记忆与上下文

这是 PentAGI 相对早期 AutoGPT 类项目更“像产品”的地方：

长期记忆： PostgreSQL + pgvector，保存研究结论与成功路径

工作记忆： 当前目标、状态、上下文

情景记忆： 动作、输出、模式

可选知识图谱： Graphiti + Neo4j（Beta）

链摘要（chain summarization）： 压缩旧对话，控制长任务 token

v2.1 又补了用户资源库、Flow 工作区文件、知识库语义检索和匿名化。

## 2.3 执行隔离

所有进攻性动作默认进 Docker 沙箱，按任务选镜像；安全任务默认 Kali 类镜像，预装 nmap、Metasploit、sqlmap 等 20+ 工具。生产建议两节点：控制面与 worker 分离，避免不可信代码与主控同机。最低资源：2 vCPU / 4GB RAM / 20GB 磁盘。

## 2.4 模型策略

不绑死一家模型。官方支持 OpenAI、Anthropic、Gemini、AWS Bedrock、Ollama，以及 DeepSeek、GLM、Kimi、Qwen、MiniMax，还有 OpenRouter / DeepInfra / LiteLLM 等兼容端点。本地模型走 Ollama 或 vLLM 是明确路径，这对数据不出域的安全团队有实际意义。

# 三、测试方法与边界

本报告的“测试”是产品与工程测评，不是对第三方系统的渗透。原因有三：

EULA 明确：仅允许对拥有或书面授权的系统使用；未授权访问被禁止。

本环境无法代表真实授权靶场，也没有必要为了写评测去演示攻击手法。

进攻性工具的方法细节属于双用途能力，报告只评架构、部署、治理与公开评测，不复述利用步骤。

测评材料包括：

官方 README、Quick Start、v2.1 Release Notes、EULA、NOTICE

Help Net Security、SecurityLab、Spark42 2026 夏季榜、俄语实践者评测

与 Strix、CAI、Shannon、PentestGPT、XBOW、NodeZero 的公开对比

内置自测工具（ctester / etester / ftester）说明项目把 LLM、嵌入向量、函数调用当成一等公民来测，这比很多“包装一层 prompt 的红队 Bot”更像工程产品。

# 四、安装与工程成熟度测评

## 4.1 部署路径

两条官方路径都成立：

交互式 Installer（推荐）： Linux amd64/arm64、Windows、macOS，TUI 向导。

手工 Docker Compose： 拉 docker-compose.yml + .env，docker compose up -d，默认 https://localhost:8443，初始账号 admin@pentagi.com / admin。

可选叠加：

docker-compose-langfuse.yml：LLM 追踪

docker-compose-graphiti.yml：知识图谱

docker-compose-observability.yml：Grafana / Jaeger / Loki / VictoriaMetrics

工程判断： 部署体验明显强于早期 AutoGPT。Go 单体后端 + Compose 全家桶，比 Python 研究原型更接近可运维平台。代价是组件多：Postgres、向量、爬虫、可选 Neo4j/Langfuse，心智负担不低。

## 4.2 接口与二次开发

REST + GraphQL，Bearer Token

文件库与知识库有完整 CRUD

多租户靠 TENANT\_ID 做资源命名空间

默认自签证书，外网暴露必须改 PUBLIC\_URL / CORS

工程判断： 这是 PentAGI 相对 CLI 型竞品（PentestGPT、Shannon）的核心差异——它想做平台，而不是一次性扫描器。适合内部红队门户、流水线编排、把“一次任务”变成可查询对象。

## 4.3 可观测性

可选栈相当完整：OpenTelemetry、Grafana、Langfuse、ToolCall 实时日志、执行监控（循环/低效时 mentor 介入，Beta）、任务规划开关、按 Agent 类型限制 tool call。

俄语实践者在 2026 年 4 月的横向试用里，把 PentAGI 评为“见过的架构里最好的”，理由正是：四层记忆、容器隔离、专职分工、稳定性。但同一作者也强调：好架构不等于立刻能进生产，还要看授权、靶场和密钥治理。

## 4.4 官方自己承认的能力边界

这些比营销口号更有参考价值：

不是 BAS / 对手仿真产品，没有预置 ATT&CK 战役包

Agent 自动写攻击脚本目前应视为概念/未来工作

报告可 Web 查看、复制、Markdown/PDF；JSON flow-report 并未作为正式导出格式

Graphiti 知识图谱仍是可选 Beta

执行监控与智能规划是可关的 Beta

## 4.5 许可证与云服务分界

代码：MIT

使用约束：EULA（授权测试、合法合规、用户对 Agent 行为自负）

VXControl Cloud SDK 代码可看，但云服务是另一套条款

EULA 还写明：软件本身“并不内置攻击工具”，而是协助拉取 Kali 等公开工具集；这是法律责任切割，不改变实际能力画像

# 五、能力画像：强在哪，弱在哪

## 强项

平台完整度高。 UI、API、记忆、观测、沙箱、多模型，在开源进攻性 Agent 里属于第一档产品化。

隔离模型认真。 不是在宿主机直接 os.system，而是容器选镜像 + worker 分离。

模型中立。 美、中、欧云模型与本地 Ollama/vLLM 都能接，适合数据主权敏感环境。

长任务意识。 摘要、记忆、tool-call 上限、reflector、mentor，针对的是 LLM 渗透里最常见的“死循环烧 token”。

二次开发友好。 GraphQL + 文件/知识库 API，适合做成企业内部“红队操作系统”。

## 弱项与风险

缺少与 XBOW Benchmark 对标的公开成绩。 Spark42 2026 夏榜给 PentAGI 的 Benchmark 一项几乎是最低档（1 分），这是最大硬伤。Strix / CAI / Shannon / PentestGPT 都更愿意用公开靶标说话。

“全自主、零人工”被媒体夸大。 仓库自己写的是 autonomous and assistant-guided；生产上仍需范围、授权、密钥、网络隔离和人工验收。

贡献者集中。 Star 很高，核心提交高度集中在创始人，bus factor 不低。ToolVitals 也提示维护信号“活跃但混杂”。

MCP 缺失。 2026 年安全 Agent 生态已把 MCP 当编排层，PentAGI 仍走自有工具协议，和编码 Agent / CI 的衔接不如 Strix。

双用途治理主要靠 EULA 和用户自觉。 开源 + Kali 工具链 + 自主规划，降低了专业红队门槛，也降低了滥用门槛。

默认口令、自签证书、把流量送给外部 LLM/搜索引擎。 安全团队若未改配置，会把目标信息泄露给模型供应商。这是所有 LLM 渗透产品的共性问题，PentAGI 文档有提醒，但不能替用户做完。

## 第三方位置

Spark42《Top 10 AI-Powered Penetration Testing Tools, Summer 2026》开源赛道排名：

Strix 75

CAI 71

Shannon 68

PentAGI 66

PentestGPT 64

评语大意：已经从“雄心勃勃的自主 Agent”长成带 API/记忆/沙箱的平台；公开独立验证仍落后于平台表面成熟度。最适合安全工程团队搭内部进攻实验室或 API 驱动流水线，而不是“开箱即用、用分数证明能打过人类”的扫描器。

# 六、与同类产品对比

对比要按任务层分，不能把通用 Agent 框架和垂直红队产品放在同一张表里硬比。

## 6.1 垂直 AI 渗透 / 红队产品

维度PentAGIStrixCAI（Alias Robotics）Shannon（Keygraph）PentestGPTXBOWNodeZero / Horizon3形态自托管平台（Web+API）CLI/平台，偏 AppSec+修复闭环研究级安全 Agent 框架白盒优先的 Web/API 自主测试 CLI学术出身，现分 Agent / Legacy 助手商业自主 Web 攻击平台商业持续验证平台开源MIT + EULAApache-2.0开源框架开源MIT（学术+工程）闭源 SaaS闭源 SaaS典型场景内网/综合渗透实验室、平台化红队代码仓库、PR、Web、修复回流CTF、研究、多模型实验有源码的 Web 应用CTF/辅助决策 + 逐步自主化Bug bounty 级 Web 利用验证企业内网/云攻击路径验证执行环境Docker Kali 沙箱Docker / 本地较灵活，隔离不统一Docker + 工作区断点续跑Docker 管道厂商云端 Agent 群厂商托管多模型很强，含本地强极强（300+ 模型叙事）依赖云模型，本地弱强，含 Ollama厂商模型厂商模型记忆/知识pgvector + 可选图谱中等有，研究向工作区级有平台内平台内可观测性Langfuse + OTel/Grafana有运行查看器OTel/Phoenix 强CLI 阶段日志Langfuse（后期补）平台报表企业报表公开靶标成绩几乎没有对标榜有部分有研究基准高（白盒 XBOW 变体）有历史 86.5%/104HackerOne 成绩与自有基准企业案例CI/修复闭环API 可接，非原生 PR 修复强项弱中弱弱（发现为主）企业工单流产品化高（像内部平台）高（像开发者工具）中（像框架）中高（像扫描 Agent）中很高很高最适合谁要自建红队控制台的安全工程团队产研一体、要在 CI 里堵住洞的团队研究员、竞赛、机器人/OT 安全AppSec 白盒评估个人研究员、低成本入门要“可利用性证明”的业务安全要连续验证的大型甲方

## 6.2 和通用 Agent 框架的关系

LangChain / LangGraph、CrewAI、AutoGPT、AutoGen 不是竞品，是底层范式：

PentAGI 相当于用 Go 重写并垂直化了“角色分工 + 工具循环 + 记忆”这一套，再焊上 Kali 沙箱和报告 UI。

若目标是做任意业务 Agent，不该选 PentAGI。

若目标是授权范围内的进攻性安全自动化，通用框架要自己接工具、隔离、审计、报告，工作量接近再造 PentAGI。

## 6.3 怎么选（决策树）

要自托管、要 UI/API、要内网综合测试实验室 → PentAGI 是目前开源里最像“产品”的选项之一。

要测自己的 Web 应用/仓库，并修完再回归 → Strix 更顺。

要论文级基准、多 Agent 模式实验 → CAI。

有源码、要“没有利用就不报”的 Web 评估 → Shannon。

要最低成本理解 LLM 渗透怎么想 → PentestGPT Legacy / Agent。

要可利用性证明、接受商业闭源 → XBOW。

要持续打内网攻击路径、给董事会看验证 → NodeZero / 同类 BAS-ish 商业产品，而不是 PentAGI。官方也承认自己不是这一类。

# 七、安全、合规与双用途

PentAGI 处在 2026 年进攻性 AI 的典型张力里：开源降低了专业红队成本，也把“会规划、会调工具”的能力交给任何能申请到模型密钥的人。

必须写进评估结论的约束：

只允许授权测试。 无书面授权即违法，与工具是否开源无关。

目标数据会离开本机。 除非全链路本地模型 + 关闭外网搜索，否则侦察内容会进入 OpenAI/Anthropic/Gemini/搜索引擎。

容器隔离不是法律隔离。 扫错网段、扫到生产、扫到第三方 SaaS，责任在操作者。

默认凭据必须改。 admin@pentagi.com / admin 只是安装占位。

不能替代持证渗透测试。 适合做预检、回归、训练和内研，不适合单独作为等保/监管交付物。

出口与供应链。 法律实体在阿联酋，工具链是全球开源组件；采购时仍应按本组织的开源与供应链政策做来源审查，而不是按“俄罗斯/非俄罗斯”标签一刀切。

# 八、综合结论

PentAGI 是 2025–2026 开源进攻性 Agent 里产品化最完整的一档：Go 后端、Web 控制台、GraphQL、容器沙箱、多层记忆、多模型、可观测性栈，已经不像演示仓库。v1.0 自称 Production Release，v2.1 补齐文件与知识库后，更像可落地的内部平台。

它目前还不是“最能打”的开源 AI 渗透器。公开基准、CI 修复闭环、贡献者多样性都落后于 Strix / Shannon / CAI 这一组。媒体所说的“四个 Agent 零人工打穿一切”，和官方能力边界、第三方榜单都不一致。

更准确的定位是：

给安全工程团队的自托管红队操作系统雏形，不是给董事会的一键扫描器，也不是给脚本小子的全自动黑客。

## 建议采用方式

只在隔离实验室对自有靶场做 PoC，先跑通模型、记忆、Langfuse，再谈扩大范围。

控制面与执行节点分开，外网搜索与云模型默认最小化。

人工复核所有“高危发现”，把 Agent 输出当线索而不是结论。

若主需求是应用安全与修复闭环，并行评估 Strix；若主需求是 Web 白盒验证，并行评估 Shannon；不要用 PentAGI 一家覆盖全部。

采购/开源引入时区分 MIT 代码与 VXControl Cloud，避免把可选云服务误写成“必须绑定俄罗斯或阿联酋云”。

## 附录：关键来源

仓库与许可证：https://github.com/vxcontrol/pentagi

公司主体：https://vxcontrol.com/

产品页：https://pentagi.com/

...