---
title: 汽车功能安全之LockStep Core原理与实践
url: https://mp.weixin.qq.com/s/w-g-CKPbY-FpmPpH7D1Lcw
source: Doonsec's feed
date: 2026-06-28
fetch_date: 2026-06-29T06:33:00.934772
---

# 汽车功能安全之LockStep Core原理与实践

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaC5RpvZLVl5HNDE9ia35poTry5apmbFwNA3NuT39icias1L5jyFX2D5jPic6JsoSbUwd5RAyuMK6iaBzUbiaCXibus77UaiaGOaUYkDbyQ/0?wx_fmt=jpeg)

# 汽车功能安全之LockStep Core原理与实践

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247573595&idx=1&sn=425c418664766cc4030f3cb49a733ec6&scene=21#wechat_redirect)

**01**

**什么是 LockStep Core（锁步核）**

先解释 Lockstep 这个词，字面意思是步调完全同步，该词汇最早源自军事场景，用来形容士兵齐步行进、所有人动作步伐保持统一，后来被引入计算机容错领域，定义为：依靠多套相同冗余硬件，在同一周期处理一模一样的指令，让多颗 CPU、内存实现高精度同步运行

我们所说的 LockStep Core，中文称作锁步核，由主核（Master Core）与校验核（Checker Core）两部分组成。两颗核接收完全一致的输入数据、执行相同运算逻辑，再通过片上硬件比较器，逐时钟周期对比主核与校验核的输出结果，英飞凌 Aurix 系列芯片就是典型应用案例，其锁步工作逻辑如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaDtpPqvxX7IT8y61kBe3lVD1hFrwxml6eSbk8R3rGWxYx9HcNCo7EHKbibPFeGMp34p5N7rWPic8vX9Ku3PqSUBGRvbz9gRw1S2s/640?wx_fmt=jpeg&from=appmsg)

LockStep工作原理图

1. 主核、校验核输入完全相同；
2. 在校验核的输入通路插入固定时钟延时，延时周期数通常设为 2 个 cycle；
3. 设主核输出数据为 a [i]，校验核输出为 b [i]，二者运算算法完全一致；
4. 对主核输出 a [i] 做按位取反操作，再插入同等时长延时，得到信号 x [i]；
5. 最后将 x [i] 与校验核输出 b [i] 做同或运算，生成比对结果 cmp [i]。

比对判定规则：若 cmp [i]=1，代表锁步校验检出异常；若 cmp [i]=0，代表锁步校验结果正常。

**相同之处**

1. 主核、校验核输入数据完全统一；
2. 底层硬件运算逻辑、处理算法完全一致。

**不同之处**

1. 延时位置区分：校验核在输入端增加延时，主核在输出端增加延时，但两边延时时钟周期数量相等；
2. 取反操作区分：仅主核输出做信号反转，校验核无该操作，该设计用来规避共模干扰。

正常工况下，x [i] 与 b [i] 必然互为反向信号，经过按位同或后输出恒为 0，以此证明两颗 CPU 硬件运行无故障。

另外 LockStep 属于纯硬件层面的冗余防护机制，运行过程不会对上层软件造成任何影响。英飞凌 Aurix 锁步 CPU 还会同步复制以下硬件模块：

* TriCore TC16E / TC16P 内核
* CPU 专用特殊功能寄存器 SFR、片上控制寄存器 CSFR
* 连接 SRI 总线的主、从接口
* 对接 SPB 总线的主接口
* 中断路由单元接口
* 系统控制单元 SCU 接口
* 程序存储区访问接口 PMI
* 数据存储区访问接口 DMI

**02**

**LockStep 锁步功能有什么作用**

英飞凌官方安全手册明确说明：锁步依靠硬件冗余机制，检测 TriCore CPU 出现的永久性硬件故障与瞬时性偶发故障。

我们可以结合故障场景拆解理解锁步的检测能力，芯片可能出现的典型故障包含：

1. 延时电路损坏，导致两路比对信号时序错位；
2. CPU 算术逻辑单元 ALU 硬件失效，运算输出数值出错；
3. 信号取反非门电路故障，无法完成输出反转；
4. 输出传输线路发生短路、断路，造成结果异常。

只要锁步校验结果正常，就能证明上述四类硬件电路均工作完好；一旦检出永久性或瞬时故障，说明对应硬件单元出现损坏或临时失效。

故障信号会接入 SMU 安全管理单元的告警寄存器，锁步故障触发后，SMU 会发起系统复位。

锁步核心原理简单来说：使用一颗独立校验 CPU，实时监控另一颗独立主 CPU 的运行状态。

**03**

**哪些场景需要开启 LockStep 锁步功能**

根据英飞凌官方规范：功能安全等级达到 ASIL C、ASIL D 的应用场景，必须启用 LockStep；而 QM 质量管理等级、ASIL A、ASIL B 无强制开启要求。

多核 MCU 架构下，分配给 ASIL C 及以上安全等级任务的内核，均需要打开锁步功能。

**04**

**为什么要使用 LockStep 锁步机制**

ISO 26262 汽车功能安全标准第五部分硬件安全附录 D 的表 4 中明确，双核锁步是诊断覆盖率较高的处理器硬件安全机制，标准 D2.3.6 小节做了详细说明。

**标准原文核心释义**

1、设计目的：通过逐周期对比两颗同步运行处理单元的运算结果，尽早识别处理器内部硬件失效；

