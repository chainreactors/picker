---
title: 浅析TrustZone架构
url: https://mp.weixin.qq.com/s?__biz=MzI0Njg4NzE3MQ==&mid=2247490763&idx=1&sn=453bcd0289f6c0bf154bc8746f2765c3&chksm=e9b93aa7deceb3b129010c0eca72540c90fdd7ae58553b7bf829cf8671813cc462d5a44a7cf5&scene=58&subscene=0#rd
source: vivo千镜
date: 2023-03-30
fetch_date: 2025-10-04T11:08:15.071568
---

# 浅析TrustZone架构

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpD1HbuUxMLPhuv2ZHoicIicMicXDxAPIsJSWyTQkMA0ibibCDZqcfDtPuk9rPbcfSOl9bOLKuk9x15l7sA/0?wx_fmt=jpeg)

# 浅析TrustZone架构

迎风

vivo千镜

**PART****0****1**

**引言**

##

随着移动互联网时代的发展，智能手机已经融入到人们的日常生活和工作中，人们可以使用智能手机与好友实时聊天，可以使用智能手机拍摄美景，可以使用智能手机进行指纹支付，还可以使用智能手机处理工作邮件，等等。在便捷我们生活和工作的同时，智能手机不可避免地存储着包括聊天记录、照片、视频、指纹等个人数据，而这些数据或多或少涉及用户的隐私，使得用户对智能手机的隐私保护能力有一定需求。

为了满足用户的隐私保护需求，**千镜安全实验室推出千镜安全架构，从应用层、框架层、内核层、芯片层这四个层级对用户的隐私进行保护，而TrustZone[1]属于芯片层级的保护，提供密钥存储、硬件加解密等硬件安全能力，能够有效保证指纹、个人身份信息等关键隐私数据不被破解、窃取。**

##

**PART****0****2**

**TrustZone架构**

##

TrustZone是一种在ARM指令集芯片上实现可信计算的架构，例如智能手机中的高通芯片、联发科芯片以及麒麟芯片都属于ARM指令集芯片。TrustZone通过划分所有的硬件和软件资源来构建两个世界：安全世界和普通世界。其中安全世界对应可信执行环境（Trusted Execution Environment，TEE），而普通世界对应富执行环境（Rich Execution Environment，REE）。如图1所示，深蓝色部分为安全世界，浅蓝色部分为普通世界。此外，为了细化安全世界和普通世界结构，ARMv8定义了异常等级来进行权限控制，将异常级别从低到高划分为EL0-3四个层级：EL0对应用户模式，可以运行一些应用程序；EL1对应内核模式，可以在该层级运行操作系统，为EL0层提供系统调用接口，实现硬件的控制；EL2对应管理程序模式，可以对OS进行管理，完成不同OS的资源分配；EL3对应安全监控模式，运行ARM可信固件（ARM Trusted Firmware，ATF），负责两个世界的切换。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpD1HbuUxMLPhuv2ZHoicIicMicEibvbiajicWadAgoVicd8ibxibxhTuC3H5EI4vEza1IKiasRAkvLo8t4whCKw/640?wx_fmt=png)

图1 TrustZone异常级别[2]

如果在EL0、EL1、EL2时需要完成安全世界与普通世界之间的切换，需要先转换到EL3中。无论是普通世界还是安全世界，从低层到高层的转换需要调用指令[3]，如图2所示，对于EL0而言，可以通过调用SVC（Supervisor Call）指令进入EL1层；对于EL1而言，既可以通过调用HVC（Hypervisor Call）指令进入EL2，又可以通过调用SMC（Secure Monitor Call）指令进入EL3；对于EL2而言，可以通过调用SMC指令进入EL3。由于SMC指令和HVC指令未在EL0中进行定义，只能在EL1及更高的异常级别上调用，故EL0想要切换到EL3必须先切换EL1，再由EL1切换到EL3。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpD1HbuUxMLPhuv2ZHoicIicMichlocrDQh5LcqHP08IK6FAicQfenopGB9URknAfQwTgp75gacm3zKbOg/640?wx_fmt=png)

