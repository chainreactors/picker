---
title: 汽车安全入门04_攻击面建模：从物理接触到远程
url: https://mp.weixin.qq.com/s/izCKxjttAR9Z-NsCiz903Q
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:54:12.418981
---

# 汽车安全入门04_攻击面建模：从物理接触到远程

# 汽车安全入门04\_攻击面建模：从物理接触到远程

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6O3eEzvdjBLDUVbviaExUmiblfHpQCKv4bWeBbRcTrlUyH0pYg2icjjCsaeBDRWKwcTzBoSVHspJjND9qTT4l7U2T7ibWNyHShrz54/640?from=appmsg)
> **导语**：拿到一辆车，先别急着接 CAN。Cocoa Beach 黑客会议那一对搭档 Charlie Miller 和 Chris Valasek 早在 2014 年就告诉你——汽车攻击面是一张可建模的图。本文基于他们的论文《A Survey of Remote Automotive Attack Surfaces》，把这张图展开成红队能直接照着打的实战地图。

---

## 一、三阶段攻击解剖

Miller 和 Valasek 把现代汽车的远程攻击拆成 3 个阶段，这是攻击面建模的第一根柱子：

**阶段 1 — 远程攻陷某个 ECU**：利用无线接口（蓝牙、蜂窝、Wi-Fi、RKE、TPMS 等）拿到车内某个 ECU 的代码执行权限。这阶段只要让一个"听外面信号"的 ECU 失守即可。

**阶段 2 — 把消息搬到 CAN 上**：失陷的 ECU 通常不能直接控制刹车/转向，因为这些"安全关键 ECU"往往在另一条 CAN 网络上。攻击者必须**穿越网关**——要么欺骗网关，要么再攻陷网关一次。

**阶段 3 — 让目标 ECU 做危险动作**：向安全关键 ECU 注入精心构造的 CAN 帧，触发物理动作（刹车、转向、油门）。这一步要靠**逆向工程** CAN 数据，每个厂家都不一样。

这套三阶段模型的红队意义：评估一辆车的"远程沦陷难度"，等于把 3 个阶段分别打分，再加起来。第一阶段看无线接口数量，第二阶段看网关隔离强度，第三阶段看 ECU 是否愿意听从 CAN 帧。

![三阶段攻击链路](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6N1k1CwSEynF8wpPoRsFMl2dGbp127aQbAibUu6KJPE90WTkoFziahsBCvxnRBcEM4yzm7UVUAkxnFpSxVhz9BTjvvrsYIew8DV8/640?from=appmsg "三阶段攻击链路")

---

## 二、6 大远程攻击面

论文把现代汽车能接收的"外面信号"分成 6 类，按距离排开：

### 2.1 PATS — 被动防盗系统（< 10 cm）

钥匙里的小芯片和转向柱上的传感器用 RF（射频）通信，必须在 10 cm 内。攻击面小，但能做的事也很窄——基本上只能干扰启动，远程 RCE（远程代码执行）几乎不可能。

### 2.2 TPMS — 胎压监测系统（~ 1 m）

每个轮胎的压力传感器周期性发 RF 数据给 SJB（智能接线盒）。研究表明 TPMS 信号能被干扰甚至**远程变砖**，但攻击面小，且多数车型 TPMS 只控制仪表盘灯，不连 CAN。

### 2.3 RKE — 远程钥匙进入/启动（5-20 m）

钥匙扣发出加密信号，ECU 解密后决定开锁/启动。攻击面中等——研究过 Rolling Code（滚动码）漏洞的人都知道，这里能做**重放攻击**和**拒绝服务**，但 RCE（远程代码执行）面依旧小。

### 2.4 蓝牙（10 m+，部分协议更远）

论文视此为**现代汽车最大威胁面**。原因：协议栈复杂、数据丰富、几乎每辆车都有。2010 年华盛顿/UCSD 研究员通过蓝牙栈拿到 telematics（远程信息处理）ECU 代码执行权限——这是学术圈第一次走通整车入侵。

两种攻击场景：

* **未配对时**：任何人能接触到，蓝牙栈崩溃/溢出即 RCE。
* **已配对时**：需要用户配合，威胁较低。

### 2.5 RDS — 无线数据系统（~100 m）

FM/AM 收音机附带的数据广播，必须解析才能显示电台名/歌名。理论攻击面存在，但 Miller/Valasek 认为威胁比蓝牙低得多。

### 2.6 Telematics（远程信息处理）/蜂窝/Wi-Fi（城市级）

**远程攻击的圣杯**——OnStar（通用安吉星）、Safety Connect（丰田）这类远程信息处理系统通过蜂窝网络和车对话。范围广，能完全控制 ECU，并能通过麦克风监听车内对话。

研究历史：华盛顿/UCSD 团队曾**无需用户交互**远程攻陷 telematics ECU。

### 2.7 互联网/Apps（全球）

2014 款 Jeep Cherokee 自带 Wi-Fi 热点，论文里直接 nmap 扫出开放端口 2021、6667。这块打开了一个全新的攻击面——浏览器漏洞、恶意 App、互联网服务漏洞。论文判断这是 2014 年之后增长最快的入口。

---

## 三、信息物理特性放大器

