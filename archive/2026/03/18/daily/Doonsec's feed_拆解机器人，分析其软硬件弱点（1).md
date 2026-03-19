---
title: 拆解机器人，分析其软硬件弱点（1)
url: https://mp.weixin.qq.com/s/kU0XYhP0zhr-kMgcJmYT4g
source: Doonsec's feed
date: 2026-03-18
fetch_date: 2026-03-19T04:16:32.215049
---

# 拆解机器人，分析其软硬件弱点（1)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ccVb6wGibibCGVO4oYs4b0QMvKE7xRqRZ8sicntKuvvhVVdzUXETSOVFC0NtpXCSNMrhRrpBvib5BpDDXpepBFOuevrdhletAevpibGMCMzFy6AI/0?wx_fmt=jpeg)

# 拆解机器人，分析其软硬件弱点（1)

原创

孙志敏
孙志敏

AI与安全

![]()

在小说阅读器中沉浸阅读

考虑到机器人的价钱及复杂程度，很多人没有条件去仔细研究它，但软硬件架构又是安全研究非常必要的条件，有必要深入了解。

最近，国外有公司对某款做了深入的拆解和分析，包括软件反汇编，非常专业，可以借鉴。考虑到敏感性，具体厂商的名字不做说明。

1

硬件关键信息

1.外形。全人形机器人置于支撑架内。外部底盘上看不到任何电子元件，其密封外壳旨在保护内部系统免受环境因素和人为破坏的影响。支撑架机构清晰可见，用于测试和维护程序。