图2异常级别请求指令

为了支持TrustZone，需要对系统各个子模块进行设计和扩展，本文主要介绍六处进行软件支持或者硬件扩展的模块，具体系统框架如图3所示。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpD1HbuUxMLPhuv2ZHoicIicMicbKCZTibMDaoAkGksHcL5ibx1b4svmypqiaqoANwfLoDc3qrpvJ4eMAc5A/640?wx_fmt=png)

图3 基于TrustZone的系统框架[2]

① **物理核（即CPU）虚拟化**：通过配置物理核中的安全配置寄存器（Security Configuration Register，SCR）最低位NS（Non-Secure）位完成物理核的虚拟化，将物理核虚拟成安全核和非安全核，其中安全核用于运行安全世界的代码，非安全核用于运行普通世界的代码，物理核以时间分片的方式执行来自安全世界和普通世界的代码。与此同时时，也有两个状态与之对应，安全状态对应安全世界，非安全状态对应普通世界。这些状态由NS位决定[4]，如图4所示，当NS位为“0”的时候表示安全状态，当NS位为“1”的时候表示非安全状态，NS位由EL3进行配置。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpD1HbuUxMLPhuv2ZHoicIicMicbz39OCuKcXwyoHLdNRnWLAsYjJXWxvTK8bU4piarS9bzG9duI7vzyRA/640?wx_fmt=png)

图4 安全配置寄存器SCR[4]

② **总线扩展**：为了识别CPU的安全状态，需要对系统总线进行扩展，在总线的每一个读写通道增加了一个额外的信号控制位与SCR中的NS位相关联，具体到AMBA3 AXI（Advanced eXtensible Interface）总线中的控制位为AWPROT[1]和ARPROT[1]，其中AWPROT[1]负责写入事务，ARPROT[1]负责读取事务。当AWPROT[1]和ARPROT[1] 置为“0”时表示安全世界的事务，置为“1”时表示普通世界的事务。主设备在总线上发起事务时需设置这些信号，而从设备的解析模块会对主设备设置的信号进行辨识，以确保主设备发起的操作没有违规。

③ **外设扩展**：为了确保与总线相连的硬件能够识别总线新增的信号控制位，需要对外设进行安全扩展。新增一个TrustZone 保护控制器（TrustZone Protection Controller，TZPC）组件控制外设的安全特性，并且与AXI-to-APB桥一起配合，使得外设能够支持TrustZone特性。如图5所示，AXI-to-APB桥位于AMBA3 AXI总线和APB（Advanced Peripheral Bus）外设总线之间，负责APB外设地址与AMBA3 AXI总线地址的转换，而TZPC组件包含三组通用寄存器DECPROT{2:0}，每组通用寄存器可以记录8个DECPROT信号，每一个信号控制一个外设的安全配置，负责对应总线中的信号控制位，如果该信号为“0”，则表示该外设为安全外设，如果信号为“1”，则表示该外设为非安全外设。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpD1HbuUxMLPhuv2ZHoicIicMicOqkT7NsnAtiaHkoianJ30XEDaEkGHibdum5ZJMMhMmDGfYyhBeu1nbQXA/640?wx_fmt=png)

图5 使用TZPC实现外设的安全扩展[1]

④ **内存扩展**：同理，为了确保内存能够正确识别总线的信号控制位，新增一个TrustZone地址空间控制器（TrustZone Address Space Controller，TZASC）组件来实现对内存地址的安全扩展，将内存区域划分为安全内存区域和非安全内存区域，安全世界可以访问安全内存和非安全内存，而普通世界只能访问非安全内存，如图6所示。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpD1HbuUxMLPhuv2ZHoicIicMichcia7eobbNFhMOZmolcmpuNjt056qsKib9cCNpp1H9Yz4omY7nyZZALg/640?wx_fmt=png)

