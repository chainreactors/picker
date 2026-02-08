---
title: 基于特斯拉联网汽车LTE连接安全分析
url: https://mp.weixin.qq.com/s/eXZARVSSb_CxViEuWUkYHg
source: Doonsec's feed
date: 2026-02-07
fetch_date: 2026-02-08T04:29:51.757493
---

# 基于特斯拉联网汽车LTE连接安全分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qfVK35GYW1vlvVrQnJNIX3RILoBbLo8pwFibThJdF9HkYxR7FiaXD4aXHC8nZuZrSEOjYxDJ3EWF6u6J7Wq5GwmQ/0?wx_fmt=jpeg)

# 基于特斯拉联网汽车LTE连接安全分析

原创

Yang
Yang

AI+网络安全笔记

![]()

在小说阅读器中沉浸阅读

参考来源：《Security Analysis of LTE Connectivity in Connected Cars: A Case Study of Tesla》

链接: https://pan.baidu.com/s/17loSTtxWdqO1L2BOYx-GmQ 提取码: wd4y

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qfVK35GYW1vlvVrQnJNIX3RILoBbLo8pjsIVEHW2SgYfN9FUpkb9eG7j922ib0eygmwaN7OvQWxgNlBkxfEibQiag/640?wx_fmt=jpeg&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qfVK35GYW1vlvVrQnJNIX3RILoBbLo8peJzbpvmPbYrTmudnzUoUibkWnDlSPaibXEfFVOhic3xs10QAgQe5EtEyw/640?wx_fmt=jpeg&from=appmsg)

信令流：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qfVK35GYW1vlvVrQnJNIX3RILoBbLo8pB0o1XfNaf2o9K7eNXujYiawYf28iabzSaSIlRbPnQkx3VI8IfmVc1MuQ/640?wx_fmt=jpeg&from=appmsg)

这篇论文对联网汽车的 LTE 连接进行了全面的安全分析，并以特斯拉汽车（Model 3 和 Cybertruck）作为案例研究。研究强调，现代联网汽车严重依赖持久的 LTE 连接来实现关键功能，但在这种安全关键领域，移动网络漏洞的安全影响仍未得到充分研究。

作者使用自定义的 LTE 实验环境进行了一项黑盒、非侵入式的安全评估。他们的主要发现揭示了特斯拉车载信息系统存在一些系统性的弱点和架构上的错误配置：

易受 IMSI 捕获攻击： 特斯拉汽车容易受到 IMSI 捕获攻击。当车载信息控制单元 (TCU) 暴露在广播合法公共陆地移动网络 (PLMN) 标识符的恶意基站（rogue base station）下时，可能会泄露其国际移动用户标识 (IMSI) 和临时移动用户标识 (GUTI)。与智能手机不同，汽车缺乏用户可见的控制或通知功能来阻止或检测此攻击，这使得车辆特别容易受到攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qfVK35GYW1vlvVrQnJNIX3RILoBbLo8piaO9j2FsF1IibVDlzcCzEHPVGldnGhqscwy8geHBReCwvX2d7uthyGlw/640?wx_fmt=jpeg&from=appmsg)

恶意基站（假基站）攻击： 车辆容易连接到恶意基站。攻击者通过伪造运营商信息并使用增强的信号强度，可以诱骗 TCU 连接到未经授权的 LTE 网络，从而导致部分或完全连接状态。这可能通过阻止访问后端服务来造成拒绝服务 (DoS) 状况，并为进一步的攻击打开大门。

回落和部分状态缺陷： TCU 对网络状况不佳的应对能力很差。当遇到控制平面拒绝或 PDN 连接失败时，它会持续进入重复的重连循环。至关重要的是，它不会切换到备用连接选项（如 eSIM 配置文件或 Wi-Fi），这会导致服务中断时间延长并增加漏洞风险。

宽松的 PLMN 强制和白名单策略：TCU 的网络选择过程非常宽松。在初始连接阶段，它会接受来自各种 PLMN 的连接，包括测试和任意标识符，然后才进行严格的过滤。数据网络服务激活期间发生的二次过滤不足以阻止初始连接到不受信任的基础设施。

