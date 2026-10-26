---
title: GitHub AI 渗透红队开源盘点：本周 6 个新项目，星标实时核对
url: https://mp.weixin.qq.com/s/LNizqJrKuhG9q-ryIvg_NQ
source: Doonsec's feed
date: 2026-10-25
fetch_date: 2026-10-26T07:15:02.772983
---

# GitHub AI 渗透红队开源盘点：本周 6 个新项目，星标实时核对

# GitHub AI 渗透红队开源盘点：本周 6 个新项目，星标实时核对

原创

写代码的老兵
写代码的老兵

船山信安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

实战笔记 · PENTEST × AI 安全

# GitHub AI 渗透红队开源盘点：本周 6 个新项目，星标实时核对

船山信安 · 每周开源雷达

2026-10-19 ｜ 数据来自 GitHub API 实时核对

AI 自己上手打渗透、自己给大模型做红队，这件事已经不是 PPT 上的概念。它从一行 demo 跑成了 clone 下来就能用的脚本——但能跑，不等于你能信它。本周我们扫了 GitHub 上新冒头的 AI 渗透与红队项目，挑出本号还没写过的 6 个，星标逐一实时候对。

01

## 按用途分三块看

### 框架与编排类

**LuaN1aoAgent**：把一次渗透拆成 Planner、Executor、Observer 三个角色，用任务图和推理图记录“测到哪、为什么”，每条结论都要挂证据链。自带 Docker 沙箱，强制把执行限制在授权范围内。仅限合法授权测试。

**Deepteam**（confident-ai）：把 LLM 红队拆成 6 个原语——漏洞分类、攻击模拟、评估引擎、多轮推进、护栏。覆盖 OWASP LLM Top 10，能直接当 CI 里的回归测试。仅限合法授权测试。

**PyRIT**（微软）：老牌 AI 红队编排框架，擅长把多步攻击、自定义评分器串成可复现的实验。研究型团队用它做系统性度量。仅限合法授权测试。

### 工具与扫描类

**garak**（NVIDIA）：LLM 漏洞扫描器，靠 probe 生成攻击、detector 打 PASS/FAIL，吐 JSONL 报告。适合把“已知失败模式”扫一遍。仅限合法授权测试。

**promptfoo**：配置驱动的红队与评测，一条 YAML 就能在每次合并跑攻击回归。已被 OpenAI 收编，依然开源 MIT。仅限合法授权测试。

### MCP 与数据集类

**OffensiveSET**（PentesterFlow）：一个 MCP server，专门生成多轮渗透对话数据集，给想微调“会像渗透测试员一样思考”的安全 LLM 的人用。自带失败样例与报告模板。仅限合法授权测试。

02

## 重点项目一览

|  |  |  |  |
| --- | --- | --- | --- |
| 项目 | 实时星标 | 语言 | 一句话定位 |
| LuaN1aoAgent | 1425 | TypeScript | 三角色自主渗透 Agent，证据链可追溯 |
| Deepteam | 3027 | Python | LLM/Agent 红队框架，覆盖 OWASP LLM Top 10 |
| PyRIT | 4648 | Python | 微软 AI 红队编排，多步攻击可复现 |
| garak | 9610 | Python | LLM 漏洞扫描器，JSONL 报告 |
| promptfoo | 26119 | TypeScript | AI 评测与红队，YAML 配置 CI 友好 |
| OffensiveSET | 104 | TypeScript | MCP 数据集生成器，微调安全 LLM 用 |

星标为 2026-10-19 GitHub API 取值，实时可能有浮动。

03

## 老兵的判断

它能帮你省掉三件事：把已知攻击模式自动化（prompt injection、越权、数据泄露，有人写好的探针比人肉点快）；把证据留成报告（JSONL、YAML、CVSS，初稿直接产出）；把回归做成习惯（每次改 prompt、改工具、改模型，自动重跑同一批攻击）。

它帮不了三件事：替代人的判断——工具报 PASS 不代表安全，报 FAIL 也不代表一定被打穿，它测的是“已知探针没踩到失败”，不是“没有漏洞”；发现业务逻辑里的 0day——LLM 看不懂你那套奇怪的优惠叠加规则，跨系统脏逻辑得人盯；保证不误报——幻觉是这类工具的通病，会编一条根本跑不通的命令，也会把正常响应错判成漏洞。

幻觉与误报这条单独拎出来说：任何自动化扫描的结果，都必须有人复核一遍再进报告。直连生产系统做红队更是想都别想——拿个隔离环境、拿个只读副本先跑。

04

## 合规红线

1仅限授权测试：只能打你拥有或书面授权的系统。未授权目标，一个包都不要发。

2本地模型保数据主权：涉及业务数据、代码、凭据的红队任务，优先本地或私有部署的开源模型，别把敏感上下文往外送。

3不未授权使用：工具能力越强越要守边界。把授权范围写进配置，超范围的动作一律不跑。

05

## 开源地址汇总

https://github.com/SanMuzZzZz/LuaN1aoAgent

https://github.com/confident-ai/deepteam

https://github.com/microsoft/PyRIT

https://github.com/NVIDIA/garak

https://github.com/promptfoo/promptfoo

https://github.com/PentesterFlow/OffensiveSET

参考来源

数据截至 2026-10-19，星标以 GitHub 实时为准（本次通过 GitHub API 逐项核对，stars 会随 Star 数变化浮动）。

合规声明：本文仅作技术信息整理与工具介绍，所有项目均须用于合法授权的安全测试与研究；未授权测试、未修复系统的完整利用链、任何绕过防护的实际操作均不在本文讨论范围。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

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