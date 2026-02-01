---
title: SerDes的TDC
url: https://mp.weixin.qq.com/s/9PN93hbszRLDN4hkW-tAgA
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:24:32.659886
---

# SerDes的TDC

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwibFl5Q9bMyzDObMT3dGsGLDWbFeeKYY2cnD4EBKchEVs5Igtq0UHpia54lnsR8bGO91PNOiaHFEibJQA/0?wx_fmt=jpeg)

# SerDes的TDC

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247568414&idx=2&sn=e8421575011428f2d73cc0b393889274&scene=21#wechat_redirect)

**01**

**TDC 是什么？**

TDC 的全称是 Time-to-Digital Converter，即时间数字转换器。

它的功能与传统的 ADC 非常相似，但测量的对象不同：

* **ADC：**将电压的模拟量转换为数字码。
* **TDC：**将时间间隔的模拟量转换为数字码。

在 SerDes 中，TDC 的核心任务是精确测量两个数字事件（通常是时钟边沿或数据边沿）之间的时间差，并以数字形式输出这个差值。

**02**

**有什么作用？**

在高速 SerDes 的接收端，TDC 扮演着“高精度时间尺”的角色，其主要作用包括：

**（1）替代传统的相位检测器：**

* 在传统的 BBPD 中，输出是一个二元信号：时钟领先或滞后于数据。
* 而 TDC 的输出是一个多比特的数字码，直接量化了时钟与数据之间的相位误差大小。这为 CDR 提供了更丰富、更精确的信息。

**（2）实现数字环路滤波器 CDR**

* 基于 TDC 的 CDR 是一种全数字化的架构。TDC 测量出的相位误差作为数字码被送入一个数字环路滤波器。
* DLF 对该误差进行滤波和处理，然后控制一个数字控制振荡器 来调整时钟相位和频率。
* 这种架构易于在先进工艺下实现，具有更好的可移植性和可配置性。

**（3）测量时钟抖动和信号完整性**

* TDC 可以用于在线监测模式，持续测量恢复时钟或输入数据的抖动特性，并将数据输出供系统分析。这对于系统诊断和健康状态监测非常有价值。

**（4）辅助其他校准**

* 在 SerDes 内部，许多模块对时序非常敏感。TDC 可以用于精确测量和校准各种路径的延迟，例如用于 DFE 抽头延迟线的校准、时钟路径的偏斜校准等。

**03**

**怎么实现？实现原理是什么？**

TDC 的实现方法多种多样，但在 SerDes 这种对面积和功耗极其敏感的应用中，最主流的方法是基于 Vernier Delay Line 的 TDC。其核心原理是利用数字逻辑门的传播延迟作为基本的时间标尺。

下面我们以 Flash TDC 和 Vernier TDC 为例，说明其实现原理。

**实现原理一：Flash TDC（直接法）**

这是最直观的方法，类似于 Flash ADC。

核心结构：一串连续的缓冲器构成一个延迟链，和一个寄存器阵列。

工作原理：

1. Start 信号（如数据边沿）注入延迟链，像波浪一样依次通过每个缓冲器。
2. Stop 信号（如时钟边沿）作为采样寄存器的触发信号。
3. 在 Stop 信号到来瞬间，寄存器会捕获到延迟链上每个节点的状态，形成一个温度计码。
4. 例子：假设 Stop 信号到来时，前 5 个缓冲器的输出为高，后面都为低，那么温度计码就是 ...11111000...。这说明 Start 信号传播到了第 5 和第 6 级缓冲器之间。
5. 这个码值经过一个编码器，就转换成了代表时间差的数字输出。

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwibFl5Q9bMyzDObMT3dGsGLD2w5AwXIsgNoVJZF4UfO0TLO8boN5leO2pja99icRKL5aF6Mib5c3SViaA/640?wx_fmt=jpeg&from=appmsg)

flash TDC工作原理

**实现原理二：Vernier TDC（游标卡尺法）**

这是最常用且能实现高分辨率的方法，其原理类似于游标卡尺。

核心结构：两条延迟链。

* Start 链：由延迟为 T\_s 的缓冲器组成。
* Stop 链：由延迟为 T\_p 的缓冲器组成。
* 关键：T\_p > T\_s。

工作原理：

1. Start 信号进入 Start 链。
2. Stop 信号进入 Stop 链，但比 Start 信号晚一段时间T\_in（这就是要测量的时间差）。
3. 由于 Stop 链的单元延迟 T\_p 更大，Stop 信号在每个阶段都会“追赶” Start 信号。
4. 在每个节点，仲裁电路（如一个D触发器）判断 Stop 信号是否追上了 Start 信号。
5. 最终，在某个节点 N，Stop 信号首次超过 Start 信号。
6. 测量的时间差为：T\_in = N \* (T\_p - T\_s)。

