---
title: 【S&P 2022论文分享】以Protocol为中心的UEFI固件SMM提权漏洞静态检测
url: https://mp.weixin.qq.com/s?__biz=MzA4ODYzMjU0NQ==&mid=2652312716&idx=1&sn=a9dc5e61b6a12c595f594002d685994d&chksm=8bc48902bcb30014ce28544f1a191a8ea7b17b35199b3f9de1d05f66596afc117f9c99a7467e&scene=58&subscene=0#rd
source: 网安国际
date: 2023-03-25
fetch_date: 2025-10-04T10:38:39.452572
---

# 【S&P 2022论文分享】以Protocol为中心的UEFI固件SMM提权漏洞静态检测

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icelxY6ibIXSW10S48wtYJr7mAbheaW8A33fq8H10jibm3DUDhakVLE0XaXzXnibGUUdm5kCx9Rdhic9EgyZ1w8Ajrw/0?wx_fmt=jpeg)

# 【S&P 2022论文分享】以Protocol为中心的UEFI固件SMM提权漏洞静态检测

原创

尹嘉伟 等

网安国际

**前言**

本文根据英文原文“Finding SMM Privilege-Escalation Vulnerabilities in UEFI Firmware with Protocol-Centric Static Analysis.”整理撰写。原文发表在IEEE Symposium on Security and Privacy. 2022。本文较原文有所删减，详细内容可参考原文 。原文作者为尹嘉伟、李孟豪、吴炜、孙丹丹、周建华、 霍玮、薛晶灵。

01

**介绍**

