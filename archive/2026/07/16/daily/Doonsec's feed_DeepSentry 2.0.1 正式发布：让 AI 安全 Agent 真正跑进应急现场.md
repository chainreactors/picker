---
title: DeepSentry 2.0.1 正式发布：让 AI 安全 Agent 真正跑进应急现场
url: https://mp.weixin.qq.com/s/jsOyLcJORUrLotkCBjGt1g
source: Doonsec's feed
date: 2026-07-16
fetch_date: 2026-07-17T04:55:46.985121
---

# DeepSentry 2.0.1 正式发布：让 AI 安全 Agent 真正跑进应急现场

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUTQGRQ4GO92jMZxiagYIV4EuficzyK09FLvnAauH00SRxeCVZTekNIvHMIibJbz439qFiaiaiaWpibAcBQHsxKtc1lqAmbKNhL4lJff2GcX4Ldm2U/0?wx_fmt=jpeg)

# DeepSentry 2.0.1 正式发布：让 AI 安全 Agent 真正跑进应急现场

Hx0战队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

编者荐语：

DeepSentry 2.0.1 重磅开源！告别“人工敲命令+翻日志”的低效模式，这款AI安全Agent支持自然语言驱动，内置60+工具，可直连现场执行任务并生成报告。真正让AI从“给建议”进化到“干实事”，安全应急与运维必备神器！

以下文章来源于Hx0极客圈
，作者asaotomo

![](https://wx.qlogo.cn/mmhead/rqvn1hjHytedfdS681PB4EroprjS2nmYaD5EibbpYicfwoZVQiaiavVZEBTaybhia7ZibDxjt0LMcWS8s/0)

**Hx0极客圈**
.

我们致力于将 AI 赋能于安全，用极客精神重塑工具。

> 摘要：DeepSentry 2.0.1 Ultimate 正式开源：支持自然语言驱动、60 个安全运维工具、本地/远程/Fleet 执行、多 Agent 协作与可审计报告，让 AI 真正参与安全应急、智能运维和攻防值守。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOibworDwZ3OOdOyqUJ40utAaF6l6nKXG8oaSsehxxT29hl9DOhia6gbSAHhYkMxHCJowkiaMl31Fx9GJRobN6kMaia6L9xgrEfe6YY/640?wx_fmt=png&from=appmsg)

# 如果把大模型接进终端，就能得到一个“AI 安全工程师”吗？

我们越来越确定：不能。

真正的安全工作，不是让模型解释一条命令，也不是把日志复制进对话框里等待总结。一次完整的排查，往往要经历目标确认、信息收集、日志筛选、进程与网络关联、可疑文件复核、风险判断、处置建议和报告留痕。远程连接会中断，输出可能很长，目标机可能缺少工具，高风险操作还必须经过确认。

所以，我们继续打磨 DeepSentry。

今天，DeepSentry v2.0.1 Ultimate 正式发布并开源。

它不是一个只会给建议的安全聊天机器人，而是一个能够在授权环境中真正执行任务的AI 安全应急与智能运维 Agent：你只需要用自然语言描述目标，它会自动规划步骤，调用 Shell 或 Go 原生工具，连接本地或远程目标，持续观察执行结果，并把关键证据、风险结论和处置建议沉淀为 Markdown 报告。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOibiaAD5vpIiarr4uuu3Uvhq4ib4Rv5Nko1IwPCRFbImicLnnbJA1fhUd1DNLXBnxebLoAZ83kLut8jFkJl89dwmxvtn6LMcP9RBGQc/640?wx_fmt=png&from=appmsg)

产品官网：https://www.hx0.store/products/deepsentry

# 一句话说清 DeepSentry

把“人工逐条敲命令、来回翻日志、手动拼证据”的安全工作流，变成“描述任务—自动执行—持续分析—输出报告”的 Agent 工作流。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOib9cYmFCEcEhZWpqwtaiaeMS8lvtrfialwVMkXEz6JZfPf6FmtmtY2tfTFwt3WR8VjiaJnGjs9IwXb6nrURernvB7yBPgZRs557G4/640?wx_fmt=png&from=appmsg)

