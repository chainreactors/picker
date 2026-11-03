---
title: GitHub AI 渗透一周报：本周 8 个新项目（Agent / 框架 / Skills）
url: https://mp.weixin.qq.com/s/nrpQGdoc7ab0C02hlB5hdA
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:45:26.629346
---

# GitHub AI 渗透一周报：本周 8 个新项目（Agent / 框架 / Skills）

# GitHub AI 渗透一周报：本周 8 个新项目（Agent / 框架 / Skills）

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

# GitHub AI 渗透一周报：本周 8 个新项目（Agent / 框架 / Skills）

2026-11-02 · 船山信安 · 数据来自 GitHub 实时 API

这一周 GitHub 上又冒出来一批 AI 渗透相关的开源项目。我们按星标、许可证、语言逐个跑 API 核验，把本号还没写过的挑出来，归成了自治 Agent、编排框架与 Agent Skills 三类。老兵的判断写在后半段——能帮你什么，帮不了什么，哪些地方会出幻觉和误报。

## 一、自治 Agent 与编排框架

这一类是主力，主打「给目标、出结果」。多 Agent 协作、ReAct 推理、从侦察到利用的编排是共同特征。每一个都只做合法授权测试场景。

**Decepticon**（BitterSecurity/Decepticon，6.5k⭐，Python）— 专业自主红队 Agent，跑完整攻击链——侦察、利用、提权、横移、C2，像真实对手那样干，而不是只扫一遍打印报告。仅限合法授权测试。

**defending-code-reference-harness**（anthropics/defending-code-reference-harness，7.7k⭐，Python）— Anthropic 官方出品的 Claude Code 安全技能集（威胁建模 / 扫描 / 分类 / 打补丁），外加一个「侦察-发现-验证-报告-修复」的自主扫描 harness。仅限合法授权测试。

## 二、Agent Skills 与知识库

这一类把「能力」和「知识」喂给通用 Agent，让 Claude Code、Copilot、Cursor 这类客户端直接调起安全动作或方法论。门槛低、落地快，适合个人装完就用。

**hack-skills**（yaklang/hack-skills，2.6k⭐，CSS）— 把渗透方法论写成 Agent 可用的技能文件，让 AI Agent 变成实战黑客，yaklang 团队出品。仅限合法授权测试。

**secknowledge-skill**（Pa55w0rd/secknowledge-skill，439⭐）— Web 与 AI 安全测试知识技能库，沉淀大量真实漏洞案例与安全文档，给 Agent 当检索型知识底座。仅限合法授权测试。

**threat-modeling**（fr33d3m0n/threat-modeling，350⭐，Python）— AI 原生的自动化软件风险分析 / 威胁建模技能，以代码为中心、用 LLM 驱动做安全评估。仅限合法授权测试。

**pentest-skills**（crazyMarky/pentest-skills，352⭐，Python）— 写给 Claude Code 的渗透测试技能集，用自然语言驱动专业级渗透（信息收集、利用、报告）。仅限合法授权测试。

**ghsa-skill-builder**（yhy0/ghsa-skill-builder，75⭐，Python）— 把 GitHub Advisory 漏洞库自动转成结构化安全技能，让 Agent 直接调用最新漏洞知识。仅限合法授权测试。

**Sec-Skills**（boqiqibo/Sec-Skills，54⭐，Python）— 面向大模型的安全 Skills 集合，覆盖常见网络安全动作。仅限合法授权测试。

## 重点项目表（实时星标 / 语言 / 一句话定位）

|  |  |  |  |
| --- | --- | --- | --- |
| 项目 | 星标 | 语言 | 一句话定位 |
| anthropics/defending-code-reference-harness | 7692 | Py | Anthropic 官方 Claude Code 安全技能+自主扫描 harness |
| BitterSecurity/Decepticon | 6511 | Py | 专业自主红队 Agent，跑完整攻击链 |
| yaklang/hack-skills | 2602 | CSS | 把渗透方法论写成 Agent 技能文件 |
| crazyMarky/pentest-skills | 352 | Py | 自然语言驱动专业级渗透测试技能 |
| fr33d3m0n/threat-modeling | 350 | Py | AI 原生自动化软件风险分析 / 威胁建模 |
| Pa55w0rd/secknowledge-skill | 439 | — | Web 与 AI 安全测试知识技能库 |
| yhy0/ghsa-skill-builder | 75 | Py | 把 GitHub Advisory 漏洞库转成安全技能 |
| boqiqibo/Sec-Skills | 54 | Py | 面向大模型的安全 Skills 集合 |

## 老兵判断：能帮什么，帮不了什么

**能帮的：**它们最适合做广度侦察和重复劳动——资产梳理、已知 CVE 匹配、配置审计、CTF 与靶场训练。带技能化封装的（hack-skills、pentest-skills）把方法论标准化，新人上手更快；带知识库的（secknowledge-skill、ghsa-skill-builder）让 Agent 直接调起最新漏洞情报，省下翻文档的时间。

**帮不了的：**业务逻辑漏洞、需要社会工程与现场判断的环节，机器目前还替代不了人。多 Agent 系统在真实大网里容易被卡在「该往哪走」的决策点上，创意链式的攻击路径仍靠人拍板。Defending-code-reference-harness 这类官方 harness 更偏「找洞+补洞」的防御侧流程，进攻场景得自己接工具。

**幻觉与误报：**这是最该警惕的。Agent 会编造不存在的参数、把推测当结论、把扫描噪音报成高危。所有高危结论必须人工复核，不要把 Agent 的输出直接当报告发出去。星标高不等于可靠，先在小靶场验证再上生产环境。

## 合规红线

① 仅限合法授权测试：所有工具只在你拿到书面授权的目标上使用，未经授权不得对任何系统发起测试。

② 本地模型保数据主权：涉及敏感代码与目标信息时，优先用本地或私有化部署的模型，避免数据出域。

③ 不未授权使用：不把自动化能力用于未授权的侦察、利用或数据获取，遵守所在司法辖区的法律法规。

## 开源地址汇总

https://github.com/anthropics/defending-code-reference-harness

https://github.com/BitterSecurity/Decepticon

https://github.com/yaklang/hack-skills

https://github.com/crazyMarky/pentest-skills

https://github.com/fr33d3m0n/threat-modeling

https://github.com/Pa55w0rd/secknowledge-skill

https://github.com/yhy0/ghsa-skill-builder

https://github.com/boqiqibo/Sec-Skills

参考来源：数据截至 2026-11-02，星标以 GitHub 实时 API 为准；许可证与语言取自各仓库元数据。本文仅作技术盘点，不构成使用建议，所有工具仅限合法授权测试场景。

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