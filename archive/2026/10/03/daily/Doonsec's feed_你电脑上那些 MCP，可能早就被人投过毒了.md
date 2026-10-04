---
title: 你电脑上那些 MCP，可能早就被人投过毒了
url: https://mp.weixin.qq.com/s/QBHmjBSMy2EAbvh8YZPXag
source: Doonsec's feed
date: 2026-10-03
fetch_date: 2026-10-04T07:36:58.629546
---

# 你电脑上那些 MCP，可能早就被人投过毒了

# 你电脑上那些 MCP，可能早就被人投过毒了

原创

大白
大白

知白守黑1024

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

先说一件已经发生过的事。

2026 年 6 月，微软在 GitHub 上的73 个开源仓库被临时下线，涉及 Azure、Azure-Samples、Microsoft、MicrosoftDocs 四个组织。GitHub 给出的提示是仓库违反了服务条款，实际情况是这些仓库里被推进了恶意提交。

比规模更值得看的，是它怎么触发的。

那条提交没有新增任何依赖，只加了四个配置文件。开发者在本地克隆仓库、用平常的 AI 编辑器把它打开——不装包、不点运行——payload 就以开发者本人的系统权限跑了起来。不弹窗，不二次确认，也没有沙箱。

因为这四个文件，全都是编辑器「约定要自动读」的东西。

