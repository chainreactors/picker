---
title: 新型 Bit2Watt 攻击，云租户无漏洞亦可扰乱电网
url: https://mp.weixin.qq.com/s/uQJ7jCtP9miiosSXjyUaKQ
source: Doonsec's feed
date: 2026-07-22
fetch_date: 2026-07-23T05:06:51.205054
---

# 新型 Bit2Watt 攻击，云租户无漏洞亦可扰乱电网

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2rKRZ5DPsSerbibyMicdKkVibjw7QSoCPKsX0tTerOMFU9zD1Tict63b4YvWHE7ZzngPctmnSZftGWuicTQBqpTJItT6Stk5rb6ZiaY/0?wx_fmt=jpeg)

# 新型 Bit2Watt 攻击，云租户无漏洞亦可扰乱电网

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX0FdxwmXtzDBs3MpTeHPJh8bjasjWiasTttGqqXy9vGyICOMBuYZEuEOg0YURVRn2cBs8sBBjJWgjmxicDhGtXg8c4MImYjJpTvw/640?wx_fmt=gif)

![Bit2Watt攻击示意图](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1cClDWLIz7pWEVxNYrAWg7nIKnYEbwGeSqFZ019myuQUQRs1cRODhLbR43BYm3GV2NwlzLAopQI0broFPSswMm3rVnrCHZgAw/640?wx_fmt=jpeg)

一名云租户只需使用普通的GPU访问权限，就能让数据中心的功耗快速上下波动，足以威胁其连接的电网，且无需任何漏洞或入侵。

这就是Bit2Watt攻击的核心主张。该研究由浙江大学三位学者完成，论文已被IACR硬件安全会议CHES 2026收录。证据分为两部分：他们在真实GPU上测量了功率调制，并模拟了可能引发的电网失稳。

该技术颠覆了传统的电网攻击模型：无需被篡改的传感器、控制系统的恶意软件或窃取的操作员凭据，只需一个故意制造异常行为的工作负载。

其原理在于：GPU的功耗紧随其计算任务变化。饱和张量核心时电流飙升；切换至空闲状态时电流骤降。按固定节奏在这两种状态间切换，就能在电源插座处产生可控的功率振荡。

作者将其归结为一个直白的问题：“纯粹的计算行为，作为合法工作负载执行，是否可能被武器化以破坏电力基础设施？”论文的其余部分就是他们的回答。

Part01

Bit2Watt攻击原理

第一种方法称为SWMA，它上传一个特制的CUDA内核，在高强度计算模式与近乎空闲模式之间快速切换。主机端控制器设置切换时间表，并通过标准工具（使用cudaMallocManaged分配的统一内存标志）来切换模式，无需任何特殊手段。

在测试的GPU上，这种合成工作负载产生的功率分量频率约为1.5kHz至6kHz，在RTX 4090上达到峰值，远超家用空调等负载摆动时产生的几赫兹频率。

该现象同样出现在数据中心级GPU（如A100和Tesla V100）上，并非仅限于游戏显卡。这种自定义内核及其紧密轮询循环，云服务提供商或许能够学会识别其指纹。

第二种方法LTMA才是运营商应当担心的。它并非使用合成内核，而是将功率调制隐藏在实际的LLM训练过程中，通过调整超参数和插入辅助操作，在不中断训练的前提下使计算负载上下波动。

其控制精度不如SWMA，受限于训练循环的迭代速度，频率较低（大约1.2至3kHz）。但它能达到更大的振幅，并能融入正常的训练噪声中，这正是它更难被发现的原因。两种方法均无需提升权限，因为租户本就可以控制自己的训练脚本和作业调度。

Part02

规模化后的电网风险

上述数据均为单GPU的表现，只有规模化时才会产生威胁。论文模拟了最危险的大规模场景：一个1MW的局部电网，90%由分布式能源（如屋顶太阳能和电池，越来越多地接入本地电网）供电，1000块GPU以完全同步的方式调制功率。

![Bit2Watt功率调制模拟](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1qYRZB6ICA8j6dpJaib1yu5ffsmIUGJdhK9Z8S1G0BKrPW0QTdpruaX6RmDL3C68cmgAeEqID3juJm4Yiama0rnHYq0d5GtZvzA/640?wx_fmt=jpeg)

在该最坏情况模拟中，电流总谐波失真（THD）达到46.8%，远超论文参照IEC 61000-3-12标准设定的13%阈值。阻尼比降至-0.27，这是一个负值，标志着系统处于不稳定模式——电网不仅不能抑制扰动，反而会将其放大。

论文进一步将模型扩展至一个9,241个节点的电网（模拟欧洲输电网络），其中相当于系统负载2%的局部扰动经过13个阶段级联扩散，最终甩掉了约81%的负载。这个数字叠加了最坏情况假设，且仅适用于这一特定模型，属于模拟结果，并非实际预测。

完全同步是实现该攻击的关键假设，同时也是对攻击者而言最乐观的情况：论文承认，在真实的云GPU集群中实现功率切换的精确对齐仍是一个悬而未决的问题。在其2kHz模型中，时间抖动标准差为100微秒时，聚合振幅降低了约20%，且论文并未声称该数值反映典型云环境。