Vernier TDC 的工作原理与数据流如下图所示

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwibFl5Q9bMyzDObMT3dGsGLDBnbOl7epb5Ma32ibeWSGFmNBMcE0qibExLMBR2ksskJJ5apGKUTrBS3w/640?wx_fmt=jpeg&from=appmsg)

Vernier TDC工作原理

**04**

**有哪些应用场景？**

**（1）全数字 CDR**

这是 TDC 在 SerDes 中最核心的应用。基于 TDC 的 ADCDR 架构，尤其适用于需要快速锁定、低功耗和先进工艺集成的场景。

**（2）抖动测量与性能监控**

可以作为内置的测试仪器，实时测量恢复时钟的周期性抖动、随机抖动，或者分析输入数据的抖动特性，无需外部昂贵的高速示波器。

**（3）DFE 时序校准**

DFE 需要将数据延迟精确的 1 UI（单位间隔）。由于工艺、电压、温度的变化，模拟延迟线的延迟会漂移。TDC 可以精确测量这个延迟，并通过反馈环路将其锁定在准确的 1 UI。

**（4）时钟偏斜测量与校准**

在多通道 SerDes 中，TDC 可以测量不同 Lane 之间的时钟偏斜，并为主动偏斜校准电路提供误差信息。

**（5）更广泛的半导体应用**

* 激光雷达：通过测量激光飞行时间来计算距离。
* 粒子成像：用于捕捉高能物理实验中的事件时间。
* 高精度时钟发生器：用于锁相环和时钟同步。

**05**

**总结**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9TwibFl5Q9bMyzDObMT3dGsGLDDwebZFOINe426HrGQM9sbyNhFn6kMBXH5lpGPPSeoOibGc4Ms5Gf3fQ/640?wx_fmt=jpeg&from=appmsg)

TDC 代表了 SerDes 技术向全数字化、高度集成化发展的重要趋势，它将模拟世界中最难控制的“时间”参数，转化为了易于处理的数字信号，极大地增强了系统的智能化和可靠性。

来源：知乎@yueleyue

https://zhuanlan.zhihu.com/p/1969328429297041851

谈思-汽车出海安全合规（欧洲）

交流群

谈思 AutoSec Europe 峰会旨在搭建一个能融汇全球视野与中国实践、连接技术前沿与落地应用的国际性专业平台，以助力中国汽车应对在出海过程中面临的网络与数据安全合规痛点。从前沿技术研讨、合规要点解析到经验交流，都将通过本平台为您提供持续支持。社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibTH2iaYqMA6sf7DgCTTHwEaAvzywYkvdmgUK1SGVhE9yFHl4kVTARp5M5LiaVIM6WcG0PcXYsZZEbQ/640?wx_fmt=png&from=appmsg)

谈思-SDV&AIDV技术出海

交流群

诚邀行业同仁加入谈思SDV&AIDV出海技术交流群，聚焦软件定义汽车、AI定义汽车、下一代EEA、智能座舱、智能驾驶、软件架构、域控制器开发、芯片技术、软件工具等核心议题，欢迎大家加群交流探讨~~社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9c00NyPNPSRjUzbpUxiaFiakfz8AEVJkxCmGicv14KyKqgPM8H649icFnmroPiaR6UvNSZwhCrN3T3UYg/640?wx_fmt=png&from=appmsg)

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicHdaQsibvoH8dLYIIcT5YQibwbnuZn1MLCOMydw2SMKWbibsLpooeE2jgCt8FABvsVmlJZO5PO00Ryw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561756&idx=2&sn=f9b8c214978537f47cccba736cdb5bfd&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563394&idx=2&sn=ed98964862cf2f8280a4d6db9cd0a273&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDj35QtelfANiaT02jEgnILSunGiau3UuDTOv2qX6O4hhDic8KG4o42ibTJBQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563583&idx=2&sn=c73d1a26f0b229d865acaf1cade3c761&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247557132&idx=2&sn=2e44d4c2d77a2eec377d0553442d2c1b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561775&idx=1&sn=948a9e7f8d4fbed363c6a6a5479cd39e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkfxA4GZice84BsCR4zGV0oqJXpEjUsUpGKcFcCx1BiaDYDQU4cT3nTtpA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561260&idx=2&sn=0ca6395502487515a921f32288b7e8df&scene=21#wechat_redirect)

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

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJVW2JR9ib5icMR4wIs58nO6ia3OicH5l6vONnmuhfLqMKqj8T2AnD7W1vqQ/640?wx_fmt=png&from=appmsg)

**公司类型占比**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJU6yKtYSJu4oPaJABYuCSyTpLXjRNbVv7OUTUUCxmB1OuPhtcM4j1kw/640?wx_fmt=png&from=appm...