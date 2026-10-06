---
title: 汽车安全入门 03：ECU 与 UDS 诊断服务
url: https://mp.weixin.qq.com/s/WnOH5s0-GUCVdUgvVnu-ng
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:22:56.717473
---

# 汽车安全入门 03：ECU 与 UDS 诊断服务

# 汽车安全入门 03：ECU 与 UDS 诊断服务

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PfhS7ibY53PwRhmRPQtvr42QCrLIGK3gyDNxAibdaADwYfjA5WPXthJmS3MzWBShB5xNp9E8pnNzB2ELsGNRVRS4Io4orAJIh1s/640?from=appmsg)
> **导语**：上回说到 OBD-II 那条 16 针线把诊断仪接进 CAN 总线。但 CAN 总线上跑的是帧，帧里塞什么、谁来解、按什么规则解，全是 UDS 在管。UDS 是 ISO 14229 定义的一套诊断协议栈，覆盖从读故障码、读传感器到刷写固件、跨域控制的全套操作。今天拆协议栈 + 十大核心服务 + Seed-Key 安全访问 + UDSim/UnlockECU 实战 + 红队攻击面，下一讲直接上攻击面建模。

---

## 一、ECU 不是"一台电脑"，而是一片域

现代汽车每辆搭载 70-150 个 ECU（Electronic Control Unit，电子控制单元），按域分布：

* **动力域（Powertrain）** — EMS（发动机控制单元）、TCU（变速箱控制单元）、BMS（电池管理系统，纯电/混动）
* **底盘域（Chassis）** — ABS（防抱死刹车）/ESC（车身稳定控制）/EPS（电动助力转向）
* **车身域（Body）** — BCM（车身控制单元，负责灯光/中控锁/雨刮）
* **ADAS 域（Advanced Driver Assistance Systems，高级驾驶辅助）** — 毫米波雷达控制器、摄像头控制器、域控制器
* **信息娱乐域（Infotainment）** — IVI（In-Vehicle Infotainment，车载信息娱乐系统）、T-Box（远程信息处理盒）

UDS 是这些 ECU 都认的"普通话"。Tier 1（一级供应商）不管给哪家 OEM（整车厂）供货，UDS 接口几乎必须按 ISO 14229 实现。

![ECU 与 UDS 协议栈](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6PXkice9VkuL87QzD05RulMeXtL2f067Z4ibZel7kPX8SnmslnBibQjbZLp8Ex3gnVwNGgqcVNpAImMibc6oc4dwGJkNw6A1Psj2yE/640?from=appmsg "ECU 与 UDS 协议栈")

---

## 二、UDS 协议栈：跑在 OSI 第 5-7 层

UDS 本身定义在 OSI 7 层模型的会话/表示/应用层（第 5-7 层），不关心底层物理传输。实际部署时最常见的承载方式：

* **DoCAN**（Diagnostic over CAN）— ISO 15765，主流方案
* **DoIP**（Diagnostics over Internet Protocol）— ISO 13400，车载以太网 OBD 口的标配
* **DoLIN**（Diagnostic over LIN）— ISO 17987，低速车身件
* **DoFlexRay** — ISO 17458，奔驰/BMW 部分高端车

红队做渗透时，第一步永远先确认用的是 DoCAN 还是 DoIP。DoCAN 用 11/29 位 CAN ID 寻址（一般诊断 ID 落在 0x7DF-0x7EF 这块），DoIP 直接 UDP/TCP 走车载以太网，工具链完全不同。

---

## 三、十大核心服务（必须背熟）

UDS 的每个服务用 SID（Service Identifier，服务标识符）一个字节标识。请求 SID 是奇数偏移，响应 SID 是请求 +0x40。十大高频服务：

| 请求 SID | 响应 SID | 服务名 | 用途 |
| --- | --- | --- | --- |
| 0x10 | 0x50 | DiagnosticSessionControl | 切换诊断会话（默认/扩展/编程） |
| 0x11 | 0x51 | ECUReset | ECU 软重启/硬重启 |
| 0x14 | 0x54 | ClearDiagnosticInformation | 清故障码（DTC） |
| 0x19 | 0x59 | ReadDTCInformation | 读故障码列表 |
| 0x22 | 0x62 | ReadDataByIdentifier | 按 DID 读数据 |
| 0x23 | 0x63 | ReadMemoryByAddress | 按地址读裸内存 |
| 0x27 | 0x67 | SecurityAccess | Seed-Key 安全访问 |
| 0x2E | 0x6E | WriteDataByIdentifier | 按 DID 写数据 |
| 0x29 | 0x69 | Authentication | 替代 0x27 的新机制（PKI 证书交换） |
| 0x31 | 0x71 | RoutineControl | 跑 ECU 内部例程（自检/标定/特殊动作） |

