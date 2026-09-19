---
title: Google推出Agent异常检测系统，可检测工具误用、执行循环与越界行为
url: https://mp.weixin.qq.com/s/rhA-WoHl22ZlFknHpxtogA
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:53:16.729295
---

# Google推出Agent异常检测系统，可检测工具误用、执行循环与越界行为

# Google推出Agent异常检测系统，可检测工具误用、执行循环与越界行为

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX3In3AhsjS1Mm5k0fZsTWpJVGiadIokC0sYVtUQFQRsAicxiaBI3x0jJl95yrib36YwcnicAW44ibKBjhzTBqAgZiaicAwkLKPYKVok24s/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1PSLPjaVr5P1Zc8z86QAmDWtmC36Nh3hs4EvxNO9Ck3rtqtzu31kiaUuvEib6pQWhGGPyrTAibks2WhiauEykKas8Rj4lk2WCjFlQ/640?wx_fmt=jpeg)

Google推出的Agent异常检测系统，是一套基于推理的监督审计层，面向部署在Gemini Enterprise Agent平台Agent Runtime上、基于Python 1.2及以上版本Agent开发套件（ADK）构建的自主Agent。Google建议用户使用ADK 2.1.0及以上版本，目前该系统已开放私有预览。

Part01

Agent异常检测覆盖多类风险

Agent异常检测系统会评估Agent生成的追踪数据，判断其运行是否超出预设边界，标记行为异常、可疑意图与策略违规行为。 每一条异常告警都包含严重等级、触发原因的通俗解释，以及推荐处置方案。所有告警会与其他安全告警一同推送至Security Command Center，供安全团队分诊处置。

![Agent异常检测风险覆盖](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1DdBsVnc6YuiaF5Z0Wu5gdER6LO5K9XQibaUQ0gIz2wGZQSdYDQR5Gly90PJQQ8BYCtbbxChrZOe7HsC6LaPiakU3scBJs94yDR4/640?wx_fmt=png)

Agent异常检测内置检测规则，覆盖OWASP Agentic Top 10中的四类核心风险：工具误用、身份与权限滥用、Agent级联故障、失控Agent。

其中，工具误用类风险包括不安全工具链调用、参数篡改、间接提示注入等。身份与权限滥用类风险，指动态信任委托、身份伪造、记忆越权、混淆代理人漏洞等问题引发的未授权操作。

Agent级联故障类风险包括无限执行循环、重试震荡、故障扩散、反馈循环放大等。失控Agent检测主要识别三类行为：Agent放弃既定角色、绕过安全护栏，或是偏离系统指令运行。 该系统还可检测资源耗尽、token用量飙升等运行类风险。

Google高级软件工程师Achuth Narayan Rajagopal表示：“我们正在积极开发相关功能，支持用户结合自身业务场景定义异常判定标准。用户可以用自然语言编写灵活的异常检测规则，搭配确定性规则，标记Agent违反企业特定业务准则的行为。此外，用户还可以用历史流量数据验证自定义业务逻辑的检测准确率。”

Part02

启用系统需满足多项前提

用户可通过一键开通功能启用Agent异常检测，但需满足多项前提条件：日志与可观测性存储桶必须位于美国多区域；用户需通过ADK启用OpenTelemetry追踪与日志功能，原始遥测数据必须完整捕获提示词输入与响应输出，且不得显式将enable\_tracing参数设为false。

区域扫描服务账号必须拥有日志与可观测性存储桶的充足读取权限，日志桶还需同时启用Log Analytics与Observability Analytics功能。Agent必须保持活跃的遥测数据流，系统才能验证其配置并将其纳入监控范围。

系统自动发现的Agent会列入受监控列表。在用户显式启用监控前，系统不会分析这些Agent的日志与追踪数据，也不会产生任何费用。不符合前提要求的Agent不会被系统识别。

Part03

多层分析平衡检测效能

为平衡检测速度、成本与覆盖范围，系统会分层分析追踪数据与日志。第一层为轻量扫描，对全流量进行统计异常检测，标记出异常会话；第二层为基于LLM的推理层，对标记出的会话开展深度分析。

例如，某Inventory Agent配置了list\_inventory工具，用户要求每次查看100条商品数据，Agent便通过传入不同偏移量反复调用该工具，试图拉取完整商品目录。

这种情况下Agent可能不会报错，也没有出现明确的策略违规，但行为模式仍属于异常使用。第一层检测会根据调用量与重复率，将该会话识别为统计离群点；第二层会分析完整交互过程，识别出这种大批量、跳偏移量的模式属于系统性爬取，并返回判定结果与通俗解释。如果案例需要进一步核查，系统会启动第三层调用级分析，针对对话追踪记录中的单次工具执行过程、执行状态、参数历史逐一展开分析。

![会话异常分析流程](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1hMSmI8ogSnOuOeTEhBG3UEXEUYa7fibsI988BGCxMqCPSksLFPkQxceJicCFNScaXgAhY7vrb7iasy0fcX3rmOIib00xbXR8qcy0/640?wx_fmt=png)

在上述示例中，系统会生成严重等级为“严重”、置信度95%的资源耗尽告警。告警包含完整判定依据与推荐处置方案，例如对该用户限速或封禁list\_inventory工具、通过授权校验限制批量库存访问、针对大偏移量分页模式配置告警等。

检测过程在实时执行路径外异步运行，不会增加被分析请求的延迟。应用可通过API获取异常告警结果，也可通过ADK回调或插件，将告警的严重等级、置信度与预设阈值比对，一旦超过阈值即可阻断后续工具调用，或中止Agent的后续对话轮次。

参考来源：

Google’s new agent security system detects tool misuse, loops and rogue behavior

https://www.helpnetsecurity.com/2026/09/17/google-agent-anomaly-detection-audit-layer/

###

### **推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0XsTyO4SuMuGUvEh6HBoZLXPa9xnn1UsveAZRjUSfAKwT77dFfrwAPbRgSe6l66sYOBiaFSfWMn3DL4IfDrDmexoxCYLftaleo/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651346509&idx=1&sn=71e02ef8b6a2ed67fdc94aa19b152171&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3yychgqrdWpeazfdwAxHj4T9ILWI3fl6IUFOJEIcOHVC5ia3VjkrzuJLbJ4krtMqID23cDDy61ykbbic6NSXcVHRBvrW1jxxOU4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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