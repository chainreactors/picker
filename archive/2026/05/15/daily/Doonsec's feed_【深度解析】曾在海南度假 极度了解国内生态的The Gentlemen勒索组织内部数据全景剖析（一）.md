---
title: 【深度解析】曾在海南度假 极度了解国内生态的The Gentlemen勒索组织内部数据全景剖析（一）
url: https://mp.weixin.qq.com/s/Htq3D6Gr2n-4Bb7emlYXgw
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:10:45.741092
---

# 【深度解析】曾在海南度假 极度了解国内生态的The Gentlemen勒索组织内部数据全景剖析（一）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/887OLfia3YQbVUdc7yicsib3AOmhibbeaPr5ibQExyHm2J7mjxSAOn6GCzibRf6LxpcBZofotbuiaXQKtU9FnKZn8qz1W7wk8GpXIqh5lJDRo9cZ2M/0?wx_fmt=jpeg)

# 【深度解析】曾在海南度假 极度了解国内生态的The Gentlemen勒索组织内部数据全景剖析（一）

原创

Moir、州弟
Moir、州弟

solar应急响应团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/DxUXemrrntp3gibjPSCHmSEpdPDqfBcXT5e151v5AJSbV5JtaALLzQe0I1Jibbet7rTia8icjmgo5r4hpY3IMpYPIw/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

依托 **Solar 安全运营响应团队**的日常实战沉淀，我们会定期分享在安全运营中处置的典型应急响应事件，涵盖**银狐木马、APT 攻击、勒索病毒**等各类主流威胁。

作为专业的应急响应中心，Solar 致力于为复杂多变的安全事件提供从深度溯源到闭环处置的全流程支持。针对银狐、APT 等具有高隐蔽性的威胁，我们不仅聚焦于对其攻击行为的深度剖析，更致力于还原其完整的活动链路，并同步输出切实可行的**清除闭环操作方案**。

**突发危机干预通道：**若您的核心资产正面临加密锁定或数据勒索风险，请通过文末二维码联系我们。我们提供全天候紧急介入服务，协助您快速切断攻击链路，全力挽回业务损失。

### 内部聊天记录意外泄露的始末

在切入本次技术复盘之前，我们先理清一下数据来源的时间线。

2026年5月初，暗网常用的托管服务商 4VPS 遭到未知攻击。虽然其官方声称核心基础设施未受影响，但在几天后的 5月4日，知名网络犯罪论坛 Breached 上便出现了一个引发圈内广泛关注的帖子。一名代号为“n345”的用户，公开挂出了一份标价 10,000 美元的内部数据售卖帖。

而这份数据的主体，正是近期在亚太地区极其活跃的 **“The Gentlemen”** 勒索组织。随后，该发帖人直接通过网盘放出了这批数据的免费下载链接。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQaBaPBRyS13LJUzHFpuGjwBNuN1xmD5hsgtrgd4086vf83maxaYP6NJ0LRSms6G6F2o6hmbF1dcg6QrY1mmc4KSUQx2ClYLOok/640?wx_fmt=png&from=appmsg)

暗网论坛 Breached 上的发帖截图

通过论坛截图可以看到，发帖人直接附带了网盘链接。我们团队在获取到这份名为 `8990.zip` 的离线数据包后，对其进行了初步解包提取。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQYmuITibg6ylnDBFb4ZTcBICLpPonFbzNW4LWoJu05fw77OeDu55zckymusJSc2lF6BFYIDibLsZgKqJ9UklMbic6jS57PDV3gxhg/640?wx_fmt=png&from=appmsg)

被泄露的“8990.zip”压缩包解压后的文件结构截图

正如上图所示，压缩包内并非普通的文本，而是包含了大量以数字命名的文件夹，提取出了多达 3733 行的团队内部原生俄语聊天记录，以及 312 张带有极高情报价值的后台渗透截图（其中甚至包含类似左下角的 Vcenter 网络配置界面，暗示其已深扎某些目标的核心虚拟化设施）。

这种直接获取勒索组织内部原始沟通记录的机会非常难得。在获取客户正式授权的情报研究范围内，Solar 应急响应团队的安全专家决定转换视角，从这批泄露的日志入手，直接从攻击者的“第一视角”去审视他们的日常运作、目标挑选逻辑以及渗透手法。

### 目标明确的勒索商业版图

