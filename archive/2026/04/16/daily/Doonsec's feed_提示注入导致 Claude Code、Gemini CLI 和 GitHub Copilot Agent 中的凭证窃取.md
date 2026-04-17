---
title: 提示注入导致 Claude Code、Gemini CLI 和 GitHub Copilot Agent 中的凭证窃取
url: https://mp.weixin.qq.com/s/f4DqX-qGX38HnWwE4SzKyA
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:49:14.257709
---

# 提示注入导致 Claude Code、Gemini CLI 和 GitHub Copilot Agent 中的凭证窃取

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/cBGhzWwhSAgptYyJhibwNF3SXU6lr9uicReJtI8ocj6zxWqcpQrX36ZiaTPopSF4VgWCPyr6yxf4gw5GFZfW2AEQMfnIRT1YSlSmBaRbmPy3ss/0?wx_fmt=jpeg)

# 提示注入导致 Claude Code、Gemini CLI 和 GitHub Copilot Agent 中的凭证窃取

原创

🅼🅰🆈
🅼🅰🆈

独眼情报

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![Claude Code Security Review 帖子提取了 API 密钥，这些密钥以 PR 评论的形式呈现，是在 PR 标题提示注入后提取的。](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAiapMcQLSLMO3SvjLicgdOrAuiaM8uxmF0mJyXzQI9htJ3uRVGaqhmynznoQxQRf1eQTavE4DRcG9r0WxPjMvyvbOsUiaeoSRBLQec/640?wx_fmt=png&from=appmsg)

Claude Code Security Review 帖子提取了 API 密钥，这些密钥以 PR 评论的形式呈现，是在 PR 标题提示注入后提取的。

## 长话短说

独立安全研究者 Aonan Guan 联合约翰斯·霍普金斯大学的 Zhengyu Liu 和 Gavin Zhong,在 2025 年 10 月至 2026 年 3 月间陆续向 Anthropic、Google、GitHub 三家披露了同一类提示词注入漏洞——通过 PR 标题、Issue 正文、Issue 评论等 GitHub 用户生成数据,劫持 GitHub Actions 中运行的 AI 代理,窃取仓库的 GitHub Actions 密钥。研究者将这类攻击命名为「**Comment and Control**」,戏仿自传统 C2(Command and Control)——整条攻击链不需要任何外部基础设施,GitHub 自身既是注入面,也是外带通道。

同一套思路在三个不同厂商的产品上全部奏效:Anthropic Claude Code Security Review(PR 标题注入)、Google Gemini CLI Action(Issue 评论伪造「可信内容区」)、GitHub Copilot Agent(HTML 注释隐藏 payload)。GitHub 在 Copilot 上部署了三层额外的运行时防御——环境变量过滤、密钥扫描 API、出站网络白名单,研究者逐一绕过。

三家厂商都支付了赏金,总额 1937 美元,但均未发布公告、未分配 CVE——这是本次事件最值得警觉的点。处于脆弱版本的仓库,按常规漏洞扫描器的工作方式,在可见信号面上等于「无风险」。

**研判**:这不是三个可以打补丁的漏洞,而是一类架构冲突的三次实例化。AI 代理拿着生产密钥去处理外部提交的文本,用的是同一个运行时——「必须读取不可信输入」与「必须持有高权限密钥」这两项要求在当前工程范式里直接对撞。再叠加 VRP(漏洞奖励计划)对新型代理类漏洞的分级惯性,整条发现-披露-修复-通告的链条都出现了系统性钝化。对于自建或外采 AI 代理工作流的团队,现在就需要把「代理账户」当成一名新员工,按最小权限原则重新审计工具清单和密钥边界。

## 事件速览

