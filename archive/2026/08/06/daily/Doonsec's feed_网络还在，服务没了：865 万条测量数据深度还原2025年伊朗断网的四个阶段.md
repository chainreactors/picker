---
title: 网络还在，服务没了：865 万条测量数据深度还原2025年伊朗断网的四个阶段
url: https://mp.weixin.qq.com/s/Q-WVIA22Z9ihp8qQK6EEWg
source: Doonsec's feed
date: 2026-08-06
fetch_date: 2026-08-07T04:22:50.011317
---

# 网络还在，服务没了：865 万条测量数据深度还原2025年伊朗断网的四个阶段

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/cLf3QJbZL4CeMOEfia22SI6ZuC5iaqXMy94nzpibvlq1v0EoVqI7frnib6Gbh3sAW36rbhuHXMQg74Vso0PYbJwIGGYMdX9lWCsRmFjHNKgSzXA/0?wx_fmt=jpeg)

# 网络还在，服务没了：865 万条测量数据深度还原2025年伊朗断网的四个阶段

NISL实验室
NISL实验室

NISL实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

今日，国际互联网协会（Internet Society, ISOC）在其官方网站发布了清华大学网络与系统安全研究室、中关村实验室与奇安信 XLab的联合研究成果。该成果是研究团队围绕**伊朗2025年6月大规模断网事件**开展的深度归因分析。***不同于传统意义上依赖路由回撤的大规模互联网中断事件，研究团队通过对此次事件的系统测量与分析***，系统性地证实了伊朗已具备面向网络服务级别的精细化管控能力。相关学术研究成果已发表于国际交叉领域顶会WWW 2026。

传统断网监测看到的是“网络还在不在”，但网络存活不代表其运行的服务真实可用。本文在此基础上追问“网络里的服务还能不能用”。通过对 865 万条主动测量结果进行服务级分析，本文提出一套面向服务层的断网监测框架，并基于该框架细致刻画了伊朗断网行动由局部试探、全国封锁到分级恢复的全过程。这次断网具有三个典型特征：分阶段（phased）、渐进式（progressive）和分布式（distributed）。

![](https://mmbiz.qpic.cn/mmbiz_png/cLf3QJbZL4CddtvHY6vlMIK80f0UY1f7E0uhHbJnjGApxMOuiahRx3wRIS5iaLklCib1MhCbAoGXKichiaBciaFtQVZOzfs7DLhZAOh87GrciceYpM/640?wx_fmt=png&from=appmsg)

原文标题：Characterizing Iran’s Phased National Internet Shutdown in 2025: A Progressive and Distributed Action

原文作者：Shibo Cui, Mingxuan Liu, Baojun Liu, Haixin Duan, Ruixuan Li, Chaoyi Lu, Jin Zhang, Zhicheng Wang, Jinghua Bai

原文链接：https://dl.acm.org/doi/10.1145/3774904.3792699

发表会议：The ACM Web Conference 2026（WWW 2026）

ISOC 博客链接：https://pulse.internetsociety.org/en/blog/2026/08/when-networks-stay-up-but-services-disappear/

**1、当“在线”不再等于“可用”**

一次全国性断网，通常会留下很直观的技术痕迹：BGP 路由被大规模撤回、网络前缀从全球路由表中消失，或者跨境流量突然跌至低谷。但 2025 年 6 月发生在伊朗的事件呈现出一种更隐蔽的模式：***许多网络仍然可以在全球路由系统中被看见，IP 地址也未必完全失去响应，然而其中承载的 DNS、Web、邮件和 VPN 等服务，却从境外逐步变得不可达。***

这意味着，仅凭“路由是否存在”或“主机能否被 ping 通”来判断网络状态，可能会把一场大规模服务封锁误判为网络仍然正常。论文将这种现象称为**服务级断网（service‑level shutdown）**：BGP层面的基础网络表面上仍然保持互联，然而真正影响用户体验和信息流通的服务层却被有选择地限制。

**2、从海量测量中捕捉服务“失活”**

研究团队构建了一套面向服务层的断网监测框架。数据采集端依托 400 余个分布式测量节点，对伊朗全部可路由 IPv4 地址空间中的公开服务进行持续主动探测，覆盖 HTTP、SSH、DNS、SNMP 等多类协议，共获得 865 万条测量结果。

随后，监测框架让每个网络服务**在短时间窗口都形成具有代表性的随机样本**。系统将 IP 与端口对加入随机化测量队列，分散探测顺序带来的时间偏差；随后按 10 分钟粒度汇总服务状态，把探测到的活跃服务数量作为整体网络服务活性的代理指标。

![](https://mmbiz.qpic.cn/mmbiz_png/cLf3QJbZL4CibSHJ36aA1uJRZuCMhX08CdZjDAZSVfkK4wNGwJabOjYCKBAQAba3wcb8mdJPnZ30hLbj8J9Yic2LUEtfI3MXDIh5j0Yp6SxlE/640?wx_fmt=png&from=appmsg)

图1: 服务级断网监测核心思路：让每个短时间窗口都形成具有代表性的随机样本

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cLf3QJbZL4BmMVrD5QCcOHT6TpGh2LLFYUbfw6AiaT4vUcyqiaPdddMIQ9ff8E48VOPzcU6D2syv6Croho3ZQUSNwdFibR6LicfUac08YcPaqXE/640?wx_fmt=png&from=appmsg)

图2: 服务级断网监测框架：随机化主动测量、动态基线与异常下降检测（来源：论文 Figure 1）

为了区分正常波动和人为封锁，研究使用自适应滑动窗口建立动态基线：窗口保留最近三天的健康观测，并自动排除已被判定为断网阶段的数据，避免异常值反过来“污染”基线。当当前活跃服务量相对基线的下降超过统计阈值时，系统将该时间段标记为断网。论文用服务阻断率（Service Blocked Ratio，SBR）量化下降幅度。

**框架设计特点**：随机抽样解决“服务空间太大、无法短时遍历”的问题；动态基线解决“昼夜变化和日常波动”的问题；服务阻断率则把不同阶段、不同 AS 和不同协议放到同一尺度上比较。

**3、断网并非一次“拉闸”，而是四个阶段**

系统监测结果显示，这次行动并非在某个时刻一次性关闭全国网络，而是经历了两个局部演练（LSD, Localized Shutdown Drill）、一次全国封锁（NS, Nationwide Shutdown）和一次分级恢复（NSR, Nationwide Shutdown Recovery）。四个阶段共同组成了一条清晰的断网时间线。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cLf3QJbZL4DuAIBFoeicsjQhibaiaeCGfRdDUZOFTicJWCs6cNx50IOc5Duvu5UPSIzf6vmqsLYbiaVu2GKdP24yUoJPWhTWQlibJrgtt7iaibYwqb0/640?wx_fmt=png&from=appmsg)

