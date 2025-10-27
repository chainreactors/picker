---
title: 可信执行环境之AMD内存加密技术概述
url: http://blog.nsfocus.net/amd/
source: 绿盟科技技术博客
date: 2022-12-29
fetch_date: 2025-10-04T02:40:15.706522
---

# 可信执行环境之AMD内存加密技术概述

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# 可信执行环境之AMD内存加密技术概述

### 可信执行环境之AMD内存加密技术概述

[2022-12-28](https://blog.nsfocus.net/amd/ "可信执行环境之AMD内存加密技术概述")[王拓](https://blog.nsfocus.net/author/wangtuo/ "View all posts by 王拓")[机密计算](https://blog.nsfocus.net/tag/%E6%9C%BA%E5%AF%86%E8%AE%A1%E7%AE%97/)

阅读： 1,963

## ****一、引言****

可信执行环境（Trusted Execution Environment，下称TEE）是目前主流隐私计算技术之一，其通过软硬件方法在中央处理器中构建一个安全的区域，保证其内部加载的程序和数据在机密性和完整性上得到保护[1]。基于硬件的TEE使用硬件支持的技术为代码的执行和环境中数据的保护提供了更好的安全性保证。目前主流TEE方案有x86架构的Intel SGX技术、Intel TDX技术、AMD SEV技术及ARM架构的TrustZone技术等[2]。

本文将简单介绍包含AMD SEV所采用的内存加密技术[3]，包含安全内存加密（Secure Memory Encryption, SME）和安全加密虚拟化（Secure Encrypted Virtualization, SEV）两个部分。

## ****二、安全内存加密（S********ME********）****

简单来说，SME主要通过一个加密引擎对进出内存的数据进行加解密来实现。AMD在其芯片中配有内存控制器，控制器内包含高性能的AES加解密引擎。如图1所示，向内存中写入数据时，该引擎执行加密，而在从内存中读取数据时，该引擎执行解密。AES所使用的密钥会在每次系统重置时随机生成，存储在专用的硬件寄存器中并由AMD安全处理器（AMD-SP）进行管理，不会被CPU上的任何软件所访问也不会暴露在CPU芯片之外。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/wps_doc_1-6-300x300.png)

图1 内存加解密示意图

内存页加密的控制是由操作系统或虚拟机管理器的负责页表管理的软件进行控制。其使用物理地址中的第47位，也称C-bit来标记是否加密该页。如图2所示，当C-bit置为1时，表示应加密该页，则对该内存的访问由AES引擎自动进行加密与解密。反之则不进行加解密。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/wps_doc_2-9-300x187.png)

图2 加解密控制示意图

对于SME的使用，可分为全内存加密与部分内存加密两种。对于全内存加密，即设置所有内存的页表项C-bit为1，便可实现全内存加密，此时可以防止攻击者直接拿走内存模块后提取其内容，同时也可以防止冷启动、内存接口窥探等攻击。对于部分内存加密，其可以选择只加密部分内存区域而不是全部，可以只对敏感数据提供加密保护，相比于全内存加密而言灵活性更高，并且可以为加密与非加密的工作负载提供隔离，降低性能影响。

此外，针对操作系统或虚拟机管理器不支持的情况，SME还支持一种特殊的更简单的模式Transparent SME（TSME）。在此模式下，无论C-bit如何设置，所有内存都是加密的。但是在使用TSME模式时，其他内存加密特性均不可用。

以上便是对安全内存加密技术原理的简单介绍，下面我们将重点介绍安全加密虚拟化技术。

## ****三、安全加密虚拟化（S********EV********）****

* **技术架构**

SEV是AMD-V技术的扩展，其支持使用一个虚拟机管理器控制并运行多台虚拟机。SEV硬件通过ASID标记虚拟机的代码与数据。在虚拟机的整个运行周期中，ASID在内存中保持不变，保证了虚拟机数据能被正确识别并且不会被系统中其他软件访问。当数据写入或读出内存时，则由AES加密引擎使用ASID所关联的密钥对数据进行加解密。如图3所示，每个虚拟机都通过ASID仅与自己的加密密钥相关联，其他虚拟机或虚拟机管理器只能访问加密后的数据，使得虚拟机之间、虚拟机与虚拟机管理器之间具有强隔离性。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/wps_doc_3-8-300x300.png)

图3 SEV架构

* **内存加密**

