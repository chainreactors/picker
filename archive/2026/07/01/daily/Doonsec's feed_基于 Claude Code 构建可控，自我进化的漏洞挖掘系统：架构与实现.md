---
title: 基于 Claude Code 构建可控，自我进化的漏洞挖掘系统：架构与实现
url: https://mp.weixin.qq.com/s/MdTPfyqdtTZghFdmpDzCug
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:52:41.010837
---

# 基于 Claude Code 构建可控，自我进化的漏洞挖掘系统：架构与实现

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eMTyD09PvabKdgNqW7Q7H8LNXNxu0NCEAmZhcuPadU2E04c4t6Vz00yu422nBISY8g3sgUj2iafDsqzD74tqO8C2TZBhvyzo0icAWic7uFaKQE/0?wx_fmt=jpeg)

# 基于 Claude Code 构建可控，自我进化的漏洞挖掘系统：架构与实现

whoami4936
whoami4936

SecurityPaper

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 基于 Claude Code 构建可控，自我进化的漏洞挖掘系统：架构与实现

## 为什么直接让 AI 挖洞会翻车

让 AI 直接做渗透测试，你会遇到五个确定性的失效模式——不是偶发 bug，是 AI 的天性决定的：

**scope 漂移**——AI 看到"有意思"的域名就去戳，忽略授权边界。 **扫描器结果轻信**——AI 直接采信 nuclei 输出，不做独立验证。 **状态遗忘**——上下文压缩后丢失已测记录，重复测或漏测。 **判定不一致**——同一个 CORS `*` 响应，不同时间 AI 给不同结论。 **经验不沉淀**——每次从零开始，不积累有效策略。

这五个问题不是调 prompt 能解决的。我基于 Claude Code 的原生扩展机制搭了套系统，核心思路是**职责分层**：prompt 管 SOP（怎么测），script 管判断（判什么），hook 管边界（能不能跑）。能代码化的绝不写进 prompt。

下面讲这套系统的关键设计。

---

## 整体架构：自包含的 ~/.claude/ 目录

整个系统完全自包含在 `~/.claude/` 下，不依赖外部路径：

```
~/.claude/├── commands/    斜杠命令入口（/hunt）├── hooks/       工具调用前的硬拦截器（scope 强制）├── agents/      角色 + 阶段 SOP（7 个 typed agent + 9 个 exec 模板）├── skills/      工具说明书 + 工具可执行文件（合一）├── bin/         27 个 shim（指向 skills/ 里的可执行文件）├── scripts/     确定性逻辑（11 个 Python 脚本）├── schemas/     数据契约（六态 verdict 枚举）└── workflows/   阶段契约（phase_manifest.json，17 阶段）
```

工具可执行文件和 SKILL.md 放在同一个 `skills/<tool>/` 目录下，bin/ 里的 shim 指向它们。**换机器只需复制 `~/.claude/` + 装运行时（Python/Java），不依赖任何绝对路径。**

---

## 设计一：Skills 让 AI 自动选工具

渗透测试要用一堆工具——FOFA 查资产、httpx 探存活、nuclei 扫漏洞、dirsearch 爆路径。传统做法是写脚本串起来。Claude Code 的 Skills 机制更聪明：你给每个工具写份说明书，AI 自己判断该用哪个。

机制在 SKILL.md 的 description 字段。Claude Code 读所有 skill 的 description，按当前任务语义自动路由：

```
# fofa/SKILL.mddescription: "FOFA 资产收集：子域拉取、反查同集团资产。当用户要做资产发现、按公司名找关联资产时使用。"
```

你说"查这个公司有哪些资产"，AI 自动调 fofa；说"这些 URL 哪些活着"，自动调 httpx。不用你指定工具名。

更关键的是**工具领地设计**——每个 skill 显式声明"何时不用我"，定义工具间边界：

```
# fofa/SKILL.md 的 "不要使用" 段- 存活检测 → httpx（FOFA 只给历史测绘，非实时）- 指纹识别 → xingfinger- 漏洞扫描 → nuclei
```

AI 读到这些边界就不会越权——不会拿 FOFA 去做存活检测（那是 httpx 的活）。

工具的参数正确用法也写在 skill 里。比如 httpx 检测 CDN/WAF 用的是 `-cdn` 参数（不是 `-waf`，这个 flag 不存在）。AI 查 skill 就知道，不用试错。

Skills 的真正价值不只是调公共工具——你可以把自己的私有 POC、定制字典、检测规则都沉淀成 skill，AI 按需自动调用。等于把个人积累的经验变成了一套会自动运转的工具库。

---

## 设计二：侦察并行——collect 串行 + deep 四路 fan-out

