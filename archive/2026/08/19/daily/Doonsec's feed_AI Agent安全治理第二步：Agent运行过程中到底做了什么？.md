---
title: AI Agent安全治理第二步：Agent运行过程中到底做了什么？
url: https://mp.weixin.qq.com/s/ujbA27CUZRpquiH1SKsquQ
source: Doonsec's feed
date: 2026-08-19
fetch_date: 2026-08-20T02:51:39.157712
---

# AI Agent安全治理第二步：Agent运行过程中到底做了什么？

# AI Agent安全治理第二步：Agent运行过程中到底做了什么？

sec0nd安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于绿盟科技
，作者绿盟君

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM5hQWTd2AHZRBvI0pibt2oAA2HeHMTOqTNt5kkrQUmdaYQ/0)

**绿盟科技**
.

绿盟科技 官方微信

![](https://mmbiz.qpic.cn/mmbiz_gif/2icibGKbYdhcwueLEggyPhKuibn1YBGoOBZ0JYxnRqM7yZBurze4okckSMwiaZgvqibmGzzZtBk1q7o3ZVFdCxYATw93Gkz68f0rthBCicBBjpcls/640?wx_fmt=gif)

**摘要**

上一篇文章讲的是Agent资产发现——把公司里到底有多少Agent搞清楚。盘点做完，安全团队马上会碰到下一个问题：这些Agent跑起来之后，到底做了什么？

举个例子，用户让Agent"查看服务器配置"，模型可能只是读了几条系统信息，也可能调了脚本、连了外部网站。权限清单只能回答"能做什么"，回答不了"实际做了什么"。

Agent行为观测的关键，是同时保留两类证据：语义层回答"Agent准备做什么"，执行层回答"系统实际发生了什么"。两层关联起来，才能得到一条可解释、可验证的执行轨迹。

本篇是绿盟科技"Agent安全治理系列"的第二篇。

**01**

**为什么只看一种日志不够？**

Agent的一次任务会跨过多层边界：用户向模型提出目标，模型选择工具，工具再通过操作系统启动进程、访问文件或发起网络连接。

这就带来一个问题：只看对话和工具日志，不能独立证明操作已经发生；只看系统事件，又不知道这条进程、这个路径、这个IP属于哪次Agent会话。

所以，Agent行为观测不是简单地把日志多采几份，而是让不同层面的证据互相解释。比如，一条工具日志显示"读取配置文件失败"——语义层只能说明Agent尝试过这项操作。但如果执行层同时记录到文件已经被打开、相关子进程已经跑起来了，安全人员就能判断失败到底发生在哪一步。

**02**

**语义层观测：Agent准备做什么？**

语义层不是要获取模型的全部推理过程，而是记录行为还原所需的上下文：用户任务、会话、模型输出、工具名称、调用参数、目标资源和工具结果。

这些信息不一定来自同一个位置——终端Agent、框架类Agent等。所以语义观测更适合设计成多源接入：先把不同来源转换成统一的会话、消息和工具事件，再进入后续关联流程。

常见的语义行为观测方式有四种：

**生命周期Hook**：Hook会在工具执行前后或会话状态变化时自动调用脚本或服务，记录工具开始、结束、参数和调用标识，也可以承担通知与权限控制。不同Agent支持的Hook并不完全相同，配置缺失、处理器失败或远端执行时，还需要其他证据补充。

**Agent框架观测**：自建Agent可以通过框架插装或回调记录模型、工具和检索步骤。LangSmith、Langfuse等平台会把这些步骤组织成完整链路。

**LLM Gateway**：模型网关可以统一记录调用方、模型、token、延迟和错误，但通常看不到模型返回后本地工具如何执行。

**本地会话日志**：终端Agent通常会保存会话记录。Claude Code的JSONL可以还原用户消息、模型输出、工具调用和结果。

这四种方式并非互相替代，无论选哪种，最终都应转换成统一事件模型，保留Agent身份、会话、工具、时间、资源和结果等关键字段。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhcy3XibVPfibJovD3qicrSeDZehsxiaicFjDNqAwyenL0XDickBq3icKUqX7iaZOMuMYuZUdAYgniclB5EFk9JCBNIe0SLoAKad2TUfiaEDFg/640?wx_fmt=png)

图1 语义层记录 Agent 从用户任务到模型回答的行为过程

**03**

**执行层观测：系统实际发生了什么？**

执行层关注的是操作系统"实际看到了什么"，eBPF技术刚好可以解决这个问题。eBPF 是一种在 Linux 内核中安全、动态运行沙箱程序的技术，通过事件驱动地挂载到内核或应用的各类钩子上，实现无需修改内核源码即可进行高性能的网络处理、可观测性、安全监控和性能分析。因此，eBPF技术可以从进程、文件、网络等关键位置采集运行事件，不依赖Agent主动上报，也不要求每一种工具单独适配。无论Agent用的是Bash、Python、Git，还是调了网络客户端，只要操作最终落到操作系统里，就会留下可观测的执行事实。

