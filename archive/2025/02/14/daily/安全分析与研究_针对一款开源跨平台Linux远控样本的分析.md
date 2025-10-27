---
title: 针对一款开源跨平台Linux远控样本的分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490489&idx=1&sn=e3f9b98799f83408765ecfd1ad180d55&chksm=902fb491a7583d87cfaabb66a3c37a004878627b8b86cbd0d880670f766d19897982a00ba2a3&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-02-14
fetch_date: 2025-10-06T20:36:08.136452
---

# 针对一款开源跨平台Linux远控样本的分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmVZCzW0CpdlVznRjrnY28dow3NpBCss05IdG7YnTm993CRbQkkVvSE7tMAshWsu37SH3AAglxxIOQ/0?wx_fmt=jpeg)

# 针对一款开源跨平台Linux远控样本的分析

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

近日有人在社交平台上分享了一款开源的跨平台Linux远控攻击样本，样本被命名为ChaosRAT，威胁情报平台上有相关的样本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVZCzW0CpdlVznRjrnY28dopYjHBPicp7cMiaDu8U4qaLOiayflic12Gdum4MLXQOvm1cRibZlna8x6lZw/640?wx_fmt=png)

通过搜索发现该RAT样本，此前被用于相关的攻击活动，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVZCzW0CpdlVznRjrnY28do1L7eqVVU08icwQykjEtjVcPJOkD02nqBr9uic7qCichyyaCCjjFmrnctA/640?wx_fmt=png)

该攻击活动图片来源于网络，笔者从平台上下载该样本，发现沙箱没有跑出行为，于是对样本进行了相关分析。

样本分析

1.通过分析，发现该样本使用了开源的远控工具，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVZCzW0CpdlVznRjrnY28doibMnxqhfyREZ4zmficQnCk9seic7zkoShjE7icoLkTkQDsLQJxddwSA4Yg/640?wx_fmt=png)

2.样本使用的开源模块，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVZCzW0CpdlVznRjrnY28doYNCiblDfWu0BTicHpsLEDRMNpLJyASBeVR2chJ0ja6ZqWHb8l9mMQn0A/640?wx_fmt=png)

3.开源的远控工具地址https://github.com/tiagorlampert/CHAOS，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVZCzW0CpdlVznRjrnY28doO8xITfh4fQ8zvNNCS29Ylpa5YWChK9FVTWtnRs05tvuCMbwwLLCcsQ/640?wx_fmt=png)

4.逆向分析样本的入口代码，会解析一个配置文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVZCzW0CpdlVznRjrnY28doCBpnpjw9Kas41ibvr1VZiayZTbrPkDMBX2qnH0TKZQrPM5xNG6ffaPcQ/640?wx_fmt=png)

5.开源代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVZCzW0CpdlVznRjrnY28doKa1yGhQxcTiaJM0YFb0sdRdfuQicgrnodkBhydlHnwBrgoMq57F5NoCw/640?wx_fmt=png)

6.查看开源代码中读取和解析配置信息的代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVZCzW0CpdlVznRjrnY28do1NHbT3yo3AY1PN2Pdnl3tVHZT2qDolcROXg6xib00eLZYqWzk7f1UgQ/640?wx_fmt=png)

7.发现是使用Base64解析的配置信息，提取样本中使用的加密信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVZCzW0CpdlVznRjrnY28dogplfpoK1QeeF7bhlu89c6Pic5ibuhObJvSTbmPF3vIYBzYlfuDtnbabA/640?wx_fmt=png)

8.通过Base64解析之后，得到配置信息，包含远程服务器的端口、IP地址、Token信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVZCzW0CpdlVznRjrnY28dotdvLwBsYe1s2VrZZ49FJ0XEZhhbOfqTTRS5UkSfnqwNZclH9vKziadg/640?wx_fmt=png)

9.获取远程C2地址为176.65.141.63，端口为5223，通过威胁情报平台查询C2地址，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVZCzW0CpdlVznRjrnY28dogWuuiaLcicTy8sXDAvICJ2VqH4kt4ImRkxeeFKLlUAibTNXEntYFoL5UQ/640?wx_fmt=png)

该开源远控其他东西，有兴趣的自己去研究吧，很多黑客组织在攻击的时候也都会使用一些开源的远控工具，包含一些APT组织也常常喜欢使用一些开源的RAT工具。

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