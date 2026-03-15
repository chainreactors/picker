---
title: 一个人搭14个AI龙虾员工，两周烧了2000块后我明白了什么
url: https://mp.weixin.qq.com/s/S-D1d2KcFPJrjWfu6Ntltg
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:31:21.051466
---

# 一个人搭14个AI龙虾员工，两周烧了2000块后我明白了什么

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MGmpoYTX6riaXoXxsdJ0loHKcMicxZEF97uCyrL8glVxLUV2FGibtoo2xHwjTHQKict5vdt1lJgT0DmDpsYl0Q8t6S1kDQwTiajjFSZMGV6VVR6M/0?wx_fmt=jpeg)

# 一个人搭14个AI龙虾员工，两周烧了2000块后我明白了什么

原创

AI安全工坊
AI安全工坊

AI安全工坊

![]()

在小说阅读器中沉浸阅读

# OpenClaw养14个AI，烧了2000块

我花了两周时间，在 OpenClaw 里搭了一个企业级多团队架构。

不是那种"3个 AI 员工互相@一下"的玩具demo，是真正按照公司组织架构来的。CoS（幕僚长）、CSO、CFO、CTO、CMO、COO、CPO、CISO、CCO、CHRO、Legal、Intel、VP Infra、Ops……一口气配了 **14 个企业级 Agent**。

然后我发现一个残酷的事实：**OpenClaw 安装是免费的，但运行起来真TM烧钱。**

两周下来，光 token 就烧了 1-2000 块。

这篇文章，就来聊聊我踩过的坑，和普通人为什么不应该碰这玩意儿。

**但先说清楚：我不是炫技，这是我对 OPC（One Person Company）的一次实践。**

作为 AI 自媒体博主，我在探索一人|公司这个模式——人还是我一个，但想提前搞清楚如果未来业务做大了，CSO、CFO、CTO 这些角色到底怎么配合，跨部门协作为什么这么难。OpenClaw 可能明年就过时，但**通过 AI 放大的企业思维会永久沉淀**。

这2000块，是提前交的学费。

---

## 一、企业级多团队架构长什么样？

先说说我搭的这套东西。

打开 `~/.openclaw/agents` 目录，里面是这样的：

```
agents/
├── cos/          # 幕僚长（总调度）
├── cso/          # 首席战略官
├── cfo/          # 首席财务官
├── cmo/          # 首席营销官
├── cpo/          # 首席产品官
├── coo/          # 首席运营官
├── cto/          # 首席技术官
├── ciso/         # 首席信息安全官
├── cco/          # 首席合规官
├── chro/         # 首席人事官
├── legal/        # 法务顾问
├── intel/        # 情报部
├── vp_infra/     # 基础设施VP
└── ops/          # 运营工程师
```

**14 个 Agent，每个都有独立的 workspace、memory、配置文件、Discord 账号。**

这套架构不是平铺直叙的。它是这样工作的：

```
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MGmpoYTX6rjUurU62lqoBiakfO2Z43XpNl3AYQmrfSuI2oP3xPBFeNwGf9mJWat6oheDyu2I1cPTIbeYkBYrToceZvvZHiadHULoHZoTibZjOE/640?wx_fmt=png&from=appmsg)
```

![](https://mmbiz.qpic.cn/mmbiz_png/MGmpoYTX6rgXHNWGOyq7SKj2ADq0Zs9XX1k8hyPNV1DseAP3t7Cz681aUmEXsDAG5qNmjrsXIzJw3a0Lstc6mwuGVjabEgHBoKhxxTkvsuM/640?wx_fmt=png&from=appmsg)

**14 个 Agent 分工**：

| 角色 | 全称 | 职责 | Skills |
| --- | --- | --- | --- |
| 🎯 CoS | Chief of Staff | 总调度，智能派单，唯一对接用户 | 37（专属） |
| 📈 CSO | Chief Strategy Officer | 战略规划、路线图、重大决策 | 10（全局） |
| 💰 CFO | Chief Financial Officer | 预算、成本、财务分析 | 14（专属） |
| 📣 CMO | Chief Marketing Officer | 营销、内容、品牌、增长 | 57（专属） |
| 🎯 CPO | Chief Product Officer | 产品规划、需求、用户体验 | 10（全局） |
| ⚙️ COO | Chief Operating Officer | 执行落地、流程、进度跟踪 | 10（全局） |
| 💻 CTO | Chief Technology Officer | 技术架构、代码、系统设计 | 42（专属） |
| 🔒 CISO | Chief Information Security Officer | 信息安全、风险管理、安全合规 | 10（全局） |
| 📋 CCO | Chief Compliance Officer | 审议把关、合规、风险评估 | 10（全局） |
| 👥 CHRO | Chief Human Resources Officer | 人才、文化、组织、绩效 | 10（全局） |
| ⚖️ Legal | Chief Legal Officer | 合同、法律、知识产权 | 10（全局） |
| 🔍 Intel | Intelligence | 竞品监控、市场趋势、情报收集 | 10（全局） |
| 🏗️ VP\_Infra | VP of Infrastructure | 服务器、部署、可用性保障 | 10（全局） |
| 🛠️ Ops | Operations Engineer | 系统监控、自动化、DevOps | 10（全局） |

**工作流程**：

1. 1. 你在 Discord #总部 频道 @CoS：“帮我做个新产品的技术方案和预算”
2. 2. CoS 判断需要 CTO + CFO，通过 `sessions_spawn` 并行派发
3. 3. CTO 写技术方案，CFO 算成本，各自完成后通过 `announce` 自动回传 Discord
4. 4. CoS 汇总结果，给你完整的方案+预算

听起来很美好对吧？

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MGmpoYTX6rhLPJ2Iiavqe7aM2pk1Q9548KaS9jhMnrEDSUQenNzOFKgN4HOCk7hcauibM61pLRZ8JOyT6wb5Y9srzN8NP67p4Dt8DENGweRZs/640?wx_fmt=jpeg&from=appmsg)

