---
title: GPU机密计算——以NVIDIA H100为例
url: https://mp.weixin.qq.com/s?__biz=MzIyODYzNTU2OA==&mid=2247497490&idx=1&sn=08e3711bf076d67599497ec33b2d6aa7&chksm=e84c51cddf3bd8dba463e17415522ffe2dae22f30e82a4de5664fb41bc80cb495dba9d6e8e54&scene=58&subscene=0#rd
source: 绿盟科技研究通讯
date: 2024-07-03
fetch_date: 2025-10-06T17:43:19.978944
---

# GPU机密计算——以NVIDIA H100为例

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hiayDdhDbxUa7Ef0Td7En3riaNEuU1YPWwvbiaHfbLdlABA6ePNBibGHibBHTQWDTGOicBxYHYUBCEICNtjH5AtYerGw/0?wx_fmt=jpeg)

# GPU机密计算——以NVIDIA H100为例

原创

创新研究院

绿盟科技研究通讯

![](https://mmbiz.qpic.cn/mmbiz_gif/hiayDdhDbxUa7Ef0Td7En3riaNEuU1YPWwudiapTsLbsnKIn6MrY6pFl9Q6CCIibEKyvefUdoqZUbzWyxOP5eraztQ/640?wx_fmt=gif&from=appmsg)

一.  背景

机密计算通过在基于硬件的经验证的受信任执行环境中执行计算来保护正在使用的数据。这些安全且隔离的环境可以防止未经授权访问或修改使用中的应用程序和数据，从而提高管理敏感数据和受监管数据的组织的安全级别。为了将GPU也纳入可信执行环境，保护GPU上的数据的机密性和完整性，英伟达在H100显卡首次集成了机密计算能力。

二.  英伟达GPU机密计算介绍

2.1

机密GPU的发展

为了保护视频的版权，保证播放过程中的视频数据安全，英伟达在显卡中应用了VPR（VIdeo Protected Region）技术，该技术通过独特的硬件和固件保护GPU内存区域。当GPU内存被VPR保护时，有且仅有一个安全显示引擎可以从该区域读取数据并写入HDMI或DP通道，其他任何引擎在尝试读出数据时都会出错。

受VPR启发，英伟达在Ampere架构GPU中实现了机密计算的部分基础能力。Ampere架构的固件允许在GPU内存里创建一个保护计算的飞地，保证仅有SEC2安全微控制器可以从飞地读取数据，并且加密后写入外部。这项能力被称作APM(Ampere Protected Memory)。

机密计算要求同时保护数据和代码的机密性和完整性，APM仅提供了数据的机密性，无法提供代码的机密性，也不能保护数据和代码的完整性。

最终在Hopper架构的GPU H100上，英伟达实现了完整的机密计算能力。

2.2

H100机密计算架构

英伟达在H100上实现的机密计算依赖CPU上已有的机密虚拟机可信执行环境（CVM TEE，confidential virtual machine trusted execution environment），例如AMD CPU的SEV-SNP和Intel CPU的TDX1.x。图1展示了该方案的架构。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUa7Ef0Td7En3riaNEuU1YPWwaSvzyX06z96icGqjPm3jQErEKkibuCze19N8mIB8fIvP2yuqllqFxUBg/640?wx_fmt=png&from=appmsg)

图1 可信执行环境

GPU的内存从逻辑上被划分为受保护区域和不受保护区域，不受保护的区域没有访问限制，GPU 计算保护区（CPR，compute protected region）则有访问保护。如图1所示，GPU以机密模式启动时，CPR内存的输入和输出受到限制：PCIe防火墙阻止CPU访问大部分寄存器和CPR内存，NVLink防火墙阻止其他GPU对当前GPU CPR内存的访问。除非有硬件强制加密，否则GPU中的硬件引擎无法向CPR之外写数据。DMA引擎是唯一一个用户态可用的能对CPR外部做读写的引擎，DMA硬件确保数据在被写到CPR之外时会先经过硬件加密。这些措施确保了CPR中的数据不会被泄露。

以机密计算模式启动的GPU会启用硬件保护，确保代码和数据的机密性和完整性：

1、基于安全启动和度量，在启动时建立信任链。

2、通过SPDM（Security Protocol and Data Model）会话实现与CPU TEE中的驱动的安全连接。

3、GPU会生成一个证明报告，提供签名之后的度量值。

机密计算环境中的用户可以验证该证明报告，仅在报告是可靠且正确的情况下继续使用GPU。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUa7Ef0Td7En3riaNEuU1YPWwia9Jtaf70GHOBC5uv6xMh0hG0NUtXsjEkmIKgLxVWzmNN826PkhDrtA/640?wx_fmt=png&from=appmsg)

图2 机密计算模式保护GPU

图2展示了GPU在机密计算模式关闭和开启时，和主机上的CPU进行数据交换的流程。在GPU机密计算模式关闭时，英伟达驱动和GPU进行明文通信，hypervisor对GPU有完全访问权限，GPU中的数据没有足够的安全性；当机密计算模式开启时，机密虚拟机中的英伟达驱动会和GPU TEE建立一个安全通道用于数据交换，并且每个guest驱动组件在与GPU通信的时候，使用独立的加密密钥保证数据安全。机密计算模式开启后，hypervisor无法访问机密虚拟机的CPU内存以及GPU显存。

