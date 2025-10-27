---
title: CAGE:基于GPU扩展实现ArmCCA
url: https://mp.weixin.qq.com/s?__biz=MzIyODYzNTU2OA==&mid=2247498204&idx=1&sn=66de5e0213714eab34221f4981f2de36&chksm=e84c5f03df3bd61577a8a0470b813dab0505cf1edc403118407d314a92c91411197b73357392&scene=58&subscene=0#rd
source: 绿盟科技研究通讯
date: 2025-01-03
fetch_date: 2025-10-06T20:09:47.556679
---

# CAGE:基于GPU扩展实现ArmCCA

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hiayDdhDbxUYn9w1gticzmXqLTdianSah4xyIU3NPQRTavlTchwyVicEww7qKZaRtaiaxkMGNMcMsMEKxm0YQT8Cichg/0?wx_fmt=jpeg)

# CAGE:基于GPU扩展实现ArmCCA

原创

创新研究院

绿盟科技研究通讯

![](https://mmbiz.qpic.cn/mmbiz_gif/hiayDdhDbxUYn9w1gticzmXqLTdianSah4x1szibNW7MqXQbwZVg9X7WXjK9F3I0ZcocAHiaSSEzB96d13Tu24S5n7Q/640?wx_fmt=gif&from=appmsg)

一.  论文背景

为了更好的支持机密计算，Arm提出了机密计算架构（CCA，Confidential Compute Architecture），CCA通过创建多个互相隔离的地址空间（realm）来保证敏感任务的机密性和完整性。在CPU上实现CCA后，Arm尝试将机密计算推广到GPU中，但目前还没有可用的硬件和固件出现，传统的基于TEE实现GPU机密计算的方式并不适用于Arm的realm架构。为了解决这一问题，Chenxu Wang等人提出了一种利用GPU扩展实现Arm CCA的方案，称之为CAGE。

CAGE为Arm CCA提供GPU运算支持的同时，能够保护GPU中的敏感数据。根据论文中的测试结果，该方案对程序性能只有微小的影响。

二.  前置知识

2.1

Arm TrustZone和Arm CCA

TrustZone基于硬件提供隔离的、机密的执行环境，依据处理器运行状态划分为安全区和非安全区。非安全区中是常规操作系统、应用以及hypervisor，安全区软件结构与非安全区类似，但是是一个隔离的环境，仅用来运行安全组件。内存、中断和外设资源基于TrustZone特性分到两个区。TrustZone固件利用最高权限的Secure Monitor实现非安全区和安全区的切换和资源分区。然而，研究表明安全区中的组件（安全OS和安全hypervisor）存在漏洞，攻击者可以通过控制这些组件来破坏系统，影响到非安全区和Secure Monitor。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYn9w1gticzmXqLTdianSah4xMcOW9WdichRaU0APSKOl4eYIqsiaktH9Bibiclm8VIM4wmyeBico6Xicl90w/640?wx_fmt=png&from=appmsg)

图1 ARM CCA架构

在最新的Armv9架构中，Arm引入了CCA和RME来增强安全性。图1展示了CCA的架构。CCA保留了TrustZone安全区和非安全区的设计，在这个基础上引入了额外的realm区和root区。realm区与其他区隔离，里面运行多个机密realm实例，realm实例被不受信任的软件组件管理（非安全区的hypervisor）。为了实现realm区内不同realm之间的内存隔离，realm区的hypervisor层运行着一个轻量的RMM（Realm Management

Monitor）。root区里面是固件中存储的最高权限的Monitor代码，Monitor利用GPC（Granule Protection Check）为整个主存提供灵活的细粒度访问控制。具体来说，当一个软件尝试访问物理地址空间（PAS），GPC会检查GPT（Granule Protection Tables），获取该物理地址空间的安全属性，判断该次访问是否合理。出于安全性考虑，CCA建议将GPT存放在root区的物理地址空间中，并且只允许Monitor来配置GPC寄存器。

与传统的Arm TrustZone相比，CCA利用硬件层面的隔离保证root区中最高权限的Monitor的安全性，提供了高级的有硬件协助的内存隔离架构。

2.2

Arm GPU与SMMU

在大部分基于Intel芯片搭建的主机上，GPU与CPU在内存上是相互独立的，GPU拥有专用的显存，而主流的Arm GPU通常与CPU共享统一内存与外设。为了处理主机和GPU的数据交换，Arm开发了一系列的GPU软件，包括内核层驱动和用户层运行时。这些软件管理GPU计算环境，同时负责与GPU硬件交互。使用GPU加速计算时，GPU要准备执行环境。首先分配物理内存，创建GPU专用的buffer；然后将计算需要的重要组件（代码，数据，元数据）加载进对应的内存空间中；同时，GPU软件栈要创建GPU专用的页表，配置GPU寄存器，以便GPU通过DMA访问计算需要的组件；另一方面，GPU软件需要与硬件交互，规划执行顺序，通过MMIO提交GPU任务；当计算完成后，GPU软件会获取计算结果，然后恢复环境。

GPU以及其他外设需要和CPU共享主存，为了管理支持DMA的外设，Arm提出了SMMU。

