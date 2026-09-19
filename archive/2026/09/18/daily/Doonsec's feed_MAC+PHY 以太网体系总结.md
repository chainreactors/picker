---
title: MAC+PHY 以太网体系总结
url: https://mp.weixin.qq.com/s/IYNFszOPs-lPKn0hGT3n7A
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:53:29.290507
---

# MAC+PHY 以太网体系总结

# MAC+PHY 以太网体系总结

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

**01**

**核心总纲**

以太网通信的核心架构为MAC（数据链路层）+PHY（物理层）分层协同\*\*\*\*工作机制，二者职责严格解耦、上下联动配合，缺一不可。MAC负责数字帧协议处理与数据调度，PHY负责物理信号编解码与线路传输；通过标准化业务接口与管理总线完成交互适配，保障网络数据稳定收发。业界所有以太网硬件落地方案，均基于该标准分层架构衍生，可适配不同传输速率、应用场景与量产需求。

**02**

**分层架构与核心职责**

**2.1 上层：MAC 层（OSI-L2 数据链路层）**

定位：纯数字逻辑、片内集成、负责“数据内容”，不感知物理信号特性。

核心职责：帧封装/解封装、CRC校验、地址过滤、DMA数据搬运、流量控制、寄存器配置与中断管理，实现合规、安全、高效的数字数据包交互。

**2.2 下层：PHY 层（OSI-L1 物理层）**

定位：数模混合、多为外置独立芯片、负责“信号传输”，不解析数据包协议内容。

核心职责：数据编解码、串并转换、时钟恢复、差分信号驱动、链路自动协商、线路信号均衡与故障检测，为MAC提供稳定的物理传输通道。

**2.3 中间联动层（二者交互桥梁）**

业务通道：RGMII/GMII/RMII/MII 并行数据接口，传输收发业务帧；管理通道：MDIO/MDC 管理总线，实现MAC配置PHY、读取链路状态，完成速率/双工模式同步。

**03**

**底层细节落地（模块机制+工作流程，支撑上层论点）**

**3.1 MAC 核心内部模块（保障数字链路可靠性）**

整体分为发送通路、接收通路、公共控制模块三部分，形成完整数据闭环：

* TX发送通路：DMA取数→TX FIFO跨时钟域缓存→帧组装（帧头/填充/VLAN）→CRC32校验生成→并行数据输出，支持Pause帧限流、半双工冲突避让
* RX接收通路：接口数据采样→前导码剥离→CRC校验、帧合规检测→MAC地址硬件过滤→RX FIFO缓存→DMA搬运至内存，异常帧直接丢弃，降低CPU负载
* 公共控制模块：APB寄存器配置、中断控制器、链路状态同步、低功耗管理、多时钟域同步复位逻辑

**3.2 PHY 核心内部模块（保障物理传输稳定性）**

* PCS编码子层：完成8b/10b、曼彻斯特编解码，适配网线传输特性
* PMA物理子层：串并转换、CDR时钟恢复、信号均衡、差分电平驱动，解决长线传输衰减与偏移问题
* 自动协商模块：与对端PHY协商最优速率、双工模式，同步状态给MAC
* MDIO管理模块：响应MAC读写指令，上报链路状态、误码统计、硬件故障信息

**3.3 完整协同工作流程**

* 发包流程：CPU/DDR数据→MAC组帧校验→RGMII并行输出→PHY编解码+差分驱动→网线传输至对端
* 收包流程：网线差分信号→PHY整形解码→并行数据送入MAC→MAC校验过滤→DMA落内存→CPU中断处理

**3.4 核心工作模式**

* 全双工：收发独立通道，无冲突，主流设备默认模式，传输效率最高
* 半双工：单信道分时复用，启用CSMA/CD冲突避让，仅老旧设备使用

**04**

**主流硬件落地方案**

基于标准MAC+PHY分层架构，业界衍生出三类成熟的商用落地方案，分别适配低速量产、定制开发、高速骨干传输三大核心应用场景，覆盖绝大多数以太网工程需求。

**4.1 方案一：SoC片内MAC + 外置分立PHY（10M/100M/1G）**

定位：工业、车载、消费电子量产主流方案

优势：成本低、时序易收敛、温区适配广、维修替换方便、功耗低、架构成熟稳定

劣势：占用PCB面积大、并行接口布线有约束、速率上限仅千兆、多网口拓展繁琐

**系统详细框图（架构流向）**

CPU/片上总线(AHB/AXI) → APB配置总线 → MAC寄存器模块CPU/DDR内存 → MAC内置DMA → MAC TX/RX FIFO → MAC帧处理模块MAC数字接口（RGMII/RMII/GMII）→ 外置PHY芯片 → RJ45网口 → 双绞线链路MAC MDIO/MDC管理总线 → PHY寄存器（链路协商/状态上报）

框图说明：整体分为芯片内数字域、板级外设模拟域两级架构，数字业务与物理信号完全隔离，MAC负责所有协议与数据调度，外置PHY独立完成信号适配，是目前最成熟的千兆以内以太网硬件架构。

