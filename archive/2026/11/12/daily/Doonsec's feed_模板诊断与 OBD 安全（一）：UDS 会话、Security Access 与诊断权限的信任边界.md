---
title: 模板诊断与 OBD 安全（一）：UDS 会话、Security Access 与诊断权限的信任边界
url: https://mp.weixin.qq.com/s/0gCvzw7yCbIWcMEeIZYGhw
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T08:59:26.376348
---

# 模板诊断与 OBD 安全（一）：UDS 会话、Security Access 与诊断权限的信任边界

# 模板诊断与 OBD 安全（一）：UDS 会话、Security Access 与诊断权限的信任边界

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCpMaDYVGMMtuR3fmy750iaicCKDagwQOrg64LEaCmsteVt9oP58YVs2DKiaaBP7Ls7WrHegrKtLib2VwklnMT6yamPZTbdJSEmSX8/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247582550&idx=1&sn=d7226bc800af241beba7f3da987f9de3&scene=21#wechat_redirect)

上期结尾我们预告了诊断口。它常常是整车最容易被忽略的高权限入口：物理可达、协议公开、工具成熟，而且一旦解锁就能读写 ECU、改写配置、发起刷写。本期按连载顺序，把 UDS 会话、0x27 安全访问、刷写权限链与 OBD / DoIP 的信任边界走一遍。先说清楚一件事——「插上 OBD 就能为所欲为」是错的，实际风险取决于会话状态、安全访问与网关策略这三道门。

**一、先把协议栈摆正**

UDS 不是一个协议，而是 ISO 14229 系列定义的应用层服务集，要靠下层协议承载：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaB9UuTzXrz3RlpyDxEqDegleszwicxQgSH5E52FhH2ncGC7h1ialacU5GJD6xc15zwIV5shru70X0Rucw5RjYOTXGzqIiapn3q3KE/640?wx_fmt=png&from=appmsg)

图1 | 谈思实验室整理制表

还有一个高频混淆：**OBD-II 的法定定位是排放诊断**，源于排放法规，核心是监测尾气相关系统、点亮 MIL、存储排放相关 DTC（SAE J1979 / ISO 15031-5 定义 PID）；**UDS 是面向整车所有 ECU 的增强诊断**，覆盖读写、例程、刷写、故障存储。二者目的不同，不能把「OBD 合规」当成「诊断接口已做安全设计」。国内对应的专项标准是 **GB/T 44778-2024《汽车诊断接口信息安全技术要求及试验方法》**——注意是 **GB/T，推荐性国家标准**，2024 年 10 月 26 日发布并同日实施，不是强制性标准，与 GB 44495—2024 不能混称（关于这一点上期已纠过一次）。

**二、会话：权限的第一道门**

诊断会话由 0x10 DiagnosticSessionControl 切换。工程上最常见的映射是：`10 01` 默认会话、`10 02` 编程会话、`10 03` 扩展会话——**这是 AUTOSAR/DCM 与主机厂诊断规范的典型实现，不是 ISO 14229 文本强制规定「0x02 必为编程会话」**，具体取值与行为由 ECU 实现决定。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDfHw3qibKB9mflibJ4UMQ226PYKiatv3gz3GqKIy2DUvoCYBTgWvVXB1ZSMIKicTibB4ickrxfPPerTPtvP50P5rXqR9RH0pDib4Ztbs/640?wx_fmt=png&from=appmsg)

图 2｜UDS 诊断会话状态与切换示意

来源／图片性质：公开技术图，谈思实验室整理；会话子功能取值与超时数值为典型工程实现，非 ISO 14229 强制值

ISO 14229-2 的规范机制有两条值得记牢：

* **单一会话：**规范明确「单一 server 在同一时刻只能有一个诊断会话处于 active」，因此每个点对点通道需要一个 S3Server 定时器；
* **超时回退：**S3Server 超时（期间无任何诊断请求，包括 TesterPresent）后，Server 应退出非默认会话、回到 defaultSession。工程上常见 5000 ms 与 `0x3E 80`（抑制正响应保活），**但规范不规定默认绝对数值**，5000 ms 是项目惯例。