英伟达针对侧信道攻击也做了相应的防御。在GPU机密计算模式下，硬件确保所有GPU性能计数器处于关闭状态，防止可能的数据泄露。

2.3

GPU证明

为了将GPU纳入可信范围，需要让GPU证明其合法性，并且给出当前处于良好已知状态的证据。这里的证据就是GPU的度量值，验证报告就是GPU信任根签名后的度量值。签名保证了度量值不会被纂改，通过建立的安全信道获取证明报告，可以消除设备欺骗攻击。

获取报告后，CVM需要验证报告的真实性，评估GPU状态。状态评估需要一组基准值，这组值称为RIM(Reference Integrity Manifest)，RIM由英伟达官方离线生成，并随每个驱动和VBIOS的版本更新一起发布。通过比较GPU给出的度量值和英伟达给出的RIM，CVM验证GPU状态是否合法。

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUa7Ef0Td7En3riaNEuU1YPWwwEibBU1kibySAoicmueR0HGZcaicIM2w4y7j0FkN76nHJshiareqEBSCwEQ/640?wx_fmt=png&from=appmsg)

图3 本地验证GPU证明报告

整个过程如图3所示：

（1）CVM和GPU建立可信通道，作为后续数据交换的基础。

（2）CVM请求GPU给出证明报告。

（3）GPU根据当前状态，获取度量值，生成证明报告，并使用信任根对报告签名。

（4）GPU将签名后的证明报告发送给CVM。

（5）CVM对报告进行验证：验证证书签名的有效性，取出度量的标准值，比较报告给出的度量值和标准值，生成验证结果。

生成证明报告需要RTR（Root of Trust for Report）、RTS（Root of Trust for Storage）和RTM（Root of Trust for Measurements）。RTS对应安全存储，用于存储度量值。RTM在图3中没有表现出来，它负责度量选定的GPU状态，并将度量结果存储到RTS中。RTR负责获取度量值，生成证明报告，并用证明密钥对报告签名。

CVM中的本地验证器用于验证GPU给出的报告。验证过程需要英伟达提供的两个远程服务：Nvidia OCSP Service和Nvidia RIM Provider Service。

OSCP（Online Certificate Status Protocol）Service用于验证证书链。本地验证器可以根据OCSP服务的返回确认证书的状态：如果返回值是“good”，那么GPU的报告是可信的；如果返回值是“revoked”，则GPU不可信，可以断开与当前GPU的连接，或者采取其他安全措施。

RIM Provider Service持有英伟达所有显卡驱动和VBIOS发布版本所对应的RIM文件。验证器通过GPU证明报告中携带的唯一标识符，请求英伟达服务获取对应的RIM文件。之后，使用该文件验证GPU是否可信。

本地验证器帮助实现简单且快速的GPU机密计算。但是，官方也指出该方案目前存在一些问题，比如本地验证器必须明确被CVM信任。为了解决相关问题，英伟达给出了远程验证器的方案，即将验证服务放在远程服务器上，业务方先验证服务可靠性，确定服务可靠后再使用验证服务来验证报告。目前英伟达已经部署了类似服务NRAS（NVIDIA Remote Attestation Service），该服务目前仅支持GPU验证，将来可能会扩展到其他的英伟达产品。

三.  总结与展望

机密计算是数据安全发展历史上的伟大创新，并且正处在不断的发展中。英伟达将机密计算扩展到GPU中，在hopper架构中首次引入完整的机密计算能力，增加了机密计算的应用范围。2024年3月，英伟达发布Blackwell架构，进一步强化了机密计算能力，主要目的是为大语言模型提供高性能的安全性。相信在不久的将来，伴随着软硬件的技术创新，所有计算都可以成为机密计算。

参考文献

Dhanuskodi, Gobikrishna, et al. "Creating the First Confidential GPUs: The team at NVIDIA brings confidentiality and integrity to user code and data for accelerated computing." Queue 21.4 (2023): 68-93.

https://docs.attestation.nvidia.com/OCSP/ocsp\_introduction.html

内容编辑：创新研究院 杨博杰
    责任编辑：创新研究院 陈佛忠

本公众号原创文章仅代表作者观点，不代表绿盟科技立场。所有原创内容版权均属绿盟科技研究通讯。未经授权，严禁任何媒体以及微信公众号复制、转载、摘编或以其他方式使用，转载须注明来自绿盟科技研究通讯并附上本文链接。

**关于我们**

绿盟科技研究通讯由绿盟科技创新研究院负责运营，绿盟科技创新研究院是绿盟科技的前沿技术研究部门，包括星云实验室、天枢实验室和孵化中心。团队成员由来自清华、北大、哈工大、中科院、北邮等多所重点院校的博士和硕士组成。

绿盟科技创新研究院作为“中关村科技园区海淀园博士后工作站分站”的重要培养单位之一，与清华大学进行博士后联合培养，科研成果已涵盖各类国家课题项目、国家专利、国家标准、高水平学术论文、出版专业书籍等。

我们持续探索信息安全领域的前沿学术方向，从实践出发，结合公司资源和先进技术，实现概念级的原型系统，进而交付产品线孵化产品并创造巨大的经济价值。

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiayDdhDbxUYMlia0GKQHicTyBRHSyD6ibba4VF5uA0VNyPYLNlSictiaOkWdN0OIForLCw4RqxibM0iaibia8jyPFs37bSQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

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