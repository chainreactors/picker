---
title: DeepSentry V2.0.5 Ultimate 正式发布并开源：12 类专职 Agent、77 个工具，一次真实排查给你看
url: https://mp.weixin.qq.com/s/JXKbhv6spS7qJd0_NAqEXA
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:22:10.075881
---

# DeepSentry V2.0.5 Ultimate 正式发布并开源：12 类专职 Agent、77 个工具，一次真实排查给你看

# DeepSentry V2.0.5 Ultimate 正式发布并开源：12 类专职 Agent、77 个工具，一次真实排查给你看

原创

asaotomo
asaotomo

Hx0极客圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

产品发布 · 安全运维 · 证据链

12 类专职 Agent，77 个工具
一次真实排查给你看

同一份虚构日志，实跑 2.0.4 与 2.0.5：12 类专职 Agent、77 个工具，以及可以交给同事复核的证据档案。

· DeepSentry 2.0.5 Ultimate · 2026 年 9 月 24 日

凌晨收到告警：“有人登录了运维账号，随后审计服务停了。”接下来要交代清楚的是**谁在什么时间做了什么、证据在哪、下一步该确认什么**。若要跨多台主机取证、让同事复核，工作还必须能继续、能交接。

2026 年 9 月 24 日发布并开源的 DeepSentry 2.0.5 Ultimate，正把安全工作组织成一条可检查的链。

立即下载体验：https://www.hx0.store/products/deepsentry

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GO8B4CcdeNSuMibMbYh4VZ2lgoDXqQ4w2kbwLDOic3jf8h1HMQvbzz8ia0wf08R7PMTWgLg7VpntTwtFVZrr1urNicoo7l7p9sEgcPg/640?wx_fmt=png&from=appmsg)

**这条链：**限定范围 → 分工采证 → 核对结论 → 必要时确认变更 → 留下报告与证据。下面不只讲功能，也给出一份可复核的本地实跑样例。

01它和其他 Agent 有什么不同

同样叫 Agent，要完成的事并不一样。下面按各项目的官方定位对照：编码、授权渗透，以及安全应急和日常运维，各自解决的是不同问题。

Codex / OpenHands

以软件工程任务为中心。Codex 的官方介绍聚焦编写、理解和修改代码；OpenHands 将自身定位为编码 Agent 与工程自动化平台。它们适合围绕代码仓库进行开发、测试和交付。

Codex 官方文档　·　OpenHands 官方说明

PentestGPT

以获授权的渗透测试为中心。它的 Agent 版本面向渗透测试流程与目标验证，适合围绕测试范围推进发现、验证和记录。

PentestGPT Agent 官方说明

DeepSentry

以安全应急与日常运维的实际目标为中心。一项任务可能同时涉及本机、SSH / Telnet / FTP、网络设备、Fleet 多目标、网页巡检、聊天入口和定时执行。主 Agent 管控范围与最终结论，专职 Agent 处理不同证据类型；报告把动作、授权、风险与证据编号联系起来。

选择它的理由，是你要管理的是**运行中的系统与可交付的调查过程**，而不只是一个代码仓库或一次靶场验证。

DeepSentry 官方 README

02从 2.0.4 到 2.0.5，增加了多少

我们直接对照 2.0.4 标签与 2.0.5 当前代码的注册表：**专职子 Agent 从 8 类增至 12 类，增加 4 类（+50%）；内置工具从 73 个增至 77 个，增加 4 个（+5.5%）**。这里统计的是“可用角色和工具数量”，不是准确率、检出率或性能提升。

![2.0.4 至 2.0.5 的注册表增量与交付物变化](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GO8cZXuWnJcJREBzDyKEc7y3RkCpkMtFGbxgN7DichHTPGp4MfX4qJyNScK9QuHHt7xryRJn1yCYVDfoQgWmibBqjJbE2Mp5ZOhAs/640?wx_fmt=png&from=appmsg)

图 1　注册表增量：角色 +4，工具 +4，交付物增加可校验证据档案

新增角色分别面向**服务器基线加固、终端基线加固、主机应急响应、网络设备分析**。新增工具为 task\_wait、task\_context、computer\_use、http\_proxy。角色扩展了分工，工具补上了长任务等待与上下文、桌面交互和代理接入能力。

更重要的变化发生在交付环节：2.0.5 每次会话除了 Markdown 报告，还会写入同名 .evidence.jsonl。记录经过脱敏，按序号和 SHA256 串联；项目内置校验函数可检查记录是否缺失或改写。中断、等待补充与失败会标明未完成，避免把过程中的猜测包装成最终结论。

2.0.5 更新日志

03哪些工作最适合交给它

场景一　多台主机的应急初筛

例如值班人员收到“审计服务被停”的告警，先用 Fleet 指定目标组，要求只读收集最近登录、提权、进程和服务状态。主机应急角色做时间线，基线角色核对配置，主 Agent 把相互矛盾的线索和未证实项单独列出。需要恢复服务或隔离账号时，再明确确认目标和动作。

可直接尝试

检查 prod-web 目标组最近 30 分钟的登录与审计服务状态；只读采证，按主机和时间线列出原始依据。先提交报告，不执行重启、封禁或改配置。

场景二　网络设备与网页控制台巡检

