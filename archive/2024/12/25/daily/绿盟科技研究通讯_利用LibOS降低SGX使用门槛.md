---
title: 利用LibOS降低SGX使用门槛
url: https://mp.weixin.qq.com/s?__biz=MzIyODYzNTU2OA==&mid=2247498138&idx=1&sn=5c837a62353956bf5bb9234385cf0771&chksm=e84c5f45df3bd6538f90ba9a54a660075b5a03d28392a03bdcce1572c39a2e1af06c75d973f8&scene=58&subscene=0#rd
source: 绿盟科技研究通讯
date: 2024-12-25
fetch_date: 2025-10-06T19:38:21.771655
---

# 利用LibOS降低SGX使用门槛

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hiayDdhDbxUamQra0EMdw6qWMHdRRkE0D3TZRDbyScCTSIEsibK6lib23JZHur436fyCZrk3Dt63rAyE7Ok68xNIQ/0?wx_fmt=jpeg)

# 利用LibOS降低SGX使用门槛

原创

创新研究院

绿盟科技研究通讯

![](https://mmbiz.qpic.cn/mmbiz_gif/hiayDdhDbxUamQra0EMdw6qWMHdRRkE0D7ibJJVg74zfhibX1Dibkk0dIxsybH7a4rJEQtzx9VC47bkRr4dDRRxAcQ/640?wx_fmt=gif&from=appmsg)

一.  什么是LibOS

lIbOS的全称是library operating system，即“库操作系统”。顾名思义，lIbOS的主要作用是将一些原本属于操作系统的服务（如网络通信、文件系统等）进行模块化与抽象化，最终以库的形式提供给应用程序调用，其具有轻量化、跨平台、可定制等优点。与传统操作系统不同，lIbOS本质是使用高级编程语言是实现的一系列库，其工作在应用层，通过实现对所涉计算机资源的管理与调度功能，让应用程序能够直接访问所涉计算机资源，并为应用程序提供所需的运行时。我们可以将它和容器技术以及虚拟化技术放在一起比较，如图1所示。相比于容器技术中多个应用共享宿主机内核，LibOS为每个应用提供单独且隔离的运行环境，具有更好的隔离性；而LibOS是只具有部分OS能力，相当于对完整的OS做了裁剪，相比于虚拟化技术更加轻量，资源消耗更少。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUamQra0EMdw6qWMHdRRkE0DgI63RseqD07G2x3B9picPkuEficn3aZERLmlWKgeya9Bxib3tv2wcZW8Q/640?wx_fmt=png&from=appmsg)

图1 容器、虚拟机与LibOS的对比

对于LibOS的特点总结如下[1]：

（1）模块化：将操作系统的功能结构化，按模块划分，以类库（library）来实现和封装系统的基本功能。模块化可以抽象出软件内部的实现细节，限制单个源代码更改的范围，并方便对各个部分做出修改和重用，满足其专业定制的需求，灵活组装出精简、优化的库操作系统。

（2）专用化：开发人员可以根据自己对应用服务的特殊需求改写库，实现自定义抽象，省略不必要的抽象，跨设备驱动程序和应用逻辑执行全系统优化，剔除不需要的系统组件，从而构建出高度专业化的操作系统，满足其安全性和高效性。

（3）单地址空间：应用程序与特定的驱动、核心库运行在一起，共享同一内存页表，不存在运行时状态上下文切换的额外开销，因此可以提高程序的运行速率，实现更高效的应用服务。

在机密计算领域中，LibOS被用于简化SGX应用构建的工作中，使得SGX应用开发难度得以降低。目前有两大主流开源项目致力于实现LibOS来简化SGX的集成工作，它们分别为Gramine[2]与occlum[3]。下面我们将对它们进行介绍与分析，介绍它们如何通过LibOS来降低SGX使用门槛。

二.  LibOS如何降低SGX使用门槛

2.1

常规SGX应用构建过程

长期以来，SGX应用的开发都具有一定的上手门槛，开发者需要手动管理 Enclave 生命周期、内存隔离、线程调度等底层细节，这不仅增加了开发难度，也限制了SGX技术的广泛应用。以SGX工程示例为例（图2），开发者需要分别在App与Enclave中分别实现非可信区与可信区代码，并在Enclave.config.xml中定义enclave属性，如堆栈大小、内存大小、安全策略等。此外，开发者还需要再Enclave.edl描述文件中定义Enclave与不可信区域之间的通信接口，包括ecall（进入 Enclave）与ocall（调用外部功能）等。可以看出，与开发传统应用相比，开发SGX应用的复杂度大大提高，其需要开发者分别设计可信部分与不可信部分应用以及它们之间的通信，并且要自行管理Enclave相关配置。若开发想要将已有应用迁移入SGX中，则需要对应用进行重构，这将大幅度增加SGX的使用门槛。而使用LibOS则可以对这些复杂的部分进行封装，简化SGX应用的构建过程。下面我们将分别通过介绍两个开源项目，来看看它们是如何简化SGX应用构建难度的。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUamQra0EMdw6qWMHdRRkE0D5VqKwNKVpqkia4wNd6kv0nuXalAWyQqcnlLO7UUktBslpicicBcVKSWTA/640?wx_fmt=png&from=appmsg)

