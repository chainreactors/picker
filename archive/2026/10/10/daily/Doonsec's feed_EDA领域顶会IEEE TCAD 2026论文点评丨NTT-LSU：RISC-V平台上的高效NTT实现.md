---
title: EDA领域顶会IEEE TCAD 2026论文点评丨NTT-LSU：RISC-V平台上的高效NTT实现
url: https://mp.weixin.qq.com/s/oDfwV0FEXF_wTm_1jFJUtQ
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T08:01:18.326946
---

# EDA领域顶会IEEE TCAD 2026论文点评丨NTT-LSU：RISC-V平台上的高效NTT实现

# EDA领域顶会IEEE TCAD 2026论文点评丨NTT-LSU：RISC-V平台上的高效NTT实现

原创

明经典
明经典

信息网络安全杂志

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**一、引子**

随着NIST后量子密码标准的正式发布，后量子密码方案能否在各类终端设备上高效运行，已成为关乎全球数字安全的核心议题。格密码以严谨的安全性证明和较高的计算效率等优势，成为应用广泛的主流方案，而数论变换（NTT）是格基密码系统高效落地的核心基石。RISC-V凭借开源、可定制的特性，已成为嵌入式、物联网等资源受限场景的主流架构，但长期以来，该平台上的NTT硬件加速始终陷入高性能与通用性不可兼得的技术困境，效率与灵活该如何取舍？发表于IEEE TCAD 2026的NTT-LSU: Tightly Coupled Architecture for Efficient NTT Implementation on RISC-V Processor一文，为解决这一困扰业界的技术难题提供了新的思路。

二、**论文速览**

近年来，RISC-V平台的NTT硬件加速主要分为内存映射（Memory-mapped）、松耦合（Loosely coupled）和紧耦合（Tightly coupled）三类主流方案。内存映射加速器挂载于系统总线，数据传输延迟极高；松耦合加速器依赖专用接口，通用性差且未解决传输延迟问题；传统紧耦合加速器普遍耦合于指令的译码（ID）或执行（EX）阶段，会拉低处理器主频且数据仍需在寄存器中转，此外，多为固定功能设计，仅支持单一后量子算法或安全等级，无法适配多场景的差异化需求。

这些缺陷共同导致了一个长期悬而未决的核心问题：RISC-V平台始终未能实现“低延迟、高灵活、低面积”三者的平衡。针对这一痛点，本文作者跳出了“加速器必须耦合于ID/EX阶段”的固有思维，提出将NTT 加速单元与RISC-V处理器的加载存储单元（LSU）深度紧耦合的全新架构，让NTT 单元直接从数据内存加载数据并将结果直接写回，彻底消除寄存器中转的额外开销，同时保证NTT单元不进入处理器关键路径、不影响主频。为进一步提升数据传输效率，作者设计了96/32位混合位宽数据通路：NTT运算时启用96位通路，单周期加载3个32位计算所需数据；普通运算则保持32位通路，从而控制功耗增长。此外还扩展了3条自定义RISC-V指令，支持多项式维度n、模数q的灵活配置与NTT/INTT运算的一键切换，并通过单蝶形单元资源复用、In-place计算等技术进一步压缩硬件开销。

基于XC7A200T FPGA平台的实验结果显示，该方案在保持CV32E40P 处理器50MHz主频不变的前提下，对ML-KEM、ML-DSA、FN-DSA三类NIST标准算法的 NTT/INTT运算实现了6.01-10.12倍的加速比，256点NTT运算仅需2310个时钟周期，吞吐量达到0.111，分别是传统协处理器方案的3.6倍和EX级集成方案的5.8倍；同时资源开销控制在极低水平，仅比原版处理器增加29.6%的查找表、12.5%的触发器和5个数字信号处理器，无需占用任何块随机存取存储器，最终在可扩展方案中取得了最优的面积-时间积（ATP）性能。

**三、深度解剖**

突破：重新定义了RISC-V紧耦合加速器的设计逻辑

本文最核心的贡献在于颠覆了“紧耦合=耦合于ID/EX阶段”的传统行业共识，首次提出将密码加速单元与LSU单元直接耦合的架构范式。这一设计带来两大革命性优势：其一，NTT单元不进入处理器关键路径，完全不影响处理器主频；其二，数据直接在内存与NTT单元间交互，彻底消除了寄存器中转的额外开销。这种“LSU紧耦合”的新思路不只局限于NTT加速，还为其他密码算法加速开辟了全新的研究方向。

