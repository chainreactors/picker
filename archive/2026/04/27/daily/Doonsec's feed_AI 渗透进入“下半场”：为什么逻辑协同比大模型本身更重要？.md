---
title: AI 渗透进入“下半场”：为什么逻辑协同比大模型本身更重要？
url: https://mp.weixin.qq.com/s/-MJC6jpQvMsgW6vZan-Tlw
source: Doonsec's feed
date: 2026-04-27
fetch_date: 2026-04-28T05:26:31.824954
---

# AI 渗透进入“下半场”：为什么逻辑协同比大模型本身更重要？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PIWj1VguNouJLHsU1esEBc9717n9QPDZZSTujT7RPibbO4k5HdkOUGAqOPuPmk8icGHYI1oCXBUEkdloWJhYYkPibwiciaCHYFF45361n5nnpCS8/0?wx_fmt=jpeg)

# AI 渗透进入“下半场”：为什么逻辑协同比大模型本身更重要？

原创

APT-101
APT-101

APT-101

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

作为渗透测试工程师的今天，如果你的渗透测试还停留在 **“喂一行 Prompt，等一行结果”** 的原始阶段，那你可能正在错过一场效率革命。

GitHub项目：Pentest AI Agents。它不是一个简单的脚本库，它是为 Claude Code 注入灵魂的 28 个专业子智能体（Subagents）集合。**Pentest AI Agents**。这不仅是一套脚本，更是一套成熟的、可落地的 **AI 渗透测试操作系统**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PIWj1VguNotDhCnUnQvrOnC8FWGNr29fPWSlndDy4h44DCHs7icoLcCv6IjVfPrXEbZb9d5FicETp9HyFoBedtnaXqaFtQV0jMYpUkkJ7nSoE/640?wx_fmt=png&from=appmsg)

---

## 一、 项目定位：从“对话框”走向“作战室”

**一句话定位：** 该项目是专为 Claude Code 设计的 28 个专业子智能体（Subagents）集合。

它将 Claude 从一个通用的语言模型，改造为一个拥有多专业背景、具备文件系统读写权限、且自带安全护栏的红队作战平台。它的目标不是替代专家，而是通过自动化繁琐的侦察、分析与报告环节，让专家回归到最高价值的“逻辑博弈”中。

---

## 二、 架构概览：三层联动体系

项目的整体架构可以概括为：**指令层、逻辑层、数据层**。

* **指令层 (.claude/agents/)**：28 个 `.md` 格式的专家定义。
* **逻辑层 (Swarm Orchestration)**：基于任务路由的编排逻辑，负责在不同阶段调用最合适的专家。
* **数据层 (db/)**：基于 Bash 驱动的 **SQLite 发现数据库**。这是项目的“长期记忆”。

```
项目根目录/├── .claude/agents/          ← 28 个专业 Agent 定义（.md 文件）│   ├── swarm-orchestrator   ← 总指挥（Swarm 编排器）│   ├── engagement-planner   ← 渗透测试规划师│   ├── recon-advisor        ← 侦察与枚举顾问│   ├── web-hunter           ← Web 渗透猎人│   ├── api-security         ← API 安全专家│   ├── vuln-scanner         ← 漏洞扫描专家│   ├── poc-validator        ← PoC 验证专家│   ├── attack-planner       ← 攻击链策划师│   ├── exploit-chainer      ← 漏洞链式利用专家│   ├── ad-attacker          ← Active Directory 攻击专家│   ├── credential-tester    ← 凭证破解专家│   ├── exploit-guide        ← 漏洞利用指南│   ├── bizlogic-hunter      ← 业务逻辑漏洞猎人│   ├── bug-bounty           ← 赏金猎人│   ├── mobile-pentester     ← 移动端渗透专家│   ├── cloud-security       ← 云安全专家（AWS/Azure/GCP）│   ├── cicd-redteam         ← CI/CD 持续红队│   ├── osint-collector      ← OSINT 情报收集│   ├── social-engineer      ← 社会工程学专家│   ├── wireless-pentester   ← 无线网络渗透│   ├── forensics-analyst    ← 数字取证分析师│   ├── malware-analyst      ← 恶意软件分析师│   ├── threat-modeler       ← 威胁建模专家│   ├── detection-engineer   ← 检测规则工程师（蓝队视角）│   ├── report-generator     ← 报告生成器│   ├── privesc-advisor      ← 提权顾问│   ├── stig-analyst         ← STIG 合规分析师│   ├── ctf-solver           ← CTF 解题助手│   └── _scope-guard         ← 范围守卫（安全护栏）├── .claude/commands/        ← 斜杠命令├── db/                      ← Bash 驱动的 SQLite 发现数据库│   ├── findings.sh          ← 工程会话管理 CLI│   ├── handoff.sh           ← Agent 间交接脚本│   ├── schema.sql           ← 7 张表的数据库设计│   └── lib/                 ← 公共库└── examples/                ← 示例输出（报告片段、检测规则等）
```

