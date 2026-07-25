---
title: DeepSentry v2.0.2 Ultimate 正式发布：让安全 Agent 更稳定、更可控、更适合真实环境
url: https://mp.weixin.qq.com/s/DzL48iZESTzQrEz9AUtZwQ
source: Doonsec's feed
date: 2026-07-24
fetch_date: 2026-07-25T04:58:32.436317
---

# DeepSentry v2.0.2 Ultimate 正式发布：让安全 Agent 更稳定、更可控、更适合真实环境

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PUTQGRQ4GO8EVoric9bh8mmvmVMkR4v5X7es1rGUsAjrZlia38DHRy3zk6ltIicUmF371Fdou4cg5um6rMx2hFSUicKIrpXyv2NrQ3JAhGRDSIw/0?wx_fmt=jpeg)

# DeepSentry v2.0.2 Ultimate 正式发布：让安全 Agent 更稳定、更可控、更适合真实环境

Hx0战队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

编者荐语：

告别“盲盒式”AI运维。全新Runtime v3稳控高危操作；深度适配华为/H3C/锐捷/Cisco等网络设备；支持CTF竞赛与WebShell环境。70+工具链，Go原生实现。AI提效，你掌安全。

以下文章来源于Hx0极客圈
，作者asaotomo

![](https://wx.qlogo.cn/mmhead/rqvn1hjHytedfdS681PB4EroprjS2nmYaD5EibbpYicfwoZVQiaiavVZEBTaybhia7ZibDxjt0LMcWS8s/0)

**Hx0极客圈**
.

我们致力于将 AI 赋能于安全，用极客精神重塑工具。

2026 年 7 月 23 日，由 Hx0 战队研发的DeepSentry v2.0.2 Ultimate 正式发布。

DeepSentry 是一款面向安全应急与智能运维场景的 AI Agent。用户可以通过自然语言描述任务，由 Agent 进行步骤规划，并结合 Shell、内置工具以及本地或远程连接能力完成信息采集、日志分析、安全排查和结果整理，最终生成可审计的 Markdown 报告。

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GOicrXiaryLKYnHy7qGNTh4jeJXY5uBfvkcI5xdDh3IlZ2JiaxOLz2ibqdvfUUD0XNTKBrYLjoZLwdNm5RFuAmt9HIx47wqwywo23x8/640?wx_fmt=png&from=appmsg)

产品官网：https://www.hx0.store/products/deepsentry

与单纯的命令生成工具不同，DeepSentry 更关注一个完整任务能否持续执行：包括如何选择工具、如何保留证据、如何处理中断、如何控制高风险操作，以及如何在本地、远程设备和多目标环境中完成任务。

在 v2.0.2 中，我们没有将重点放在功能数量的简单堆叠上，而是集中改进 Agent 运行时、远程协议、网络设备适配、故障恢复、安全审批和交互体验，希望让 DeepSentry 在真实安全运维场景中更加稳定、清晰和可控。

# 一、Runtime v3：重新梳理 Agent 的执行过程

v2.0.2 默认启用新的 Runtime v3，同时保留agent\_runtime: legacy兼容模式，方便部分旧模型网关在出现兼容问题时临时切换。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO9vmccJB1EfL9DqzHDvAVhEPF3eW9BlKwaHLK3tPqQtwwoDibZWjicOmYEeUPPlHaQvNws8QOHsBFDumIo4mq57MvKk7Uf4ibjuhw/640?wx_fmt=png&from=appmsg)

新的运行时进一步结构化了 Agent 的消息和执行过程，将文本、推理、工具调用、工具结果和证据引用分别记录，并为每次运行、轮次、步骤和工具调用分配稳定标识。

这项改动解决的并不是“界面显示方式”问题，而是复杂任务中的执行可靠性问题。

例如，当模型一次返回多个工具调用时，Runtime v3 可以完整识别并执行。对于低风险、只读且幂等的独立操作，可以在受控范围内并行；涉及文件修改、配置变更或者其他高风险动作时，仍然保持串行执行和人工审批，避免为了提高速度而牺牲操作安全。

