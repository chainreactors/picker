---
title: dsh-agentteams-dashboard：把一支 AI 智能体队伍装进一个桌面控制台
url: https://mp.weixin.qq.com/s/WSvdDnkNZdGYD3E499aoSA
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:55:13.366375
---

# dsh-agentteams-dashboard：把一支 AI 智能体队伍装进一个桌面控制台

# dsh-agentteams-dashboard：把一支 AI 智能体队伍装进一个桌面控制台

原创

鸿渐在路上
鸿渐在路上

鸿渐在路上

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

#

**npm**：`dsh-agentteams-dashboard` v0.2.0 · MIT · 2026-10-03 发布 **运行环境**：Node `^22.19.0 || >=24` 它的作用是：把 [AgentTeams](https://github.com/agentscope-ai/AgentTeams) 的多智能体集群，接进 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 的图形界面。

## 什么是它

多智能体集群一旦跑起来，管理就会变成一件麻烦事：Worker 有没有在跑、任务卡在谁那里、聊天记录在哪翻、控制台在哪个端口——都得靠人记。

`dsh-agentteams-dashboard` 把这些收进**一个面板**。装上之后，在 DSH 的主界面里会多出一个 AgentTeams 区域。

它提供三样东西：

**一、AgentTeams 面板**

十个功能页，总览、Worker、任务、聊天、团队、Manager、Human、知识库、审计、设置。

**二、`agentteams_*` 工具**

52 个工具（读 30 个、写 22 个）。装上之后，模型可以直接读集群状态、下指令——**不用切到别的窗口**。

**三、工具卡片**

工具调用的结果会渲染成对话里的卡片，参数、返回结果都能直接看。

---

## 总览页：HELIOS 指挥舱

总览不是一个数据表格，而是一个全屏 3D 场景（three.js，vendor 内置，不请求外部资源）。

场景里的每个元素都对应真实的运行状态：

**地球核心** —— 集群本体

**轨道环** —— 每条倾斜轨道代表一个 Team

**星球** —— 每个 Worker 是一颗星球，可自定义星名别名、色相、类型（岩石 / 气态 / 冰封）、大小

**带行星环的那颗** —— Leader。有决策权的那一个，**靠行星环一眼就能认出来**

**双向流星** —— 消息在轨道之间流动

**HUD 面板** —— 模块导航、核心遥测、集群健康环、实时事件流、事件密度图

交互支持拖拽旋转、滚轮缩放、点击星球锁定查看详情，闲置时自动巡游，也可以全屏。

**点开任意星球会拉出运维抽屉**：唤醒、休眠、确保就绪、删除，以及工具审批、内置工具开关、知识库浏览器。

为什么把 Worker 画成星球而不是方框——星球天然带着轨道、归属和大小差异，而这正好就是 Team 和 Leader 之间关系的形状。

---

## 聊天窗口

不只是文本收发。

**Markdown 和表格能正常渲染**，工具调用会显示成 `🔧 工具名` 加上参数块，思考过程可以折叠，流式输出带光标。

**审批请求是可以直接点的卡片。** 批准、拒绝、取消三个按钮都会直接发 `/approval` 命令——**不需要复制粘贴命令**。

**@ 提及是机器可读的。** 你打 `@某人`，系统会自动解析成 `m.mentions.user_ids`（完整的 Matrix ID）。群聊里 @ 谁就唤醒谁；私聊不需要 @，每条消息自动投递给对方。

**进房间会自动拉取最近 200 条历史消息**，和长轮询的增量按 eventId 去重合并——**不会重复，也不会漏**。

---

## 安装

bash

```
dsh plugin --profile web add dsh-agentteams-dashboard
```

包是纯 ESM，没有构建步骤，也没有运行时依赖。从本地目录装也可以：

bash

```
dsh plugin --profile web add /path/to/agentteam-desktop
```

装完重启目标 profile。如果只改了前端 bundle，刷新页面就行；改了 profile、manifest 或宿主代码才需要重启。

**它依赖 Node `^22.19.0` 或 `>=24`。**

---

## 配置

### 面板里配

打开面板，首次运行会自动进入 Setup 区。填入 controller 地址，加上 token 或者用户名密码，保存即用。

**不需要重启，也不需要改文件。**

保存的值放在 `$DSH_HOME/dsh-agentteams-dashboard.json`（默认 `~/.dsh/`），**文件权限只有属主可读写**。

有个细节做得比较到位：`Test connection` 用真实请求验证凭据，**但不会保存**——错的值会在被写进去之前就失败。

### 写在 profile 里

部署默认值适合写进 `cordis.patch.yml`：

yaml

```
- id: agentteams-dashboard   name: 'dsh-agentteams-dashboard'   config:     controllerUrl: 'http://127.0.0.1:8090'     controllerTokenEnv: 'AGENTTEAMS_AUTH_TOKEN'     matrixHomeserverUrl: 'http://127.0.0.1:18088'     requestTimeoutMs: 10000     resourcePollMs: 15000     infraPollMs: 30000
```

两种方式可以叠加。**优先级是：面板保存的值 > profile 的 config > 环境变量。**

面板里存的凭据永远赢过环境变量。所以在某个恰好导出了旧 token 的 shell 里重启 DSH，**不会悄悄换掉身份**。

聊天走的是 Matrix 长轮询 `/sync`（25 秒挂起、按房间过滤、基于游标），**新消息几乎即时到达，空闲房间不消耗资源**。

---

## 凭据怎么处理

AgentTeams controller 接受 bearer token，而**L2 人的 Matrix access token 本身就是那个 bearer token**。

也就是说——**把它交给浏览器页面，等于交出一个长效的、权限范围很大的凭据。**

这个插件的做法是**把所有凭据留在宿主进程里**：

面板只调用同源的 `/api/agentteams-dashboard/*`，由宿主进程负责附加凭据。**浏览器只能知道来源**（`env` / `file` / `login` / `none`），**拿不到值**。

面板也不会回读已保存的值——它只报告「哪些字段设了」和「哪个来源赢了优先级」。

Token 的读取顺序支持**文件热轮换**：

每次请求都会重新读取 `controllerTokenFile` 指定的文件，**所以运维换文件不需要重启 DSH**。

---

## 部署形态的差异

AgentTeams 有两种部署方式，差别不只是表面：

|  | embedded（单机 Docker） | Kubernetes |
| --- | --- | --- |
| controller | 主机上的 `:8090` | 集群内 Service |
| worker-proxy 端点 | 通过共享 Docker 网络转发到 Worker 应用 | **`503`** ——没有稳定的 Pod DNS 可转发 |

**插件把这个 503 理解为「这个部署模式不暴露它」**，渲染成中性的「仅嵌入式部署 / Kubernetes 模式下不可用」提示，而不是红色报错。

其余功能——项目、任务、聊天、审计、团队——两种模式完全一致，因为它们直连 controller。

同样的处理方式也用在运行时能力上：QwenPaw 运行时不支持的接口（比如 0.2.x 的审批级别 API）会**明确提示**，而不是渲染一个必然失败的按钮。

---

## 工具列表

**读（30 个）**

```
agentteams_status              agentteams_worker_list agentteams_worker_get          agentteams_worker_status agentteams_worker_approval_get agentteams_worker_tools agentteams_worker_skills       agentteams_project_list agentteams_project_workflow    agentteams_project_history agentteams_task_get            agentteams_task_events agentteams_spawn_list          agentteams_spawn_messages agentteams_team_list           agentteams_team_get agentteams_human_list          agentteams_human_get agentteams_manager_list        agentteams_manager_get agentteams_mcp_server_list     agentteams_skill_list agentteams_audit_list          agentteams_gateway_routes agentteams_knowledge_list      agentteams_knowledge_read
```

**写（22 个）**

```
agentteams_worker_create       agentteams_worker_update agentteams_worker_delete       agentteams_worker_wake agentteams_worker_sleep        agentteams_worker_ready agentteams_worker_approval_set agentteams_worker_tool_set agentteams_team_create         agentteams_team_delete agentteams_human_create        agentteams_human_delete agentteams_manager_create      agentteams_manager_delete agentteams_project_create      agentteams_project_pause agentteams_project_resume      agentteams_project_replan agentteams_project_complete    agentteams_task_cancel agentteams_knowledge_write
```

统一返回格式：

json

```
{ "ok": true, "value": { } }
```

json

```
{ "ok": false, "error": { "code": "upstream-error", "message": "…" } }
```

### 一个容易做错的选择

**传输失败会被翻译，业务状态不会。**

controller 用 `403` 和 `404` 来**隐藏某个资源是否存在**。如果中间层「善意地」改写这个状态，要么会泄露资源存在性，要么会让调用方无法区分「被拒绝」和「不存在」。

所以状态码原样透传。

| 错误码 | 状态 | 含义 |
| --- | --- | --- |
| `not-configured` | 503 | 没配 controller 地址或凭据 |
| `upstream-unreachable` | 502 | 连不上 controller |
| `upstream-timeout` | 502 | 超过 `requestTimeoutMs` |
| `upstream-error` | controller 原状态 | 透传 |
| `invalid-input` | 400 / 404 / 405 | 本地拦下的，没打上游 |
| `internal-error` | 500 | 插件自身的问题 |

---

## 版本兼容性

它声明的是开放的 peer 区间：

json

```
"peerDependencies": {   "@deepseek-ai/cordis": "^4.0.1 || ^4.0.4",   "@deepseek-ai/dsh-tools": "^0.1.0-rc.6 || ^0.2.0-rc.1",   "@deepseek-ai/dsh-system-prompt": "^0.1.0-rc.6 || ^0.2.0-rc.1" }
```

然后逐条列出依赖的契约在 `0.2.0-rc.2` 里有没有变——`defineTool`、`ToolDefinition.output`、`execute`、`ctx.webServer.register`、`main` slot、`tool.call.toolview` slot，**全部标注为「未变」**。

如果将来接口会变，它会**响着坏**而不是静默失效：客户端注册错误会在 Web 启动审计里暴露出来，宿主侧不匹配会让插件 fiber 失败，DSH 会报出来。

`npm test` 不需要额外安装，是升级 DSH 之后最快的自检方式。

---

## 一句话

如果你在用 DeepSeek Harness 又在跑 AgentTeams，这个插件把控制台收进同一个界面，**而且它在几个地方守住了边界**——凭据不下放浏览器、不支持的接口不假装支持、业务状态不「善意」翻译。

许可证 MIT，装一条命令。

---

**本文信息来自 npm registry（v0.2.0，2026-10-03 发布，MIT）与官方 README。界面截图为本地运行实例。**

预览时标签不可点

作者提示: 内容由AI生成

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/CBe66ugaImkzTuGpxLlDkuWfRfcuWiaYlKbypOEeluoeT5LhlEDaDmw1ib8BfauticSPGXzrUB3dwPibVbxemlXsLrewQrNFYAsaQOCUMMT6Xvc/0?wx_fmt=png)

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