---

## 三、 核心架构：Swarm 编排体系

该项目模仿了现实中红队小队的协作模式，将渗透测试拆解为 6 个 Phase（阶段）：

1. **规划（Planner）**：委派 `engagement-planner` 生成 MITRE ATT&CK 映射计划与 RoE（交战规则）。
2. **侦察（Recon）**：调用 `recon-advisor` 与 `osint-collector` 建模，结果自动写入 SQLite。
3. **验证（Validator）**：`poc-validator` 负责对漏洞扫描结果进行二阶段验证，过滤 AI 误报。
4. **利用（Exploit）**：`exploit-chainer` 关联多个低危发现，构建端到端攻击路径。

```
Phase 1: 规划阶段┌─────────────────────────────────────────────┐│ swarm-orchestrator (总指挥)                   ││   ↓ 委派给 engagement-planner                ││   → 制定渗透测试计划、MITRE ATT&CK 映射       ││   → 生成 RoE（交战规则）模板                  │└─────────────────────────────────────────────┘Phase 2: 侦察阶段┌─────────────────────────────────────────────┐│ swarm-orchestrator                           ││   ↓ 委派给 recon-advisor                     ││   ↓ 委派给 osint-collector                   ││   ↓ 委派给 web-hunter                        ││   → 收集攻击面情报                           ││   → 端口扫描、子域名枚举、OSINT              │└─────────────────────────────────────────────┘Phase 3: 漏洞分析与验证┌─────────────────────────────────────────────┐│ swarm-orchestrator                           ││   ↓ 委派给 vuln-scanner                     ││   ↓ 委派给 poc-validator                     ││   → 跑 Nuclei/Nessus/OpenVAS                 ││   → 生成 PoC 验证每个发现                    ││   → 过滤误报                                 │└─────────────────────────────────────────────┘Phase 4: 攻击链构建┌─────────────────────────────────────────────┐│ swarm-orchestrator                           ││   ↓ 委派给 attack-planner                    ││   ↓ 委派给 exploit-chainer                   ││   → 关联多工具发现                           ││   → 构建端到端攻击路径                       ││   → 优先级排序                               │└─────────────────────────────────────────────┘Phase 5: 漏洞利用┌─────────────────────────────────────────────┐│ swarm-orchestrator                           ││   ↓ 委派给 exploit-guide                     ││   ↓ 委派给 ad-attacker                       ││   ↓ 委派给 credential-tester                 ││   ↓ 委派给 privesc-advisor                   ││   → 执行利用                                  ││   → 凭证破解                                 ││   → AD 攻击                                  ││   → 权限提升                                 │└─────────────────────────────────────────────┘Phase 6: 报告┌─────────────────────────────────────────────┐│ swarm-orchestrator                           ││   ↓ 委派给 report-generator                  ││   → 生成专业渗透测试报告                     │└─────────────────────────────────────────────┘
```

---

## 四、 Agent 详细分类：28 位“数字专家”

为了保证专业深度，项目将 Agent 细分为七大类别，涵盖了从移动端、云安全到工业合规（STIG）的全场景覆盖。

* **指挥协调类**：`swarm-orchestrator`（总指挥）、`engagement-planner`（规划师）。
* **侦察枚举类**：`recon-advisor`（扫描）、`osint-collector`（情报）、`web-hunter`（Web 猎人）。
* **深度渗透类**：`ad-attacker`（AD 域控）、`api-security`（接口安全）、`cloud-security`（云安全）。
* **利用验证类**：`poc-validator`（PoC 验证）、`exploit-chainer`（漏洞链构建）。
* **特定领域类**：`mobile-pentester`（移动端）、`wireless-pentester`（无线）、`cicd-redteam`（持续红队）。
* **防御与取证类**：`detection-engineer`（检测规则）、`forensics-analyst`（数字取证）。
* **辅助产出类**：`report-generator`（报告生成）、`stig-analyst`（合规分析）。

