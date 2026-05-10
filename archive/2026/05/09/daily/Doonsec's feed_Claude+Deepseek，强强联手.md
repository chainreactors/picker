---
title: Claude+Deepseek，强强联手
url: https://mp.weixin.qq.com/s/K8IHwdhB3liAKSle659YcQ
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:36:02.336934
---

# Claude+Deepseek，强强联手

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2PhZXrB0gN4Mib2OyTcgBibJ8uXevdkBJa1Bgr9SHcznvcM6C1TooWuicwfmicKicmwX2on0kEVrqsQa4qmxFicYz3zmQiaQhiatRoyR89ITibicibiarnM/0?wx_fmt=jpeg)

# Claude+Deepseek，强强联手

白帽子

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于MicroPest
，作者MicroPest

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4Js0Fg5RusDlZibK1UwhTjVtSot4fe7fa4m608ZbrWXkg/0)

**MicroPest**
.

个人开发的小工具

用Claude的优秀界面和Agent能力，配上DeepSeek V4的高性能和成本优势，本质上就是一次“1+1 > 2”的精巧整合，目标就是追求那个最佳平衡点：**既要极致体验，又要性价比，还要省心**。

这是一篇笔记，没什么含量。

因为付费的问题，很久没用claude了。看到有人用claude的程序外接deepseek的大模型，强强联手，试了下，确实不错，记录下来。

1、下载claude

https://claude.ai/login

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN6dv6jEX24VIMWIAu8EMdQHX4icghyDoIE3TWyWZRTH1O0mtho4nvRWqQn8pP2ezXF6C7U7l9KoSqCTWkRxlHCfgj8rbic5Bf69Y/640?wx_fmt=png&from=appmsg)

为什么这个要强调，因为下了几个都下的不对，跟后面的衔接不上。

2、安装好后，一般会在这个路径下：

C:\Users\Administrator\AppData\Local\AnthropicClaude

3、运行后，安装好先别登录账号。第三方模式和 Claude 官方账号互不兼容，之前登录的要先退出，重新打开。

打开顶部菜单 Help → Troubleshooting → Enable Developer Mode，打开开发者模式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN7qcxNu5ib0rrnPFyxI5IbHWROJqUxNicIwxQpQO8PHm26BlGPnH2APcic0Hiak470w7Pa0kIP0spyVsPr76eAvPaicd3r8fpjlaO0U/640?wx_fmt=png&from=appmsg)

按提示重启，菜单栏会多出一个 Developer 的选项。

![](https://mmbiz.qpic.cn/mmbiz_png/2PhZXrB0gN5zLsS8WqssbQewEdfd3nic168WnGUCFQqUBNjiavv6KSrlH4whL4nv2j0HibRI1njbQuqqRsvrXUaAERddicfxicQBoNalzIpyPx1c/640?wx_fmt=png&from=appmsg)

依次填写如下内容：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN5bJnWlXiaZYRcaBTHVLsTb7KSDPeDBhia0GicILwGwpnicOnDm1JCRsLibkPv6EmLe8rcbicJhGErwGLwd7dK51iasJUvMsdRvpsAfHs/640?wx_fmt=png&from=appmsg)

Cowork 和 Code 都是 agent 类型的请求，DeepSeek 会自动把思考强度设成 max，这就是满血版 V4-Pro Max。模型 ID 下面有个 1M-context 开关，记得打开，[1m] 后缀解锁百万上下文。

加完点击右下角的 Apply locally，然后选 Relaunch Now。桌面客户端会自动重启。进到主界面，你会看到有 Cowork 和 Code 两个标签。

默认模型就是刚才填的 deepseek-v4-pro[1m]。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN7QMO0iasSgNiclZcVWa8N020c9QPTYIE6jObL3fOgGnnPkXQIodcpWBxwybarlt7PtibIypagVf9HkJFkNiatXce700S1R6ZVjQk4/640?wx_fmt=png&from=appmsg)

4、能接的模型，远不止 V4。

Gateway 只认接口协议，理论上任何兼容 Anthropic 的模型都能接入。

一个桌面客户端，随意切换多个模型。

Cowork 是给非技术用户的桌面 Agent，读你电脑里的文件、整理表格、写报告。Code 是带图形界面的 Claude Code，能调用系统命令、Skills、MCP。

5、综合来看，这个组合的表现可以称得上惊艳。

* 整体表现足以媲美顶级模型：基准测试显示，DeepSeek V4 Pro与Claude Opus 4.6、GPT 5.4等顶尖闭源模型并驾齐驱，在部分编程任务上甚至超越Sonnet 4.5。在多智能体（Agent）任务和写代码方面，社区评价很高。
* 强大的1M超长上下文：这是DeepSeek V4的“杀手锏”之一，在处理超过3-4万token的超长代码重构时，优势非常明显，Agent场景下实用性极强。
* 兼具效力和经济性：很多人选择这个组合的原因是，DeepSeek V4-Flash被公认为当今世界上性价比最高的模型。就算用Pro版，百万token的输出成本也仅为Claude Sonnet 4.6的四分之一左右（约24块钱 vs 100块）。如此巨大的成本优势，让开发者工作时更有底气。

当然，也要提一下需要注意的地方：有用户发现，DeepSeek V4在承担高难度任务时，对Token的消耗可能会比较大。同时，它也和所有“换壳”方案一样，可能无法100%支持Claude的部分原生高级功能（如某些Artifact的渲染），实测中也偶尔会遇到一些因依赖1M上下文而生成的BUG。

总的来说，这个“外壳+内核”的想法，已经成为当前AI社区最热门、最现实的生产力实践之一。它可能预示着一个新时代的到来：未来的胜者不再是某个单一的“最强模型”，而是那个能让我们自由选择、无缝集成所有最强模型的“平台”本身。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/2dMzopbOicLibMplBZwCuQE2bMW3MP0GqZsRm1iaMYBL5dP8CfNuJwnEdFkXzbeJxcFJcPam8qQIv2TA6cCvLUMTA/0?wx_fmt=png)

白帽子

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2dMzopbOicLibMplBZwCuQE2bMW3MP0GqZsRm1iaMYBL5dP8CfNuJwnEdFkXzbeJxcFJcPam8qQIv2TA6cCvLUMTA/0?wx_fmt=png)

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