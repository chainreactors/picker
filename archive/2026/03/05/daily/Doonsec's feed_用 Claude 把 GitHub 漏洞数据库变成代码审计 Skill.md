---
title: 用 Claude 把 GitHub 漏洞数据库变成代码审计 Skill
url: https://mp.weixin.qq.com/s/3vdborbClBeBYo4SEFbKjg
source: Doonsec's feed
date: 2026-03-05
fetch_date: 2026-03-06T04:02:23.074511
---

# 用 Claude 把 GitHub 漏洞数据库变成代码审计 Skill

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XicibtbHqiaeHLQhKGZ8BTlKD5YysTl6RliciaZYE4wCXH19BlPelib8QX0PV4IFAvQt8smlaqPz7XOJ5TdfBUuqLtAmH897jZugA7zgQgASM3zRs/0?wx_fmt=jpeg)

# 用 Claude 把 GitHub 漏洞数据库变成代码审计 Skill

原创

yhy0
yhy0

谁不想当剑仙

![]()

在小说阅读器中沉浸阅读

> 让 Claude 自动将 GitHub 公开漏洞数据库转化为代码审计专用的结构化安全技能（Skills）

## 起因

我前段时间做了一个叫纯钧（ChunJun）的 AI 代码审计系统。系统架构上做了不少工作——预扫描、CodeQL、Agent 多阶段验证、对抗反思——但审计效果始终不够理想。

反思了一下，猜测一个可能的原因：**我给 Agent 的只是通用的代码审计思路，它可能还需要一份更具体的漏洞模式知识作为技能。**

比如 SQL 注入，Agent 能依赖的大概就是通用认知——「`cursor.execute()` 使用 f-string 拼接用户输入」。但翻一翻 GitHub Advisory Database 就会发现，真实世界中开发者踩的坑远比这复杂得多：

* asyncmy 通过 dict keys 注入——库只转义 value 不转义 key（CVE-2025-65896）
* ormar 通过 ORM 聚合函数 `min()`/`max()` 注入——开发者以为 ORM 就是安全的（CVE-2026-26198）
* LLM 框架直接拼接用户 prompt 进 SQL——AI 时代的新攻击面（CVE-2024-12909）

这些是**开发者真实会犯的错误**，也是**安全研究人员发现的巧妙绕过思路**。它们被记录在 GitHub Advisory Database 里，大部分都包含了根因分析、修复 commit、CWE 分类等完整信息。

光 Python 生态，CRITICAL + HIGH 级别就有 **3,777 条**，其中 CVSS >= 8.0 的有 **946 条**。

这些都是安全研究人员的成果。但让人一条条去看、分析、提炼？几千条，不现实。

所以想法很简单：**让 Claude 来干这件事——自动拉取、分析、结构化，生成 Agent 能用的安全技能。**

## 思路

拿到这些漏洞数据后，怎么让它们对代码审计真正有用？

最简单的做法是做成知识库，用 RAG 检索——但这不是我这次想做的。我想要的是**更主动的方式**：把漏洞模式提炼成结构化的检测规则，作为 Claude Code Skill 直接加载到 Agent 的工作流中。

核心思路是 **按漏洞原语（Vulnerability Primitive）聚合**：

946 条漏洞不会生成 946 个 Skill。同一种 Source→Sink 模式的漏洞归到同一组，提炼出通用的检测策略，具体 CVE 只是作为案例来佐证。当前已生成 6 个 Skill（注入、路径遍历、认证绕过、反序列化、SSRF、XSS），包含 44 个真实案例。

每个 Skill 核心回答一个问题：**在一个完全陌生的代码库中，怎么系统性地找到这类漏洞？**

不是「这个漏洞是什么」，而是「这类漏洞怎么找」。安全研究员的分析思路和绕过手法，才是最有价值的部分。

## 生成的 Skill 长什么样

每个 Skill 分两层，渐进式加载：

**第一层：Detection Strategy（检测策略）**——Agent 审计时首先加载，定义这类漏洞的通用检测模型。