技术分水岭：将RISC-V上的后量子密码加速推向实用临界点

长期以来，RISC-V的后量子密码加速方案始终陷入“性能-灵活-开销”的三角困境，NTT-LSU架构实现了三者的较优平衡，大幅提升NTT计算效率的同时，全面支持ML-KEM、ML-DSA和FN-DSA三类NIST标准算法，且资源开销仅为同类可扩展方案的1/3-1/2。

与经典工作对比可知，Fritzmann等人提出的RISQ-V紧耦合加速器、Banerjee等人提出的Sapphire加速器，虽然在单周期性能上更优，但均以显著增加硬件资源、牺牲可扩展性为代价，而本文在保持灵活通用的前提下，取得了较优的面积-时间积（ATP）性能。

Fritzmann工作链接：https://doi.org/10.13154/tches.v2020.i4.239-280

Banerjee工作链接：https://doi.org/10.13154/tches.v2019.i4.17-61

**四、局限与展望**

值得注意的是，本文仍存在一些有待完善的地方：其一，本文实验仅在FPGA平台进行，未完成ASIC流片验证，实际芯片的时序、功耗和面积表现仍需进一步验证；其二，加速器实际未考虑侧信道安全防护，而密码硬件的抗侧信道攻击能力也是实际应用中的重要要求之一。

未来，如果能在加速器上集成掩码、乱序等侧信道防护技术，可能会增强硬件的安全性与可靠性，此外，还可以将LSU紧耦合的思路拓展到其他后量子密码算法或者其他需要加速的场景中。

**五、写在最后**

开源的RISC-V架构是我国芯片自主可控的重要突破口，而后量子密码迁移又是未来数字安全领域的重要课题，NTT-LSU架构的设计思路，为我国自主研发高性能、低功耗的后量子安全芯片提供了宝贵参考，我们可以沿着这一新型紧耦合思路，探索更多密码算法与处理器架构深度融合的方式。

**点评专家：明经典 副教授 硕导**

**专家单位：南京理工大学**

**原文标题：NTT-LSU: Tightly Coupled Architecture for Efficient NTT Implementation on RISC-V Processor**

**原文作者：Zhao, Yinqiao and Xie, Zilong and Zhan, Ruidian and Xiong, Xiaoming and Chen, Yun and Cai, Shuting**

**期刊/会议：IEEE TCAD 2026**

DOI：10.1109/TCAD.2025.3627145

版权与来源声明：本文依据《中华人民共和国著作权法》第二十四条之规定，为介绍、评选之目的，在此适当引用。原文版权归原作者所有。

![图片](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8yDJWicSECDq8dgel7DctAMAnNheJf2kkfQOiaFMdZaWNIDt9IxOkEhI5TJar4wnyAiba9twTOxeKZg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&randomid=qnylxjok&tp=webp#imgIndex=2)

**信息网络安全**

《信息网络安全》创刊于2001年，是由公安部主管，公安部第三研究所、中国计算机学会主办，面向国内外公开发行的国内首批信息安全类期刊之一，于2015年成为中国科技核心期刊，2017年成为中国科学引文数据库来源期刊，2018年成为中文核心期刊，2022年入选CCF计算领域高质量科技期刊分级目录。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsN9e1fkuM1ibgD3PcZiaqJrZia7KQWDwichD8lvo4RqfPcNkuyqje45IOXD0HocBDntaDdK4tibWoTIs5Ww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&randomid=fbknkhlb&tp=webp#imgIndex=3)

中文核心期刊

中国科技核心期刊

中国科学引文数据库来源期刊

CCF计算领域高质量科技期刊

![图片](https://mmbiz.qpic.cn/mmbiz_png/v4vz52CcB12BRNZGqdRDIBsUQ6WickDoUNkuVicKXooNbRSzdGDGuJtxJodlbpr1B07yAReAz5V5jj47Yaq7ujRw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&randomid=23elspay&tp=webp#imgIndex=4)

我们在不断努力和完善中，期待您的关注和支持！

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsNibBlGIDAuhv04Ap5j7X2I4Se7j2nvibDibXXmaA8WJqgXZ2Lh8sShG6jas26z3WlRcANNqZnr3nMTnQ/0?wx_fmt=png)

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