---
title: G.O.S.S.I.P 阅读推荐 2024-11-01 交叉火线—对苹果设备跨异构计算单元内存的模糊测试
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499093&idx=1&sn=ce06536691fa915b82f009ff29147964&chksm=c063d38cf7145a9a65c53900038e6ab37710128acea5547ee150318161543dc8eb9a53ed0f8c&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-11-02
fetch_date: 2025-10-06T19:17:58.780479
---

# G.O.S.S.I.P 阅读推荐 2024-11-01 交叉火线—对苹果设备跨异构计算单元内存的模糊测试

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21FoZT9ibbDEkcHx3K8IFOKYpKG4wSESWiaK8MsGfxM3ZO4UPI7Rk6IBoGIv5XOBeLR3lEffOe04UI6w/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-11-01 交叉火线—对苹果设备跨异构计算单元内存的模糊测试

Jiaxun@ZJU

安全研究GoSSIP

今天为大家推荐的论文来自浙江大学网络空间安全学院申文博老师研究组与中关村实验室、美国哥伦比亚大学、薮猫科技合作完成并投稿的，发表在CCS 2024上的最新研究论文**CrossFire: Fuzzing macOS Cross-XPU Memory on Apple Silicon**。该论文提出并实现了首个针对Apple Silicon GPU/NPU内存破坏缺陷的模糊测试工具CrossFire，评估了在macOS中跨XPU（GPU和NPU）内存交互带来的安全隐患。此外，该论文揭示的跨XPU交互逻辑不仅适用于苹果操作系统，也适用于其他采用统一内存架构（UMA）的设备和系统。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FoZT9ibbDEkcHx3K8IFOKYpFZM0yShVblkJE0sNeNM8qv3pLsAXRHIibPElstwTwLBG95W5nOcgibqg/640?wx_fmt=png&from=appmsg)

随着AI技术的广泛应用，GPU和NPU等异构计算单元被大量引入，显著提升了设备在图像处理、机器学习等任务中的性能。CPU通常具有较全面的安全防护机制，但GPU等异构计算单元的安全防护措施却相对不足。GPU和NPU处理敏感数据时，缺乏完善的隔离和防护机制会引入新的攻击面，导致攻击者能够利用GPU/NPU的内存破坏缺陷攻击CPU，绕过CPU侧的防护机制。因此，挖掘XPU的内存破坏缺陷具有重要意义。

模糊测试是发现软件缺陷的有效手段之一。然而，通过模糊测试挖掘XPU的内存破坏缺陷极具挑战性。首先，模糊测试的载荷需要在正确的通信环境和上下文中被注入到内存的有效区域，但建立这种复杂环境困难大且有效区域有限。其次，合法的内存数据生成难度较大，因其数据结构复杂、内核检查严格且检查代码隐蔽在调用链深处。最后，由于macOS的生态封闭性（例如相关内核扩展和固件是闭源的），全面插桩以获取操作系统与XPU的交互逻辑变得困难，现有工具如KextFuzz的插桩覆盖率较低，无法满足这一需求。

CrossFire是首个专为分析和挖掘XPU内存破坏缺陷而设计的工具。作者基于m1n1 hypervisor构建了一套完整的macOS执行跟踪工具链并集成至CrossFire，其能够对几乎所有内核扩展和XNU内核进行详尽的执行流跟踪。CrossFire深入研究了跨XPU内存的管理机制，并创新性地提出了三项核心技术：基于虚拟化的跨XPU内存监控与定位技术（MemPin）、针对XPU的数据约束提取技术（ConExtract）与XPU可达感知的被动模糊测试技术。借助这些技术，CrossFire能够有效识别跨XPU内存中的关键测试区域，生成有效的数据变异，并感知这些变异是否被XPU处理。

得益于上述设计和技术创新，CrossFire共发现了15个系统缺陷，其中8个已被复现和确认，获得了2个Apple的CVE编号及Apple的公开致谢。

**1. 背景与挑战**

随着人工智能和高性能计算需求的日益增加，macOS中的XPU（如GPU、NPU）被广泛应用于图形处理、机器学习等领域。然而，由于XPU通常缺乏CPU所具备的完善的内存保护机制（如指针认证、地址空间布局随机化等），其安全性相对较弱，成为潜在的攻击目标。苹果芯片上的统一内存架构（UMA）进一步扩大了XPU的攻击面，因为CPU与XPU共享同一内存区域，攻击者通过XPU便可能威胁到运行在CPU上的软件和系统。

