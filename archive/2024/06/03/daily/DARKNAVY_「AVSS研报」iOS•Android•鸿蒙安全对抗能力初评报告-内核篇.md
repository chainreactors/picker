---
title: 「AVSS研报」iOS•Android•鸿蒙安全对抗能力初评报告-内核篇
url: https://mp.weixin.qq.com/s?__biz=MzkyMjM5MTk3NQ==&mid=2247485773&idx=1&sn=da3dd8be7ee3a6fabce17efcad7b91ed&chksm=c1f44d85f683c493508f09ecfcfb628efac292f46bee1ba680f614fb413b4889f83e33a4fa2d&scene=58&subscene=0#rd
source: DARKNAVY
date: 2024-06-03
fetch_date: 2025-10-06T17:32:39.401612
---

# 「AVSS研报」iOS•Android•鸿蒙安全对抗能力初评报告-内核篇

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6aFicjrXnvggHqA7wUFeCm1Aprp7yicRg5FjTicLOPYggCKqPHowdow10GXaXAvJD7lgwzhLjSRYlH7alGWFBkrUg/0?wx_fmt=jpeg)

# 「AVSS研报」iOS•Android•鸿蒙安全对抗能力初评报告-内核篇

原创

AVSS

DARKNAVY

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6aFicjrXnvggHqA7wUFeCm1Aprp7yicRg5JPWxBKosJjzOjDOLdEv3ANLAw6CggARBcibXHraICrGmQIZwq4cibHhA/640?wx_fmt=png&from=appmsg)

**五**部不同品牌型号的手机，摆在做为消费者的我们面前，哪一部手机更能防止我们的隐私被窃取？十台不同的智能汽车呢？哪一辆更能防止恶意获取我们的定位甚至听到我们车内的声音？

做为普通的消费者，**我们目前无从知晓**。做为长期研究高级复杂攻击的技术人员，我们清楚，这些手机和汽车面对高级持续性攻击时，**终归可以被攻破**。

漏洞永远无法完全消除。所有安全努力的目标，在于**尽可能提升攻击者的成本**：时间、算力、能力等等。

这就是我们推动 [AVSS（Adversarial Vulnerability Scoring System）评估框架](http://mp.weixin.qq.com/s?__biz=MzkyMjM5MTk3NQ==&mid=2247485683&idx=1&sn=26825be1d4758a94860d15bcd5d5a91a&chksm=c1f44c3bf683c52df22b3805b7f09d7e26155f7fcb4c2643e8c02231927bf08695d8cd764f61&scene=21#wechat_redirect)的初衷。我们希望通过**科学公正的量化安全**，**推动安全价值可度量、可感知**，努力提升攻击者成本、保护用户的产品企业应该被看到，消费者也有权更便捷地做出更安全的选择。‍‍

*以下内容重点摘取了国产操作系统的技术分析部分。‍*

**AVSS报告**

**本**报告由 DARKNAVY 基于AVSS理念，以高级持续性对抗攻击视角，从移动端操作系统内核安全对抗的**五个阶段：1. 定位攻击入口；2. 构造利用原语；3. 绕过内核监控；4. 扩散恶意行为；5. 完全系统控制**，对如下设备系统进行对抗评估：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6aFicjrXnvggHqA7wUFeCm1Aprp7yicRg5jjIgbtEosjXkL3a37I4iaOcct5f9lT2PAYlpEJszIyIwWMApKQic1vtg/640?wx_fmt=png&from=appmsg)

**所测试设备操作系统均为截止2024年5月的最新版本。其中*HarmonyOS NEXT Developer Preview2 即华为自研内核的鸿蒙系统，又称鸿蒙星河版或纯血鸿蒙，下文中使用 HarmonyOS NEXT*****指代。****

**AVSS结论**

* HarmonyOS 4.2 在**整体安全性方面略优于原生 Android 14、ONE UI 6** 等操作系统内核，并且在多个维度中**与 iOS 17 能力指数接近或相当**；
* HarmonyOS NEXT 采用了**新的微内核架构，**在部分维度如后利用的影响扩散上，其安全性已经有了**较为显著的进步，**在传统安全性方面**还有提升的空间**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6aFicjrXnvggHqA7wUFeCm1Aprp7yicRg51dOf0xdPAroEmAAY8AkauVIGQBATyoB4lGUcGrWkRnicIOvrmVf0M3g/640?wx_fmt=png&from=appmsg)

以上量化指数对比，基于对如下五大类内核安全防御能力（共50余子项防御量化维度和指标）进行对抗评估得出：