数 0x10 是"进门"，0x27 是"解锁"，0x2E 是"改值"。这三步连贯起来就是你远程调 ECU 的最短路径。

---

## 四、Negative Response Code：UDS 的错误字典

UDS 出错时 ECU 不回正常响应，而是回 `7F <SID> <NRC>` 三字节格式，NRC（Negative Response Code，负响应码）一个字节标识错误类型。最常砍到的几个：

| NRC | 名称 | 实战含义 |
| --- | --- | --- |
| 0x12 | SubFunctionNotSupported | 子功能不支持 — 目标 ECU 没实现你发的那个 sub-function |
| 0x13 | IncorrectMessageLengthOrInvalidFormat | 报文长度错 — 漏带 sub-function 字节 |
| 0x14 | ResponseTooLong | 响应太长 — 触发 ISO-TP 多帧传输（下面讲） |
| 0x22 | ConditionsNotCorrect | 条件不满足 — 比如车速不为 0 时拒绝刷写 |
| 0x24 | RequestSequenceError | 请求顺序错 — 没先 0x10 切到编程会话就发 0x27 |
| 0x31 | RequestOutOfRange | 参数越界 — DID 编号超范围 |
| 0x33 | SecurityAccessDenied | 安全访问拒绝 — 0x27 没解锁就调 0x2E |
| 0x35 | InvalidKey | Seed-Key 算错 — 算法或参数错了 |
| 0x36 | ExceededNumberOfAttempts | 超过最大尝试次数 — ECU 锁定一段时间 |
| 0x72 | GeneralProgrammingFailure | 刷写失败 — Flash 校验出错 |
| 0x78 | RequestCorrectlyReceivedResponsePending | 忙，等待中 — ECU 在算长 key，让你别急 |
| 0x7E | SubFunctionNotSupportedInActiveSession | 当前会话不支持 — 没切到 Programming Session |
| 0x7F | ServiceNotSupportedInActiveSession | 服务不支持 — 比如 Default Session 下禁止 0x2E |

红队视角下这几个最常打交道的：**0x22**（车速/电压/P 挡条件）和 **0x33**（认证失败）几乎每个项目都会遇到。0x36 触发多了 ECU 会进锁定状态，严重的直接锁死，必须拆电池或者长按某键才解得开。

---

## 五、ISO-TP：UDS 在 CAN 上的多帧传输

CAN 单帧最多 8 字节载荷（CAN FD 最多 64），UDS 一条诊断消息动辄几十上百字节。ISO 15765-2（即 ISO-TP）定义了四种帧类型解决这个：

* **单帧 SF**（Single Frame）— 第一字节低 4 位表示后续数据字节数（0-7）
* **首帧 FF**（First Frame）— 数据超过 7 字节时用，前两字节标识总长度（最大 4095 字节）
* **连续帧 CF**（Consecutive Frame）— 按 0-15 序号循环发送剩余数据
* **流控帧 FC**（Flow Control）— 接收方告诉发送方块大小（BS）和最小间隔时间（STmin）

红队做 fuzz（模糊测试）时常见坑：FF 没收完就发完 CF，ECU 直接 NRC 0x14（ResponseTooLong）把你踢出去。下一篇讲攻击面建模时会专门拆这块。

---

## 六、SecurityAccess 0x27：Seed-Key 流程拆解

UDS 的安全访问用挑战-应答（Challenge-Response）模式，规则简单：

```
Tester → ECU:  27 01              # requestSeed (sub-function = 0x01)
ECU   → Tester: 67 01 AA BB CC DD  # positiveResponse + 4 字节 seed
Tester → ECU:  27 02 XX XX XX XX  # sendKey (sub-function = 0x02) + 计算出的 key
ECU   → Tester: 67 02              # 解锁成功
```

算法藏在 ECU 里，Tester 必须算出匹配的 key 才能解锁。算法各家不同：

* **Bosch（博世）** PowertrainBoschContiSecurityAlgo1
* **Conti（大陆）** ContiSecurityAlgo
* **Delphi（德尔福）** DelphiAlgo
* **日系 OEM** 自研

Seed 长度通常 2-8 字节，Key 长度一般等于 Seed 长度。

![SecurityAccess Seed-Key 流程](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6M282v1ciby7ibTbc0ZwNUcIVqwNfESR8qSEcXG62FN1AdOGwAMTMWeYaMyN7nQ2iarygTiaGSqWbRn4ic8LR87HzH4335TU7Lw2icIM/640?from=appmsg "SecurityAccess Seed-Key 流程")

---

## 七、UDSim 实战：图形化 ECU 模拟器

UDSim（github.com/zombieCraig/UDSim）是 Craig Smith 写的 UDS 模拟器 + 模糊测试器，三种模式：