同时，v2.0.2 增加了按需工具发现机制。系统不再无差别地向模型提供所有工具，而是根据当前任务筛选候选能力，以降低上下文占用和工具误选概率。

针对模型服务不稳定的情况，新版本还增加了结构化错误分类、退避重试和模型故障切换机制，可对限流、超时、服务端错误、连接异常以及输出格式异常进行区分处理。用户也可以通过models[]配置主模型和备用模型。

# 二、工具从65个扩展至70个，但重点不只是数量

v2.0.2 的内置工具由 65 个增加至 70 个。

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GO9Kca2Sicz85pACZ3r9Itia7bxM12JK75SkoAXASaDOQX6DatIG1n1MCOeeTk45Pe8JNsQccDVWYeHwd6KfLsQibtUqt2pRP5fz3A/640?wx_fmt=png&from=appmsg)

新增能力主要面向以下几个方向：

* 主机安全事件基线采集；
* WebShell 排查；
* 网络设备快速诊断；
* 限时比赛任务；
* 比赛答案完整性和证据覆盖检查。

目前，DeepSentry 的内置工具覆盖网络、进程、日志、文件、文档、Web、数据库、流量包、Fleet 多目标、代理转发、定时任务和配置管理等场景。

其中，大量能力使用 Go 原生实现。在部分精简系统或受限目标环境中，即使没有预装nmap、file、strings、tcpdump等常用程序，也能够完成一部分基础信息采集和分析任务。

工具数量只是表面变化。v2.0.2 更重要的改进，是让工具调用、结果记录、错误恢复和证据引用形成更加完整的执行链路。对于体积较大的工具输出，系统会将原始结果保存为 artifact，并记录来源、目标、摘要和 SHA-256 信息，避免长上下文整理后只剩自然语言结论、丢失原始证据。

# 三、增强华为、H3C、锐捷和 Cisco 网络设备适配

网络设备是本次版本更新的重点方向之一。

v2.0.2 对 SSH 和 Telnet 交互进行了较大调整，增加了对以下常见设备 CLI 的适配：

* 华为 VRP；
* H3C Comware；
* 锐捷 RGOS；
* Cisco IOS。

新版本可以识别多种登录提示、命令行 Prompt 和分页提示，并根据设备类型执行相应的关闭分页命令。

对于华为和 H3C 设备，还可以在完成配置后识别super、system-view、子配置视图以及quit、return等命令引起的 Prompt 变化。

在读取长配置或大量接口信息时，执行器会继续排空设备输出，直到重新识别到 Prompt，避免上一条命令的残余输出影响下一条命令。

新版本还区分了“设备命令过滤后的投影结果”和“输出确实超过限制被截断”两种状态，减少 Agent 将正常过滤结果误判为证据缺失的情况。

需要说明的是，DeepSentry 对网络设备的支持主要用于授权环境下的信息采集、状态诊断和辅助研判。进入配置模式或者执行修改型命令时，仍然会按照高风险操作流程进行审批。

# 四、重构FTP与FTPS连接，提高传输可靠性

v2.0.2 对 FTP 连接、登录和数据通道进行了重构。

新版本支持：

* 明文 FTP；
* 显式 FTPS；
* 隐式 FTPS；
* EPSV 与 PASV；
* EPRT 与 PORT；
* 被动、主动及自动回退模式；
* 私有 CA 和证书校验；
* 分阶段连接、命令和传输超时。

在被动模式下，程序优先使用 EPSV，不支持时再回退至 PASV，并避免直接信任服务端返回的异常地址，以降低 NAT 环境下连接错误和 FTP Bounce 风险。

文件下载时，数据会先写入权限受限的临时文件，只有在确认传输成功后才原子替换最终文件。发生中断、超时或数据不完整时，不会留下看似完整、实际损坏的证据文件。

新版本也加强了路径和命令参数校验，用于防止 CRLF 命令注入等问题。

这些改进不会改变 FTP 协议本身的安全属性。在生产环境中，仍然建议优先使用 SFTP，或者使用开启证书验证的 FTPS。

# 五、新增比赛模式与答案自检能力

