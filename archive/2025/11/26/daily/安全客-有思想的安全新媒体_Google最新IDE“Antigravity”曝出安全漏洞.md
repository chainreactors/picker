---
title: Google最新IDE“Antigravity”曝出安全漏洞
url: https://www.anquanke.com/post/id/313413
source: 安全客-有思想的安全新媒体
date: 2025-11-26
fetch_date: 2025-11-27T03:10:47.807752
---

# Google最新IDE“Antigravity”曝出安全漏洞

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# Google最新IDE“Antigravity”曝出安全漏洞

阅读量**23336**

发布时间 : 2025-11-26 18:29:37

**x**

##### 译文声明

本文是翻译文章，文章原作者 wunderwuzzi，文章来源：embracethered

原文地址：<https://embracethered.com/blog/posts/2025/security-keeps-google-antigravity-grounded/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

上周谷歌发布了一款名为 **Antigravity** 的 IDE。它本质上是几个月前 Windsurf 授权协议的产物——谷歌以约 **24 亿美元** 的价格获得了该代码的非独占许可。

由于它基于 Windsurf，我很好奇早在 2025 年 5 月（远在交易之前）我向 Windsurf 报告的漏洞是否已在 Antigravity IDE 中得到修复（详见《Month of AI Bugs》的详细分析）。

**简而言之：没有。**

本文将介绍五个安全漏洞，包括数据泄露漏洞，甚至通过 **间接提示注入实现远程命令执行**。作为外部研究者，尚不清楚为何这些已知漏洞会出现在产品中，但自上周二研究人员开始报告问题后，谷歌已在此处公开记录这些漏洞。我个人猜测，谷歌安全团队对 Antigravity 的仓促发布 **缺乏充分准备**。

目前我暂不公开漏洞利用 payload 细节，主要目的是提高 awareness 并提供实用缓解措施。

### Antigravity 系统提示

作为参考，你可以在此处查看我会话中的系统指令。

![]()

**注意**：我的会话附加了两个 MCP 服务器（可在提示底部看到），因此工具部分包含这些服务器的所有工具。这是“快速”模式的提示。

另外，感谢 p1njc70r 首次公开 Antigravity 系统提示，我认为他分享的是“规划”模式的提示，可在此查看。

让我们开始分析漏洞。

### 漏洞 #1：远程命令执行

Antigravity IDE 默认允许 AI 根据“判断”通过工具执行终端命令。默认设置下，AI 自行决定命令是否“安全”，**无需人工干预**。这本质上是在“赌运气”。

例如，若攻击者尝试运行 `calc.exe` ，由于未执行恶意操作，许多模型（包括 Claude 和 Gemini 3）会允许。但一旦攻击者试图加载远程脚本（如使用 `curl`），多数模型会拒绝请求。但关注我研究的人都知道，这种拒绝仅来自模型的“建议”，而非 **安全边界**。

我通过一些技巧绕过了模型限制，成功让 Antigravity 中的 Gemini 3 和 Claude Sonnet 4.5 执行通过 `curl` 下载并通过 bash 管道运行的任意远程代码：

截图显示，一个源代码文件中的指令劫持 Gemini 3 下载远程脚本并通过 bash 执行（随后启动计算器）。这证明我们可通过远程脚本实现 **任意代码执行**。

![]()

该演示表明，Antigravity 过度依赖 LLM 的“自我约束”来实现安全，这是根本缺陷。

我将其称为 RCE 的原因是它属于间接提示注入，漏洞 #3 会更清晰地体现这一点。

### 漏洞 #2：Antigravity 遵循隐藏指令

Gemini 模型擅长解析 **不可见指令**，而 Gemini 3 尤为突出。这一特性现在也影响到新的 Antigravity IDE。

攻击者可在代码或其他数据源中隐藏指令（在 UI 中对用户不可见），当 Antigravity 将其发送给 Gemini 时，模型会 **执行这些隐藏指令**。这增加了攻击“隐身”成功的可能性。

**演示：通过隐藏指令执行任意命令**
我创建了一个包含不可见指令的文件，要求打印特定文本并调用 `run_command` 下载恶意软件并运行。我使用 ASCII Smuggler 创建/解码隐藏的 Unicode 标签指令。

文件进入聊天上下文后，结果如下：

![]()

这非常危险——代码审查 **无法检测** 此类隐藏指令！

我早在 Bard 时代就首次报告了此弱点，但模型或 API 层面 **从未修复**。因此，所有基于 Gemini 模型构建的应用都继承了此行为。正如我们之前在 Google Jules 中展示的，所有使用 Gemini 的谷歌产品都受此影响。

影响正不断恶化。正如两年前预测的那样，模型能力越强（如 Gemini 3 Fast），绕过安全护栏的可能性越高。

### 漏洞 #3：MCP 缺乏人工干预机制

调用 MCP 服务器工具时，Antigravity IDE 缺少关键安全控制：**完全没有人工干预（HITL）功能**。

这意味着，一旦添加 MCP 工具，间接提示注入攻击或模型幻觉即可调用 **任何工具**。更严重的是，攻击者可通过源代码或 MCP 工具调用中的 **隐藏 Unicode 标签字符** 植入指令。

例如，Linear 工单中隐藏的指令：当开发者通过 MCP 工具调用将工单带入聊天上下文时，远程指令会传递给 LLM，最终导致开发者工作站 **完全被入侵（典型 RCE）**。

![]()

这再次增加了攻击在开发者眼皮底下逃脱检测的可能性。根据工具功能，AI 可在 **无需开发者同意** 的情况下实现数据泄露、代码执行、数据篡改或删除。

