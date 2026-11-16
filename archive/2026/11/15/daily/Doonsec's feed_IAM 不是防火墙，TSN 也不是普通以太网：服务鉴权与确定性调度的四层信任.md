---
title: IAM 不是防火墙，TSN 也不是普通以太网：服务鉴权与确定性调度的四层信任
url: https://mp.weixin.qq.com/s/VrGfB8XBxA5YKCfQRigjZg
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:44:23.103201
---

# IAM 不是防火墙，TSN 也不是普通以太网：服务鉴权与确定性调度的四层信任

# IAM 不是防火墙，TSN 也不是普通以太网：服务鉴权与确定性调度的四层信任

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCpMaDYVGMMtuR3fmy750iaicCKDagwQOrg64LEaCmsteVt9oP58YVs2DKiaaBP7Ls7WrHegrKtLib2VwklnMT6yamPZTbdJSEmSX8/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247582550&idx=1&sn=d7226bc800af241beba7f3da987f9de3&scene=21#wechat_redirect)

上期我们把 SOME/IP-SD 拆到字段级，结论是「收到格式合法的 OfferService，不等于对方就是预期 ECU」。今天兑现预告，往上一层走：AUTOSAR Adaptive Platform 用 IAM 回答「谁能调用」，用 TSN 回答「什么时候能发、占哪条队列」。这两套机制常被画在同一张架构图里，却经常被当成彼此的替代品。这一期把规范原文、工程实现与论文里的攻击前提分三层摆开，顺带把「默认拒绝」这个被写滥的词放回它该在的位置。

**一、先把平台边界摆正：AP 与 CP 是分工，不是升级**

Classic Platform（CP）面向 MCU 上的经典 ECU，静态配置、OSEK/经典 OS、面向信号的 RTE；Adaptive Platform（AP）面向 MPU / 高性能计算节点，以 C++、POSIX OS 与面向服务的通信支持动态部署。**这只是架构分工**：不代表所有 HPC 都必须用 AP，也不代表 CP 节点不能承载高算力任务。

ARA（AUTOSAR Runtime for Adaptive Applications）是 AP 应用看到的功能簇接口集合。公开技术资料列示的簇包括 `ara::com`（通信管理）、`ara::iam`（身份与访问管理）、`ara::crypto`（加密）、`ara::exec`（执行管理）、`ara::sm`（状态管理）、`ara::phm`（平台健康管理）、`ara::ucm`（更新与配置管理）、`ara::diag`（诊断）、`ara::log`（日志与追踪）、`ara::per`（持久化）、`ara::nm`、`ara::idsm`（入侵检测系统管理）、`ara::tsync`（时间同步）等，下面是 POSIX PSE51 / C++ STL 操作系统接口与硬件 / 虚拟机 / 容器层。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAMvWshibhIlm853ibvygK5ynDLdRfWXBNEia6LqNDPQ9LvS0cBCL2Fmp541vByyIaXvtiaJtctSMepX7zZsOt88POTMS6wxmfoibXU/640?wx_fmt=png&from=appmsg)

图 1｜AUTOSAR Adaptive Platform（ARA）功能簇架构

来源／图片性质：公开技术资料图，谈思实验室整理；图中并列 ara::com / ara::iam / ara::crypto / ara::exec / ara::ucm / ara::idsm / ara::tsync 等，并标出 IPC / Signal PDU / SOME/IP / DDS 绑定，非 AUTOSAR 官方发布页原图

有两处值得先圈出来：其一，`ara::com` 下面并列**IPC、Signal PDU、SOME/IP、DDS**多种绑定——上期拆的 SOME/IP-SD 只是其中一种；其二，`ara::tsync` 与 `ara::idsm` 是独立于 `ara::iam` 的簇，时间同步与入侵检测不是 IAM 的子功能。本期后半段讲 TSN，正是要从 `ara::tsync` 这一层往下走到交换机。

