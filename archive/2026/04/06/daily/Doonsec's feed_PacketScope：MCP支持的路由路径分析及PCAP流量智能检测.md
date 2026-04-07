---
title: PacketScope：MCP支持的路由路径分析及PCAP流量智能检测
url: https://mp.weixin.qq.com/s/upfno1sO-xbNRAdAyz-G4w
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:27:58.925816
---

# PacketScope：MCP支持的路由路径分析及PCAP流量智能检测

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/iaJcPGD01bWXuTQHEuEHNsuDzFsYNVteewrDEb9ce3qCib2tORmkKe16KCKwhZTYWTVWFmBESvbgPEMd2xT5XUhiaXWwt55U5QQzNiaG3NQ7ZpY/0?wx_fmt=jpeg)

# PacketScope：MCP支持的路由路径分析及PCAP流量智能检测

赛博新经济
赛博新经济

赛博新经济

![]()

在小说阅读器中沉浸阅读

PacketScope是基于eBPF的端侧通用防御框架，通过在TCP/IP协议栈处理路径上动态观测、实时感知每一个分组单元在系统内的处理轨迹，绘制协议交互全景图，再辅助以大模型分析，PacketScope实现了协议栈内核级别的分组可视化、安全性分析与可编程防御。

项目介绍：🔗https://packetscope.net/

项目地址：🔗https://github.com/Internet-Architecture-and-Security/PacketScope

大家好啊！前期几篇推送，我们介绍了PacketScope开源项目。我们简要回顾一下，PacketScope由Analyzer、Tracer、Guarder三个模块构成，三者协同工作，共同构成了从观测、分析到实时防御的端到端协议栈安全防御体系。其中，Analyzer模块通过eBPF技术实时捕获协议栈中分组的处理路径，构建细粒度的协议交互全景图，实现协议栈行为的可视化与深度分析；Tracer模块对分组在互联网上的逐跳路径进行探测与标注，结合AS、地理位置及威胁情报数据，实现路由路径的可视化与风险分析；Guarder模块则借助大语言模型对实时流量进行长上下文语义推理，识别恶意行为并自动生成eBPF规则，通过XDP在协议栈内核层面实现零延迟的攻击拦截与动态防御。

**近期，我们对PacketScope进行了扩展开发，新增了2个功能：**

1．**重构Tracer模块：**支持ICMP/TCP的双协议路由路径探测，并集成MCP服务直接给OpenClaw智能体调用；

2．**扩展Guarder模块：**支持用户手动上传PCAP格式的流量分析，大模型分析后直接反馈用户流量分析检测结果。

**01**

面向OpenClaw的ICMP/TCP双协议路由路径分析

如前所述，PacketScope的Tracer模块专注于路由追踪与分析。端侧路由追踪从用户真实位置出发，能够绕过服务端无法触及的“最后一公里”网络及中间设备的权限限制，精准定位链路中的丢包、高延迟或路由绕行等故障。只有端侧发起的TCP/ICMP探测，才能真正还原业务访问的真实路径。这使得端侧路由追踪成为诊断边缘网络问题、优化CDN调度、验证安全策略有效性的关键手段，为提升终端用户体验提供了不可替代的数据基础。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaJcPGD01bWUNR6jLYdVshSpm4kxRpCC66AudZP2Y0QEZe4a4icLKyEF9zux5biaptvQlSmqniaKGkCD53h7TVWupLddMN9eblyFlITZbwmCTicc/640?wx_fmt=png)

图1 PacketScopeTracer模块

传统依赖ICMP或UDP的路由探测技术易受中间设备干扰——防火墙与网络设备常屏蔽ICMP回显请求或限制UDP端口，导致探测失败。为此，我们对Tracer模块进行了扩展，引入基于TCP协议的路由探测机制：向目标路径的每一跳发送TCP SYN报文，并指定常见Web端口（如80、443），通过逐跳增加TTL触发中间路由器返回ICMP超时消息。由于TCP的80端口承载HTTP业务，防火墙和路由器为保障Web连通性通常不会丢弃此类流量，因此TCP探测能够获得更贴近真实业务链路的路径与时延信息。重构后的/api/trace接口支持显式指定protocol=tcp与port参数，可灵活适配不同服务端口的探测需求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaJcPGD01bWV0FHYOfBjpYl1JRsHwRdCmjMIGomKiaQSTkgJPc4L7gUbdZ0k9SRTvclvoHZ1wb0m7XemPvHJMibrqTRE3cFhwibvdldRxxkds3A/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWW6jNmwhCVwK7tD6tKMflRpLjt1j7vfCzEjEPjjHhwOP7wsibWJGibstTibdRCPUzVL2tlwCwjl9viav4qiaQTAF20aPg0oYHEMH6GU/640?wx_fmt=png)