1. 内核与用户态攻击面防御能力
2. 内核内存破坏类漏洞防御能力
3. 内核任意读写利用防御能力
4. 后利用影响扩散防御能力
5. 纵深防御能力

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6aFicjrXnvghcbh7wZURtE1zkxzZhibKQrNrFYokklFogibSEHgYichyqoy0Wbic6XgjrFmtZckkyJGOwkModJNFp2w/640?wx_fmt=png&from=appmsg)

**阶段一：定位攻击入口、寻找其中的漏洞 —— 内核与用户态攻击面防御能力指数**

攻击者需要首先确定其可以访问的内核资源，并寻找其中的内核漏洞。内核暴露的非必要资源越少、潜在存在的的漏洞数量就越少。

**阶段二：利用漏洞“做坏事” —— 内核内存破坏类漏洞防御能力指数**

攻击者发现的漏洞通常为编码缺陷，攻击者需要通过精妙的构造，才能够将这些编码缺陷转化为有危害性的内核敏感数据访问。内核通过在设计、实现、编译时对可能出现的代码非预期行为添加检查，防止代码缺陷演变为危害性操作。

**阶段三：绕过内核中“巡逻的守卫” —— 内核任意读写利用防御能力指数**

部分内核针对其中部分关键的代码及数据额外设置了专门的、实时的守卫——运行时的完整性监控。攻击者需要绕过这些守卫、或通过其他途径完成攻击。

**阶段四：恶意行为影响范围扩散 —— 后利用影响扩散防御能力指数**

攻击者通过某内核资源攻破了其所在的功能模块，内核对各功能模块的拆分与隔离，将受攻击者攻陷的模块与其他功能正常的模块隔离开来。

**阶段五：持久化驻留、信息窃取 —— 纵深防御能力指数**

部分系统中，内核便是管理用户数据的最底层，内核被攻破便意味着所有的用户数据均能够被攻击者控制。部分先进的操作系统在内核之下，仍有多种措施保护重要的用户敏感数据。

****AVSS综述****

**### **内核与用户态攻击面防御能力指数****

**该指数对应阶段一：定位攻击入口、寻找其中的漏洞的防御能力**

HarmonyOS 4.2版本内核针对用户态攻击面的防御能力与原生Android 14、One UI 6、IOS 17操作系统内核能力相当，**均部署了成熟的安全防御机制**。

HarmonyOS NEXT版本针对用户态攻击面的防御更优于其余操作系统内核，其微内核架构能够**极大地减少运行在特权层级的代码数量**，从而降低产生漏洞的风险。

**操作系统内核面临的主要威胁来自于用户态程序。对于攻击者而言，对用户态可访问的内核资源限制程度、内核运行于高特权级的代码数量等，都是影响其攻击难度的重要因素。**

* *内核向用户态程序提供了丰富的资源访问接口，如系统调用、驱动、procfs、sysfs等，而所有暴露给用户态的接口便能够成为暴露给用户态的攻击面。内核可以通过对用户态程序进行访问控制，对用户态系统程序与不可信应用程序进行隔离，从而减少暴露给不可信应用程序的内核接口、减少直接暴露给不可信应用程序的攻击面、增加攻击者的攻击成本及攻击难度。*

  *‍‍‍‍*
* *内核运行于高特权级的代码数量，与高特权级的漏洞数量形成正比。选择不同的内核架构，内核态代码量级不同，内核态出现的漏洞数量也相差甚远。*

HarmonyOS 4.2版本使用了较为成熟的安全防御机制例如**SElinux、Seccomp、Namespace、Capability**等（iOS 17中使用SandBox、entitlement能够起到类似的效果），HarmonyOS NEXT在已有的防御机制上还设计了独立的一套**CAPABILITY SYSTEM**机制用来限制可访问内核的功能以及**IPC的权限校验**。

HarmonyOS NEXT使用IPC进行通信时使用内核对象作为数据传输的载体，CAPABILITY SYSTEM通过权限划分确保只有那些有内核对象读取(或写入)的能力可以从内核对象中接收(或发送)消息。因此，消息的内容不能被恶意进程访问。

HarmonyOS NEXT采用微内核架构，有效减少了内核TCB（Trusted Code Base），与传统宏内核相比，**内核代码量只有不到1/4**，能够有效减少漏洞的产生，以下为各评测操作系统内核的TCB大小对比：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6aFicjrXnvggHqA7wUFeCm1Aprp7yicRg5CeYH85GX0cficKZPodBVZT0cGWqia6cgvseWwXHoH06D1WRuaYGZA82w/640?wx_fmt=jpeg)