针对网络安全竞赛和限时演练场景，v2.0.2 新增了--competition模式。

比赛模式会更加关注：

* 时间范围控制；
* 关键证据绑定；
* 最小处置方案；
* 修复后的复验；
* 必要的回滚说明；
* 最终答案格式。

同时，新版本新增competition\_answer\_check工具，可从任务完成度、技术准确性、AI 使用效率、输出规范、证据覆盖和幻觉纠正等方面，对当前答案进行一次结构化检查。

这一能力的定位是辅助选手在提交前发现漏项和无依据结论，而不是保证自动得出正确答案。比赛结果仍然取决于题目环境、模型能力、任务描述、工具权限以及使用者对证据的判断。

# 六、统一控制端代理能力

v2.0.2 新增了更加直接的代理启动参数：

```
-proxy http://127.0.0.1:8080
```

或者：

```
-socks5 socks5://127.0.0.1:1080
```

两种命令行代理参数互斥，只影响当前运行进程，不会自动修改配置文件。

对于需要长期使用代理的环境，也可以通过 controller\_proxy 配置 HTTP、HTTPS、SOCKS5 或 SOCKS5H 代理。

代理能力可作用于模型接口、MCP HTTP、普通 HTTP/Web、浏览器、TCP、CIDR、数据库探测以及 SSH、Telnet、FTP 等控制端连接。代理用户名、密码和完整 URL 会在界面、报告、模型上下文和事件记录中进行脱敏处理。

# 七、进一步完善TUI、WebShell和非交互环境体验

DeepSentry 默认提供全屏 TUI Agent 面板，支持多轮输入、任务中断、会话恢复和斜杠命令。

v2.0.2 新增终端背景自动识别，可根据深色或浅色背景选择相应的高对比度主题，也可以通过--theme dark或--theme light手动指定。

针对长期运行时可能出现的重复行、边框残留、窗口缩放错位和中文输入法光标问题，新版本进行了集中修复。

* WebShell 和非 TTY 场景也得到进一步完善：
* 显式 --no-tui --task 任务不会再被误判为交互会话；
* 未经授权的高风险操作会保守拒绝，不会在后台永久等待人工输入；
* WebShell 后台任务新增独立的 status.json；
* 任务状态可以区分排队、运行、完成和失败；
* 经典命令行模式会返回与任务状态匹配的退出码；
* 非 TTY 日志会移除 ANSI 控制序列，便于在网页终端、CI 和文本审计中读取。

对于需要通过蚁剑、冰蝎、哥斯拉、网页终端或其他受限终端执行任务的场景，可以继续使用：

```
./deepsentry --webshell -c config.yaml --task "查看当前系统版本和监听端口"
```

程序提交后台任务后会返回进度日志和报告路径，用户可以通过cat等方式查看执行状态。

# 八、安全执行和证据保护继续加强

安全 Agent 本身也需要受到约束。

v2.0.2 对高风险操作确认机制进行了调整：

* Y：只批准当前一次操作；
* A：在当前会话中允许目标、动作和参数范围一致的同类操作；
* N 或 Esc：拒绝；
* 直接按回车：默认拒绝。

会话授权不会写入 checkpoint，新建会话或恢复会话时会被清空，避免之前的授权在新任务中被隐式继承。

证据文件、checkpoint、报告、浏览器 artifact 和 WebShell 进度文件等，也进一步收紧为0600文件权限或0700目录权限。

本次发布还升级了存在已知安全问题的 Go 依赖，在 CI 中增加静态安全分析和二进制可达漏洞检查。发布构建启用了-trimpath，并提供与跨平台程序对应的SHA256SUMS，用户下载后可以先校验文件完整性再运行。

# 九、DeepSentry适合哪些场景

当前版本主要面向以下授权场景：

安全应急响应

读取系统和安全日志，排查异常登录、可疑进程、异常网络连接、Web 目录变化以及可能的后门文件，并将执行过程整理为证据链。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO811AVFIBHl2OLibDVHphnfrUjFzpSicAgbzX9aBd2Spboib9S8fubnuRzHuq3JkACakoFiawgNFBV1HZhxEcgMHJibMwZFxrCicjOkY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GOibOt1JmPBpbg3EnQPvvaFedbRgO6tGOjwBTfxIUWhzb5Jo0njleUlAmNSWxEtQ768prhF8tibS4GfXiclelrsYuqZMAsj88CD3t4/640?wx_fmt=png&from=appmsg)

