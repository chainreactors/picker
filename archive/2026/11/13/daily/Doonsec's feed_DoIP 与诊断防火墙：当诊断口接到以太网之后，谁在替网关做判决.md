---
title: DoIP 与诊断防火墙：当诊断口接到以太网之后，谁在替网关做判决
url: https://mp.weixin.qq.com/s/ukf3Yp62Yv6uP8VhWfcV4A
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:15:53.450048
---

# DoIP 与诊断防火墙：当诊断口接到以太网之后，谁在替网关做判决

# DoIP 与诊断防火墙：当诊断口接到以太网之后，谁在替网关做判决

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCpMaDYVGMMtuR3fmy750iaicCKDagwQOrg64LEaCmsteVt9oP58YVs2DKiaaBP7Ls7WrHegrKtLib2VwklnMT6yamPZTbdJSEmSX8/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247582550&idx=1&sn=d7226bc800af241beba7f3da987f9de3&scene=21#wechat_redirect)

上期我们把 CAN 上的三道门拆完了：会话决定哪些服务可见，0x27 决定哪些服务可用，网关决定哪个 ECU 能被碰到。今天兑现预告，把诊断口搬到以太网。多出来的不只是带宽——车辆发现、路由激活、TLS、VLAN、证书与审计，每一层都要重新回答一次「谁在说话、凭什么信」。而型式检验的问题，也从「能否刷写成功」变成了「为什么只允许这一次刷写」。

**一、先把协议栈摆正，别把 DoIP 和 UDS、SOME/IP 混着叫**

DoIP 不是应用层诊断服务，而是**把诊断消息搬到 IP 网络上的传输与网络层协议**。这一族标准的分工是：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaC1UZ8dW2FgfH5ldIEC0ibCib242KQSmTVxia4J5pKWKGLKJicLocDhenvhgId9VJE9Bibic8IHMvbNwXtebn7re168WpH1JOW07658Y/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBnTEbnyQlBpeTqCAicklibEfcS2rPRkPw0qu2GY22ty9BKzicttgUPoiaFbicggXnzNtBQ2TV5KKPIRr0u91JPUVNQg7S8UMrJXcus/640?wx_fmt=png&from=appmsg)

图 1｜汽车诊断通信的 OSI 分层与 DoIP 协议栈

来源／图片性质：公开技术资料图，谈思实验室整理；图中明确标出 ISO 14229-5 UDSonIP、ISO 13400-2 中的 Transport Layer Security (TLS) 与 ISO 13400-3 有线接口，非标准原文

一个值得记的细节：**GB/T 43258.2—2023 的规范性引用文件里包含 IETF RFC 5246（TLS 1.2）与 RFC 8446（TLS 1.3）**。这说明国标采标时已把传输层安全纳入引用范围，但「引用了 TLS」与「量产车默认启用双向证书认证」是两件完全不同的事，后面会展开。

顺带划清两个高频混淆：DoIP 负责诊断传输，**SOME/IP 是面向服务的通信中间件（下期讲）**，二者不是替代关系；**OBD-II 的法定排放诊断**与面向整车所有 ECU 的 UDS 增强诊断，目的也不同。把「OBD 合规」当成「诊断接口已做安全设计」，是审计里最常见的一句话错误。

**二、六道闸门：从物理接入到 UDS 响应**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCoiaHwH6Iqal013ia7ZTFPUNFGCZEgmHgfZjkQ3bk96KVojGnJeic8wDlbicTIOR1u5pm9ic7JASIUkRMQoKicNM5iaRHV8ScoHeuUC0/640?wx_fmt=png&from=appmsg)

图 2｜DoIP 诊断入口的六道闸门：标准定义什么、OEM 决定什么

来源／图片性质：谈思实验室编辑部绘制示意图，依据 ISO 13400 / GB/T 43258 与 AUTOSAR DoIP 公开资料整理，非标准原文

**1、物理 / 链路接入。**ISO 13400-3 规范有线车辆接口，ISO 13400-4 规范高速数据链路连接器；GB/T 43258.4—2023 的说明里专门提到，**为解决车辆制造商自定义引脚的冲突**（例如引脚 3 和 11）规定了方案 2。这点后面讲 OBD 引脚时还要回来。

