---
title: 哈尔滨工业大学（深圳）与中国科学技术大学合作完成：首个完全在FPGA硬件内实现自举密钥展开的独立TFHE全同态加密加速方案
url: https://mp.weixin.qq.com/s/7WFjUrJDoLdvxIiuqc6Muw
source: Doonsec's feed
date: 2026-06-25
fetch_date: 2026-06-26T06:05:59.241722
---

# 哈尔滨工业大学（深圳）与中国科学技术大学合作完成：首个完全在FPGA硬件内实现自举密钥展开的独立TFHE全同态加密加速方案

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FNlvhjUaDTMibn6DTqN5DK3icPLNfoiahTJ19NanHSjSNQI4scrlrArJsianr7OaWv46hHXviczOicHicia91sYzHASaMtFttC3HXRQnLtmYcpicI72o/0?wx_fmt=jpeg)

# 哈尔滨工业大学（深圳）与中国科学技术大学合作完成：首个完全在FPGA硬件内实现自举密钥展开的独立TFHE全同态加密加速方案

原创

边松
边松

信息网络安全杂志

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**引子**

全同态加密被誉为密码学的“圣杯”。通俗地说，它就像一种神奇的“锁箱计算”：你可以把敏感数据锁进箱子交给第三方处理，对方无需打开箱子就能完成计算并返回结果，数据在整个过程中始终处于加密状态。这意味着企业可以放心地将隐私数据外包给云端，而无需担心泄露风险。然而，这种“魔法”的代价是极高的计算开销——其中“自举”操作如同不断给疲惫的计算过程“充电”，虽然能保证计算持续进行，却也成为系统中最耗时的环节，单次操作往往占据毫秒甚至分钟级时间，严重制约了实际部署。

**论文速览**

现有FPGA硬件加速方案面临“开发效率-性能”的两难：高层次综合（HLS）开发周期短但资源开销大；寄存器传输级（RTL）优化精细却难以充分挖掘并行性，且多数方案依赖外部处理器协同调度，系统复杂度高。哈尔滨工业大学（深圳）集成电路学院与中国科学技术大学网络空间安全学院合作的文章“YAXY: A New Hybrid FPGA-based Hardware Acceleration of TFHE”提出了一种HLS与RTL协同优化的混合加速方案YAXY。该方案在HLS层面通过参数化自举密钥展开技术，将迭代次数成倍缩减，并配合流水线数据调度实现片内外数据无缝衔接；在RTL层面设计层次化流水线架构，并采用统一的蒙哥马利模乘器与数论变换（NTT）加速核心运算。经实测验证，该方案在Xilinx ZCU102平台上以300MHz频率运行，单比特密文自举延迟仅为0.44ms，是目前独立FPGA实现中的最低延迟。与现有方案相比，其在频率归一化后的速度与资源权衡指标上表现最优。

**深度剖析**

全同态加密的硬件加速是制约其工程化应用的核心瓶颈之一。作为首个完全在FPGA硬件内实现自举密钥展开的独立加速方案，YAXY加速器针对现有FPGA方案在开发效率与性能之间的权衡难题，技术特点较为鲜明：在算法层面，通过参数化自举密钥展开技术减少迭代次数，并配合流水线调度实现片内外数据衔接；在电路层面，采用层次化流水线与统一的蒙哥马利模乘器、NTT运算单元，完成了无需外部协处理器的独立加速。这种架构对于简化系统集成、降低部署门槛具有实际价值。

从实测结果看，该方案在频率归一化后的速度与资源权衡上表现较优，且能在中等规模FPGA上达到当前独立实现中的较低延迟。对于隐私计算在边缘侧等场景的落地，该工作提供了可借鉴的硬件实现路径。

**点评专家：边松（****北京航空航天大学****）**

原文标题：YAXY: A New Hybrid FPGA-based Hardware Acceleration of TFHE

**原文作者：Yangfu Xu, Aijiao Cui, Xiangyu Guo and Yier Jin**

哈尔滨工业大学（深圳）集成电路学院：徐阳夫，崔爱娇（教授），郭想宇

中国科学技术大学网络空间安全学院：金意儿（教授）

**期刊/会议：IEEE Transactions on Emerging Topics in Computing**

**DOI：h**ttps://doi.org/10.1109/TETC.2026.3691777

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