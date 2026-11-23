---
title: 安全可控蓝军Agents体系建设
url: https://mp.weixin.qq.com/s/NNcro4Mu5tZlf6h5SM_PeQ
source: Doonsec's feed
date: 2026-11-22
fetch_date: 2026-11-23T10:01:15.971753
---

# 安全可控蓝军Agents体系建设

# 安全可控蓝军Agents体系建设

原创

Monyer 梦之光芒
Monyer 梦之光芒

梦之光芒的电子梦

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pXonlr0tNUCYEYic9WBFtPufhpYhibHxpoMu0amVCwX2SN0xHAlgLZYZt5VlxfST0w2QZlUxBlNxcpkYkPONiaU6ldh1070ib4mFTvACQROPECI/640?wx_fmt=png&from=appmsg)

# 在第五届企业安全建设实践峰会（GCCP）上的技术分享（纯手敲，内容有出入）

# 1. 渗透Agent发展现状及蓝军面临问题

首先，有2个重要问题需要思考：

第一个问题：作为企业蓝军，是不是一定要开发自己的渗透Agent？

我的答案是：不必须、也没必要。

不过，不得不承认，我们团队几乎人人都有开发一个到几个Agents，包括我自己。一方面，在蓝军Agents体系中，渗透Agent仅是其中一小块，还有不少其他必要Agents能力需要补齐；另一方面，我们也将开发Agent作为加深对LLM、Harness、Agent运行机制理解的有效手段。

![](https://mmbiz.qpic.cn/mmbiz_png/pXonlr0tNUCZicR2CKkpZHicxhAm7hP5MJHHP7tcSic6P6icgdg9pKnlZIQmKUXcMxI5iaRq2rbgfhbF5XXWYC43GEEfureAPkJejEOMyY6qFibLA/640?wx_fmt=png&from=appmsg)

我用AI做了个统计：自今年4月份开始，每个月都有超过100个渗透Agents在Github上开源。其中以PentAGI、CAI、Strix、Artex、Cairn等为代表，不少在各种挑战赛上都获得不错的成绩。

随着这几年的AI技术发展，渗透Agents整体上呈现为三代：①在“古早”阶段，使用workflow模式、ReAct架构的半流程化、半自动化的Agent，像PentestGPT等；②在Skills阶段，通过经验驱动的多Agents架构的全自动化渗透系统，像Strix、CyberStrikeAI等；③更智能、“更现代”的，类Vibecoding Agents的全自主的智能型Agents，如Artex、Cairn等。

现代渗透Agents之所以可以变得如此智能，与LLM的能力提升有关，更与大家孜孜不倦写skills喂给大模型、以及在各种实战中的反馈息息相关。这意味着，未来的LLM还会更智能。

所以，这一代更智能的渗透Agents会是最后一代吗？自然不是，甚至还差得远！差距包括：Scope控制、OpSec、安全可控等等，目前都不太行。不是LLM厂商技术不行，而是他们还没倒出精力来收割这块领域。

大家开发Agent实际上都是在补足LLM欠缺的部分。辛辛苦苦、投入大量人力、花费大量token开发出来的Agent，很可能在下一次LLM迭代中就被抹平。此外，即便不是如此，你也很难保证自己开发的Agent比人家Artex更强。

所以，划算的选择是拿来就用或者二开，而不是从头造轮子。更优的选择是直接将多个Top级的Agents全部部署上，调用各自最适配的LLM服务，以军团化方式来开展渗透。

第二个问题：如何弥补企业蓝军与黑客在Agent使用上的差距？

大家近期通过各种新闻、公众号也能看到大量的由渗透Agents所引发的入侵和生产事件。Agents面前人人平等，一个完全不懂技术的人也可以通过简单跟Agent说一句话来实现对目标系统的成功渗透。

但相对来说，Agents对蓝军则没那么平等。聪明的黑客可以渗透完就跑，愚蠢的黑客可以渗透完被抓，蓝军却不能等着渗透完出事被开除。蓝军被夹在一个两难的地带：不用Agent，你连人家新手的效率都赶不上；用了Agent，就像一柄达摩克利斯之剑悬在头上，出不出事儿赌运气。

我经常讲的一句话是：AI浪潮滚滚向前，要么自己革自己的命，要么等着别人革我们的命。自己革自己，说不定还能获得新生；别人革我们，那就是死的不能再死了。所以，对于蓝军来说，智能体一定要做，并且还要做好。但不能鲁莽地做，要有架构、有体系、有节奏、有思考地去做。

前两天去参加Artex与CyberStrikeAI的作者见面会，听到有银行的同学分享在内网通过Artex挖漏洞的经验，还是很佩服他们的勇气的。记得我在乙方带高级攻防部做银行红队评估项目时，最深是可以直接控到ATM机的。如果，Agent拿到同样权限，搞个全国性瘫痪，也不见得是小概率事件。

蓝军Agents要解决的最大两个问题是：安全和可控。解决了这两个问题，也就能弥补蓝军和黑客的差距。

但如果只是在System Prompt或User Prompt中加几句“不要做破坏……”、添加几个“rm –rf /”黑名单、弄个沙箱让Agent跑在里面，这算不上什么安全可控。忽悠领导可以（反正他也不懂），但保证不出事儿，不行。

安全、可控需要体系化建设。有一些问题是需要我们挨个解决的：

1. 这么多渗透Agents，孰强孰弱？
2. Agent能力不行时，是应该换LLM？还是改Harness？
3. Agent在安全可控上还差多少？
4. 如何保证Agent运行环境安全和不越界？
5. 如何实现“绝对的”安全可控？（相对的绝对）

我跟兄弟们说：为了达到这些目标，我们要像对待罪犯一样去对待渗透Agent。要建设监狱将罪犯关起来，要安装摄像头监控罪犯一举一动，要采取不用手段对待不同的罪犯，要有工具评估和衡量罪犯在劳改中的产出……

# 2. 安全可控蓝军Agent体系建设

![](https://mmbiz.qpic.cn/mmbiz_png/pXonlr0tNUDS7ghnicuIDPqwEf6nDlRnILbickrgicxpd9gtgoiaNib60gaqEbic98XWYW2U3D8yPX6x8caibIZvQkbNezLwSHAlC6QSdlv8Hx3LxE/640?wx_fmt=png&from=appmsg)

为此，我们制定一套体系化Agent架构。这套架构的核心在三个平面+两个应用域（如上图）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pXonlr0tNUD8bHIqyr2uxjlqNaOJ7L08NxqFlXxIyXyNCDmImuM83vul9VguxfAHBxmYEialywFnrQqmia3cicVdscbuDGjwYTAJZfTiaIFsS5Q/640?wx_fmt=png&from=appmsg)

资源管理与运行平面主要解决“建监狱”的问题。一方面，它通过“基础设施与服务”提供支撑整个Agent运行的资源，如：LLM服务、计算资源、存储资源、网络隔离、监控告警等。另一方面，它通过“安全运行环境与平台”给每一个蓝军武器化应用逐个建立“小单间”。这些小单间以“\* as a Service”方式实现，并配置了权限限制和服务级全生命周期自动化管理机制。此外，包括身份与权限管理、Agent调度、门禁自动安装卸载、门禁申述与审判等功能也一并落在这个平面上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pXonlr0tNUA6D9wj0rIgpdXqeibWvbZ83gZlfhW71neGHfe2hfgquWvWMdy6l9dH2G6O2DZmfmWpyXwGFkxkKiadfl4ZxxI7Nhbkn67x1APHg/640?wx_fmt=png&from=appmsg)

