---
title: AI安全案例分析xa0| Miasma 蠕虫攻击微软 GitHub
url: https://mp.weixin.qq.com/s/MOMEFpztXDNKRs_Ep48Pjg
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:52:13.067457
---

# AI安全案例分析xa0| Miasma 蠕虫攻击微软 GitHub

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uZT6kWW1jClYLaNFy5lxwxHWPwdv6LoNdsrHOpia9ZiaowicDsnc8rtp7PjGFzQ1R7NZkXALLZ1bj1w3Lx0g0DzSCSUqicib3enlBLrSWeNT9pgA/0?wx_fmt=jpeg)

# AI安全案例分析 | Miasma 蠕虫攻击微软 GitHub

Z2O安全攻防

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于M01N Team
，作者天元实验室

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7uERcmjBkGVib8AMWSKro7Df5WQVQcRsb8cibRD823fTRg/0)

**M01N Team**
.

研战一体，以攻促防，共筑网络安全未来！

![](https://mmbiz.qpic.cn/mmbiz_gif/uZT6kWW1jCmOKaCaN2nkMX6C65RiaDmtvYMSVebviaOWuuaANf7mndH9vLw75lupbzAxFIc43OcpoMFR9hRdz4WC6Zz4jVk55WiajgHrPuBbNs/640?wx_fmt=gif&from=appmsg)

**概述**

2026年6月5日，微软73个GitHub仓库在105秒内被批量禁用，触发封禁的是一个开发者用VS Code打开了一个被污染的项目文件夹。攻击来自 Miasma 蠕虫，一个由 TeamPCP 运营的自复制供应链攻击工具。它把攻击入口从"安装依赖时触发"前移到了"打开项目时触发"。执行这一步的，是 Claude Code、Gemini CLI、Cursor、VS Code 这些 开发者每天都在用的AI 编程工具。

**01 事件背景**

Miasma 蠕虫是 TeamPCP 于 2025 年 9 月在 npm 生态中首次投放的 Shai-Hulud 蠕虫的演化变种，2026 年 5 月以 Mini Shai-Hulud 工具包形式公开发布后，迅速扩散并持续变异。

![](https://mmbiz.qpic.cn/mmbiz_jpg/uZT6kWW1jCnN1OA6tKGk5u7E1rpN7xic1gACmh7sgYOBN5CMEY64tWt5v9Mj5GibhnVtA12ZiaJnqwiclxCP4fy2zz9vsbxpBia5S4X2ibJLQXlnc/640?wx_fmt=jpeg&from=appmsg)

在攻击微软仓库之前，Miasma 已经完成了三波递进式攻击：

* •Wave 1（6 月 1 日）：通过 npm preinstall 钩子投毒 32 个 @redhat-cloud-services 命名空间包，超过 90 个版本受影响，攻击者通过劫持 CI/CD 的 OIDC 发布凭据，将带有 SLSA 供应链完整性签名的恶意包推入 npm 注册表。
* •Wave 2（6 月 3 日）：改用 Phantom Gyp 技术，通过 binding.gyp 文件在 npm install 阶段触发代码执行，绕过大多数只检查 preinstall/postinstall 钩子的安全工具，57 个 npm 包受影响。
* •Wave 3（6 月 3 至 5 日）：完全跳过包管理器，直接向 GitHub 源码仓库推送恶意提交，通过 AI 编程工具和 IDE 的自动化配置触发 payload。微软 73 个仓库在此波次中被波及。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uZT6kWW1jClBgrJJSlHAWMdJmFuSzvILBX7MLVicUm4zRIG0vEaPx5D4NEozhHw1Ftsodf0jVwYv5160JTh8P8pCibGKLbKo6mUPGSXl3n1Ms/640?wx_fmt=png&from=appmsg)

攻击者并非随机选择目标。5 月 19 日微软 durabletask PyPI 包被同一贡献者账号污染时，凭据就已经落入攻击者之手。6 月 5 日，攻击者再度使用这套凭据，向 Azure/durabletask 仓库推送恶意提交。受害账号的Token 17天没轮换，或者已经被蠕虫再次拿下。

**02 攻击机制分析**

Miasma 的 Wave 3 的核心创新是它把攻击触发点从安装依赖前移到了打开项目。一次 git clone 是安全的，只要开发者在任一受支持的工具中打开该目录，payload 就会自动执行。

攻击者向 Azure/durabletask 推送的提交（commit hash: 5f456b8）有几个刻意为之的反常特征：提交说明声称修改了 DataConverter但实际上没有任何源代码变动；时间戳被篡改为 2020 年以规避基于时间的异常检测；提交说明中附带 [skip ci] 标志以阻止 CI 流水线自动扫描。

这次提交新增了 5 个文件，对应 4 个不同的攻击入口，核心 payload 是 .github/setup.js——一个 4.6 MB 的混淆 JavaScript 凭据窃取器。其余 4 个配置文件的作用，是让不同的开发工具在不同触发条件下自动执行这个 payload：

|  |  |  |
| --- | --- | --- |
| **文件路径** | **目标工具** | **触发机制** |
| .claude/settings.json | Claude Code (Anthropic) | SessionStart 钩子，会话启动时自动执行 |
| .gemini/settings.json | Gemini CLI (Google) | SessionStart 钩子，结构与 Claude Code 完全相同 |
| .cursor/rules/setup.mdc | Cursor AI | 提示词注入：alwaysApply: true，诱导 Agent 执行「初始化脚本」 |
| .vscode/tasks.json | VS Code | runOn: folderOpen，打开文件夹时自动触发，无需 AI 介入 |

Cursor 的触发方式是通过 alwaysApply: true 的规则文件向 AI Agent 注入一条指令——运行 setup.js 以完成项目初始化。Agent 会将其识别为合理的项目要求，主动调用执行。这本质上是提示词注入与供应链攻击的结合：攻击者把恶意指令写进仓库配置，让 AI 替自己完成最后一步执行。

当 .github/setup.js 被执行，凭据窃取随即展开。它动态下载适配当前平台（Linux/macOS/Windows）的 Bun 运行时，并在后台执行二阶段 payload，扫描范围覆盖 GitHub Token、npm Token、AWS/Azure/GCP 密钥、SSH Key、Kubeconfig、Docker 配置，以及 shell 历史和浏览器存储的数据。

这套蠕虫的 C2完全运行在 GitHub 本身：攻击者通过三条独立的 GitHub Commit Search 频道下达指令、接收窃取数据，整个通信过程对传统网络层检测工具几乎不可见。拿到新凭据后，payload 继续调用 /user/repos 和 /user/orgs 接口枚举可访问仓库，向更多仓库推送恶意提交，完成下一轮传播。

payload 中的死亡开关会在目标机器上放一个诱饵 Token，名字叫 IfYouInvalidateThisTokenItWillNukeTheComputerOfTheOwner。这个 Token 一旦被吊销，会直接触发 rm -rf ~/，清空开发者机器上的所有数据。管理员如果发现异常去吊销这个 Token，反而可能把开发者整台机器给清掉。

**03 AI 编程工具成为新攻击面**

传统 IDE 更多扮演编辑器角色，而当前的 AI 编程工具已经演化为半自动开发代理——它不只能读取代码，还能根据项目配置主动执行命令、修改文件、调用终端。这种自动化能力是其核心价值所在，也正是它被 Miasma 劫持的根本原因。

Claude Code 的 SessionStart 钩子、Gemini CLI 的会话初始化机制、Cursor 的 alwaysApply 规则……这些功能本身的设计目标是帮助开发者自动完成项目初始化。但当恶意仓库中存在对应配置文件时，这些效率特性就变成了自动执行恶意代码的入口。

攻击者没有突破任何平台漏洞，没有利用任何 CVE。他们是利用了一个深层假设：如果一个配置文件存在于仓库中，工具就应该执行它。这是开发者信任模型的结构性缺陷，而 AI 工具的自动化程度越高，这个缺陷的影响半径就越大。

从攻击演化的角度看，这代表了供应链攻击的第四阶段，攻击者不再等代码被下载或安装，而是等开发者打开项目。攻击目标从「代码怎么被执行」转移到了「代码什么时候被工具自动执行」。

**04 影响范围**

6 月 5 日 UTC 16:00 至 16:02，GitHub 自动封禁系统在 105 秒内禁用了 Microsoft 旗下 Azure、Azure-Samples、Microsoft、MicrosoftDocs 四个组织共 73 个仓库。被封禁的仓库涵盖 Azure Functions、Durable Task 生态、AI 示例项目、连接器 SDK 及文档仓库，包括：

* azure-search-openai-demo（Azure OpenAI RAG 示例，被大量企业参考部署）
* durabletask 及其 .NET、Go、Java、JavaScript、MSSQL 实现
* functions-container-action（Azure Functions 官方 GitHub Action，被封禁期间全球 CI/CD 流水线受阻）
* llm-fine-tuning、windows-driver-docs 等

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uZT6kWW1jCmDrusfMmyVM7sy7XMQd0w3ofnYWPgDvNBR7ScgONfCUtLBOQqS0bDcQvvVXBeWLx6lHjgL9icLvPZnGibYSa3odqXZKtNsQicmo0/640?wx_fmt=jpeg&from=appmsg)

