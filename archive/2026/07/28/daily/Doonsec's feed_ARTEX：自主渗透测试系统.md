---
title: ARTEX：自主渗透测试系统
url: https://mp.weixin.qq.com/s/f3r-Tie_cft32obLvAILLg
source: Doonsec's feed
date: 2026-07-28
fetch_date: 2026-07-29T04:59:58.811890
---

# ARTEX：自主渗透测试系统

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0zk3Ye7cp022ZQx8qGFNzTESrKMLQicRXdqyx9N6naIT7g16HtvmDVj6LO8Bhj0ib9lhsNIaw40hXXPZVbhC258siaJ5gJqKR8N3J8fW5ILYco/0?wx_fmt=jpeg)

# ARTEX：自主渗透测试系统

攻防路
攻防路

攻防录

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

ARTEX 是一个把 AI agent、资产图谱、流量录制和任务编排放进同一套工作台的自主渗透测试系统，后端用 Go，前端用 Next.js，开箱就带 Web UI。

项目地址：http://github.com/Autumn-27/ARTEX
在线 Demo：http://artex-demo.vercel.app/

适用于两类人看：一类是在用 agent 做单点测试的人，另一类是在搭资产平台、自动化平台、攻防工作台的人。这个项目的重点不是聊天界面，而是把目标录入、资产归并、任务拆分、执行留痕和人在环审批串到了一起。

## 技术原理

ARTEX 的核心不是“让 AI 自动点点点”，而是把渗透流程拆成几层稳定的运行单元，再让 agent 在这套约束里工作。

先看它的整体结构：

| 层级 | 作用 | 对应实现 |
| --- | --- | --- |
| 数据层 | 保存资产图、探索图、任务状态、流量记录 | PostgreSQL + `data/traffic` |
| 执行层 | 跑 planner、worker、chat agent | `agent/` |
| 编排层 | 派生子任务、管理目标、处理触发器 | `server/orchestration.go` 、`server/scheduler.go` |
| 安全控制层 | 对高风险工具调用做拦截和审批 | `guard/guard.go` 、`intercept/` |
| 接入层 | MCP、Web UI、录制代理、资产同步 | `mcphttp/` 、`server/`、`sync_scopesentry.go` |

### 1. 双图模型

ARTEX 里有两张图：

1. 资产图，用来存域名、站点、接口、参数、指纹、服务这些结构化对象。
2. 探索图，用来存目标、意图、事实、发现和执行链路。

这两个东西分开，意义很大。

普通 agent 工作流常见的问题，是“把所有上下文都堆在聊天记录里”。轮数一长，模型只知道自己说过什么，却很难稳定回答三个问题：现在已经摸到了哪些入口、哪些方向已经证伪、哪些目标还没完成。

ARTEX 的做法是把结构化信息写回图里。`graph_overview`、`list_assets`、`list_findings` 这些工具不是装饰，它们是 agent 每轮重新建立态势感知的入口。这样一来，任务暂停、页面刷新、甚至换一轮执行，都还能回到同一份状态。

### 2. planner 和 worker 分工

ARTEX 没把一个大模型当万能执行器，而是把任务拆成 planner 和 worker 两类角色。

| 角色 | 主要职责 | 典型行为 |
| --- | --- | --- |
| planner | 看全局态势、拆目标、决定下一步意图 | 读取 `graph_overview`，创建或收束任务 |
| worker | 执行具体测试动作、写回事实和资产 | 调工具、跑命令、登记 `insert_assets`、`report_finding` |
| chat/main agent | 处理人机对话、解释当前进展 | 回答“现在做到哪了”这类问题 |

这种拆法的好处是，规划和执行不抢同一段上下文。

执行 agent 可以把注意力放在当前意图上，比如枚举接口、验证参数、读流量记录。规划 agent 则盯住整场任务状态，负责避免重复探索，也负责在足够证据出现时推进目标完成。

### 3. 流量代理是系统内建能力

ARTEX 有一个很实用的设计：把录制代理直接放进运行时。