![Miasma 攻击链](https://mmbiz.qpic.cn/mmbiz_png/j7ZnQr1RD1iarkzlNIJFDWUvvNLNIjlov3yGDBY0ib4FwehQpDUibGmks5lFicHKAx6sfHSzbpkWW3Jo1huicriaNQJZsAtC5DgMbxAXicxibZmk75g/640?wx_fmt=png&from=appmsg)

一条 commit 加四个配置文件，覆盖四款主流 AI 编辑器

01攻击面，已经挪到你自己电脑上

过去谈 Web 安全，思路是「把服务器守好」。但 AI 编程助手把一大块可信边界搬到了开发者的本机：你装的每一个 MCP 服务器、每一个 agent skill，都在你的机器上、以你的身份运行。

问题出在一个很少被提起的细节上：MCP 的工具描述（tool description）是写给模型看的指令，不是写给用户看的说明文档。它通常被折叠、被截断，你基本不会逐字读完；但模型会把它当成需要遵守的要求。

于是就有了三种典型的投毒方式。

![MCP 工具投毒的三类变体](https://mmbiz.qpic.cn/mmbiz_png/j7ZnQr1RD1iagvdWoNYHBbcFSmhNnjUz2wib2Cqicb8rd4CzTicYHkcJHH4sqlFnWASoRd3jsasRp4YVpmP6MVqxq4Z0Iyf5bBoKn7xKV6pY4BQ/640?wx_fmt=png&from=appmsg)

CSA 归纳的三类变体，以及它们共同的成因

这三种里最容易被忽视的是第二种。它的危险在于「先通过审核、再变坏」——你当初确认的那个工具确实无害，但确认过一次之后，之后服务端返回什么内容，客户端就不再较真了。开头那个微软的案例同源：信任锚在「这是微软的仓库」这个名字上，至于提交往里写了什么，没人再看。

不用假设。2025 年 4 月，Invariant Labs 演示过一个「潜伏型」MCP 服务器：它先挂出一个无害的 get\_fact\_of\_the\_day 小工具，等你批准之后，再把工具描述换成藏有指令的版本，指挥同时连着 WhatsApp 的 agent 去读取完整聊天记录，并把内容塞进一次正常的发消息调用里带出去。这段 payload 藏在 Cursor 界面横向滚动才能看到的位置，用户全程没有察觉。

02主角是一个「先扫自己」的工具

![Snyk Agent Scan 官方终端演示](https://mmbiz.qpic.cn/sz_mmbiz_png/j7ZnQr1RD1hZrZ5UM5KS2NNmibkaibKPHdAX3b25Yu1WtlIib2AibPyT1aVFibfA6aDnCTFggKX6zGER9BEJEUezldibGyk7j3L8c0qKFygnk7ibGM/640?wx_fmt=png&from=appmsg)

mcp-scan 时期的官方演示：一条命令扫出 W001 工具描述异常、E001 提示注入与两条 toxic flow

Snyk Agent Scan，前身就是安全圈熟知的mcp-scan。它出自 Invariant Labs——就是上面做 WhatsApp 演示的那支团队，从 ETH Zurich 分出来，2025 年 6 月 24 日被 Snyk 收购，工具随之改名并继续以开源方式维护。

几个基本事实：仓库累计3,110 Star（2026-10-02 实测），Apache-2.0 许可，2025 年 4 月建仓，最后一次提交在 2026 年 9 月 30 日，仍在活跃维护。需要说明的是，这个项目不接受外部贡献，只收 issue。

它做的事很直接：把本机上所有 agent 组件——编辑器、MCP 服务器、agent skills——找出来，逐个查有没有被投毒、有没有可疑数据流。装完第一条命令，扫的就是你自己。

03它怎么工作

![Agent Scan 工作架构](https://mmbiz.qpic.cn/mmbiz_png/j7ZnQr1RD1jSuL8wg9BMS3BeKor4FcjctBro0nTg3LAwVYjBfKv7DAeiac5bpmDZCUcPicLNqvWXDA3w13rz7zNiayjqo8kFVZ7ibHhGpfktwEQ/640?wx_fmt=png&from=appmsg)

官方文档里的架构示意：一条命令 → 扫描器 → MCP 服务器与 skills

流程拆开是三步：

发现。遍历本机各 agent 的配置路径。覆盖面比想象中宽——Claude Code、Claude Desktop、Cursor、VS Code、GitHub Copilot、Windsurf、Gemini CLI、Amp、Amazon Q、Kiro、OpenCode、Codex 等都在自动发现范围内，并且区分系统级、用户级、项目级、插件级四种配置作用域。

取描述。对每个 MCP 服务器，它要么启动 stdio 进程、要么连接远端 URL，把工具描述拉回来看。这一步是它能查到投毒的原因，也是它最大的风险点——后面会说。

分析。本地检查加云端 API 联合判断，配置里的密钥等敏感值在发出前先做脱敏。

结论以风险指标 + 分数的形式给出，满分 1000 分，分四档：100 低、300 中、600 高、1000 严重。v0.6 版本共覆盖14 类风险，MCP 侧 4 类（工具描述注入、不可信内容、隐私数据、破坏性能力），skill 侧 10 类（提示注入、可疑下载地址、恶意代码、凭据处理、硬编码密钥等）。

04输出长什么样

![Agent Scan v0.6 风险报告](https://mmbiz.qpic.cn/mmbiz_png/j7ZnQr1RD1ia54L2x9l13ibV3DTkrvy3540hicev2uA59RrjmicveIj5p8xlsPHxGvun8EYXP3ibnTYddo6F8fa88f25YbIPzia1TwHNz59VpkDXU/640?wx_fmt=png&from=appmsg)

v0.6 的评分式输出：github 服务器命中 1000/1000 的提示注入，release-helper 命中 600/1000 的可疑下载地址

![Agent Scan v0.5 输出](https://mmbiz.qpic.cn/mmbiz_png/j7ZnQr1RD1iaeDKIuBBY4FwXewh6C6TgWdefoPWZC2j9ugvmuw3hDAIuhiaT8wlOZROjE2icbX8hSooI46UzicttC3qgnaDewjUc7FiamdLDVibLE/640?wx_fmt=png&from=appmsg)

旧版（v0.5.x 线）的问题码输出：E001 严重提示注入，工具描述里直接写着 IGNORE PREVIOUS INSTRUCTIONS

两版输出的差别值得留意：旧版给的是问题码（E/W 开头），新版给的是带分数的风险指标。官方明确说两条输出格式都属于实验性质、可能随版本变动，不建议把某个字段写进生产流程去依赖。

05装机：两条命令的事

它不发 npm 包，官方只提供两种装法：`uvx`免安装运行，或者从 GitHub Releases 下独立二进制。前置条件只有一个：Snyk 免费账号，去账号页生成一个 API Token。

BASH

# 1｜把 Snyk 令牌放进环境变量

export SNYK\_TOKEN=你的令牌

# 2｜扫描整台机器上的 agent、MCP 服务器与 skills

uvx snyk-agent-scan@latest

# 3｜也可以只扫一个配置，或某一批 skill

uvx snyk-agent-scan@latest ~/.vscode/mcp.json

uvx snyk-agent-scan@latest ~/.claude/skills

想接进流水线，用它自带的 CI 模式：有发现就以非零码退出，直接卡住构建。

BASH

# 只做结构探查，不跑安全分析

snyk-agent-scan inspect

# CI 模式：有发现即以非零码退出

snyk-agent-scan --ci --dangerously-run-mcp-servers

# 从源码运行（仓库已 clone 到本地）

uv run pip install -e .

uv run -m src.agent\_scan.cli

官方仓库里还带了一个「故意有洞」的演示 MCP 服务器，配一个 mcp.json 就能复现上面那些发现，适合先拿来练手再扫真环境。

06已经发生的实锤

不是纸上推演。已经确认的漏洞与规模数据里，有四条值得记住：

CVE-2026-33032

nginx-ui 的 MCP 集成里，`/mcp`接口有白名单加鉴权，`/mcp_message`却只查 IP 白名单，而默认白名单是空的——空被当成「全部放行」。任何能访问到它的网络攻击者，都能无鉴权调用全部 MCP 工具，包括重载 nginx 配置。

CVE-2025-54073

典型的命令注入：mcp-package-docs 把未经净化的输入参数直接拼进`child_process.exec`的 shell 命令字符串，最终演变成远程代码执行。

CVE-2026-30623

2026 年 4 月 15 日 OX Security 披露的 LiteLLM 认证后远程命令执行：往 MCP 服务器配置里填任意 command 与 args，LiteLLM 不做校验就直接在宿主机上执行。OX 把这族问题归为「设计层面」的缺陷——根源在 MCP SDK 的 stdio 传输会照单执行拿到的任何命令。

规模数字

OX Security 在 2026 年 4 月的披露里给出量级：约 20 万个存在风险的 MCP 实例、相关软件包累计 1.5 亿次以上下载；CSA 在 5 月的简报里沿用了这组数字。2025 年 7 月 Knostic 做的一次互联网扫描发现 1,862 个暴露在公网的 MCP 服务器，其中手工验证的 119 个全部无需鉴权就能读到工具列表。OWASP 的 MCP Top 10 里，工具投毒排在 MCP03 位。

项目方自己的数据：Snyk 在 2026 年 2 月的 ToxicSkills 研究里扫了 3,984 个公开 agent skill，确认76 个恶意 payload，其中13.4%（534 个）至少含一个严重级问题，发布时仍有至少 8 个恶意 skill 公开可下载。

07用它之前要知道的四件事

一、扫描本身有风险。为了拿到工具描述，它会执行配置里的 stdio 命令、也会向外发起请求。官方建议：扫不可信的第三方配置时，放进 Docker 容器或一次性环境里跑，并且逐条确认它要连的服务器。

二、它盯的是「agent 自己的问题」。官方列出的检测面是提示注入、工具投毒、toxic flow、恶意 skill 这类 agent 原生风险；传统静态分析那一套——第三方库的已知漏洞、弱加密算法、不安全配置——不在它的射程内，要交给别的工具。

三、它是体检，不是疫苗。扫描给出的是某一时刻的结论。Rug Pull 恰恰发生在两次扫描之间，所以真正的防线是持续校验：给工具定义做哈希或版本锁、按工具收敛权限、维护 MCP 服务器白名单。

四、最终判断还得是人。评分能帮你排序，但一个 300 分的「不可信内容」到底能不能接受，取决于你把它和什么东西连在一起用。

回到开头那四个配置文件。它们能得手，靠的从来不是多高明的漏洞，而是没人去看那几行新增的配置。

把 MCP 配置和 skill 文件当成代码来审，把「连接时的信任」换成「每次都验」——工具能帮你把问题摊到桌面上，但这个习惯只能自己养。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/zlD2iah6QpJjciciaI6Ylp5L7rn9Y2O6cTxzf9Suxyw0cwibRgVtpuBzNrqS1ibK3USX8IXHulcNen2rMApDXn352cg/0?wx_fmt=png)

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