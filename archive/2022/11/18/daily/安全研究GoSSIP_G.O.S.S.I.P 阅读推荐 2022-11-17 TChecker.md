---
title: G.O.S.S.I.P 阅读推荐 2022-11-17 TChecker
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247493292&idx=1&sn=cf2a25e194492d62db485d727b0042fa&chksm=c063c875f71441631fb55678fe988ef0de38a2b251d2cae6fd5583a163814fe02884004b1edb&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2022-11-18
fetch_date: 2025-10-03T23:07:34.300515
---

# G.O.S.S.I.P 阅读推荐 2022-11-17 TChecker

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21GlqIoiaGd62HcTrPSUYmfGiaLxQOC1m36ib2DFfiaYwAUKicoDAgmzJOOzkc3TSGoxFFFMywBSNXIDB9g/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2022-11-17 TChecker

Changhua@CUHK

安全研究GoSSIP

今天为大家推荐的论文是来自[香港中文大学计算机安全实验室](http://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247483652&idx=6&sn=2900a2d02b01d9e30fd4aff5d7a56149&chksm=c0602fddf717a6cb30143c06da999e41b6e3cfd0a08f799c853f0b5ddaad431ed7c337ea0311&scene=21#wechat_redirect)投稿的关于污点分析的最新研究工作TChecker: Precise Static Inter-Procedural Analysis for Detecting Taint-Style Vulnerabilities in PHP Applications，目前该工作已经收录于CCS 2022。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GlqIoiaGd62HcTrPSUYmfGiaCWLeTm4UIZEmhHwe9fYCcbhxsyOKicQ31ruLtZl8cDjobdey7XQ5SibA/640?wx_fmt=png)

污点分析是一种常用的程序分析方法。根据指定的source和sink，污点分析工具跟踪由source引入的污点数据并判断其是否能够不经过无害处理（sanitization）传播到sink。根据跟踪手段，污点分析又分为动态污点分析和静态污点分析。相比动态污点分析，静态污点分析有更好的代码覆盖量。这篇论文提出并实现了一个在PHP应用程序上的静态污点分析工具，TChecker。相比于已有的静态污点分析工具，TChecker分析并支持PHP的多种语言特性，这使得它能够准确的跟踪污点数据并具有更低的漏洞误报率和漏报率。

作者调查已有的对PHP程序的污点分析工具（RIPS, PHPJoern, etc）并发现他们在设计上或实现上有以下缺陷。首先，他们不能准确地判断call site（e.g., $obj->foo()）的目标函数。这是因为PHP是一个弱类型语言，call site的receiver（e.g., $obj）类型往往不会在程序中显式定义。常见的做法是只匹配函数名（e.g., foo()）而忽略receiver的类型，但这往往会导致极大的误报或漏报。更先进的工具RIPS通过intra-procedural data-flow analysis判断receiver类型，但因为receiver可以在函数外被赋值（e.g., $this->module->foo()），这种方法仍然不能有效分析很多call sites。

其次，已有工具为了简化分析，在实现上做了一些不（总是）正确的假设。比如说，RIPS的开源实现认为只要函数调用的参数是污点数据，那么函数一定会返回污点数据。RIPS的商业实现认为一个call site总是调用同样的函数，但实际上receiver可以是不同的类型，因此call site可能在不同contexts下调用不同的函数。

最后，作者发现已有的开源污点分析工具不支持PHP的一些特有的语言特性，比如dynamic includes。这让他们在遇到这些不支持的语句时过早地停止污点传播而导致漏报。

**设计与实现**

下图展示了TChecker的系统总览图。TChecker首先创建一个call graph，再在callgraph的帮助下进行污点分析。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GlqIoiaGd62HcTrPSUYmfGiaaParSicKXOuicH9x53ibgtoLWfXyQhrLcWluibEkzYq5Yw6XxicrgAmicocw/640?wx_fmt=png)

首先，TChecker通过对receiver和variable function name （e.g., $a()）进行inter-procedural data-flow analysis来推断一个call site的调用函数。这里的一个问题是，实现inter-procedural analysis反过来需要call graph。为了解决这个问题，作者迭代对一个call site进行数据流分析来决定它的目标函数。具体来说，每当TChecker连接一个call edge，它就会判断这条新加入的call edge是否影响call site。根据这条call edge引入的新的数据流，TChecker分析call site的receiver或variable function name在新的context下的值并不断更新这个call site的target functions。值得注意的是，由于PHP的多态性，根据call site还原的调用函数名可能不与函数定义名相同，因此作者在还原call site的调用函数名后需注意类的继承关系。此外，由于静态分析函数变量值（e.g., $a()）的复杂性，TChecker会使用通配符来表示一些它不能解析的变量，这会导致一定的误报。根据实验结果，由于TChecker在实现上更好地支持了PHP的语言特性，它不能解析的call site比例小于0.1%。

在污点分析模块，TChecker根据当前的contexts决定一个call site的调用函数。具体来说，由于绝大部分有多个调用函数的call site是method call sites（e.g., $obj->foo()），并且调用一个非静态method前必须调用构造函数，因此TChecker选择在同一类下已有其他methods被调用的method作为调用函数。进行跨函数污点传播往往很耗时，TChecker采用选择性污点传播来提高分析效率。最后，TChecker支持多污点传播，在当前实现下它能检测SQLi, XSS, 和DoS漏洞。

**结果**

作者用TChecker测试了17个PHP应用程序，并与其他静态污点分析工具的测试结果比较。实验结果显示TChecker可以检测出其他静态污点分析工具检测出的全部漏洞。TChecker还检测出了50个其他静态工具不能检测出的漏洞，其中包括18个新的漏洞，目前5个漏洞已经被修复。

在误报上，TChecker具有153（53.87%）个误报，和最少漏报的工具结果接近（52.02%），作者发现很多误报来自应用程序的无用代码。在漏报上，作者收集了PHP应用程序在CVE database的所有已知漏洞，发现TChecker由于不能识别insufficient sanitization而仍有一些漏报。为了减少静态分析工具的漏报，一个方法是更好的分析PHP程序的sanitization行为。最后，在检测时间上，由于TChecker更完整的数据流分析，它的分析时间可能是其他静态工具的几倍。由于TChecker能以不错的精度（precision）检测出更多漏洞，作者认为这个这个检测时间是可以接受的。

论文下载：

https://seclab.cse.cuhk.edu.hk/papers/ccs22\_tchecker.pdf

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