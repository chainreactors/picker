---
title: Autosar CyberSecurity之HSM和CSM， CryIf，Crypto Driver之间的关系
url: https://mp.weixin.qq.com/s/W-hyP5Jbx3WF9af2Ajashg
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:02:29.687841
---

# Autosar CyberSecurity之HSM和CSM， CryIf，Crypto Driver之间的关系

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaDAlVgadOXc0nyk4EgeQD8icKIgdQI6NMOqcDBNQRlCdF3HkX7VgibxbbicQHdiaIribvebn8vWCVRx60Uxl2hEtHRq6QaEqff5qiaI4/0?wx_fmt=jpeg)

# Autosar CyberSecurity之HSM和CSM， CryIf，Crypto Driver之间的关系

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

**汽车网络信息安全概述**

随着汽车网联化和智能化，汽车不再孤立，越来越多地融入到互联网中。同时，汽车也慢慢成为潜在的网络攻击目标。这边不做过多赘述，只是强调一下 网络安全和功能安全的区别，经常会有人疑惑这两者之间的关系，这边引用一张vector的图，非常清晰的展示了两者之间的区别：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicaFgIStgRmVsCA3Gnm8AXOpT860UORxYf4dUPcfkWT6V1qcdpicDx0Om3xRibcBKiaL4tKeD6lq9ib5g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

1）功能安全是保护人为目的的，车如果发生故障的话，目的是让车能尽可能的可控，不会失控去对人做出伤害。

2）网络安全是反过来保护车辆系统的，防止黑客的入侵，控制或者窃取车辆信息，使车辆不可控，或者干一些违法的事情。

**02**

**网络安全相关**

那么车辆哪些部件是网络安全相关的，哪些不是相关的呢？ISO21434中已经给出明确的定义，如下图所示，展示了如何判定汽车中的相关组件是否和网络安全相关。这个判断一般是由主机厂做，然后把需求给到下层供应商，所以我们不做过多描述：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicaFgIStgRmVsCA3Gnm8AXOaC8oZrqNO8zibz8e5hQwHglnEV3Mt1qSCm2IecfcHWo7tsjMmdlfPng/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

这边我们做出如下总结：

1）像T-BOX，TCU，网关等节点或功能，必须考虑网络安全，因为它们有直接的对外连接

2）具有高功能安全等级，比如ASIL C/D的节点，也要实施网络安全

3)  涉及存储和处理与车辆或者驾驶员相关数据的节点，也需要实施网络安全措施，以防止重要信息泄露或者被窃取

4)  有无线连接的节点，比如蓝牙，NFC，WIFI等有关的组件也要涉及网络安全，因为他们是最容易被攻击的组件

5)  对外连接的节点，比如对外连接的总线，OBD

对于网络安全相关的部件需要做哪些安全保护措施，这边引用了vector一张图来展示：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicaFgIStgRmVsCA3Gnm8AXOrpia2SialmDQptjN7KsUM11PqS3H8muUdwuV8QEUx0Pr0Vs5NyUjiaadA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

**03**

**AUTOSAR CP 信息安全架构**

那么在AUTOSAR架构中是怎么实现网络安全功能的呢？

如下图，是AUTOSAR CP 信息安全架构图：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicaFgIStgRmVsCA3Gnm8AXOCnZWicpNwxA0mhNmTbrJlbF0CpCeyKg70X5hZIqUuCFg5ro0VxeLrsw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

可以看到Crypto Stack分为三部分:

**Crypto Service Manager（CSM）：** 是其他软件模块调用加解密模块的第一接口。应用层SWC通过RTE访问CSM，而其他底层软件（BSW）或者复杂驱动（CDD）则可以直接调用CSM。同时CSM也负责安全相关任务的队列管理，即优先级管理。

**Crypto Interface（CryIf）：**CSM往下调用的接口模块，每一个CryIf中的加密基元都会与CSM中的一个服务相对应。而且CryIf支持分发相关任务，进一步调用不同的驱动。

**Crypto Driver（CryDrv）：** 驱动模块，访问相关部件，实现加解密操作，例如访问加解密加速器或者真随机数生成器等。