**2、 IP 可达 + 车辆发现**。UDP 与 TCP 均使用 13400 端口。DoIP 实体获得 IP 地址后会主动发**出车辆通告 / 车辆声明（0x0004，通常 3 次）**；诊断仪也可发送车辆识别请求（0x0001），实体以 UDP 单播返回识别响应，携带 VIN（17 字节）、逻辑地址（2 字节）、EID（6 字节）、GID（6 字节）等字段。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaAJ2WX1YGR1EQ249FnC5YGFQmGLic1wIamdYrSIcUu70oZdsiaH2ZCNiaNrFHn96ibduUqkjqshPjvh0vGcW827cyfJY9unoicQ245Y/640?wx_fmt=jpeg&from=appmsg)

图 3｜DoIP 车辆发现与车辆识别时序

来源／图片性质：公开技术资料图（含原作者水印），谈思实验室整理；展示 Vehicle announcement (3x) 与 Vehicle identification request / response，非标准原文

**这里第一条红线：**收到格式合法的车辆通告，只说明「对方声称拥有某个逻辑地址」。ISO 13400 本身没有提供跨 OEM 的 PKI、证书吊销查询或身份声明机制，**不能把「收到了通告」写成「对方已通过身份认证」**。

**3、 TCP / TLS 协商**。ISO 13400-2:2019 引入 TLS 保护的 DoIP 连接，协议栈图里也把 Transport Layer Security 单列在 TCP/UDP/IP 之上。**但是否启用、TLS 版本、密码套件、证书验证方式与 OCSP/CRL 流程，由车辆安全规范与工程实现决定**。本刊本次未取得 ISO 13400-2:2019 可公开核验的全文条款，因此不断言 TLS 在该版中是「强制」还是「可选」，只写「机制可用、启用由 OEM」。

**4、 路由激活。**诊断仪建立 TCP 连接后发送 **RoutingActivationRequest（载荷类型 0x0005）**，携带源地址 SA、激活类型 Activation Type，以及部分工程实现里的 OEM 特定字段；实体返回 0x0006 响应。它的作用是**向 DoIP 实体注册诊断仪的源地址，激活成功后诊断报文才被接收**——它是会话建立机制，不是通用访问控制判决。

公开的 AUTOSAR DoIP 模块实现里，拒绝激活的条件包括未知源地址、该地址已在另一 socket 激活、缺少认证、确认被拒、激活类型要求安全 socket，以及未在配置时间内发送激活的 socket 会被关闭。**这些是 AUTOSAR / OEM 实现，不是 ISO 13400 逐条强制**，写测试用例时别标错依据。

**5、 诊断报文与防火墙决策。**诊断消息载荷类型为 **0x8001**，0x8002 / 0x8003 为正 / 负确认；此外还有 0x0008 Alive Check 响应、0x4001 DoIP 实体状态请求、0x4003 诊断电源模式信息请求。Tester 源地址与目标 ECU 逻辑地址、物理 / 功能寻址属于地址模型；**哪个源能到哪个目标、哪些服务码可用，由网关策略决定。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCDfTnW5Ra0z1InfqfhhBE2Y4ZgFDyE68NS574Xp21IYSVSm5Epu8KoqOuaQNt7ibSkkIyrkHXaHbO5ibaj2Ra3g0kXTtYDlicWqM/640?wx_fmt=png&from=appmsg)

图 4｜DoIP 报文结构与逻辑地址

来源／图片性质：公开技术资料图，谈思实验室整理；示 Protocol Version / Inv. Protocol Version / Payload Type / Payload Length 与 Source / Target Address，最大 1518 字节为不含 VLAN Tag 的以太网帧前提

工程上应禁止网关把任意源地址的报文无差别转发到所有 ECU，并对 0x27、0x2E、0x31、0x34—0x37 等高风险服务单独限流。**「诊断报文可转发」是协议能力，「无差别转发」是配置错误，两者不能混写成标准原文。**

**6、UDS 会话与审计。**到了这一层才回到上期讲的 0x10 会话、0x27 解锁与刷写流程。区别在于：IP 化之后，每一次会话都要能回溯到车辆发现、路由激活与证书决策的完整链路。

