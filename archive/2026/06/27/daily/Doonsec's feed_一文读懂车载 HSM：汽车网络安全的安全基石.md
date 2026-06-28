---
title: 一文读懂车载 HSM：汽车网络安全的安全基石
url: https://mp.weixin.qq.com/s/la_RXZMvAFvDFHkTtykP0Q
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:09:21.229168
---

# 一文读懂车载 HSM：汽车网络安全的安全基石

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaBTHXciaJBPxoZ3ChJhcFye3NqPn8nJ08DUSdenqia3icDNag9RHpmQShNdv9XQkZEictpnOXpBamiadZdoW8nMONfV18uSM0EV0e1U/0?wx_fmt=jpeg)

# 一文读懂车载 HSM：汽车网络安全的安全基石

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

**硬件安全模块 HSM 基础概念**

谈及信息安全与加解密工作，我们常会用锁与钥匙做类比，这里用一个生活化场景通俗解释 HSM：

一位父亲给三个儿子各购置一台掌上游戏机，为防止孩子沉迷，他把每台机器单独收纳进可上锁的盒子，盒子交由孩子自行保管，但钥匙统一由父亲留存。孩子想要游玩时，必须把盒子送到父亲处解锁；钥匙绝不会交给孩子，避免孩子私自配钥匙。而盒子不长期放在父亲身边，是考虑到父亲不便随身携带过多物品。

这个场景里，父亲是整套安全体系的核心依托，对应到技术领域就是 HSM。HSM 全称 Hardware Security Module，中文名为硬件安全模块，核心价值是管控机密数据、执行各类密码学运算。

它属于一类计算机硬件设备，专门用于保管、保护高等级身份认证体系用到的密钥与各类敏感信息，同步配套完整密码学操作能力。HSM 所有功能围绕加密、解密展开，既能隔绝未授权主体，保障只有合规接收方、合规应用程序可读取敏感数据，也能提供安全解密手段，保障传输信息的机密性与真实性。

HSM 的安全功能专业且单一，行业普遍存在一项工程需求：在保障安全能力达标的前提下，尽可能降低算力消耗、提升运算效率。该需求在工程乃至各行各业都十分常见，对应的解决思路是搭载专用硬件资源，也就是硬件加速器，依靠定制集成电路或专用硬件单元分担运算压力。

传统 IT 领域的 HSM 多以拓展板卡、外接设备形式，直连电脑或网络服务器；伴随云计算技术成熟，云端 HSM 应运而生，同样承载敏感数据管理、加解密运算等安全服务，文中附带 Utimaco 云端 HSM 架构示意图。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaB4ucchaPu1LE5Cm52h25luxN9GQr8PCzgb3gWicyjBtfmXlKpOQMe0AsNdTypicLagW1x29ib3IeBjricZ3RibC71J71mfvBiadtZZA/640?wx_fmt=png&from=appmsg)

图：Utimaco 云端HSM的架构示意图

**02**

**车载场景下的HSM**

大众谈及汽车安全，第一反应大多是行车安全、碰撞测试、安全气囊等硬件防护，但汽车安全覆盖维度更广。如今车辆全面联网、智能化程度持续提升，车载信息安全的重要性愈发突出，相关机构早已提前布局相关研究。

早在 2008 年，欧盟就出资启动 EVITA 车载安全项目，全称 E-safety Vehicle Intrusion Protected Applications，目标是强化车载网络、车联网 V2X 业务的网络攻击抵御能力。项目梳理车载电子电气使用场景，排查潜在安全威胁与对应风险，梳理出整套车载网络安全规范，并将研究成果转化为标准化文档，给出可落地的软硬件架构设计指引。

EVITA 项目还划定了车载 HSM 硬件分级规范，依据硬件安全性能划分为 Full HSM、Medium HSM、Light HSM 三类，这套分级标准目前广泛应用于汽车网络信息安全行业，核心差异如下：

