---
title: Decepticon：提出\"Vibe Hacking\"新范式，一条命令自动打完从侦察到持久化的完整红队链路
url: https://mp.weixin.qq.com/s/kgeE-9GCQjeiMt46EfLnvw
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:04:04.092167
---

# Decepticon：提出\"Vibe Hacking\"新范式，一条命令自动打完从侦察到持久化的完整红队链路

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/9mJNQIzib3Q31HXI7c0wiceDvFDkFHD6Z4eUyIWGGhEV5LR7yhdwNrXsAP2uqBRPYibdH8CuhtFoUxutdstIXDwmPNy7P7oNiaRdAdh8tWCyS1I/0?wx_fmt=jpeg)

# Decepticon：提出"Vibe Hacking"新范式，一条命令自动打完从侦察到持久化的完整红队链路

原创

JunYi
JunYi

毅心安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## Decepticon：提出"Vibe Hacking"新范式，一条命令自动打完从侦察到持久化的完整红队链路

作者：PurpleAILAB | 项目地址：github.com/PurpleAILAB/Decepticon | ⭐ 4.5k Stars

---

各位好，今天介绍的这个项目，可能是最近让我觉得**概念定义最清晰**的 AI 红队工具。

名字叫 **Decepticon**（没错，就是变形金刚里那个反派联盟的名字），副标题是 **"Vibe Hacking Agent"**。作者是韩国团队 PurpleAILAB，v1.0.0 在 2026 年 3 月 25 日正式发布，有英文和韩文双语 README，有 Discord 社区，有完整的 Mintlify 文档站。目前已收获

1. 4. 5k Stars，881 Forks，这个量级对于一个新项目来说，说明它踩在了一个真实的需求点上。

---

项目流程图