图2 SGX工程示例

2.2

Gramine项目介绍

Gramine是机密计算联盟的孵化项目之一，其前身为Graphene。它是一个通用的LibOS，它可在不修改原始应用的情况下，将应用运行至SGX环境中。其示例代码图3所示。开发者仅需开发核心代码，并再Gramine的配置中定义执行策略与安全策略。完成编译后可使用Gramine的命令行工具，通过gramine-sgx helloworld命令快速将程序运行至受保护的SGX Enclave中。需要注意的是，开发者可以在配置中开启动态内存释放与分配功能，以简化对Enclave的管理工作。该项目支持对多种高级编程语言所实现的项目进行迁移，在其示例中，包含了如何将python、rust、nginx、redis等项目运行至SGX中的示例。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUamQra0EMdw6qWMHdRRkE0DBfuRDnzzD4oyaE3gaz1OGJTPSEmzoIcampzllVfqvgWdacia5UPVYPQ/640?wx_fmt=png&from=appmsg)

图3 Gramine工程示例

Gramine的核心思路在于，通过实现一个LibOS来封装Linux系统调用，提供一个操作系统级的抽象层，在SGX Enclave区域中模拟大部分操作系统功能，实现了应用程序在不需要修改的情况下即可在SGX Enclave中运行。此外，Gramine还提供了Enclave进程管理、虚拟化支持、文件系统支持、调试支持等，在扩大了安全防护范围地同时，帮助开发者能够更容易地在SGX环境中调试应用程序。除了支持SGX，Gramine还致力于丰富其封装的系统调用，实现在任意平台上均可运行Linux应用程序。

2.3

occlum项目介绍

occlum也是机密计算联盟的孵化项目之一，旨在帮助开发者快速将原有应用迁移至SGX中。其思路与Gramine项目类似，同样为实现一个LibOS，将操作系统的核心功能封装成库，与应用程序集成，使得常规的Linux应用程序可以在不做大规模修改的情况下运行在SGX中，其架构如图4所示。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUamQra0EMdw6qWMHdRRkE0DH6k93icgmlZCcVPZWkpKLbzkZJXZwoiaDyM8sKoLqeLdXXyA2mZe3pJw/640?wx_fmt=png&from=appmsg)

图4 occlum架构

我们继续分析其示例工程[5]。如图5所示，用户需要在配置文件中定义如何将文件和资源集成到occlum实例中去。在编译核心代码时，需要使用occlum提供的occlum-gcc进行编译。而要在occlum上运行代码，则需要先初始化occlum实例，生成安全的文件系统镜像与occlum SGX Enclave，然后再将应用运行至SGX Enclave中。其操作流程如下所示：

```
```shellmkdir occlum_workspace && cd occlum_workspaceocclum init && rm -rf imagecopy_bom -f ../hello.yaml --root image --include-dir /opt/occlum/etc/templateocclum buildocclum run /bin/hello_world```
```

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUamQra0EMdw6qWMHdRRkE0D2F5MXMnm9ZQVjoricetmibFLuL5F9YS6okbdaMwJiaz75Jt38rd0yZxTA/640?wx_fmt=png&from=appmsg)

图5 occlum工程示例

occlum同样支持将多种其它高级语言项目或应用运行至SGX中，它与Gramine一样具有很强的兼容性与移植性。Gramine是一种通用LibOS，而与之不同，occlum是专注于将普通应用运行至SGX Enclave的LibOS。它支持高效的多进程和多线程环境，优化了内存管理和并行计算的性能，提升了 SGX Enclave 中的计算效率。

三.  小结

本文我们介绍了LibOS的基本概念，并通过两个开源项目介绍了该技术如何帮助开发者降低使用SGX的难度。LibOS作为一种介于容器与虚拟化之间的技术，在一些场景中具有独到的作用。Gramine和Occlum则利用LibOS特点与SGX的安全需求，巧妙地利用LibOS简化了SGX环境下的应用开发。但二者在目标和优化重点上有所不同，Gramine适合大规模、云原生的应用，而 Occlum 更适用于需要高安全性和高效计算的 SGX 应用。本文旨在帮助读者对这一技术与开源项目有所了解，希望能够帮助读者根据自己的场景需求，选择合适项目，来构建属于自己的机密应用。

参考文献

[1].  舒红梅,谭良.库操作系统的研究及其进展[J].计算机科学,2018,45(11):37-44.

[2].  https://gramineproject.io/

[3].  https://occlum.io/

[4].https://github.com/gramineproject/gramine/tree/master/CI-Examples

[5].https://github.com/occlum/occlum/tree/master/demos/hello\_c

内容编辑：创新研究院 王拓
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