14-Agent协作流程

现实是：这些 Agent 每开一次会，就是几十刀往外扔。

---

## 二、烧钱的三个真相

### 真相1：Multi-Agent 协作 = Token 乘法器

你以为 14 个 Agent 协作，token 消耗是单 Agent 的 14 倍？

错了，是几十倍甚至上百倍。

为什么？因为 Agent-to-Agent 通信需要不断传递上下文：

1. 1. CoS 发一个指令给 CTO
2. 2. CTO 要读取完整的对话历史（几千 tokens）
3. 3. CTO 调用工具（写代码、搜索文档）
4. 4. CTO 生成回复，再通过 announce 回传给 Discord
5. 5. CoS 看到结果后，再委派给 CFO 和 CMO……

这还只是一个简单的任务。如果是复杂项目，CoS 并行 spawn 13 个子 Agent，每个子 Agent 都要读一遍完整上下文，token 就像流水一样没了。

我测过一次，让 CoS + CTO + CFO 开个会，讨论一个新产品的技术方案和预算。

**单次会议：18 美元。**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MGmpoYTX6rjhppfzO3uvwYTLlCIxzCRqk35f9kXy1lOGOhQUfuCzMrhsQMGyOc8Iib1iadEuTjTcXDWdSjrHice6ygOzlq3dvy0QZ3CCE3949A/640?wx_fmt=jpeg&from=appmsg)

Token消耗乘法效应

还有个隐蔽的坑：每个 Agent 启动时都要加载自己的 skills。

举个例子：

* • CoS 装了 37 个 skills（规划/通讯/多 agent 编排）
* • CTO 装了 42 个 skills（架构/安全/K8s/Docker/代码审查）
* • CMO 装了 57 个 skills（社媒全栈/SEO/内容创作/视频）
* • CFO 装了 14 个 skills（金融数据/风险/交易）

每个 skill 在 system prompt 中占 ~150 characters。一个装了 50 个 skills 的 Agent，光启动就吞 7500 字符（~2000 tokens）。

14 个 Agent 一起启动，光 skills 描述就要烧几千 tokens，什么都没干。

### 真相2：记忆系统吃 token 比你想象的狠

OpenClaw 的记忆系统设计得很好，每个 Agent 有独立的 memory 文件，可以跨会话保持上下文。

但这也意味着，每次对话，Agent 都要先读一遍自己的完整记忆。

我的 CoS Agent，两周下来：

* • `MEMORY.md` 文件：20KB+
* • `memory/2026-03-13.md`（每日记忆）：15KB+
* • 每次启动对话，先吞 5000+ tokens

然后生成回复，再写回 memory，又是几千 tokens。

如果你开启了 `memorySearch`（语义检索），还要用 embedding 模型把记忆向量化存进数据库。我用的是 `text-embedding-3-small` 通过 yunwu 中转，成本不高（~¥0.001/万 token），但每天 14 个 Agent 的 embedding 累加起来也是笔钱。

还有 Workspace 文件结构的坑。

每个 Agent 的 workspace 有这些文件：