从 `server/manager.go`、`agent/worker.go` 这几块代码能看到，流量捕获开启后，系统会把代理地址和 CA 证书注入到 WebFetch、Bash 子命令以及浏览器 MCP 里。结果就是：

* agent 发起的 HTTP 请求能自动被录下来；
* Playwright 这类浏览器动作也能走同一条代理；
* 后续回看时，可以优先查 `traffic_search` / `traffic_get`，不用重复打目标。

这点对真实测试很重要。

很多“AI 渗透”项目只强调自动化执行，但不太处理留痕问题。ARTEX 反过来把“可回放、可复查、可检索”当成一等公民。对团队协作来说，这比单次跑出一个 PoC 更值钱。

### 4. MCP 和平台工具直接进系统

ARTEX 不只是调用外部工具，还把工具管理本身做进了平台。

从 `server/platform_tools.go` 可以看到，它内置了创建和更新 Skill、自定义 Tool、MCP 服务的能力；`mcphttp/client.go` 则补上了 HTTP 传输的 MCP 客户端。换句话说，这个平台不仅让 agent 使用工具，还想让 agent 参与“扩工具”这件事。

这一层和一般的扫描平台差异很大：

| 能力方向 | 常见平台 | ARTEX |
| --- | --- | --- |
| 任务执行 | 扫描器或脚本为主 | agent + tool 协作 |
| 资产管理 | 多为结果列表 | 资产图 + 探索图 |
| 流量复盘 | 常依赖外部代理 | 内建录制代理和检索工具 |
| 工具扩展 | 人工接脚本 | Skill / Custom Tool / MCP 一起管理 |
| 自动编排 | 通常较弱 | 有子任务、触发器、调度器 |

### 5. ScopeSentry 同步解决了“目标从哪来”

很多自主测试平台，最开始就卡在资产喂给谁、怎么喂。

ARTEX 这里补了 ScopeSentry 同步。README 和 `server/sync_scopesentry.go` 里都写得比较清楚：它可以按项目或任务维度把域名、子域、IP、端口、站点、端点这类资产导进来，再归并到平台内部的资产图。

这意味着它不只是适合“我手工输一个 URL，然后让 agent 跑起来”的场景，更适合接到已有 ASM 或资产测绘链路后面。

## 快速上手

下面按 README 里的推荐路径走一遍。

1. 克隆项目

```
git clone https://github.com/Autumn-27/ARTEX.git
cd ARTEX
```

2. 用安装脚本快速部署

```
./install.sh
```

脚本会引导你选择两种模式：

| 模式 | 适合谁 | 特点 |
| --- | --- | --- |
| 全部 Docker | 想快速跑起来 | 自动拉起 ARTEX 和 PostgreSQL |
| 本地编译运行 | 想改代码或二开 | 可自定义数据库和构建方式 |

如果只想先体验，直接走 Docker 路径更省事。默认访问地址是：http://localhost:8787 录制代理端口是：`8788`。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0zk3Ye7cp02xa4T0ooS8tXKdQn4kIhlQXicQMyOgQNLQtdnjicFUSaUCAhd8tLRgUzKxNcFX9RXdI3zXzp67ftSOUIHJNLGpn5uaG3XdHYa1Y/640?wx_fmt=png&from=appmsg)

3. 手动用 Docker Compose 启动

```
cp .env.example .env
docker compose up -d
```

这里至少要填好 `POSTGRES_PASSWORD`。如果你准备直接让 agent 开始探索，还要补 `ANTHROPIC_API_KEY` 或 `OPENAI_API_KEY`。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0zk3Ye7cp02z01Mfg3ZpxU9CVTLazA2kNAdJNfibuiaO6VaDfRAkibibCIdNABJ9PyNtRmhEDpo21QhSLknjDD9MM0XOAZtBOtvGnMS9HFNtPDA/640?wx_fmt=png&from=appmsg)

4. 首次进入界面完成初始化

第一次打开后，会进入初始化页面，设置管理员密码。之后建议先做三件事：