**三、TLS 只解决其中一段：安全车载以太网没有单一开关**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaC6eTicO1buvrL1gY41Qq1UrRhwFicGWJbxGfd7yJSUSibG7OxzBS7ulxiaw7cSJBhOvBeWic5l92VViaibaLiajpyWDJbiakLpjy4T6jvc/640?wx_fmt=png&from=appmsg)

结论很朴素：**MACsec 保护不了「诊断仪有没有权发 0x2E」，TLS 也保护不了「这个证书是否已被吊销」**。工程上可部署的诊断防火墙决策包括：仅允许登记设备的源 MAC/IP；只连接指定 DoIP TCP 端口；只对白名单目标逻辑地址建立路由；按会话、身份与服务码限制 UDS 访问；对 0x27 种子—密钥尝试、0x2E 写入、0x31 例程控制与 0x34—0x37 刷写设置次数、速率与冷却窗口；物理寻址只开放确有业务需要的 ECU；拒绝跨 VLAN 无条件转发诊断报文；产线与售后模式使用短时效凭证、关闭默认永久开放端口。

**这些全部是 OEM 工程经验，不是 ISO 13400 规定的固定阈值。**公开材料里没有「每辆车必须限流 N 次」这类统一结论；阈值要依据资产价值、攻击可行性、可用性需求与实测日志做风险接受，并留下批准人。

带宽也常被误读成安全等级。单对双绞线车载以太网常见 100 Mbit/s 与 1 Gbit/s 两档，行业资料通常分别对应 IEEE 802.3bw（100BASE-T1）与 IEEE 802.3bp（1000BASE-T1）**——精确编号与发布日期本次未取得 IEEE 官方页面，标为待核实，企业标准管理员应复核。**高带宽利于摄像头数据、OTA 包与诊断大数据，也让扫描、泛洪和未压缩诊断流量扩散得更快。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCSRwZD9DVV1c4d5dJicq266jlQ5Usm5rwOHvCPPhA8zzgp5csy2NC1icHd5C0DqgLq7kaiauNZ3spQhoKT2yUiboOQhQgHs8RFxYU/640?wx_fmt=png&from=appmsg)

图 5｜100BASE-T1 车载以太网网络拓扑示意

来源／图片性质：公开技术资料图，谈思实验室整理；为物理层拓扑示意，不代表某一量产车型的实际域划分

**四、物理接入 ≠ 内部身份：OBD 以太网引脚怎么说**

ISO 13400-3 规范有线接口，但 OEM 是否使用激活线、激活电平与时序、连接器引脚，以及是否允许通过 OBD 接口建立整车诊断连接，均可因车型而不同。公开技术资料里流传较广的一种方案是：以太网只占 5 个针位——引脚 3 / 11 为差分对 A（RX+/RX−）、12 / 13 为差分对 B（TX+/TX−）、引脚 8 为以太网激活线（车辆侧约 9.56 kΩ 输入电阻，用于区分两套引脚方案），并注明依据 ISO 13400-4 Option 1、BMW 的 ENET 线即按此接线。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDnicibtWokkTCjFtoELu1hUJ9gt2OmvYYEkicrX76RcXwtY93pxicCYg2amdSNAzySJJKTlfVPxN6MWnOurP8QCqpia1Bw1YnFD55E/640?wx_fmt=png&from=appmsg)

图 6｜OBD-II 以太网引脚的一种方案（3/11、12/13、8 激活线）

来源／图片性质：公开技术资料图，图内注明依据 ISO 13400-4 Option 1；仅为一种引脚方案，量产车型引脚分配由 OEM 定义，不得外推

**请把它当「一种方案」而不是「通用引脚表」**。GB/T 43258.4—2023 之所以要规定方案 2，恰恰是因为 OEM 自定义引脚会冲突；在没有该车维修手册、ECU 接口规范或可信拆解依据前，写「OBD 第 X 针就是以太网激活线」都应标待核实。

更重要的判断是层级：能接入 RJ45 或 OBD 端口，只证明获得一个物理 / 链路层入口；诊断仪还要依次完成 IP 可达 → 车辆发现 → TCP 连接 → 路由激活 → UDS 会话。即使前序全部成功，目标 ECU 是否可达仍受网关策略、VLAN、功能寻址范围、会话状态与证书权限约束。反过来，一个直连测试设备能访问内部 ECU，说明车辆把外部接入点放进了内部信任域，或者隔离控制已经失效——**不能仅凭「能 Ping 通」推断已取得 ECU 控制权。**