为什么会存在 CSM, CryIf，Crpto Driver？

是为了将硬件HSM的接口做一个封装，以便上层服务可以标准化调用，而不受HSM的不同的影响。

**04**

**汽车信息安全之锚：HSM**

HSM是硬件安全模块的英语缩写，全称是Hardware Security Module。 随着信息安全变得越来越重要，在通信领域常用的AES、SHA、RSA等加密算法被越来越多地应用到汽车上。但通常这类加解密算法都需要大量的数学运算，需要消耗很多CPU时间和资源，汽车上的ECU又有比较高的实时性要求，为了节省主CPU的资源，HSM应运而生。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicaFgIStgRmVsCA3Gnm8AXOEjuibsNge2cNd2HnRSWjiaeaK4pJS83BU1icuXMAPV3WvKHAibvL3l42Hw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

HSM（Hardware Security Module），它一般会有一个独立的CPU，专门用来进行加解密运算，还有一些针对特定算法的硬件加速器（如AES-128、SHA-256等）。有了HSM模块，程序中就可以把加解密运算交给HSM来执行，主CPU就可以去做其他工作，一段时间后来查询结果，或等待HSM计算完成后通过中断等方式通知主CPU计算结果即可。

而且HSM通常还拥有单独的存储区，包括RAM和NVM，HSM的存储区在正常运行状态下应只允许HSM核读写，主核不能读写。这样就可以把算法秘钥等重要数据存储在HSM存储区，与主核进行隔离，进一步加强安全性。此外HSM模块还会带有真随机数生成器等加密算法常用外设。

HSM两个主要功能：

第一个是存储管理密钥。 第二个是加速加解密算法。

**05**

**英飞凌AURIX系列MCU的HSM**

以TC397为例，HSM作为外设之一，挂载在单片机的SPB系统外设总线上。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicaFgIStgRmVsCA3Gnm8AXO47nlG3QontjndG2fbWr8JMYmWw9YibLCXVwghxaPhhR2Tl0o5VNVINw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

HSM展开后的架构图，HSM有一个基于ARM Cortex-M3的CPU，有随机数生成器TRNG，AES算法等硬件加速器，以及中断、Timer等组成部分。

其中存储软件程序和数据的PFlash和DFlash实际上与芯片的其他部件共用一块Flash，但是能通过TriCore的访问控制设置，来保护HSM所对应的Flash区域不被非法访问或篡改。安全密钥的存储就是在其中的DFlash里。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicaFgIStgRmVsCA3Gnm8AXOYvfW0zVDBV2ict6QMW0b5CTRt9wjI8xmBibjeL9b2MRdyrC1vcLrwSRw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

**06**

**AUTOSAR中的HSM接口：Crypto Stack**

除了硬件实现，广义的HSM还包括相应的固件和驱动。AUTOSAR跟HSM最相关的就是Crypto Stack：将硬件HSM的接口做一个封装，以便上层服务可以标准化调用，而不受HSM的不同的影响。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicaFgIStgRmVsCA3Gnm8AXOS96ZSgGEBQJiaZ58YkDNNuLx9BdEp16VyJBOxBTAiaxZe7KibMUmibCLHA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

上层应用需要执行加密相关的任务时的一个基本工作流程，SWC提供必要的data及jobid，调用CSM提供的接口，接下来分析主核的CSM stack的各个模块为了完成这个任务需要的配置。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicaFgIStgRmVsCA3Gnm8AXOxOHvqT425IJFXESyyVxkSicyC7ZXLBsfMcrdQIhQcdYZj5onbxcKylg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

**07**

**CSM, CryIf，Crpto Driver每层都做了什么?**

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicaFgIStgRmVsCA3Gnm8AXOBpxCeAnSO5CJocSk7zOtjBaGGU5eMSooBb5ZHnA0fWcnoKIOjKnPlA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

举个栗子， HSM有两个加密驱动对象Crypto Driver Object：HW-AES和HW-RSA

