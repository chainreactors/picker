---
title: ACM CCS 2025论文解读 | CPU Fuzzing的下一站不是更随机，而是更懂语义：从DiveFuzz看RISC-V验证的反馈升级
url: https://mp.weixin.qq.com/s/DLyBJlE43DI6v9G7X6ZSgQ
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:01:59.765403
---

# ACM CCS 2025论文解读 | CPU Fuzzing的下一站不是更随机，而是更懂语义：从DiveFuzz看RISC-V验证的反馈升级

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FNlvhjUaDTMZvjk3jZ7xhGVUG47BYvLLgeJGnG2hibNKBwzsE305k5Pgxq3rp8ovHIH5n4TomwDzaIybmfgBYlU6xArmbnSl10MPflZspTkg/0?wx_fmt=jpeg)

# ACM CCS 2025论文解读 | CPU Fuzzing的下一站不是更随机，而是更懂语义：从DiveFuzz看RISC-V验证的反馈升级

原创

何家骥；蔡军锋
何家骥；蔡军锋

信息网络安全杂志

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FNlvhjUaDTNhG7mrR0wntCd7xNAm2opibIKYSFUGHZR1BpJ6MS2xS8c4cVYFk3ZqqtmMUk5dwua1ic841kANGXtSBEs1SM1MPaicTSrjib711AA/640?wx_fmt=png&from=appmsg)

**引子**

RISC-V架构的开放特性让处理器验证有了大规模“白盒试验场”，也让一个关键问题浮出水面：当我们说CPU Fuzzing“覆盖得更多”时，到底覆盖的是代码结构，还是漏洞真正藏身的微架构状态？CPU漏洞往往不是简单崩溃，而是指令序列、操作数和流水线状态共同作用后的错误写回、权限绕过或异常偏差。因此，CPU Fuzzing的瓶颈不只是生成更多指令，而是生成更能触达关键语义状态的指令。DifuzzRTL、Cascade到DiveFuzz这条线，正体现了将语义多样性融入测试用例生成的趋势。

