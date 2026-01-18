---
title: PacketScope：LLM赋能的协议栈交互行为智能分析
url: https://mp.weixin.qq.com/s/q6rorlNj-SES1rG4eNpncg
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:35:56.039664
---

# PacketScope：LLM赋能的协议栈交互行为智能分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibNQ9fXTAVian8OJ2MqicmPjhUeB8vGIzovQyFhS332XeGeMvokfVHqeGWnAFf3SblAZViat3OHrSIsFwYbCpcae9A/0?wx_fmt=jpeg)

# PacketScope：LLM赋能的协议栈交互行为智能分析

原创

赛博新经济
赛博新经济

赛博新经济

![]()

在小说阅读器中沉浸阅读

PacketScope是一种基于eBPF的TCP/IP协议栈通用防御框架。通过在协议栈处理路径上动态观测、实时感知每一个分组单元在系统内的处理轨迹，绘制协议交互全景图，再辅助以大模型分析，PacketScope实现了协议栈内核级别的分组可视化、安全性分析与零延迟防御。

项目介绍：🔗

https://internet-architecture-and-security.github.io/packetScope-website/

项目地址：🔗

https://github.com/Internet-Architecture-and-Security/PacketScope

大家好啊！前期几篇推送，我们介绍了PacketScope开源项目。我们简要回顾一下，PacketScope由Analyzer、Tracer、Guarder三个模块构成，三者协同工作，共同构成了从观测、分析到实时防御的端到端协议栈安全防御体系。其中，Analyzer模块通过eBPF技术实时捕获协议栈中分组的处理路径，构建细粒度的协议交互全景图，实现协议栈行为的可视化与深度分析；Tracer模块对分组在互联网上的逐跳路径进行探测与标注，结合AS、地理位置及威胁情报数据，实现路由路径的可视化与风险分析；Guarder模块则借助大语言模型对实时流量进行长上下文语义推理，识别恶意行为并自动生成eBPF规则，通过XDP在协议栈内核层面实现零延迟的攻击拦截与动态防御。

