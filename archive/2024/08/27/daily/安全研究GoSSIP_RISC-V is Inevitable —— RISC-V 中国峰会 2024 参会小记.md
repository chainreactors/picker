---
title: RISC-V is Inevitable —— RISC-V 中国峰会 2024 参会小记
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498761&idx=1&sn=7b9f942ea3651ffa7f7ee01cdd9ffd6a&chksm=c063d2d0f7145bc6bf07713a64ae52a44e4befe1cfcb7ca64cfb81fafef4ea5999be5d9ff0e0&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-08-27
fetch_date: 2025-10-06T18:06:26.798130
---

# RISC-V is Inevitable —— RISC-V 中国峰会 2024 参会小记

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPdGgoxJoVxcFXcBoBibjDibIFJ3icic0EhxVAN5fTeQeiaOZRwXRhgptKsjMg/0?wx_fmt=jpeg)

# RISC-V is Inevitable —— RISC-V 中国峰会 2024 参会小记

原创

G.O.S.S.I.P

安全研究GoSSIP

RISC-V 虽然距离和 ARM、x86 达成三分天下的目标差得很远，但是由于其开源的特性，得到的关注已经非常之大。RISC-V 中国峰会这几年都搞得非常热闹，包括三年自然灾害期间也还坚持搞过。今年的RISC-V 中国峰会在杭州举行，G.O.S.S.I.P 派出两位记者前往参会，并记录下来了很多精彩瞬间，今天特地发出来与大家分享！

## Day 1

RISC-V 在现实世界的使用和部署情况到底如何呢？在第一天RISC-V 基金会CEO Calista Redmond 女士的发言中，我们可以看到一些数据：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPdLQM0lEiclMCxNJZJxoS1uQO8VOtyURT4NZrmnXxB9ueribIdhefYG91w/640?wx_fmt=png&from=appmsg)

目前 2024 年，这颗星球上已经有一百万颗芯片包含了 RISC-V 内核！根据 The SHD Group 的预测，2030 年会有一千六百万颗支持 RISC-V 的芯片。这里 Calista Redmond 女士还 cue 了一下某些不愿透露流片数量的（不）知名架构。

这些芯片都在哪里呢？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPdTTydzkUwbkiaST28ZdAyCd35lv8OJlpnDBhpbag3CsibGVljwibXg5d0w/640?wx_fmt=png&from=appmsg)

AI！事实上，Nvidia 和 Meta（Facebook）的 AI 加速器中，都已经出现了 RISC-V 的身影。当然，这只是一百万颗当中的很小一部分。目前来讲，大部分的 RISC-V 芯片都出现在了 embeded（嵌入式）的领域，并且可以说已经打下了坚实的基础。The SHD Group 也对 2030 年的 RISC-V 市场做出了预测：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPd45ZUeiawEPMpc5sGAW5qN2Z9ricaltNm7yXWglIcHKhibWJK7A0QWUGLQ/640?wx_fmt=png&from=appmsg)

大家可以发现，在这个预测中 RISC-V 的主要发力点大都是新兴技术相关领域，比如可穿戴设备、5G 基础设施、AI 计算设备。毕竟在传统的强生态领域（如服务器、桌面电脑、移动设备），RISC-V 的生态想要赶上其他老大哥实在是太难了！RISC-V 要想达到三分天下的目标，还是得找到一个独特的角度。

达摩院将视野投向了高性能和 AI 领域：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPd0uJnibU2ib0eic86KB1OOpdXs58sOkgul30KsiaaoZFklhZkQ2uwTBG98A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPdYt96G8cAIPc7MsKSrMiaTicib9iagNbkPnsQG4Eofgd0oUwLAUM4DCmCMg/640?wx_fmt=png&from=appmsg)

奕斯伟计算（ESWIN）又给我们介绍了垂直领域中的应用，比较有趣的是他们还展示了一个车路云协同系统的实践案例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPd7cja7JkTu5xweUYbXjtRWlda3xLVJdwSR6ZrZB5e77uiaMiaOIq5ia9bA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPdhD4NUElPZj17dOsTsTh9z44BZcbGChg1LtdCO40ClOMkOQ2hnQ0rMw/640?wx_fmt=png&from=appmsg)

"RISC-V is Inevitable" 这句话究竟会成为一个自证预言，还是一个单纯的美好愿景/商业口号呢？让我们拭目以待！

---

### 硬件安全架构

硬件安全架构研讨会是本次 RISC-V 中国峰会的一个同期论坛，也是我们编辑部特派记者关注的重点。