它们每个都有自己的通道。每个通道连接到一个CSM队列和一个Crypto Driver Object队列。

两个Crypto Driver Object都在分别处理一个加密作业：AES-high和RSA

其中一个Crypto Driver Object的队列包含另一个作业(AES-low)。如果HSM的HW-AES已经完成了AES-high的任务，则将AES-low的任务作为下一个任务处理。

假设应用程序的新作业调用RSA:

1)  如果RSA的Crypto Driver Object不繁忙，则立即处理该任务。

2)  如果RSA的Crypto Driver Object很忙，但是Crypto Driver Object的队列未满，则该作业将按优先级顺序列在该队列中。一旦Crypto Driver Object空闲，将执行Crypto Driver Object队列中具有最高优先级的作业。

3)  如果RSA的Crypto Driver Object很忙，并且Crypto Driver Object的队列已满，则该作业将按照优先级顺序存储在CSM队列中。·

4)  如果RSA的Crypto Driver Object忙，且Crypto Driver Object队列和CSM队列都已满，CSM会拒绝请求。

5)  如果RSA的Crypto Driver Object是活动的，则作业已经在加密驱动程序中启动，正在等待更多的数据来处理或完成命令。

**08**

**Crypto Driver（CryDrv）配置**

主核的Crypto层主要负责与HSM的交互，将任务转发给HSM，并获取响应 Crypto模块需要如下container，如果不存在就需要右键Crypto添加这些Container.

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicaFgIStgRmVsCA3Gnm8AXOzrukpBaKn4aBXmpvQseONxeHClPVl5EVjXKUbCkCVAjiayk42jmQJnw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

**1)  CryptoPrimitives配置用到的算法**

这边举一个CAMC Verify的例子。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicaFgIStgRmVsCA3Gnm8AXOuLJ7zx9tJsktT40Ik96XOLI0rNs8OSicFFIjwAacoXL2tYibDz0eLCkQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)

**2)  配置CryptoDriverObjects**

添加一个Object: HSM\_Crypto

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicaFgIStgRmVsCA3Gnm8AXO1xPqL7R2UqhzictXricBFzcUmvk5mXZI7tA2coORTnviapdKrzzrRpUZg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13)

**3)  配置CryptoGeneral**

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicaFgIStgRmVsCA3Gnm8AXOHSBJibosNG5yCsSkrnPYRazN1LvyRtwaLcEhQMDryzznmicibuHW2YBeA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)

**4)  配置CryptoKeyElements**

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicaFgIStgRmVsCA3Gnm8AXOsWibwXHTl0Ma5magMJwcezVYUtbNjA5HUcaYoibzZr2lGoLgcRIXKjibQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=15)

**5)  配置CryptoKeyTypes**

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicaFgIStgRmVsCA3Gnm8AXOKU4xnZIBSthICPa2fzxSNnxia2QEpamqKkOY2afkLD5VT5iaGyiaencbQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16)

**6)  配置CryptoKeys**

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicaFgIStgRmVsCA3Gnm8AXOrKKWeTnNG04X4z3CYmjVB1CdJxnCe5TsSlFEv4cXxyx7ImhGp7tMpg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=17)

**09**

**Crypto Interface（CryIf）配置**

CryIf将CSM层的请求转发到对应的CryptoDriver。它涉及到的主要配置就是CryIfChannel。它将Csm层的job和实际处理cryptoDriverObject对应起来。 CryIf模块需要如下container: CryIfChannels, CryIfCryptoModules, CryIfKeys, CryIfGeneral。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicaFgIStgRmVsCA3Gnm8AXOtF6VL8ULDhVCuAgVPNic5k2teWAhoiatgdklAjBPqODgakDNRVbAMf7g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=18)

**1)  配置CryIfChannels：**

Driver Objects Ref就是Crypto模块配置中配置好的。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicaFgIStgRmVsCA3Gnm8AXOu36R19yKyMEB1fkkobvFjZsH5B7ibhkSHHTnDl8BQZdsKsrM0qabwew/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=19)

**2)  配置CryIfCryptoModules**

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicaFgIStgRmVs...