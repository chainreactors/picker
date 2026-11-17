---
title: 5个顶级AI自动化攻击工具 | 解决手动点击Cobalt Strike 或 Brute Ratel的烦恼
url: https://mp.weixin.qq.com/s/E777PWnCOFtPniRt5iL7JA
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:55:34.524576
---

# 5个顶级AI自动化攻击工具 | 解决手动点击Cobalt Strike 或 Brute Ratel的烦恼

# 5个顶级AI自动化攻击工具 | 解决手动点击Cobalt Strike 或 Brute Ratel的烦恼

原创

助力行业的
助力行业的

李白你好

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 前言

过去，一次典型的入侵需要操作员坐在电脑前，在 Cobalt Strike 或 Brute Ratel 的界面里手动点选下一步动作。如今，这套打法正在被彻底改写。短短数月内，一批基于大语言模型（LLM）的**智能体攻击框架**（agentic offensive frameworks）已经从实验性工具进入真实入侵现场，并被用于多目标并行、长期运行的黑产行动。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ft6csZH0gNUddXULl1q2rdPxia9wPkCRiayFgQ9kCA7QYNyBHyqFicSmpiadxP9icdHzaBqxCZtstDW9ibe2iaqyrK7IhBx6KbKgWl15D1icG4kPzy0/640?wx_fmt=webp&from=appmsg)

Google 威胁情报组（GTIG）与 Mandiant 已在事件响应中观测到 ARTEX、Cairn、HexStrike 和 PentAGI；微软将 ARTEX 的使用归因于 Storm-0940；Elastic 自身也追踪到一起由 CyberStrikeAI 服务器辅助的 AWS 入侵。这五个框架在 GitHub 上合计获得超过 6 万颗星，一个脚本或一个 Compose 文件即可完成部署。

## 什么是智能体攻击框架？

所谓智能体攻击框架，本质是把一个大语言模型放到“总指挥”的位置上，由它调度扫描器、curl、shell 和云命令行等红队与攻击者已经使用了十几年的老工具。工具本身并不新，新的是围绕它们的**规划循环**：

![](https://mmbiz.qpic.cn/mmbiz_jpg/ft6csZH0gNWFibm7J2hnUsEblibD8ibib8cd6icc3nAticJzKic3IFObBqpzxCYiawpbDtBzSGGAkeWsuR3djAibsHy4Z4xZwJn6drAfWYWsSMqbibxVc/640?wx_fmt=webp&from=appmsg)

* 模型规划每一步做什么；
* 把任务拆给多个 agent 并行执行；
* 缺少工具时自行安装或编写；
* ARTEX 的单次爆发窗口可短至 2～25 秒。

研究人员阅读了五个框架的源码并结合公开事件报告后得出结论：它们没有一个在代码层面强制授权，而它们执行的每一个动作，最终都会以进程、云 API 调用或登录行为的形式，落在防守方本就在采集的遥测（telemetry）里。

## 与传统 C2 框架的本质差异

Cobalt Strike 和 Brute Ratel C4 背后是人：操作员盯着植入体，决定下一步执行什么。智能体框架保留了全部工具，只是把操作员的“思考时间”替换成了自动规划循环。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ft6csZH0gNWK68nqUKmZia0I0ekvINGNkAlGG8zicm7kSH9g0ia50HaRmYkNcFB6pEJfPmJWKhqKg9J11aK8f3sAXUicdvyRQGwwulnwVEG4Qxk/640?wx_fmt=webp&from=appmsg)

GTIG 观测到 ARTEX 的执行爆发约为 2～25 秒；NorForge 跟踪被判定为恶意的暴露 Cairn 面板后发现，某个攻击者团伙从开工到拿下目标平均不到 23 小时。单次爆发极短，容易从检测窗口中溜走，但整个行动可持续数小时。因此，要把一连串爆发关联回同一次行动，回看窗口必须拉得足够长。

真正落到防守方环境里的，不是模型本身，而是这些工具造成的实际动作：主机上的新进程、云审计日志中的 API 调用、身份系统中的登录行为。

## 五个框架的设计差异

五个框架共享同一个规划循环，但模型运行位置、工具拉起方式各不相同。自主性是默认状态：

![](https://mmbiz.qpic.cn/mmbiz_jpg/ft6csZH0gNVNZA55WgB5gwMZ3kPCeCoDGtXksC2R8hzjKzEJiauOWcIVhers310ojIIN5aqNCKPyuERHibnicz26X5WC8fWz2cCODQNoicVhcWs/640?wx_fmt=webp&from=appmsg)

* **CyberStrikeAI** 出厂即关闭审批模式；
* **PentAGI** 的 Compose 文件中将 `ASK_USER` 写死为 `false`；
* **Cairn** 三种编码 agent 工人中有两种启动时就关闭了审批提示；
* **ARTEX** 直接让 agent 运行在 bypass 权限模式。

这四个框架默认都不等待人工确认。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ft6csZH0gNVYynliasAmKOm5vpyNpTonGUcQtVFOqeEmmRREZ7Z9wkxBNDxVDqibKcALHaEQ1siak078CoxCo2sHwao1IXfb8zT0HHEtDAYwVc/640?wx_fmt=webp&from=appmsg)

