---
title: 武汉大学国家网络安全学院本科生成果被信息安全领域国际权威会议ESORICS 2026录用
url: https://mp.weixin.qq.com/s/DOfTM9QOQ-GJ32hQ3MrdTg
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T08:01:21.101321
---

# 武汉大学国家网络安全学院本科生成果被信息安全领域国际权威会议ESORICS 2026录用

# 武汉大学国家网络安全学院本科生成果被信息安全领域国际权威会议ESORICS 2026录用

信息网络安全杂志

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

近日，武汉大学国家网络安全学院NIS&PLab成员、信息安全专业2024级本科生贺启航撰写的论文被第31届欧洲计算机安全研究研讨会（the 31st European Symposium on Research in Computer Security, ESORICS 2026）录用。论文题目为“TransBit: Efficient Hotpatching for Real-time Microcontroller-based Embedded Devices”（《TransBit：面向基于微控制器的实时嵌入式设备的高效热补丁技术》）。贺启航为论文第一作者，与武汉大学计算机学院计算机科学与技术专业2023级本科生柯昀志、武汉大学武汉数学与智能研究院何艺研究员（通讯作者）、清华大学李琦教授、武汉大学国家网络安全学院王骞教授合作完成。

![](https://mmbiz.qpic.cn/mmbiz_png/FNlvhjUaDTNx1rjG2O3BrlmcQnFU7OGYT1icy9r1YhRIxLRJVrB56oqyhZUaq7xanp9YDcXR2cVqsmia3botdNqxa7yFKIbOzthYVvWiaRZJ3g/640?wx_fmt=png&from=appmsg)

图-1 TransBit核心机制设计

随着基于微控制器单元（MCU）的嵌入式设备日益互联，固件漏洞使得设备面临严重的安全风险。目前，热补丁技术能够在无须重启系统或重新刷写固件的情况下修复漏洞，是一种具有广阔应用前景的解决方案。然而，在基于MCU的设备上实现热补丁面临巨大挑战，根源在于这类设备通常直接从片上NOR Flash中执行代码，导致在线代码修改成本高昂且受到严格限制。现有解决方案主要通过硬件支持或软件间接跳转来应对这一问题，但存在适用范围有限、补丁容量受限、持续产生运行时开销和存储开销等问题。为解决上述问题，作者提出了TransBit—一种面向基于 MCU 的嵌入式设备的新型热补丁机制。TransBit利用NOR Flash编程操作的非对称特性，实现高效的原地控制流重定向。TransBit引入了两项关键技术。首先，它采用双向指令变形技术，在目标函数入口处预先放置无副作用的占位指令，并仅通过从1到0的位翻转对这些指令进行重写，从而同时支持补丁的安装与卸载。其次，它引入了一种容错补丁分派机制，利用故障处理程序，容忍原地更新过程中偶发的位翻转失败。实验评估结果表明，TransBit能够维持系统的实时性保证，其热补丁触发延迟与基于硬件的方法相当；与基于软件的解决方法相比，其延迟降低了65%～78%。同时，TransBit保留了纯软件设计的灵活性，能够支持多种处理器架构，且不存在固有的补丁数量限制。与现有基于软件的解决方案相比，TransBit在实现显著更高性能的同时，仅产生可忽略不计的运行时开销，其所需存储开销还不到现有软件方案的20%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FNlvhjUaDTN95thyaXE62Xjg1kU3OMDhuicl5hR3sUmQaWmnibdLibiaGicoyTeRsVbcI8700UsicM1qYJibTyyIkLIiaJ0FwWN1x6pd4Me7cIMD5dI/640?wx_fmt=png&from=appmsg)

图-2 TransBit工作流程

据悉，ESORICS 2026将于2026年9月14日至18日在意大利罗马召开，会议地点为罗马第一大学主校区。ESORICS于1990年首次在法国图卢兹举办，已有三十余年历史，是欧洲计算机安全领域历史悠久、具有重要国际影响力的学术会议，吸引了来自全球学术界和工业界的研究人员参与。该会议是中国计算机学会（CCF）推荐的网络与信息安全领域B类国际学术会议，主要关注计算机安全、信息安全、网络安全与隐私保护等方向，被录用的论文反映了网络与信息安全领域的重要国际前沿研究成果。

来源：武汉大学

![图片](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8yDJWicSECDq8dgel7DctAMAnNheJf2kkfQOiaFMdZaWNIDt9IxOkEhI5TJar4wnyAiba9twTOxeKZg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

**信息网络安全**

《信息网络安全》创刊于2001年，是由公安部主管，公安部第三研究所、中国计算机学会主办，面向国内外公开发行的国内首批信息安全类期刊之一，于2015年成为中国科技核心期刊，2017年成为中国科学引文数据库来源期刊，2018年成为中文核心期刊，2022年入选CCF计算领域高质量科技期刊分级目录。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsN9e1fkuM1ibgD3PcZiaqJrZia7KQWDwichD8lvo4RqfPcNkuyqje45IOXD0HocBDntaDdK4tibWoTIs5Ww/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

中文核心期刊

中国科技核心期刊

中国科学引文数据库来源期刊

CCF计算领域高质量科技期刊

![图片](https://mmbiz.qpic.cn/mmbiz_png/v4vz52CcB12BRNZGqdRDIBsUQ6WickDoUNkuVicKXooNbRSzdGDGuJtxJodlbpr1B07yAReAz5V5jj47Yaq7ujRw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

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