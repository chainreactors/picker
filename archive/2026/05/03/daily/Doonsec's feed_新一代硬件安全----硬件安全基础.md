---
title: 新一代硬件安全----硬件安全基础
url: https://mp.weixin.qq.com/s/_l3Fo94d3yXlUL71r7w2Ww
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:28:15.355631
---

# 新一代硬件安全----硬件安全基础

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaApbiaTeydYCIEaPpjmsGKBtWE8KJ14x1daE1uH52r89gQD8p0laMyqXJdQibbvtdibhxe02AppO36Jia7nkcb7P6t2YVLqiajdic5Uc/0?wx_fmt=jpeg)

# 新一代硬件安全----硬件安全基础

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

**1.1硬件安全基础**

在当今这个信息技术无所不在且高度互联的时代，网络安全正变得越来越具有挑战性。例如，随着物联网(IoT) 的兴起，大多数此类设备都会通过某种方式接入互联网，通常普通用户也难以理解其背后的机理。正如图 1.1中所描述的历年来发生在现实世界中的海量攻击所示，这事实上扩大了攻击面，并会导致严重的后果。在网络安全的领域中，硬件安全着重关注直接通过底层的电子器件来实现安全和信任。例如，研究人员曾提醒人们注意针对现代处理器的推测性执行的严重攻击[Koc+19a, Lip+18a]，抑或剖析了加密硬件模块的侧信道泄漏问题[Ler+18]。再比如，在许多商用计算机和其他定制设备中，都使用了所谓的信任根(RoT)技术，用于计算的隔离和证明[Mae+18, Zha+19, Nab+20]。

接下来，我们将讨论硬件安全的基本方面并对所选现有技术进行回顾，在本专著的其余章节中，这些内容将被认定为常识。

应该理解的是，本章仅能对此广阔且飞速发展的领域提供一个概述，但我们会聚焦于其中重要的技术方面和最具开创性的保护方案，使得读者可掌握必要的背景知识，以理解本专著。

**1.1.1 运行时数据安全**

电子产品中数据处理的保密性、完整性和可用性会受到各种威胁的影响，诸如(1)对数据的未经授权的访问或修改，(2)利用侧信道、故障注入、物理读取或探测的攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicj2hdhvV3RLPKqjX9Lb2ibHLs792M5icaSnjBZtlhPjyy5ThWzq3QgahuU5oSiciblHD1dFQhz6V7Y3Q/640?wx_fmt=png&from=appmsg)

图1.1 现代的硬件设备部署在我们周边，且与互联网连接，但通常缺乏内置的安全概念和措施。因此，在给人们的日常生活带来了大量的安全风险。本图摘自[Gra16]。

**1.1.1.1 对数据未经授权的访问或修改**

试图窃取或破坏数据的常规攻击主要在软件层面和互连系统上实施。对此，密码学代表了一种普遍适用的保护方案，但如下所示，也有许多专用的、以硬件为中心的安全保护特性：

* 用于可信执行的隔离飞地 (TEEs), 诸如工业界中的ARM TrustZone、Intel SGX，学术界的MIT Sanctum解决方案 (参见Fig. 1.2; 关于每种TEE的更多背景，请参见[Mae+18])
* 用于监视和交叉检查不受信任的第三方知识产权（IP）模块的包装器[Bas+17]
* 用于系统设计安全的集中式知识产权保护（IP）基础设施 [Wan+15b]
* 计算验证 [Wah+16]
* 安全的任务调度 [Liu+14]
* 安全的片上网络 (NoC) 架构 [Fio+08]等。

然而，如果缺乏精心的设计和实现，上述安全特性本身也容易遭受针对硬件的攻击。具体而言，可参考章节[BCO04, Bay+16,Qiu+19, OD19, CH17]，其中对此类攻击进行了更加详细的讨论。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicj2hdhvV3RLPKqjX9Lb2ibHVIfMAEBOj1iavuCyhCQqmVPQ1Zib2tnOicZLhGEYqlMk8cxO4x9f2qxPA/640?wx_fmt=png&from=appmsg)

Fig. 1.2 用于可信执行的隔离飞地是典型的以硬件为中心的安全特性。图中所示分别为 (a)Intel SGX，(b)MIT Sanctum和©ARM TrustZone的高级架构。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicj2hdhvV3RLPKqjX9Lb2ibHrjXbicw0hGn1S9J1ZliaXZZnwnOHBx4Ku09aAibuuOt42Hljy9DBibTp8Q/640?wx_fmt=png&from=appmsg)

Fig. 1.3 波动差分逻辑( WDDL）可用于缓解功耗侧信道攻击。这是通过冗余的差分组合逻辑路径实现的，这些路径针对任何操作都实施反向切换，从而掩盖了特定状态转移的功耗差异。此外，预充电逻辑也被用来降低切换期间的峰值功耗。本图摘自[Fuj+14]。

**1.1.1.2 侧信道与故障注入攻击**

由于底层电子器件的敏感性和脆弱性，侧信道攻击可利用物理信道的泄露推断出相关信息[ZF05]。例如，众所周知，当硬件实现未采取保护措施时，高级加密标准 (AES) 易遭受基于功耗的侧信道攻击[BCO04, OD19, SW12]。

另外一个例子事关信息的泄露，与现代处理器中的定时行为，或者基于高速缓存与缓冲区的推测执行特性有关[OST05, Lip+18a, Sch+19]。

大多数针对侧信道攻击的安全对策都采用了某种隐身或屏蔽技术。这涉及到对于通过侧信道泄露的信息扩散的控制。

具体可通过各种手段实现，包括从整系统级[GMK16]到单个门电路[Bel+18]的解决方案，另见图1.3的例子。然而，此类对策的韧性仍取决于其整体上的物理实现。例如，Fujimoto等人[Fuj+14]已证明，即使先进的WDDL方案也会遭受布局上的微弱不对称的影响，使得攻击者最终可推导出密钥。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicj2hdhvV3RLPKqjX9Lb2ibH8X4A6GNbVXx2fLkbtx9RahlTtQf1nj2n063w0VtGicZyh7eKJ2WUlNA/640?wx_fmt=png&from=appmsg)