第一个报告来自中科院信工所的李沛南老师。他们主要关注的是 TEE 架构中，安全 Enclave 管理服务（Enclave Magagement System）的安全性。在投稿至 Micro 2024 的文章 HyperTEE: A Decoupled TEE Architecture with Secure Enclave Management 中，他们为管理服务专门分配了一个（低配的）核心，并规范化其接口，以完全的空间隔离方式来保护管理服务免受攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPdElkoPyDYWf6aco0MMYIrNLmGTbqFpopDEaHE89VEUbkXp3H9TSy6Yw/640?wx_fmt=png&from=appmsg)

他们也将这套方案拓展至了香山芯片，从论文中的进程级 Enclave 支持扩展至了对于 VM Enclave 的支持，目前已经可以软件模拟在 Linux 系统中启动 VM Enclave。

第二个报告来自我们上海交通大学 IPADS 实验室的杜东老师，介绍了他们发表在 ISCA 2024 的工作 sNPU: Trusted Execution Environments on Integrated NPUs。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPdYctVs8c7fYJt3B2qf7RNaorcicxiad7eSh3ibx76Q7mYb3iaqF8trqs1Sg/640?wx_fmt=png&from=appmsg)

> \*论文作者包括：Erhu Feng1, Dahu Feng1, Dong Du, Yubin Xia, Haibo Chen

他们采访了相关的厂商：在工业界中，NPU 的主要使用场景用于移动端的生物验证，大部分产品中的 NPU 目前仅供 TEE （或者说 Secure World）使用。在这篇工作中，他们将 TEE 场景下的 NPU 攻击分为三大类：(1) 控制 NPU 攻击 CPU；(2) NPU 内部攻击；(3) 从 CPU 攻击 NPU，并分别设计了保护。

在他们开展工作时，还没有 NPU 内部攻击的实际案例。巧合的是，就在今年一月份，Trail of bits 团队发现了 leftoverlocals 漏洞，这一漏洞影响了 Apple、AMD、以及 Qualcomm，这种大规模的影响面使其引起了领域内广泛的关注，也助力了这篇文章的成功投稿。机会留给有准备的人！

%%

* NPU 攻击 CPU（其实主要是DRAM）-> 基于 NPU 简单的内存访问模式这一观察，实现简单的地址翻译检测
* NPU 内部攻击（LeftoverLocals，非常幸运，爆出来之前都不存在现实中的此类攻击）-> 基于 ID 划分 NPU 内部的 SRAM，为每一个 NPU core 和 Scratchpad entry 添加 ID。
* CPU 攻击 NPU -> 门锁、轻量化 NPU 驱动
  %%

第三个报告来自浙江大学的申文博老师，围绕 ARM 的指针验证机制介绍了他们团队的一系列工作，其中有一些在我们去年的 G.O.S.S.I.P 暑期学校也介绍过。
第一项工作 kCPA 将指针验证运用在加固 Linux 内核上，并利用开源的 m1n1 bootloader 在真实的 Mac 硬件环境上进行了测试（TDSC 24）；第二项工作逆向了 Apple 魔改后的指针验证硬件机制，揭秘了 Apple 的 dark magic（USENIX 23/Blackhat USA 23）；第三项工作设计了一种软硬件协同的轻量加密数据原语 RegVault，以进行小粒度的内核结构体保护（DSA 22）；第四项工作利用指针验证机制设计了针对 DMA 攻击的保护硬件 DMAAuth（USENIX 24）。

%%

* PA 加固 Linux 内核 kCPA，在真实硬件测试。技术难点：指针的污点传播，代码指针相对好处理，但数据指针
* Apple M1 PA 逆向（usenix23）
* 小粒度内核数据结构保护 轻量级加密数据原语 RegVault（DSA22）
* DMAAuth 异构安全架构（usenix24）
  %%

压轴的第四个报告来自华为 2012 系统安全实验室的张路波，为我们介绍了许多他们实验室（工业界）正在尝试的软硬协同内存安全技术实践，力图歼灭内存安全问题。他们介绍了 AEGIS 安全指令集、基于 ARM 指针验证进行控制流数据流保护、面向 XPU 加速计算场景内存安全

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPd4uZ7oP5IuXLguhSCZvbZVfEqBKwxWZKABVYjkD8CR6h3nEQFXkfc2w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPdVvqrcVJDwH5Xq6bgfzjicBwzbBBEZ0pwfyLyvdtDlxJgvZeibUROoy9A/640?wx_fmt=png&from=appmsg)

---

## Day 2

### 1. 可抵御缓存测信道攻击的随机化缓存设计

第一个报告来自中科院信工所的宋威老师，针对冲突型缓存测信道攻击提出了缓存随机化防御。首先，需要进行缓存测信道攻击，就必须要有驱逐集，从而根据访问时长获取信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPd246iaA4jV02uHtL4TcBNzjQ7MQjF5cMeOfic3azuxYgqzVVus7DtcO8A/640?wx_fmt=jpeg&from=appmsg)

那么怎么获得驱逐集呢，一般来说，有如下三种算法：