```
## Detection Strategy

Sources（用户输入入口）：
- request.args, request.json, request.form
- tool_call.arguments（MCP/Agent 场景）
- 配置文件中用户可控的字段

Sinks（危险函数）：
- cursor.execute(), engine.execute()
- Model.objects.extra(where=...), Model.objects.raw()
- asyncmy/PyMySQL 的 dict 参数传递

Sanitization（安全屏障）：
- 参数化查询 (cursor.execute(sql, params))
- ORM 标准查询方法（filter/exclude/get）

检测路径：
1. 搜索 sink 调用
2. 回溯数据流，检查参数是否来自 source
3. 验证路径上是否存在有效 sanitization
4. 无 sanitization → 标记为候选漏洞
```

**第二层：Real-World Cases（真实案例）**——Agent 需要深入验证时按需加载。每个 Case 从真实 GHSA/CVE 的 patch diff 中提炼，包含完整的攻击链分析：

```
### Case N: [package] — [漏洞模式] (CVE-xxxx-yyyy, CVSS x.x)

Root Cause: [一句话根因]

Source → Sink 路径:
- Source: request.form["package"]
- Sink: os.path.join() + open()
- Sanitization Gap: replace() 不处理 ".." 序列

Vulnerable Code Pattern (affected-file.py):
  # 5-15 行真实漏洞代码

Attack Path:
  1. 攻击者通过 [source] 注入 [payload]
  2. 数据经过 [中间处理]
  3. 到达 [sink]，触发 [危害]

Why Standard Scanners Miss It:
- CodeQL: [具体原因]
- Bandit: [具体原因]

How to Detect:
  1. 定位 Sink → 2. 回溯 Source → 3. 验证 Sanitization
```

这种两层结构让 Agent 审计时**先用轻量的检测策略快速扫一遍，发现可疑点再加载具体案例深入确认**——而不是把几千条漏洞全塞进上下文。

## 它怎么工作

ghsa-skill-builder 是一个 Claude Code Skill。放到 `.claude/skills/` 目录下，对 Claude 说一句话就能触发完整流程：

```
拉取最近三年 Python 高危漏洞，生成代码审计 skills
```

Claude 会自动执行：

**全量拉取** → 调用 GitHub Advisory API，分页遍历指定生态的所有漏洞。支持 PIP、GO、NPM 等 7 种生态，支持按时间范围、CVSS 分数过滤。

**拉取完整详情** → 对每条漏洞调用 REST API 获取完整的漏洞描述和 patch commit URL。

**分析漏洞模式** → 按 CWE 分组，获取 patch diff，提取漏洞代码模式和安全研究员的发现思路。

**生成结构化 Skill** → 输出 `vuln-patterns-*/SKILL.md`，包含检测策略和真实案例。

也支持增量检查——定期跑一下，看看有没有新的高危漏洞需要补充到现有 Skill 中：

```
帮我检查一下漏洞 skills 是否需要更新
```

## 数据洞察

拉取 Python 生态全量数据后，一些有意思的发现：

**946 条高危漏洞的 CWE 分布 Top 5：** 代码注入（CWE-94）107 条、反序列化（CWE-502）86 条、路径遍历（CWE-22）81 条、输入验证（CWE-20）59 条、命令注入（CWE-78）46 条。

**AI/LLM 框架漏洞正在爆发。** langchain、vllm、smolagents、langflow、bentoml 等 AI 框架贡献了大量 CVSS 10.0 的漏洞——MCP 工具命令注入（`terminal-controller`，CVSS 10.0）、Agent 沙箱逃逸（`smolagents`，CVSS 9.9）、AI 框架反序列化（`vllm`，CVSS 10.0）。**CVSS 满分漏洞中，AI/LLM 相关的挺多的。**

这也是我觉得这个工具有价值的原因之一：AI 安全是一个快速变化的领域，新的攻击面不断出现，靠人工逐条跟踪效率很低。

## 快速开始

### 前置条件