通过作者的分析，Apple Silicon上的跨XPU内存主要有两类。如图1所示，其分别是：类型1，XPU与CPU的用户态代码共享的内存；类型2，CPU用户态代码与内核代码之间共享的内存，并用于进一步与XPU共享并处理。这两种内存在系统中均分配有共享标签，可以帮助CrossFire识别它们。类型2内存在内核代码中可以通过ID被提取使用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FoZT9ibbDEkcHx3K8IFOKYpyVEsM4zECSE4Jv7XUroQ2ZtqiahIvzl5siax84aELycCfZUIFHt8cicxA/640?wx_fmt=png&from=appmsg)

有关类型1和类型2内存用法的文档非常有限。通过跟踪并分析系统执行流，作者得出了两个关键发现。首先，从功能角度来看，类型2内存比类型1内存更为重要。类型1内存仅包含由XPU用户态处理的相关计算数据，包括计算的输入/输出以及指向计算资源（如顶点、片段等）的XPU用户态虚拟地址。相比之下，类型2内存包含由XPU内核处理的相关控制指令。其次，从攻击面的角度来看，类型2内存比类型1内存更有价值。XPU中有两层隔离：用户-内核隔离和XPU-CPU隔离（XPU侧的内存映射防护，将XPU与CPU侧的操作系统隔离，防止XPU直接访问操作系统内存）。因此，XPU内核需要进入特权状态调用特权函数来访问操作系统的内存。由于存在这两层隔离，类型1内存必须穿过两层隔离才能影响CPU侧的操作系统，这使得其攻击面较小。然而，类型2内存直接影响XPU内核的控制流，因此更容易绕过这些隔离，导致更大的攻击面。根据上述发现，CrossFire主要关注类型2跨XPU内存，因为类型1内存总体上不是一个有价值的模糊测试目标。

一个典型的类型2跨XPU内存调用如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FoZT9ibbDEkcHx3K8IFOKYpSJmw4Zicehia71Bq3YgBKe9xNRLqx06wv36KvRerzNicRwzm4OwmJ4CWw/640?wx_fmt=png&from=appmsg)

简要来说，在类型2跨XPU内存中，用户态程序首先将相关数据写入用户态-内核共享内存中，随后内核根据用户的请求填充内核-XPU共享内存。具体地，其详细数据处理过程如图2所示。1）用户态程序分配用户态-内核共享内存并获得内存标识符ID和目标块umem0。2）用户态程序准备有效的数据。3）用户态程序通过系统调用或驱动调用向内核发出请求。ID将作为系统调用参数的一部分被发送。4）内核通过ID获取共享内存目标块kmem0。kmem0和umem0共享相同的物理内存区域。5）内核检查kmem0中的内存数据。6）内核根据kmem0的内容填充内核-XPU共享内存kmem1。7）内核将内存提交给XPU。8）XPU处理共享内存kmem1。

模糊测试是发现漏洞最有效的方法之一。掌握了以上的XPU交互流程后，便可以运用模糊测试来测试XPU交互逻辑。然而，这一测试面临以下三个挑战：

1. 模糊测试的载荷需要在一个**正确建立的通信环境****与上下文**下注入到跨XPU内存的**有效区域**中。然而，建立这样的通信环境与上下文是复杂的。用户态程序与XPU间的调用通常是：用户态程序->用户库->内核->XPU(协处理器)固件，然后XPU再进行处理。此外，尽管CPU和XPU通常会分配大量的跨XPU内存，但其中只有一小部分是有效的模糊测试区域。其主要原因是即使在跨XPU内存中存储少量有效数据，也需要分配整个内存页面。
2. 只有**通过内核检查**的载荷才会进一步提交到XPU。生成合法的跨XPU内存数据比生成一般的内核输入更加困难：1) 跨XPU内存输入的大小更大，结构更复杂。根据作者的调查，跨XPU内存的平均总大小为0x5b3f60字节。2) 内核对负载的检查严格。在一个简单的例子中，作者通过手工分析发现，在有效区域的0xa20字节中，有0x130字节会被严格检查。3) 包含跨XPU内存数据检查的内核代码隐藏在系统的调用链深处难以定位。尽管内核在系统调用入口处解析大部分常规的系统调用输入，跨XPU内存数据只在其它准备工作完成后才被检查和处理。4) macOS的XPU相关内核扩展是闭源的，并且是用C++开发的，形成了大量的间接调用，从而使得大多数现有的静态和动态分析方法无效。
3. 最后，难以全面拦截macOS的执行过程以**分析真实的跨XPU内存**操作。由于macOS的大部分内核扩展和固件是闭源的，源代码插桩是不现实的。KextFuzz在面临这样的困境时提出了一种通过二进制重写对kext二进制文件进行插桩的方法，但该方法仅限于无用指令的插入位置。实验表明KextFuzz只能对大约30%的基本块进行插桩，这无法满足作者的需求。

