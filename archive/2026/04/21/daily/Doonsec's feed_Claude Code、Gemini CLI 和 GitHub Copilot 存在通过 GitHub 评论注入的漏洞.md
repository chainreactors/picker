---
title: Claude Code、Gemini CLI 和 GitHub Copilot 存在通过 GitHub 评论注入的漏洞
url: https://mp.weixin.qq.com/s/zvO7JA79mbOKJP8mtfPCuQ
source: Doonsec's feed
date: 2026-04-21
fetch_date: 2026-04-22T04:41:08.785822
---

# Claude Code、Gemini CLI 和 GitHub Copilot 存在通过 GitHub 评论注入的漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7N3EyzEuGufSia4Nvgg7UOk6MwHXmaqiciaU2BX1qibxkSFQ4lOu3a5CURrHdyNPVmBbbrRmp0ZUhpTGTrWd41lwCcocmTguE2q4W0/0?wx_fmt=jpeg)

# Claude Code、Gemini CLI 和 GitHub Copilot 存在通过 GitHub 评论注入的漏洞

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一种名为“评论和控制”的跨供应商关键漏洞类别是一种新型的提示注入攻击，它利用 GitHub 拉取请求标题、问题正文和问题评论来劫持 AI 编码代理，并直接从 CI/CD 环境中窃取 API 密钥和访问令牌。

此次攻击的名称刻意模仿了恶意软件活动中常用的经典命令与控制（C2）框架。经确认，三款广泛部署的人工智能代理程序——Anthropic 的 Claude Code Security Review、Google 的 Gemini CLI Action 和 GitHub Copilot Agent（软件工程代理）——存在漏洞。

据研究员关傲南称，整个攻击循环在 GitHub 内部运行：攻击者编写恶意 PR 标题或问题评论，AI 代理将其读取并作为可信上下文进行处理，执行攻击者提供的指令，并通过 PR 评论、问题评论或 git 提交泄露凭据，无需外部服务器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7Mz3n10zyoZ352icGm7EkTK2Cx1t3Yelf4DD3P4tUxP2jInibtDqQu5ZKkJW1zQalDL6w9ULia4PAOVlTKk1N3TPMq1K7qUq9lwIc/640?wx_fmt=png&from=appmsg)

与经典的间接提示注入不同，后者是被动的，需要受害者明确地请求 AI 处理文档，而评论和控制是主动的：GitHub Actions 工作流会在 <command>  `pull_request`、  <command>`issues`和 `issue_comment` <command> 事件上自动触发，这意味着只需打开 PR 或提交问题即可激活代理，而无需受害者进行任何交互。

## **发现 1：Claude 代码安全审查 — PR 标题与 RCE 有关**

在 Anthropic 的 Claude 代码安全审查操作中，PR 标题会直接插入到代理的提示符中，没有任何清理措施。由于 Claude CLI 的调用没有 `--disallowed-tools` 任何 `--allowed-tools` 限制，子进程会继承所有环境变量，包括 `ANTHROPIC_API_KEY` 和 `GITHUB_TOKEN`。

攻击者只需提交一个恶意标题的 PR，该标题会突破提示上下文，指示 Claude 执行 `cride`  `whoami`、  `ps auxeww``cride` 或 `env` `cride` 命令，并将完整的凭据转储以 JSON 格式的“安全发现”发布到 PR 评论中。该漏洞被 Anthropic 评为 CVSS 9.4 严重级别（从 9.3 升级），并通过 HackerOne 平台报告（#3387969），并获得了 100 美元的赏金。

## **发现 2：Gemini CLI 操作 — API 密钥泄露问题评论**

Google 的 Gemini CLI 操作会将问题标题、正文和评论包含在代理的提示上下文中的“附加内容”部分。攻击者通过在其后立即注入一个伪造的“可信内容部分”，可以绕过 Gemini 的安全指令，导致 Gemini 将内容 `GEMINI_API_KEY` 作为公开问题评论发布，任何人都可以查看。

该漏洞由研究员 Neil Fendley 与约翰·霍普金斯大学的合作者一起向 Google VRP (#1609699) 报告，并获得了 1,337 美元的赏金。

## **发现3：Copilot Agent——三层防御绕过**

GitHub Copilot Agent 的发现技术难度最高。GitHub 实施了三项运行时级别的缓解措施：环境变量过滤、密钥扫描和网络防火墙——但所有这些措施都被绕过了：

* **环境变量过滤绕过：** 该 `UU()` 函数仅过滤子 bash 子进程中的敏感变量。 `ps auxeww` 从该子进程运行会读取 `/proc/[pid]/environ` 未经过滤的父 Node.js 进程和 MCP 服务器，从而恢复 `<path>`  `GITHUB_TOKEN`、`  <path> `GITHUB_COPILOT_API_TOKEN`` 和两个额外的凭据。
* **绕过秘密扫描：**  GitHub 的扫描器会检测 `ghs_`/`ghu_` 标记前缀。在提交之前对输出进行 Base64 编码可以绕过所有模式匹配。
* **防火墙绕过：** 编码后的凭据文件通过标准方式泄露 `git push` 给 PR（白名单操作），使其与正常的 Copilot 工作流程活动无法区分。

为了进一步增强隐蔽性，攻击载荷隐藏在问题正文中的 HTML 注释内，在 GitHub 渲染的 Markdown 视图中不可见，但会被 AI 代理完全解析。

受害者只看到一个看似无害的可见请求，却在不知情的情况下将问题归咎于 Copilot。该漏洞最初通过 HackerOne 平台报告（#3544297），最初被标记为“已知问题”而搁置，但在研究人员提交了 Copilot 压缩包的逆向工程源代码后，该问题被重新开启 `index.js`。GitHub 最终悬赏 500 美元奖励该漏洞的修复者。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7OECRSImGgjiaO2hBgQiaoxjgFHzR8Ptic425tqp73yPjFdkica7biaIFKZoqvv6RS4S0XesnyhkpKd1NVDy1BM5DtjVJB0EicPm9D4M/640?wx_fmt=png&from=appmsg)

这三个漏洞都存在相同的架构缺陷：不受信任的 GitHub 数据流入 AI 代理，该代理在同一个运行时环境中持有生产机密信息和不受限制的工具访问权限。

正如研究人员指出的那样，这是首次公开跨厂商演示单个提示注入模式击败多个主要人工智能代理，其中包括一个部署了三个专用运行时防御机制的代理。

安全专家警告说，这种模式远不止 GitHub Actions，任何处理不受信任输入并能访问工具和密钥的 AI 代理都会受到影响，包括 Slack 机器人、Jira 代理、电子邮件代理和部署自动化管道。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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