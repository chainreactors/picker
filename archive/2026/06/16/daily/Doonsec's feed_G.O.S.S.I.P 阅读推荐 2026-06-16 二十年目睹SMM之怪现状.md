---
title: G.O.S.S.I.P 阅读推荐 2026-06-16 二十年目睹SMM之怪现状
url: https://mp.weixin.qq.com/s/X9wu46qITGmrRmGrvOLkmw
source: Doonsec's feed
date: 2026-06-16
fetch_date: 2026-06-17T07:00:51.575090
---

# G.O.S.S.I.P 阅读推荐 2026-06-16 二十年目睹SMM之怪现状

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eQ0Wf6rqolWMtDiavaejLIZLEFXyCk6XG8VmWMv8CHgq8GSx1GQiamXgaf3fcy0OUsvoxZGh5rl5oFuRvibIfcibbhZYoyOCWResNqvbInlzlWU/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2026-06-16 二十年目睹SMM之怪现状

原创

G.O.S.S.I.P
G.O.S.S.I.P

安全研究GoSSIP

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

你是否还记得彭博社（Bloomberg）曾经有一则非常愚蠢、充满了不懂技术的人会犯的错误的文章？这篇文章的作者估计是读了什么都市传说，然后再把它和一些特定的技术嫁接一下，最后就炮制出来一个假新闻。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolXOSlpKlyPTtyqyuyyZkrmIAMdxic2vE1Mlowib4PiaYx4SHKTDXibwF8QpZ68mwfycqYePm9rnDSBnj2icl1TSia1zBnHm95ibnRBETI/640?wx_fmt=png&from=appmsg)

话说回来，如果假新闻背后可能有那么一点点真实的东西，很可能就是在坊间流传甚广的“Intel SMM Hack”，也就是针对x86架构上的System Management Mode（SMM）这个不太为人所知的管理模式进行利用（abuse），用来搞一些非常隐蔽的安全攻击。整整20年前，在2006年的CanSecWest会议上发表的演讲 *Using CPU System Management Mode to Circumvent Operating System Security Functions* 可能是最早一批揭示SMM安全风险的技术讨论，而在整整20年后，来自WOOT 2026的SoK论文 *20 Years of Power, Privilege, and Peril in x86 System Management Mode* 带我们回顾了这20年间的各种怪现状：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolUyHpv605WsjpdVjJJmjAOp9PziaRAxGYX4Gt3MYvKr2XOSjmwaK1ciaVLMGRu5yehoTsLI79ML5AE6vRCd9SJhsiaodVazQvib7YA/640?wx_fmt=png&from=appmsg)

首先，我们都知道Intel那个向北京致敬的Ring设计，3环就只能是老百姓代码住，0环是给内核权限保留的，不过后来虚拟机管理器（hypervisor）需要更高的权限，于是就出来了一个“负一环”，没想到大家又发现环内有环（置身环内？）：在x86处理器的最底层还有一个系统管理模式——SMM，不管出于是类似嵌入式系统那样保证在死机的时候可以进行处理的目的，还是为了让服务器在上层的操作系统之外能够支持BMC这种远程管理功能，总之SMM模式听上去是很有用的，问题就在于它太过于底层，不受上层任何的约束，同时它又能够干预到上层代码，所以这个模式就真的是充满了风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQ0Wf6rqolXwkzsbaeCZrdTKaSwM8vDwJRH8tZE3Uha17BLKC4bU4WxkCQ3h4FJ4kiajrtGYdlOxXewtn69qCYFjOx77LticrO88U19BVF3EQ/640?wx_fmt=png&from=appmsg)

本文的作者开展了非常系统性的调研（当然在AI时代这个工作会更加便捷）：他们对过去20年间针对SMM安全的69项不同的研究进行了总结，形成了今天我们推荐给大家的这篇SoK论文。论文的第二章系统性地总结了SMM的实现特性，虽然这部分知识在Intel的手册里面都有，但是作者不光介绍了SMM的特征还把它和其他的一些同类的特权隔离方案（比如Intel ME）以及一些TEE（SGX、TDX、SEV、TXT）进行了横向比较：

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolWkftV5v5d0axjJvAJdcObDJTWUTW8AeaH1LOvw81htkZJJK9xyaUaQOc59ypiasowLIlQzErUAiaQnxUv46OdA909eYScrsPXEo/640?wx_fmt=png&from=appmsg)