在进入繁杂的渗透细节前，我们需要先给这个组织简单画个像。

The Gentlemen 勒索软件组织于 2025 年 7 月首次出现，从其暴露出的运作痕迹来看，他们采用的是非常成熟的勒索软件即服务（RaaS）模式。

![img](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQbib0cnVoen3AI1OOqmk9lnodjxibCLLItBHB89OfibVMQbMSVflWtuCtOp0zNOJCkCEFjvULOXmRyOr6nVg7AI7QcxbEhYxrBoBw/640?wx_fmt=png&from=appmsg)

The Gentlemen 核心成员在暗网的 RaaS 招募广告贴

在这份被泄露的内部招募贴中，核心成员 Zeta88 明确给出了极具诱惑力的分成模式（90% 的收益归属渗透者），并在下方详细罗列了他们自研加密器（Locker）的技术特性。比如采用 Go 语言编写、支持 XChaCha20 异步加密、跨平台（支持 Windows、Linux、NAS 等），并且自带自动绕过特定程序等免杀机制。

在攻击目标的挑选上，该组织具有极强的高级目标导向特征。

![](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQbhVL6rMY0yFl4EXGJSmr8ILxJjQ1VjmpsccibzSsBhzzP140Drbl7FBga5Ns5lngLUFHZBPuO9fVnicUmicBiapYTSXSfHK1OyshQ/640?wx_fmt=png&from=appmsg)

The Gentlemen 目标行业与地区分布统计图(数据来源 solar勒索家族情报平台)

结合外部的行业统计图表与我们此次复盘发现的名单，他们将制造业、医疗保健和金融保险业作为首要打击目标，并且在亚太地区（尤其是中国、泰国及南美地区）的攻击占比极高。这种专门挑软肋捏的打法，给国内的很多大型代工企业和出海企业带来了极大的安全压力。

### 从第一视角还原渗透链路

为了真实还原攻击链路，我们将这三千多行聊天记录与相关的截图进行了结构化的翻译与交叉比对。梳理完我们会发现，他们的渗透思路并不像影视剧里那样神秘，反而与很多贴近实战的红队打法如出一辙。

#### 务实的目标筛选逻辑

在代号为 `100256` 的沟通频道中，核心成员 zeta88 和 qbit 详细展示了他们是如何筛选攻击对象的。

![img](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQYVVPIXWczUrSHxyEeUpkCymOVr3GDXxQbFmGt64QpJj9fkOMqqujSWdZO1EKNI3FbicVQ8m49S8IwzUccFpqJWlUdMhZOajNWo/640?wx_fmt=png&from=appmsg)

攻击者利用 ZoomInfo 评估企业营收并筛选目标的内部聊天

从上图的聊天记录中可以看出，他们高度依赖商业情报平台（如 ZoomInfo）来预估目标公司的年营收。如果一家企业的营收体量不够，他们通常会直接跳过。

更值得注意的是他们对技术入口的筛选标准。在批量资产测绘的基础上，他们并不盲目攻击，而是重点排查那些配置了 FortiGate 防火墙、且**启用了 LDAP 并在网关上有大量活跃用户**的企业。在他们的渗透逻辑里，“具备内网、拥有域环境且与 LDAP 集成”才是值得投入精力的高价值目标。

#### 严重依赖边缘设备与身份凭据

在确立目标后，该组织的大部分突破口都聚焦在企业网络的最外围边界。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQZfIBjibk9ewgHbDX08n6ArlflwzJSrkhPTAH3ZIALBQtSPpu36icplOuXvKkuiaQtWuXiboA98CAStUZ4RdSLPpeibLxcpiaXdYCasY/640?wx_fmt=png&from=appmsg)

攻击者在群内分享防火墙内部策略与 VPN 明文凭据

在上图这段内部对话中，成员之间正在相互分享从攻陷设备中提取出的内部路由策略和 VPN 配置信息。甚至明确写出了某目标开发 VPN 的网关地址及明文账号密码。

在他们熟悉的攻击路径里，一旦利用边缘设备的弱口令或未修补的历史漏洞建立了 SSL VPN 连接，他们就会直接提取设备上的 LDAP 绑定凭据。这种利用网关信任域进行二次渗透的手法，使得他们在潜入企业核心活动目录（AD）时拥有了合法的身份掩护，极难被传统的内网监测设备发现。