**4.2 方案二：FPGA硬核MAC + 外置分立PHY（10M/100M/1G）**

定位：研发调试、工业控制、自定义协议柔性方案

优势：可编程性强、支持多网口扩展、可定制TSN/EtherCAT等工业协议、迭代灵活

劣势：成本高、功耗大、时序调试复杂、不适合大批量量产

**系统详细框图（架构流向）**

FPGA内部逻辑资源 → 自定义用户协议层（TSN/EtherCAT/自定义帧处理）→ FPGA内置硬核MAC → MAC FIFO/DMA模块 → RGMII并行接口→ 板载外置PHY芯片 → RJ45网口 → 外部网络链路FPGA内部逻辑 → MDIO管理时序 → PHY链路配置与状态采集反馈

框图说明：在标准MAC-PHY架构基础上，增加可编程自定义逻辑层，可灵活改造帧格式、时序逻辑与工业协议，硬件底层仍依赖外置PHY完成物理传输，兼顾灵活性与物理兼容性。

**4.3 方案三：片内MAC+SERDES集成，无外置PHY（10G/25G+高速）**

定位：数据中心、服务器、5G基站高速骨干方案

优势：集成度极高、布线极简、传输距离远、超大带宽、无外置PHY器件损耗

劣势：流片与设计成本极高、高速信号SI/PI设计难度大、功耗高、仅适配高端场景

**系统详细框图（架构流向）**

SoC/NPU/网络处理器内部总线 → 高速MAC控制器 → PCS编解码子层 → PMA串行收发模块→ 片内SERDES高速差分通道 → SFP/SFP+光模块 → 光纤高速传输链路（无外置PHY芯片，PHY层所有功能全部集成在芯片硬核内部）

框图说明：高速架构彻底取消分立PHY器件，将传统PHY的PCS/PMA物理层功能全部集成至芯片内部，以高速串行SERDES替代并行RGMII接口，大幅提升带宽与传输距离，适配10G及以上高速网络场景。

**05**

**核心技术总结**

1.分层解耦是架构核心：MAC专注数字逻辑与协议处理，PHY专注物理信号传输，二者职责边界清晰，是以太网通信稳定、通用、可移植的根本保障；

2.双向联动是运行关键：业务数据通道负责帧数据传输，MDIO管理通道负责链路状态配置与同步，软硬件协同实现链路自适应、速率双工匹配；

3.场景适配是选型核心：工业消费量产场景选用SoC内置MAC+外置PHY方案，定制协议开发选用FPGA硬核MAC方案，高速数据中心场景选用片内SERDES集成架构，三类方案可完整覆盖全速率以太网应用需求。

来源：可乐验证圈

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA7BGa1vwHmHNlluBv83nX42cOwngUmsgRicQ6oyhxN3HmOsFIml2sUM8Yibk5GELQqiaFLt2dVzmf01r90xrW0vMWGpJX7zOsmkM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247575659&idx=3&sn=1b3acb3a33e0fc992b67b37bc4d04a0e&scene=21#wechat_redirect)

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

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJU6yKtYSJu4oPaJABYuCSyTpLXjRNbVv7OUTUUCxmB1OuPhtcM4j1kw/640?wx_fmt=png&from=appmsg)

**文章**

# [不要错过哦，这可能是汽车网络安全产业最大的专属社区！](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&chksm=e9270eacde5087bacb4d9c888f3a21ceae227156c89aba0be7d9ebc8b02a68b4f11e7595255a&scene=21#wechat_redirect)

[关于涉嫌仿冒AutoSec会议品牌的律师声明](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247531034&idx=2&sn=e466ca3e7c2927a91dd9a81be705afe1&chksm=e9273ec1de50b7d7f540ae2e4c255bfb42f842228a87f7dbc65297027a878544a9e796e09cf6&scene=21#wechat_redirect)

[一文带你了解智能汽车车载网络通信安全架构](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247517280&idx=2&sn=8bfafb17871598c9cc0041bc9ee5f65d&chksm=e927c0bbde5049ad8cdb3647f6cdfce00c2db7a7b484941027bb7edf3128e4eaa74d6727dd46&scene=21#wechat_redirect)

[网络安全：TARA方法、工具与案例](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247502093&idx=1&sn=ec4b373a33ca04d79afbb0b0b880bd4e&chksm=e9278dd6de5004c01bdd83ad0dd89c3549c7ae2ceb362959dbcb159324b2593d70bce78d82a9&scene=21#wechat_redirect)

[汽车数据安全合规重点分析](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247519068&idx=1&sn=78c66e13bd8798afd46c766b8f18abe7&chksm=e927cf87de504691c816f78b55daf93bdfb72fc1cb870d926de8b471eb3e1be61058498327b1&scene=21#wechat_redirect)

[浅析汽车芯片信息安全之安全启动](http://mp.weixin....