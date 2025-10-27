---
title: 新型勒索病毒使用BYOVD技术对抗安全软件
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490399&idx=1&sn=4930eda061bf1e37abec8fd94f44feee&chksm=902fb477a7583d618495f2c77cad732142e3f8f7ec8411ac345df2da14b284c288843989ddb0&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-02-10
fetch_date: 2025-10-06T20:36:51.005181
---

# 新型勒索病毒使用BYOVD技术对抗安全软件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmUeBIuTpsS9Gb5JkY8HHg65OwP2RaNfqZibC1VLejPKcq3qbIlm4lr9Cr8P4UVwFHG3dkVEQjKzYgw/0?wx_fmt=jpeg)

# 新型勒索病毒使用BYOVD技术对抗安全软件

原创

pandazhengzheng

安全分析与研究

‍

**‍安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

今天看到群里有人求助，询问是不是使用了BYOVD技术，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUeBIuTpsS9Gb5JkY8HHg65dkfz3eDXbvCxicWnEh0wDH0WkQxEJpUtUWQNvJeM7NYicfhHyWnLB5VQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUeBIuTpsS9Gb5JkY8HHg65S5Rdu3ZNZLtOGElNfH1ibKc5LvaHBwBP1icTia9mT44E0opbgtSia66VnQ/640?wx_fmt=png)

最近一两年BYOVD技术被广泛应用到了各种黑产攻击、APT攻击以及勒索病毒攻击活动当中，笔者近期在对某黑产组织进行跟踪，捕获到该组织的最新攻击样本，通过某安全厂商的驱动程序漏洞，利用BYOVD技术对抗其他各种终端安全软件包括各种EDR、AV、XDR软件等，对该样本进行详细分析，该组织正处于发展阶段，通过肉鸡控制大量主机，从而进行网络违法犯罪活动。

勒索病毒

1.勒索病毒样本，编译时间为2025年2月5日，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUeBIuTpsS9Gb5JkY8HHg65du1dmJHFPtP11aUnFFVsJVqA827y53iaEmuiajWLZK509LUjFyk2Cbxw/640?wx_fmt=png)

样本时间非常新，搞勒索的果然挺积极的，一开年就开始搞钱了。

2.勒索病毒加密后的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUeBIuTpsS9Gb5JkY8HHg65ibEqhsg0noBKiaQfichSzbXfR9yt4RiaUugxDictZulWtadt5HKic34qZYSw/640?wx_fmt=png)

3.生成的勒索提示信息文件名为RECOVERY INFO.txt，勒索提示信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUeBIuTpsS9Gb5JkY8HHg65NGP5XdtrEjy7TRUqFCU1yfWLKUwHCsL0hSOFezpERmtQMo5GKVdiaMw/640?wx_fmt=png)

4.同时还会生成一个wxr.txt的文件，包含用户的ID以及主机相关信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUeBIuTpsS9Gb5JkY8HHg65QlP30sRs33ibUMibRHmKPGVs6UwPR0s6bnYZvoiaQzicX7O3Qx8prtKl3A/640?wx_fmt=png)

5.勒索病毒解密暗网网站，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUeBIuTpsS9Gb5JkY8HHg65tcFWxeVM24wjFmAF61jgHUpibEHo7exWiaEQShLnOp4JAqdgYmASxib9g/640?wx_fmt=png)

勒索病毒后面有空给大家详细分析吧，这里就不多扯了。

BYOVD技术

1.先看看驱动程序，带有金山的数字签名，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUeBIuTpsS9Gb5JkY8HHg65ccFTzVVNkE5w2YMo3Y6Xm2gfDDn4yQyfhHF35ldrx3tGUevv7YlzBQ/640?wx_fmt=png)

2.驱动程序在VT上只有两家报毒，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUeBIuTpsS9Gb5JkY8HHg6527rrrVUIcsVC9zean0Iq82IicaYbstKNNHezvsJHjU07gzItcdj0XFQ/640?wx_fmt=png)

3.通过分析该驱动程序，可被利用用于对抗安全软件，与此前笔者研究过的BYOVD技术中的驱动一样，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUeBIuTpsS9Gb5JkY8HHg655oiabiamq82yibDUhqDwH3xaeSEXdMjZt9rRicUocDxofY3dsAmg9D4GHQ/640?wx_fmt=png)

4.加载可利用的驱动程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUeBIuTpsS9Gb5JkY8HHg652OamicaurrHI2Kru6Mm8B5Hoqx9d2R2lWdZGRgA9wauooZmoKBicUGng/640?wx_fmt=png)

5.调用驱动程序的接口，对抗安全软件进程，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUeBIuTpsS9Gb5JkY8HHg65OXlT4MEI6gVGTyLU4JN2E0BPzAXgbJnV39EOHePIL6aHX9odSyDWTQ/640?wx_fmt=png)

6.接口代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUeBIuTpsS9Gb5JkY8HHg65pnp8NrtFD0lESGJfTRxXoqw4Gmbro1NUVYAMAHWFT6Kglh9SETB4MQ/640?wx_fmt=png)

7.干掉进程，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUeBIuTpsS9Gb5JkY8HHg65icvKAuhx56mZDjFDjiaaM41HGp7X35TtbhvrcTTNIReWSwrKqiaSyfeDQ/640?wx_fmt=png)

恶意软件研究包含的东西实在是太多了，笔者要分享的东西也太多了，慢慢来吧，有兴趣可以加入笔者专业群，与各位同行一起学习交流。

总结结尾

如果对恶意软件分析感兴趣的，可以加入笔者的全球安全分析与研究专业群，一起共同分析和研究全球流行恶意软件家族。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmXDIda3D6VvFWhqojST24E2rTRBJMYDfYowK8WcvBScfWlJiaYZ5elMdlrREG1LDVODxFQ0Eoy0YLQ/640?wx_fmt=jpeg)

安全分析与研究，专注于全球恶意软件的分析与研究，深度追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmW8qYF2seSKglWFKoJdassltn5V5IPUn3OGXsdD4v2nRPg8ZzFAicpXlmlwVmd9KTm4XPkRcXtBEKw/640?wx_fmt=jpeg)

王正

笔名：熊猫正正

恶意软件研究员

长期专注于全球恶意软件的分析与研究，深度追踪全球黑客组织的攻击活动，擅长各种恶意软件逆向分析技术，具有丰富的样本分析实战经验，对勒索病毒、挖矿病毒、窃密、远控木马、银行木马、僵尸网络、高端APT样本都有深入的分析与研究

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