#### 团队协作与技术经验沉淀

在进入内网后的维权与最终的加密阶段，组织内部展现出了完整的技术分享机制。

![img](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQY1oSUPkLtKGibz7xiatVIHgGHL10miaQcsCNnYB4bPicA4nAr1KnwQ9yibAStxCya8MzCicQq7m9JUa9k4gYMUyzrV1IVkEZNIBv5Wg/640?wx_fmt=png&from=appmsg)

成员之间探讨勒索加密器具体参数配置的聊天截图

例如在准备执行破坏前，成员 Wick 在群里直接指导其他人如何使用加密器命令行。他们会精确地探讨如何使用 `--superfast` 加快加密速度，以及利用 `--system` 替代普通路径以绕过特定限制。

此外，他们还在频道内沉淀了大量的攻击技巧。比如讨论如何使用 DumpBrowserSecrets 工具批量提取管理员的浏览器 Cookie 以劫持关键系统的会话，或是探讨如何利用符号链接技术阻断终端上的 EDR 进程启动。这些痕迹都表明，该团伙具备相当深厚的技术底蕴。

### 攻击者极其本土化的活动轨迹

在梳理这些枯燥的渗透术语时，我们意外捕捉到了一些极其特殊的情报线索。如果说技术是可以跨国界学习的，那么下面这些生活与工具轨迹，则暗示着这个看似遥远的俄语系黑客组织，对国内生态有着异乎寻常的了解。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQYXnQHKzicJ8aiaaGMttwV0YVLe2TyYWPicPVcEpuYldlPvtasoQyLwlEXZJ6MgwV1Q3cV28ujeMffIm8nrO6uBeaStl9jZX2n5Gk/640?wx_fmt=png&from=appmsg)![img](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQaEiaTDmFAPfC9kFcbohFmf1Js3KFN9EDXibJpvmA9EAumaF9fEIicbN16njnXQNReHDNXbpXDgcZcic0Bf92ImJHNSgeBic5nAPl6Q/640?wx_fmt=png&from=appmsg)![img](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQYtHw3LeS9qIQbM23126fEg1W1Q75GKMY3uR30vvhBvFszR9ickgQVW3opCFzGcdLDp2BMRTLicjicIUKFxYlgMpLP9PvN7PzEOiag/640?wx_fmt=png&from=appmsg)

核心成员用俄语讨论曾在中国海南停留及就医的聊天记录

在某天深夜的闲聊中，核心成员 zeta88 突然用俄语感慨：“我想念中国了，更确切地说是想念中国的食物和天气。”

随后，另一名代号为 quant 的成员直接跟帖爆出了更具体的地理坐标：“靠，哥们，我之前在海南待过，那是真舒服。”

如果说生活轨迹只是巧合，那么他们对国内安全工具的熟练运用则进一步印证了我们的猜想。

![img](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQbOkdgiaFyefrGfP9h8Gfgwtjs7FEgCfGpSQQTtvmYLUI8fbe0pvtmOiarZL7pZlsZPWN1cVcpia1hX0GZn1ZDHpXbsYxIwtu4sRQ/640?wx_fmt=png&from=appmsg)

核心成员在内部群组分享国内大语言模型链接

在讨论技术难题时，zeta88 在群内整理了一份大语言模型辅助工具清单（见上图）。令人惊讶的是，除了国际通用工具，清单中赫然列出了国内头部的几款 AI 产品：Kimi、文心一言（ERNIE）、智谱，并特别点名了 DeepSeek 和 Qwen。

![img](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQaOBKEhdHw8bv8btUqfTGx3P4hVYibt2nl64yHw2398gibURv0KeOfPPicpkL9dWSCfWhprexf1UtPK8sQqTTicSxhGibicyIBl5zRIA/640?wx_fmt=png&from=appmsg)

攻击者交流使用国内哈希解密平台 chamd5 的记录

不仅如此，在涉及到密码破解与哈希解密的工作环节（见上图），zeta88 还向团队强力推荐了国内知名的安全社区解密平台 chamd5.org，并表示自己甚至拥有该平台在 Telegram 上的定制查询机器人。

这些生动的细节为我们勾勒出了一个截然不同的攻击者画像。他们不仅具备极高的网络攻防技术，更是深谙中国社会环境与本土技术生态的“老玩家”。这种对国内环境的信息熟悉程度，无疑会让他们在针对国内企业发动定向攻击时更加得心应手。

