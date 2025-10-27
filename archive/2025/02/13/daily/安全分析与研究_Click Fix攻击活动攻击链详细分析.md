---
title: Click Fix攻击活动攻击链详细分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490465&idx=1&sn=44925a956b7401b47a1357644ca3e29a&chksm=902fb489a7583d9f5932366f8615cf270f0f9d23b58e11be86334a57f930e405453ec536e9fd&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-02-13
fetch_date: 2025-10-06T20:35:42.955500
---

# Click Fix攻击活动攻击链详细分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmXiaD7iaTbKuM47q8J6x7YM1Jemuc2EdiaHEYfTIiaucUD5IcUPicjm8FhprLMFKlfJXnIMOkaICLQL2jw/0?wx_fmt=jpeg)

# Click Fix攻击活动攻击链详细分析

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

Click Fix攻击是一种复杂的社会工程形式，利用真实性的外表来操纵用户执行恶意脚本，自2024年初首次出现以来，这种策略已导致多起恶意软件分发活动，涉及受感染的网站、恶意分发基础设施和电子邮件网络钓鱼。

最近一段时间Click Fix/Fake CAPTCHA攻击活动非常频繁，笔者对最新的一例Click Fix攻击活动的最新攻击链案例进行了详细分析，分享出来供大家参考学习，省略了高级样本的逆向分析过程，对这部分感兴趣的，可以自行调试分析研究一下，如果实在分析不出来，搞不定的时候，再来找笔者交流沟通吧，最近这类高级样本非常流行，全球的客户应该已经遇到了不少这样的攻击样本，很值得深入的分析研究一下。

攻击链分析

1.访问钓鱼网站，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXiaD7iaTbKuM47q8J6x7YM1Jx04UCickyXKDuPzAtWSnzTgCPVMKb45NjC7l6DlJGiavagUofX1JgxOg/640?wx_fmt=png)

2.点击验证按钮之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXiaD7iaTbKuM47q8J6x7YM1JHSwBuaSfGh3Ywjl6KWKXUGIicBXd94lWLA7oWlorHgzS3G2RhUS3e6A/640?wx_fmt=png)

3.按照上面的提示信息，执行相关的操作，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXiaD7iaTbKuM47q8J6x7YM1JGOFP1rq8PhLV1aBHicYFSNhadMUqoB10z8covSpYgHNUEU01oqowcsw/640?wx_fmt=png)

4.执行上面的恶意脚本，恶意脚本会从远程服务器上下载高级恶意样本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXiaD7iaTbKuM47q8J6x7YM1JclGsG8TOwm9xMPa7bJqjzbmATwbr7bNkluBQCBqvp3vibndiaib2vlx0Q/640?wx_fmt=png)

5.下载的高级恶意样本，使用NET语言编写，NET Reactor加壳保护，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXiaD7iaTbKuM47q8J6x7YM1JyX5BqAEbkPmneApAHT43etnmD2kAWAVAouQSN98RHJzwSb0icsVcxxA/640?wx_fmt=png)

6.动态调试，获取到核心的PayLoad，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXiaD7iaTbKuM47q8J6x7YM1JyYd9FCjMhbQ6gcKDqzfCJAiaXQtfqibKHT55nL2nP5oibOF9NPg8RrR0g/640?wx_fmt=png)

7.核心PayLoad的编译时间为2025年2月7日，最新编译的攻击样本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXiaD7iaTbKuM47q8J6x7YM1Jbe4ibY7njPYMqDFf5dJDRRVrkwIXib3oYQJbJPJGcOT5yTOkANtm8VSg/640?wx_fmt=png)

8.通过分析该PayLoad为一款窃密木马家族，里面包含各种流程混淆加密处置，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXiaD7iaTbKuM47q8J6x7YM1JGRg3YQT3EKaS2chDicFOpFHkOK6rMaHk2ks0TojLvetQkMibeCDKBmicQ/640?wx_fmt=png)

9.采用了DGA算法，生成远程服务器C2，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXiaD7iaTbKuM47q8J6x7YM1JzdQM1v78xKsCCMyE0YkicPOOiaPexiaR8gZg6RqVnDku8uC1VgFAicg4nw/640?wx_fmt=png)

其他分析过程省略，该样本分析调试有点意思，最近也非常流行，有兴趣的朋友自己去研究一下。

对DGA解析出来的C2域名进行查询，在国内几家大安全厂家威胁情报平台均未标记。

如果对Click Fix/Fake CAPTCHA攻击活动感兴趣的，可以参考笔者之前发布的相关分析视频，里面有完整的攻击过程演示。

威胁情报

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXiaD7iaTbKuM47q8J6x7YM1Jq78UsF4frXKvqyDw84nG9a3unRiaYSJvEQ5uic9e8Lwa8yibnmvicN9xHQ/640?wx_fmt=png)

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