2.上半身躯干保护罩完好无损。胸板是机器人中央计算和电源管理系统的主要入口。外部线束安装点和传感器阵列清晰可见，但目前内部电子元件尚未暴露。![请参考图注](https://mmbiz.qpic.cn/sz_mmbiz_png/ccVb6wGibibCGb1MibX6ZchyicJiaJYnhnW6ibKGY2QY6IWyZicsObEicIJJzvCh9arHjbs9VrBaVpSrJ3j2pAib4zWnGJc4U0Giac6ZBLl44QGxrbq5Y/640?wx_fmt=png&from=appmsg)

3.打开胸盖，露出主PCB板。可见组件包括：

(1) 用于散热的主动冷却风扇模块；

(2) 带有多个JST型连接器的主控板；

(3) 带有可见电容的配电电路；

(4) 电机驱动接口和传感器连接点。

该PCB板作为机器人的中央计算和配电枢纽，负责协调所有子系统的通信。

![请参考图注](https://mmbiz.qpic.cn/sz_mmbiz_png/ccVb6wGibibCETgFZrU5zRqj45oohiadhqpwick2EGhaY7GZSDKmiaJHcYuZchPcyy3xtLwia9MdWQbOaX6Bhfflibsm750YgiaQuSlFaUW0gBgRCeQ/640?wx_fmt=png&from=appmsg)

4.主PCB架构特写。可见的关键组件包括：

(1)覆盖主SoC/CPU复合体的大型散热片；

(2)多个用于模块化连接的白色JST连接器；

(3)成簇排列的功率调节MOSFET；

(4)带有专用功率级的电机驱动电路；

(5)用于本体感受反馈的传感器接口连接器。

内部线束标识表明子系统之间采用了标准化的连接协议。

![请参考图注](https://mmbiz.qpic.cn/mmbiz_png/ccVb6wGibibCFiaWtiazwquTAvZLQxicHlR0hgxLcxwLAYqUkQGFNRicRhBIQ4eu5vGMHhibicTM6oRgicRZ6nSUtUcQT4t1vUqwy3pL8iawz8niabDpIA/640?wx_fmt=png&from=appmsg)

5.上部PCB板主要负责电源管理。关键电源元件包括：

(1) 用于电机控制的大电流功率MOSFET；

(2) 高压线束上的Kapton绝缘胶带；

(3) 电源部分的专用冷却风扇；

(4) 多级稳压电路；

(5) 用于电源滤波和稳定性的大容量电容。

该部分负责满足人形机器人运动和操作所需的巨大功率需求。

![请参考图注](https://mmbiz.qpic.cn/sz_mmbiz_png/ccVb6wGibibCFK7cxJicRD15qxDSYXG8I6VUL589ib0yqCQiaEDge2HfTdJLYOFUfQV5JHz1v19ictw6LaApFaktMBkZaSAWewlyiccibaevhZBDFTg/640?wx_fmt=png&from=appmsg)

6.主处理复合体宏观视图。芯片标识：

(1)瑞芯微 RK3588 SoC - 8 核 ARM Cortex-A76/A55 处理器，

(2) FORESEE eMMC - 嵌入式 NAND 闪存，

(3) SK 海力士 LPDDR4/5 RAM - 高带宽系统内存，

(4) WiFi/蓝牙模块- 屏蔽射频部分（左侧），

(5) PMIC - 多个电源管理集成电路，

(6) 270µF/16V 电容- 大容量电源滤波。

RK3588 作为主要计算平台，用于高级控制、AI 推理和系统编排。

![请参考图注](https://mmbiz.qpic.cn/mmbiz_png/ccVb6wGibibCFEJibWSbJ6z7ZPHpXwtYo7ZIm55FN8cFW6AXYbc3maIp0pfxrg9aIZqzO6FKPlDIbAP6ibRRLCR9w9le4EuhGbxU9bnBiagXpyxw/640?wx_fmt=png&from=appmsg)

2

硬件分析发现的问题

物理拆解揭示了几个与安全相关的架构决策和潜在的漏洞途径：

攻击面识别

暴露的硬件架构存在多种攻击途径：

1. 物理访问点：胸腔可直接通往主控板，如果物理安全受到损害，则可进行硬件级攻击。

2. 模块化连接：JST 连接器的广泛使用虽然便于维护，但也为恶意硬件植入或信号注入攻击创造了潜在的插入点。

3. 未屏蔽的组件：一些关键集成电路缺乏防篡改封装或硬件安全模块，可能导致芯片脱落攻击或侧信道分析。

4. 电源管理复杂性：多级电源调节系统虽然是电机控制所必需的，但会通过电压毛刺引入潜在的故障注入机会。

RK3588 作为其核心部件，一直有漏洞被发现，下面是一些例子：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ccVb6wGibibCESPwdumv5micyQ6nOBZ6iaSXOpqofJtvUCUKWF9fO3pKNTfOVdzzeoPZwYCr5V7pIuEIYHUdoGphSbsuFL543OnCKzU72ZsUTs0/640?wx_fmt=png&from=appmsg)

对人形机器人安全的影响

硬件拆解和漏洞分析揭示了人形机器人部署中的关键安全隐患：

1.易于访问的物理接口、已记录的片上系统 (SoC) 漏洞以及有限的安全启动实现，共同构成了复杂的风险状况。能够进行物理访问的攻击者可能：

•通过未受保护的调试接口提取固件和加密材料

•在引导加载程序级别注入恶意代码，绕过更高级别的安全控制

•在加密操作期间，对未屏蔽的 RK3588 执行侧信道攻击

•通过已记录的TEE漏洞破坏机器人的可信执行环境

这些硬件层面的漏洞构成了基础性的攻击途径，能够破坏后续章节中描述的整个安全架构。由于缺乏硬件安全模块，再加上RK3588已知的漏洞，因此在任何部署方案中，物理安全都必须是首要考虑因素。

从硬件到软件的安全边界过渡发生在多个层面——引导加载程序、内核和用户空间——每一层都继承了下一层的安全漏洞。这种级联漏洞模型通过我们的拆解分析得到了实证验证，它证实了关于人形系统中跨层攻击传播的理论预测，同时也揭示了纯粹理论分析会忽略的特定实现层面的漏洞。

3

小结

从上面的硬件情况看，基本就是一个标准的嵌入式系统，传统的分析方法，尤其是OT领域的分析方法，应该都可以用。

下一篇将详细分析其软件架构及反汇编跟踪情况，有兴趣的请关注。

![](https://mmbiz.qpic.cn/mmbiz_gif/NB91guJr0w3nSyvUF9MgTABODeoVticjUljjdKUictmqNBvykumXicg13ic8CwNJJbA0sjhaB1vet4oCLQ0QTWz28w/640?from=appmsg)

关注我，始终为您提供最有价值的前沿信息和分析判断。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rhmRSVBNbicqDIxcZyn1sK1icxG8aZVh9lVqRTa042xtzVBrJs2tcFPYv4HmkmFCDu8mtZJYw4x2vrbBx2mJf2AA/0?wx_fmt=png)

AI与安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rhmRSVBNbicqDIxcZyn1sK1icxG8aZVh9lVqRTa042xtzVBrJs2tcFPYv4HmkmFCDu8mtZJYw4x2vrbBx2mJf2AA/0?wx_fmt=png)

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