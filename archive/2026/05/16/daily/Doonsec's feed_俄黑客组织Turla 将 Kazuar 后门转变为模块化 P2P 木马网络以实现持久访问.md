---
title: 俄黑客组织Turla 将 Kazuar 后门转变为模块化 P2P 木马网络以实现持久访问
url: https://mp.weixin.qq.com/s/h671x3uIGVMoVIozCWrsoQ
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:47:09.637494
---

# 俄黑客组织Turla 将 Kazuar 后门转变为模块化 P2P 木马网络以实现持久访问

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PaFY6wibdwyKrtg6LYVksrhfqgJUxibZ9n7rncuBffnMIHUia3iccNPzmzLlUd1w2VK1bffjdW4nniaK4DIpicWXFeuTJVPS00ekvjGJSibYXw7zSU/0?wx_fmt=jpeg)

# 俄黑客组织Turla 将 Kazuar 后门转变为模块化 P2P 木马网络以实现持久访问

会杀毒的单反狗
会杀毒的单反狗

爱拍照的老李

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**导****读**

俄黑客组织 Turla 将其定制的后门 Kazuar 改造成了一个模块化的点对点 (P2P) 僵尸网络，该网络旨在隐蔽地持续访问受感染的主机。

根据美国网络安全和基础设施安全局 (CISA) 的评估，Turla 与俄罗斯联邦安全局 (FSB) 第 16 中心有关联。它与更广泛的网络安全社区追踪到的 ATG26、Blue Python、Iron Hunter、Pensive Ursa、Secret Blizzard（前身为 Krypton）、Snake、SUMMIT、Uroburos、Venomous Bear、Waterbug 和 WRAITH 等名称的活动存在重叠。

该黑客组织以攻击欧洲和中亚的政府、外交和国防部门而闻名，他们还攻击了 Aqua Blizzard（又名 Actinium 和 Gamaredon）之前入侵的终端， 以支持俄方战略目标。

微软威胁情报团队在周四发布的一份报告中指出： “此次升级符合 Secret Blizzard 的更广泛目标，即获取系统长期访问权限以收集情报。 虽然许多威胁组织依赖于越来越多地使用原生工具（即“借用系统资源”二进制文件 (LOLBins)）来逃避检测，但 Kazuar 向模块化僵尸网络的演进凸显了 Secret Blizzard 如何将弹性和隐蔽性直接融入到他们的工具中。”

Turla 的一项关键工具是 Kazuar ，这是一个 复杂的 .NET 后门程序 ，自 2017 年以来一直被持续使用。微软的最新研究成果显示，Kazuar 已从一个“单体”框架演变为一个模块化的机器人生态系统，该系统包含三种不同的组件类型，每种组件都有其明确定义的角色。这些变化实现了灵活的配置，减少了可观测的资源占用，并有助于执行广泛的任务。

已发现，传播该恶意软件的攻击依赖于 Pelmeni 和 ShadowLoader 等投放器来解密和启动模块。构成 Kazuar 架构基础的三种模块类型如下：

* 内核：作为僵尸网络的中央协调器，向工作模块发出任务，管理与桥接模块的通信，维护操作日志和收集的数据，执行反分析和沙箱检查，并通过配置设置环境，该配置指定与命令和控制 (C2) 通信、数据外泄时间、任务管理、文件扫描和收集以及监控相关的各种参数。
* Bridge：充当领导者内核模块和 C2 服务器之间的代理。
* Worker：会记录击键、挂钩 Windows 事件、跟踪任务，并收集系统信息、文件列表和消息应用程序编程接口 ( MAPI ) 详细信息。

内核模块类型公开了三种内部通信机制（通过 Windows 消息传递、邮件槽和命名管道）以及三种不同的与攻击者控制的基础架构通信的方法（通过 Exchange Web 服务、HTTP 和 WebSocket）。该组件还会“选举”一个内核领导者，代表其他内核模块与桥接模块通信。

微软解释说：“选举通过邮件槽进行，领导者的选出依据是工作量（内核模块的运行时间）除以中断次数（重启、注销、进程终止）。一旦领导者当选，它就会宣布自己是领导者，并通知所有其他内核模块将状态设置为静默（SILENT）。只有当选的领导者不会处于静默状态，这使得领导者内核模块能够记录活动并通过桥接模块请求任务。”

该模块的另一个功能是启动各种线程，在内核模块之间建立命名管道通道，以进行内核间通信，指定外部通信方法，以及通过 Windows 消息传递或邮件槽促进内核到工作节点和内核到桥接节点的通信。

内核的最终目标是从C2服务器轮询新任务，解析传入的消息，将任务分配给工作节点，更新配置，并将任务结果发送回服务器。此外，该模块还包含一个任务处理器，用于处理内核领导者发出的命令。

Worker 模块收集的数据随后会被聚合、加密，并写入恶意软件的工作目录，然后从该目录泄露到 C2 服务器。

微软表示：“Kazuar 使用一个专用的工作目录作为集中式的磁盘暂存区，以支持其跨模块的内部操作。该目录通过配置定义，并始终使用完全限定路径进行引用，以避免在不同的执行上下文中出现歧义。”

在工作目录中，Kazuar 按功能组织数据，将任务、收集输出、日志和配置资料隔离到不同的位置。这种设计使恶意软件能够将任务执行与数据存储和泄露解耦，在重启后保持运行状态，并在模块之间协调异步活动，同时最大限度地减少与外部基础设施的直接交互。

技术报告：

《Kazuar：国家级僵尸网络的剖析》

https://www.microsoft.com/en-us/security/blog/2026/05/14/kazuar-anatomy-of-a-nation-state-botnet/

新闻链接：

https://thehackernews.com/2026/05/turla-turns-kazuar-backdoor-into.html

**![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGC3gsJClsh4Fia0icylyBEnBywibdbkrLLzmpibfdnf5wNYzEUq2GpzfedMKUjlLJQ4uwxAFWLzHhPFQ/640?wx_fmt=jpeg)**

扫码关注

军哥网络安全读报

**讲述普通人能听懂的安全故事**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz/AnRWZJZfVaF2RjjiaFU5rh9gjoyybDu9EvVnCYlqGSXDTZyuDbPbic33rGMe0dfB3HAicVkh6kdgo7T3OAOGwOtYw/0?wx_fmt=png)

爱拍照的老李

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

![作者头像](http://mmbiz.qpic.cn/mmbiz/AnRWZJZfVaF2RjjiaFU5rh9gjoyybDu9EvVnCYlqGSXDTZyuDbPbic33rGMe0dfB3HAicVkh6kdgo7T3OAOGwOtYw/0?wx_fmt=png)

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