1. Full HSM 与 Medium HSM：区分标准为硬件是否搭载非对称加密加速单元；
2. Medium HSM 与 Light HSM：区分标准为是否配备独立运算存储单元、内置真随机数发生器。

配套 EVITA HSM 分类对照表可直观区分三者硬件能力差异。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAEYzedHk75BbMn1CDCjrH5eVxzNBheSeDsb5cIglgoWXdKSok1CZPHCPGwWAnP7ZIIElLgvgvoO2BcQmk1L0ptSvVAqd084yU/640?wx_fmt=png&from=appmsg)

**03**

**英飞凌 AURIX 芯片集成的 HSM 模块**

下面以英飞凌 AURIX 系列芯片内置 HSM 为例，讲解车载 HSM 硬件落地形态。

狭义层面的 HSM 单指硬件载体，汽车电子领域中，它要么是独立芯片，要么是主控芯片内部隔离的专属分区。互联网行业成熟安全芯片品类繁多，但能满足严苛车规可靠性标准的产品十分有限，英飞凌 AURIX 系列芯片广泛装车，且原生集成 HSM 硬件单元，其内部框架结构包含以下组件：

1. 32 位 ARM Cortex M 处理器，主频最高 100MHz；
2. 专属隔离保护存储区；
3. BootRom 启动固件，支撑安全可信启动功能；
4. AES128 对称加密硬件加速器，CMAC 消息验证码加解密吞吐速率超 25MB/s；
5. 真随机数发生器 TRNG，用于密钥生成、挑战应答校验等场景。文中附 AURIX 芯片 HSM 内部框架示意图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCaZ9KSXHYL7yjmTZ33za3jDsofIDKLkzeD3SmmqkJTqPzPhPO1viaBaS47HcQibo3PQ57vrYlyRpZ6UCliaT5mrbhNjLIlicQHicLA/640?wx_fmt=png&from=appmsg)

图：AURIX的HSM框架图

补充介绍模块核心算法单元 AES 加速器与 CMAC：

AES 全称高级加密标准，是主流对称加密算法，常用 AES128、AES256 两个版本，二者区别在于密钥长度（128 比特 / 256 比特）与加密迭代轮数（10 轮 / 14 轮），日常 WiFi 加密设置中也常出现 AES 选项。AURIX 集成的加速器专门适配 AES128，针对 128 比特数据定制专属叠加、移位、替换运算电路。

CMAC 全称为基于密码的消息认证码，依靠密钥搭配对称加密算法（如 CBC-MAC）生成校验码，通过比对 CMAC 数值完成权限校验与身份核验，车辆安全启动流程也依靠校验固件 CMAC 实现可信验证。

配套逻辑框图展示 HSM 与芯片其余模块的连接关系：HSM 经由系统外设总线 SPB 和芯片其他单元通信；存储程序、数据的 PFlash、DFlash 为芯片全局共享存储，但可通过 TriCore 内核访问权限管控，隔离保护 HSM 专属存储分区，杜绝非法读取、篡改，各类安全密钥统一存储在 DFlash 分区内。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAYU25Hhz7ftr8T3aiaBEU28E0BKajRCTn5WwE6jZ8PwQ2K2ibMpcfvlyun5DXfRtIWo1gbR62T6qKf1UgGswCCVjeKwMKWhRAf8/640?wx_fmt=png&from=appmsg)

图：HSM及AURIX芯片内其他部件的连接框图

**04**

**AUTOSAR 标准中的 HSM 软件交互接口**

广义 HSM 除硬件本体外，还包含配套固件与驱动程序，车载电子软件体系核心规范 AUTOSAR 针对 HSM 设计了完整密码学软件栈，适配车辆联网、智能化带来的信息安全需求，整套密码栈分为 CSM、CryIf、CryDrv 三大模块：