目前，大多数Arm GPU和其他支持DMA的外设都是物理连接到一个SMMU。与CPU的MMU类似，SMMU也支持通过地址转换来控制外设对物理地址空间的访问。为了实现访问控制，高权限的软件会通过MMIO配置SMMU的寄存器。Arm CCA中，SMMU还支持GPC，CCA引入了只能从root区访问的额外的SMMU MMIO寄存器，用来保护SMMU GPC。这些寄存器提供了针对SMMU GPC的基础配置能力，包括GPT基址、GPC控制、错误处理以及TLB无效化。

三.  威胁模型

在Arm CCA框架下，假设存在一个攻击者，能够同时控制安全区和非安全区的软件栈，包括非安全区中的GPU软件、操作系统、hypervisor以及安全区中相同层级的软件。这个攻击者试图泄露或者篡改机密GPU任务中的敏感数据，他可以（1）直接访问存有敏感数据的统一内存或者控制具有DMA功能的外设来读取数据；（2）破坏GPU组件（破坏内存管理，改变机密任务的执行顺序，修改GPU寄存器状态）以打破互相隔离的执行环境；（3）提交恶意任务到GPU，实现访问或篡改其他realm的数据。论文中给出的CAGE方案能够防御上述所有软件层面的攻击，同时还能防御冷启动攻击等物理攻击。侧信道攻击和拒绝服务攻击则暂时不在考虑范围内。

四.  方案设计

CAGE的作者观察到，GPU软件在大多数时候不需要访问敏感数据。因此，可以将这部分GPU软件放在不受信任的区域，然后基于TCB来做数据相关操作。同时，SMMU的GPC能够约束外设对内存的访问，可以提供GPU环境隔离的基础能力。CCA架构下，Monitor拥有最高的权限，将安全模块部署到Monitor中，用这些模块来控制对显存和GPU寄存器的访问，就实现了一个类realm架构的可用于GPU的机密计算方案。这就是CAGE的基本思想。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYn9w1gticzmXqLTdianSah4xn8etnI7icLICiaFf2WqbCdZwN2omHvdohQ7LooM7N21jH7lVwFj4R1rA/640?wx_fmt=png&from=appmsg)

图2 CAGE架构

图2展示了CAGE的架构。CAGE在Monitor中部署了三个安全组件：

1. Shadow Task Mechanism：该机制使用不可信的GPU软件栈来创建和管理stub GPU任务，这些任务在提交前被安全的替换成带有真实数据的真实GPU任务。这需要配合调整GPU任务内存结构。Stub任务中只有相关配置信息，不携带任何敏感数据，敏感数据会通过加密信道预先传输到realm中。

2. GPU Environment Protection：在Shadow Task Mechanism的内存布局基础上，保护GPU运行时和GPU内存，防止非法访问。CAGE利用了CCA和GPC现有的内存隔离机制，实现GPU执行环境和其他组件之间的双向隔离。

3. GPT Maintenance Optimization：CAGE需要使用不同的GPT来确保机密计算环境和其他组件的内存隔离。CPU GPT由Monitor在Boot阶段初始化，而GPU GPT在对应realm被创建的同时初始化，CAGE在GPU机密计算过程中动态的管理这些GPT，以实现计算上的优化。

利用上述三个组件，CAGE实现了对GPU计算中数据的保护，同时使性能损失尽可能小。

五.  总结

本文介绍了一种支持ARM CCA的GPU机密计算实现。CAGE方案在Arm CCA的基础上，针对GPU设计出realm风格的机密计算架构，保护了GPU计算的机密性和完整性，迈出了将Arm机密计算扩展到GPU的重要一步。

参考文献

[1] Wang, Chenxu, et al. "CAGE: Complementing Arm CCA with GPU Extensions." Network and Distributed System Security (NDSS) Symposium. 2024.

内容编辑：创新研究院 杨博杰
    责任编辑：创新研究院 陈佛忠

本公众号原创文章仅代表作者观点，不代表绿盟科技立场。所有原创内容版权均属绿盟科技研究通讯。未经授权，严禁任何媒体以及微信公众号复制、转载、摘编或以其他方式使用，转载须注明来自绿盟科技研究通讯并附上本文链接。

**关于我们**

绿盟科技研究通讯由绿盟科技创新研究院负责运营，绿盟科技创新研究院是绿盟科技的前沿技术研究部门，包括星云实验室、天枢实验室和孵化中心。团队成员由来自清华、北大、哈工大、中科院、北邮等多所重点院校的博士和硕士组成。

绿盟科技创新研究院作为“中关村科技园区海淀园博士后工作站分站”的重要培养单位之一，与清华大学进行博士后联合培养，科研成果已涵盖各类国家课题项目、国家专利、国家标准、高水平学术论文、出版专业书籍等。

我们持续探索信息安全领域的前沿学术方向，从实践出发，结合公司资源和先进技术，实现概念级的原型系统，进而交付产品线孵化产品并创造巨大的经济价值。

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiayDdhDbxUby1015gywIBBffBcajfQYiawvOY5CaPz1AToFT9QgyCdcGhhGCTQdzuheM5uVWicDqicLe2hNlzUVUw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**长按上方二维码，即可关注我**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYc15Dsy8RcPfwerHzBEhBVQk20S88RRtnlBS56ZnUv3JStz1JUyyBicDvreCNoDaJZ8ul5xxtWRmg/0?wx_fmt=png)

绿盟科技研究通讯

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYc15Dsy8RcPfwerHzBEhBVQk20S88RRtnlBS56ZnUv3JStz1JUyyBicDvreCNoDaJZ8ul5xxtWRmg/0?wx_fmt=png)

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