会话切换的副作用同样属于典型工程行为：重置安全访问状态（已解锁回锁定）、改变可用服务集、默认会话下写 DID（0x2E）通常被拒。一句话——会话决定「哪些服务可见」，安全访问决定「哪些服务可用」。

**三、0x27：奇偶子功能背后的挑战响应**

0x27 SecurityAccess 是挑战响应机制：奇数子功能 requestSeed（请求种子），紧随其后的偶数子功能 sendKey（发送密钥）；诊断仪用项目私有算法从种子算出密钥回传，ECU 复算比对，通过才解锁对应安全级别。常见的 NRC 有 0x35 invalidKey、0x36 exceededNumberOfAttempts、0x37 requiredTimeDelayNotExpired。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAHPG1lZoklsEr9w7eZJHgO9Ay5awndTefA3ToPgd9tEZyJMLDAgaakMKjFLwpMkib76ibQsCucclwAdZJskp2foPUpHOkkWTuLI/640?wx_fmt=png&from=appmsg)

图 3｜UDS 0x27 Security Access 种子—密钥挑战响应

来源／图片性质：谈思实验室编辑部绘制示意图，依据 ISO 14229-1 机制整理，非标准原文

**规范与实现的分界必须写清：**种子/密钥的字节长度、算法、安全级别语义（Level 1/2/3 或 FBL、标定、刷写等命名）、尝试阈值与冷却时长，都由项目诊断规范定义，ISO 14229 不强制统一取值；规范只定义服务、子功能奇偶配对与相应 NRC 的含义。不同安全级别通过服务表与 security mask 控制「某服务在某级别下可用」，否则返回 NRC 0x33。

真正决定工程强度的，是下面这七类常见实现缺陷：

**1. 种子可预测或固定**——伪随机质量差、种子池过小，甚至种子与密钥映射表可查；

**2. 算法硬编码**在诊断仪或量产固件里，固件被提取后可逆向重放；

**3. 密钥长度过短**（如 2 字节种子，穷举空间仅 65536）；

**4. 无尝试次数限制或延时惩罚**，允许在线暴力破解；

**5. 错误计数器不持久化**，ECU 复位即清零，可反复尝试；

**6. 解锁后权限过大**，单一级别同时开放读内存、写标定、刷写；

**7. Bootloader 与应用共用同一密钥/级别**，应用层漏洞可横向到刷写权限。

顺带记一个容易踩的测试细节：若请求种子时 ECU 返回全零种子，通常表示「该级别当前已解锁」，不是出错；延时惩罚期间即使送对密钥也会被拒，且错误尝试会重置计时。自动化诊断测试若没覆盖这两条，实车上会出现「密码明明对却进不去」的假故障。

**四、刷写流程：0x27 管「谁」，Bootloader 管「什么」**

典型刷写顺序（工程实现，非 ISO 14229 规定的唯一流程）为：进入编程会话 `10 02` → `27 01`/`27 02` 解锁 → `2E` 写维修店 ID 与刷写指纹 → `34` RequestDownload → `36` TransferData 循环 → `37` RequestTransferExit → `31` 触发校验例程 → `11 01` 复位。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBDiaBAgLL4DECib6SUXTcPn33wDgtNcsGCkiamLObcL3iasia7hFxibgOztUgWaYyhIfLibOtkqicTDbxBib40wUhpRRmZrwsF1ibjlhcvo/640?wx_fmt=png&from=appmsg)

图 4｜UDS 编程会话刷写序列

来源／图片性质：公开技术整理图，谈思实验室整理；步骤顺序为典型工程实现，非 ISO 14229 强制唯一序列

这里有两层常被合并的闸门：

* **0x27 回答「谁被允许发起刷写」；**
* **Bootloader 的签名/哈希验证与安全启动链回答「刷进去的是什么」**。前者失守不等于后者失效，但反过来，签名验证做得再好，若 0x27 可被低成本解锁，攻击者仍可反复发起刷写、耗尽存储或触发降级。GB 44496 软件升级安全与 GB 44495 外部连接安全，分别约束这两层。

