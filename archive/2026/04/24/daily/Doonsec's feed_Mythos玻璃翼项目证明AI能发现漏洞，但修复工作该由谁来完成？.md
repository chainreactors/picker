---
title: Mythos玻璃翼项目证明AI能发现漏洞，但修复工作该由谁来完成？
url: https://mp.weixin.qq.com/s/1N5QY453xAWwUM3pvW2Yiw
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:33:20.199342
---

# Mythos玻璃翼项目证明AI能发现漏洞，但修复工作该由谁来完成？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1es1MeiaFTpM4na7RGE9x2Q5w1BINeRax1QV7cozwrgcicksaexGsOFaSAbeNWvvQ40KylakKFtHek8N7LaWvaOMXVL2ws6SEQU/0?wx_fmt=jpeg)

# Mythos玻璃翼项目证明AI能发现漏洞，但修复工作该由谁来完成？

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0skh5iaG47INDKo10sx0bI4Q0chfZ1cRovf79U5raDAD6rq0zD1UDaRxewIOqNPPJlhAunrNwA1WWX3WZIwXA41jv4marEGTzk/640?wx_fmt=png&from=appmsg)

##

上周，Anthropic公司公布了玻璃翼项目（Project Glasswing），其AI模型在发现软件漏洞方面效率惊人，以至于该公司采取了非常规措施推迟公开版本发布。目前仅向苹果、微软、谷歌、亚马逊等企业联盟开放访问权限，旨在赶在攻击者之前发现并修补漏洞。

作为玻璃翼项目前身的Mythos Preview模型在所有主流操作系统和浏览器中均发现了漏洞。其中部分漏洞在经历数十年人工审计、激进模糊测试和开源审查后依然存在。有一个漏洞甚至在OpenBSD中潜伏了27年——该系统被公认为全球最安全的操作系统之一。

人们很容易将此归类为"AI实验室宣称其AI过于危险"的套路，类似OpenAI当年对GPT-2的操作。但这次情况有本质不同：Mythos不仅发现了独立漏洞（CVE），更实现了：

* 将四个独立漏洞串联成攻击链，同时绕过浏览器渲染器和操作系统沙箱
* 通过竞争条件在Linux系统中实现本地权限提升
* 针对FreeBSD的NFS服务器构建了包含20个组件的ROP链，攻击载荷分散在多个数据包中

对比鲜明的是，Anthropic前代旗舰模型Claude Opus 4.6几乎完全无法自主开发漏洞利用程序，而Mythos在Firefox JS引擎测试中成功率高达72.4%。这已非理论推演或三五年后的预测，而是即将到来的工程现实。

##

**Part01**

## ****玻璃翼项目暴露的真实网络安全缺口****

安全负责人最应警惕的数字是：Mythos发现的漏洞中仅有不到1%得到修补。全球最强大的漏洞发现引擎对阵最关键软件系统时，整个生态却无法消化其输出。玻璃翼解决了发现问题，但修复难题仍悬而未决。

防御者为何力不从心：日历速度 vs 机器速度

网络安全行业多年来始终绕不开这个结构性矛盾，AI的介入使其无法继续被忽视。防御者遵循日历速度工作流：收集情报→制定方案→模拟威胁→实施缓解→循环往复，顺利时完成周期仍需四天。而攻击者（尤其是全程运用大语言模型的）正以机器速度推进。

AI驱动的攻击已实现全自动化

今年初，某攻击组织在针对FortiGate设备的攻击链中部署了托管LLM的定制MCP服务器。该AI自主完成：后门创建、内网拓扑测绘、漏洞评估、以及优先执行获取域管理员权限的攻击工具。最终导致106个国家2516家机构同时沦陷——从初始访问到凭证转储再到数据外泄，整个攻击链完全自主运行，人类仅事后查看结果。

AI漏洞发现速度远超修复能力

攻击与防御的速度差并非新现象，但原本细微的差距现已裂变为鸿沟：

* AISLE等自主系统在OpenSSL近期协同发布中发现14个CVE中的13个，这些漏洞曾逃过多年人工审查
* XBOW成为2025年HackerOne平台排名第一的黑客，超越所有人类参与者
* 从漏洞披露到武器化利用的中位时间从2018年的771天骤降至2024年的数小时
* 到2025年，多数漏洞将在公开披露前完成武器化

若将Mythos级发现能力纳入此图景，世界不会自动变得更安全，只会迎来需要人工核实的海量有效发现，而组织流程、业务连续性考量和补丁周期等环节十年来未有本质改变。

**Part02**