仅有攻击面还不够。有些车天生就**容易被远程打**——它们装了一堆"电脑自动控制物理动作"的功能，攻击者只要把伪造的 CAN 帧灌进去，车就会主动执行。

论文列出 4 大放大器：

| 特性 | 物理动作 | 攻击意义 |
| --- | --- | --- |
| 自动泊车 | 方向盘低速自动转向 | 方向盘 ECU 听 CAN 帧，可被诱导 |
| 自适应巡航控制（ACC） | 高速刹车/加速 | 制动 ECU 听 CAN 帧 |
| 碰撞预防 | 高速自动刹车 | 制动 ECU 听 CAN 帧 |
| 车道保持 | 高速小幅转向 | 转向 ECU 听 CAN 帧 |

注意：这些特性通常带安全机制（例如泊车只在低速生效），但有这些特性的车确实比没的车更容易打。

---

## 四、网络架构：网关隔离是核心

论文的核心贡献之一：列出 21 款车的内部网络架构，看 ECU 之间隔了几层。

关键判据：

* **无线入口 ECU 在哪条总线**（是否在动力 CAN 上）
* **网关 ECU 是否被保护**（是否能被攻陷）
* **安全关键 ECU 在哪条总线**（是否与无线入口 ECU 同总线）

红队最爱：无线入口和动力 ECU 在同一条总线 + 网关没有鉴权 = 第一阶段直接打穿到第三阶段。论文里 2014 款 Jeep Cherokee 就是这个例子，**被评为最易被远程攻击的车**。

最难打的：无线入口 ECU 和安全关键 ECU 分得很开 + 网关有强鉴权 + 没有信息物理特性放大器。论文里 2014 款 Dodge Viper 排第一难。

---

## 五、红队实战：从远程到刹车的 5 步走

把论文模型落到实战，就是 5 步：

1. **资产测绘**：拿到目标车型年份，定位无线入口 ECU 和它所在总线。
2. **入口选择**：从蓝牙/蜂窝/Wi-Fi 中挑攻击面最大的入口，先做 fuzz（模糊测试）。
3. **第一阶段突破**：拿到 telematics/蓝牙 ECU 的 shell。
4. **第二阶段穿越**：通过网关（必要时再攻陷网关）把消息搬到动力 CAN。
5. **第三阶段注入**：逆向工程目标动作对应的 CAN 帧格式，注入触发。

第 05 讲会拆每一步的工具——CANtact、Macchina M2、HackRF 怎么配，SocketCAN 怎么用。

---

## 六、防御纵深：CAN 注入检测

论文最后一章给的防御建议里，最适合立刻落地的是**CAN 注入检测**。理由：

* 已知 CAN 注入攻击只有两种模式：**UDS（统一诊断服务）诊断帧** 或 **正常帧超高频率发送**。
* 正常帧注入必须 20-100 倍频率才能压过原 ECU，这模式太显眼。
* 汽车总线高度规律，没有人类交互，行为异常极易识别。

Miller/Valasek 自己做了一个 OBD-II 小设备，学习正常流量，检测到异常直接短路 CAN 总线。这种 IDS（入侵检测系统）装置现在很多车型已经预装，是 ROAD 数据集（自动驾驶研究常用的真实道路数据集）这类研究的方向。

---

## 七、思考题

1. 你手上的目标车（比如 2018 款某车型），6 大远程攻击面里实际开放了几个？怎么验证？
2. 如果只允许你阻断一条无线入口，你会选哪条？为什么？
3. 给出 2014 款 Jeep Cherokee 和 2024 款同厂商纯电车的攻击面对比——你会怎么打分？

下讲第 05 讲《硬件选型：CANtact / Macchina / HackRF》，把这套模型落到工具上——你买什么硬件、配什么软件，能直接复现本文的 5 步走。

---

## 素材出处

* A Survey of Remote Automotive Attack Surfaces — Miller & Valasek, Black Hat 2014
* Koscher et al. Experimental Security Analysis of a Modern Automobile, 2010
* awesome-vehicle-security 列表 #31 / #54 / #59

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OvJccxcPY7uHYqRq3SdAjgJaLu5eueIm5a0K70g3u0t8NhdmzGTRhzw9icX0bAk2YujLibnjKVClS2pdFO4RmYA096XLBQVSjgg/640?from=appmsg)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6N0vXSHeHbE91aXG33aOB8RvBgJAkSHicMnbkGk9Ila66Sw7dds3cpe326wq4fQyWw0An50peRum7YvDXC9h4GKYgkb05Xzpec0/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621549&idx=1&sn=21c4b072726d2387d562109ada6b9bbb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6Pl8jAcm1WjHPzibkblNAA7dL8DJicicBFrTED1sTuplFzx9lAP7IIQFvZicPfToqxo8A08TibFulB25a04ZA4S0fSmI83SMWTzJQA8/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621944&idx=1&sn=3cc6dc9876a20466d4ec3634deb80220&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6NvMLlegdl20ibaWSAPG3srMaSu73eKuVjgZbXnPBzSRlow5iaEpCEUqPQRa2JGib3JJ2rAb5cicjUT4g7Oev9KXYZTZvDRkib64jzk/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650622065&idx=1&sn=09f8ae84c06d4331e71c277b177ae701&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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