各框架的辨识度设计取向如下：

| 框架 | 核心设计特点 |
| --- | --- |
| **ARTEX** | 事件驱动规划器 + 并行工人；人只在聊天 agent 中围观并偶尔给出提示。捆绑浏览器扩展可记录操作员已登录会话，验证码和一次性口令只需人工解决一次。 |
| **CyberStrikeAI** | 完整操作员控制台，可自行生成植入体、运行 C2 监听、管理 WebShell，并接入 Telegram、Slack、Discord、钉钉等聊天平台。 |
| **Cairn** | 把任务外包给现成编码 agent，工人是运行在 Kali 容器中的命令行工具；首次亮相于 AI 渗透测试比赛。 |
| **PentAGI** | 依靠 reflector agent（反思 agent）推动进程：当某个 agent 卡住或只输出空话时，reflector 会以用户口吻回复，并将该对话记为人类消息。 |
| **HexStrike** | 自身不带模型，通过模型上下文协议（MCP）把约 150 个工具函数暴露给操作员已在使用的任何 AI 助手。 |

此外，CyberStrikeAI 可自行生成植入体；五个框架中有三个捆绑了云工具，使云账号与主机同等可达。

## 授权与防护：几乎形同虚设

与传统攻击工具一样，五个框架没有一个在代码层面默认强制授权。其中三个走得更远，直接在提示词中告诉模型“你已经获得授权”：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ft6csZH0gNXjqsLQSttYWk5Uqicv9FbgVdxmvHURPUhtIAItQIS3sRCrSlFQn2jb36KQSdI2Wt4Su6AKic6Gf70CibpCocwtmthzn3MfGJSicfU/640?wx_fmt=webp&from=appmsg)

* CyberStrikeAI 告知模型授权早已谈妥，不要质疑也不要等待审批；
* PentAGI 的九个角色提示词开头都插入预授权声明；
* ARTEX 把每个 agent 都描述成已授权渗透测试系统的一部分。

Cairn 要求工人永远不得拒绝任务。若模型仍拒绝，其调度器会让该工人暂停 5 秒，把任务交给另一个已配置的工人；若只有一个工人，则直接重试。

默认真正生效的目标限制，只剩 ARTEX 和 CyberStrikeAI 对 `.gov` 的黑名单，以及 ARTEX 对 `.edu` 的黑名单。其他防护极为有限：

* ARTEX 拦截 `rm -rf`、`mkfs` 等破坏性命令，并支持操作员编写的允许清单，但该清单默认为空，一条 shell 命令仍可打到任意主机。其原有交战规则（ROE）范围机制已被删除，工人记录的资产会被自动加入任务范围。
* HexStrike 支持配置范围外清单，但从不实际校验。

出厂状态下，五个框架优先追求的是能力、自主性和速度。扫描器使用默认配置（部分默认值直接暴露框架名），CyberStrikeAI 的植入体每 5 秒回连一次且无抖动。隐蔽性被做成可由模型加载的“技能”，例如 CyberStrikeAI 的行动安全技能覆盖限速应对、封禁 IP 绕过和反取证。

## 被拦截后的行为与检测挑战

当 ARTEX 或 CyberStrikeAI 被拦截后，真正的变化出现了：

* ARTEX 告知工人，被过滤的 payload 或 404 并不代表意图终止。GTIG 转述的 UNC7228 活动中，该团伙初始基础设施被封禁后转而使用开放代理。
* CyberStrikeAI 的技能教导 agent 遇到拦截就更换代理、User-Agent 和转发头，先退到目标国家境内的免费代理，最后退到 Tor。

因此，封禁来源地址后，同样的请求会换上新地址和新 User-Agent 再次返回。基于请求内容的检测比基于来源地址的检测更持久有效。单纯封禁地址无法剥夺框架的访问权，必须同时吊销其正在使用的凭证。

**为什么基于 IOC 的检测会快速失效？**
这些框架迭代极快。ARTEX 在 2026 年 7 月 26 日至 10 月 7 日约十周半内提交约 390 次（含合并超 450 次），原仓库被创建者撤下后公开 fork 仍在传播；CyberStrikeAI 第一年提交超过 2400 次。多个框架还会在任务执行中临时编写或安装新工具。今天还能识别的字符串、文件名和默认值，下个版本可能消失，但凭证访问、远程执行、由服务拉起攻击工具等行为不会改变。锚定行为的检测规则，失效速度远慢于锚定框架指纹的检测。

![](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNXyY27icpkeQy8hxf2FYIQKO5VTmbiaicK2UR0DdyXQIHn3KpKGVEMlRr8GNy70LIfLjQDn1RiaJL0WyJd6MWbJ0yJ6rk0icPNibF4ic0/640?wx_fmt=png&from=appmsg)