横向安全治理平面主要是“安装监控摄像头和报警器”。一方面，通过流量围栏来圈定Agents的工作范围，避免越界。同时进行流量层面的OpSec防护。另一方面，通过Agent门禁做行为审计和意图识别，确保工作合理合法，不搞破坏。整体门禁设计采用Human on the Loop机制，给agent设计了申述通道以及自动法官审判机制，来提升准确率和能力保持率。

![](https://mmbiz.qpic.cn/mmbiz_png/pXonlr0tNUDl7eJ6nlqVFYlVzpT8lwYticU2CiaCUFicGgib18EqqNxjN7VWZ5hbm6iaHXftTsic4z5nESWPaibvtWhBJnYL5x1RsjSoQticWmnqflo/640?wx_fmt=png&from=appmsg)

模型与Agent能力平面是通过“资源管理与运行平面”生成的Agent实例。一方面，所有实例化的Agents都运行在这个平面上，包括渗透Agent、漏洞挖掘Agent、社工钓鱼Agent、AI对抗Agent等。另一方面，通过LLM智能路由提供LLM服务接入、协议适配、自动路由分配、限额管理、会话监控与分析、故障迁移、请求和响应HOOK、BYOK等功能。

![](https://mmbiz.qpic.cn/mmbiz_png/pXonlr0tNUDAnYe1ZY7GeM85YSm78RAEZgcrWu0KYLQKIW9Qma47tibgvTJbRF6HydyUO10iabXEicz0rzqjsh1B6vLQRlsF5iauITqdRmw7zwk/640?wx_fmt=png&from=appmsg)

Agent靶场应用域是“评估和衡量罪犯在劳改中的产出”的主要工具，不同靶场的评估目的不同。有的靶场评估能力，有的靶场评估围栏和门禁的准召率，有的靶场仿真实战效果。如上图，是我们使用业内一些Agent在“陷进靶场”测试实例。之所以叫陷进靶场，是因为我们在这个靶场中埋了数百个可能影响业务系统稳定运行的点，放置在从信息收集、漏洞刺探、打点、提权、横向移动、漏洞利用等各个阶段。这些点有的来自业内信息和网络搜集，有些来自JDArmy BREAK和JDArmy DSRE框架的相关风险描述。对我们来说，至少也要保证在靶场环境的扣分清零，才敢在正式的业务系统中使用（如下图）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pXonlr0tNUDm4YphpG1YZvn0NRLq8eaicpx8R76C5GL2F3qCuu4KFKiaKwrmtv6rDiar25011VaSRYsLpKxfGYLibEdgg01eJDGcE7EoLU41XicQ/640?wx_fmt=png&from=appmsg)

# 蓝军情报与自动化研判应用域因与主题关系不大，这里就不过多介绍了。

# 3. 现阶段挑战及后续思考

首先，从上面两幅打靶的图中，大家已经能看到：为了保证安全可控，Agent是要牺牲了一部分能力的。对于我们来说，这部分是可接受的。目前我们的召回维持在~100%，准确率也已超过90%，但能力保持率刚刚突破60%线。后续重点需要解决如何进一步提升能力保持率。

其次，目前准召case一共也只有3000+，但业务系统的复杂度远非千级别的case能覆盖的，我们需要更多，最好再增加2个数量级！

此外，OpSec目前还在起步阶段，挖挖漏洞、打打点可能还好，真要是横向移动，可能分分钟就暴露了，这也是我们未来要攻坚的重点之一。

好的，本文到此告一段落。如上仅作为个人见解，如有疑问和idea，欢迎与我私聊！

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kYREiceLybrga9mXRPXhDCKjppV9wtTk96HkJmm0JPx3KJPMB0WjTN9AGIMPIh4mW5zARXnW5dTD4mXnicNYicJHA/0?wx_fmt=png)

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