同时，作者重点关注了SMM在演化过程中（对，和其他软硬件一样，SMM的安全机制也是在不停改进的）新增的各种防护机制：

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolWpiaKKGVZeCqoBveO4QxASC7MBPU4CC49GLlnjfxAFhLekvjjEgAdLGDcb8PCZhxoKzkUJwJh1NTZWk3BdS5icF602TlzP0xhqo/640?wx_fmt=png&from=appmsg)

讲完了SMM的知识，论文的第三章就正式进入到了二十年目睹之怪现状：上来就弄了一张超大的表格，总结了SMM相关安全攻防的研究，把这些研究分为了三个阶段，并在第四章进行了详细讨论。

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolWFIfL7uj7CP1ibq9ibeJO7tgPLibz5kBGRMToNmpFb1ia7EbcswYt6qY83sHREfrY5NTE6S3hHsvPrIcZFf7v8B06WSHOzLtdcq8w/640?wx_fmt=png&from=appmsg)

作者认为，SMM相关安全攻防研究的第一个阶段（Era 1）和每一类计算机系统的早期都很像，那就是只重视功能不重视安全，导致各种错误的配置满天飞，攻击者往往就是很简单地利用了不正确的SMM配置（特别是针对SMM特有的SMRAM这块内存空间）来实施越权攻击。这里作者专门提了一下Intel Security在2014年发布的CHIPSEC安全评估工具，算是一个当年的SOTA安全评估工具（查缺补漏）：

![](https://mmbiz.qpic.cn/mmbiz_png/eQ0Wf6rqolUFbdfSCYG2Hh5VLPN4J1ACXlZu4dGrtp584lVKUZV1bbN0AnZa4tJpIoCJCXFVqfCMJNliaiantcsCwhh74IgvdhV2IwulSBpW8/640?wx_fmt=png&from=appmsg)

SMM相关安全攻防研究的第二个阶段（Era 2）体现出来的特点跟Android安全发展历史很像：low hanging fruit都被摘完了，于是大家开始硬着头皮去分析（二进制）代码，挖掘里面的漏洞并且想办法写exploit，这个阶段Intel甚至还搞了个专门针对BIOS的“亦可赛艇”项目——Intel’s Excite project（在WOOT 2015会议上报告 https://www.usenix.org/system/files/conference/woot15/woot15-paper-bazhaniuk.pdf 不知道为什么WOOT 2015那个主页上点击“technical sessions”就会跳转到USENIX ATC 2015页面，难道他们不晓得ATC已经亖了吗）专门利用符号执行来分析SMM相关的代码的安全性，这不禁让我们怀念起来安全研究还没有被Fuzzing刷屏的年代。

进入到SMM相关安全攻防研究的第三个阶段（Era 3，2020年至今），整个研究都进入到了自动化阶段，不管是大量使用各种安全分析工具技术还是引入AI辅助，这个阶段大量针对SMM的CVE被曝光，更有意思的是，作者关注到了AMD相关的SMM安全漏洞开始增多，这正好对应了苏妈开始暴打牙膏厂的趋势，看起来Bjarne Stroustrup的金句“世上只有两种编程语言：一种是总是被人骂的，一种是从来没人用的”也可以用在这里~~~

论文的5.6章也很有意思，作者讨论了其他的一些平台（ARM、RISC-V）在吸收Intel平台的经验教训方面做得如何，当然肯定还是那个老生常谈的黑格尔老师的名言“人类从历史中学到的唯一教训就是人类无法从历史中学到任何教训”

---

> 论文：https://vanbulck.net/files/woot26-smm.pdf
> 数据集：https://github.com/antonislouca/SoK-SMM

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