与SME一样，SEV也是通过标记C-bit来控制页表是否被加密。但在SEV中，虚拟机可以选择其想要私有的数据内存页并通过标准CPU页表完成。对于虚拟机想要保密的内存数据，使用虚拟机的密钥进行加密；而对于与其他虚拟机或虚拟机控制器的共享内存中的共享数据，则使用虚拟机管理器的密钥加密。此时SEV虚拟机通过共享内存进行通信，而将其他内存使用密钥进行加密，保障其机密性。

* **密钥管理**

从上面的介绍中可以看出，SEV的安全性依赖于密钥的安全性，若密钥泄露则虚拟机中的加密数据不再安全。为保护密钥安全，AMD-SP中运行的SEV固件提供了一个安全的密钥管理接口来实现。虚拟机管理器使用这个接口来启动虚拟机，并执行正常的虚拟机活动。

为保护虚拟机的安全性，SEV固件需要保证平台的真实性、虚拟机启动的认证和虚拟机数据的保密性。对于平台的认证，可通过其身份密钥来证明。该证明由AMD和平台所有者共同签署。启动认证则是向虚拟机所有者证明启动过程时安全的，SEV固件向虚拟机所有者提供与SEV相关的虚拟机状态的签名，以验证虚拟机是否处于预期状态。详细认证过程如图4所示，用户向云系统提供虚拟机镜像，SEV固件启动虚拟机，并返回固件、内核等的度量值。用户验证度量正确后，向虚拟机提供机密信息来允许虚拟机继续启动。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/wps_doc_4-4-300x165.png)

图4 认证过程示例

虚拟机的机密性则是通过内存加密密钥的机密性来保证，SEV密钥管理接口不允许内存加密密钥以及其他任何SEV相关状态在未正确认证的情况下从固件中导出，可以防止虚拟机管理器获取密钥并窃取虚拟机中的数据。

## ****四、S********EV********应用场景****

* **云上应用场景**

随着云计算的发展，各行各业对云的使用率不断提高，对云的需求不断增加。然而云基础设施或人员并不总是可信的，多个用户之间的共享硬件同样可能会带来安全问题。而使用SEV则会为云上虚拟机提供更好的安全隔离，且加密内存可以防止云服务商中的恶意分子窃取数据。

* **安全沙盒**

SEV是围绕安全沙盒环境的理念构建的，沙盒像虚拟机一样拥有自己的磁盘和操作系统，在沙盒内运行的软件不受系统上其他软件。因此SEV可以用于创建安全的沙盒执行环境，目前比较典型的应用便是将SEV与Kata容器相结合成为机密容器。由于Kata是通过虚拟化技术实现轻量级沙盒为容器提供隔离性，将其沙盒与SEV相结合便可使容器运行在TEE中，为容器运行提供更高的安全性。

## ****五、总结****

SEV代表了一种新的虚拟化安全范例，与传统计算系统相比，不同级别上执行的代码是隔离的，任何一方都不能访问另一方的资源，为低权限代码提供了安全性。加密虚拟机不仅可以让虚拟机免受物理威胁，还可以免受其他虚拟机甚至是虚拟机管理器本身，适用于不需要完全信任主机的虚拟机管理器和管理员场景。未来我们将继续关注相关技术的研究，我们将在下一篇介绍其他TEE方案。

### 参考文献

[1] 《隐私计算白皮书》

[2] Jauernig P, Sadeghi A R, Stapf E. Trusted execution environments: properties, applications, and challenges[J]. IEEE Security & Privacy, 2020, 18(2): 56-60.

[[3] Kaplan D, Powell J, Woller T. AMD memory encryption[J]. White paper, 2016.

**版权声明**
本站“技术博客”所有内容的版权持有者为绿盟科技集团股份有限公司（“绿盟科技”）。作为分享技术资讯的平台，绿盟科技期待与广大用户互动交流，并欢迎在标明出处（绿盟科技-技术博客）及网址的情形下，全文转发。
上述情形之外的任何使用形式，均需提前向绿盟科技（010-68438880-5462）申请版权授权。如擅自使用，绿盟科技保留追责权利。同时，如因擅自使用博客内容引发法律纠纷，由使用者自行承担全部法律责任，与绿盟科技无关。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/tetragon/)

[Next](https://blog.nsfocus.net/aptconfuciuspakistanibo/)

### Meet The Author

王拓

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)