![](https://mmbiz.qpic.cn/mmbiz_png/FNlvhjUaDTMibLJ9EWJyfCEGFngmU7hjyCPx37Ijx2ibvmGz8mH3KWXzsEdaUSFDryqRn8jgKwAVu5iamnf0AN1xnqxDh62OZujia2Oqxf5ASzs/640?wx_fmt=png&from=appmsg)

**论文速览**

《DiveFuzz: Enhancing CPU Fuzzing via Diverse Instruction Construction》由中国科学院信息工程研究所科研团队发表于CCS 2025，面向RISC-V CPU差分模糊测试。发表于S&P 2021的DifuzzRTL用控制寄存器覆盖率开启硬件fuzzing的差分测试范式，发表于USENIX 2024的Cascade通过复杂长程序提升内部状态触达能力；但二者仍会生成大量“看似不同、实际写回数据高度重复”的测试。DiveFuzz把操作数构造推迟到运行时：与ISA模拟器交互，依据寄存器、内存上下文补全操作数，用Shift-XOR记录对顺序敏感的操作数组合，并用最近读写寄存器队列增强数据依赖；并通过操作码分布再平衡，规避已知漏洞和误报。实验显示，在香山、CVA6、Rocket、NutShell上，DiveFuzz达到同等覆盖平均比DifuzzRTL快204倍、比Cascade快114倍，发现26个新漏洞，其中15个获得CVE。

![](https://mmbiz.qpic.cn/mmbiz_png/FNlvhjUaDTOy9jp72jbeSxmULcjJZZyiaaYbF9XKibAciaMgykvaetETta2djjxsm1exCFs3Rk7jK4MGuCuicZsVPziarjbsh2oIdAqFIEI8AeG4/640?wx_fmt=png&from=appmsg)

**深度解剖**

DiveFuzz的重要性，不仅在于刷新了覆盖率数字，更在于它重新校准了CPU Fuzzing中多样性的含义。DifuzzRTL证明了“覆盖率引导+差分测试”可以在真实CPU RTL中挖出漏洞，但其反馈主要落在控制寄存器等结构层面；Cascade则指出短程序难以激发复杂微架构行为，因此通过长程序和交织的数据流、控制流提升状态触达能力。二者分别回答了“如何引导测试”和“如何构造复杂程序”的问题。

DiveFuzz进一步追问：程序看起来复杂，是否真的产生了足够不同的执行结果？论文观察到，现有fuzzer生成的指令流存在大量写回数据重复，操作码分布也不均衡。这意味着测试表面上不断运行新输入，实际上可能反复经过相似状态。DiveFuzz因此把关注点落到操作数内部值和写回数据上：同一条除法、浮点或CSR相关指令，只要操作数和上下文不同，就可能触发完全不同的舍入、异常、权限检查或边界行为。

因此，相比Cascade，DiveFuzz不只是让程序更长，而是让每条指令携带更高的状态区分度；相比DifuzzRTL，它也不只是追求覆盖率增长，而是试图提高覆盖背后的有效状态变化。它的分水岭意义在于：CPU fuzzing的下一步提升，可能不在于扩大随机空间，而在于更细地理解“什么样的指令变化真的改变了处理器状态”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FNlvhjUaDTOndKFKdmJ9cjdtAS5EGRuJKMDpCQQk15XWicMRWlVkXqc7GtuB2rmGSRIBtdzOgkpY2b8kGVA6o63yapH00H2whGUzbXhgxEyk/640?wx_fmt=png&from=appmsg)

**局限与展望**

当然，DiveFuzz的“语义”仍主要通过写回数据和操作数内部值来刻画。对于缓存一致性、瞬态执行、多核交互、侧信道等更深层的微架构行为，写回数据未必总能充分反映关键状态变化。论文自己也提到，未来可以将抽象写回数据形式化为新的覆盖指标，以丰富CPU fuzzing的反馈体系。沿着这个方向，后续工作值得进一步思考：除了写回值，哪些运行时上下文最能代表漏洞触发条件？能否让fuzzer从“发现重复”进一步走向“理解重复为何无效”？

![](https://mmbiz.qpic.cn/mmbiz_png/FNlvhjUaDTOuF5LEHEQKonkSIZhwuicYYyqQWQeh00drJk573LhKEpOo18RrpNOYLlcSr81kVhicIlrTkjvyuibafToCpMeKsFN7S5rDEnWnME/640?wx_fmt=png&from=appmsg)

**启示**

对国内同行而言，DiveFuzz的启示不是“再做一个更复杂的fuzzer”，而是重新审视反馈信号的质量。RISC-V开源生态给了我们观察RTL、ISA模拟器和运行轨迹之间关系的机会，香山、NutShell等平台也提供了难得的真实对象。真正值得投入的，可能是把测试生成从“形式合法”推进到“状态有效”：让每一次变异都更可能触达新的执行语义。CPU Fuzzing的关键，正在从生成更多程序，转向生成更有利用价值的程序。

**本文仅代表作者个人观点**

![](https://mmbiz.qpic.cn/mmbiz_png/FNlvhjUaDTOHUO1q5She4mbEiaDeFm2kXzrOPb89NbyHzq8EAzjgCWMy6M9uwa4TzWBsLiav9R0ibN2UROpEvzBxO8sDGlZgWnCPM2YXuErMAA/640?wx_fmt=png&from=appmsg)

**本期点评论文**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FNlvhjUaDTOXzibTAicianhvgiaxdR14GhvROqBSjQCnRBb8ua2dr8vZOr6wiarNzZMZU4EoyNI6zWyVyga05NuiaicLh7AjheqJtIjAkO7MNCIb2Y/640?wx_fmt=png&from=appmsg)

**推荐人：**

何家骥（天津大学教授，处理器漏洞挖掘、密码芯片设计与安全分析）

蔡军锋（天津大学博士生，处理器漏洞挖掘）

**原文标题：**DiveFuzz: Enhancing CPU Fuzzing via Diverse Instruction Construction

**原文作者：**Zihui Guo, Miaomiao Yuan, YangiYang, et al.

**期刊/会议：**ACM CCS 2025

DOI：https://doi.org/10.1145/3719027.3765167

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