这部分是真实企业开发流程所依赖的基础设施。仓库被禁用期间，依赖这些 Action、SDK 和文档的团队的构建流水线直接中断。截至分析时，Miasma 活跃攻击已累计波及 100+ 组织的 473 个以上包制品，攻击面横跨 npm、PyPI、GitHub Actions 和 AI 工具配置。

**05 防护建议**

Miasma 表明，AI 编程工具已经成为供应链攻击的新入口。对于开发者而言，除了关注依赖包和第三方组件，还需要关注仓库中的 AI 工具配置、IDE 自动任务等非代码文件，因为这些配置同样可能成为恶意代码的触发点。对于接触过受影响仓库的环境，也应及时排查本地配置并轮换相关凭据，避免凭据持续泄露带来的二次传播。

从企业防护角度来看，未来供应链安全需要覆盖整个开发流程，而不仅是代码和制品本身。AI 工具的自动执行能力、开发终端权限以及仓库配置文件都应纳入安全治理范围，避免开发效率功能被攻击者利用，成为新的传播路径。

**06 结语**

Miasma 的攻击全程走在合法轨道上：合法账号、合法提交、合法配置文件、合法工具调用。这使得传统的 SCA 扫描、制品签名验证和依赖审计几乎全部失效。

这个案例揭示了一个供应链安全的新阶段：当 AI 编程工具被广泛接入开发者工作流之后，仓库里的配置文件不再只是项目偏好设置，它们是可执行的攻击载荷投递路径。