### 从内网视角看企业安全建设

复盘至此，The Gentlemen 勒索组织第一阶段的运作全景已初步展现。从针对性的目标筛选、对边缘身份设施的精准打击，再到深谙本土生态的隐蔽作案手法，这给我们日常的企业安全建设提供了非常务实的参考。

结合此次暴露出的攻击路径，Solar 应急响应团队建议企业重点关注以下防御维度：

1. **收紧边界设备的身份基线**：类似 FortiGate 等 VPN 边缘接入设备是本次事件中的突破重灾区。严禁在对外暴露的网关上使用弱口令，强制开启双因素认证（MFA），这是阻断自动化撞库与凭据复用最有效、成本最低的手段。
2. **切断 LDAP 与 AD 的过度信任**：攻击者极度偏好从 VPN 侧获取 LDAP 凭证进而在域内提权。建议对 AD 域控的查询权限进行严格的基线梳理，推进网络微隔离，避免一台边缘设备的沦陷直接导致核心认证架构的底牌尽失。
3. **警惕凭据抓取与合法工具的滥用**：在终端侧，除了部署常规的安全软件，应重点强化对系统内存（如 LSASS 进程）的读取保护。同时，对类似 NetExec、rclone 等容易被黑客当作内网横向和数据外传通道的合法工具，建立严格的运行监控策略。

**由于本次泄露的数据体量庞大且技术细节繁多，关于该组织在内网横向移动中具体使用的提权手段和其它紧张刺激的聊天，我们将放在本系列的（二）中为您做更深度的硬核技术拆解。**

网络安全是一项需要持续投入和动态调整的系统工程。面对愈发专业且狡猾的勒索团伙，基础架构的每一次权限收敛都至关重要。如果您在企业日常安全运维中遇到疑难问题，或需要专业的应急支撑，欢迎随时与我们团队交流探讨。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/887OLfia3YQaNjaj1NLuPOcc3WXqDZia6QmzCWq3evwI6IOTbdUgeUjkwWYTlq7CbQdicHjDd1N8nT1GyS5eP7IvavVDjgbOxibbD6EtAnOzJII/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)
> 在企业日常的安全运维中，突发勒索病毒往往让人措手不及。遇到这种情况，正确的应急响应流程能够最大程度控制影响范围、降低数据损失。
>
> 这里为大家准备了一张完整的《勒索病毒应急处置指南》长图，建议各位安全从业者和IT运维人员收藏备用。如遇突发情况，请保持冷静，参考本图进行快速、规范的处置
>
> 附加资料下载： 防御与响应同样重要。扫描图末的二维码，还可以直接获取完整的《2025年勒索病毒年报》以及《勒索处置一体化》等专业文件，帮助大家深入了解当前的威胁趋势，提前做好防御规划。
>
> 安全无小事，掌握科学的处置流程，是我们应对突发安全事件最有效的武器。

![img](https://mmbiz.qpic.cn/mmbiz_png/887OLfia3YQYVX1ZfrWicEuL2OiaJyQsCtosffoTELZXib71tGsGSiaOkia7VhXKdSTBRNwEauZzASIUicXXhdJdSpOcJ0OjJA5Awf91LicibDt0H6HQ/640?wx_fmt=png&from=appmsg)

以下是solar安全团队近期处理过的常见勒索病毒后缀：

|  |  |  |
| --- | --- | --- |
| **收录时间** | **病毒家族** | **相关文章** |
| 2025/01/14 | Medusalocker | [【病毒分析】深入剖析MedusaLocker勒索家族：从密钥生成到文件加密的全链路解析](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247497133&idx=1&sn=450c9eacc3956465a4c74fbdc1e6aa6e&scene=21#wechat_redirect)  [【病毒分析】新版勒索病毒MEDUSA LOCKER 首发深度分析](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247503856&idx=1&sn=c598583331355f663797d16674d27849&scene=21#wechat_redirect) |
| 2025/01/15 | Medusa | [【病毒分析】“美杜莎”勒索家族：从入侵到结束的全流程深度解析](https://mp.weixin.qq.com/s?__biz=MzkyOTQ0MjE1NQ==&mid=2247496674&idx=1&sn=563563c98553956ba754f944352c26b3&token=227041078&lang=zh_CN&sce...