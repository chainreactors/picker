---
title: RoKoko：在后量子框架下同时达成线性时间证明者、多对数级通信复杂度、多对数级验证者复杂度，验证速度提升100倍
url: https://mp.weixin.qq.com/s/Jw6wTJe_yca-WDlxI3j8VA
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:30:29.167362
---

# RoKoko：在后量子框架下同时达成线性时间证明者、多对数级通信复杂度、多对数级验证者复杂度，验证速度提升100倍

# RoKoko：在后量子框架下同时达成线性时间证明者、多对数级通信复杂度、多对数级验证者复杂度，验证速度提升100倍

原创

张乐友
张乐友

信息网络安全杂志

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

（一）引子

2024年8月，NIST正式发布首批后量子密码标准，ML-KEM（基于模格的密钥封装机制）和ML-DSA（基于模格的数字签名）进入标准化轨道。与此同时，一个更深层的问题摆在学界与工业界面前：后量子零知识证明距离实用还有多远？

传统的高效零知识证明系统多依赖双线性配对，其安全性无法抵御量子计算机的威胁。而可以抵御量子计算机的基于格的后量子零知识证明，又长期被一个顽固瓶颈所困：安全参数翻倍，证明体积扩大四倍，验证时间急剧上升，远不具备工程落地的条件。

2025年底，RoK and Roll首次打破了这个二次方壁垒，将后量子SNARK的通信复杂度压缩至接近线性。而2026年3月，由Klooss等五位作者发布的RoKoko，在此基础上又迈出了决定性的一步——不仅在渐近意义上再度优化了一个对数因子，更在工程实测中交出了令人信服的成绩单：验证速度提升100倍、证明体积约200KB、证明者运行时间与当前最优方案持平。

RoKoko所解决的核心问题，是如何在不依赖可信设置和不引入量子脆弱假设的前提下，同时实现：线性时间证明者、多对数级通信复杂度、多对数级验证者复杂度。这三个目标在后量子框架下同时达成，此前尚无先例。

（二）论文速览

论文的技术起点是此前作者团队的系列工作：RoK, Paper, SISsors于2024年提供了格基简洁证明的基础工具箱；RoK and Roll在2025年首次实现了O(λ·polylog)规模的后量子SNARK，其中λ为安全参数。RoKoko的核心贡献，是引入一种名为committed refinement的框架，系统性地将上述方案中残余的一个*Θ(logλ)*因子从通信量中消除。

RoKoko采用递归分折范式：证明者将见证拆分为ρ份子见证，发送对应的交叉项，再由验证者提供随机挑战，将子见证折叠为规模缩减ρ倍的新见证，如此递归，直至见证规模降至可直接发送的量级。RoKoko的关键创新在于：在每轮折叠中附上对折叠正确性的格基承诺，从而将验证者对随机投影约束的逐轮核验转化为对承诺的统一检查，从根本上消除验证时间与递归深度之间的线性依赖关系。

相较当前最优的格基多项式承诺方案Greyhoun，RoKoko在验证时间上实现约100倍加速，证明者运行时间相近，证明体积约200KB，具有显著竞争力。

（三）深度剖析

众所周知，在区块链、分布式系统等场景中，验证者往往是资源受限的节点。而验证时间的压缩，直接决定了证明系统能否在这些受限环境中实际部署。Greyhound此前的验证时间已是格基方案中的优秀水平，RoKoko在此之上再压缩两个数量级，意味着原本需要数秒的链上验证，现在可在毫秒级完成，这是从原型系统到生产级部署的关键跨越。

同时，RoKoko的安全性建立在Module-SIS和Module-LWE这两个目前最受信任的后量子困难假设之上，无需可信设置，验证过程完全透明。相比之下，主流非后量子SNARK依赖椭圆曲线配对，一旦大规模量子计算机出现即告破防。RoKoko所代表的格基路线，是目前学界公认最具长期安全保障的证明系统技术路径之一。

