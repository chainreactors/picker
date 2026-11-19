---
title: ARTEX---FBI点名的AI渗透框架:3小时拿下特权访问,12000个fork逼得作者删库
url: https://mp.weixin.qq.com/s/fDncX6lljLqcqSkQrGX_bQ
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:40:35.174268
---

# ARTEX---FBI点名的AI渗透框架:3小时拿下特权访问,12000个fork逼得作者删库

# ARTEX---FBI点名的AI渗透框架:3小时拿下特权访问,12000个fork逼得作者删库

Z0安全
Z0安全

Z0安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 项目概述

ARTEX 是一套开源的 AI 自主渗透测试框架，Go 写后端，Next.js 做 Web 控制台，PostgreSQL 存数据，默认监听 8787 端口。它的用法粗暴到离谱：操作员在 Web 界面里用自然语言写一个目标，比如"拿到目标内网某系统的管理员权限"，再圈定范围、配好允许和禁止规则，剩下的从信息收集、漏洞利用、权限提升到数据外带，全部由 AI 代理自己跑，人只需要在关键动作的审批门上点确认。

它不自带模型，想接谁接谁：Anthropic Claude、OpenAI GPT、DeepSeek、GLM、Grok、Kimi，甚至本地 Ollama 都行，只要是 OpenAI Chat Completions、OpenAI Responses 或 Anthropic Messages 三种 API 格式之一就能跑。2026 年 7 月底开源发布，8 月就被各路黑产和威胁组织拿去打真实目标，10 月 8 日作者在 fork 数突破 12000 之后主动删库跑路——但已经晚了，fork、镜像、改名版本（ScopeWeaver、LUCK、Guanlan SEC）和一个叫 ARTEX PRO 的商业版继续满世界流通。11 月 13 日 FBI 直接为它发了 FLASH 预警，一个开源工具混到被 FBI 单独发通告的待遇，历史上没有几个。

在被恶意使用的案例里，韩国多家金融机构约 67000 人的个人信息被拖库；ConnectWise Cloud Backup 的供应链被打穿，波及超过 2250 个下游租户；Barracuda 的云环境里有人拿偷来的云访问密钥配合 ARTEX 做机器速度的凭据串联。Microsoft 的观测数据更吓人：Storm-0940 的一个源地址每分钟打出 2900 次失败登录，从首次定位到拿到特权云访问最短不到 3 小时；11 月 5 日记录到的最快案例，一个代理从 GitHub 上搜到泄露密钥到摸进 Azure Key Vault，只用了 5 分钟。Google 和 Mandiant 复盘的某次行动中，23 秒内落进了 27 个独立的入侵事件——不是 27 次敲键盘，是侦察调用、认证尝试、资源查询各算一个事件，全程没人在旁边指挥。

事件时间线：

| 时间 | 事件 |
| --- | --- |
| 2026-07-26 | ARTEX 在 GitHub 开源发布，AGPL-3.0 协议 |
| 2026-08 | 开始出现在野滥用，金融、政府、医疗、制造多行业被扫 |
| 2026-09 | Storm-0940 用它打 Microsoft 365、Okta、AWS 和 Web 应用；韩国金融机构 67000 人信息泄露 |
| 2026-10 | ConnectWise Cloud Backup 供应链攻击，2250+ 下游租户被波及 |
| 2026-10-08 | 作者删库，当时 fork 已超 12000 |
| 2026-11 初 | Censys 统计到 1600+ 个暴露公网的 ARTEX 控制台 |
| 2026-11-13 | FBI 发布 FLASH 预警 |

## 项目特点

