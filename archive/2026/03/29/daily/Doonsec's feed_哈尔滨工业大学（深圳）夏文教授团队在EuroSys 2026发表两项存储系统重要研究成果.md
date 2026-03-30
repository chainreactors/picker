---
title: 哈尔滨工业大学（深圳）夏文教授团队在EuroSys 2026发表两项存储系统重要研究成果
url: https://mp.weixin.qq.com/s/Z2AyLqZSt87ysyueGZEzMg
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:40:37.041773
---

# 哈尔滨工业大学（深圳）夏文教授团队在EuroSys 2026发表两项存储系统重要研究成果

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FNlvhjUaDTPqkZicAiac0lVf7Nibsst06A24KiapRQbPApyPYhfqUnibq7RQ3qq69p1FOQVtuUdic6OdlFAMZIsPaykzrUdCLoJvnickKnuSqHtJKE/0?wx_fmt=jpeg)

# 哈尔滨工业大学（深圳）夏文教授团队在EuroSys 2026发表两项存储系统重要研究成果

信息网络安全杂志

![]()

在小说阅读器中沉浸阅读

哈尔滨工业大学（深圳）夏文教授团队在计算机系统领域顶级会议EuroSys 2026（CCF-A类）上发表两项重要研究成果，分别针对非易失性内存文件系统性能优化和高效差量压缩技术提出创新性解决方案，显著提升了存储系统的性能与效率。

**成果一：提出****“****机会主义消序****”****机制，构建高性能非易失性内存文件系统****ChimeraFS**

崩溃一致性是文件系统稳定性的基石，但其对存储操作顺序的严格要求严重限制了I/O并行度，尤其是在能直接访问硬件的非易失性内存文件系统中，顺序保障操作导致的缓存刷写与等待极大降低了系统性能。

团队提出了一种机会主义消序的新型I/O机制，该机制充分发挥持久性内存的I/O并行优势。该机制的核心设计是：利用快速校验和计算消除元数据和数据写入之间的顺序性，将校验和计算、元数据I/O与并行数据写入操作并行执行。为实现该机制，团队设计了以下三个模块：（1）消序控制器，对不同I/O模式自适应地进行I/O消序和并行化处理，确保并行化的实际收益。（2）拓扑感知的I/O调度器，高效调度数据与元数据I/O，最小化硬件I/O竞争。（3）轻量化恢复校验器，显著降低恢复过程中的校验和计算开销。实验表明，该机制充分释放PM的I/O并行能力，性能领先于其他先进的PM文件系统。基于机会主义消序机制，团队构建了面向新型非易失内存的ChimeraFS文件系统。

图一展示了不同文件系统在不同I/O大小、I/O模式以及并行度下的性能，实验结果表明ChimeraFS取得了总体最好的性能，在所有负载中，性能都优于另一PM上的数据写入并行化文件系统OdinFS。ChimeraFS在4KiB和32KiB写入中，高并发场景（超过8线程）下分别比其他文件系统性能提升1.99×至10.13×和1.19×到5.77×。该成果已发表于领域顶级会议Proceedings of the Twenty-First European Conference on Computer Systems（EuroSys ’26，CCF-A）。

![](https://mmbiz.qpic.cn/mmbiz_png/iaKL0GKANXgMYEzIgln6hpFRBnHrIIU0ETSnaMNtug5d8b9FB37tAY4TuRL03JbUIOfallq995rbh4UcRaQEOaYZYK574kU5ick0ZWLhaiaeVA/640?wx_fmt=png&from=appmsg)

图1 文件系统并行I/O性能

**成果二：提出****FastDelta****框架，实现****“****一次滚动哈希，全程多次复用****”****，突破差量压缩性能瓶颈**

在数据备份存储领域，差量压缩能实现极高的数据缩减率，但巨大的计算开销严重制约了备份吞吐。传统方法在内容感知分块、相似性检测和差量编码三个阶段需独立重复计算耗时的滚动哈希，存在严重的计算冗余。

针对这一根本性瓶颈，团队提出了名为FastDelta的高效差量压缩框架。其核心创新在于“一次滚动哈希，全程多次复用”。首先，在内容感知分块阶段仅计算一次滚动哈希，并通过内容感知采样策略稀疏记录哈希值，供后续阶段直接复用，彻底消除了相似性检测与编码中的逐字节哈希计算，获得数倍计算速度提升。其次，该基于内容的采样方法相比定长采样，有效克服了“边界漂移”问题，在减少内存开销的同时保证了算法精度与稳定性。最后，通过将采样逻辑嵌入分块过程，并结合局部性感知与捎带式I/O优化，实现了低开销的元数据管理与压缩。

图二、图三分别展示了不同差量压缩框架的备份吞吐和去重压缩率，FastDelta 在保持极高压缩率的同时，将备份速度提升至接近传统分块去重的水平，相比现有差量系统提升约1.3×-2.1×，有效解决了长期以来差量压缩“高压缩比、低吞吐量”的权衡难题。

![](https://mmbiz.qpic.cn/mmbiz_png/iaKL0GKANXgNicYaR1fPUmWk5620NJr0vFW2FJm4G5W54KppqwC0MFlPF0RbHq9nRLs2aA3ulZAwoue9llf6qiaoIlKet8qTVmGQthOSo2VnTM/640?wx_fmt=png&from=appmsg)

图2 备份系统吞吐速度

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaKL0GKANXgMPqOKoNQyLmAKTRmySNTJmqlroopapSBPXkicAY9TE6atRCyFOm9icHlVmgrvkyrs4Nm2OTAPzJLESqhanpgCfCgvOoYfNtdNao/640?wx_fmt=png&from=appmsg)

图3 去重压缩率

哈尔滨工业大学（深圳）夏文教授团队立足国家战略需求和学术前沿，长期从事存储系统、操作系统、云存储、去重压缩、系统安全等领域研究，近年来主要研究成果发表在OSDI、FAST、USENIX ATC、ASPLOS、EuroSys等国际顶级会议，荣获省部级一等奖两项，促进了国家计算机系统与计算机存储学科的发展。

来源：哈尔滨工业大学（深圳）网络空间安全研究院

推荐阅读

[保研、毕业答辩、评奖学金都能用！部分高校网安学院开始“认”开源贡献了](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247515175&idx=1&sn=6485d82b0140ac3b34276820533d0855&scene=21#wechat_redirect)

[AI查重系统频“误判”，学生何时能自证清白？中山大学、东南大学网安学者揭露检测系统技术困局与出路](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247514984&idx=1&sn=0dd459f54976d8c7d16c462a796aae7c&scene=21#wechat_redirect)

[用AI“写”论文算作弊吗？中山大学、东南大学、兰州大学网安学院导师拆解“真创新”](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247514957&idx=1&sn=34ed3abd735a4f0743cf4ad5ccc9cf04&scene=21#wechat_redirect)

[让论文“跑”起来！如何用开源项目“喂”出实战型网安人才？华中科技大学、西安电子科技大学、重庆邮电大学联手揭秘](https://mp.weixin.qq.com/s?__biz=Mzg3NjU0Nzg1Nw==&mid=2247515125&idx=1&sn=d27ca6c3e262ed1286ed316789009a8c&scene=21#wechat_redirect)

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

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsNibBlGIDAuhv04Ap5j7X2I4Se7j2nvibDibXXmaA8WJqgXZ2Lh8sShG6jas26z3WlRcANNqZnr3nMTnQ/0?wx_fmt=png)

信息网络安全杂志

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