刷写前后还有两个副作用要写进测试用例：`0x28` CommunicationControl 抑制应用报文以降低总线负载，但不当抑制可能让其他 ECU 误判节点丢失进入跛行；`0x85` ControlDTCSetting 暂停 DTC 记录，若刷写失败后未恢复，会导致 DTC 记录长期失效。

**五、从 OBD 口到网关：物理可达 ≠ 为所欲为**

OBD-II 使用 SAE J1962 定义的 16 针 D 形连接器，位于驾驶侧仪表台下方：针脚 4/5 为底盘/信号地、6/14 为 CAN High/Low、16 为蓄电池正极，7/15 常用于 K-Line，1/8/9/11/12/13 为厂商自定义。物理可达是事实，但接入设备发出的每一个请求都要过三道门：会话状态、0x27 解锁、网关路由策略。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaATP2x991J7wf4YAPMryZ6ibicZyL28eqL7mSE75FBSBm31QkbHib9t7rRj7icEvpPMADooBicrxe7vyicbq9XbJHK3glTbKR2Kmm78s/640?wx_fmt=jpeg&from=appmsg)

图 5｜SAE J1962 OBD-II 16 针连接器引脚定义

来源／图片性质：公开标准资料图，谈思实验室整理；针脚用途为标准化定义，厂商自定义脚位因车型而异

长报文靠 ISO-TP（ISO 15765-2）分段。经典 CAN 8 字节帧的四类帧结构如下，注意前提：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBCGIFohiaqXYAIMk4yEiaLTmibFhPL1ssyMP75xGIEOFqaCl1AzL2CcUUENPpUic37ZkG7aQAiaodibcyZfFiaRDcvLk8fq7gfx5lwms/640?wx_fmt=png&from=appmsg)

图 6｜ISO-TP（ISO 15765-2）四类帧结构

来源／图片性质：谈思实验室编辑部绘制示意图，依据帧类型定义整理，非标准原文；单帧 7 B / 首帧 6 B 仅在经典 CAN 8 字节数据场下成立

到了车载以太网，DoIP（ISO 13400 / GB/T 43258）要求外部设备先完成**车辆发现与路由激活**，网关据此决定把诊断报文路由到哪个目标 ECU。**未经路由激活的外部设备不应被转发到任意 ECU**——这是诊断隔离最关键的控制面。在此基础上，工程上还会叠加：网关对源 IP/MAC、目标 ECU 与诊断服务做白名单；物理寻址与功能寻址分开策略；对 `0x27`、`0x2E`、`0x31`、`0x34—0x37` 等高风险服务单独限流；产线模式与售后模式使用不同激活凭证。这些都属于工程经验，不是标准逐条强制。

**六、真实案例与证据边界**

**2015 Jeep Cherokee（点到为止）**：研究者论文明确提到，选择该车是因其车机可同时与两条 CAN 总线交互，攻击面大；攻入车机后向总线注入指令，实现对制动、转向等物理功能的控制。本期只取其中一个承重结论——**诊断/车机对 CAN 的高权限，加上接口隔离缺失，会把单点失陷放大为整车影响**。事件全貌与 140 万辆召回已在 11 月 10 日企业故事篇展开，不重复。

**2025 Hardware.io 起亚 / MOTREX 车机披露**：会议披露称 MOTREX MTXNC10AB 车机（涉及 2022—2025 年部分车型）可通过 RTOS 漏洞调用 `micomd` 守护进程向 M-CAN 发送伪造帧，并指出固件 PNG 缺数字签名、Bootloader 仅用 1 字节 CRC 校验完整性、串口日志明文存 RSA 私钥与蓝牙配对 PIN。**截至本期截点，未检索到起亚或 MOTREX 的官方确认、CVE 编号或修复公告**，因此只能写「会议披露，厂商未确认」，不能写成「起亚车机已被攻破」。