| 特点 | 说明 |
| --- | --- |
| 自然语言驱动 | 一句话目标，框架自己拆解成攻击步骤 |
| 多代理协作 | Planner 负责拆目标，Worker 认领执行，默认 3 个并发 |
| 模型无关 | 不绑定任何厂商，三家 API 格式通吃，支持本地 Ollama |
| 全程留痕 | mitmproxy 录流量，所有代理会话、审批、拦截动作落 PostgreSQL |
| 模型故障转移 | 一家 AI 厂商封 key 自动切下一家，一个战役可摊在多家 provider 上 |
| 资产联动 | 直接同步 ScopeSentry 的域名、子域名、IP、端口、端点数据 |
| 人工审批门 | 关键动作需要人工确认，不是完全放飞 |
| 默认黑名单 | 自带 blocklist 排除 .gov / .gov.cn / .edu / .edu.cn 目标（可改） |
| 复测闭环 | Retest 工作流独立拉起复测代理验证修复效果 |

## 执行模型

```
                 ┌──────────────────────────────┐
                 │     Web 控制台  :8787          │
                 │  Next.js 前端 + SSE 活动流     │
                 └──────────┬───────────────────┘
                            │ 任务:目标 + 范围
                            │      allow/deny 规则
                            │      超时 + 收尾步骤
                            ▼
              ┌───────────────────────────┐
              │        Planner 代理        │
              │    目标 → 攻击 intents     │
              └──────────┬────────────────┘
                         │ 派发 intents
                         ▼
        ┌────────────────────────────────────┐
        │     Worker 代理 ×N（默认 3 并发）    │
        │   nmap / curl / Impacket / ...      │
        └──────┬──────────────────┬──────────┘
               │ 写回结果          │ 请求响应留痕
               ▼                  ▼
   ┌──────────────────┐   ┌───────────────┐
   │   共享黑板        │   │  mitmproxy    │
   │ facts/findings/  │   │  全流量录制    │
   │ hints 全代理可读  │   └───────────────┘
   └───────┬──────────┘
           ▼
   ┌─────────────────────────────┐
   │        PostgreSQL            │
   │  资产图 ⇄ 探索图（双图互联）   │
   │  会话/审批/拦截动作全量落库    │
   └─────────────────────────────┘

   LLM 侧：Anthropic / OpenAI / DeepSeek / GLM
           / Grok / Kimi / Ollama(本地)
   failover：一家封 key → 自动切下一家
```

整个执行链是典型的 planner/executor 架构。Planner 把目标翻译成攻击 intents，Worker 认领后调工具执行，所有结果写回共享黑板——facts、findings、hints 三类信息对全部代理可见，避免重复劳动。数据层是双图模型：资产图记录目标长什么样（域名、服务、应用、端点之间的关系），探索图记录任务目标、研究方向、事实与发现之间的脉络，两图互联，任何一个 finding 都能回溯到对应资产和探索过程。每一步的关键动作走到人工审批门，操作员可以拦截确认，拦截记录同样落库。

## 核心功能模块

### 任务系统

| 字段 | 说明 |
| --- | --- |
| 目标 | 自然语言描述，如"获取目标网络所有财务文档" |
| 范围 | 目标资产圈定，配合 ScopeSentry 资产同步 |
| allow/deny 规则 | 白名单放行、黑名单禁止，粒度到具体动作 |
| 测试账号 | 可预置合法凭据供代理使用 |
| 超时 | 任务级时间上限 |
| 收尾步骤 | 任务结束时的固定动作（清理/报告） |

### 双图数据模型

资产图存目标侧：域名、子域名、IP、端口、端点及其关系。探索图存过程侧：任务目标、研究方向、事实、发现。两图互联带来的直接好处是审计和复盘——从一条漏洞记录能一路点回它属于哪个资产、由哪个代理在哪个探索方向上挖出来的。所有代理的会话、审批、拦截动作全量持久化在 PostgreSQL，对授权测试来说这是合规审计的完整证据链。

### 流量录制

内置 mitmproxy，所有代理发出的请求和收到的响应全部留痕。这意味着测试过程可回放、可举证，蓝队拿到记录就能完整复盘机器做了什么。

### 模型故障转移