2026 年 10 月 28 日，普华基础软件与 AUTOSAR 联合发布 CAPI 1.0。中国经济时报报道称其完整覆盖 AUTOSAR 自适应平台全部 15 个核心功能簇；另有产业报道把它描述为汇集华为、小米、阿里达摩院、中国一汽等多家机构一线实践的白皮书，并提到同期 V26.10 适配国密算法。**两种表述本期都按 Q4 产业动态处理**：它不是 AUTOSAR 强制要求，不是 OEM 工程配置，也不能证明某量产车型使用了特定 AP 版本；本刊同样未检索到可核验的 AUTOSAR AP 量产车型 / 版本清单，因此不提供渗透率数字。

**二、IAM 规范怎么说：Grant 是配置事实，决策是运行时结果**

AUTOSAR IAM 需求文档（RS\_IAM\_00001—00007 等）给出的模型并不复杂，但每个词都有固定含义：

* **Subject**：发起访问的主体，通常是一个 Adaptive Application、进程或进程的一部分，也可对应 UID；
* **Resource / Object**：被访问的资源，可以是服务接口、服务实例、Method、Event、Eventgroup、Field，也可以是另一个进程；
* **Action / Intent**：想做的动作，20-11 规范称 Intent，后续资料多称 Capability；
* **Grant**：写在 Manifest / 部署配置里的**授权事实**；
* **Access Control Decision**：PDP 返回的**Allow / Deny 布尔结果；**
* **PEP / PDP**：策略执行点与策略决策点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaC6AibVvHAQZjTDxric7Y2LkXnia6ku6mX40sGicyrmwLEEQqpzlCfS7rPn1Nz9CSWkVqYoC8FOEj2L5QHKmdljOU9FyoWG8W6YMos/640?wx_fmt=png&from=appmsg)

图 2｜AUTOSAR AP IAM：一次服务调用，要经过哪些判决点

来源／图片性质：谈思实验室编辑部绘制，依据 AUTOSAR IAM 需求 RS\_IAM\_00001 / 00002 / 00004 / 00005 / 00006 / 00007 与公开技术解析整理，非 AUTOSAR 规范原文

调用链是：应用发起访问 →**PEP 截断控制流** → PEP 通过 Execution Management / 操作系统机制识别请求者身份（Linux 可用 `SO\_PEERCRED`、`getpeerid()`，QNX 用消息传递）→ PEP 把 Subject、Resource、Action、Environment 交给 PDP → PDP 依据 Manifest 中的 Intents 与 Policy 返回决策 → PEP 放行或拒绝并记录。

**这里有一条最容易被工程实现绕过的红线**：RS\_IAM\_00002 规定，PEP 必须位于「对象进程 / 操作系统 / AP 基础平台进程」之一，**且不得运行在请求者自己的进程里**；理由写得很直白——Adaptive Application 被视为「可能已被攻陷」，应用不能判决自己的请求，也不能伪造身份或改写策略。RS\_IAM\_00004 进一步要求运行时阻止应用绕过 AUTOSAR 定义的 API 直连服务实例，否则 IAM 形同虚设；RS\_IAM\_00005 限制应用读取其他应用的权限信息；RS\_IAM\_00006 明确 **Policy 不属于 AUTOSAR 元模型**，可由实现自定义，但 PDP 必须能同时取得 Intents 与 Policy。

部署层还能查到更具体的工程痕迹：设计期有 `GrantDesign` 元类，平台级落为 `Grant`；`ComMethodGrant` 允许进程执行服务接口方法，`ComOfferServiceGrant` 允许进程请求提供服务实例；本地 IAM 需先配置显式 IPC，再由 `arapipcd` 守护进程以 `--use-iam` 配合 `iam\_\_flatcfg.bin` 启用，配置文件路径由环境变量 `ECUCFG\_ENV\_VAR\_ROOTFOLDER` 决定。**这些属于具体实现的做法，不是 AUTOSAR 对所有项目规定的统一默认值**。

**三、Grant 不是「进程合法」，而是三元组判决**

把 IAM 读成「这个进程是不是合法进程」，是第二高频误读。真正的判决粒度是**Subject × Resource × Action**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCTD4uBKJ4Xzd6oGMEjjLFQvQEGJB6hn8mhicqHM29iag9icPTxvtqib76726DeMct5aY3Z2sopSsdwpLAaVvSdwlicpNYsmmWbiadNk/640?wx_fmt=png&from=appmsg)

图 3｜Grant 不是「进程合法」，而是「谁对哪个资源能做哪个动作」