1. CSM（密码服务管理器）：上层调用加解密功能的统一入口。应用层软件组件通过 RTE 调用 CSM，底层基础软件、复杂驱动可直接对接；同时统一管理安全任务队列，实现任务优先级调度；
2. CryIf（密码接口层）：承接 CSM 下发指令，内部每一项加密基础功能都对应 CSM 一类服务，支持任务分发，可调度不同软硬件驱动，分别处理对称、非对称加密等运算；
3. Crypto Driver（密码驱动）：底层硬件交互单元，直接操控加密加速器、真随机数发生器等硬件，完成实际加解密运算。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBa1sgic1iavrNwWSws5vic7422OZhiaSjc0CPAAF0IpWRTZ7PWEDG1ZxvUs0jvJc54icTvCo7qEDhO05tb1zD88BBiarnsj5lCLPKmY/640?wx_fmt=png&from=appmsg)

图：AUTOSAR中HSM相关模块的框图

**05**

**Vector 厂商 HSM 固件解决方案**

Vector 是业内主流 AUTOSAR 底层软件供应商，推出了符合 AUTOSAR 规范的完整 HSM 固件方案，配套架构示意图如下：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCrictqiaNZM40nHSce9geibhtl36ibkpicicY44xhAUY7FGB0qicuD6ltPJ7kLHfVrvaCT3SSrc7WHc0qU8FK1TEc3eIQT8lxR8I4Wck/640?wx_fmt=png&from=appmsg)

图：Vector的HSM固件方案

方案内 vHSM 加密模块对应 AUTOSAR 标准中的 CSM，向上为应用层、底层基础软件提供统一抽象加解密服务；CryIf 接口层依靠进程间通信、共享内存机制实现，根据安全启动、SecOC 车载安全通信等不同业务场景，调度对应底层驱动，对接加密硬件加速器、密钥存储隔离内存等硬件资源。

整体 HSM 固件和芯片硬件深度绑定，需匹配对应芯片型号开发适配。

**06**

**硬件安全模块 HSM 的性能优化能力**

**1. 原生硬件架构从底层筑牢安全防线**

伴随车内互联设备持续增加，混合式车载网络对 “安全左移、软硬件解耦、软件迭代更新” 提出更高要求。集中式车载架构落地后，可统一管控全车信息安全能力，同时保障各域控制器外接 ECU 的运行安全，而 HSM 是实现 SecOC 车载安全通信不可或缺的核心部件。HSM 能够校验所有车载交互数据真实性，阻断攻击者绕过 ECU 安全接口、非法侵入主控芯片与车载网络的路径。

集中式车载架构还存在另一项痛点：车载计算平台会整合多套 ECU 功能，内部划分多虚拟机运行多类软件应用，安全防护需求同步激增，新一代 HSM 硬件架构可适配这类集中化算力平台的安全需求。

**2. 独立内核分担安全任务，适配实时操作系统**

HSM 全部安全运算逻辑封装在专属处理器内核中，依靠配套软件协议栈调度运行。整车主控芯片可专注处理车辆业务逻辑，HSM 内核独立承载全部安全工作，包含车载加密通信、运行入侵检测、安全启动、固件刷写、日志记录、调试安全管控等，防护能力远优于纯软件安全方案。

集中式车载计算平台会出现多应用同时调用加密接口的场景，普通 HSM、纯软件加密方案很难兼顾多数据流实时处理。新一代 HSM 搭载实时操作系统与灵活会话调度机制，可高效并发处理多路安全请求。

**3、多核/多应用的支持**

面向未来车载电子架构，多内核并行发起加密请求已成常态，新款 HSM 固件最多支持 16 组并行加密会话，会话数量可按需配置。

实现多核、多应用并发的核心在于专属固件驱动架构：各虚拟化应用可独立集成驱动，便于软件模块分开开发；系统集成阶段通过链接器统一调度，驱动多实例共用硬件共享内存资源。每个应用生成独立会话通道，驱动可同步处理多路主机内核下发的加密请求，配套示意图展示多核心并行会话处理逻辑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaC26w4tjvhR7Yr1U7nKcPfkM6VM3icFwLtIFFGMxmcOM0Zrh27X4UpzUNGRWbia3QhV79dok2cZy1w3EFUADc0L92SRvFN9s7DOA/640?wx_fmt=png&from=appmsg)