**2. 设计与实现**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FoZT9ibbDEkcHx3K8IFOKYpOeXQu8bNLQMkkU5vOmx7P6j9Qx23vNricDQyha2dic8BfapPsK3qmQlQ/640?wx_fmt=png&from=appmsg)

CrossFire针对跨XPU内存中的有效区域进行模糊测试，提出了三个技术：

1. **基于虚拟化的跨XPU内存监控与定位技术（MemPin）**：通过利用正常程序的通信上下文，将模糊测试的载荷注入到合法的输入中，并使用硬件虚拟化提供的Stage-2页表监控macOS对跨XPU内存的访问，精确定位有效的模糊测试区域，从而提升模糊测试效率。
2. **针对XPU的数据约束提取技术（ConExtract）**：从内核代码中提取到达XPU所需要的数据约束条件，提高模糊测试数据通过内核的严格检查并成功提交至XPU的概率。
3. **基于覆盖率感知XPU可达的Fuzzing**：通过hypervisor实现macOS的执行流跟踪，不仅可用于分析真实的跨XPU内存操作，还能在不手工分析的情况下感知变异载荷是否提交至XPU。一旦载荷导致通信环境被破坏，系统会自动重启至正常程序状态。

**2.1 基于虚拟化的跨XPU内存监控与定位技术（MemPin）**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FoZT9ibbDEkcHx3K8IFOKYp4ljMx1NibhDat1ABuVyKXXTYzZUoibtK7PJ3SfgTnE6nfeiaWXkq2vN9w/640?wx_fmt=png&from=appmsg)

如上图所示，启动正常与XPU进行交互的程序后，因为所有的内存在虚拟内存区域中都有相应的共享标记，MemPin可以把所有标记共享的内存块都找出来，然后通过用户态程序与内核对内存块的读写将有效区域找出来。具体来说，1) 作者可以找到所有分配的跨XPU内存范围MEM0、MEM1和MEM2，这些内存范围可以通过VMA标签轻松获取。作者将这三个范围转换为物理地址，并设置监控。2) 通过监控，作者可以获取这三个MEM上的所有用户写入区域。3) 随后，当内核通过ID访问被监控的跨XPU内存时，监控将感知到这一操作，这意味着被访问的跨XPU内存就是目标块。通过步骤2提供的用户写入区域，作者可以精确定位模糊测试的有效区域，而不用去管ID是从哪生成又是如何传播的。

为了实现上面的想法，MemPin通过对跨XPU内存的Stage-2页表项的操作（无效化与有效化），做到了在用户态程序与内核对共享内存进行操作的时候触发系统异常的效果。在异常处理中MemPin可以区分出触发内存操作的是用户态还是内核态、读操作还是写操作。MemPin从而做到了对模糊测试有效区域的定位，同时还做到了对相应跨XPU内存处理代码的定位。

**2.2 针对XPU的数据约束提取技术（ConExtract）**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FoZT9ibbDEkcHx3K8IFOKYpFrcNgC1Y4EibZFWvq8mC4bgBf34OjUwNmAtyrcuKQuiar9CxQ9Qms70g/640?wx_fmt=png&from=appmsg)