![](https://mmbiz.qpic.cn/mmbiz_png/ibNQ9fXTAVian8OJ2MqicmPjhUeB8vGIzovGGJW03xvkIgeRh76esDEuaZ80TichKx4M5JgyLvtykWv4AxL52XyROg/640?wx_fmt=png&from=appmsg)

图1 PacketScope总体结构图

今天我们为大家介绍一下PacketScope项目的协议交互智能分析功能，即利用大模型对PacketScope构建的协议交互全景图进行智能分析与调试，从而自动识别协议栈的性能瓶颈与潜在攻击，为网络性能优化和入侵检测等提供支持依据。

**01**

协议交互全景图的语义扩展与下载

当前，互联网上每天吞吐的数据量已超108TB，这些数据的传输依赖于底层网络协议的交互。协议交互如同网络空间中纵横交错的“高速公路网”（如图1所示），为海量数据的流动提供路径与通道。你是否也曾好奇：我们能否直观感知这张协议交互的“高速公路网”究竟是何模样？其中是否存在堵塞或低效的路径？又有哪些路段可以被优化与修整？PacketScope的协议交互全景图分析功能，正是为解决这一问题而生。

在前面的推送中我们介绍过，协议交互全景图是PacketScope的Analyzer功能基于eBPF技术实现的可视化轨迹图，它通过对网络协议栈中的活跃套接字与数据包进行实时监控，完整捕获数据包在内核协议栈中的处理路径，记录其每一步的处理动作、状态变更及上下文依赖关系，从而清晰、细粒度地呈现底层协议栈中每一次分组流动、每一个协议调用以及每一条跨层依赖关系，最终构建出协议栈底层处理的完整轨迹图，为网络性能分析与调优、攻击检测等提供支撑依赖（详见推送“PacketScope之协议交互‘透视镜’”）。

![](https://mmbiz.qpic.cn/mmbiz_png/ibNQ9fXTAVian8OJ2MqicmPjhUeB8vGIzovkLuIYHKjQq4SR8a0Kfch5VGb11lhmOibuxWqr69VyqAQCKkGm6zfn7A/640?wx_fmt=png)

图2 网络空间中的复杂协议交互（注：该图由AI生成）

近期，我们对PacketScope的协议交互分析功能进行了扩展和改进，新增了协议交互图JSON格式数据下载功能，用于将内核/应用函数调用关系结构化输出，进而可以支持大模型开展性能分析与安全分析。

![](https://mmbiz.qpic.cn/mmbiz_png/ibNQ9fXTAVian8OJ2MqicmPjhUeB8vGIzovaSqqcyibaMWzUwo3QLZz2bkzt2D124R0tCicjHAZiblEAyqkEnEboqbvw/640?wx_fmt=png)

图3 协议交互图的下载

进入PacketScope的【函数调用链监控器】，如图2所示在函数调用链拓扑图页面中可以看到【下载拓扑数据】按钮。用户点击后即可下载当前页面对应的函数调用链拓扑图数据。下载的JSON数据经过专门的结构化与语义化处理，能够更好地被大模型理解和解析。

* **JSON 数据结构说明**

导出的JSON主要包含以下两部分：

▶ graphNodes：函数节点信息，描述每个函数的基本属性及性能指标，包括：

* 函数唯一标识（id）
* 函数名（name）
* 所属阶段/类别（category，如接收、处理、发送）
* 调用地址（addr）
* 调用次数（callCount）
* 总耗时、平均耗时、最小/最大耗时
* 采样耗时列表

面向大模型的自然语言描述（description）

▶ graphLinks：描述函数之间的调用链路，包括：

* 调用源与目标函数
* 调用方向
* 调用次数及权重
* 归一化权重
* 面向大模型理解的调用关系描述

示例结构如下：

![](https://mmbiz.qpic.cn/mmbiz_png/ibNQ9fXTAVian8OJ2MqicmPjhUeB8vGIzov2c83jHsvgx64YUeuP5QPSvMwHfvaynYjdVU9o8eEhUP3DIoFwdibgfQ/640?wx_fmt=png)

**02**

协议交互全景图的大模型分析

用户点击下载某个网络流的协议交互全景图到本地后，可以将该JSON格式的交互图上传到大模型LLM，辅助以提示词，利用大模型的长上下文推理能力来分析该协议交互全景图，例如包括：

1. 请对该协议交互图进行整体评估分析；
2. 该协议交互图中是否存在瓶颈路径，可修复优化网络传输性能；
3. 交互图中是否存在异常，甚至网络攻击引起的恶意交互行为等。

![](https://mmbiz.qpic.cn/mmbiz_png/ibNQ9fXTAVian8OJ2MqicmPjhUeB8vGIzovU5AvaE74j6ugUFiaTziadVOz02L12ibjkOX5oKz88UMamv0lO1JibAoJbQ/640?wx_fmt=png)

图4 DeepSeek分析协议交互图结果

如图3所示，DeepSeek等大模型对交互图分析完毕后，会给出直观的结论报告，可以作为管理员、协议栈开发者、安全人员决策的关键依据。

**03**

未来展望

PacketScope项目逐步揭开了端侧协议栈复杂交互的“黑盒”，推动终端安全从隔离检测向内部认知与智能化防御演进。

在后续版本中，我们将扩展PacketScope，原生支持MCP（Model Context Protocol）协议，使得PacketScope可直接通过MCP与大模型客户端对接，从而支持PacketScope三个功能模块的MCP Server大模型调用，成为终端的智能网络操作手。例如，可以直接实现协议交互图数据到大模型的回传，在线分析推理终端的协议交互行为，无需再手动下载JSON文件上传到大模型；分析完毕后，远程下载eBPF规则到终端执行，阻断攻击等。从而实现真正的从感知、到决策、再到阻断的一体化智能防御体系；

此外，PacketScope项目将进行轻量化改造升级，开放更为灵活的编程接口便于专业人员自定义函数观测点及监控调参，扩展支持更广泛的生态版本等，敬请关注！

我们期待与安全社区和互联网研究者一起携手交流，共同打造面向未来的协议栈安全基石。

**P.S.**大家在安装或使用的过程中有任何问题，欢迎在Issues里面提问留言。

项目介绍网站：https://internet-architecture-and-security.github.io/packetScope-website/

项目Github开源地址：https://github.com/Internet-Architecture-and-Security/PacketScope

作者们将在第一时间回复解答。欢迎关注我们的PacketScope技术交流群（由于群已满200人，二维码失效，欢迎群内的小伙伴邀请好友入群）！

下面是利用NotebookLM为PacketScope生成的介绍视频：

**往期推荐:**

[PacketScope：端侧协议栈防御的“智能铠甲”](https://mp.weixin.qq.com/s?__biz=MzA3MTAwODc0NQ==&mid=2649891394&idx=1&sn=ee3f7dbf01cd349c0b64077647aa089a&scene=21#wechat_redirect)

[PacketScope之协议交互“透视镜”](https://mp.weixin.qq.com/s?__biz=MzA3MTAwODc0NQ==&mid=2649891429&idx=1&sn=b3baf94a79527d604c005e092c86e998&scene=21#wechat_redirect)

[张力拉满、丝滑对接：大模型LLM赋能eBPF重塑网络攻击防御新范式](https://mp.weixin.qq.com/s?__biz=MzA3MTAwODc0NQ==&mid=2649891564&idx=1&sn=77e5f6945dfbcd5f6b4e29ebae5bbfae&scene=21#wechat_redirect)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ibNQ9fXTAVianBKqe9LBRDkFTe4vrBHA8VVOcs0wauglpkBn55FibV2m5bZBmgkLTFrNzLQ93ELgWjYuhFv2WDIdA/0?wx_fmt=png)

赛博新经济

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ibNQ9fXTAVianBKqe9LBRDkFTe4vrBHA8VVOcs0wauglpkBn55FibV2m5bZBmgkLTFrNzLQ93ELgWjYuhFv2WDIdA/0?wx_fmt=png)

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