开发安全不能再只停留在依赖包扫描上。覆盖范围需要延伸到开发者终端、AI 工具配置文件、IDE 自动任务、凭据生命周期和仓库写入治理。攻击者已经找到了新入口，防守方需要把这个入口纳入威胁模型。

**关于 AISS 安全智链社区**

本案例已收录至 AISS 安全智链社区案例库，社区地址：https://aiss.nsfocus.com/#/

**参考链接**

[1] StepSecurity: Miasma Worm Hits Microsoft Again — https://www.stepsecurity.io/blog/miasma-worm-hits-microsoft-again-azure-functions-action-and-72-other-repositories-disabled-after-supply-chain-attack-targeting-ai-coding-agents

[2] The Hacker News: Miasma Worm Hits 73 Microsoft GitHub Repositories — https://thehackernews.com/2026/06/miasma-worm-hits-73-microsoft-github.html

[3] Microsoft Security Blog: Preinstall to persistence — https://www.microsoft.com/en-us/security/blog/2026/06/02/preinstall-persistence-inside-red-hat-npm-miasma-credential-stealing-campaign/

[4] The Register: Miasma supply-chain attack toolkit goes public — https://www.theregister.com/cyber-crime/2026/06/09/miasma-supply-chain-attack-toolkit-goes-public-on-github/5253074

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

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