ConExtract的流程分为三步。首先，其对内核二进制文件进行指令替换和预处理。其次，ConExtract在macOS运行后记录内核的执行流和上下文。最后，ConExtract为跨XPU内存的每个字节分配唯一的污点标签，并根据收集的记录设置模拟执行引擎的运行环境，在模拟执行过程中跟踪污点标签的传播。当ConExtract检测到内核对跨XPU内存的检查时，它识别出与该条件传播相关的污点标签，并定位到跨XPU内存中包含数据约束的位置。通过污点分析提取的数据约束即为不可变字节的位置，其可以指导模糊测试中跨XPU内存的变异，从而提高了变异载荷通过内核检查并到达XPU的成功率。

**2.3 基于覆盖率感知XPU可达的Fuzzing**

CrossFire选择对内核扩展进行插桩而非XPU固件，主要有两个原因。第一个原因是XPU固件很难进行插桩。XPU固件是闭源且复杂的，导致模拟执行XPU固件进行插桩非常困难，目前尚无公开研究针对Apple XPU固件的模拟执行。第二个原因是XPU固件受硬件保护，用户无法在运行前或运行时对XPU固件进行插桩。

在作者的实验中，当目标块无法提交到XPU时，其将触发相应的错误处理。随后，XPU将拒绝种子应用程序对XPU的进一步任务提交（但种子程序对此无感知，仍会持续向内核提交XPU请求）。此外，因为被拒绝提交的执行流包含的基本块数量远少于正常提交时执行的基本块数量，所以CrossFire可以通过基本块覆盖率感知提交的状态。

因此，CrossFire结合了两项之前提到的新技术：MemPin和ConExtract，采用了一种基于Hooking的感知XPU可达的灰盒模糊测试方法。它会在这些技术设定的范围内变异目标内存生成载荷。同时，CrossFire利用基本块的覆盖率来判断变异载荷是否到达XPU。如果出现载荷未到XPU的异常，CrossFire将重新执行种子应用程序以恢复正常的XPU交互环境。

**3. 实验总结**

CrossFire对多款应用程序进行了评估，总结如下：

1. 通过MemPin，CrossFire能够减少平均87.3%的无效变异区域。

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FoZT9ibbDEkcHx3K8IFOKYpSkKn6kIH07wJ8QX0WhHIRL7j1QhMY3ibbeCeBmRNzfk9B3Apblt4oSA/640?wx_fmt=png&from=appmsg)
2. 通过ConsExtract，CrossFire能够提升大约83.9%的模糊测试速率（单位时间内的有效到达XPU的载荷提交）。
3. 通过ConsExtract中的插桩方法，CrossFire对macOS中所有内核扩展都进行了插桩测试。作者发现除了corecrypto 和AppleMobileFileIntegrity以外，剩余的内核扩展的所有基本块都可以被插桩。
4. Bug发现与确认。CrossFire一共发现了15处苹果系统的缺陷。目前，苹果在macOS Sequoia 15的更新中对其中的6处进行了合并致谢，在此前Apple系统的安全更新中给予了2个CVE。

**4. 工具开源**

CrossFire已在GitHub上开源 （项目地址：https://github.com/ZJU-SEC/crossfire），研究人员还可以通过这个工具追踪调研macOS的其他内核组件。

作者还组建了TOAST（Terminal OS Architecture & Security Team）研究小组，致力于终端操作系统与体系结构安全技术的研究和创新。小组地址：https://toast-research.tech，https://toast-research.github.io，其中提供了团队的成员介绍以及最新研究进展等。

论文pdf获取：联系作者吧~

投稿作者简介：

朱家迅，浙江大学博士生，浙大AAA成员，导师为申文博研究员。他的主要研究领域包括终端设备的软件与系统等。他的成果发表于学术会议ACM CCS、USENIX Security以及工业会议Black Hat USA，曾获全国大学生信息安全竞赛一等奖。

林明皓，浙江大学科研助理，主要研究方向为逆向。他的成果发表于ACM CCS、SpaceSec以及Black Hat USA，曾在腾讯玄武与科恩实验室、美国科罗拉多大学实习工作，获DataCon2022 IOT安全第一名，DataCon2023漏洞识别第二名，GeekCon2024第一名。

申文博，浙江大学百人计划研究员，计算机科学与工程系副主任。他的研究方向为操作系统安全、云原生系统安全与软件供应链安全，在各类顶级会议已累计发表超过50篇论文，并获得了4项杰出论文奖。

个人主页 https://wenboshen.org 。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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