图6 使用TZASC实现内存的安全扩展[2]

内存区域的划分是在系统启动时通过配置TZASC组件（TZC-400/TZC-380）来实现的。以TZC-400为例[5]，TZC-400由Control unit和Filter unit构成，其中Control unit用于对每一个区域的安全设置进行编程，具体包括使能情况、安全访问权限、Base地址、Top地址和Non-secure ID filtering（基于NSAID信号），在Control unit的配置下，始终存在1个全地址区域Region 0，并且可以扩展8个分离的区域Region 1 - Region 8，Region 1-Region 8的区域互不交叉，如图7所示。而Filter unit用于对访问进行安全检查，根据NSAID信号决定是否允许访问该地址。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpD1HbuUxMLPhuv2ZHoicIicMicERGCzRMrjwIYt4J6Hs0onZqLoibzicRTSZfowtzPiaO0ns9M0nGPDUudg/640?wx_fmt=png)

图7 内存区域划分[5]

同样的，新增一个TrustZone内存适配器（TrustZone Memory Adapter，TZMA）实现对片上静态内存安全区域与非安全区域的划分。TZMA最大支持2MB空间的片上静态RAM划分，高地址部分为非安全区域，低地址部分为安全区域，两个分区都必须按照4KB进行对齐。TZPC组件中的TZPCROSIZE寄存器为TZMA记录分区大小信息。

⑤ **中断扩展**：由于引入了TZPC，外设分为安全外设和非安全外设，而外设产生的中断也分为安全中断和非安全中断，为了确保安全中断在安全世界处理，非安全中断在普通世界处理，需要对中断进行扩展。在通用中断控制器（Generic Interrupt Controller，GIC）中[6]，将中断源分为三组：group0、secure group1、non-secure group1。其中，group0是EL3处理的安全中断组，secure group1是S.EL1和S.EL2处理的安全中断组，non-secure group1是NS.EL1和NS.EL2处理的非安全中断组。当一个中断挂起的时候，GIC根据中断组和处理器的安全状态使用不同的中断信号，如图8所示，对于group0的中断，始终使用FIQ信号；对于secure group1的中断，如果处理器当前为安全状态，则使用IRQ，如果当前为非安全状态，则使用FIQ；对于non-secure group1的中断，如果处理器当前为安全状态，则使用FIQ，如果当前为非安全状态，则使用IRQ。即IRQ中断是用于当前世界的中断，直接对中断进行处理即可，而FIQ中断是用于进入EL3，以便完成世界的切换后对中断处理。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpD1HbuUxMLPhuv2ZHoicIicMicfBxCDDkUNOtTYVLd1vDzK7IoZM6ohHAspZAvx5ib7sbT0BKicMRepvHg/640?wx_fmt=png)

图8 中断源处理[6]

⑥ **内存映射**：由于引入了TZASC，内存被分割为安全内存和非安全内存，无法满足软件连续内存地址空间的要求，为此，引入虚拟地址的概念，并且使用内管管理单元（Memory Management Unit，MMU）技术完成虚拟地址向物理地址的转换[7]。MMU由Table Walk Unit和页表缓存（Translation Lookaside Buffer，TLB）组成。TLB的格式如图9所示，图中TAG表示虚拟地址，Translation Regime表示异常级别，NS位用于标识是否为普通世界，Descriptor表示映射的物理地址。当一个虚拟地址被传递给MMU时，MMU首先检查TLB是否有存在该地址的映射。如果没有，则从Table Walk Unit中查找对应的地址映射。非安全状态下的虚拟地址只能转换为非安全内存地址，而安全状态下的虚拟地址不仅可以转换为安全内存地址，也能够转换为非安全内存地址。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpD1HbuUxMLPhuv2ZHoicIicMicia6K30qF1QjicZySmTrlrUP8gPqgl95HlNmUyE30p1pXQzMJwDzZmy2g/640?wx_fmt=png)

图9 TLB详情[2]