图2 图3 使用方式介绍

此外，我们扩展了Tracer模块，接入了OpenClaw（即“小龙虾”）。核心机制是将Tracer封装为MCP服务端，然后由OpenClaw作为MCP客户端进行动态配置与调用。

▶首先，Tracer后端启动FastMCP服务，监听指定的主机、端口和挂载路径，并通过@mcp.tool()装饰器暴露trace\_target、analyze\_target、get\_history等工具接口。

▶随后，用户在OpenClaw的配置界面中添加该MCP服务器的地址、传输协议（如SSE或streamable HTTP）及认证信息。

▶OpenClaw会自动拉取服务端的工具列表，并将这些工具注册到自身的智能体调度体系中。

▶完成配置后，用户可在飞书等对话软件中以自然语言方式向小龙虾发出指令（例如“追踪某个域名的路由”），小龙虾会解析意图并调用对应的Tracer MCP工具，最终将探测结果返回至对话界面，实现了 Tracer 服务对上层智能体应用的透明集成。

![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWXOuZibEW3wJDwe5ushh64Ioibhx6RcJGqZIS7mAbISUItXlb6CjiahrsoXVia3L9q0xyiamVU6H8icXia1ma4UtvAsVibLI4KluGgvmYo/640?wx_fmt=png)

图4 使用方式介绍

TCP追踪原理的核心在于规避网络设备对ICMP和UDP的封锁，利用TCP业务端口的宽松过滤策略获得更可靠的路由信息；而接入OpenClaw的过程则通过MCP协议的标准化工具发现与调用机制，将Tracer从单一HTTP接口升级为可被智能体直接调度的基础能力。两者结合不仅提升了探测的鲁棒性，也极大拓展了Tracer在自动化运维、安全分析及自然语言交互场景中的应用范围，体现了模块化重构带来的架构优势与生态兼容性。

![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWXC7MibF7fa29l6FSxXKulL8maDfoOvBtEbBfj4iaWCiafSlFJ8oKzQ5Xg6FlZIznNt03oUS8gticdxDv8FRwVjMOtpq6Zecv62HxE/640?wx_fmt=png)

图5 使用方式介绍

**02**

PCAP流量智能分析

PCAP文件的智能分析是Guarder模块新增的关键功能，它借助AI大模型将传统需要专业人员手动翻阅数万条数据包的抓包分析过程压缩至数秒，自动输出威胁识别、流量统计与安全建议，大幅降低分析门槛；该功能主要面向网络安全工程师、系统运维人员和安全分析师，可用于应急响应时快速定位攻击来源、日常巡检中排查流量异常、渗透测试后分析攻击路径，以及帮助不熟悉Wireshark的运维人员快速读懂抓包数据。

**PCAP智能分析的核心流程分为4个步骤：**

**（1）上传文件。**用户通过拖拽或点击选择方式上传.pcap或.pcapng格式的抓包文件。系统限制单文件不超过 32 MB，最多处理前 5000 个数据包（超出部分自动截断），以保证分析时效。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaJcPGD01bWVv6G0IITpRKTU4YZiaBgrb4wzNPXiaTpSTaNYeNkB0ofh0ATV15m5WbuBAK0kVJIxzWHnDbSG636cVyOuKSnRO0jzxHRLnhjZyQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWUjFotuD6ERFT4NiayXom9mAlaVkpf9B7ia8Ib29WsPZiaCIXYH8B1gwKP8icVTjDUm7ccoIrI6SafvxHKiaIFpRm8QoIUIffNC9Eib0/640?wx_fmt=png)

图6 图7 上传文件实例

**（2）选择分析策略。**系统提供多种预定义分析模式（如安全威胁识别、流量基线分析、攻击路径追踪等），用户也可选择“自定义”模式，输入自然语言Prompt来引导AI关注特定威胁类型（例如“重点识别DNS隧道行为”或“分析内网横向移动，关注SMB/RDP流量”）。

![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWWc6yuMTxUAqresursjWtMSvqvUg2HNO1yNwO55RrVibXjnu3WkeMzKkpTN25oCwl3NJdWuQSHVREURDWIN4ibNqhfGxv6OouQ2k/640?wx_fmt=png)

图8 选择分析策略实例

