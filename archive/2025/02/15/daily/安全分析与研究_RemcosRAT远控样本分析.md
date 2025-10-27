---
title: RemcosRAT远控样本分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490503&idx=1&sn=28006c1f85e8f5014f9db11768657e14&chksm=902fb4efa7583df9c541622228ae99f87615be5357c978f826ae9efd24ac5d521b0c1a587ca0&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-02-15
fetch_date: 2025-10-06T20:37:48.303137
---

# RemcosRAT远控样本分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmWZmr8ica3eEGMux8BKZqW4jQvIJtNAyfxeY0e3yicib8sBOIhFpW8fnlf6RK2KoWM8wpjia7CF3ibWR2Q/0?wx_fmt=jpeg)

# RemcosRAT远控样本分析

原创

pandazhengzheng

安全分析与研究

‍

**‍安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

RemcosRAT(远程控制和监控软件)是一种用于远程控制计算机的商业远程访问工具，RemcosRAT被宣传为可用于监视和渗透测试目的的合法商业软件，但已被用于众多黑客攻击活动，包含一些APT攻击活动，此前APT-C-35组织（肚脑虫，又称Donot是一个针对巴基斯坦、斯里兰卡等印度周边国家政府机构等领域进行网络间谍活动，以窃取敏感信息为主的攻击组织）就曾利用RemcosRAT远控进行攻击活动。

RemcosRAT一旦被安装就会在受害者计算机上打开后门，授予远程控制用户完全访问计算机的权限。

RemcosRAT由网络安全公司BreakingSecurity开发并维护，官方网站：https://breakingsecurity.net/remcos/

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWZmr8ica3eEGMux8BKZqW4jic7whhZ38PVh0HHuV0TMFzR33SBypGdJyibWiacUszkd8dwHJd8wsfoDA/640?wx_fmt=png&from=appmsg)

样本分析

1.样本外壳使用VB编写，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWZmr8ica3eEGMux8BKZqW4jf0V0AicaiaAYQRTPSrnFTI2etK0e80FrznC6iaUJ5ib1Pb8sfAtJfdhfog/640?wx_fmt=png)

2.对VB程序进行反编译，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWZmr8ica3eEGMux8BKZqW4j9mqZmA0b9pyvPWlGvSSh0oIM1IavcxBNnOickZO3uDAsrdfZv9Ziawrw/640?wx_fmt=png)

3.获取程序内核PayLoad，采用C/C++编写，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWZmr8ica3eEGMux8BKZqW4j4tU7sMdjIeKAzPMoWwaz1OGQVeWxRynXzGCLka7m1gBwUxQgNKTh5w/640?wx_fmt=png)

4.创建互斥变量，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWZmr8ica3eEGMux8BKZqW4jWPGmiajOQutEFM6zUWicS8t9aT2BBJkPFVLAyicJjUxuXNV7KzNx7kA4g/640?wx_fmt=png)

5.RemcosRAT版本信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWZmr8ica3eEGMux8BKZqW4jeRPyRmM5zwYmUJZA2OsPYjicicTTriablnC7SN8diboSrtVYdwNYm6BoGw/640?wx_fmt=png)

6.加密的配置信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWZmr8ica3eEGMux8BKZqW4jfdicnpOxMnA4oYLzkuNkN7PSOw2QdC1H4iam0ibNWsHibia1qeuT3ow7lAQ/640?wx_fmt=png)

7.解密之后的配置信息，C2地址为irukdns.warzonedns.com，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWZmr8ica3eEGMux8BKZqW4jqh526Rh6PYpOfv7iacwFvyjaYbmKUHdYsdRYykNA7lvvv3K7OqY4icUg/640?wx_fmt=png)

8.可以通过威胁情报平台关联到一些相关的样本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWZmr8ica3eEGMux8BKZqW4jFKWian4hFBw1u0udwIFic20BjWamAu8fVh0EIhBp0mGt2NGsgMDelu6w/640?wx_fmt=png)

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

‍

‍

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