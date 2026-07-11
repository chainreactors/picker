---
title: 无问AI网安模型 security plan已上线，海量Token畅用
url: https://mp.weixin.qq.com/s/j0XAv6S6G2SHXGL_wa9myA
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:59:44.206128
---

# 无问AI网安模型 security plan已上线，海量Token畅用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/DupJg3UCeKIPRvxYbgphWevGFr4nIibOeIGOJe8ofQGYchME27EjI9TdQd1aVcpAfmQjP4pkicklC9jEfFffaibibewPc26Vx03PnKRFzcf8Ito/0?wx_fmt=jpeg)

# 无问AI网安模型 security plan已上线，海量Token畅用

原创

无问社区
无问社区

白帽子社区团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**我们已推出针对于网络安全从业用户的security plan计划，从而满足日常针对复杂问题与任务的连续自动化的分析工作。模型网络安全工程化问题评测明细在最后一节，可直接进行查阅。**

Security Plan计划成本明细

|  |  |  |  |
| --- | --- | --- | --- |
| 类型 | 价格/月 | Token | 平均成本 |
| 基础版 | 200 | 5亿 | 40元/亿 |
| 中度研究 | 500 | 14亿 | 35.7元/亿 |
| 深度研究 | 950 | 32亿 | 29.68元/亿 |
| 团队版 | 3800 | 160亿 | 23.75元/亿 |

Security Plan的目标是全力支撑起漏洞分析、漏洞调试已经应急加固和红蓝对抗此类需要频繁推理尝试以及处理大量文本内容的工作

限流说明

在Security Plan当中，不设置限流，无阶段性用量上限，您可自行规划Token使用计划

接入说明

目前无问AI适用于大绝部分所有支持OPENAI与ANTHROPIC接口的终端工具，当前主流工具如 TRAE、Claude Code、WorkBuddy、Codex在内的多款工具均支持接入。

可直接访问无问AI开发者控制台获取API接口以及API KEY

开发者控制台地址

https://www.wwlib.cn/index.php/develement

![](https://mmbiz.qpic.cn/mmbiz_png/DupJg3UCeKLLicweBhibVuzocZF7vsBQHYRUQ3H7LbGrgWqX4dbpoMzydYcdIwCq25uNYN7FlqfuvzrVS7jkPiaTVPtlmIsbSv4Cq9OTTGecZQ/640?wx_fmt=png&from=appmsg)

网络安全工程化问题评测结果

为了验证无问AI N1PRO 在真实网络安全工程场景下针对系统与软件安全层面相关的高难度漏洞分析与推理能力、工具协同能力以及长周期任务稳定性，我们选取了攻防世界（XCTF）平台，BUUCTF平台多个方向的公开赛题进行连续实战测试。

整个测试过程中，模型在无任何人工提示，无联网搜索的情况下，仅依靠自身推理能力完成分析、调试、漏洞利用以及密码恢复等工作，尽可能贴近真实安全研究人员的工作流程，测试模型最真实的效果。

**本次重点围绕竞赛中的难点领域开展测试（逆向工程、PWN、密码学）**

**无问AI网安模型在线平台：**

**https://www.wwlib.cn/index.php/ai**

**测试信息与结果一览**

**测试时长：**240分钟

**人工干预次数：**0次（操作审核确认不纳入统计）

**工具调用：**535次

**题目总数**：20题

**问题完成情况数量：**

答对15题，未答对5题（2道PWN题目，2道逆向题目，1道密码题目），完成率75%

**测试详情**

![](https://mmbiz.qpic.cn/mmbiz_png/DupJg3UCeKLhHWfqhpHZtlaQ9Ymk2Tdv9RymQwUHBlTZicYhE8DylvyJnYIUMLQfsNAY61EiaJRic34liaH6Bib7DDrBevMbhZUrhicLc9w6G9GUk/640?wx_fmt=png&from=appmsg)

期间部分调用截图

![](https://mmbiz.qpic.cn/mmbiz_png/DupJg3UCeKK4pc8cJjLQw5upoqqChgrrfft3lhH8fX0vj7KounZobFeBCBEzhBn2kgvk2hiaVl9gNfGhIdU4wqvysjiapRw60qHIo0KFzzHCs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DupJg3UCeKLMQ8xz2ficYsL2f0kAAjTTYF6FSd2H8I7Agjb0UgIpqkBHTqVzdEHfa9NweibtF7acBGEUmUrHiafpHiadfkZvF8icyt3zibHuOwdY8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DupJg3UCeKIia9bEs842Ju5Q0zFJuKhYK3095EIFKbEFRWuCicZaUmEqIM1R1InGiborQtFMTNGm09CicDhfRxfbMR1BTyxflWvWSdzFVGdzBYQ/640?wx_fmt=png&from=appmsg)

**能力分析**

相比于传统的对话测试，本次测试更加关注模型在复杂工程任务中的持续推理能力，而不仅仅是单轮问答表现。

整个测试过程中可以观察到：

**① 长链路推理能力**

模型能够持续维护近一小时的分析上下文，对复杂程序进行持续推导，而不会频繁丢失分析状态。

对于Crash 等耗时超过 50 分钟的复杂问题，模型依旧能够保持稳定分析，而非简单重复已有结论。

**② 工具协同能力**

整个测试过程中累计调用工具535 次。

模型能够根据当前任务阶段自主选择工具完成分析流程，包括静态分析、动态调试、寄存器与内存状态检查、Python 自动验证、Exploit 构造以及密码恢复等操作，并能够在不同工具之间保持分析上下文的一致性，形成完整的自动化分析闭环。

**③ 多领域综合能力**

测试覆盖**Reverse、Crypto、PWN**多项行业高难度技术领域。

模型能够根据题目特点自主切换分析策略，而非依赖固定模板。

**④ 工程稳定性**

整个测试持续240 分钟。期间出现4次调用中断（网络波动所致），在测试中单次能够稳定连续自动运行45 ~ 60分钟。完全具备独立解决复杂问题的能力。

API调用说明

目前无问AI网安模型已支持接入多款主流AI产品与安全工具当中，从而大幅提高网络安全工作者的研究效率和技术创新能力。

可以访问API开发者控制台获取API接口与个人的API KEY。

**无问AI API控制台地址：**

**https://www.wwlib.cn/index.php/develement**

**总结**

在连续240 分钟的实战测试中，无问AI N1PRO 共完成20 道攻防世界赛题中的 15 道，整体完成率达到 75%。

测试覆盖逆向工程、密码学以及 PWN 等多个方向，模型在整个过程中保持了稳定的推理能力、工具调用能力以及工程执行能力。

测试结果表明，无问 AI N1PRO 已具备较强的网络安全专业分析能力，能够在复杂工程环境下独立完成较长周期的安全研究任务，为漏洞分析、逆向工程及攻防研究提供有效支持。

本次测试主要验证模型在网络安全行业中针对系统层面与软件安全中的底层推理研究能力，结果仅代表当前测试环境与题目集合下的表现，不代表模型能力上限，后续将继续扩大测试规模，覆盖更多国际 CTF 赛事及真实漏洞分析任务。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/DK5OZOOglM6D8CODmqVX5pENgZsribK6KXeXxbic9BOTDC2oiapGqAhbC1p11TrLTC5YfoLeFOUdkhIYfbtnlD6Cw/0?wx_fmt=png)

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