图3: 伊朗 2025 年 6 月服务活性与四阶段断网时间线（来源：论文 Figure 2）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cLf3QJbZL4CGRETC7U4xT5zNvtNeCiaOTaK0c0lNUTmEmnyKeyQ1jPAQZlZvp2xD5iacjV8Txo09Ws3N4Ug4wM2ERN7OvWshsd1LwKSMEw7GI/640?wx_fmt=png&from=appmsg)

图4: 断网自基础设施及隧道服务向应用服务的扩张（颜色越深代表受阻断越严重）

**阶段一｜局部试探：先触及基础设施与隧道服务**
6 月 13 日开始的第一阶段持续约 30 小时，影响 36 个头部 AS，重点落在 DNS、NTP 以及 L2TP、IKEv2 等核心基础设施和隧道协议上。其目标更像是控制解析、时间同步与网络连通通道。

**阶段二｜范围扩张：从底层设施走向应用服务**
6 月 17 日的第二阶段影响扩大到 60 个头部 AS；受影响的头部服务由 12 类增至 36 类，Web、邮件、文件传输和共享服务开始大面积受限。封锁从“基础设施控制”转向“信息获取与交换阻断”。

**阶段三｜全国封锁：98 个头部 AS、49 类服务受影响**
6 月 18 日进入全国封锁阶段。伊朗头部 100 个 AS 中有 98 个受到影响，头部 50 类服务中有 49 类被阻断，服务活性几乎跌至低点。这一阶段展示了由局部控制快速升级为全国性服务封锁的能力。

**阶段四｜分级恢复：网络回来，但并不同步**
6 月 21 日后网络进入恢复阶段，但恢复并不是简单地恢复原状：不同 AS、不同服务以不同速度回归。到该阶段末，头部 100 个 AS 中只有 30 个恢复正常，9 个部分恢复，仍有 61 个继续受影响；50 类头部服务中，16 类恢复、15 类部分恢复、19 类仍被阻断。

**4、渐进式升级：封锁范围逐渐扩张**

本次断网是渐进式的，体现在两个维度：一是受影响网络从少数 AS 扩张到几乎所有头部 AS；二是受影响服务从底层基础设施和隧道协议扩展到 Web、邮件、文件传输等用户可感知的应用服务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cLf3QJbZL4A4Y9kyokA2micpHLLicsfxmzal2TH5MtNw8W3QSu6B53LtVvo0zRS2eFMwdXPfWg6rCNJtb5HUCqjNFUabmSMiaaqtiagPlMDgUf0/640?wx_fmt=png&from=appmsg)

图5: 头部 100 个 AS 在四个阶段中的状态迁移（来源：论文 Figure 3）

