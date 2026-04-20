---
title: 从零构建 AI 渗透测试 Agent：TCH 智能渗透黑客松实战复盘
url: https://mp.weixin.qq.com/s/lRp0ztT95JoY1GZdbm8irg
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:55:34.452835
---

# 从零构建 AI 渗透测试 Agent：TCH 智能渗透黑客松实战复盘

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/m5jbNT90t25hZy3nDUiaNnq0dRXfkyMHFbojnOxgac0O0XibL77uPKAxjlzoaDz2kozoNJwaGgHVTGJd6BEN42GViaP4kYdy2fG5kpHhicGia5vg/0?wx_fmt=jpeg)

# 从零构建 AI 渗透测试 Agent：TCH 智能渗透黑客松实战复盘

原创

wgpsec
wgpsec

WgpSec狼组安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**点击蓝字**

![](https://mmbiz.qpic.cn/mmbiz_gif/4LicHRMXdTzCN26evrT4RsqTLtXuGbdV9oQBNHYEQk7MPDOkic6ARSZ7bt0ysicTvWBjg4MbSDfb28fn5PaiaqUSng/640?wx_fmt=gif)

**关注我们**

***声明***

本文作者：WgpSec·AI组

本文字数：18289字

阅读时长：约60分钟

附件/链接：点击查看原文下载

**本文属于【狼组安全社区】原创奖励计划，未经许可禁止转载**

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，狼组安全团队以及文章作者不为此承担任何责任。

狼组安全团队有对此文章的修改和解释权。如欲转载或传播此文章，必须保证此文章的完整性，包括版权声明等全部内容。未经狼组安全团队允许，不得任意修改或者增减此文章内容，不得以任何方式将其用于商业目的。

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4LicHRMXdTzAJOBqtShvMBtBXnAYfHAuziaELxUkYo5Ta1ro6AohToV1RDuFmiaib25w2GypianXgcfVmGR4uSFAdHw/640?wx_fmt=jpeg)](http://mp.weixin.qq.com/s?__biz=MzIyMjkzMzY4Ng==&mid=2247503851&idx=2&sn=8c8c8a70ec6a67177bcd17e612c19330&chksm=e8276832df50e124980c93a3ce2a9d1a863df53ec09163698948d0b385ffbd8f9564161edae7&scene=21#wechat_redirect)

> ❝
>
> 本次大赛由智能渗透主战场与"零界"平行战场组成，两个战场相对独立。 赛事参赛者需以大语言模型为核心构建自主渗透智能体，在隔离架构中逐区突破，完成从漏洞发现、利用执行到攻击路径编排的全流程验证，见证 AI 从“解题能力”向“破网能力”的跃迁。同期推出智能体专属平行战场——“零界”，AI社交，人类禁言。
> **项目开源地址**: https://github.com/wgpsec/tchkiller
> **安全技能skills库：**https://github.com/wgpsec/AboutSecurity
> **环境自动化部署工具:**https://f8x.wgpsec.org

## 一、开篇：让 AI 全自主打比赛

### 主赛场 —— 聚焦 AI 智能体的自主渗透能力

这次第二届 TCH 黑客松的赛制不同于第一届：选手要通过自主渗透智能体，在隔离环境中突破四大赛区渗透场景：

* **识器·明理** — 20+ SRC 场景，侧重自动化众测与主流漏洞发现
* **洞见·虚实** — 典型 CVE、云安全及 AI 基础设施漏洞
* **执刃·循迹** — 多层网络环境，多步攻击规划与权限维持
* **铸剑·止戈** — 企业核心内网域渗透

赛制采用阶梯解锁——Agent 必须在当前赛区达到 flag 提交阈值（14/6/9 个），才能解锁下一赛区。

每道赛题设定一个基础分值。当参赛队伍成功提交正确 Flag 时，最终得分将在基础分值上根据解题名次系数与提示系数进行调整。

也就意味着：第一天就得尽力抢一血，在31名以后题目分值直接扣80%，做了等于白做。不出意外在第一天的时候就遇到了各种问题，程序bug、赛题调度策略没考虑好、调试机会用完，导致第一天没有及时追上，头部队伍在第一天上午，采用先看难题提示，尽快做出抢到一血，解锁下一赛区的策略迅速打到了第三赛区。

复盘来看查看漏洞提示 -10%，如果在第一时间做出来题目抢到一血，其实查看提示这个分值不会有太大影响，还能尽早解锁下一赛区。

| 解题名次 | 分值调整 |
| --- | --- |
| 第1名 | +20% |
| 第2名 | +10% |
| 第3名 | +5% |
| 第11名及以后 | -10% |
| 第21名及以后 | -50% |
| 第31名及以后 | -80% |

**核心挑战：比赛期间选手不能 SSH 登录干预**，Agent 必须 100% 全自主完成：发现目标 → 分析攻击面 → 漏洞利用 → 获取 flag → 提交结果。

并且在本次比赛允许使用国外模型使用claude gemini，这就带来了成本和效率的考量：我是用最贵的模型打完全程？还是控制分配着来？这个在后面我们会讲到。

最终团队在 613 支队伍中排名第 45，解出 35 题。赛道三的多级内网环境成为了我们的软肋——Agent 在内网横向题差 2 个 flag，最终未能进入赛道四。针对第四赛区我们也编写了一个非常详细的ad-pentest-skills，在最后很可惜没有用上。

### 平行赛场："零界"智能体社交平台

"零界"是专为 Agent 打造的社交+策略赛场。人类观察者拥有"上帝视角"审计权，但严禁发言。

这个论坛非常有意思，每个 Agent 拥有独立账号，可进行发帖、评论、私信，并且Agent 之间可通过私信进行情报交换、谈判或策略欺诈。"零界"是专为 Agent 打造的社交+策略赛场。人类观察者拥有"上帝视角"审计权，但严禁发言,最后也是因为各种bug问题导致无法正常跑起来。

本文完整复盘我们基于 claude-agent-sdk 开发的 \*\*tchkiller \*\* 以及零界论坛agent **Aetheris**的设计、实现和比赛的实战迭代过程。

* 完整赛制规则： https://zc.tencent.com/hackathon

## 二、架构设计：把 LLM 放在正确的位置

第一版我们基于pi agent做了一个gui界面的自动化工具，但是后期维护起来太过于麻烦。在临近比赛三周的时候我们花了两天时间使用claude agent sdk重构了一个版本。

![](https://mmbiz.qpic.cn/mmbiz_jpg/m5jbNT90t27wuZWtKvZktAsSnxGLLB8HlAkO7LEvPZiaViaKibNkQhmKF3tReiaIApaqpSGXCoo9llE0U5CibAWcPJ27x9P2tJxciaasRpB6deMb0/640?wx_fmt=jpeg&from=appmsg)

### 基于比赛设计的三层架构

选目标、分配时间、提交 flag——这些决策有明确的规则和边界条件，用脚本执行就行。LLM 负责理解目标系统、规划攻击链、执行渗透操作。

参考这个策略设计了 tchkiller 的三层架构：

```
Layer 0: watchdog.sh         — 进程保活（crontab 调度，崩溃自动重启）
Layer 1: competition.py      — 确定性 Python 编排器（调度、提交、状态管理）
Layer 2: main.py + cc sdk   — AI 渗透引擎（LLM 驱动的攻击执行）
```

完整三层架构

```
Layer 0: watchdog.sh (保活)
  └─ 24h 不间断监控 competition.py
  └─ 崩溃自动重启 + --resume 断点恢复
  └─ 频繁重启保护 (冷却机制)

Layer 1: competition.py (确定性 Python 编排器)
  ├─ TCHPlatform: 官方 HTTP API 客户端 (5 个接口)
  │   ├─ GET  /api/challenges     → 赛题列表 + 进度
  │   ├─ POST /api/start_challenge → 启动实例 → entrypoint
  │   ├─ POST /api/stop_challenge  → 停止实例 (释放槽位)
  │   ├─ POST /api/submit          → 提交 flag
  │   └─ POST /api/hint            → 查看提示 (-10% 分数)
  │
  ├─ Strategy Engine (硬编码规则，不用 LLM)
  │   ├─ 优先级: level → easy → medium → hard
  │   ├─ 超时: easy=15min, medium=25min, hard=45min
  │   ├─ Hint: 第2次失败后自动请求 (hard 题第1次失败后)
  │   ├─ 模式推断: title+description 关键词匹配
  │   └─ 重试: 最多 3 次，每次附加历史信息
  │
  ├─ Worker Pool (1-3 并发，可配置)
  │   ├─ asyncio.Semaphore 控制并发数
  │   ├─ 每个 worker: start → 攻击 → submit → stop
  │   └─ 硬超时保证槽位不会卡死
  │
  └─ State Persistence (JSON，支持断点恢复)
      └─ comp_state.json: 所有赛题进度 + 全局统计

Layer 2: tchkiller (渗透智能体)
  └─ orchestrator + teams + skills + MCP tools
  └─ 一切以攻破赛题获取 flag 为目的
```

#### Layer 0：保活层

watchdog.sh 通过 crontab 定时启动，监控 competition.py 进程状态。如果进程崩溃，自动重启并附加 `--resume` 参数从上次进度恢复。它还内置了频繁重启保护——连续崩溃 5 次后进入冷却期，避免死循环。

#### Layer 1：确定性编排器

这一层是纯 Python，没有 LLM 调用。它负责：

* **竞赛平台交互**：通过官方 API 获取赛题列表、启停实例、提交 flag
* **调度策略**：优先级（easy → medium → hard）、超时控制（easy=15min, medium=25min, hard=45min）、重试逻辑（最多 3 次），后边没想到大家一上来就看提示做难题抢分。
* **并发管理**：Worker Pool 支持 1-3 个并发 worker，30 秒错开启动避免 thundering herd
* **状态持久化**：JSON 文件保存每题的尝试次数、已提交 flag、累计开销，支持中断恢复

为什么不让 LLM 来做调度？我们在早期benchmark中试过——让 AI 决定"接下来应该攻击哪个目标"。结果遇到了 3 个问题

1. 它会反复挑同一道简单题刷（因为"有信心"），而把未尝试的难题一直搁置。
2. 它在评估一个题目做的时间较久认为做不出来后，即使此时远远未达到超时时间,任然强行停止了 worker，让其做其他题目。（这种题目有时是卡在爆破上，得继续投入,而不是提前关闭）
3. 调度 agent 在上游llm 渠道出现 419 限流或者其他问题时，直接导致整个调度逻辑失效。

#### Layer 2：AI 渗透引擎

这是 LLM 真正发挥作用的地方。基于 Claude Agent SDK，主引擎负责：

* 接收目标信息和上下文
* 通过 MCP 工具与目标系统交互
* 执行多轮渗透测试（Orchestrator 模式支持最多 3 轮评估-反馈-迭代循环）
* 保存证据和漏洞报告

**关键设计决策**：每个 worker 运行一个独立的 tchkiller 子进程。这意味着：

* 不同 worker 之间完全隔离（各自的 API key、evidence 目录、provider 配置）
* 一个 worker 崩溃不影响其他 worker
* 每个 worker 可以使用不同的 LLM 提供商，避免 API 配额竞争

## 三、Prompt 工程：把安全专家的经验注入 LLM

Prompt 决定了 Agent 在实战中的表现上限。

### 多层 Prompt 注入架构

```
┌────────────────────────────────────────────────────┐
│ Layer 1: CLAUDE.md — MCP 工具说明 + Skills 用法     │
├────────────────────────────────────────────────────┤
│ Layer 2: System Prompt — 角色 + 渗透方法论 + 规则   │
├────────────────────────────────────────────────────┤
│ Layer 3: User Prompt — 目标 + 模式策略 + 评委反馈   │
└────────────────────────────────────────────────────┘
```

Layer 1 是 Claude Code 启动时自动加载的 CLAUDE.md，内容固定：MCP 工具列表、Skills 调用方式、VulnDB 查询规范。Agent 进入项目目录后就能读到。

Layer 2 的 System Prompt 通过 `build_system_prompt()` 动态构建，包含角色定义、渗透方法论、Last-Mile 利用表、Cookie 决策树、断路器规则、Flag 搜索清单等。这层的内容在 R1/R2/R3 中保持不变。

Layer 3 的 User Prompt 通过 `build_target_prompt()` 逐轮构建，内容随轮次变化：

```
# R1: 完整模板 — 目标 + 赛区策略 + Skill 推荐 + 排除漏洞类型
target_prompt = build_target_prompt(
    target=target, mode=mode, team=True,
    round_num=1, hint=hint,
    exclude_vulns=["missing_header", "tls_ssl"]
)

# R2+: 精简模板 — 跳过侦察 + 注入 Judge 反馈 + 移除 Skill 推荐（由 Judge 精准推荐）
target_prompt = build_target_prompt(
    target=target, mode=mode, team=True,
    round_num=2, extra_prompt=judge_feedback
)
```

R1 和 R2 的 User Prompt 差异很大：R1 注入完整的赛区策略和 top 10 Skill 推荐列表；R2+ 跳过所有侦察模板，直接注入 Judge 返回的 `attack_commands` 和 `recommended_skills`，让 Agent 从上一轮停下的地方继续。

### 赛区策略注入

四个赛区的攻击思路差异很大，我们为每个赛区准备了独立的策略文件（`prompt/modes/*.md`），在 R1 时自动注入到 User Prompt 中：

| 赛区 | 策略文件 | 核心指导 |
| --- | --- | --- |
| 识器·明理（SRC） | `src_hunt.md` | 按参数级别系统测试每个输入点，Header 指纹快速判断技术栈 |
| 洞见·虚实（CVE/云） | `cve_cloud.md` | 精确识别版本号 → search\_vulndb → nuclei 验证 |
| 执刃·循迹（内网） | `network.md` | RCE 优先，SSRF/LFI 读不出所有 flag 时必须 pivot 内网 |
| 铸剑·止戈（域渗透） | `domain.md` | 枚举 → 攻击路径 → 提权 → DCSync，加载 AD 相关 Skill |

比如内网赛区的策略明确写了"不要花超过 15 分钟用 SSRF/LFI 读 flag——如果读不到，说明 flag 在另一台内网机器上，赶紧建隧道"。这种针对性的指导能避免 Agent 在错误方向上耗时间。

R2+ 不再注入赛区策略，因为 R1 已经完成了侦察，后续轮次的方向由 Judge 反馈驱动。

### 双 Agent 架构：渗透 Agent + Judge Agent

单次执行模式的核心问题是：Agent 自行决定何时停止。它经常在发现第一个漏洞后就觉得"任务完成了"，即使还有更多攻击面未覆盖、flag 未提取。

我们的方案是引入 **Judge Agent（评委 Agent）**：

```
Round 1: 渗透 Agent 执行 → 产出 evidence + vulns
         ↓
         Judge Agent 评估（完成度、覆盖面、flag 状态）
         ↓ (未完成)
Round 2: 渗透 Agent + Judge 反馈 → 针对性补充攻击
         ↓
         Judge Agent 再次评估
         ↓ (完成/已达 3 轮上限)
         结束
```

**Judge Agent 的关键设计**：

1. **用廉价模型**：Judge 只做评估不执行，所以用 MiniMax 等快速廉价模型，把 API 预算留给渗透 Agent
2. **结构化输出**：Judge 返回 JSON（`complete`, `confidence`, `feedback`, `attack_commands`, `recommended_skills`），便于程序解析
3. **跨轮记忆**：前一轮 Judge 的决策会注入到下一轮评估中（"我上次建议了 X，Agent 有没有执行？"）
4. **反馈动态注入**：Judge 推荐的具体攻击命令直接注入到 Round 2 的用户提示中

**Judge 推荐 Skill**

系统内置了 78+ 安全方法论 Skill（SQL 注入、X...