## ****如何构建适配Mythos的安全体系****

面对玻璃翼项目，本能反应是追问"如何发现更多漏洞"，但这实则是错误命题。真正的问题是："当数千个可 exploitation 漏洞明日出现在你案头时，现有体系能否有效处理？"对多数组织而言，诚实答案是否定的。根源不在于工具或人才短缺，而是依赖周期性人工启动流程的结构性缺陷——这套机制设计初衷是应对细水长流的漏洞，而非排山倒海的冲击。

我们无法修复所有漏洞，也无法实施所有加固方案。这非悲观论调，而是有效安全体系的务实起点。关键问题不是"CVE是否严重"，而是"该漏洞在当下部署环境中是否具备可 exploitation 条件？"适配Mythos的安全体系需要三大支柱：

第一：信号驱动验证替代计划性测试

当新威胁出现、资产变更或配置漂移时，防御措施需立即针对具体变化进行测试，而非等待季度渗透测试或人员档期。"计划性验证"的前提是威胁环境稳定，如今这个假设已彻底失效。

第二：环境特异性上下文优先于通用CVSS评分

玻璃翼将产生CVE雪崩，但多数漏洞管理程序仍依赖CVSS评分排序。这种脱离上下文的指标仅反映漏洞理论危害，无法判断在具体基础设施中的可 exploitation 性。当发现量从数百激增至数千时，无上下文优先排序不仅降低效率，更会彻底瘫痪流程。

第三：闭环修复消除人工交接

现有模式无法应对"漏洞披露数小时内即遭利用"的新常态。典型流程：扫描器发现漏洞→分析员分类→工单转交其他团队→数周后打补丁→无人复验。这套人工交接链正是系统崩坏处——若从发现到修复再到复验的周期离不开人工转单，就永远无法接近机器速度。

这并非要求采购更多工具，而是发挥防御者唯一不对称优势：你掌握组织拓扑而攻击者不掌握。但该优势的发挥前提是能以机器速度行动。

**Part03**

## ****自主暴露验证如何弥合差距****

## ****Picus的解决方案****

需要坦诚说明：本文作者来自Picus Security——家专注于自主暴露验证平台的厂商。玻璃翼项目让我们及交流过的众多CISO认清：暴露管理程序中的验证环节已成为最关键瓶颈。漏洞发现即将变得极其高效，而修补过程仍将缓慢痛苦，其间唯一可控杠杆是识别真正关键的漏洞——这正是验证的价值。

从四天到三分钟：Agentic工作流如何变革周期

我们开发的Picus Swarm AI团队将传统四天周期压缩至分钟级。这套AI Agent协同完成了原本需要四个团队交接的工作：

* 研究Agent接收并审核威胁情报
* 红队Agent对照环境生成经安全检查的攻击方案
* 模拟Agent在实际终端和云环境执行，收集遥测与证据
* 协调Agent衔接发现与修复环节：创建工单、触发SOAR方案、推送攻击指标至EDR、验证修复效果

所有操作皆可追溯审计，各Agent在预设边界内运行。从接收CISA警报到生成可立即修复的验证结果，全链仅需三分钟。当Mythos级模型抛出数千发现时，你需要能立即判断哪些在特定环境中可 exploitation、现有控制措施能否拦截、以及供应商专属修复方案的系统。

**Part04**

## ****令人不安的真相****

衡量玻璃翼项目的唯一标准将是：多少漏洞在被利用前得到修补。无关发现数量或攻击链复杂程度，关键在于生态能否消化AI的产出。单纯可见性从来不够——83%网络安全项目仍无实效。改变游戏规则的是弥合发现与实证的差距：确认潜在漏洞是否真会危及你的环境。这就是验证的价值。在后玻璃翼时代，它将是漏洞洪流与入侵浪潮间的唯一屏障。

**参考来源：**

Project Glasswing Proved AI Can Find the Bugs. Who's Going to Fix Them?

https://thehackernews.com/2026/04/project-glasswing-proved-ai-can-find.html

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1NlibR8DpnkZguk1so3ThwkXScRIP7SKicZdaVeLa1eMHdfLgFsOaFCP6qt2JaDlnDPzLe5MJBV1micoP6YM0SG5C9X1ibsshUiccM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337140&idx=1&sn=134af642d92b85fc1076a8c83c09945c&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1bKq2xLKwFuy1Yl63ibm7kJUCW7hP4uRIhllVu6icLPkYcerZIx5264cbnPu5uCLCpb0ic16Gm32GC3B6ou34yFia9Nm4YJTGU4iag/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

向上滑动看下一个

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