---
title: AI安全运营缺的关键层，长亭开源了！
url: https://mp.weixin.qq.com/s/74GKBw1CNW6QsLisdNWSmg
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:48:52.752898
---

# AI安全运营缺的关键层，长亭开源了！

![cover_image](http://mmecoa.qpic.cn/sz_mmecoa_jpg/iaZq4cu1zibCwHcZQhm1xWXmnjdsCqVORuQmjKoVnlbf4ceM0NeKE9IrA3DCtcTHOHm5aW3BibbWjt5NTC9IsW8gw7IKrwAXq4J2u75MBUpydU/0?wx_fmt=jpeg)

# AI安全运营缺的关键层，长亭开源了！

长亭科技

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![长亭科技首图.gif](https://mmbiz.qpic.cn/sz_mmbiz_gif/uX9TOlqibIRt44X90E9PETrmK51HlViaYlbb192iabZdBhB8oGpvdVf6QxujNWwCNGcHlXKe1PCQ5WOWuCZUMO8WyWmqEyVTNDMSoKXHsZcwhw/640?from=appmsg)

AI正在改变安全工程师的工作方式。

查资料、翻文档、写PoC、改脚本，过去要一点点啃的活，现在交给大模型能很快完成。它们读本地仓库、调终端、跑测试，甚至把陌生接口文档整理成可执行步骤。个人终端上，Agent如鱼得水。

但一到生产内网，就卡壳了。

模型不能随便接，数据不能随便出，设备不能随便碰。账号、权限、审计、变更，每一步都是墙。个人终端上那些Agent工具，在生产环境里被网络边界、权限边界和变更流程切得七零八落，Agent四处碰壁，有力使不出。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/iaZq4cu1zibCygppSiaW4B91ahv4GmG5j3qXyFmib9CPWvWa8ZZGBrzBVr2vDciaibmegpVlicD6HtF6ZetsrkibIDxXqnwRPt7veJsicp52qiaegHnibk/640?wx_fmt=png&from=appmsg)

于是大部分安全运管团队只能让AI停在“外围”：手工把数据喂给模型分析，或者在SOC侧接条消息流生成研判建议。到了真要查WAF日志、封禁IP、解封回滚、同步黑名单、通知值班群的时候，还是人来打开一个个控制台，复制参数、跑脚本、填工单。

模型缺的不是能力，缺的是**一套能让它在生产环境里大展身手的基础设施**。

**SOC看了数据，SOAR跑了流程，Agent时代缺什么？**

过去，SOC时代解决的是“看见数据”。告警、日志、资产、漏洞、威胁情报汇聚起来，让安全团队一眼看到。

后来，SOAR时代解决的是“编排流程”。重复处置动作写成playbook，让固定流程自动跑起来。

到了AI Agent时代，老流程遇到了新问题。

Agent像一个会思考、会决策的安全值班员，会根据上下文判断下一步，先查什么，再验证什么，什么时候处置，什么时候通知，什么时候停下来等人确认。

但问题就在这里，这个AI值班员，凭什么能操作你的WAF？凭什么能封禁IP？操作错了谁来负责？

让Agent真正成为一个可以放心的AI员工，除了数据和流程，AI安全运营还需要两层新的关键基础设施。

**一、让 Agent 在生产环境里可管理、可隔离、可运行。**

**二、让 Agent 能调用真实安全设备，而且调用过程可授权、可约束、可审计。**

围绕这两个基础设施，长亭开源了两个项目。

**两个开源项目，补全 AI 安全运营底座**

**Agent Compose：Agent的运行控制面**

Agent Compose解决的是Agent Session（代理会话）怎么被组织、隔离、调度和回放，面向的是Agent在内网中的运行控制面。

多个Agent在同一个环境里跑，谁能访问什么资源，谁和谁隔离，执行过程怎么记录，出了问题怎么回溯，这些基础治理能力，Agent Compose统一提供。

**OctoBus：安全设备的统一操作网关**

但光有运行环境还不够。AI要进入安全运营现场，不能只会理解文本，还需要一个稳定、清晰、可控的工具入口，去连接真实的安全设备或系统。

前不久，长亭开源了Chaitin-CLI，把长亭部分核心安全产品的常用操作统一到命令行入口。但企业的真实环境更复杂：安全设备来自不同厂商、不同版本，分布在不同网络区域，各有账号体系、接口风格和审计要求。

OctoBus解决的就是这层接入和治理问题。它把分散在平台后端、项目脚本和个人经验里的安全设备操作，沉淀成统一的开放调用入口，把一次操作需要的参数、目标设备、权限边界和审计记录说清楚。

OctoBus不是再做一个脚本集合，而是给 Agent、工作流和安全平台提供一组可授权、可约束、可审计的安全设备操作能力。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/iaZq4cu1zibCzyib9JsPuSvvXrpoQxjq9aTf82T4r7VPxGJalcRkBU3PCsfkZ28bCEJY7dYvkTL2gBzicrY2hQxd6Klib7tr5StMNNnoKxTKP1UM/640?wx_fmt=png&from=appmsg)