**（3）智能分析与检测。**点击“开始AI分析”后，系统依次执行：上传文件→AI 解析→生成报告，即界面进入分析状态，顶部进度条显示三个阶段。全程通常在10秒左右完成。AI模型解析数据包的头部信息、协议字段、流特征及常见攻击指纹等。

![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWXeMq7A97BlFmPYnIZSkK3Xd2o3tyuNC9H9ENM2YlNvZS3ez0v9WWW0gAJpHhmVia4ycMpB2euWTMpwOzgylLKpegUY2bQ3nPcI/640?wx_fmt=png)

图9 智能分析与检测实例

**（4）生成结构化报告。**分析完成后，结果面板包含四个标签页。分析摘要：自然语言概述流量特征、主要威胁及整体安全态势。威胁列表：结构化表格呈现每条威胁的源/目的IP、端口、协议、威胁等级及描述。流量统计：可视化展示总数据包数、总流量、持续时间、连接数；协议分布（TCP/UDP/IPv4等）；TCP Flags计数；Top 5源IP及端口（附流量进度条）。安全建议：AI 根据分析结果给出具体处置建议，如封锁 IP、配置访问控制、排查可疑主机等。

![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWXyQWxqxAUvGhRQ8acCxlaZ2T9RsUclK9RtZEm7Yw8BCsyRGTWoDODkKJk3OVcM5hrf987LiaAyhfT7lPuAUt3qOtXPFne3rEeI/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaJcPGD01bWXHaeSLpJnxCNibqjvyCsGicDKugzkScRMqVbNBnhsCzspta1Y29G15XXhNSrNYVVqtwNRwibmRZqYPCibFGUWpfghqnyADr8Vfpws/640?wx_fmt=png)

图10 图11 生成结构化报告实例

**03**

未来展望

PacketScope项目逐步揭开了端侧协议栈复杂交互的“黑盒”，推动终端安全**从隔离检测向智能化可编程防御演进。**

**【预告】PacketScope全新版本上线在即，两大升级抢先看！！！**

✅**智胜未来：**全面接入OpenClaw智能体，实现Analyzer、Tracer、Guarder的全模块智能化升级，构建端侧安全的一体化AI智能防御阵地。

✅**敏捷无界：**告别BCC依赖，架构更精简，完成轻量化转身。开放灵活接口和自定义编程接口，让精准监控与灵活调参触手可及，轻松覆盖多元化生态场景。

敬请关注！

我们期待与安全社区和互联网研究者一起携手交流，欢迎大家参与PacketScope研发讨论，共同构建端侧防御的安全基石。

P.S.大家在安装或使用的过程中有任何问题，欢迎在Issues里面提问留言。

▶项目介绍网站：https://packetscope.net

▶项目Github开源地址：https://github.com/Internet-Architecture-and-Security/PacketScope）

作者们将在第一时间回复解答。欢迎关注我们的PacketScope技术交流群（群已满200人，可扫描下面二维码加好友、邀请入群，也欢迎群内小伙伴邀请好友入群）！

![](https://mmbiz.qpic.cn/mmbiz_png/iaJcPGD01bWWd3aKVWMcjsQvgoJEP6PsIWibllGTvicJbic8YqtbjDTMVzSqma4s3WTQ7n25KO13iaEMxDngPJpW1ygNsHX55AUTPcFagfgYMOCw/640?wx_fmt=png)

**往期推荐:**

[PacketScope：端侧协议栈防御的“智能铠甲”](https://mp.weixin.qq.com/s?__biz=MzA3MTAwODc0NQ==&mid=2649891394&idx=1&sn=ee3f7dbf01cd349c0b64077647aa089a&scene=21#wechat_redirect)

[PacketScope之协议交互“透视镜”](https://mp.weixin.qq.com/s?__biz=MzA3MTAwODc0NQ==&mid=2649891429&idx=1&sn=b3baf94a79527d604c005e092c86e998&scene=21#wechat_redirect)

[张力拉满、丝滑对接：大模型LLM赋能eBPF重塑网络攻击防御新范式](https://mp.weixin.qq.com/s?__biz=MzA3MTAwODc0NQ==&mid=2649891429&idx=1&sn=b3baf94a79527d604c005e092c86e998&scene=21#wechat_redirect)

[PacketScope：端侧协议栈防御的“智能铠甲”](https://mp.weixin.qq.com/s?__biz=MzA3MTAwODc0NQ==&mid=2649891669&idx=1&sn=dae538ee5551947c3aa6ec31a0f5c230&scene=21#wechat_redirect)

预览时标签不可点

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