例如，你可以直接告诉它：

> 检查这台服务器的系统版本、CPU、内存、磁盘、监听端口、最近登录用户和异常进程，最后按风险等级输出巡检报告。

也可以让它完成更复杂的任务：

> 合并分析 auth.log、secure 和 syslog，梳理失败登录、成功登录、sudo、su 和 SSH Key 登录行为，输出异常来源 IP、时间线、证据和封禁建议。

DeepSentry 会根据任务自行组合信息采集、日志分析、网络连接、进程排查、文件识别等能力，而不是要求用户先把每一步命令写好。

![](https://mmbiz.qpic.cn/mmbiz_jpg/PUTQGRQ4GOibICNfo0yJdPg5h39FNau6iaZC1ibfRUwnic4MvrT2zcAREHGL19xlfHibYxQ6NotEfP2UrzyoAQsfIjHHF8lg21h6Q7r6ZZXUPFSU/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUTQGRQ4GO8uWyYr3D3sic0zFYmicReVicNPjRczmtOrQW9iatpvqen4tGxjGURiaWIoicBo0EFpSruoichtYAobBIcOiaQrNIeHpIaePVwXFly3uCE/640?wx_fmt=jpeg)

# 2.0.1，不只是一次“小版本更新”

相比 v2.0，2.0.1 更关注一件事：让 Agent 在真实终端、真实远程环境和真实长任务里运行得更稳定、更清楚、更安全。

# 01 默认 TUI：从“执行命令”变成“持续协作”

DeepSentry 默认进入全屏 TUI Agent 面板，支持多轮输入、任务中断、会话恢复和斜杠命令。

你可以一边观察思考与工具执行过程，一边补充要求或修正方向；按下e，还能一次展开或折叠全部思考、长工具输出和子 Agent 结果。对复杂排查来说，它更像一个持续工作的安全任务台，而不是运行一次就结束的脚本。

# 02 60 个内置工具：没有完整工具链，也能开始排查

2.0.1 已内置 60 个安全应急、运维和取证工具，覆盖：

* 网络、端口、路由与连接分析；
* 进程、服务、用户与登录审计；
* 日志、文件、归档、哈希与敏感信息扫描；
* HTTP、网页快照与服务指纹；
* MySQL、Redis、PostgreSQL、Oracle 等数据库探测；
* PCAP、SQLite、CTF 文件与 Flag 辅助分析；
* Fleet 多目标、文件传输、代理转发、定时任务和配置管理。

大量能力采用 Go 原生实现。即使目标机上没有安装nmap、file、strings、tcpdump等常用工具，也能完成相当一部分基础排查。这对极简服务器、比赛靶机和受限环境尤其重要。

# 03 WebShell 后台模式：非交互环境也能跑长任务

在蚁剑、冰蝎、哥斯拉、网页终端等非 TTY 环境中，长任务最怕连接断开、页面超时或者一直没有输出。

2.0.1 的--webshell模式会把任务提交到后台，并立即返回报告路径和进度日志路径。你可以随时通过cat查看执行进度和最终报告，不必让网页连接一直挂着。

同时，本次修复了 SSH 长任务的输出流问题：远程任务不再等全部结束后才一次性显示，后台进度日志会持续写入。

# 04 Fleet 多目标优化：批量巡检不再被重复确认打断

面对多台服务器、业务集群或 AWD 靶机，DeepSentry 可以通过targets[]和标签选择器批量执行任务。

2.0.1 会根据fleet\_exec的真实命令和fleet\_file的实际文件动作动态判断风险。uptime、df -h、ss -lntp等只读操作可以更顺畅地自动执行；上传、删除、重启、写文件等高风险动作仍会进入确认流程。

控制端如果直接调用可能卡在密码输入的裸ssh、scp或sftp，系统也会主动拦截，并提示改用已经配置好的 Fleet 目标。

这让批量巡检既保留安全边界，也减少了无意义的反复确认。

# 05 Shell 双层安全复核：自动化不等于放弃控制

安全 Agent 能执行命令，首先要解决的不是“能不能执行”，而是“什么时候必须停下来问人”。

2.0.1 引入 Shell 双层安全复核：程序规则初判为高风险后，再交给 AI 结合真实命令和任务上下文复核；只有两层都判断为高风险，才请求人工确认。如果复核不可用，则按失败关闭原则处理。

对于 sudo，本机 TUI 通过系统sudo -v完成验证，DeepSentry 不接触密码，后续统一使用sudo -n；远程目标缺少免密授权时会立即返回，不再让界面卡在密码提示中。

# 06 长上下文更透明：你终于知道 Agent 还能“记住”多少

过去使用长上下文模型时，最容易混淆的是：当前会话用了多少 Token，与模型真实上下文窗口到底是多少。

2.0.1 会在标题栏直接显示有效上下文窗口及其来源，例如：

* mimo / mimo-v2.5-pro · ctx=1.05M[配置]
* custom / qianfan-code-latest · ctx≈131.1K[安全默认]

初始化向导支持自动、64K、128K、256K、512K、1M、2M 或自定义窗口。DeepSentry 会根据真实窗口做分层上下文管理：固定保留原始目标和最新修正，压缩早期执行轨迹，保留最近步骤与高价值线索，减少复杂任务做到一半“忘记前情”的情况。

# 07 多 Agent 并行协作：复杂排查可以分头取证

一次应急任务可能同时涉及登录日志、异常进程、网络连接和 Web 目录。如果所有方向都串行分析，时间和上下文都会被快速消耗。

DeepSentry 可以让多个子 Agent 按独立证据方向并行工作，例如：

* 日志分析 Agent：只负责异常 IP、登录时间线和原始证据；
* 网络分析 Agent：只负责外连、PID、DNS 和可疑目标；
* WebShell 排查 Agent：只负责近期修改文件、哈希和代码证据。

子 Agent 不会互相复制整段长对话，而是通过有界的“核心线索板”共享 IP、URL、CVE、哈希、文件路径和明确结论。最终由主 Agent 按“已验证事实、证据、冲突与不确定项、下一步”合并结果。

# 08 模型与终端兼容性继续增强

2.0.1 还补上了一批看起来细小、实际很影响使用体验的问题：

* 模型偶尔返回普通 Markdown 而不是 JSON 时，可自动识别询问、Shell 代码块或自然语言结论，不再直接解析失败；
* file\_upload、file\_download支持包含空格和引号的路径；
* 远程配置扫描、Secret 扫描和 Service Unit 审计更稳更快；
* Markdown 表格、询问面板和日志按 Emoji 字素簇计算宽度，组合表情不再挤坏边框；
* 初始化向导增加百度千帆 Coding Plan、火山方舟 Coding Plan、Xiaomi MiMo Token Plan / MiMo Claw 预设。

这些更新共同指向同一个目标：让 DeepSentry 从“功能能跑”，进一步走向“现场好用”。

# 它能用在哪些场景？

## 日常安全巡检与智能运维

自动检查系统资源、进程、端口、网络连接、登录行为和服务状态，按风险等级输出结果，适合云主机验收、上线前检查和周期性巡检。

## 安全事件应急响应

围绕异常登录、可疑外连、Web 目录篡改、疑似 WebShell、异常进程和敏感配置开展关联分析，把零散现象整理成可审计的证据链。

## 多服务器与攻防演练值守

通过 Fleet 批量检查多台目标，按标签选择生产、测试或 AWD 主机，汇总服务存活、磁盘、端口、进程和文件变化，快速定位需要优先处理的机器。

## CTF / AWD / AWD-Plus 辅助

自动识别题目附件、搜索 Flag、解压归档、提取字符串、分析 PCAP 和 SQLite，或在 AWD 环境中检查服务可用性、Web 目录、异常进程与反连连接。

## 自动化与无人值守任务

除 TUI 外，DeepSentry 还支持经典 stdout、JSONL、静默、计划、无人值守和 checkpoint 恢复模式，可接入脚本、CI、cron 与值班巡检流程，并通过钉钉、飞书或 HTTP 邮件网关发送结果。

# 它和普通 AI 助手有什么区别？

普通 AI 助手更擅长“告诉你应该怎么做”；DeepSentry 更关注“在授权范围内把任务持续做完”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO9InLfO3OIco3Hg32icuFBATnnvW9crWsf4TPYn9aeQzXaVZJ050Pbv3Oia3ES3MQlbU3ZHCtWnUXJ8bPDR08L2ZMw67XA4iamWbc/640?wx_fmt=png&from=appmsg)