来源／图片性质：谈思实验室编辑部绘制，表内 5 行映射为编辑部示例、非 AUTOSAR 规范表格；判决结果为工程建议，非规范统一默认

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA4PvQyTRR43sUicsCmoLTupuNwU2OGicnervYibMtMJPfTSGLwlV2rjE7RPM05sYs91Cf9yePia5zrJ0cMpx99ezWmMa04Zo98WEM/640?wx_fmt=png&from=appmsg)

两个必须写清的边界：

* **SOME/IP-SD 白名单只保护 SOME/IP 绑定这一层**。上期讲的 Offer / Find / Subscribe 过滤、组播范围与 TTL 校验，覆盖不到 `ara::com` 的其他绑定；服务发现通过，不等于方法调用有权。
* **Linux capabilities、SELinux / AppArmor、POSIX DAC 是操作系统级访问控制**，与 IAM 组成纵深防御，但不能替代应用层服务授权；反过来，IAM 放行也不代表固件合法、密钥未泄露或数据不敏感。

**「默认拒绝」这个词要放回它该在的位置**：RS\_IAM\_00001 的用例写的是「设计者声明 App 的预期用途，集成者审阅请求动作集合并通过赋予 GRANT 接受」，其目标是「攻击者控制 App 后不会获得比 App 初始权限更多的权限」。本刊本次未取得对应版本 SWS 中关于「Grant 缺失时默认放行还是拒绝」「服务发现阶段与方法调用阶段是否都强制校验」的逐条原文，因此不把「默认拒绝」写成 AUTOSAR 通用默认，也**不把「双重校验」写成规范强制**；正文只作为工程建议给出，并标注待核实。做项目时请回到所选 AUTOSAR 版本的 SWS 与供应商实现文档逐条核对。

**四、AP 各安全机制只覆盖一段，谁也替代不了谁**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDIS5XzWh6EPLzDmzDAfvCLfTotibpoMeGPvBFQVAiacW1zgsGxreRA3KCl76DHMvq47pa19ecEEUcicicl8WnJ1q76Y4ewa4RXfxM/640?wx_fmt=png&from=appmsg)

 一句话记法：**MACsec 不证明应用权限，mTLS 不决定方法授权，UCM 验过签名不代表新 Grant 合理，IAM 放行也不代表数据不敏感。**

**五、TSN 不是「更快的以太网」，是一套以时间为基准的调度体系**

AVB 是 IEEE 802.1AS、802.1Qav 等构成的时间同步与音视频传输体系；TSN 在其上扩展 802.1Qbv、802.1Qci、802.1CB、802.1Qcc 等。**AVB 是 TSN 的前身与应用子集，不等于完整 TSN**。 SOME/IP 位于中间件 / 应用层，TSN 位于以太网链路与转发层，二者可组合，但不存在「启用 TSN 后 SOME/IP 自动安全」或「启用 SOME/IP-SD 后无需门控」的关系。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaD1sVIEibiatAmELkHPgGicTJ634923iaCMmkL9waXxs8I0QCufZjM64wB3FbdPnHpqDKibXfYp8Yd4EGxQfAhYqbFu9X5pVJz4CU9s/640?wx_fmt=jpeg&from=appmsg)

图 4｜IEEE 802.1Qci 每流过滤与监管（PSFP）流程

来源／图片性质：公开技术资料图，谈思实验室整理；图示流过滤器、门控、计量表与 Gate ID 门控列表，为技术原理示意，非 IEEE 标准原文

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDe2JaO2gwxmIIlIqVVBou2XklkibLs8yNbJr2UIicNia0xYbv2eYfMNjian0prXJFuK92EB6NBhJhK44XrDic1RI26KJiau5b1v1YKc/640?wx_fmt=png&from=appmsg)