```
workspace/
├── SOUL.md           # 身份定义（每次加载）
├── AGENTS.md         # 团队花名册（每次加载）
├── IDENTITY.md       # 身份信息（每次加载）
├── USER.md           # 用户偏好（每次加载）
├── TOOLS.md          # 可用工具（每次加载）
├── MEMORY.md         # 长期记忆（每次加载）
├── memory/           # 每日记忆（按需加载）
│   └── 2026-03-13.md
└── work/             # 工作目录（不加载）
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MGmpoYTX6ria9I3vDJ0XK7x6oyibYVdxyJSc1POlJOFZibWA2y4Gg1D1IWBgTutguPhnce98RAIiaHBJ4kG7z9xxBZh0iaTNptyiahCjbrvgstt1g/640?wx_fmt=jpeg&from=appmsg)

Workspace文件加载与Token消耗

除了 work/ 目录，其他文件每次对话都要全部读一遍。

我测了一下，一个配置完善的 Agent，光启动加载这些文件就要吞 8000-10000 tokens。14 个 Agent 并行启动，启动成本就是 10 万 tokens（约 ¥7）。

什么都没干，启动就烧 7 块。

### 真相3：免费安装，贵在运行

OpenClaw 本身是开源的，安装零成本。

但一旦跑起来：

* • 每个 Agent 用的都是 Claude Opus 4.6 或 Sonnet 4.6（调用 API 收费）
* • Multi-Agent 协作会疯狂消耗 token
* • 记忆系统每次启动都要读写几千 tokens
* • 你还没算上 VPS 费用、存储费用、带宽费用

我两周烧了1-2000块，已经算节制的了。因为我做了这些优化：

* • Thinking Budget 分级：CoS 用 16384 tokens，核心 C-Suite 用 12288 tokens，执行层用 8192 tokens
* • 模型混搭：CoS 用 Opus 4.6，核心部门用 Sonnet 4.6，执行层用 GPT-5.4/5.3/5.2
* • 三家 Provider 交叉 Fallback：yunwu → hongmacc → 302ai → gemini，单一 provider 故障时自动切换

如果你不做这些优化，直接全员 Opus 4.6 + 默认配置，一个月烧几万块不是梦。

我在 Discord 上看到有人搞了个 12 人团队（售前、渗透测试、项目经理、财务、运营……），跑了两周直接放弃了，每天烧 300+ 刀。

---

## 三、我踩过的 7 个坑

### 坑1：Discord Bot 4014 错误

14 个 Bot 创建好，Token 配好，OpenClaw Gateway 启动，日志显示 “logged in”，但 Discord 频道发消息完全无反应。日志疯狂报错：

```
[discord] gateway closed with code 4014 (missing privileged gateway intents)
```

原因是 Discord 的 Privileged Gateway Intents（包括 Message Content Intent）默认关闭，而且只能在 Developer Portal 网页手动开启，API 无法操作。

14 个 Bot 逐个去网页点太傻了。可以用 API 批量设置 Application flags（虽然不是 Intent 但能解决问题）：

```
curl --proxy http://127.0.0.1:7890 \
  -X PATCH \
  -H "Authorization: Bot YOUR_BOT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"flags": 8912896}' \
"https://discord.com/api/v10/applications/@me"
```

`8912896` = EMBEDDED + PRESENCE\_LIMITED + MESSAGE\_CONTENT。14 个 Token 跑一遍脚本，3 分钟搞定。

### 坑2：改了配置不生效

修改了 `openclaw.json` 的某个 Agent 配置，重启 Gateway，Agent 行为完全没变。

OpenClaw 的 session 会缓存之前的配置，重启 Gateway 不清缓存。每次改配置后必须手动清 session：

```
find ~/.openclaw/agents/*/sessions/ -type f -delete
openclaw gateway restart
```

我栽过两次：第一次改 Discord 频道 ID 不生效，第二次改 model fallback 不生效。现在养成习惯，改配置 = 先清 session。

### 坑3：Provider 稳定性差异巨大

CoS 回复时 Discord 偶尔显示 “Unexpected event order”，hongmacc 的 codex 模型经常超时。我统计了两周的错误率：

|  |
| --- |
|  |

|  |
| --- |
|  |

| Provider | 错误率 | 说明 |
| --- | --- | --- |
| xxxai | 0% | 最稳定，但 codex 支持有限 |
| xxmacc (Claude) | 1.4% | 偶发流式错误，可接受 |
| xxmacc-openai | 12.9% | codex 流式不稳定 |
| xxwu-gpt | 46.2% | 不稳定，只能当最后 fallback |

### 坑4:想用 Symlink 省空间

325 个 skills 按角色分配到 14 个 workspace，真实复制要占 200+ MB。想用 symlink 节省空间，结果日志报 `Skipping skill path that resolves outside its configured root`。

OpenClaw 对 skill 路径做 realpath 安全检查，要求解析后的真实路径必须在 workspace 根目录内。symlink 指向外部目录会被拒绝。

没办法，只能真实复制。磁盘空间换安全性。

当前目录结构：

```
~/.openclaw/
├── skills/                # 10 个全局通用
├── skills-archive/        # 315 个源文件
├── workspace-cto/skills/  # 真实复制 42 个
├── workspace-cmo/skills/  # 真实复制 57 个
└── ...
```

### 坑5：子 Agent 工作目录串位

CoS spawn CTO 执行任务，CTO 写完代码后，产出文件出现在 CoS 的 workspace 而不是自己的。

因为 subagent 启动时继承 parent 的 cwd（CoS 的 workspace），CTO 没有先 cd 到自己的 workspace。

解决方法是在每个子 Agent 的 `AGENTS.md` 中强制规定，子 session 第一条命令必须 `cd {自己的workspace}/work`，所有产出放 `work/output/` 下。

这个坑很隐蔽，因为 SOUL.md 在 spawn 时不会加载（只有 AGENTS.md + TOOLS.md 加载），所以工作流程规则必须写在 AGENTS.md 里。

### 坑6：安全隐患（官方警告）

**2026年3月10日，国家互联网应急中心发布风险提示**：OpenClaw 在默认配置下存在较高安全风险，攻击者一旦找到漏洞，可轻易获得系统完全控制权。

工信部网络安全平...