微软近期在 GitHub Copilot 中添加的功能值得借鉴：MCP 工具的结果会显示给开发者，由其决定是否纳入提示上下文。

### 当前 MCP 缓解因素与建议

* 可禁用单个工具，这是积极的一面，但目前无法安全启用危险工具。
* 可行的折中方案：工具自动批准，但对标记为 `readOnly`、`destructiveHint` 或 `openWorldHint` 的工具强制 HITL。但需注意，即使 `readOnly` 工具也可能导致数据泄露，因此自动工具调用通常存在风险。
* **最佳实践**：允许客户和企业根据自身风险偏好配置设置。

### 漏洞 #4：通过 `read_url_content` 泄露数据

Antigravity IDE 存在多个数据泄露漏洞，此处描述的漏洞 **继承自 Windsurf**，至少自 2025 年 5 月起就已存在。

问题出在 `read_url_content` 工具，在间接提示注入攻击中可 **无需人工干预** 调用。

![]()

漏洞演示流程：调用 `read_file` 工具读取 `.env` 文件，然后使用 `read_url_content` 工具将文件内容发送给攻击者。

**注意**：攻击 payload 不一定来自源代码文件。如前所示，它可嵌入工具调用响应（如 Linear 工单），或由模型自主触发（如被后门感染）。

### 漏洞 #5：通过图像渲染泄露数据

类似地，AI 可通过 markdown 语法渲染 HTML 图像来泄露数据。我通过在 `.c` 文件中植入提示注入漏洞，快速复现了 Windsurf 中的数据泄露案例：Antigravity 在解释该文件时，调用 `read_file` 工具读取开发者的 `.env` 文件，并通过加载图像的 HTTP 请求将密钥泄露给第三方服务器。

![]()

不止我发现此问题，p1njc70r 也报告了类似情况，并从谷歌获得了相同的敷衍回应。

### 缓解建议

1. 启用 MCP 服务器时需谨慎，禁用危险工具。
2. Antigravity 团队应默认添加 MCP 工具的 **人工干预控制**，并对破坏性工具强制 HITL。
3. 构建 CI/CD 工具以 **自动检测隐藏 Unicode 标签**，手动代码审查无法应对此类攻击。
4. 在问题修复前，开发者应考虑使用替代 IDE。
5. 禁用“自动执行”（默认启用），改用手动批准，并通过“终端命令白名单”仅允许可信命令。
6. 若组织广泛使用此 IDE，建议开展红队/紫队演练以识别检测和监控机会。
7. 随时准备点击“停止”按钮！
8. “深度思考”和“规划”模式对对抗性错位（如提示注入）的抵抗力更强，但 **非万能解药**！

### 结论

本文回顾了 Windsurf 和 8 月“AI 漏洞月”中讨论的常见漏洞。遗憾的是，谷歌最新的 Antigravity IDE 重复了与 Windsurf 相同的错误，而这些漏洞早在 2025 年 5 月就已披露。

技术上，这些漏洞的修复相对简单，只需提供“开箱即用”的安全配置。未来几周 Antigravity 的演进值得关注——安全是否会成为优先事项？

本文翻译自embracethered [原文链接](https://embracethered.com/blog/posts/2025/security-keeps-google-antigravity-grounded/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313413](/post/id/313413)

安全KER - 有思想的安全新媒体

本文转载自: [embracethered](https://embracethered.com/blog/posts/2025/security-keeps-google-antigravity-grounded/)

如若转载,请注明出处： <https://embracethered.com/blog/posts/2025/security-keeps-google-antigravity-grounded/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **740**

* 粉丝
* **6**

### TA的文章

* ##### [英国议会委员会提出立法建议，拟建立软件安全责任制度](/post/id/313382)

  2025-11-26 18:30:59
* ##### [Firefox曝出严重漏洞，致1.8亿用户面临安全风险](/post/id/313385)

  2025-11-26 18:30:35
* ##### [Tor项目全面升级其加密核心，启用新一代洋葱加密机制](/post/id/313391)

  2025-11-26 18:30:03
* ##### [Google最新IDE“Antigravity”曝出安全漏洞](/post/id/313413)

  2025-11-26 18:29:37
* ##### [伪造的“Windows更新”界面正在助推新一波ClickFix社交工程攻击浪潮](/post/id/313431)

  2025-11-26 18:28:44

### 相关文章

* ##### [英国议会委员会提出立法建议，拟建立软件安全责任制度](/post/id/313382)

  2025-11-26 18:30:59
* ##### [Firefox曝出严重漏洞，致1.8亿用户面临安全风险](/post/id/313385)

  2025-11-26 18:30:35
* ##### [Tor项目全面升级其加密核心，启用新一代洋葱加密机制](/post/id/313391)

  2025-11-26 18:30:03
* ##### [伪造的“Windows更新”界面正在助推新一波ClickFix社交工程攻击浪潮](/post/id/313431)

  2025-11-26 18:28:44
* ##### [高级威胁组织ToddyCat升级攻击工具库，新型工具专门窃取Outlook邮件并劫持Microsoft 365访问令牌](/post/id/313434)

  2025-11-26 18:27:40
* ##### [威胁行为体利用Blender基金会官方文件作为载体，传播臭名昭著的StealC V2信息窃取木马](/post/id/313427)

  2025-11-26 18:26:53
* ##### [供应链攻击“Sha1-Hulud”已波及超800个npm软件包与数千个GitHub代码库](/post/id/313439)

  2025-11-26 18:26:16

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)