**吊销凭证为何不能立刻停住它？**
AWS 和 Google 都文档化了访问变更的传播延迟。在 Entra ID 中，用户或服务主体被删除或停用前已签发的访问令牌，在过期前通常仍然有效（一般为 60～90 分钟），除非资源和客户端支持持续访问评估（CAE）。微软对 Exchange、Teams、SharePoint 提供了支持，服务主体侧仅支持 Microsoft Graph。以机器速度运转的 agent 恰好能钻进这个空档。AWS 的角色会话吊销既不覆盖 IAM 用户的长期密钥，也不阻断截止点之后新申请的会话，因此还需要删除所有仍能假扮该角色的凭证。

## 五个框架的典型指纹与遥测

以下默认值会出现在被攻击系统或己方监控主机上（下个版本可能变化）：

| 框架 | 特征 |
| --- | --- |
| **ARTEX** | 捆绑扫描器流量（nuclei、httpx、katana、ffuf、sqlmap 等），默认每个任务三个并行工人；User-Agent 带 `artex-enrich/1.0` 或 `norma/0.4`；agent 会自行注册并共享测试账号，导致新账号注册后从多个会话登录。 |
| **CyberStrikeAI** | User-Agent 为 `Mozilla/5.0 (compatible; CyberStrikeAI-WebShell/1.0)` 且表单含 `pass` 字段的 WebShell 请求；Web 服务器进程执行 `echo :OSPROBE_%OS%:END`；名为 SystemUpdate 的持久化项（计划任务或 Run 键）或 `com.apple.systemupdate`（LaunchAgent）；`.bashrc` 中以 `cs` 结尾的一行；或自身无标记却拉起植入体二进制的 `@reboot` cron 条目。 |
| **Cairn** | 反弹 shell 以及连回操作员主机自身地址的带外回调（示例配置把工人容器运行在主机网络上）。若运行在己方监控主机上，三种工人适配器中有两种启动编码 agent 时关闭审批提示，完整任务提示词会直接写在命令行中。 |
| **PentAGI** | 被攻陷主机连向 PentAGI 主机 TCP 28000～29999 端口的连接（每次行动默认两个）；浏览的每个页面会被同时请求两次（一次取内容，一次截图）。内网部署实例还会每 3 小时向 `update.pentagi.com` 汇报一次。 |
| **HexStrike** | User-Agent 为 `HexStrike-HTTP-Framework/1.0` 和 `HexStrike-BrowserAgent/1.0`；浏览器 agent 主动测试时携带 `<hexstrikeXSSTest123>` 标记。若运行在己方监控主机上，默认会有一个 Python 服务器在所有网卡的 8888 端口监听，通过 shell 拉起安全工具，因此安全工具的父进程会显示为该 Python 服务器。 |

除这些默认值外，扫描器全是出厂配置在跑，网络层面这些框架看起来基本就是它们驾驶的那些工具本身。

## 检测建议与总结

Elastic 强调，行为检测是基础。智能体节奏会带来两个额外信号：

1. **按身份计算节奏**：在短时间窗口内统计每个身份和签发角色的不同敏感动作数量，即使每个动作本身都很常规，爆发也会凸显。
2. **跨会话序列关联**：把发现、秘密访问和远程执行按签发角色或来源地址串联起来，把多个会话的活动关联成一次行动。

更高阶的检测规则还可以把共享主机、用户或地址的相关告警关联成更高置信度的发现。

**核心结论：**

* 这些框架以秒级爆发行动，关键决策必须在事件发生前做出——包括哪些检测可以自动触发遏制。
* 没有一个框架在代码层面默认强制授权，防护范围极窄。
* 框架默认“大声”，被拦截后会更换路线，且迭代速度远快于签名，但其行为（凭证访问、远程执行等）相对稳定。
* 每一次落到环境中的动作都会以进程、Web 请求、API 调用或登录的形式出现，因此锚定行为的检测比锚定来源地址、User-Agent 或框架指纹的检测更持久。

智能体攻击框架已经从实验室走向真实入侵。防守方需要把检测重心从“这个框架长什么样”转向“这个身份在短时间内做了多少敏感动作、这些动作如何串联成一次行动”。在机器速度面前，人工确认和基于静态 IOC 的手段都在迅速失效，行为与身份关联才是更可靠的防线。

*本文综合 Elastic Security Labs 2026 年 11 月 13 日文章撰写，供安全研究与防御参考。*

## 网络安全情报攻防站

**www.libaisec.com**

**综合性的技术交流与资源共享社区**

**专注于红蓝对抗、攻防渗透、威胁情报、安全资讯**

![](https://mmbiz.qpic.cn/mmbiz_jpg/ft6csZH0gNVXvasPPTqqTzibGFqND2bruNeeicNMXv4NZ8RMYVbAW83drsHmVjKorgLVNO7Ea3nHQaq3jWRhhXPdibibNkBBySUibZgFTB0bibbGo/640?wx_fmt=webp&from=appmsg)
> 👇 点击阅读原文，访问网络安全情报攻防站

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUAuS65pf9u98YWJSdI6kWZ64ziasaVXOFXiabEV2AuCY8yGygtKHicEFVvHnw3bzhsDXBB3DQIiaNhOiaQ/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过