* **Learning 模式** — 监听 CAN 总线，自动学习 ECU 的 UDS 行为并保存
* **Simulation 模式** — 用学习好的配置模拟 ECU，对诊断仪做应答
* **Attack 模式** — 对目标 ECU 做主动 UDS 模糊测试

配置用纯文本 key=value，比如定义一个 0x7E0 的服务端：

```
[7e0]
pos = 300,131
responder = 1
positiveID = 7e8
negativeID = 7e8
{Packets}
7e8#0650030096177000
```

经典组合是 **ICSim（Instrument Cluster Simulator，仪表盘模拟器） + UDSim + SocketCAN（Linux 内核原生 CAN 协议栈）** 一起跑，搞个虚拟仪表盘 + 虚拟 ECU 出来，练手写 UDS 注入时不用上真车。下一篇讲攻击面建模时会用到这套环境。

---

## 八、UnlockECU：Seed-Key 不再神秘

seed-key 算法一般藏在车厂的私有 DLL 里，逆向门槛高。UnlockECU（github.com/jglim/UnlockECU）做的事很关键：把 30+ 家供应商的安全访问算法逆向实现成 C#，配上 `db.json` 数据库免去额外 DLL 依赖。

用法直接：

```
1. 从实车抓 seed（UDS 0x27 01 应答）
2. 在 UnlockECU 选 ECU 型号（如 ME97）
3. 工具自动选算法 → 算 key → 给你 UDS 0x27 02 应答帧
4. 直接用 key 解锁 ECU，进入编程会话刷写
```

实战链：caringcaribou 枚举 UDS 服务 → 抓到支持 0x27 → UnlockECU 算 key → 进入编程会话 → 刷写恶意固件。整个链路开源 + 自动化，红队视角下这是教科书级别。

---

## 九、红队攻击面：UDS 常见被砍姿势

按被砍次数排：

1. **默认开放编程会话** — 不少车的 0x10 0x02（Programming Session）默认无认证，进入后 0x34/0x36/0x37 直接刷固件
2. **Seed-Key 算法被泄露** — 供应商 DLL 反编译后 key 算法全公开，等于 0x27 形同虚设
3. **DID 误用** — 0x22 读 VIN、里程、密钥等敏感 DID 没设访问控制
4. **0x23 裸读内存** — 给个内存地址就能 dump 整个 Flash（闪存），密钥、私钥全暴露
5. **0x31 RoutineControl 滥用** — 标定/工厂测试 Routine 在售后仍开放，可改写关键参数
6. **DoIP 远程访问** — 现代车 OBD 口背后就是 DoIP 设备，攻击者远端进 CAN 就是这一步

---

## 十、思考题

* **Q1**：拿到一台车的 OBD 口，怎么在不接真实 ECU 的情况下练 UDS 注入？（提示：上文的 UDSim）
* **Q2**：如果某 ECU 的 0x27 安全访问只用 OEM 私钥签名证书，但固件可以从公开渠道下载，会有什么后果？
* **Q3**：0x31 RoutineControl 的 sub-function 0x01（Start Routine）能不能跑出 0x10 之外的会话切换？

---

## 十一、素材出处

* awesome-vehicle-security #146 UDSim：https://github.com/zombieCraig/UDSim
* awesome-vehicle-security #167 UnlockECU：https://github.com/jglim/UnlockECU
* TR22 UDS Fuzzing：https://www.youtube.com/watch?v=c\_DqxHmH7kc
* Wikipedia ISO 14229 UDS：https://en.wikipedia.org/wiki/Unified\_Diagnostic\_Services
* PortSwigger 风格 WebSocket 测试思路延伸到 UDS

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6PjHIPf1jyjZAuKCFQqkfhubaJckZrdndCzfSKKwyBf0nsEkJme3ib31bB0cvb25hOaoCrsFUpMXQ32Z3KjLwUZsiaicuraUy0gq8/640?from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6OAMy8tboafOkXDAfytbR26LBtWs9RL9JqnIcFvricpP5aU50PqVRbLIpIvWWF22soekYHIgZoplChAFFIe1sUNGqQ917QB7pU4/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621549&idx=1&sn=21c4b072726d2387d562109ada6b9bbb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6ONdek1OzyFqksQncgiay0mIKtPYYaI082SibapG5AwQL3ZsIA249rd1IscmYfOJsFog1vcIqdd9z3y9pTHwFIYDPlSt4NEudfQM/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621944&idx=1&sn=3cc6dc9876a20466d4ec3634deb80220&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6P9ZMPm72oHeeuJFraDdqT0kDbibzaqzntwCUzKtBKickr3WrkPnJyia2Kqmw7ibbJOrAf9TrEzjOkAMafDa61QQuSiba4e5FRPoiamo/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650622065&idx=1&sn=09f8ae84c06d4331e71c277b177ae701&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

内容含AI生成图片

阅读原文

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacM...