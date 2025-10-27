---
title: SCA可达性分析基础知识普及
url: https://buaq.net/go-141155.html
source: unSafe.sh - 不安全
date: 2022-12-24
fetch_date: 2025-10-04T02:24:50.240498
---

# SCA可达性分析基础知识普及

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

SCA可达性分析基础知识普及

SCA可达性分析基础知识普及 日期：2022年12月23日 阅：101 最近开发安全
*2022-12-23 17:0:58
Author: [www.aqniu.com(查看原文)](/jump-141155.htm)
阅读量:26
收藏*

---

SCA可达性分析基础知识普及

日期：2022年12月23日
阅：101

最近开发安全/软件供应链安全是海内外最火爆的细分领域之一，SCA的可达性分析更是多次被提及。借着这个机会，做一个基础知识的普及。一是鸿渐作为深耕代码安全领域的小公司，靠的是专业硬实力，秀一下。二是很多职能人员缺乏专业性、没有鉴别能力，什么是好的，什么是差的，完全辨别不了，盲从心理特别厉害；我们一直怀着感恩的心服务客户，相互尊重，相互成就，有责任和义务做个普及；三是号召更多的有为青年加入我们，踏踏实实做一款好用易用的代码安全产品。

SCA工具基于代码（源代码、二进制代码）和构建文件（c语言的makefile文件、maven项目的pom.xml文件等）分析得到被测项目使用了哪些第三方组件，并关联得到这些组件包含的漏洞。问题在于，**传统SCA工具仅分析组件和漏洞的存在性，并未分析组件是否被自研代码调用（组件可达性），漏洞是否会被自研代码触发（漏洞可达性），这造成了大量的误报。**

2022年华中科技大学文明副教授等人开展了一个大规模的实证研究，首次以漏洞代码的可达性的视角，分析了生态系统中漏洞对下游软件所造成的安全威胁，结果显示已有SCA工具的**误报率高达86%**.[1] 也就是说，SCA工具报出的潜在漏洞，其中86%的漏洞对应代码没有被实际使用，漏洞无法触发。

由于SCA工具报出组件和漏洞数量太多，如果出现漏洞都去改，工作量太大(升级意味着换调用第三方组件的接口，换接口意味测试量加大)。ShiftLeft的报告显示，客户希望在不影响软件交付时间的情况下交付安全软件，而传统的SCA工具会报出大量（数千个）开源漏洞，大多数最终被发现没有影响（误报）。这些解决方案非但没有帮助开发人员，反而拖慢了他们的速度。

**SCA****可达性分析的意义在于，去掉引入但未使用的组件，同时降低无法触发漏洞的优先级，将注意力集中在实际影响代码的安全漏洞上，从而大幅提高SCA工具的可用性。**

SCA工具中的可达性分析，按层次可分为构建可达性、组件可达性和漏洞可达性。

## 2.1 构建可达性分析

构建可达性分析是SCA工具的基础功能，分析构建文件中引入的第三方组件，如分析maven项目的pom.xml文件得到引用的第三方jar包。

## 2.2 组件可达性分析

组件可达性分析，即分析开源组件（包括拷贝引入的开源代码和构建引入的开源组件）是否被自研代码引入（include/import）并调用。

组件可达性分析采用基于抽象语法树的方法实现，主要技术难点是大规模不完整代码解析技术，即在无需编译通过的前提下（要求被测代码都能编译是不现实的），快速准确解析不完整源代码。2018年北京大学马森等人在软件工程顶级会议ICPC上发表的论文[6]很好的解决了这一问题。

## 2.3 漏洞可达性分析

漏洞可达性分析，即分析漏洞是否会被自研代码触发。有两个技术难点：

一是漏洞细粒度对齐技术，由于CVE漏洞仅给出漏洞对应的组件或版本，需要进一步将漏洞对应到函数或行，才能用于漏洞可达性分析。鸿渐SCA通过基于专利的漏洞对齐技术，将超过10000个漏洞对应到函数或行，以支持细粒度漏洞可达性分析。

二是源代码静态分析技术（即SAST技术），即通过控制流分析、值依赖分析和约束求解等技术，判断自研代码到漏洞是否有可行路径，从而判断漏洞是否会被自研代码触发。鸿渐科技在SAST有着深厚的积累，发表了多篇论文、专利。

由于可达性分析需要强大的静态代码分析技术支持，根据调研，除鸿渐科技的SCA工具外，**国内尚没有支持可达性分析的SCA工具**，国际上仅有美国ShiftLeft公司[3]、美国MEND公司[4]的SCA工具包含部分可达性分析功能，这三家公司的共同点是都有强大的SAST工具作为技术支持。

ShiftLeft SCA在报告中声称，通过引入“攻击者可达性”（即漏洞可达性分析），可以将开源漏洞报出数量减少93%.

MEND SCA仅在报告中提到其正在申请的专利可以确定哪些漏洞直接影响代码，以最大程度地减少误报。[2]

参考文献

[1] <https://www.shiftleft.io/blog/introducing-attacker-reachability-reducing-open-source-vulnerability-tickets-by-90-or-more/>

[2] <https://www.mend.io/wp-content/media/2021/11/MEND-How-to-Reduce-Your-Alert-Count-Early-in-Development.pdf>

[3] <https://www.shiftleft.io/>

[4] <https://www.mend.io/>

[5] Qing Gao, Sen Ma, Sihao Shao, Yulei Sui, Guoliang Zhao, Luyao Ma, Xiao Ma et al. “static C/C++ bug detection in the presence of incomplete code.” In 2018 IEEE/ACM 26th International Conference on Program Comprehension (ICPC), pp. 385-3853. IEEE, 2018.

文章来源： 鸿渐科技

文章来源: https://www.aqniu.com/vendor/92563.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)