---

## 五、 安装与使用手册

要驱动这支“数字红队”，你需要按照以下步骤操作：

### 1. 环境准备

确保已安装 **Claude Code**。如果未安装，请执行： `npm install -g @anthropic-ai/claude-code`

### 2. 项目克隆与安装

```
# 克隆项目git clone https://github.com/0xSteph/pentest-ai-agents.gitcd pentest-ai-agents
# 给予安装脚本权限chmod +x install.sh
# 执行安装。建议选 --global 全局安装，方便在任何项目下唤起专家./install.sh --global
```

### 3. 快速启动

在你的渗透测试目标目录下开启 `claude` 终端，直接通过斜杠命令调用：

* **`/swarm`**：启动总指挥模式，自动开始规划和侦察。
* **`/web-hunter`**：专门针对 Web 目标开启深度挖掘。
* **`/report-generator`**：根据 `db/` 下记录的漏洞数据，自动生成 Markdown 报告。

---

## 六、 核心痛点讨论：AI Agent 的工程化“深水区”

在实际使用过程中，有两个 AI 领域的底层问题是任何开发者都无法回避的。Pentest AI Agents 给出了一套极具工程美学的参考答案：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PIWj1VguNouZpdRs1WeFoaIV3CpS4ibPFeKeGBdK2JlJMAI0XnL4lAD9SI019ibRz9zJyicKlpmJf0qiap5LDibCMA3iaNLockiaLGl7RUdqjhnjHQ/640?wx_fmt=png&from=appmsg)

### 1. 上下文大小（Context Window）的极限博弈

**痛点：** 渗透测试产生的 Nmap 扫描结果、HTTP 流量包、目录爆破日志动辄数万行。直接塞进对话，会导致 AI 变得“健忘”甚至产生逻辑崩溃。

**项目的解法：** **物理隔离 + “外挂”索引**。 它利用子智能体（Subagent）机制，让每一个任务都在独立的 Session 中运行。主进程只通过 SQLite 数据库传递资产的 **ID 索引**。

* *例子：* 主 Agent 只告诉 `web-hunter`：“去分析 ID 为 7 的主机。” 子 Agent 随后精准读取数据库中该主机的服务信息。这种 **“按需按量读取”** 的逻辑，绕过了上下文窗口的物理限制。

```
# 智能体能力配置文件定义subagents:  - name: "ad-attacker"    allowed_tools:       - "read_file" # 允许读取扫描结果      - "write_file" # 允许写入攻击路径      - "run_terminal_command"    # 强制预读指令    pre_run_commands:       - "cat ./recon/active_hosts.txt" # 启动即同步状态
```

### 2. 结果协同中的“逻辑断层”问题

**痛点：** 当 Agent A 仅将“扫描结果”传给 Agent B 时，往往丢失了关键的“思考过程”。这可能导致 Agent B 无法理解漏洞的利用环境，从而导致任务失败。

**项目的解法：** **带推理证据的交接（Handoff with Reasoning）**。 在 `handoff.sh` 和各 Agent 的 Prompt 设计中，强制要求输出包含：

* **`Reasoning`（逻辑链）**：我为什么得出这个结论？排除了哪些干扰项？
* **`Evidence`（证据路径）**：支撑结论的原始日志在哪一行？ 通过这种方式，Agent 之间传递的不仅是数据，更是**结构化的知识**。即使后续 Agent 遇到死路，也能通过回溯推理链快速重定位。

```
// 核心调度逻辑：决定何时切换 Agentasync function orchestrator(userInput) {  // 1. 调用 Planner Agent 生成结构化计划  const plan = await callSubagent("engagement-planner", userInput);
  // 2. 解析计划中的任务阶段  const tasks = parseMarkdownPlan(plan);
  for (let task of tasks) {    // 3. 根据任务标签动态选择子 Agent    const agentName = routeToAgent(task.category); // e.g., "web" -> "web-hunter"
    // 4. 传递“上下文简报”而非全量历史    const brief = {      objective: task.description,      prior_findings: await readLocalFile("findings_summary.md"), // 读取共享黑板      evidence_path: "./log...