图. HSM固件在并行会话中处理来自多个主机核心的请求

整套架构的核心交互单元为主机 - HSM 桥接模块，负责打通主机系统与 HSM 子系统，统筹两端全部数据交互，隔离主机与安全内核，管控双向数据流。桥接模块寄存器会缓存主机下发的加密请求队列，基于 HSM 硬件资源负载最优原则调度任务，缩短安全运算响应耗时，新一代 HSM 软件完整落地多核、多应用并发能力。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCtvibAYOJ4eWN4CGp4jiaSPOeBVb9APWaZslAtRz4icwA1EtPicg3BfjTt8H5ic5GPoSl1Mfiaib7Anb8AhhPrqSlyVGT0VH5iaXFwrL4/640?wx_fmt=png&from=appmsg)

图. HSM固件在并行会话中处理来自多个主机的请求

**4. 批量消息验证码机制大幅提升实时运算性能**

新一代电子电气架构下车载通信数据量暴涨，需要同时兼容 CAN/CAN FD、车载以太网多类总线加密传输，保障海量协议数据交互安全，批量 MAC 接口是 HSM 应对该场景的核心优化方案。

工作逻辑：主机先收集一段周期内全部待校验报文，通过桥接模块寄存器一次性批量下发至 HSM；HSM 内核统一完成全部报文校验运算，再批量回传结果，仅单次数据交互即可完成百条报文处理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBPpEvpAbz5AEDH7z6g7opovJE75dRib6gJ5s0xSVw1t82RGKp2TdImXgZayNRI1b6mFd2TavD76JrjbIsSE36beuUfc6icyZNyM/640?wx_fmt=png&from=appmsg)

图. HSM固件在并行会话中处理来自多个主机的请求

以 100 条报文举例，假设单次主机与 HSM 数据传输耗时 10 微秒，逐条处理总延迟可达 1 毫秒，会对车载实时系统造成压力；采用批量 MAC 接口后，处理耗时可压缩至原有百分之一。该功能对搭载域控制器、车载计算平台、存在大量 PDU 交互的车企十分友好，可在海量报文场景下维持车载通信实时加密校验，目前批量 MAC 功能已集成进新一代 HSM 固件。

**5. 适配未来车载架构的定制化 HSM 方案**

车载网络全面向集中式域控平台转型，软硬件分层解耦成为行业趋势，HSM 是保障这类平台安全的核心硬件。它不仅能依靠 SecOC 保护域控外接 ECU 的 CAN/CAN FD 通信数据，防止数据篡改、非法读取，还可支撑高安全等级、大流量、高实时性车载应用稳定运行。新一代 HSM 原生适配多核、多应用场景，搭配批量 MAC 接口，即便面对异构格式、超大通信流量，也能保障加密通信实时性。

结合车载网络多元化、自动驾驶持续落地的行业趋势，各大车企会基于自身电子电气架构制定专属安全规范。新一代 HSM 固件支持定制开发，可匹配车企差异化安全标准；固件适配主流新款车规微控制器，主机驱动以源代码形式交付，方便车企、零部件厂商复用、二次开发。兼具高性能与灵活定制能力的新款 HSM 固件，是未来集中式混合车载网络安全防护必不可少的核心组件。

来源：

1、E-safety Vehicle Intrusion Protected Applications (EVITA)，

https://argus-sec.com/e-safety-vehicle-intrusion-protected-applications-evita/

2、How hardware security modules enable AUTOSAR，

https://www.embedded.com/how-hardware-security-modules-enable-autosar/

3、Vector Cyber Security Solution – vHSM Firmware，

https://assets.vector.com/cms/content/events/2018/Webinars18/Vector\_Webinar\_MICROSAR\_HSM\_20181127.pdf

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez7...