值得注意的是，本文出现的时间节点恰好处于后量子证明系统从理论竞赛阶段向工程可行性验证阶段过渡的关键窗口。IACR新闻页面将格基简洁论证列为当前最活跃的研究前沿之一，RoKoko的发布，标志着这一方向的工程成熟度已达到可认真评估部署路线图的阶段。

（四）局限与展望

RoKoko也并非完美无缺。第一，200KB的证明体积，相较成熟的配对基SNARK（如Groth16约200字节）仍有三个数量级的差距；在证明体积极度敏感的场景中，短期内难以直接替代。第二，线性时间证明者虽是理论上的优秀指标，但实际工程中证明者的绝对运行时间对于需要亚秒级响应的实时应用仍有挑战。第三，对R1CS的支持尚处于理论完备但工程优化不足的阶段，距离对接Circom、Noir等主流电路编译器还需系统性适配工作。

RoKoko开辟的committed refinement范式有望成为后续工作的标准起点。可以预见的研究方向包括：与基于哈希的STARK证明系统的递归组合，以实现更灵活的可组合证明链；在后量子匿名凭证、隐私保护数据核查等应用场景中的工程实例化；以及进一步将证明体积压缩至10KB以内的理论探索。

对于关注密码学与公共安全交叉应用的读者，这一进展的意义不应被低估。可验证计算、隐私保护的合规核查、跨机构数据主权认证——这些场景共同依赖的技术底座，正是高效、透明、后量子安全的证明系统。RoKoko所代表的方向，是密码基础设施在量子时代保持安全可用的关键保障之一。这不是遥远的未来，而是正在成形的现实。

**点评专家**：张乐友  教授

**研究方向：**匿名加密、区块链隐私保护

**专家单位：**西安电子科技大学

**原文标题：**RoKoko: Lattice-based Succinct Arguments, a Committed Refinement

**原文作者**：Michael Klooss,Russell W. F. Lai,Ngoc Khanh Nguyen,Michał Osadnik,Lorenzo Tucci

**DOI**：https://ia.cr/2026/575

版权与来源声明：本文依据《中华人民共和国著作权法》第二十四条之规定，为介绍、评选之目的，在此适当引用。原文版权归原作者所有。

推荐阅读：

[CRYPTO 2025：面向NP的自适应安全SNARG](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247516531&idx=1&sn=0b751c1e0eaeaa94798a9f64ba5912f9&scene=21#wechat_redirect)

[PKC 2026 ：标准模型下可复用的恶意安全HSS方案](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247516530&idx=1&sn=1379b3952ab3928d6f22321afd5e9010&scene=21#wechat_redirect)

[当数学遇见工程：后量子密码的实现和挑战](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247516492&idx=1&sn=aa4e92d3a1319076e972e6e861f7f46d&scene=21#wechat_redirect)

[哈尔滨工业大学（深圳）与中国科学技术大学合作完成：首个完全在FPGA硬件内实现自举密钥展开的独立TFHE全同态加密加速方案](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247516297&idx=1&sn=b30e41113ea34afbfa8e45293840bdbe&scene=21#wechat_redirect)

[密码领域顶会CRYPTO 2025 | 高效并行性与灵活函数表达能力兼得，全同态加密向前一步](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247516548&idx=1&sn=0fc77d905d300396b03c23379fdbea7e&scene=21#wechat_redirect)

[密码领域顶会Eurocrypt 2026 | 全同态加密领域中国团队（华东师范大学、北京航空航天大学）最新进展](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247516547&idx=1&sn=d8230ed3642e62d79c4a545900f4d274&scene=21#wechat_redirect)

[HOST 2025 | 从“密钥恢复”到“物理层数据重建”：基于三维功耗曲面的AI芯片隐私泄露分析](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247516550&idx=1&sn=13918edb12fa6529c2872d4a19601fdf&scene=21#wechat_redirect)

[Cryptography 2025  | 抗量子密码时代，基于深度学习的芯片侧信道高效评估机制](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247516551&idx=1&sn=56ed7ce5953c805ca9edff780db8c13f&scene=21#wechat_redirect)

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