**五、型式检验的问题变了：为什么只允许这一次刷写**

诊断口 IP 化后，测试日志至少要关联：测试日期与 VIN、ECU 硬件与软件版本、测试仪身份与证书序列号、测试仪软件版本、物理接口、VLAN / IP / MAC、车辆发现报文、路由激活请求 / 响应及源地址、UDS 会话状态、目标逻辑地址、服务码、结果、失败原因、证据文件哈希。只保存「诊断仪最终提示成功」，不足以证明网关策略有效。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAYeo4icrricQKNJgOc9zKPMddiaDzTwzOZGQqaaCQDF6xF3U7iavsABzhWgnsP4ic6jF2iaUzPSGDVL42a30IN6nfWItRCMDvRAJ1QY/640?wx_fmt=png&from=appmsg)

证书体系的关键不只是「签发」，还有撤销、替换、时钟与审计：明确根证书、中间 CA、车辆端与诊断端证书用途；在脱机车间维护 OCSP/CRL 缓存或短效证书策略；为证书过期、临时离线、紧急回退、设备丢失和员工离职设定流程。**私钥、种子、密钥派生材料与敏感审计数据不得直接写入普通诊断日志。**

OTA 后的诊断回归，覆盖的是「升级前允许什么、升级后是否仍然允许」：路由激活成功与失败路径、物理 / 功能寻址、允许与拒绝的目标 ECU、读 / 写 / 例程 / 刷写服务限流、VLAN 与域隔离、产线 / 售后模式切换、证书过期吊销与时钟异常、异常断开后的状态恢复、已知合法工具与新版本工具。测试目标不是穷举所有 IP 报文，而是确认每次策略变更都能对应到变更说明、威胁模型、验证记录与审批人。

合规衔接上再强调一次属性差异：**GB 44495—2024 是强制性整车信息安全标准**，覆盖外部连接、通信、软件升级、数据安全等域，DoIP 的有线诊断入口、诊断网关、ECU 逻辑地址、目标服务、VLAN 与升级链路都在检验视野内；**GB/T 44778—2024 是推荐性诊断接口专项标准**（本刊 11 月 12 日已展开）；UN R155 的 CSMS / VTA 与 Annex 5 威胁场景、ISO/SAE 21434 的 TARA 则要求把以太网交换机、DoIP 网关、区域控制器、诊断仪证书与 SBOM 构建产物当作可分析资产。阈值、算法与日志留存期主要由企业标准、合同与具体法规决定，公开材料没有证明上述文件统一规定了限流次数、TLS 版本、VLAN 编号或日志保存年限。

**六、案例边界，与下期预告**

**截至 2026 年 11 月 13 日，本刊未检索到经工信部、市场监管总局、NHTSA、OEM 安全公告或法院确认的量产车 DoIP 攻击案例。** 公开可见的模糊测试材料多使用「客户设备、不便透露具体信息」的未具名 DoIP 设备，缺少车型、漏洞编号、修复版本与供应商确认，不能外推为特定车型失陷。2015 Jeep Cherokee 只作为「车机跨接总线后放大影响」的一句对照（其攻击路径与 DoIP 网关不直接相同，事件全貌见 11 月 10 日）；2025 Hardware.io 关于起亚 MOTREX 的披露为会议披露、厂商未确认，本期不重复展开。

这个结论只代表**截至本次检索的证据状态**，不能解释为「DoIP 不存在风险」。恰恰相反：正因为缺少公开量产案例，企业更要把自己的路由激活日志、网关策略与回归记录做成可回放的证据。

**下期第 05 期：**《SOME/IP 服务发现与车载以太网服务治理》——Service Discovery 的 Offer / Find / Subscribe、单播与组播、Method / Event / Field、服务实例与事件组生命周期、SOME/IP-SD 与 VLAN / 防火墙联动，以及动态服务发现的重放与伪造风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAgMtYBvxP2sDlfLAwoYib8145dMuTYZVJicxeicYLHeLoLWHibwZOxZKBcEFdvDzVLDUxffphYZ209H0Iy8LeZicYic10LYFWtDYGfM/640?wx_fmt=png&from=appmsg)

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**精品活动推荐**

[![](https://mmbiz.qpi...