这些事实主要包括：启动了什么命令和子进程、访问了哪些文件路径、连接了哪些IP和端口，以及执行最终是成功、失败还是异常退出。

语义层记录"Agent调用Bash访问一个网站"，执行层则可能进一步看到：Bash启动了curl进程，curl向某个目标IP发起连接，随后以正常状态退出。这样，Agent声明的工具调用就不再只是日志里的一条记录，而是得到了系统侧证据的验证。

执行层的另一个价值，是能覆盖"工具内部的工具"。Agent界面可能只展示一次Bash调用，但Bash内部可能还启动了解释器、系统命令、网络客户端或其他脚本。通过进程父子关系，可以沿着进程链继续追踪这些间接行为，了解一次工具调用最终影响了哪些系统资源——不必要求每个命令都提供专用日志。

不过，执行观测也需要控制范围。直接采集全主机事件不仅会产生大量无关噪声，还可能增加存储、分析和敏感数据治理的压力。同时也要认识到，对于加密网络内容、模型提示词和推理过程，执行层看不到，仍需结合语义层才能完整理解。

![](https://mmbiz.qpic.cn/mmbiz_png/2icibGKbYdhcwOXP8xeQhtprUgDomf9OLPrtPXIFytWjIY4625CF86c6KdhvmC8bl4OS4NPh37ASVKHricjtpe7ZGvPJqy5k7awlPIQfPkocRY/640?wx_fmt=png)

图2 执行层从操作系统侧观测 Agent 产生的真实行为

**04**

**怎么把"意图"和"事实"串起来？**

语义层告诉我们"谁、为什么、准备访问什么"，执行层告诉我们"系统里实际发生了什么"。但光采集到两类信息还不够，关键是把它们关联起来，回答一个更具体的问题：这一次文件访问或网络连接，究竟是由哪个Agent、哪次任务、哪个工具调用触发的？

首先，为每次Agent运行建立统一身份。Agent启动后，无论它继续调用Shell、Python、Git，还是启动更多子进程，这些操作都应继承同一个会话身份。这样，即使一台服务器同时跑着多个Agent，也能先区分每条系统行为分别属于谁。

其次，把工具调用的时间范围与实际进程联系起来。Agent准备调用工具时记录开始，工具返回结果时记录结束。在这段时间内出现的命令、文件和网络活动，构成关联的候选范围。但时间接近并不代表一定相关，还需要结合工具参数、命令内容和进程之间的关系进一步判断。

最终，关联后的日志能够被还原成一条连续轨迹。从上向下看，某次工具调用最终产生了哪些系统行为；从下向上追，某个进程、文件访问或网络连接是由哪次Agent任务触发的。关联的本质就是用会话身份、执行时间、进程关系和操作目标，把Agent的意图与系统的真实行为连成一条从决策到执行的完整链路。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhcy7oEuNGLySHqn4Cwibcf7WakcdZtLNmaBGx1lgoUNVDRBVo5julRHTWRib3TGShfTJtEGpXxVBWl7F1XMgLVCxyHf2kN6IRNZJk/640?wx_fmt=png)

图3 同一Agent实例内，工具调用与系统事实的关联逻辑

**05**

**一次真实任务：完整轨迹长什么样？**

用户询问服务器配置后，Agent依次调用lscpu、free -h、df -h、uname -a等命令，获取处理器、内存、磁盘和操作系统信息。对话记录呈现用户问题、模型输出、工具参数和返回结果；系统侧则记录真实启动的进程、命令参数、进程编号和退出状态。两类信息关联后，形成"用户提问→Agent调用工具→系统执行命令→结果返回→模型回答"的完整轨迹。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhcy8sVhTLdP0Z0B8uj2rCCXJT6GHSScvEq5R3sgC32NhMsmZpfiaia8ibt9oyqOESp2g0ocox1dUzWFxZiaausib5ppxpmPAj6Kt6aQM/640?wx_fmt=png)

图4 用户提问Agent语义轨迹