BIOS（Basic Input/Output System），即基本输入输出系统，负责在通电引导阶段进行硬件初始化，并为操作系统提供运行时服务。而随着云计算、物联网为代表的互联网的快速发展，运行在16位寻址的实模式的BIOS已经不能满足计算机系统的快速发展。因此，英特尔、AMD等厂商联合设计了UEFI (Unified Extensible Firmware Interface）规范，即可扩展固件接口规范。UEFI规范定义了一系列操作系统和硬件交互所需的标准接口。UEFI固件提供两类服务，一类是启动引导服务，另一类是运行时服务。系统加电以后，首先执行的是启动引导服务，其负责在通电引导阶段运行硬件以及运行时服务驱动初始化并校验固件的完整性。而运行时服务实现操作系统对于硬件的安全访问控制，其功能主要包含：提供处理器过热保护等安全防护措施、电源管理、SPI Flash等硬件资源的访问控制以及微码更新。并且，UEFI固件定义了操作系统和底层硬件的安全边界，因此UEFI固件是整个计算机系统的信任基。

为了提供对外围硬件的安全访问控制，UEFI固件为操作系统提供了诸多运行时服务，例如系统电源管理服务、SPI闪存读写服务以及硬件错误处理服务。在Intel以及AMD计算机平台中，这些运行时服务由系统管理中断 (System Management Interrupt, SMI) 处理程序提供。SMI处理程序具有对系统底层硬件的访问控制能力，这也使得SMI处理程序成为恶意攻击者的重要攻击目标。并且，最近的研究表明，利用商用UEFI固件的SMI处理程序中存在的运行时服务漏洞，攻击者可以对计算机系统的关键底层硬件，例如SPI Flash以及电源管理等实施攻击。

为了保护UEFI固件提供的运行时服务的安全运行，在基于Intel和AMD的平台中，UEFI固件基于CPU以及内存实现了硬件隔离机制以实现对运行时服务的访问控制。基于CPU，Intel以及AMD实现了名为系统管理模式（System Management Mode，SMM）的CPU运行模式，SMM模式具有比内核模式更高的特权级别，是CPU的最高运行权限，运行在内核模式下的内核驱动程序只能通过SMI中断来访问运行在SMM模式下的UEFI固件运行时服务。

同时，UEFI固件在物理内存空间中保留了一个名为系统管理RAM (System Management Memory, SMRAM）的专用内存区域，SMRAM只能由运行在SMM模式下的运行时服务所访问，无法由内核态程序访问或修改。

虽然计算机系统部署了基于CPU以及物理内存实现的安全访问控制，但是运行于CPU最高权限下的运行时服务程序仍然暴露出严重的攻击面。例如，由于不完善的输入验证导致的内核模式到 SMM模式的权限提升漏洞。在过去的几年里，一些SMM权限提漏洞已经被UEFI固件安全研究人员相继披露。攻击者可以利用面向跳转的编程(JOP）的方式绕过运行时服务中部署的基于软件的缓解机制。例如 DEP/NX（数据不可执行）以及SMM\_CODE\_CHK的保护机制。

其中，SMM\_CODE\_CHK用于防止SMRAM中的运行时服务执行SMRAM之外的代码，SMM\_CODE\_CHK类似于内核态驱动程序的管理模式执行保护(System Management Execution Protection, SMEP)。并且由于UEFI固件运行时服务的运行资源有限，目前商用计算机系统上的UEFI固件大多没有部署诸如DEP/NX等缓解机制。因此，基于目前UEFI固件运行时服务防护措施缺失的现状，英特尔提出了几种基于硬件的缓解机制（例如，SMI Transfer Monitor, STM ）。然而，正如Intel 2020 年白皮书中所述，“大多数当前的 BIOS 不支持 STM 或其他 SMM 监视器”，因此总结当前SMM提权漏洞成因特征并且基于所提取的漏洞成因以及代码特征设计并实现自动化的SMM提权漏洞静态检测工具是具有迫切需求和价值的。

针对当前UEFI固件漏洞研究缺失的现状，本文对 UEFI 固件中存在的 SMM 权限提升漏洞进行了系统研究。通过分析，本文发现，尽管在现代CPU中部署了诸如权限控制等硬件隔离以及SMM\_CODE\_CHK等漏洞缓解机制，然而，攻击者仍可以利用SMI处理程序存在的漏洞绕过现有的漏洞防护机制，进而实现SMM提权攻击。并且，运行在处理器的最高特权下运行时服务以低特权可控数据作为输入，目前缺乏相应保护机制确保低权限可控数据已经过完备的有效性验证。并且，从运行于CPU最高特权(ring -2）下的SMI 处理程序运行在CPU最高特权(ring -2）级别下，因此，对于SMI处理程序来说，可以被操作系统权限(ring 0）的内核态程序访问控制的数据被认为是不受信任的。如果SMI处理程序使用了没有经过完善安全校验的不可信数据，并且不可信数据影响了SMI处理程序的控制流或数据流，则可能引入输入验证不当导致的漏洞，此类漏洞可能被用来劫持SMI 处理程序的控制流，进而实现权限提升攻击。

此外，本文还基于UEFI规范对SMI处理程序的执行模型进行了深入地总结和分析。在此过程中，本文发现除了上述不可信数据引入的漏洞，SMI处理程序中还存在使用UEFI固件启动阶段在非SMRAM区域创建和初始化的对象的情况，由于非SMRAM区域的对象内容可以被运行于内核态权限的内核驱动程序所修改，因此，具有内核权限的攻击者可以通过控制这部分数据影响目前SMI处理程序的执行状态，进而实现SMM提权攻击。本文将非SMRAM区域创建和初始化的对象的引用称为逃逸引用(Escaped reference)，不符合安全规范的逃逸引用可能会在SMI处理程序中引入SMM提权漏洞。通过对商用UEFI固件的逆向分析，以及对SMI处理程序的执行模型的深入分析，基于逃逸引入的创建、初始化以及使用方式，本文分类总结了两种类型的逃逸引用，遗留引用(Legacy Reference）和非预期引用(Unintential reference)。此外，通过分类总结，本文给出了SMM提权漏洞的定义，并以该定义为基础，设计并实现了用于检测运行时服务漏洞的静态分析框架。

由于UEFI固件映像是去掉符号的二进制文件，并且UEFI固件中存在大量基于回调(Callback）机制实现的跨文件的间接调用。在回调机制下，一些函数地址被存储到名为Protocol的结构体对象中，而每一个不同的Protocol结构体均由一个全局唯一标识符(Globally Unique Identifiers, GUID）所标识。当前静态分析无法准确识别基于Protocol-callback机制实现的跨文件的间接调用的目标函数，进而造成大量漏报。

针对这样的问题，提出了以Protocol为中心的UEFI固件提权漏洞静态分析方法来检测UEFI固件中存在的SMM提权漏洞。基于所提出的方法本文实现了名为SPENDER的静态分析框架，其用于高效、准确地发现UEFI固件中隐藏的SMM权限提升漏洞。SPENDER 在对1148个无符号商用UEFI固件镜像的静态分析过程中，总共发现了36 个漏洞（包括两个先前已知的 1-day 漏洞和 34 个未知的 0-day 漏洞），在检测过程中，SPENDER的误报率为 10%，SPENDER分析一个 SMI 处理程序的平均时间为12.46秒。

02

**背景**

**1. UEFI固件与SMM驱动**

UEFI固件主要包含五个模块：安全(Security, SEC）模块、EFI预初始化(Pre-EFI Initialization, PEI）模块、驱动程序执行环境(Driver Execution Environment, DXE）模块、系统管理(System Management Mode, SMM）模块和引导设备选择(Boot Device Selection, BDS）模块。其中，SMM模块由一系列SMM驱动程序组成，SMM驱动程序中包含一系列SMI处理程序，正如前文所述，SMI处理程序为上层操作系统提供许多运行时服务，以实现对整个计算机系统至关重要的外围硬件的安全访问控制。

**2.SMM驱动执行模型**

图 1描述了SMM驱动的执行模型，SMM驱动的整个生命周期主要分成两个阶段：启动阶段 (Boot Phase) 和运行时阶段 (Runtime Phase)。

![](https://mmbiz.qpic.cn/mmbiz_png/icelxY6ibIXSW10S48wtYJr7mAbheaW8A3EFzQUST6gGaeBcEznSibaiavEWywhuQYuEG15Hkv7k4KbQWc3vpXg12g/640?wx_fmt=png)

**图 1 SMM驱动执行模型**

l 启动阶段：在启动阶段，如图 1(a）所示，UEFI固件利用DXE模块的初始化函数 (Initialization function) 执行三个初始化操作。首先，DXE模块分配和初始化数据对象（本文称为Boot-only对象），在本文中，我们将 Boot-only对象所在的内存区域，称为DXE-DATA 区域(①)，DXE-DATA区域位于SMRAM 之外。其次，DXE模块利用Boot-only数据对象调用SMM模块中的初始化函数，该初始化函数会将所有SMM驱动加载到SMRAM中并执行已加载SMM驱动的初始化函数（②）。最后，DXE 模块会将SMRAM锁定，至此，SMRAM无法被运行于内核权限的内核驱动代码所访问（③）。

l 运行阶段：在运行时阶段，如图 1(b）所示，运行于内核权限的内核驱动代码通过如下三个步骤与SMI处理程序进行交互。首先(步骤1)，内核驱动代码在CommBuffer 中填充SMI处理程序执行所需的上下文信息，例如SMI处理程序序号以及所需输入数据等。CommBuffer是一个分配在DXE-DATA区域的缓冲区，内核权限下的驱动程序利用该缓冲区存储SMI处理程序执行的上下文信息，并为SMI处理程序提供输入。SMI处理程序利用该缓冲区为运行在内核权限下的程序返回中断请求结果。之后(步骤二），运行在内核权限下的驱动程序 触发SMI中断，当CPU接收到SMI 中断时，CPU会将自身权限提升到SMM权 限，并调用存储在SMRAM中的名为 SMM dispatcher的函数。SMM dispatcher函数会根据CommBuffer中保存的SMI handler序号，调用相应的SMI handler，以响应内核权限下内核驱动程序的相应请求。

*（本文只选取原文中部分章节，更多精彩内容敬请期待后续出版的《网络安全研究进展》）*

**作者简介**

尹嘉伟，中国科学院信息工程研究所在读博士生。主要研究领域为计算机可信基的攻防技术。设计并实现了UEFI漏洞自动化检测工具，该工作已经发表于S&P 2022（CCF A）。迄今为止，共挖掘UEFI零日漏洞146个，获得CVE编号68个，涉及Microsoft，Intel，AMD，Lenovo，HP，Dell, Insyde以及ASUS等厂商；利用所挖掘到的零日漏洞获得Google，Intel，Lenovo，HP，Dell，Insyde以及ASUS等厂商公开致谢。获得Intel高危历史漏洞积分第一、Intel全球安全名人榜第二、Dell安全研究人员名人堂全球排名第一的成绩；入选ASUS全球安全研究人员名人堂、微软2022第三季度LeaderBorad。利用挖掘到的UEFI固件零日漏洞，参加2019年天府杯原创漏洞演示复现赛，成功演示复现；挖掘华为鲲鹏服务器漏洞，获得华为鲲鹏2021年度公开致谢。

**相关阅读**

[【Usenix Security 2022论文分享】StateFuzz: 状态敏感的Linux内核驱动模糊测试](http://mp.weixin.qq.com/s?__biz=MzA4ODYzMjU0NQ==&mid=2652312709&idx=1&sn=1136f7e8c312bed8e2a80faf207da7c4&chksm=8bc4890bbcb3001d68c440333dce13b563a93784653fc764a4027fdfd7cdd4000901a9d5dd67&scene=21#wechat_redirect)

[【NDSS 2022 论文分享】基于无线网流量指纹分析的APP行为隔空识别](http://mp.weixin.qq.com/s?__biz=MzA4ODYzMjU0NQ==&mid=2652312701&idx=1&sn=d1439a37bbef1c524b11812da22a9a9c&chksm=8bc489f3bcb300e5540ba2db1581b3ee3cd158ae78b9820d5824d21b022cb5f464ff9e32daad&scene=21#wechat_redirect)

[【S&P 2022论文分享】移动博彩诈骗的数据分析](http://mp.weixin.qq.com/s?__biz=MzA4ODYzMjU0NQ==&mid=2652312680&idx=1&sn=bf14db7f4985fedc996f4cac62337707&chksm=8bc489e6bcb300f02e44dbb4404bc70b3f103bd57a130b238ef30cb418f1b0eb4d476e1b023c&scene=21#wechat_redirect)

[【USENIX Security  2022论文分享】揭示垂直联邦学习中存在的标签推断攻击](http://mp.weixin.qq.com/s?__biz=MzA4ODYzMjU0NQ==&mid=2652312275&idx=1&sn=f453438c42b5676b01f01acbe495e28d&chksm=8bc48f5dbcb3064b23fbb8a9246394716afd7917e37199d4f21da340745defd2db404efc7d21&scene=21#wechat_redirect)

[【DSN 2022论文分享】Invoke-Deobfuscation: 基于AST和语义保持的PowerShell脚本反混淆](http://mp.weixin.qq.com/s?__biz=MzA4ODYzMjU0NQ==&mid=2652312255&idx=1&sn=260c8da492bfa3b4867c41be6d37909d&chksm=8bc48f31bcb306275802f97a29880f761de59c02ecd1cdccc4e627c4f638e02ee2bb1574da3a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/icelxY6ibIXSW10S48wtYJr7mAbheaW8A32gEFRF62zVuLESSmkenZBW1Fk0tafAD4z46iaUJQXUWUe5ricne4Dw5g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/icelxY6ibIXSW10S48wtYJr7mAbheaW8A3Nqjk6hEThqZAZG6HNEH00dWSBt3d3VyYic4MSsuJlKVZMVhEU93rChg/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icelxY6ibIXSVlNf68NLWmpfibn7F9KsZzNAIDY1JCxHTWxVibDXwxJ6Pb5voAqiaweFCkQUPb6SJ51jPQ3iaAk8dGJw/0?wx_fmt=png)

网安国际

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icelxY6ibIXSVlNf68NLWmpfibn7F9KsZzNAIDY1JCxHTWxVibDXwxJ6Pb5voAqiaweFCkQUPb6SJ51jPQ3iaAk8dGJw/0?wx_fmt=png)

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