![](https://mmbiz.qpic.cn/mmbiz_png/9mJNQIzib3Q3ppqiaTmyW12lMRcOQd6SIqc5N54oXXN9w9pBbnNV7mYUHcqukPtR0kRGJpLBaRITw2raIYFiaGpLhsjRHHRWaBmzsFrMQ6WMB8/640?from=appmsg "null")

### 先说核心概念："Vibe Hacking"是什么

PurpleAILAB 在这个项目里提出了一个新词——**Vibe Hacking**，并把它定义为进攻性安全的新范式。

他们的定义很直接：传统红队需要几百小时的手工工作——扫描、枚举、横向移动、编写报告……大部分是重复劳动，全程令人精疲力竭。与此同时，攻击面的扩展速度已经超过了任何团队手动覆盖的能力上限。

Vibe Hacking 改变的是**人机分工**：

> "Delegate the repetitive. Focus on the decisive."
>
> （把重复性工作交给机器，人专注于决策性判断。）

AI Agent 接管扫描、输出分析、技术链条拼接和实时适应，人类设定任务、定义规则、专注于机器还不擅长的东西——直觉、判断力和创造性思维。

这个定义有别于"AI 替代渗透测试工程师"的叙事。它强调的是**红队效能的放大**，不是取代。作者说得很坦率："This isn't about making hacking easier. It's about making red teams **fast enough to matter** — before the next breach proves they weren't."

---

### 它和其他 AI 渗透工具最大的不同：思考杀伤链，不是思考检查清单

作者在 README 里有一段话值得原文引用逻辑：

> "Most security tools stop at the scan report. Decepticon doesn't. It thinks in kill chains — reconnaissance, exploitation, privilege escalation, lateral movement, persistence — executing multi-stage operations the way a real adversary would, not the way a scanner does."

这句话道出了一个安全行业长期存在的问题：大多数"安全工具"给你的是一张漏洞清单（CVE 列表），但真实的攻击者思考的是：我能不能把这些点串成一条路，从外网打进来、拿到域控、最后在里面留个后门？

Decepticon 的设计目标是后者——**按照真实攻击者的思路，执行多阶段作战**。

---

![](https://mmbiz.qpic.cn/mmbiz_png/9mJNQIzib3Q1wzSDgCruShgmrvNEcHpzvaia9P0yRiaXZicOmicuHUHvzX026IvbZbfqsfXsdYjBq0ooTiclAb1WWXGs2Uvw4I6N4Hz70Lke6Px9E/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/9mJNQIzib3Q3kYlvCf3joFjHibAtqzM3HSRsQ9VJ8JcafwWDo84XJGcpklhmiaaSh8wD5unDqnTmCQvYyeO4TJy00yRBN6bZqtmDGXhuRSRPDQ/640?wx_fmt=png&from=appmsg)

### 三大设计原则

**原则一：真实红队，不是走流程**

Decepticon 模拟的是实际对抗行为，不是对着端口列表跑 CVE 扫描。它读取一份作战计划（Operations Plan），根据实际发现的情况自适应路径，通过任何可行的路线追求攻击目标。目的是测试防御体系在**真实攻击下的实际韧性**，而不是合规打钩。

**原则二：完全隔离**

每一条命令都在硬化的 **Kali Linux 沙箱**里执行。没有任何工具碰到宿主机。没有凭据泄露。没有意外横向扩散。你拥有完整的进攻性工具箱——nmap、Metasploit、自定义脚本——但风险全部被控制在隔离环境内。这个设计是生产级红队工具的基本要求，很多同类工具跳过了这一步。

**原则三：CLI 优先**

安全工作属于终端。Decepticon 的界面是用 Ink（React-like 终端 UI 框架）构建的实时流式 CLI——没有浏览器标签页，没有仪表板，没有上下文切换。你看到的，就是 Agent 正在做的，实时发生。

---

### 五个 Agent，每个只做一件事

这是 Decepticon 架构里最值得深挖的部分：**专项化 Multi-Agent 设计**。

不是一个"全能 AI"包打所有，而是一个**总指挥** + 四个**专项 Agent**的协作体系，基于 **LangGraph** 构建：

**Decepticon（总指挥）**：整个系统的编排器。读取 Operations Plan，分析当前态势，决定派遣哪个专项 Agent 执行什么任务，维护整体杀伤链的推进状态。

**Recon Agent（侦察枚举）**：专职信息收集。在沙箱内运行 nmap 扫描、服务枚举、攻击面测绘，把发现的内容结构化输出给总指挥。

**Planner Agent（规划生成）**：专职文档生成。从任务简报出发，生成 ConOps（作战概念）、Operations Plan（作战计划）、Rules of Engagement（交战规则）等正式文档。这是从"我想测一下这个系统"到"我有一份规范化红队任务书"的自动化转化。

**Exploit Agent（漏洞利用）**：专职攻击执行。通过已发现的漏洞、弱凭据或错误配置尝试获取访问权限，调用 Metasploit 框架和 CVE PoC。

**Post-Exploit Agent（后渗透）**：专职攻陷后的动作——权限提升、横向移动、持久化、数据收集。

**这个设计里有一个非常聪明的工程决策：每个 Agent 都有独立的干净上下文窗口。**

README 里明确写了：

> "Each agent spawns with a **clean context window** per objective — no accumulated noise, no degraded reasoning. Findings persist to disk, not to memory, so every iteration starts sharp."

换句话说，发现的证据不存在内存里靠模型记住，而是写入磁盘。下次任务开始时 Agent 的上下文是干净的，从磁盘读取上次的发现继续推进。这解决了 AI Agent 长任务中上下文污染导致推理退化的核心问题，是工程设计上的真实考量，而不是 PPT 描述。

---

### 一键运行 Demo：从零到完整攻击链的实际体验

Decepticon 内置了一个零配置 Demo，**不需要任何靶机准备**，一条命令直接运行：

```
decepticon demo
```

这条命令会自动：拉起 **Metasploitable 2** 作为靶机（经典的渗透测试练习靶机），加载一份预置的 Engagement（任务计划），然后自动跑完完整的杀伤链：

端口扫描 → 服务枚举 → vsftpd 2.3.4 backdoor 漏洞利用 → 后渗透（获取 shell）

vsftpd 2.3.4 的后门漏洞是一个经典案例，触发方式是在用户名里加上 `:)`，服务器会在 6200 端口打开一个 root shell。这是 Metasploitable 2 里最标志性的漏洞场景，Decepticon 能从头跑完这条链路，说明其自主执行能力已经过真实环境验证。

---

### 完整 CLI 命令表

```
decepticon             # 启动所有服务，打开交互式 CLI
decepticon demo        # 对 Metasploitable 2 运行引导式 Demo
decepticon victims     # 启动内置靶机（DVWA + Metasploitable 2）
decepticon stop        # 停止所有服务
decepticon update [-f] # 拉取最新镜像，同步配置
decepticon status      # 显示服务状态
decepticon logs [svc]  # 追踪服务日志
decepticon config      # 设置 API Key 和配置项
decepticon remove      # 完全卸载
decepticon --version   # 显示版本
```

`decepticon victims` 这个命令值得特别说一下：内置了两个靶机——DVWA（Damn Vulnerable Web Application，Web 漏洞练习）和 Metasploitable 2（综合漏洞靶机）。不需要自己搭靶机环境，拿到工具直接开始测试。

---

### 安装与配置

**前置条件只有两个：Docker 和 Docker Compose v2。**

```
# 一键安装
curl -fsSL https://raw.githubusercontent.com/PurpleAILAB/Decepticon/main/scripts/install.sh | bash

# 配置 API Key（支持 Anthropic Claude 或 OpenAI GPT）
decepticon config

# 启动
decepticon
```

安装脚本会自动拉取 Kali Linux 沙箱镜像、LangGraph 服务和 CLI 客户端。整个 `containers/` 目录里有完整的 Dockerfile，包括 Kali Linux 环境的安全加固配置——关闭不必要的服务、权限隔离、工具预装。

贡献者开发模式需要 Python + uv，以及 Node.js：

```
git clone https://github.com/PurpleAILAB/Decepticon.git
cd Decepticon
uv sync --dev                          # Python agents
cd clients/cli && npm install && cd ../..
docker compose up -d --build
cd clients/cli && npm run dev
```

从 v1.0.0 到 v1.1.16，一个月多一点。这个增速说明项目触到了真实需求，团队也在快速迭代。今天就把 v1.1.16 的四大核心更新逐一拆解，讲清楚它们解决了什么问题，以及对安全工程实践意味着什么。

---

### 更新一：沙箱多租户——这是面向企业 SaaS 部署的基础设施升级

**核心 PR：#710**

先说背景。v1.0.0 的架构是单租户的：一个 Decepticon 实例对应一个 Kali 沙箱。这对个人研究员和小团队完全够用，但对于想把 Decepticon 做成企业级 SaaS 服务的场景，这是根本性的限制——如果多个 Engagement 共用一个 LangGraph 进程，各自的 bash 命令会混在同一个沙箱里，数据隔离无从谈起。

v1.1.16 的解决方案叫做 **per-engagement sandbox routing**：

```
# 新的沙箱解析逻辑
sandbox = get_sandbox(config)
# config 里携带 configurable.sandbox_url / sandbox_token
# 每个 Engagement 运行时从 configurable 里解析自己的沙箱地址
# 没有配置时退回到进程默认值（单租户/开发模式不受影响）
```

效果是：**一个共享的 LangGraph 进程，可以把每个 Engagement 的 bash 执行分别路由到各自独立的沙箱，做到零跨租户数据泄漏**。

这个改动和 Decepticon 的 SaaS 版本（decepticon-saas）直接联动，更新日志里还特别写了 downstream note：SaaS 侧的 GCE sandbox runtime 消费了 #710 的 per-run `configurable.sandbox_url`，需要把 SaaS 的 `decepticon` pin 升到 1.1.16 并重建 langgraph 镜像才能激活。这说明这个功能是**生产级的、配合商业产品使用的**，不是玩具性质的改动。

从安全角度看，多租户沙箱隔离解决的不只是技术问题，更是**渗透测试数据合规问题**——A 客户的 Engagement 产生的 bash 历史、侦察结果、漏洞信息，不能在 B 客户的任务里可见。这在企业红队服务里是基本底线。

---

### 更新二：开放网络研究工具套件——Recon Agent 的能力大幅扩张

**核心 PRs：#650 #654 #656 #657 #682 #684 #687 #692**

v1.0.0 的 Recon Agent 主要依赖 Kali 沙箱内部的工具（nmap 等），对开放互联网的情报采集能力比较弱。v1.1.16 专门新增了一整套**开放网络研究工具**，全部受 RoE（交战规则）管控，只允许对在 scope 内的目标发起查询。

**新增工具逐一说：**

`detect_tech_stack`：技术栈指纹识别。对目标网站做被动或主动指纹采集，识别 CMS、框架、服务器类型。这让 Recon Agent 在做初始侦察时就能拿到技术栈信息，为后续 Exploit Agent 选择合适的 Payload 提供依据。

**Live JS 密钥扫描器**：实时扫描目标网站加载的 JavaScript 文件，检测硬编码的 API Key、Token、密钥字符串。这是非常高频的信息泄露场景——开发者把 AWS Key 或者第三方 API Token 直接写进前端 JS，结果被扫描到。Decepticon 现在能自动化这个步骤。

`osint_enrich`：被动情报富化。查询目标域名/IP 的被动信息来源，比如 Shodan、历史 DNS 记录、证书透明日志、WHOIS 等，不主动对目标发包，纯被动采集。OSINT 在红队侦察阶段非常关键，这个工具让 Recon Agent 的情报能力对标主流 OSINT 工具链。

**网络侦察套件**（#684）：更完整的网络层侦察能力，包括端口探测策略、服务版本识别辅助等。

**RoE 管控的 web\_search**（#650）：允许 Agent 对开放互联网发起搜索查询，但**必须通过 Rules of Engagement 过滤**——只能查与目标相关的信息，不能跑偏。沙箱侧还配了一个 open-web fetch 引擎（#687），Agent 可以在受控环境里抓取网页内容。

这一批工具的重要性在于：过去的自动化渗透工具往往只会扫端口、跑 CVE，缺乏**情报层面的深度**。现在 Decepticon 的 Recon Agent 拥有了从被动 OSINT 到主动技术指纹识别的完整情报链，这是向真实攻击者能力看齐的必要步骤。

---

### 更新三：LightRAG 技能检索——Agent 的"技能大脑"升级

**核心 PRs：#681 #694 #695（ADR-0011）**

这是本次更新里**技术架构最有意思**的部分。

Decepticon 的技能系统（skills/）是各 Agent 的能力来源——每个"技能"是一段描述如何完成某类任务的知识和指令，Agent 在执行时通过 `find_skill` 检索相关技能来增强决策。

问题在于：随着技能数量增加（Mobile/IoT/Wireless 这次又加了一批），纯向量相似度检索的精准度会下降，特别是当任务描述比较模糊或者跨领域时。

v1.1.16 引入了 **LightRAG 风格的混合检索**（ADR-0011）：

> 向量检索（语义相似度）+ 图谱遍历（技能之间的关联关系）并行运行，综合排名后输出最相关的技能。

这个设计来自 LightRAG 论文的核心思路：把 RAG 的向量召回和知识图谱的关系推理结合起来，解决"我描述的目标和技能描述的措辞不一样，但语义相关"的匹配问题。

**对实际使用意味着什么**：Agent 在执行横向移动任务时，不只是找"横向移动"关键词相关的技能，还能通过图谱关系发现"凭据重用"→"内网枚举"→"Pass-the-Hash"这一串相关技能，形成更完整的技能链路。Agent 的单步决策质量会提升，减少因为找错技能导致的无效尝...