侦察阶段最容易慢，因为工具多、步骤长。系统的做法是**拆成两段**：

**第一段 collect（串行）**：资产收集 → DNS 解析 → httpx 存活验证。这三步是强依赖链（DNS 需要 fofa 的子域列表，httpx 需要 DNS 结果），必须串行。产出 `live.txt`。

**第二段 deep（并行）**：live.txt 产出后，coordinator 在一条消息里 spawn 4 个 agent 并行：

```
collect（1 个 agent 串行）→ live.txt  ↓deep（一条消息 spawn 4 个 agent，并行 fan-out）  ├─ xingfinger 指纹        → fp.jsonl  ├─ dirsearch 目录爆破     → dirs.json  ├─ js_extractor JS 分析   → js_analysis/  └─ 认证态识别             → auth_needed.txt
```

关键设计：**每个并行 agent 只读 live.txt，只写自己的专属文件**。原版里 dirsearch 和 js\_extractor 都直接写 `api_candidates.txt`——并行会冲突。改成各自写专属文件（如 `api_candidates_dirs.txt`），合并由 coordinator 在并行结束后一次性做。零文件冲突。

deep 阶段 4 个工具并行，时间从"4 个工具耗时之和"变成"4 个工具耗时的最大值"。

---

## 设计三：三道质量门串行，数据单向流动

这是系统可靠性的核心。17 个阶段里有 7 个 blocking 硬关卡，但流水线本身不稀奇——**真正可靠的是三道质量门。** 数据单向，不可跳过：

```
扫描器产出"候选" → ★验证门 → ★策略归一 → ★事实固化 → 报告
```

### 验证门：不复现不入库

所有扫描器输出只算"候选"，不算漏洞。候选必须经**独立复现**才能入库。验证 agent 新开干净上下文，自己发请求，不照抄扫描器结论。按漏洞类设精确门槛：

| 漏洞类 | CONFIRMED 条件 |
| --- | --- |
| CORS | ACAO 回显 + ACAC=true + 敏感数据 + 跨域可读，四者全满足 |
| SQLi | 布尔差异：`' OR 1=1--` vs `' OR 1=2--` 响应长度真有差 |
| IDOR | 对象 ID 替换 + 双身份响应内容差异 |
| SSRF | OOB 回连可重复 |
| RCE | 命令回显或 OOB，不植入 webshell |

### 策略归一门：代码审稿防误报升级

即使复现了，结论还要过 `verdict_policy.py` 的确定性归一。核心逻辑：按漏洞类检查 impact evidence，**只允许降级不允许升级**。以 Clickjacking 为例：

```
if is_clickjacking(text):    if is_sensitive_action(text) and is_authenticated(text):        return "CONFIRMED"        # 登录后敏感操作可劫持 = 漏洞    if is_public_page(text):        return "INFO_ONLY"        # 公共首页能嵌入 = 不算事    return "AUTH_NEEDED"          # 需登录态验证 = 转队列
```

**这层是代码不是 prompt，所以每次给一样的判断。** AI 说"这是 Clickjacking 漏洞"，代码查这是公共首页还是敏感操作，代码拍板。

### 事实固化门：schema 校验 + 单向渲染

归一后由 `finding_writer.py` 固化。这层做三件事：

**schema 运行时校验**——读 `finding_schema.json` 的 enum 约束校验每条记录。不合规的 verdict 降级 UNCONFIRMED。纯标准库实现（不依赖 jsonschema），enum 从 schema 文件读取，改 schema 即生效。

**全量写入 finding\_records.jsonl**——唯一事实源。

**单向渲染**——报告 agent 只能读 JSON 渲染，不能改 verdict/severity。防止报告层为"好看"而篡改事实。

---

## 设计四：零漏洞不收兵——穷尽式兜底

正常流程跑完（扫描 + 深度挖掘 + 验证），如果 confirmed=0（没挖到任何漏洞），大多数系统会直接收场出报告说"未发现漏洞"。

这套系统不这么干。**verify 产出后如果 confirmed=0，强制触发逐个 URL 穷尽式深挖**——对 live.txt 里的每一个 URL，都做五种深度测试：

1.**全参数 fuzzing**——不只高风险参数，所有参数都试2.**业务逻辑分析**——认证绕过/IDOR/竞态条件/越权，手动构造攻击场景3.**按指纹定制敏感路径**——不只通用列表，Spring Boot 配 actuator 路径、Tomcat 配 manager 路径4.**JS 逐行审计**——不只跑正则提取，读 JS 逻辑找隐藏 API 和前端权限绕过5.**响应差异分析**——对比不同输入（id=1/2/999999/-1/空）的响应差异

