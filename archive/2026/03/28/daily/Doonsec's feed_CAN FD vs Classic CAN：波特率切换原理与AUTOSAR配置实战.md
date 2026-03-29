---
title: CAN FD vs Classic CAN：波特率切换原理与AUTOSAR配置实战
url: https://mp.weixin.qq.com/s/vAZt-3mUFFcopbpdsYiqiw
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:33:28.466198
---

# CAN FD vs Classic CAN：波特率切换原理与AUTOSAR配置实战

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaBhEnicePQ29dSXaAzjfRsmf9XnjvmTZsYKErvib2zfmJrV5GLU2Zg6LwKaQ7XfBwsnibibkergmXo4smgKHkIaw3qLV96Bmym4FSc/0?wx_fmt=jpeg)

# CAN FD vs Classic CAN：波特率切换原理与AUTOSAR配置实战

谈思实验室

![]()

在小说阅读器中沉浸阅读

以下文章来源于ADAS与ECU之吾见
，作者汽车小T8

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4mITm28LeJNDb9ibicibZHxS4Yz0cWz0pqvDbQ53Ovl1bPg/0)

**ADAS与ECU之吾见**
.

汽车小T，实战干货，不容错过！

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247568414&idx=2&sn=e8421575011428f2d73cc0b393889274&scene=21#wechat_redirect)

**01**

**Classic CAN vs CAN FD：速率的本质差异**

**Classic CAN的速率上限**

Classic CAN全程只有一个波特率，最高1Mbps。这个上限不是随便定的，是由总线物理特性决定的：

波特率越高，位时间越短，信号在总线上传播的时间占位时间的比例就越大。当总线长度固定时，传播延迟会限制最高可用波特率。1Mbps对应1μs位时间，已经是Classic CAN在合理总线长度下的极限。

**CAN FD的双波特率设计**

CAN FD（CAN with Flexible Data-rate）的核心创新就是两段式波特率：

**仲裁段（Arbitration Phase）**

沿用Classic CAN的低速率（通常500Kbps），所有节点参与仲裁，保证总线访问的确定性

**数据段（Data Phase）**

仲裁赢了之后切换到高速率（最高8Mbps），只有发送节点在发，不需要仲裁，可以跑得很快

这个设计非常聪明：仲裁阶段慢一点保证兼容性和稳定性，数据阶段快起来提升吞吐量。

**帧格式对比**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaC7M6M6FqiatibN7toVsiblSoqd5wBhNY8icmuxZHSx8hZwfpBJ4s5rW1SyHrxiamvBicNOGeAdyQdgfGP5czJLm2taSc1f9tnVJqnYs/640?wx_fmt=png&from=appmsg)

**02**

**波特率切换的工作原理**

**BRS位：切换的开关**

CAN FD帧里有一个关键控制位：BRS（Bit Rate Switch）。

* BRS=1：数据段切换到高速波特率
* BRS=0：数据段保持与仲裁段相同的波特率（退化为Classic CAN速率，但帧格式还是FD）

发送节点在控制场发完BRS=1之后，立即切换到数据段波特率开始发数据。接收节点检测到BRS=1，同步切换接收波特率。帧结束后，双方再切回仲裁段波特率。

**采样点的重要性**

波特率不只是一个频率数字，还包括采样点位置。采样点决定了控制器在位时间的哪个时刻采样总线电平。

仲裁段和数据段各有独立的采样点配置：

* 仲裁段：通常配75%～80%，留足传播延迟余量
* 数据段：通常配70%～75%，速率高、位时间短，余量更紧张

采样点配错比波特率配错更隐蔽——波特率配错通常直接报错，采样点偏了可能偶发误码，只在总线负载高或温度变化时才暴露。

**收发器的限制**

不是所有CAN收发器都支持CAN FD高速数据段。Classic CAN收发器（如TJA1040）最高只支持1Mbps，用在CAN FD数据段会直接失真。

CAN FD需要专用收发器（如TJA1044、TJA1462），这些收发器的环路延迟更小，才能支持2Mbps以上的数据段速率。

**03**

**混用场景：Classic CAN节点能上CAN FD总线吗？**

**答案：能混，但有条件**

CAN FD的仲裁段与Classic CAN帧格式兼容，所以Classic CAN节点可以参与仲裁。但当CAN FD节点发出BRS=1的帧时，Classic CAN节点会把数据段的高速信号识别为错误，发出错误帧，破坏总线通信。

**解决方案：FD帧隔离**

实际项目中，混用场景通常这样处理：

**网关隔离**

Classic CAN子网和CAN FD子网之间加网关，网关负责协议转换，两边互不干扰

**只发BRS=0的FD帧**

CAN FD节点发帧时不切换波特率，数据段保持低速，Classic CAN节点可以正常接收（但这样就失去了CAN FD的速率优势）

**升级所有节点**

最彻底的方案，全部换成CAN FD节点，不再混用

**04**

**AUTOSAR配置要点**

**CanController配置**

在AUTOSAR的Can模块里，CAN FD控制器需要配置两套时序参数：

**仲裁段（CanControllerBaudRate）**

CanControllerBaudRate：500（Kbps）

CanControllerPropSeg / CanControllerSeg1 / CanControllerSeg2：根据时钟和采样点计算

CanControllerSyncJumpWidth：通常1～4个时间份额

**数据段（CanControllerFdBaudRate）：CanControllerFdBaudRate：2000（Kbps，即2Mbps）**

* CanControllerFdPropSeg / CanControllerFdSeg1 / CanControllerFdSeg2：单独配置
* CanControllerTxBitRateSwitch：TRUE（使能BRS）

**常见配置错误**

* 数据段采样点和仲裁段采样点用同一套参数：数据段位时间更短，直接套仲裁段参数采样点会严重偏移
* 收发器没换：用Classic CAN收发器跑CAN FD 2Mbps数据段，必然误码
* TrcvDelayCompensation没配：高速数据段需要开启发送延迟补偿（TDC），否则采样点漂移

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

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563394&idx=2&sn=ed98964862cf2f8280a4d6db9cd0a273&scene=21#wechat_redirect)

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

[网络安全：TARA方法、工具与案例](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247502093&idx=1&sn=ec4b373a33ca04d79afbb0b0b880bd4e&chksm=e9278dd6de5004c01bdd83ad0dd89c3549c7ae2ceb362959dbcb159324b2593d70bce78d82...