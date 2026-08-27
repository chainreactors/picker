---
title: 前沿AI正在重塑漏洞管理，传统修复体系面临系统性变革
url: https://mp.weixin.qq.com/s/yYeXBAqNB1nPAGC705esQg
source: Doonsec's feed
date: 2026-08-26
fetch_date: 2026-08-27T12:10:01.934925
---

# 前沿AI正在重塑漏洞管理，传统修复体系面临系统性变革

# 前沿AI正在重塑漏洞管理，传统修复体系面临系统性变革

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX0U4jmeudXseYBfeUttKx0Iv9wdFY5gzS1nwe7OxmicLX89SiaUJRn1icrfc3YGjj2Vos8NUq0q0FQ1nsfehGXuvcbrYHdA9qH6pU/640?wx_fmt=gif)

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX17xFoBY0kAFaB4573pxZiabZkSCibYN8icnK7srVGMzQNiaD3fxhiaTOvHrJrMUsIHdriawJ5CEt4HZqzIZXPqoV20JLjLiaAT19iaqHU/640?wx_fmt=jpeg)

漏洞管理自网络安全学科诞生以来一直是安全计划的核心组成部分。漏洞管理团队与补丁管理团队之间的共生关系同样由来已久，期间经历了冲突与感激的起起落落。尽管这种关系需要双方精心维护和培养，但双方始终朝着一个共同目标努力：识别漏洞并确认风险已从环境中消除。

然而，Anthropic的Mythos等前沿AI模型的出现，彻底改变了漏洞管理领域。这些模型能够识别0Day漏洞、串联复杂利用链，并实时适应变化。它们迫使漏洞管理计划进行自我审视，并提出一个问题：“我的漏洞管理计划准备好迎接这场革命了吗？”对许多组织而言，答案是否定的。许多漏洞管理计划本已岌岌可危，向CTEM（持续威胁暴露管理）式计划迁移的规划遥遥无期，而积压的漏洞更是堆积如山。

不应忽视前沿AI对安全领域带来的影响。漏洞管理计划需要进行系统性变革，以应对不断变化的威胁和风险格局。现在正是推动计划走向成熟的时机，以应对前沿AI模型给组织带来的日益增长的担忧。

漏洞管理计划涉及众多需要在运营一线管理的环节，那么应该从哪里着手提升计划的成熟度？与过去漏洞管理和补丁管理各自为政的运作模式不同，现在正是携手合作、共同应对新出现的网络安全问题的机会。漏洞管理和补丁管理计划如今都需要重大升级。

Part01

超越CVSS、EPSS和KEV

从漏洞管理的角度来看，仅凭CVSS（通用漏洞评分系统）评分不足以穿透漏洞的噪音，也无法为组织应优先处理的内容提供基于风险的视角。此外，通过EPSS（漏洞利用预测评分系统）和CISA的KEV（已知被利用漏洞）清单进行优先级排序，如今已成为漏洞管理计划确定优先级并管理漏洞清除工作的基本门槛。然而，面对前沿AI模型以机器速度将漏洞迅速转化为利用程序的情况，我们如何解决漏洞优先级排序的问题？我们需要超越CVSS、EPSS和KEV的优先级排序方法，准确了解哪些漏洞对组织而言真正至关重要。

在漏洞管理计划中建立暴露管理职能是应对这一挑战的关键途径。该职能通过评估组织攻击面上的真实风险来增强传统漏洞管理，从而帮助根据可利用性和业务影响来确定修复优先级。它有助于深入识别需要尽快处理的漏洞，并对组织风险降低产生最大影响。虽然这一思路并不新鲜，但其作为漏洞管理计划核心组成部分的必要性已大幅提升，以应对基于前沿AI模型的漏洞发现与可利用转化速度之快。漏洞管理计划需要比以往任何时候都更清晰地阐明哪些漏洞需要优先处理。

此外，暴露管理拓宽了传统漏洞管理计划的视野，不仅关注未修复的漏洞，还关注配置错误、可达性以及其他威胁情报来源等风险因素。这有助于为组织构建更强大的风险优先级图景。暴露管理扩展了所需工具集，通过持续监控、入侵攻击模拟和自动化渗透测试来验证暴露面，从而支撑更全面的漏洞管理计划。既然计划已不再依赖传统的漏洞管理风险指标，漏洞将在组织层面进行优先级排序，从而为应对前沿AI威胁提供强有力的响应。

Part02

补丁管理的变革

补丁管理团队同样将经历一场变革。不再只是等待补丁星期二（Patch Tuesday）来测试和部署补丁，也不再仅仅依靠专门流程来处理0Day漏洞，补丁和修复的速度必须加快，以跟上漏洞和利用程序被识别出来的机器速度。补丁管理需要转向自动化的补丁识别、测试和部署策略，采用环形部署方法，在前一个环验证稳定后再将补丁推送到下一个环。在补丁生命周期每个环节引入自动化，将有助于缩短漏洞在环境中未得到缓解的时间。

重要的是，补丁团队历来被要求在部署补丁时严格减少可用性中断，并维持业务方设定的正常运行时间要求。提高补丁速度可能会打破这种平衡，迫使补丁团队与安全团队携手，与组织中的关键利益相关者展开艰难对话，讨论在漏洞和利用程序以机器速度被识别、补丁频率不断提高的时代，正常运行时间要求应如何调整。

停机时间要求是否会改变？是否需要在弹性方面加大投入？与BC/DR（业务连续性/灾难恢复）团队的集成应如何变化并走向成熟？虽然这些对话起初可能令人不适，但考虑到不断变化的威胁格局，它们势在必行。应当主动推进这些对话，而不是等到网络安全事件以更高的频率发生之后才被迫面对。

参考来源：

Frontier AI: Vulnerability Management's Systemic Revolution

https://thehackernews.com/2026/08/frontier-ai-vulnerability-managements.html

### **推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0grlwwcpsEQ5CIH725a7xAnwDLGFctXFohPibiaOVyzdqwaibKgD4x4enG6jhdgJQHziaqTMy1WR0Hibx4MceSVKd6C7HGGlA9zLibg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651344398&idx=1&sn=56c4e0d580e04a250d0e8c6cffd592b8&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3eRDUpH3UJicSe4tdw7nZYu9aa5PQ9KgkaP84oZz0bVYdBiaDt97VfDBLulDp3sWLgvzI4m0mc89MZ7feP2yfFAmcRWOlicWubZ4/640?wx_fmt=png&from=appmsg)

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