![](https://mmbiz.qpic.cn/mmbiz_png/2icibGKbYdhcyuFaxFBacAA4RInh0CLmZ1d6OZibke7SP8iboTyy0syzbwOaMPtKMmciaQ0sCev3qzDxKm2ZG9WN7H8kutmkZ5r6G8occlGxfwxU/640?wx_fmt=png)

图5 Agent行为真实系统调用

由此，分散在对话、工具调用和操作系统中的信息被串联成一条可追溯链路：从用户任务和 Agent 意图，到命令、网络和文件行为，再到真实进程与系统调用。企业不仅能理解Agent为什么执行某项操作，也能确认它实际上做了什么、访问了哪些资源，以及最终得到了什么结果。

![](https://mmbiz.qpic.cn/mmbiz_png/2icibGKbYdhcyic8UIYcREYKhXB2vVCQm50DicHaRzTIdUmgKcb9nWRxkWpAaVQbmmh9dbbfPbJtOiaByuqbGZgQrah6q8AswtElsnDqANBqiaHjc/640?wx_fmt=png)

图6 从 Agent 工具调用到真实系统行为的关联轨迹

**06**

**常见问题（FAQ）**

**Q：Agent行为观测和传统应用监控有什么区别？**

传统应用监控看的是服务状态、响应延迟、错误率这些指标；Agent行为观测要看的是"这次操作谁触发的、为什么、实际做了什么"。Agent的任务跨模型、工具、操作系统多层边界，必须两层证据关联起来，才能还原完整轨迹。

**Q：语义层和执行层，一定要同时做吗？**

不是必须，但强烈建议。只做语义层，知道Agent"想做什么"，但无法验证操作是否真实发生；只做执行层，看到系统里"发生了什么"，但不知道是哪个Agent、哪次任务触发的。两层一起做，才能互相印证。

**Q：执行层用eBPF，对系统性能有影响吗？**

eBPF本身设计上对性能影响较小，但采集范围需要控制。直接采集全主机事件会产生大量噪声，更合理的做法是以Agent主进程、进程树、容器或cgroup圈定边界，只采集与目标Agent实例相关的事件。

**Q：如果Agent工具没有Hook，还能做语义观测吗？**

可以。Hook只是四类入口之一。如果Agent不支持Hook，还可以通过Agent框架插装、LLM Gateway或本地会话日志来获取语义信息。不同入口各有侧重，企业可以根据Agent类型灵活选择。

**Q：行为观测做完之后，下一步做什么？**

有了行为轨迹，后续可以开展异常检测（识别偏离正常模式的行为）和主动测评（在不同任务、权限和环境条件下验证Agent的安全边界）。行为观测是Agent安全治理链路的中间环节，向上承接资产发现，向下支撑异常检测和主动测评。

本文为绿盟科技"Agent安全治理系列"第二篇，后续将围绕Agent轨迹异常检测和主动测评等方向展开。

参考文献

[1] Zheng Y, Hu Y, Yu T, et al. Agentsight: System-level observability for ai agents using ebpf[C]//Proceedings of the 4th Workshop on Practical Adoption Challenges of ML for Systems. 2025: 110-115.

[2] https://www.kernel.org/doc/html/v6.4/bpf/index.html

[3] https://docs.langchain.com/langsmith/observability-concepts

[4] https://code.claude.com/docs/en/hooks

![](https://mmbiz.qpic.cn/mmbiz_gif/ZPtdzESiawhdMHyNfDvj0a36SiaN499NjK0BKean9ibV1T8rYe2gLG8OTSjeCB1NesY09JLKujB7DqpO8DGu4HFxw/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IpYUt4DIvZdb5Tviaw0y56eym8onSh6PDtdqw33esORUCLQLiaMqAMjLP0W67TaSMdiamOfCibPbhQHwib7M9NKsAiaw/640?wx_fmt=png)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhcy2fEfiaBDX2OFzKpFN7KEvKjmMzIhaA6RORU7tL1gkiaRpS4zcl7PJCmItCabibibRCiahdwAfnjvod7A1yDErahL8pO2jiaNkUWEHs/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5ODYyMTM4MA==&mid=2650479206&idx=1&sn=5056ad01dadd9af8f03ce5ae116c12b6&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhcyzuXSGvgibAR2jhESqjNEUk9EibMzBPo9WSBBswxENRKr2KcdUZbUGX19kQ5kvgk3KucgV2vxMCvib5cJR9unffxHJibxo08qec00/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5ODYyMTM4MA==&mid=2650479207&idx=1&sn=3c35c219b76b7d7f856a5656cf08f536&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/2icibGKbYdhcziav1VaI6yoOOKOlPG1uvib6Ods2W0AoaK15gl8qVwPGExdPxAN3poIGakkNr0Cs5lUYIQjxEpUYNZiahT3tELicm4c42Fic3HcMico/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5ODYyMTM4MA==&mid=2650479208&idx=1&sn=5b5a68eb8cab610c0a6ece38a3525d67&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/IpYUt4DIvZdb5Tviaw0y56eym8onSh6PDeO1pHaIGUqRCpmiczbCeAckJNSEo5lw1OO3jwJhibgqKlU5V2Ps4mt9g/640?wx_fmt=gif)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/u7ibmWw94HhyPjaGFbJ1aj02bPU5jwAmG8o7vJ9jgF7q3DaU2c6Bicqz1ZTLTRWLc188vgsWFMnyNE6CX8Y1zSaw/0?wx_fmt=png)

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