这是设计上最"务实"的一块：一个 AI provider 封禁或切断 key 后，框架自动切到下一个。单个攻击战役的请求可以摊在多个 provider、多个 key 上。FBI 对攻击者实例的分析显示，中国模型占大头，DeepSeek Flash 家族用得最多——能力够、价格便宜，而且用"授权渗透测试"的话术包装后模型基本不设防。这也是给防守方的一个提示：出口代理日志里出现大量异常的 LLM provider API 调用，本身就是可疑信号。

### 资产同步

ScopeSentry（同一作者的资产测绘和漏洞扫描平台）的 recon 数据可以一键导入，域名、子域名、IP、端口、端点直接合并进资产图供代理探索，省掉手工录入资产的步骤。

### Retest 复测闭环

任务详情页的 Retest 标签页可以翻阅历史漏洞的结论和证据，发起复测会独立拉起一个复测代理会话，可选填修复版本、测试条件和限制。修复确认后漏洞状态自动更新。渗透测试的"找→报→证明修复"闭环被完整做进了一个工具里。

### MCP 扩展

远程 MCP 服务器支持 Streamable HTTP 和 SSE 两种模式，可以把外部集成挂进代理工具箱。配置 SSE 老式服务器时 URL 填到 /sse，鉴权放 Authorization: Bearer 头里。

## 安装与部署

### 系统要求

| 组件 | 要求 |
| --- | --- |
| 数据库 | PostgreSQL（必需，无它不启动） |
| LLM | ANTHROPIC\_API\_KEY 或 OPENAI\_API\_KEY，环境变量或 UI 里配均可；本地 Ollama 走 http://127.0.0.1:11434/v1，免 key |
| 系统 | Linux / macOS / Windows 均可，镜像内置 ripgrep、curl、vim、npm、nmap 等常用工具 |
| 端口 | 控制台 8787，前端、API、SSE 活动流共用这一个后端端口 |

### 一键安装（推荐）

```
git clone https://github.com/BaaRai/ARTEX.git
cd ARTEX
./install.sh
```

install.sh 会检测并自动装 Docker，然后二选一：全 Docker 路线，回车用一个随机 Postgres 密码，脚本自动写 .env 后 `docker compose up -d --build`；本地构建路线，选数据库（连已有的或 Docker 起一个新的），生成 config.json，go 编译出内嵌前端的单一二进制后启动。

### 手动 Docker Compose

```
git clone https://github.com/BaaRai/ARTEX.git
cd ARTEX
cp .env.example .env      # 填 POSTGRES_PASSWORD，可选填 ANTHROPIC_API_KEY
docker compose up -d --build
# → http://localhost:8787
```

注意没有现成镜像可拉，镜像都是从本地 checkout 构建的——官方说明里特意提到，以前的默认镜像指向一个第三方命名空间，那边已经不托管这个项目了。./skills 和 ./data 通过 bind mount 持久化。

### 预编译二进制

从 Releases 下载对应平台的 zip，解压得到 artex + start.sh（Windows 是 start.bat）+ skills/ + config.example.json：

```
cp config.example.json config.json   # 填数据库连接
./start.sh                            # → http://localhost:8787
```

务必用 start.sh 启动而不是直接跑 ./artex，它是守护脚本，进程崩了会带 backoff 自动拉起。后台常驻用 `nohup ./start.sh >artex.log 2>&1 &`。

### 从源码构建单一二进制

```
cd web && npm ci && npm run build:static && cd ..
cp -r web/out server/webui/dist
CGO_ENABLED=0 go build -tags embedui -o artex ./cmd/artex
./start.sh
```

`-tags embedui` 才会把前端打进二进制。交叉编译用 `./build.sh --release`，产出 Linux/macOS amd64+arm64 和 Windows amd64 的 zip。UPX 自解压默认禁用——部分内核、虚拟化环境和安全策略下不兼容，确认目标环境没问题再显式传 --upx。