日常安全运维

检查系统版本、CPU、内存、磁盘、负载、监听端口、网络连接和登录情况，形成结构化巡检报告。

多目标批量巡检

通过 Fleet 管理多台 SSH、Telnet 或 FTP 目标，按照标签和选择器执行批量信息采集、文件操作和状态汇总。

网络设备诊断

通过 SSH 或 Telnet 连接常见网络设备，采集版本、接口、路由、二层状态和设备日志，辅助分析丢包、接口异常及网络状态问题。

CTF、AWD与演练辅助

完成文件识别、字符串提取、压缩包处理、流量初筛、日志分析、服务状态检查、目录巡检和证据汇总等重复性工作。

DeepSentry 可以提高信息采集和整理效率，但不会替代安全工程师对业务影响、攻击路径和处置风险的最终判断。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO8yCaibGn7v11UMjVfDoBoqVXnIXZR1Q9sFH0AuRtop2v9vKXpdgZ63fs8gz4KGU5OPMvY9fRcAM6PBnoKvdXN8J0eFHZ3D8pF0/640?wx_fmt=png&from=appmsg)

# 十、快速开始

DeepSentry 提供 Windows、macOS 和 Linux 多架构程序。下载时需要根据操作系统和 CPU 架构选择对应文件，并建议使用 Release 中提供的SHA256SUMS校验文件完整性。

首次使用推荐运行初始化向导：

```
./deepsentry --init
```

完成模型和目标配置后，进入默认 TUI：

```
./deepsentry -c config.yaml
```

用于脚本、CI 或自动化任务时，可以使用：

```
./deepsentry --no-tui -c config.yaml --task "查看当前系统版本和监听端口"
```

DeepSentry 支持 OpenAI、Anthropic、Google、DeepSeek、Qwen、百度千帆、火山方舟、腾讯混元、Xiaomi MiMo、GLM、Ollama、LM Studio 和自定义兼容接口等多种模型接入方式。

模型名称、接口地址和服务商套餐可能发生变化，实际配置应以对应服务商当前文档和账户权限为准。

# 写在最后

DeepSentry v2.0.2 Ultimate 的核心变化，可以概括为三个方向：

第一，让 Agent 的执行过程更加结构化。

从多工具调用、按需工具发现，到故障切换、checkpoint 和 artifact，系统开始更加重视复杂任务能否稳定执行和恢复。

第二，让远程环境适配更加完整。

新版本加强了网络设备、Telnet、FTP、FTPS、代理和非交互终端的处理能力，覆盖更多真实运维环境。

第三，让自动化始终处于安全边界之内。

对于修改型和高风险操作，DeepSentry 仍然坚持人工确认、保守授权和证据留痕，不以“全自动”为目标牺牲安全性。

我们希望 DeepSentry 成为安全工程师在应急响应、日常运维、竞赛演练和多目标巡检中的实用辅助工具，而不是一个脱离证据和权限边界的“自动攻击工具”。

DeepSentry v2.0.2 Ultimate 现已在 GitHub Releases 发布。

项目地址：https://github.com/asaotomo/DeepSentry

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GOicvkia3DTfb0icTLmWKYcDcdGA7aUNIS0CcbjnAMCQxDJFcFGfXjOfgo0qwhuEOsaLUMbgC3iaXUNUMgb0Dib4wgnRraUlU0U4rkKA/640?wx_fmt=png&from=appmsg)

在使用前，请先阅读项目说明和安全建议，并确保所有操作均在自有或已获得明确授权的系统中进行。

任务内容、必要上下文和工具结果可能会发送至用户配置的模型服务。涉及敏感环境时，请确认模型服务商的数据处理政策；数据不能离开本地环境时，应使用受控的本地模型，并在对外发布报告或截图前进行脱敏。

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