它拥有目标连接、工具调用、风险确认、结果观察、失败恢复、会话记忆和报告输出的完整执行闭环。你仍然负责确定范围、判断业务影响和批准高风险动作，Agent 则承担大量重复的信息采集、初步分析和证据整理。

我们不希望它替代安全工程师。

我们希望它把安全工程师从机械重复中解放出来，把更多时间留给真正需要经验的判断、决策和处置。

# 5 分钟快速开始

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOibvRIQdkxISH5Kic7JdiaVYTQbLMapc0gI5qjJFJHE7Ud2SjrC9qtWJxaZe08rkBt1RMVP3WUgQW2cuzpGmDhNK92F0zlmic6G7nM/640?wx_fmt=png&from=appmsg)

从源码构建：

git clone -b 2.0 https://github.com/asaotomo/DeepSentry.git

cd DeepSentry

bash build.sh

./build/deepsentry --version

首次使用可通过向导生成配置：

./build/deepsentry --init

配置模型和目标后，直接进入 TUI：

./build/deepsentry -c config.yaml

然后用自然语言输入你的第一个任务：

> 排查当前服务器的系统版本、内存、磁盘、监听端口和最近登录情况，最后给出风险结论。

如果你更习惯直接下载二进制，也可以前往 Releases 页面选择与操作系统和 CPU 架构匹配的文件。项目支持 Windows、Linux 与 macOS，授权协议为 Apache License 2.0。