![](https://mmbiz.qpic.cn/mmbiz_png/ibuSfucPryHVus9opXdGXFbL6V8EHvyk9icD0HWLcNeibHfcGgg0D5udEuZdvkrQrRs4HntTPT2TibGCXFLsUuh1iacj8EpeWINVUibTRn2KHk1JY/640?wx_fmt=png&from=appmsg)

### 踩坑实录

首次启动打开 http://localhost:8787 走 /setup 设置管理员密码，这里要填一个一次性 setup token——密码没设置时后端启动日志里会打印，Docker 用户执行 `docker compose logs artex | grep "Setup token"` 拿。找不到 token 八成是翻错了日志。

Web UI 默认只绑 127.0.0.1。远程机器访问、或者 ARTEX 跑在 WSL 里从 Windows 访问，需要在 .env 里设 `ARTEX_BIND_ADDR=0.0.0.0`。更稳的做法是保持 loopback，前面挂反向代理或走 SSH 隧道——控制台暴露公网等于把一个自主渗透框架直接交到别人手里，FBI 统计的 1600+ 暴露实例就是这么来的。

用 nginx 反代有个经典坑：SSE 活动流连上了但永远不出事件，原因是 nginx 默认开了 proxy\_buffering。必须关掉它，同时拉长 proxy\_read\_timeout 并设 `proxy_http_version 1.1`，流式事件才能到浏览器。另外 NEXT\_PUBLIC\_SSE\_BASE 只在 SSE 流和页面不同源时才需要，而且只在构建时生效——这个变量是烤进静态 bundle 的，改了得重新 build。

Windows 下从 WSL 访问、跨机访问这类网络位置问题，最省心的方案始终是反代只对外露 443、8787 留在内网。

### 备份与迁移

schema 迁移是幂等的：artex 每次启动都会重跑 schema.sql（ADD COLUMN / CREATE INDEX IF NOT EXISTS 风格），重启即迁移，不用单独跑迁移命令。`scripts/backup.sh --with-data` 导出带时间戳轮转的数据库 dump 和 data/ 目录归档，psql 可直接还原。

## 使用指南

### 快速开始

1. 1. 起服务，8787 打开控制台，/setup 完成 token 验证和管理员密码
2. 2. 配模型：环境变量塞 key，或者 UI 里直接填；合规敏感的团队用 Ollama 本地模型，目标数据不出内网
3. 3. 建 Task：写目标、圈范围、配 allow/deny、设超时和收尾步骤
4. 4. 盯 SSE 活动流看代理干活，审批门弹出该确认确认
5. 5. 结果进资产图和探索图，出报告；修复后拉 Retest 验证闭环

### 场景示例

授权渗透场景下它最大的价值是耐心和并行度。人做项目只会盯主入口——官网、登录页、API 网关，ARTEX 不是，它会同时去翻那些没人管的地方：供应商门户、移动端后端、员工内部应用、销售支持系统、老服务、第三方集成。FBI 预警里专门点了这些是它最爱下手的位置，因为这些不同业务部门多年前搭起来从没完整盘过点的"遗忘角落"，软凭据都躺在那。它还会自动梳理组织间的信任关系，专挑链条上最弱的供应商或 CI/CD 管线下手——供应链下手这件事在它这里属于默认动作，不需要操作员专门安排。

攻击链没有固定剧本。Datadog 分析的版本里云上后渗透没有固定打法，拿到凭据之后干什么完全取决于背后的模型，两次入侵的细节可以完全不同。没有固定指纹和固定套路可抓，检测只能落在行为上。

## 安全与防护

在野滥用已经一大堆，防守侧能盯的信号：

| 信号 | 位置 | 说明 |
| --- | --- | --- |
| 单源侦察后紧跟利用尝试的爆发式流量 | 防火墙/IDS/NetFlow | 自动化 recon→exploit 管线的典型形态 |
| 秒级密码喷洒、云资源枚举爆发 | IdP/云平台日志 | Microsoft 观测到单地址 2900 次失败登录/分钟 |
| 异常 LLM provider API 调用 | 出口代理/云安全监控 | 代理在受害网络内运行时会外联它的模型...