###

**### **内核内存破坏类漏洞防御能力指数****

***该指数对应阶段二：利用漏洞”做坏事“的防御能力***

针对内存破坏类漏洞，HarmonyOS 4.2版本内核对比常规移动端内核武装到了牙齿，除了常见的内核防御机制开启外，HarmonyOS 4.2还使用了**PAC以及CFI**机制进行更加全面的防御；**HarmonyOS NEXT中PAC以及CFI防御机制未应用**，难以阻止攻击者破坏内核代码的执行逻辑，在该方面建议参照成熟的防御机制，进一步提升内核安全性。

**目前内核提权攻击的主要方式依然是使用内存破环漏洞通过内核数据读写、内核代码执行进行提权。因此，内核对抗内存破坏类漏洞的防御能力，是内核安全性的重要组成部分。**

* *漏洞的产生是不可避免的，但是经过长期的发展，部分漏洞类型已经可以依靠编译器、堆管理器以及各种参数设置等从源头上消除，这些防御策略的使用能杜绝攻击者挖掘出该种类型漏洞。*

  *‍*
* *安全防御机制的启用程度与攻击者进行攻击的难易程度密切相关，例如：同样的栈溢出类型漏洞，攻击者面对开启canary防御机制的目标进行攻击的难度要远大于未开启canary防御机制的目标。*

  *‍*
* *漏洞的产生原因是多样的，但是漏洞的利用手段却相对有迹可循，在利用过程中及时发现并阻断该种利用手法将增加攻击者的攻击成本与攻击难度。*

HarmonyOS 4.2版本除了开启了成熟的内核防御机制例如**NX/DEP、PXN/PAN、Canary**等，还使用了**CFI保护间接跳转、PAC保护非叶子节点的返回地址**，与原生Android 14与One UI 6相比，**防御范围更加的全面**。

DARKNAVY在测试过程中发现**HarmonyOS NEXT并未使用PAC、CFI等**已经在HarmonyOS 4.2版本中部署了的防御机制。

**PAC（Pointer Authentication Code，指针认证码）是ARM架构中引入的一种安全特性。它通过在指针中插入一段额外的代码进行签名，以验证指针的完整性，从而抵御JOP、ROP等攻击。**

*HarmonyOS 4.2版本使用PAC来保护非叶子节点的返回地址，实现方式如下：*

*内核代码中存在**ptrauth\_keys\_kernel**结构体，该结构体内存在**ptrauth\_key**结构，每个进程创建的时候内核会执行**ptrauth\_keys\_init\_kernel**函数，该函数通过**get\_ramdom\_bytes**将随机数16字节写入**task\_struct**的thread结构体的**key\_kernel**字段，在该进程调用内核系统调用时，执行**sw**itch\_to**将**task\_struct**的**key\_kernel**写入**\_\_pki\_v.lo**和**\_\_pki\_v.hi**，PACIASP指令和AUTIASP指令使用寄存器\_\_pki\_v计算得出值写入栈上保证返回地址不被篡改。*

HarmonyOS 4.2版本在PAC机制上做到了用户态与内核态密钥分离，用户态与内核态算法独立并且不公开，攻击者即使获取到内核态的密钥并修改用户态密钥为内核态密钥也无法得到正确的加密结果。

```
struct ptrauth_keys_kernel { struct ptrauth_key apia;};static __always_inline void ptrauth_keys_init_kernel(struct ptrauth_keys_kernel *keys){ if (system_supports_address_auth()) get_random_bytes(&keys->apia, sizeof(keys->apia));}static __always_inline void ptrauth_keys_switch_kernel(struct ptrauth_keys_kernel *keys){if (!system_supports_address_auth()) return;  __ptrauth_key_install_nosync(APIA, keys->apia);  isb(); }
```

现今的内核攻击手段与传统手段已经大相径庭，由于Stack Canary、PAC、CFI的引入使得控制流的完整性得到了较大的提升，目前已鲜见直接通过控制流劫持攻破内核的攻击方式。

近年来针对内核提权更常见的是面向数据攻击（**Data Oriented Attack**），通过UAF、OOB漏洞修改内核中的数据指针，以实现任意内核地址读写，修改内核中的关键数据结构、提升权限。iOS 17基于其处理器提供的硬件安全能力实现了 Data PAC、Pixel 8在原生Android上使用了ARM MTE，对 Data Oriented Attack 的防御能力有了大幅度提升。但**HarmonyOS目前尚未应用上述机制**。

**### **内核任意读写利用防御能力指数****

*该指数对应阶段三：绕过内核中“巡逻的守卫”的防御能力*