* Claude Code CLI（任何支持 skills 的Agent）
* GitHub CLI（`gh`，已认证，脚本会自动检测认证状态）
* Python 3.9+、jq
* **推荐**: superpowers 插件 — 其中的 `writing-skills` 技能可确保生成的 Skills 符合质量规范（`/plugin install superpowers@superpowers-marketplace`）

### 安装

```
# 克隆到项目的 .claude/skills/ 目录
cd your-project
mkdir -p .claude/skills
git clone https://github.com/yhy0/ghsa-skill-builder.git .claude/skills/ghsa-skill-builder

# 或克隆到全局 skills 目录（所有项目共享）
git clone https://github.com/yhy0/ghsa-skill-builder.git ~/.claude/skills/ghsa-skill-builder
```

### 使用

在 Claude Code 中直接说：

```
拉取最近三年 Python 高危漏洞，生成代码审计 skills

拉取 Go 生态 CVSS >= 9 的漏洞，生成审计 skills

帮我检查一下漏洞 skills 是否需要更新

分析 GHSA-qhqw-rrw9-25rm 并加到对应的 skill 中
```

脚本也可以独立使用：

```
# 全量拉取 Python 生态索引
python3 scripts/fetch_ghsa.py PIP --since 3y

# 拉取注入类漏洞的完整详情
python3 scripts/fetch_details.py data/pip.json --cwe "77|78|89|94"

# 增量检查
python3 scripts/fetch_ghsa.py PIP --diff

# 支持 7 种生态: PIP | GO | NPM | MAVEN | NUGET | RUBYGEMS | RUST
```

## 项目结构

```
ghsa-skill-builder/
├── SKILL.md                          # Claude 的完整工作手册
├── scripts/
│   ├── fetch_ghsa.py                 # 全量拉取索引（GraphQL 分页）
│   ├── fetch_details.py              # 拉取完整详情（REST API）
│   ├── fetch_ghsa.sh                 # 轻量快速查询（备选）
│   ├── check_existing_skills.py      # 校验已有 skills 的覆盖状态
│   └── _common.py                    # 公共工具（认证检查等）
├── references/
│   ├── skill-structure.md            # vuln-patterns skill 的结构规范
│   └── case-template.md              # 单个漏洞 Case 的格式模板
├── output/                            # 生成的 Skills（可直接复制到目标项目使用）
│   ├── vuln-patterns-injection/
│   ├── vuln-patterns-path-traversal/
│   ├── vuln-patterns-auth-bypass/
│   ├── vuln-patterns-deserialization/
│   ├── vuln-patterns-ssrf/
│   └── vuln-patterns-xss/
└── data/                             # 漏洞索引和详情的本地缓存
    └── {ecosystem}.json
```

## 局限性

* **依赖 Claude 的分析质量** — 生成的 Skill 质量取决于 Claude 对 patch diff 的理解能力，建议人工抽查验证
* **Skill 需要持续更新** — 新漏洞不断出现，建议定期执行增量检查（`--diff`）
* **案例覆盖度有限** — 当前已完成 Python 的 6 类 Skill（injection、path-traversal、auth-bypass、deserialization、ssrf、xss），共 44 个案例，其他类别（如 crypto）待补充

> 以及最主要的当前生成的各种 Skills 真实效果未知，需要测试

项目地址：https://github.com/yhy0/ghsa-skill-builder

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/XicibtbHqiaeHJjCsb2NuWMPxNRUib2E5Zct9EKHn39icGxkxeCQBTEiaLgpJsptziaPIxeVCgybd5hOYIibIottNXicJn4WaTMtRZxTCrFg2bzsciaGI/0?wx_fmt=png)

谁不想当剑仙

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XicibtbHqiaeHJjCsb2NuWMPxNRUib2E5Zct9EKHn39icGxkxeCQBTEiaLgpJsptziaPIxeVCgybd5hOYIibIottNXicJn4WaTMtRZxTCrFg2bzsciaGI/0?wx_fmt=png)

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