![](https://mmbiz.qpic.cn/mmbiz_png/cLf3QJbZL4BwI7KjsM65g0cpLjljIeSlthN8bT8AS0X6ezvEJQ2g02fpDU0T838dFj3BTgsiaicvpwoQNceFvYCbR0O3yD6APOMW4t0TPbaN0/640?wx_fmt=png&from=appmsg)

图6: 头部 50 类网络服务在四个阶段中的状态迁移（来源：论文 Figure 4）

两张状态迁移图进一步说明：封锁与恢复都不是均匀发生的。此前未受影响的网络或服务会在下一阶段被纳入；进入恢复期后，又被拆分成“完全恢复、部分恢复、仍受影响”等不同状态。整个行动不是单一开关，而是一套可以细粒度调节对象和强度的控制流程。

**5、分布式执行：不同 AS 有不同“断网时钟”**

进一步比较不同自治系统（AS）的阻断时间和恢复轨迹，发现显著的跨 AS 异质性：有些网络在全国封锁开始数小时后才完全失去服务；另一些网络在恢复期反复波动，呈现不稳定的局部回归。即便处于同一全国性事件中，不同网络的执行强度、启动时刻和恢复速度也并不一致。

这种差异表明，封锁很可能并非完全依赖一个中央设备同步完成，而是由分布在多个运营商、网络节点或管理域中的机制共同执行。

![](https://mmbiz.qpic.cn/mmbiz_png/cLf3QJbZL4C1BbQZARYJTYicBtgDNFBJSQYbpPqSrKdiaF7sWMdw9vtM1EfAzuNE4RZWRoicNIycH62ficLcbPQJA2ialvSIvewuGXXJfE01UHrI/640?wx_fmt=png&from=appmsg)

图7: 恢复阶段不同 AS 的服务阻断率仍呈现显著差异（来源：论文 Figure 6）

**6、开展服务级互联网中断测量的意义**

**补充传统路由与流量监测的盲区**

BGP 路由、IP 可达性和宏观流量仍然是断网监测的重要信号，但它们分别回答的是“网络是否被宣告”“主机是否响应”和“总体通信量是否变化”。服务级测量补充了更贴近真实使用的问题，即用户所依赖的具体服务是否还能从外部真实访问。

**揭示更细粒度的断网态势**

从 DNS、VPN 到 Web、邮件，再到分级恢复，受影响对象的变化说明网络控制可以按协议、运营商和时间阶段精细实施。对研究人员、网络运营者和分析者而言，仅用“全国断网/没有断网”的二元标签已经不足以描述断网的现实态势。

**结语：看得见网络，并不等于看得见真实连接**

伊朗 2025 年 6 月的断网行动说明，互联网控制正在从粗粒度的“切断网络”，走向更隐蔽、更细致的“选择性关闭服务”。当路由仍在、地址仍可见时，依赖传统指标的监测系统可能认为网络仍然在线；而对用户来说，无法访问网页、无法收发邮件，已经意味着服务事实上的消失。

本文以 865 万条主动测量结果为基础，把一次复杂的国家级断网拆解成可观察、可量化的四个阶段，也提醒互联网测量社区：**理解网络韧性，不仅要追踪线路、路由和地址活跃性，更要持续观察线路之上真正承载信息流动的服务。**

**作者简介**

**崔世博**，清华大学网络科学与网络空间研究院博士研究生，导师为刘保君副教授。主要研究方向为互联网中断监测、定位与根因分析。在国际网络及安全顶级会议NDSS、WWW等发表论文。联系邮箱：csb24@mails.tsinghua.edu.cn。

**刘明烜**，中关村实验室副研究员。科研方向聚焦于数据驱动的网络空间安全研究。在国际网络及安全领域国际顶级会议和期刊上发表20余篇论文（含网络空间安全四大领域顶会论文10余篇），曾获得NDSS 26的最佳论文奖（Distinguished Paper）以及Ethics22的最佳学生论文奖（Best Student Paper），研究成果推进一项IETF标准草案。联系邮箱：liumx@zgclab.edu.cn。

**参考文献**

[1] Lin Quan, John Heidemann, and Yuri Pradkin. 2013. **Trinocular: Understanding Internet Reliability through Adaptive Probing.** Proceedings of the ACM SIGCOMM 2013 Conference on SIGCOMM, 255–266.

[2] Guillermo Baltra and John Heidemann. 2020. **Improving Coverage of Internet Outage Detection in Sparse Blocks.** International Conference on Passive and Active Network Measurement, 19–36.

[3] Philipp Richter, Ramakrishna Padmanabhan, Neil Spring, Arthur Berger, and David Clark. 2018. **Advancing the Art of Internet Edge Outage Detection.** Proceedings of the Internet Measurement Conference 2018, 350–363.

文案：崔世博，刘明烜，刘保君

排版：周航

审核：张一铭

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDychicnjsOmb4zS0VAMiaySibTJfuphCbswGUOqGnMKPaBSXNvYmEfvllcEiaNMH5GSmz0v0LicdGAsI4Fib1g/0?wx_fmt=png)

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