1. 组消除
2. 覆盖-裁剪-触发算法
3. 冲突测试

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPdxVXbaBSV9MdO38TsNQXoWPibnrtgfOJsvLUgd51EOvVebYQmFN27ia0g/640?wx_fmt=jpeg&from=appmsg)

#### 当前解决方法：

1. 映射随机化+周期性修改加密密钥

* 提高驱逐集寻找代价
* 但是重映射代价太高（40%-60%数据丢失），会大幅度提高访问代价（所以周期不能太短）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPdGZCshwECIiaVJonHMN2PWFzpTNOIZyjkvFbNbN33hqo0tLJJPiclPvzg/640?wx_fmt=jpeg&from=appmsg)

2. 动态随机化Skewed缓存：

* 降低了信息泄露的可能性，同时保证了性能，但在一些情况下，攻击者仍有较高成功率

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPd6jjdsOPE08RjIlQocnsbAK9WAGhbKMQrBK5dbYH6lOtNJ98B61Lm2A/640?wx_fmt=jpeg&from=appmsg)

3. MIRAGE：

* 彻底消除攻击，CPI损失约3%，但是SRAM存储空间代价很高。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPd9VXyOsm6mOrZTzzOqhIWMwvryn70NCDD4urOOJHFNhriaJw1L8UlFUw/640?wx_fmt=jpeg&from=appmsg)

#### 优化

\*\*1. 传统映射（非线性）往往需要多周期，影响性能，可以采用单周期随机映射（hash），降低代价，对不同的值选择不同种子 \*\*

2. 使用多步置换，降低数据丢失

* 传统重映射：顺序移位，如果映射位被占用，会驱逐数据
* 多步置换链（贪心算法）：对被驱逐数据进行置换，直到找到空穴，只有约10%的数据丢失

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPdT09HzWYT8dR7iaOzknMoXCdhdQOtFFSdj0EAmHtZCCtbdricrDzT7saQ/640?wx_fmt=jpeg&from=appmsg)

3. 使用缓存驱逐事件为重随机周期计量单位

替换重映射周期计数单位，用EV10代替ACC100，大幅度提高缓存性能

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPd5sTKc2bmuSECjzYArpbbicibu3IfiaL5yemdV9LpNoqz2KIviapuahiatHQ/640?wx_fmt=jpeg&from=appmsg)

4. 使用基于Z-Score的检测算法，来对GE/PPP等攻击进行检测。

防御效果如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPd6wZfWAYYQ1ZXQ0RGebM0UXMsF5DLPhjEeLJ6zgc4FAFUica6uq3rlLw/640?wx_fmt=jpeg&from=appmsg)

面积代价如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPdl8DHwNYjTyJ4SgicicThVTBDOqp5tFyutVtAdGRDnKI3HibUtkmCicxaug/640?wx_fmt=jpeg&from=appmsg)

### 2. SeChain：基于国密算法的RISC-V安全启动机制的设计与实现

第二场报告由中科院软件所团队带来，他们根据IoT设备数量迅速增加，但缺乏物理层安全机制的现状，提出对固件篡改等物理攻击防御。

#### 当前解决手段：安全启动信任链（固件完整性检查）

*主流安全启动机制*：

* *UEFI Secure Boot：有信任根风险*
* *Intel Boot Guard：重量级，而且密钥被国外厂商拥有*

#### 架构设计：

基于这些问题，该团队提出了新的设计：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPdXMAJOpYpxsnVUCpxpFtHGVvhK13WaQN2PnUdK2nxMhgc7SPicczERcw/640?wx_fmt=jpeg&from=appmsg)

*硬件信任根*：

固化在SoC的ROM中，保证其不可篡改性

*签名流程和SCU单元*：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPdqpiao8clQ70w4qZKGrrS9dj9674t938V8JF9PIbQITltXA0EQPN7OUQ/640?wx_fmt=jpeg&from=appmsg)

*验证流程和KVU单元*：

SM9的片内执行

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPd54GN0CtBBo6uG8FAiccjXBtJ0SyTyialGicweKCAmCy8NTSxroFNiaOJlQ/640?wx_fmt=jpeg&from=appmsg)

#### 实验：

有效性验证实验（如图）：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPdhPwDQVLsyqMHSwgib8EsWpMlA2ZWjvC3oWPs6FmKo9iclcNvH9RxGYHQ/640?wx_fmt=jpeg&from=appmsg)

高效性验证实验（如图）：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21Fo5P1euaQxqLJdH4DicEfPdFIXBd2w9icWSBqF2Mmxiba1tPBQ3ILDfnwNnB3Ea73f8sYeOEoNbr0vw/640?wx_fmt=jpeg&from=appmsg)

### 3. HVP: Hardware Accelerated RISC-V Android Emulator

接下来，来自Intel的Haicheng Li和Qingshun Wang为我们带来...