**"没挖到"不是跳过的理由，是逐个深挖的触发条件。** 每个新发现追加到候选池，全部深挖完重新跑验证门。如果仍然 confirmed=0，才在报告里诚实记录"已穷尽测试"。

---

## 设计五：Scope 硬约束——hook 代码强制

渗透测试第一红线是 scope。AI 天性是看到有意思的域名就去戳。

Claude Code 的 Hooks 机制给了解法。在 `settings.json` 注册 PreToolUse hook，AI 每次执行命令前先过拦截器。hook 从命令里提取目标（6 种来源：URL 正则/参数/Host header/列表文件/子域命令/MCP 字段），和 `scope.txt` 比对：

•根域覆盖自身 + 所有子域•子域只覆盖自身 + 其下级，不覆盖兄弟域•IP 精确匹配，CIDR 字节级掩码计算

**越界直接 exit 2，AI 根本执行不了那条命令。** 这是"prompt 软约束"和"hook 硬约束"的根本区别——prompt 是请求（AI 可能不听），hook 是强制（绕不过）。

fail 策略的取舍：解析层 fail-open（hook bug 不该卡死所有命令），scope 层 fail-closed（宁可误拦不可放行越界）。

---

## 设计六：双层学习闭环

AI 天然缺陷是"下次从零开始"。系统用两层闭环解决：

**短期闭环（单次内）**——`strategy_feedback.py` 把验证结果反馈成信号权重：CONFIRMED 奏效信号 +8.0，FALSE\_POSITIVE 误导信号 -8.0。权重硬限 [-30, +40]。下一轮候选打分自动加权。

**长期闭环（跨次）**——`reflect-agent` 把 confirmed 漏洞蒸馏成 pattern（指纹→漏洞类→利用方法），追加到全局经验库 `patterns.jsonl`。下次新目标的 recon 阶段查这个库——"这种指纹历史上出过什么洞"——直接定向测。**不是模型变聪明了，是经验库在积累。**

payload 脱敏（`<param>`/`<target>` 占位），不写真实凭据——经验库不变成新的泄露点。

---

## Agent 权限分层

每个 typed agent 的 `tools` 字段按职责精确授权：

| Agent | tools | 理由 |
| --- | --- | --- |
| recon/vuln-scan/verify/exploit | `Bash, Read, Write, Glob, Grep` | 需 shell 跑工具，但不需 Edit |
| report/reflect | `Read, Write, Glob, Grep` | 只读数据，物理上无法碰目标 |
| coordinator | `["*"]` | 调度大脑，需委派所有阶段 |

**最小权限不是靠 prompt 自觉，是靠 tools 字段强制。** report/reflect 没有 Bash——它们物理上无法闯祸。

---

## 设计权衡

**为什么用文件系统做状态存储**——AI 上下文会被压缩丢失，子 agent 间不天然共享记忆。文件系统提供可恢复（中断后检查文件契约从断点继续）、可审计（.audit/ 记录所有命令）、跨 agent 共享（读同一批 .hunt/ 文件）。

**为什么删除了自动 IDOR 检测和自动链式发现脚本**——前者误报率极高（匿名 HTTP 200 就报认证绕过，任何公开页都命中），后者声称探测内网但只拼字符串不发包。两者净贡献为负——高分噪声候选挤占验证预算。删除后 IDOR 和链式发现改由 verify-agent 手动测，质量更高。

**为什么 hook 用 PowerShell 不用 Python**——hook 是安全边界，第一诉求是"永远能跑"。PowerShell 5.1 是 Windows 系统自带（零安装），Python 是用户级安装（换机器可能丢）。代价：PS5.1 按 GBK 读脚本，必须纯 ASCII——中文注释会导致解析崩溃、整个安全边界失效。

---

## 小结

整套系统的核心思路一句话：**把 AI 的不确定性约束在有边界的工程系统里。**

具体落地：prompt 管 SOP，script 管判断，hook 管边界，schema 管数据，skill 管工具，agent 管执行。三道质量门串行保证输出可靠，双层闭环让系统越用越准，零漏洞兜底确保不轻易放过任何目标。

**AI 可以发现、可以判断，但最终拍板的不是它，是代码。**

完整技术文档（含 11 个脚本职责清单、17 阶段定义、数据流图、CVSS 定级矩阵）已整理，关注后回复「Hunter」获取。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/iazag5vDeG2exlukbZwEVKyIohKDySVQPQXJw5KrBSsqITHv1B8mjkLrJ0vJlibicfsHng5MPDsIGD4biaRjziaZX8g/0?wx_fmt=png)

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