简单总结：

**Agent Compose 负责Agent“怎么跑”，OctoBus负责“能调谁”** 。

**为什么需要一层独立的接入治理层**

现在很多智能体平台、低代码工作流、开发框架都能接API、写插件、做连接器，解决的是“我的应用怎么调用外部服务”。但安全生产环境的问题不只是“能不能调用”，而是“谁在什么场景下，能对哪台设备执行什么动作”。以封禁IP为例，普通连接器只需要把封禁接口调通；在真实安全运营里，还要确认调用的是生产区WAF还是测试 WAF，默认封禁多久，哪个Agent有权执行，失败时返回什么错误，操作记录如何审计。OctoBus作为独立治理层，负责把这些边界前置到调用之前：service package定义一类设备能提供哪些动作，instance绑定具体设备和环境，capset控制某个Agent或某个场景能看到哪些能力、调用哪些方法。简单说，普通连接器解决“接口怎么调通”，OctoBus解决“这次调用该不该发生、能调到哪里、出问题能不能追溯”。

落到实际场景里：

* **告警研判Agent：**只能看到日志查询和威胁情报查询。
* **封禁处置Agent：**才能调用封禁、解封和地址组更新。

**接口越是开放，边界越要清晰。OctoBus要做的，就是在Agent真正执行动作之前，把设备、权限、参数和审计先治理好。**

**38个service package，只是一个开始**

安全设备的生态碎片化，是当前AI智能体进入企业生产环境的最大阻力：厂商多、版本多、现场差异多。

长亭选择开源，是想通过社区的力量，邀请行业一起搭一层公共底座：把分散的设备操作接口，把行业里反复踩出来的接口经验、处置动作和适配逻辑，变成开放、可复用、可治理的基础设施，让企业真正把AI智能体用进生产系统，而不只是停在demo里。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/iaZq4cu1zibCy3Tic7MGH0KicnXib2lpYiazgShNwQqzBT2quSJYOsFdAHEE8DUCQAvHKDWc6IM8tFib0x4d15HK006KQQQwGJcRJgTno3haJZdcjc/640?wx_fmt=png&from=appmsg)

目前，**OctoBus已经提供首批38个service package**，覆盖WAF、防火墙、ADS、NIPS、HIDS、威胁情报和消息通知等方向，包含查询、封禁、解封、地址组更新、黑名单同步、主机隔离、通知发送等常见安全运营动作。

对企业来说，Octobus的价值不是少写几段脚本，而是接入一次后，Agent、SOAR playbook和运维脚本都能复用同一套受控操作。无论上层工具怎么变，底层适配不用反复重写。

OctoBus先把这套框架、首批38个service package放出来。后续更多设备、更多版本、更多真实场景，大家都可以在这套公共组件上继续补齐。

现在，按照下面的地址，**把AI Agent带进真实的安全生产环境**，让它大展身手吧！

* Agent Compose — Agent运行控制面

```
https://github.com/chaitin/agent-compose
```

* OctoBus —安全设备统一操作网关

```
https://github.com/chaitin/OctoBus
```

* Chaitin-CLI — 长亭产品命令行工具

```
https://github.com/chaitin/chaitin-cli
```

点击页面最下方 “阅读原文” ，可直达百智云—智能体能力安全接入系统（OctoBus）。

**欢迎Star、提Issue、贡献适配，让AI安全运营的基础设施，从一行代码开始长出来。**

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Fuleibl6qMuqy3z1PNoOSxgQbUqYibAcIb722vbFGdP1gfxibthFf1IibTtFxgfSv90xVj6dPhV9oRc39O4VGUbYQw/0?wx_fmt=png)

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