---
title: AsyncRAT远控样本分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490516&idx=1&sn=7ac10e9070240df496ebd6bd1b356d93&chksm=902fb4fca7583dea7deb83e0fa6cdd03166a45c9b98ba1f5d9ba4f5b6fa25de16e670b008855&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-02-16
fetch_date: 2025-10-06T20:36:54.366331
---

# AsyncRAT远控样本分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmWZmr8ica3eEGMux8BKZqW4jQvIJtNAyfxeY0e3yicib8sBOIhFpW8fnlf6RK2KoWM8wpjia7CF3ibWR2Q/0?wx_fmt=jpeg)

# AsyncRAT远控样本分析

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

AsyncRAT 是一种远程访问工具 (RAT)，旨在通过安全加密连接远程监控和控制其他计算机，它是一种开源远程管理工具，但它也可能被恶意使用，因为它提供键盘记录器、远程桌面控制等功能，以及可能对受害者计算机造成损害的许多其他功能，一些APT组织也曾利用它来进行攻击活动。

此外AsyncRAT 可以通过各种方法传播，例如鱼叉式网络钓鱼、恶意广告、漏洞利用工具包和其他技术，因其开源特性及模块化设计，已经成为攻击者青睐的黑客远控工具之一。

样本分析

1.母体样本运行之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWZmr8ica3eEGMux8BKZqW4jiaUsSxoDS3Kd8RX3detAIkpzdQGz4R4Wfhqvia7JgsD3Ujbrpsclnmmg/640?wx_fmt=png)

2.获取核心PayLoad,采用NET语言编写，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWZmr8ica3eEGMux8BKZqW4jrBEHBiaKDwzogUSQhKOwPSj0FPBcjaZEtopvTXT8M04o2HbyWlfgaJQ/640?wx_fmt=png)

3.AsyncRAT核心代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWZmr8ica3eEGMux8BKZqW4jqxTI9UbH90SRPAeBKcnRl5ia7ia0HzRWvAicqficLEvK3VKwh9vCqpzC8g/640?wx_fmt=png)

4.AsyncRAT开源项目地址https://github.com/NYAN-x-CAT/AsyncRAT-C-Sharp，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWZmr8ica3eEGMux8BKZqW4juRCmPcstxARqG3mib9TstbCaOqhrAHlovWnlqibJF12ZicVhuTU0j9Z7A/640?wx_fmt=png)

5.解析C2等配置信息代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWZmr8ica3eEGMux8BKZqW4jqrgEhLUjicXzy04yc2SgJU6v22ia9NEkSeXyZlYgfiakIojIraLEusfaw/640?wx_fmt=png)

6.动态调试，获取到C2配置信息，域名为favor.ydns.eu，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWZmr8ica3eEGMux8BKZqW4jGclDGxgJyRcHerNmHqkYRkQvVEib1Ihf4CVqZuLRUy2A3lVXbeYtvMA/640?wx_fmt=png)

7.在威胁情报平台查询C2域名，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWZmr8ica3eEGMux8BKZqW4j3x92zbq3MAFe1oOusFtnuTczpb1yicKggHDibcMDD7F2JticaArouBp1g/640?wx_fmt=png)

针对AsyncRAT开源项目，感有兴趣的可以自行研究。

总结结尾

黑客组织利用各种恶意软件进行的各种攻击活动已经无处不在，防不胜防，很多系统可能已经被感染了各种恶意软件，全球各地每天都在发生各种恶意软件攻击活动，黑客组织一直在持续更新自己的攻击样本以及攻击技术，不断有企业被攻击，这些黑客组织从来没有停止过攻击活动，非常活跃，新的恶意软件层出不穷，旧的恶意软件又不断更新，需要时刻警惕，可能一不小心就被安装了某个恶意软件。

对高级恶意软件分析和研究感兴趣的，可以加入笔者的全球安全分析与研究专业群，一起共同分析和研究全球流行恶意软件家族，笔者今年打算深度跟踪分析一些全球最顶级的TOP恶意软件家族，这些恶意软件家族都是全球最流行的，也是黑客攻击活动中最常见的恶意软件家族，被广泛应用到各种勒索攻击、黑灰产攻击、APT窃密攻击活动当中以达到攻击目的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmXDIda3D6VvFWhqojST24E2rTRBJMYDfYowK8WcvBScfWlJiaYZ5elMdlrREG1LDVODxFQ0Eoy0YLQ/640?wx_fmt=jpeg)

安全分析与研究，专注于全球恶意软件的分析与研究，深度追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmW8qYF2seSKglWFKoJdassltn5V5IPUn3OGXsdD4v2nRPg8ZzFAicpXlmlwVmd9KTm4XPkRcXtBEKw/640?wx_fmt=jpeg)

王正

笔名：熊猫正正

恶意软件研究员

长期专注于全球恶意软件的分析与研究，深度追踪全球黑客组织的攻击活动，擅长各种恶意软件逆向分析技术，具有丰富的样本分析实战经验，对勒索病毒、挖矿病毒、窃密、远控木马、银行木马、僵尸网络、高端APT样本都有深入的分析与研究

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

安全分析与研究

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

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