控制平面和参数错误配置： 虽然基本的连接过程符合标准，但 TCU 却宣称支持旧版 2G/GSM 服务和弱加密算法（例如 A5/3、GEA3、空加密 EEA0）。这增加了攻击面，并增加了遭受降级攻击和被动窃听的风险。

静默 SMS 和紧急消息处理： TCU会静默地接受和处理 SMS 消息以及紧急广播（ETWS/CMAS），而不会向用户显示任何通知。这种不透明性会产生用户不可见的隐藏处理路径，使其容易受到恶意 SMS 有效载荷或伪造的紧急警报的利用。这也引发了可能过滤掉合法紧急警报的担忧。

该论文还讨论了这些发现更广泛的影响，特别是对符合联合国法规 R155（网络安全）和 R156（OTA 更新）的要求。已识别的漏洞直接与安全通信、弹性、身份保护、可审计的 OTA 交付和用户意识的要求相冲突。作者强调，这些问题是系统性的，因为特斯拉的调制解调器依赖第三方组件（Qualcomm、Quectel），这表明其他使用相同硬件的汽车制造商可能存在类似的漏洞。

最后，论文提出了缓解策略，包括在确认信任的 PLMN 之前抑制永久标识符传输、实施更严格的 PLMN 白名单、改进带有随机计时器和健康监控的回落机制、禁用旧版协议和弱加密、以及使SMS 和紧急警报的处理更加透明和安全。

总而言之，该论文证明了尽管联网汽车技术取得了进步，但基本的蜂窝网络层漏洞仍然存在，并且可能在汽车领域产生重大的安全和安保后果，对现有的监管框架提出了挑战。

回落和部分状态缺陷 (Fallback and Partial States Flaws)

这一部分关注的是车辆的遥测单元 (TCU) 在面对网络连接不稳定、失败或出现异常时的反应。论文指出，TCU 的回落机制（fallback mechanism）存在严重缺陷，导致其在网络故障时表现不佳，增加了服务的不可用性和安全风险。

核心问题：

僵化的重连循环： 当 TCU 遭遇控制平面（Control Plane）拒绝（例如，“PLMN 不允许”、“EPS 服务不允许”、“APN 缺失或未知”、“MAC 失败”等标准 NAS 错误码）时，它会陷入一种“重连循环”。具体来说，TCU 会反复尝试连接，通常会进行五次或更多次的连续尝试，然后才停止或暂时进入空闲状态。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qfVK35GYW1vlvVrQnJNIX3RILoBbLo8pLwbdCs0pgBPQyYljZ9d88xkIJZzDku1XGV8xibDRpibw5tqLYVhukHTA/640?wx_fmt=jpeg&from=appmsg)

缺乏备用连接选项： 在这些重连尝试中，论文强调 TCU 从未 切换到其他可用的连接选项，例如备用 SIM 卡（eSIM 配置文件）或Wi-Fi。这与现代智能手机通常具备的更灵活的回落策略形成鲜明对比。

缺乏动态回落和恢复策略： TCU 的重连行为是“确定性的”，这意味着它没有采用随机的退避（backoff）或恢复策略来打破僵局。它只是机械地重复相同的失败尝试。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qfVK35GYW1vlvVrQnJNIX3RILoBbLo8phtPic53KdgdLLgbN8YPNZn4s4W6ZfxDP3mAg4oo1LYnHdpoCmGmGJRg/640?wx_fmt=jpeg&from=appmsg)

数据平面故障下的部分连接状态： 即使在数据平面（Data Plane）出现故障时，TCU 的表现也很糟糕。例如，当核心网络配置为触发 PDN（Packet Data Network）连接失败（如“未知 PDN 类型”、“仅允许 IPv4”等）时， TCU 尽管成功完成了网络附加 (attach) 程序，但却停留在“部分连接”状态。在这种状态下，它会驻留在网络上，但无法获得 IP 地址或建立数据传输通道。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qfVK35GYW1vlvVrQnJNIX3RILoBbLo8pvO5Qqe86UibKvbgGKyZ9dPmmqfl5s1X85jeuzGjwQTQDRDUicM9C96vA/640?wx_fmt=jpeg&from=appmsg)