一次真实攻击需要同时满足多个条件：足够多的物理聚集的GPU、它们之间的紧密同步、能够穿透数据中心电力调节阶段的调制信号，以及电网的共振恰好放大所选频率。

物理实验在受控测试平台中进行，电网级破坏来自模拟，没有攻击任何生产系统，也没有披露任何特定商业产品的安全漏洞。

![Bit2Watt实验与模拟结果](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1HNITKELPOyFbLkuofib66CmGkoLpRSRfa6YhhWryOuPeHAfPRjibEy7icaNuAicxa5SpQqnt300ZiaDQtcO9PP8VicXQ9OcA3cckWM/640?wx_fmt=jpeg)

The Hacker News已联系浙江大学研究人员，询问该攻击在真实云环境中的扩展程度，并将在收到回复后更新本文。

Part03

现实影响

该研究并非纯理论，因为物理原理已有记录。2025年8月，微软、OpenAI和NVIDIA联合发表了一篇关于稳定AI训练功耗的论文，警告大型训练作业的同步功率波动，当其频率与电网的临界频率重合时，可能“对电网基础设施造成物理损坏”。Bit2Watt正是将这种意外效应变成有意为之的武器。

电网此前已因数据中心意外行为受到过惊吓。2024年7月，弗吉尼亚北部数据中心密集区域发生输电故障，导致约1500MW的数据中心负载同时从电网脱离，原因是这些设施的自身保护系统将其切换至备用电源。

负责北美电网可靠性的NERC表示，当时该扰动并未构成可靠性风险，但运营人员仍需校正电压。它警告称，随着这些负载规模扩大，风险也在增加。2024年底，其技术委员会成立了大型负载工作组进行研究。

没有任何人发起攻击；数据中心只是在保护自己。关键在于，这不是电网差点崩溃的问题，而是如此规模的负载可能瞬间脱离电网，速度之快超出运营人员的规划能力，并且随着集群规模增长，风险不断攀升。

闭环的另一端是作者所称的Watt2Bit：扰动反馈回计算侧。论文分析表明，谐波导致的发热和电流升高可能触发热保护或过流保护，导致GPU服务器停机，从而将电能质量问题转化为拒绝服务攻击。

更奇特的是，同样的调制还能充当隐蔽信道。研究团队将比特编码为两种频率——2kHz代表1，200Hz代表0——用近场天线捕捉电磁辐射，连接至软件定义无线电，成功以零错误恢复了50位测试序列。

这与2018年THN报道的PowerHammer（气隙数据窃取攻击）非常相似，但有一个区别：PowerHammer通过电力线读取传导数据，可在从插座到建筑配电盘的任意位置进行窃听；而Bit2Watt的信道需要天线在硬件附近捕捉近场EMI。

两者均无法通过互联网远程实施；都需要在电源或机器附近获得物理接入点。

Part04

无可修补的漏洞

标准遥测手段几乎无法检测到这种攻击。机架PDU计数器每秒采样一次，NVIDIA的NVML遥测频率为450Hz，即使最快的通用接口（RAPL和服务器BMC）也仅达到约1kHz，而功率调制频率则高出数倍。

研究人员基于功率和NVML数据构建的轻量级检测器表现不佳；加入GPU性能分析特征后有所改善；专用的EMI探测效果最佳。LTMA始终比SWMA更难发现。这些结果来自研究级检测器，而非大型云服务商可能运行的专有系统，因此不能证明超大规模云服务商一定检测不到。

更大的问题并非可见性。没有产品漏洞需要修补，因为暴露点在于架构本身：不稳定的GPU负载与高比例逆变器电网之间的紧密耦合，而传统的监控系统并未跨域跟踪这种耦合。

论文同时提出了两方面的防御措施：电源侧采用电池、超级电容和谐波滤波；计算侧对GPU利用率和训练调度进行异常检测。它将两者结合的统一系统留作未来工作。

计算侧和电网侧由不同公司运营，使用不同工具监控，二者均未设计为监控对方。这条缝隙正是Bit2Watt的藏身之处，而目前没有任何一方对其负责。

参考来源：

New Bit2Watt Attack Could Let Cloud Tenants Disrupt Power Grids Without an Exploit

https://thehackernews.com/2026/07/new-bit2watt-attack-could-let-cloud.html

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3M5qLVTGP6jiaibktDcXOic6E1x1CNbVhdStkk8micFrCq9q4Hp2oH9WnQ229S3ziaeHPACAgicCRKZjic3pV1CTArGRs1KdhccugdUw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651342454&idx=1&sn=30ae51eba566ed3187493e4e817d3124&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX38DqtZUv5FjJ2NibZ3wlLba7jpicoInsIGFnVouGN6kbudJyTf7yhkPM5z8JBrkOVNnialq3PeHX0JzJ9vkBXoUwAdicH70OSf4Wc/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3vp7Nh5SN03lJzkelia9oMl3rDgBcDgQuSu66GUobMfu7PibWYZsgcVfAuZ1aAVwMiatGia3JO3kthfNotNqKQC8uiaS9Za2ky2BVI/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1ptPNnRL9ln6TVtKnqhFaD6lZpyAbLwIM5Fj1m89oyZLopZfbJiaJygvkmWZnicUqiaMDPQFh7zAOptwmFmtCGTNSDFbCOaUfcYc/640?wx_fmt=png)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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