| 维度 | Claude Code Security Review | Gemini CLI Action | GitHub Copilot Agent |
| --- | --- | --- | --- |
| 所属厂商 | Anthropic | Google | GitHub(Microsoft) |
| 注入面 | PR 标题 | Issue 正文/评论 | Issue 正文中的 HTML 注释 |
| 外带通道 | PR 评论 + Actions 日志 | Issue 评论 | Git 提交的文件 |
| 可窃凭据 | `ANTHROPIC_API_KEY` 、`GITHUB_TOKEN` | `GEMINI_API_KEY` | `GITHUB_TOKEN` 、`GITHUB_COPILOT_API_TOKEN`、`GITHUB_PERSONAL_ACCESS_TOKEN`、`COPILOT_JOB_NONCE` |
| 已有防御层 | 模型层 + 提示词层 | 模型层 + 提示词层 | 模型层 + 提示词层 + 环境过滤 + 密钥扫描 + 网络防火墙 |
| 赏金 | 100 美元 | 1337 美元 | 500 美元 |
| 严重度标记 | CVSS 9.4 Critical(由 9.3 上调) | 未公开 | 「已知架构限制」 |
| CVE/公告 | 无 | 无 | 无 |

上表信息由研究者博客的漏洞矩阵与 The Register 报道交叉核对,关键数字一致。

## 时间线(以研究者博客披露为准)

| 日期 | 事件 |
| --- | --- |
| 2025-10-17 | 通过 HackerOne 向 Anthropic 提交 Claude Code Security Review 漏洞(#3387969) |
| 2025-10-29 | 向 Google VRP 提交 Gemini CLI Action 漏洞(#1609699) |
| 2025-11-25 | Anthropic 定级 CVSS 9.4 Critical,支付 100 美元,仓库更新安全说明 |
| 2026-01-20 | Google 确认并奖励 1337 美元 |
| 2026-02-08 | 通过 HackerOne 向 GitHub 提交 Copilot Agent 漏洞(#3544297) |
| 2026-03-02 | GitHub 将报告以「Informative」关闭,称「已知问题、无法复现」 |
| 2026-03-02 | 研究者提交反编译的 `UU()` 函数和 `zJe` 过滤表,证明运行时被专门设计用于阻止这一路径 |
| 2026-03-04 | GitHub 重开报告 |
| 2026-03-09 | GitHub 支付 500 美元 |
| 2026-04-15 | 研究者公开披露 |

时区默认 UTC,个别节点博客未标注小时级精度,下文讨论时不做小时级假设。

## 共同根因:不是 bug,是架构冲突

三个独立产品、三家互不相干的厂商、三条不同的注入面和外带路径——攻击步骤落到共同的四段式:

```
不可信 GitHub 数据 → AI 代理读取为任务上下文 → 代理执行工具链 → 凭证通过 GitHub 本身外带
```

这一模式在研究者博客里被明确称为「跨厂商首次公开展示」。

这套架构冲突不是 GitHub Actions 独有的。只要满足三个条件——

* (1)代理在处理外部用户生成内容,
* (2)代理持有执行工具(bash、git、HTTP 调用、数据库连接任一),
* (3)代理能访问到生产凭据——攻击面就会以不同形态出现。

研究者在 FAQ 里直接点名 Slack bot、Jira agent、email agent、部署自动化。这个判断跟 TrueFoundry 在 2026 年 4 月 9 日引用的 OWASP Top 10 for Agentic Applications 2026 的排序一致——Agent Goal Hijacking(ASI01)在 2025 年 12 月发布时就被列为首位风险。这不是孤立事件,而是一个方向性的告警信号。

与 2025 年 6 月披露的 EchoLeak(CVE-2025-32711,影响 Microsoft 365 Copilot,CVSS 9.3)、以及 Legit Security 披露的 CamoLeak(CVE-2025-59145,影响 GitHub Copilot Chat,CVSS 9.6)相比,Comment and Control 的威胁模型更贴近「机器钓鱼」:

* EchoLeak、CamoLeak 靠图片/URL 做数据外带,最后被厂商用禁用图片渲染的方式堵上。
* Comment and Control 的外带通道**就是代理的正常输出通道**——PR 评论、Issue 评论、git commit。禁掉这些等于废掉代理。

一句话总结研究者的核心论点:「提示词注入不是 bug,是上下文——代理的本职工作就是去处理它。」

参考：https://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

独眼情报

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

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