对数据中断缺乏感知： 即使在数据通信完全中断（例如，网络路由配置错误导致所有上行流量被阻止）的情况下， TCU 也不会终止会话、尝试重新连接到其他网络或回落到 Wi-Fi。它会无限期地保持这种“有效数据通信中断”的状态。

对后端服务失败缺乏响应： 论文提到，如果 TCU 无法联系到特斯拉的后端服务（例如，通过 HTTPS 请求），尽管它会继续发送请求，但由于没有响应，它也不会采取任何行动来终止会话、重连或回落。

控制平面和参数错误配置 (Control-Plane and Parameter Misconfigurations)

这一部分深入探讨了 LTE 网络通信的“控制平面”，即负责建立、管理和维护网络连接的信令交换。论文在此发现了与安全相关的错误配置，主要集中在对旧协议和弱安全参数的支持上。

**核心问题：**

对旧版/遗留协议的支持（Legacy Support）：

TCU 报告支持 2G/GSM 服务，并且在 Mobile Station Classmark 2 和 MS Network Capability 字段中显示支持旧的加密算法，如 GSM 的 A5/3 和 GPRS 的GEA2/3。这些算法在现代标准下被认为是加密学上过时的，容易被破解。

TCU 还声明完全支持通过多种信道（包括专用的、SRVCC 至 GERAN 的以及分组交换 GPRS 信令通道）的移动终端到点 SMS。

对弱加密算法的支持（Null Ciphering）：

TCU 宣称支持多种加密和完整性保护算法，其中包括 空加密 (null ciphering)，即 EEA0（Evolved Encryption Algorithm 0）。虽然 3GPP 标准允许 EEA0，但它本不应在标准网络协商中被优先使用，因为它不提供任何加密保护。

尽管 TCU 拒绝 EIA0（空完整性保护），表明完整性保护被强制执行，但其对 EEA0 的支持仍然是一个安全隐患。

缺乏透明度和对底层协议的深度检查： 论文指出，虽然 TCU 在标准配置下表现符合 LTE 设备行为，但其对旧协议和弱密码套件的支持，以及缺乏对其内部状态的透明度，极大地扩大了其攻击面。论文提到，由于缺乏更深入的协议修改或模糊测试（fuzzing）能力，无法完全排除其在更深层次的协议处理上存在其他漏洞。

静默 SMS 和紧急消息处理(Silent SMS and Emergency Issues)

这一部分研究了特斯拉 TCU 如何处理SMS（短消息服务）和紧急广播消息，以及这些处理方式带来的安全风险。

**核心问题：**

用户界面不可见：

紧急警报 (ETWS/CMAS)： 论文测试了广播 ETWS/CMAS（地震和海啸预警系统/商业移动警报系统）消息。 TCU 成功接收并确认 了这些消息，但 没有在用户界面上显示任何提示或发出声音警告，无论使用 eSIM 还是物理 SIM 卡，也无论消息是正常还是伪造的。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qfVK35GYW1vlvVrQnJNIX3RILoBbLo8prsxgaglqs0PibwX0NONnbDnhibxr3gkkeOpqyWy7VhJxTTRWz8QfzzKQ/640?wx_fmt=jpeg&from=appmsg)

直接 SMS 注入： TCU 能够接收并确认文本 SMS 消息的送达，但同样 不会在特斯拉界面上显示任何视觉提示。

静默处理机制： 这种用户界面不可见的行为表明，TCU 可能在调制解调器（modem）或中间件层面静默处理这些消息，而不会将它们呈现给用户。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qfVK35GYW1vlvVrQnJNIX3RILoBbLo8pKJibOUUFIonv5DiawbiaS7eCPvAytlLp2HicIkSqsjAMeCIL5NGqgn8zBg/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/qfVK35GYW1tJicdibPHYmh8KWdR5icMYeibRkrWdc1DPLXQhhLiaurSFm9yqo5KDBFjyvbocf3zuLjK9pTQbWLVIH4A/0?wx_fmt=png)

AI+网络安全笔记

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/qfVK35GYW1tJicdibPHYmh8KWdR5icMYeibRkrWdc1DPLXQhhLiaurSFm9yqo5KDBFjyvbocf3zuLjK9pTQbWLVIH4A/0?wx_fmt=png)

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