MMU适用于在CPU中处理虚拟地址的内存映射，而对于部分主设备（例如GPU），其可以通过直接内存访问（Direct Memory Access，DMA）技术直接读写内存。对于同一个虚拟地址，如果软件通过CPU读取的物理地址与通过DMA读取的物理地址不一致，那么将造成获取的数据不一致，导致最后计算结果的错误。为了避免这种情况，需要对使用DMA的主设备配置系统内存管理单元（System Memory Management Unit，SMMU），确保对于同一个虚拟地址，最后DMA读取的物理地址与MMU映射物理地址一致。本质上，MMU技术与SMMU技术是一样的，只不过是作用的对象不同。

##

**PART****0****3**

**总结**

##

TrustZone围绕着CPU硬件是安全可信的概念，以CPU中SCR寄存器的NS位为起点，一步步向外扩展，包括总线的信号控制位、内存的TZASC和MMU、外设的TZPC、中断的GIC，最终为用户提供一个安全可信执行环境，在芯片层级保护用户的隐私数据。TrustZone除了保护用户指纹、个人身份信息等关键隐私数据，还一直默默地**保护用户智能手机中数据安全，包括在未解锁情况下的数据文件加密、密码保险箱中的账号密码管理、原子隐私系统中的数据存储等。**TrustZone只是智能手机保护用户数据的一种方式，还有SELinux、应用沙盒等等技术从其他层级保护用户的数据安全，最终为用户构建全方位安全保护。

**参考文献：**

[1] ARM Security Technology Building a Secure System using TrustZone Technology, 2009-9. [Online]. Available: https://developer.arm.com/documentation/PRD29-GENC-009492/c/

[2] TrustZone for Armv8-A, 2020-1. [Online]. Available: https://developer.arm.com/-/media/Arm Developer Community/PDF/Learn the Architecture/TrustZone for Armv8-A.pdf

[3] ARM Cortex-A Series Programmer's Guide for ARMv8-A, 2015-5. [Online]. Available: https://developer.arm.com/documentation/den0024/a/

[4] Arm A-profile Architecture Registers, 2022-12. [Online]. Available: https://developer.arm.com/documentation/ddi0601/latest

[5] ARM CoreLink TZC-400 TrustZone Address Space Controller Technical Reference Manual, 2015-9. [Online]. Available: https://developer.arm.com/documentation/100325/0001/

[6] Learn the architecture - Arm Generic Interrupt Controller v3 and v4, 2021-12. [Online]. Available: https://developer.arm.com/documentation/198123/0302/

[7] Learn the architecture - AArch64 memory management, 2021-11. [Online]. Available: https://developer.arm.com/documentation/101811/0102/

缩略语：

![](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpD1HbuUxMLPhuv2ZHoicIicMicYdM3njwyCs9UEnRFYJ1OrdheyzwSvecqx8olNlPA76fNUpMhbic4UOg/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpD1HbuUxMLPhuv2ZHoicIicMic1yWSmxuT3QAibtV0gyOAgibHlWf4T87GJiaJC7wWXicnAOFylT3eJlQebQ/640?wx_fmt=png)

**往期回顾**

[ITU首个！vivo 主导的2项智能终端安全国际标准立项成功](http://mp.weixin.qq.com/s?__biz=MzI0Njg4NzE3MQ==&mid=2247490760&idx=1&sn=957033ec86988afa66d94d2eabe161e7&chksm=e9b93aa4deceb3b2c1934bfc62dc58986c6a95c8af7456a20d29164ffcfbde735c77ac3d9559&scene=21#wechat_redirect)

[浅谈应用分发平台标准动态](http://mp.weixin.qq.com/s?__biz=MzI0Njg4NzE3MQ==&mid=2247490685&idx=1&sn=3bb58464eab279a40c5536a3f11c9fae&chksm=e9b93a11deceb307fdd4ce56ac560dc7f9f6ec295e7e89a599891ee595f5f2d8fa0e01bfda6e&scene=21#wechat_redirect)...