HarmonyOS 4.2版本对内核中代码及关键数据的保护较HarmonyOS NEXT更加完善，并且遥遥领先于原生Android14，其通过自研的**HKIP**机制（对标RKP机制）保护了内核关键数据，与iOS 17相比，在一些更细粒度化的防御实现上还存在改进空间比如ezhen。

*PAC和CFI等防御机制的不断完善，使得内核态的控制流完整性得到了较好的保护，通过劫持内核控制流的攻击方式已较为罕见。近年来更常见的方法是通过面向数据攻击（Data Oriented Attack）的方式，即通过获取内核的任意数据读写能力，修改内核关键数据，以进行提权攻击。因此，在攻击者获取到内核任意读写能力后，操作系统如何对抗进一步的攻击，是内核安全的核心能力。*

**内核中存在大量敏感数据以及段，例如：内核代码段，作为攻击者最优先瞄准的目标，一旦攻击者能够篡改内核代码段数据便能够获得内核的任意执行权限，操作系统从更高的层级达到保护内核数据完整性能够有效的增加攻击者的利用难度。**

RKP即“Real-time Kernel Protection”，是三星EL2层防御机制实现的名称，它是三星KNOX的组成部分。RKP机制的出现极大程度的增加了攻击者的攻击难度，传统漏洞利用方法在RKP机制面前难以发挥效果，以下是RKP中页表地址转换示意图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6aFicjrXnvggiciaIxegic4gh3icAicJToVIoEeY7lhwCWTBr5vfEZDHYoIBohch5FWdgOTZ9tFW8ibGngQJmscPjmgNQ/640?wx_fmt=png&from=appmsg)

Ref:https://blog.longterm.io/samsung\_rkp.html

HarmonyOS 4.2版本同样使用了HKIP机制从EL2层面保护了内核代码段以及只读数据段的完整性，通过mmap创建只读内存用来保存内核中的重要结构体数据及指针并使用HKIP保护该内存的完整性，其原理与RKP相似，都是在EL2层面做了多一层的页表映射来保证EL1层面对于页表的修改可以被EL2层捕获并拦截。

HarmonyOS 4.2版中HKIP机制与RKP机制保护能力相当，其保护了代码段、只读数据段、内核重要结构体等不被篡改。但是对于应用程序页表缺乏保护，攻击者可以通过修改应用程序页表任意读写未被HKIP保护的物理地址，该利用方法也被验证在Pixel、Samsung Galaxy上同样可行。

在HarmonyOS NEXT中，可以看到HKIP提供了多种保护机制，但是在实际研究过程中发现，除了代码段、只读数据段以及内核页表存在HKIP保护外，**其余重要结构体并未被保护**。

以下为部分HKIP机制与RKP机制中的防御能力覆盖范围比较：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6aFicjrXnvghcbh7wZURtE1zkxzZhibKQrzpZuiaqvexdEQp0uQlFqzkfExeEDibDwNyLrxRZibR8Lu8JxicPyBJHm2A/640?wx_fmt=png&from=appmsg)

（o 覆盖  x 未覆盖  | 未完全覆盖）

**### **后利用影响扩散防御能力指数****

*该指数对应阶段四：恶意行为影响范围扩散的防御能力*

HarmonyOS 4.2版本内核构成与原生Android 14、ONE UI 6内核构成相近，各大模块之间并没有做严格的权限隔离，iOS则是基于Mach和BSD的混合内核架构。

HarmonyOS NEXT采用微内核架构，拥有更细粒度的内核模块隔离，其将内核资源划分为多种类型，不同的类型由对应的模块进行管理，模块间通过IPC机制进行通信，对于攻击的横向扩散防御有着更好的效果。

*传统操作系统内核承担着整个系统所有资源的调度，一旦拿到内核任意一个模块的权限都将导致整个操作系统的失守，随着微内核的诞生，内核模块的权限划分更加细粒度，因此如何降低后利用的影响扩散也成为内核安全的新测量指标。*

**网络模块、文件管理模块、内存管理模块、驱动模块等作为攻击者的主要攻击目标，将其权限进行细粒度的划分，能够有效阻止攻击者从点到面的攻击扩散。**

HarmonyOS NEXT将模块之间权限进行细粒度划分，模块之间通过IPC进行通信，攻击者难以通过一个模块的攻击成果演化成对整个系统的攻击成果。

HarmonyOS NEXT将驱动程序在用户态加载，使得针对驱动程序的攻击只能获得EL0层的权限难以转化成针对内核EL1层的攻击。

![](https://mmbiz...