# 开源，是为了让它进入更多真实场景

DeepSentry 2.0.1 仍然不是终点。

安全场景的复杂性，决定了一个真正有用的 Agent 必须在真实任务中不断接受检验：不同系统、不同日志、不同模型、不同网络环境、不同权限边界，都会暴露新的问题。

因此，我们选择继续开源，也欢迎安全研究人员、运维工程师、CTF 选手和 AI Agent 开发者参与体验、提交 Issue 或贡献代码。

如果你也希望拥有一个能够连接目标、调用工具、持续分析并生成报告的 AI 安全伙伴，欢迎试试 DeepSentry 2.0.1。

GitHub：https://github.com/asaotomo/DeepSentry

如果这个项目对你有帮助，欢迎点一个 Star，也欢迎把它分享给更多正在做安全、运维、应急和攻防的人。

让 AI 不只会回答安全问题，也能在明确授权和安全边界内，真正参与完成安全工作。

> 安全声明：DeepSentry 仅允许用于你拥有或已获得明确授权的系统。请勿将其用于未授权扫描、入侵、破坏、绕过访问控制或任何违法用途。执行写入、删除、重启、上传等操作前，请确认目标范围并做好备份。

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/OC2Q345raO6FzicO8iasjtiavo2jy3hVzbIr7nVhQthvcpzut0ogYTqUOvZQj0ncoVCJoQ2HicXlmrYoJHDXW9uYjQ/0?wx_fmt=png)

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