Fig. 1.4 针对AES算法的多阶段攻击。首先，一个随机但持续的故障被注入到S-box中，以使随后的加密出现偏差。随后，通过对足够多的密文进行采样，该偏差可帮助推断出密钥。本图摘自 [Pan+19]。

故障注入攻击会引发故障以推断出敏感信息。因此，参见图1.4的例子，故障注入也用于支撑或推进其他攻击。故障注入攻击。

包括(1) 直接、侵入式的故障注入，比如通过激光[SHS16] 或电磁波 [CH17, Bay+16, Deh+12],以及 (2) 间接的故障注入，例如，通过对特定的内存位置的重复写入[Vee+16]或通过故意 "滥用 "动态电压和频率缩放(DVFS)功能[Qiu+19]。

安全对策包括对运行时故障的检测、在设计与制造阶段采取针对故障注入的加固措施[Kar+18b, LM06,Dut+18]。请注意，区分自然产生的故障和人为恶意制造的故障并非易事，这给运行时的恢复带来了实际的挑战。

**1.1.1.3 物理读取与探测攻击**

攻击者如果能够接触到电子器件并利用传统的故障分析或检测手段实施入侵，比如光电探测或聚焦离子束铣削工具[Pri+17a]，则可发动相当有力的读出攻击。其中，这些攻击包括：

（1）通过金属层或基板背面探测晶体管和导线 [Wan+17a, Hel+13]

（2）监测由CMOS晶体管开关引起的光子发射[Taj+17, Kra+21]

（3）监测存储器中的电荷 [CSW16]

如果仔细应用，这些攻击可以揭示器件内部所有的信号。比如，图1.5 展示了光电探测技术的概念和示例，允许推断各个器件运行时的比特位数据。

安全对策旨在检测或阻止攻击者的物理访问。先前的解决方案试图在后道工序(BEOL) [Wan+19, Lee+19, YPK16] 中放置屏蔽结构，在基板中放置偏转或加扰结构 [She+18]（另请参见图 1.6 )以及检测器电路 [Wei+18]。诸如[ISW03]等早期研究也考虑了正规的安全技术。然而，这种方案受制于对攻击者能力的假设，随着时间的推移，这些限制可能会变得过时，从而使这些正规的保证措施失效。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicj2hdhvV3RLPKqjX9Lb2ibHXTVDvBNXicLw1D1R11Hyib1APQ3MVNQHWm711rNSoM1k8pB7AGvyskaA/640?wx_fmt=png&from=appmsg)

Fig. 1.5 激光电压探测的概念(a)和例子(b)，其作用是在读取器件运行时的比特数据。在例子(b)中正在展现的是一组寄存器, 其中暗的单元存储的是比特“0”，亮的单元存储的是比特“0”。子图(a)摘自[Loh+16]，(b)来自由Shahin Tajik提供的相关显微图像。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicj2hdhvV3RLPKqjX9Lb2ibHeO3TliacZv1ghyjESbiaF8Ub78sjXBCt92sCJ1aib9HzR5BbxsMGjEPVA/640?wx_fmt=png&from=appmsg)

Fig. 1.6 硅基板中金字塔结构的概念，比如，可通过专用的蚀刻步骤实现。结果导致入射激光的反射光线被散射和混合，使得更加难以清晰地读出数据。摘自 [She+18]。

来源：芯事芯语

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAgXyLqfnkPJhyibCoBSOMGSsdQ03SEf01kcUbPAEzhf5nb6vyvYWINevstJCARUgy8qNpTa2lKVo7g7RPFm8IicY9aYtviaowaTE/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247557132&idx=2&sn=2e44d4c2d77a2eec377d0553442d2c1b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561775&idx=1&sn=948a9e7f8d4fbed363c6a6a5479cd39e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkfxA4GZice84BsCR4zGV0oqJXpEjUsUpGKcFcCx1BiaDYDQU4cT3nTtpA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561260&idx=2&sn=0ca6395502487515a921f32288b7e8df&scene=21#wechat_redirect)

**专业社群**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJnASqAJY7fLYIeMGl8fHu4aPXusCVuX2qAYkrb9bQMRGEBvSghHETaQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&scene=21#wechat_redirect)

**部分入群专家来自：**

**新势力车企：**

特斯拉、理想、极氪、小米、零跑汽车、阿维塔汽车、智己汽车、小鹏、岚图汽车、蔚来汽车、吉祥汽车、赛力斯......

**外资传统主流车企代表:**

大众中国、大众酷翼、奥迪汽车、宝马、福特、戴姆勒-奔驰、通用、保时捷、沃尔沃、现代汽车、日产汽车、捷豹路虎、斯堪尼亚......

**内资传统主流车企：**

吉利汽车、上汽乘用车、长城汽车、上汽大众、长安汽车、北京汽车、东风汽车、广汽、比亚迪、一汽集团、一汽解放、东风商用、上汽商用......

**全球领先一级供应商：**

博世、大陆集团、联合汽车电子、安波福、采埃孚、科世达、舍弗勒、霍尼韦尔、大疆、日立、哈曼、华为、百度、联想、联发科、普瑞均胜、德赛西威、蜂巢转向、均联...