交换机或防火墙的问题往往横跨 CLI 输出、Web 页面和截图。DeepSentry 可结合网络设备角色、Fleet 与 Hx0 鹰眼，收集设备状态、告警和网页证据，再汇成 Markdown 或 Word。这样的交付更适合发给运维同事复核，也能避免只留下“设备正常”的笼统答复。网页巡检与 Word 报告并非 2.0.5 首次出现；本次更新加强的是角色分工、操作边界与证据串联。

可直接尝试

只读检查边界防火墙今天的接口状态和高优先级告警；网页用鹰眼打开，保留关键截图，按“现象—证据—影响—建议”交付。

场景三　每天固定时间的安全值守

把资源、端口、证书或登录异常检查设为周期任务，结果回到发起它的聊天会话。2.0.5 对定时结果增加持久化待投递队列；任务完成后即使进程重启，也能恢复收件路由。适合人不在终端前、却需要持续知道“检查过什么、何时检查、下一次何时运行”的团队。

场景四　桌面系统里的重复核查

2.0.5 新增 computer\_use。鹰眼继续操作浏览器；Computer Use 操作这台电脑：先看当前屏幕，再使用鼠标和键盘。换窗口或画面变化后会重新观察，键鼠输入需要确认。例如把桌面上的文件通过微信发给同事，或打开 Burp Suite，用内置浏览器查看网页并做抓包分析。

**支持的桌面：**macOS、Windows 和 Linux X11。使用前运行 ./deepsentry --computer-check，按提示打开辅助功能与屏幕录制，就可以把本机软件放进同一次任务。

Computer Use 平台说明

04实跑一份日志，报告如何接受复核

我们构造了**9 条虚构 SSH 日志**，IP 均使用文档保留地址，不对应真实主机或安全事件。任务明确限定“只读分析当前文件、标注行号、区分观察和推断、生成中文报告”。2.0.5 实际调用工具读取文件并生成 Markdown 报告；报告旁的证据档案有 **4 条记录**，使用项目内置 VerifyEvidenceJournal 校验通过。

![本地实际运行结果的审阅页](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO8giceuHSawmYJfnOvd9BnsFVMXmcT3iall8GA1oNRBfwBte0eaP2ImY4cAHdMZ1vIqL50FIXmFd2OE3aE2AHsklqN1mYVZwLiaX4/640?wx_fmt=png&from=appmsg)

图 2　审阅页：原始日志、报告结论，以及证据校验结果

报告按行号写下可以回看的事实：L1—L3 是同一来源的三次失败登录；L5 记录 ops 成功登录；L6 记录该账号经 sudo 执行停止 auditd 的命令；L8 表示审计服务已停止。是否已经获授权、是否构成攻击，单独列为需要补充变更单和更多日志的线索。

同一会话可以继续核对

证据档案有 4 条记录，并用项目内置校验确认序号和 SHA256 连续。同事不需要重新跑一遍，也能顺着报告回到原始日志；如果要补充材料，在**同一会话**里继续追问即可。

![2.0.5 真实运行记录与报告数据](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO90wic5XHiaCrgHvHY9c2jqbLkzXoPlt6WRm8yCJeVSNaoSZvLJdKDCic7LPfuztkhloicnkWJYGaysqYSdTYq6HsAwCWcB370wzW8/640?wx_fmt=png&from=appmsg)

图 3　同一次运行留下的记录：工具动作、报告与证据校验

05同一任务，两版各跑一次

我们还下载并校验了官方 2.0.4 arm64 发布包，用**同一份输入文件、同一任务提示、同一模型配置**各运行一次。观察到：2.0.4 用 6 次工具动作、约 51.4 秒，生成 Markdown 报告；2.0.5 用 2 次工具动作、约 18.9 秒，生成 Markdown 报告及可校验的证据档案。

![同一虚构样例的两版单次运行观察值](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOicxh1L8ez752ViczplaVvB8waOaYRsnRfibtUazTQcwMnrYsokiaOYyvD7yTCcdMlZKmeRzQxXhNCez4oFcTaNYDArZE4LNXIWwX0/640?wx_fmt=png&from=appmsg)

图 4　同一任务下，2.0.5 同时留下证据档案

同一份日志、同一提示、同一模型配置：2.0.4 用 6 次工具动作、约 51.4 秒生成 Markdown 报告；2.0.5 用 2 次工具动作、约 18.9 秒完成报告，并额外写下 4 条可校验的证据记录。交付物从“一份结论”变成“结论加可复核的证据链”。

06给团队一个可执行的起点

先选择与系统架构匹配的 2.0.5 Release，核对发布包的 SHA256SUMS，再配置受控模型服务。第一项任务建议从**只读、范围小、便于人工核对**的日志或主机检查开始。

./deepsentry -h
./deepsentry --task "只读分析当前目录 auth.log；标注行号，区分观察与推断，生成中文报告，不修改文件或连接其他目标"

接入生产前，先写清目标清单和变更确认方式，再打开 Fleet、聊天定时任务和设备巡检。点击阅读原文跳转产品官网查看产品说明与下载。**它要交给团队的，是做过什么、依据是什么、下一步确认什么。**

产品说明以 官方 README 和 更新日志 为准。

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO96vQKict5Njccs0NxhzcTHbkVeVnSnNvIwf6d01l7x12WMEFaxAwJIPG1feicAbYLzUoDjBbAvhRE9t9FbusNWcVHpIUs20TSyc/0?wx_fmt=png)

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