**I****EEE 802.1DG-2025 是车载场景的「考纲」**：IEEE 802.1 官方项目页记录 2019-02-08 立项、2025-05-28 标准委员会批准、**2025-06-06 正式发布**。它不新增机制，只从 802.1 工具箱里圈出车载子集并裁决必选 / 可选：必选包括入口监管 / 流计量（Qci）、严格优先级、CBS（最高两个流量等级）与 ATS 异步流量整形（至少一个等级）；TAS / 802.1Qbv 与帧抢占为可选；FRER / 802.1CB 未进入必选基线；**时间同步本身为推荐，一旦支持调度流量才升为强制**。公开解读还提到 Avnu Alliance 的汽车认证项目已基于 802.1DG 展开。这些「必选 / 可选」清单来自对正式版的综述整理与行业解读，正文标注为转述口径，具体以标准原文为准。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCaLbvELRgNaeniamibX4LpkcWbn3qgniclDG15Oh2U2viaURNFiaUxicH1hdeQlia3ac3E8YQysTKL8pgKIsarlLN05XfO9ovfjZBsk4/640?wx_fmt=png&from=appmsg)

图 5｜IEEE 802.1DG-2025 车载 TSN 考纲、802.1Qbv 门控时序与 gPTP 信任前提

来源／图片性质：谈思实验室编辑部绘制，依据 IEEE 802.1 官方项目页、802.1DG 解读与公开论文整理；门控时序为原理示意，非标准原文图

**六、gPTP 攻击面：论文给出的是量化边界，不是量产车事件**

TSN 的确定性建立在「全网共享一个正确时间」之上，而 **gPTP（IEEE 802.1AS）原始设计缺少完整性保护**。Grandmaster 由 BMCA（最佳主时钟算法）动态选出，这既是鲁棒性设计，也是攻击入口。IFIP Networking 2026 论文把攻击归为三类：恶意 Grandmaster 分发伪造时间、被攻陷边界时钟注入累积延迟、以及选择性延迟 `Follow\_Up` 报文的非对称延迟攻击。

几条可引用但必须带前提的证据：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA3WAmGPFYk9Gyc54N3ibF9lds1EnWxwicPpKotMdlcv0BdtPrQRt0XOKl5JA7dKVLFYN7xibM91cPCs5YOWwjtdUhnXHT3xdIxGw/640?wx_fmt=png&from=appmsg)

工程风险应写成**条件式**：若 gPTP Grandmaster 未做身份与路径验证，恶意节点可能成为主时钟或注入延迟；若 GCL 可由受损管理面修改，关键时间窗可能错配；若 Qci 的流分类、门限或 Action Table 被绕过，DoS 会侵占确定性带宽；若 Stream ID、DMAC、VLAN PCP 可被伪造，普通帧可能抢占高优先级队列（电子工程专辑举例：用 PCP=7 冒充刹车指令）；若 MACsec 的密钥协商、加密与队列处理增加抖动，安全开销会挤压时间预算；跨交换机时间域不可信时，单点同步正确不代表全局正确。

**结论只写到这里**：截至 2026 年 11 月 15 日，本刊**未检索到经监管、法院或 OEM 确认的量产车 AP IAM 绕过案例**，也未检索到车载 TSN / gPTP 在真实量产车中被攻破的公开案例。上述研究均为仿真、台架、物理测试床或原型实现；一篇 2023 年 IEEE TVT 论文提到在「量产车辆映射出的现代以太网拓扑」上实验，但公开摘要不足以确认车型、硬件与实验边界，本期只列为待原文核验的线索。这个结论只代表本次检索的证据状态，不能解释为 IAM 或 TSN 没有风险。

**七、把两套机制接起来：身份、时间、转发、授权是一条链**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAOsQxzmsvFkVtZDlvSD8RRvYiaib3PTicUzVFFrAzlfbvsAypLR6aKqtavA8UtwiaMvvNtt13q24AyeGjFHXLUCbLh3F3G8ibYNvdY/640?wx_fmt=png&from=appmsg)

图 6｜一条不该断开的链：身份可信 → 时间可信 → 转发可信 → 服务授权来源／图片性质：谈思实验室编辑部绘制示意图，非 AUTOSAR / IEEE 官方架构图

典型攻击路径可以写成：运维账号或证书被冒用 → 配置管理面推送错误的 gPTP 主时钟 / GCL / Qci 规则 → 交换机或 HPC 接受错误配置 → 时间同步偏移或关键流错过门控 → 控制流延迟 / 乱序 → AP 进程收到伪造或过期的服务请求 → **IAM 的 Grant 仍按错误状态判决** → 功能异常。

反过来同样重要：**IAM ...