2、机制描述：单芯片集成两组对称处理内核，两颗内核以固定延时同步运行，运算结果实时比对，一旦数据不匹配则进入故障状态，通常触发系统复位。该机制对瞬时软故障、ALU 运算单元硬件失效防护效果突出；依托冗余设计，可同步覆盖存储器地址总线、配置寄存器故障检测；

3、优缺点

1. 优势：两条运算通路无需两套独立应用软件；
2. 劣势：双内核仅能实现单内核的运算性能；优质设计可识别并处理共因失效（例如共用时钟源故障）；
3. 局限：该方案无法覆盖系统性设计缺陷。

标准引用文献 22《Delphi Secured Microcontroller Architecture》中，完整介绍了校验 CPU 整套技术方案，也是单片机锁步架构最早的原型设计，方案组成如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaAsR6Aia9h9iaO7o4ll77r4IxicYKxCB49xy8ysENicjX9uR8zXP77A7YjJE65mS55VdUqg8Pm7PgOA2c4xY1geJEbrFg5s5ngyVCw/640?wx_fmt=jpeg&from=appmsg)

Check CPU

1. 主 CPU：负责 MCU 整机外设控制；
2. 校验 CPU：与主 CPU 同步接收全部输入信号，仅向硬件比对模块输出运算结果；
3. 硬件比对模块：对比两颗 CPU 的地址、数据、控制信号输出，检出故障后切断 ECU 对外输出；Delphi 方案中故障后 CPU 保持运行，方便故障诊断；
4. 数据流监视器 DSM：内存映射模块，可后台自主并行测试存储器，CPU 占用总线时对数据流生成校验签名；配套辅助防护：RAM 奇偶校验、关键外设备份、独立辅助时钟振荡器与故障检测电路。

**05**

**LockStep 锁步功能的使用方法**

锁步属于硬件安全机制，操作简单，仅需配置对应寄存器完成使能即可，以英飞凌 Aurix TC39x 芯片举例：该芯片总计 6 颗内核，Core0 出厂默认锁步模式；Core1、Core2、Core3 可手动开启 / 关闭锁步；Core4、Core5 不支持锁步功能。

**核心配置寄存器**

1、LCLCON0、LCLCON1：锁步控制主寄存器

1. LSEN0/LSEN1/LSEN2/LSEN3：对应 4 颗内核锁步使能位，置 1 开启锁步，置 0 关闭；
2. LS0/LS1/LS2/LS3：只读状态位，反馈内核当前运行模式，1 代表锁步模式，0 代表普通单核模式。

2、配置限制：上述寄存器仅能由启动固件操作，通过 BMI 启动管理单元完成配置。

**故障告警通路**

锁步故障信号默认接入 SMU 告警通道 ALMx [0]、ALM8 [18]，x 对应发生故障的内核编号。

**06**

**LockStep 锁步功能的测试方式**

**1. 故障注入自测试原理**

只有芯片硬件出现永久或瞬时故障才会触发锁步报错，直接硬件故障测试难度较高，因此芯片厂商内置自检电路，提供故障注入接口，TC39x 的自检逻辑如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaDUNNhurDUKWDpUqCDcwib2qicuB9ia1bLGaRzkTFPibyDJkKBgTl0Q4JDzl0LykQp8sUVCE578vfic9NDdUCosEWbKJwHtAGQAxYoA/640?wx_fmt=jpeg&from=appmsg)

故障注入工作原理图

1. 故障生成模块负责注入故障，自由运行二进制计数器采用格雷码编码，经译码定位待测试电路节点；
2. 自检电路每 8192 个时钟周期遍历测试全部节点，交替向比对器 A 侧、B 侧注入故障；完整一轮全节点自检周期为 16384 个时钟周期；若同一周期同时存在真实硬件故障与注入故障，两处故障会相互抵消，无法检出；
3. 故障编码模块记录故障节点索引，输出两组数值：从最小索引向上检索到的首个故障节点、从最大索引向下检索到的首个故障节点；
4. 锁步硬件无异常时，编码输出数值为 0 或本次自检注入故障的节点编号；系统会通过独立监视计数器校验编码数值、输入计数器数值，数值不匹配则向 SMU 上报自检故障。

**2. 对应配置寄存器**

LCLTEST 为锁步自检寄存器，LCLT0、LCLT1 比特分别控制 LCL0、LCL1 通路故障注入：置 0 不注入故障，置 1 开启故障注入。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaAsicI4svCyN6IYK7e1hn5g12icMyMxo86dGk86THG079RcBcKxlzayvxibpjJAw8ibYlohCPdRGJEJCmdKTgWnlQMhSDDSDZMrFS8/640?wx_fmt=jpeg&from=appmsg)

故障注入寄存器

来源：

https://zhuanlan.zhihu.com/p/669171808

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaD9qjQXZdMwY876TkFlhIUib1kn4wc72e4cib9eharylSOXtAgAq234jTmZYKrXsGd0OALDotYN7MYS8h0mElMEuPddlDZic56KCg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572912&idx=3&sn=58184d21d6dabc713e8d93a0c1d80e40&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247573595&idx=1&sn=425c418664766cc4030f3cb49a733ec6&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247557132&idx=2&sn=2e44d4c2d77a2eec377d0553442d2c1b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561775&idx=1&sn=948a9e7f8d4fbed363c6a6a5479cd39e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkfxA4GZice84BsCR4zGV0oqJXpEjUsUpGKcFcCx1BiaDYDQU4cT3nTtpA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561260&idx=2&sn=0ca6395502487515a921f32288b7e8df&scene=21#wechat_redirect)

**专业社群**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJnASqAJY7...