1. 在 LLM 配置页填模型、Base URL 或代理参数。
2. 在系统设置里确认并发 worker 数。
3. 视情况开启流量捕获。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0zk3Ye7cp00SIeA6BKNowibHGgiaslgRvoaQVyD0Xel7yKNdYsPVbv7KVg21QWQMW0SUOAfqRO4yVV99tLzhuE7sIoADk649duYWaAGlQ9tIE/640?wx_fmt=png&from=appmsg)

5. 导入资产或同步 ScopeSentry

如果你本来就有资产库，优先走同步路径；如果没有，也可以先手工建公司范围、录入站点和端点。

![](https://mmbiz.qpic.cn/mmbiz_png/0zk3Ye7cp00KLfPTYzWsZSlribvIicgJ7EqKZgCXoDHgs28PLxuxx780djQaggeicCml4QJqvpero2jcf14B6of5DZj8gQkMq5vhbPEK6IYY8E/640?wx_fmt=png&from=appmsg)

6. 创建任务并观察执行链路

任务跑起来后，可以重点看这几个视图：

* 任务列表：看整体状态和调度情况；
* 会话过程：看 agent 每轮调用了什么工具；
* 探索链路：看目标、事实、发现之间怎么连起来；
* 流量记录：复查请求和响应。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0zk3Ye7cp03p0lHbCicicub7vPnjAL3QiaklFgd4eZHJG8TADaZbicG5QNzp1ib65ONJqnNqPVR0kPYXXZOnxqThONJ82R4ViaphFZ5Rpne0kYSDY/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/0zk3Ye7cp02VBnicd1RlCvjLnks7kPSYk0T3x8481ahA1CzZthEyINZAPHA45R6OCgp4XZ1tVATguwuDvGKXBU9RrIGaCbZPu4DWAjLoSXvU/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/0zk3Ye7cp02cA7FnU4UzMiaWgomyl2n78HNE8U2vytA5FFsOyYMFDs3V4L8tp9uG7rvfmdJTX7icAZrH9fYCFONfDZPyIVsuJaVo3G5KFXFSg/640?wx_fmt=png&from=appmsg)

## 使用场景

### 1. 用在内网或私有化测试环境

任务示例：给一组内部站点做持续探索，把接口、参数和指纹自动沉淀到资产图里。

技术要点：

* PostgreSQL 持久化了状态，任务不会因为聊天窗口关闭直接丢掉。
* 资产图和探索图分离，适合多轮补测。
* 流量录制能让后续人工复核更省时间。

### 2. 接在 ASM 平台后面做二次探索

任务示例：先由 ScopeSentry 这类平台测绘资产，再把结果同步进 ARTEX，让 agent 继续按站点和端点深挖。

技术要点：

* `sync_scopesentry.go` 负责按项目或任务维度拉取资产；
* 导入后直接归并进内部资产图，不用重新建目标；
* 对大型目标来说，比纯手工喂 URL 更稳。

### 3. 用于多 agent 协作排查

任务示例：一个 agent 负责规划，一个 agent 负责执行，人工再通过对话窗口插入提示或审批危险动作。

技术要点：

* `scheduler.go` 支持触发式运行；
* `orchestration.go` 支持子任务和任务级操作；
* chat/main agent 可以单独承接人在环问题，不影响 worker 的执行上下文。

### 4. 做结果留痕和复盘

任务示例：团队里一个人跑自动探索，另一个人稍后接手复盘，核对某个发现是怎么来的。

技术要点：

* 会话、工具调用、流量、事实、发现都在平台内可追溯；
* 录制代理把“执行过什么请求”落到了独立数据层；
* 这类设计更适合团队环境，不只是个人玩具。

## 结尾

ARTEX 这类项目的价值，不在于“能不能全自动打下目标”，而在于它开始认真处理自主测试里最麻烦的几件事：状态持久化、资产组织、执行留痕、工具接入和人在环控制。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7vAmdAO11X4lmHfibkjicia7MkfgkmAZCoKicD7poPsfAkjB9o6vqFNE8stLqAYa4gaHHLSmU42FMuYrNiab6mWBWTg/0?wx_fmt=png)

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