**关于恶意 OBD 设备**：本刊未检索到经 NHTSA 或法院文件确认的「某恶意 OBD 设备批量用于车辆攻击」权威案例，故不写具体设备名称。可写的工程风险表述是：未经认证的第三方 OBD 设备理论上可发送任意诊断报文，实际风险取决于 ECU 会话与安全访问控制的强度——而这正是本期要拆解的部分。

**七、合规衔接：哪些是强制，哪些是经验**

* **规范/标准层**：GB 44495—2024 是强制性整车信息安全标准，覆盖外部连接、通信、软件升级、数据安全等域；GB/T 44778-2024 是推荐性专项标准，规定诊断接入端与准入端的身份认证、数据使用、密钥销毁、安全存储与权限控制试验方法（例如要求对称认证采用 SM4 或 AES-128 及以上强度、控制器使用硬件安全存储身份认证密钥）；UN R155 Annex 5 的威胁场景包含物理接触的未授权访问，应纳入 CSMS 评估；ISO/SAE 21434 的 TARA 要求识别资产、威胁与攻击路径，**但不规定具体的速率阈值或密钥长度。**
* **工程经验层**：诊断仪账号分级与证书管理、日志留存时长、白名单颗粒度、限流阈值、产线/研发/售后/报废各阶段调试口的最小开启原则，均由车企在 TARA 中自行确定，需留下可复现的验证证据。

**八、本期三句话与下期预告**

* 会话决定「哪些服务可见」，0x27 决定「哪些服务可用」，网关决定「哪个 ECU 能被碰到」——三道门缺一不可。
* 0x27 的强度不在算法多复杂，而在种子随机性、错误计数器持久化、权限最小化与 Bootloader 独立密钥。
* 物理可达不等于授权通过；把 OBD 口、DoIP 路由激活与售后工具链放进同一份威胁模型，才谈得上诊断安全。

下期接第 04 期：**「DoIP 与诊断防火墙：当诊断口接到以太网之后」**——拆车辆发现与路由激活的信任假设、网关白名单策略、诊断仪证书与账号分级，以及售后工具链怎么留证据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAgMtYBvxP2sDlfLAwoYib8145dMuTYZVJicxeicYLHeLoLWHibwZOxZKBcEFdvDzVLDUxffphYZ209H0Iy8LeZicYic10LYFWtDYGfM/640?wx_fmt=png&from=appmsg)

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

**专业社群**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJnASqAJY7fLYIeMGl8fHu4aPXusCVuX2qAYkrb9bQMRGEBvSghHETaQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&scene=21#wechat_redirect)

**部分入群专家来自：**

**新势力车企：**

特斯拉、理想、极氪、小米、零跑汽车、阿维塔汽车、智己汽车、小鹏、岚图汽车、蔚来汽车、吉祥汽车、赛力斯......

**外资传统主流车企代表:**

大众中国、大众酷翼、奥迪汽车、宝马、福特、戴姆勒-奔驰、通用、保时捷、沃尔沃、现代汽车、日产汽车、捷豹路虎、斯堪尼亚......

**内资传统主流车企：**

吉利汽车、上汽乘用车、长城汽车、上汽大众、长安汽车、北京汽车、东风汽车、广汽、比亚迪、一汽集团、一汽解放、东风商用、上汽商用......

**全球领先一级供应商：**

博世、大陆集团、联合汽车电子、安波福、采埃孚、科世达、舍弗勒、霍尼韦尔、大疆、日立、哈曼、华为、百度、联想、联发科、普瑞均胜、德赛西威、蜂巢转向、均联智行、武汉光庭、星纪魅族、中车集团、潍柴集团、地平线、紫光同芯、字节跳动、......

**二级供应商(500+以上)：**

中科数测、ETAS、BlackDuck、NXP、上海软件中心、Deloitte、奇安信、为辰信安、云驰未来、信长城、泽鹿安全、纽创信安、复旦微电子、天融信、奇虎360、中汽中心、中国汽研、上海汽检、加特兰微电子、浙江大学......

**人员占比**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJVW2JR9ib5icMR4wIs58nO6ia3OicH5l6vONnmuhfLqMKqj8T2AnD7W1vqQ/640?wx_fm...