---
title: KoiStealer窃密木马最新变种分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490812&idx=1&sn=448abaf77070a2c7b85ca73dbbc9ab2d&chksm=902fb3d4a7583ac2456a8c7a0eaa64a7dba86b9adb1d0770abe9df475012eff99601dfd9bf8b&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-03-01
fetch_date: 2025-10-06T21:58:43.589193
---

# KoiStealer窃密木马最新变种分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmU7T5UuMFWZC9yaGjPMiapqIzUHHOt1JbAUgOCiaNicEOfQKf3Gren18WFWia0tibOOLlNsrZic6kcMY39g/0?wx_fmt=jpeg)

# KoiStealer窃密木马最新变种分析

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

KoiStealer是一种新型的窃密类木马，攻击者主要通过钓鱼邮件进行传播，该窃密木马能获取受害者屏幕截图、浏览器中储者的密码、Cookie等数据，然后利用盗取的这些数据，对受害者进行更进一步的诈骗攻击活动。

该窃密木马整个攻击链还算是比较复杂的，笔者曾完整分析过该窃密木马的攻击链，相关的报告：

《伪装成花旗银行对帐单的窃密攻击活动》

《KoiStealer窃密木马最新攻击链样本详细分析》

有兴趣的可以去参考学习一下，下面笔者给大家分享一个最新的KoiStealer的变种样本，样本可以从https://malware-traffic-analysis.net/网站下载，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmU7T5UuMFWZC9yaGjPMiapqIwJ1ib4lTnQYJvnbichSxfx72vFU6pRiciciadRI6ibKeSH6g9eEAtaCfMZCQ/640?wx_fmt=png)

样本分析

1.样本采用C/C++语言编写，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmU7T5UuMFWZC9yaGjPMiapqIqbicxoTf9h9iaYxNJdRvylXRO1MoZqJJwXrXUpAEng8Kfl7NaquFPZfg/640?wx_fmt=png)

2.入口函数代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmU7T5UuMFWZC9yaGjPMiapqIK75n3Utj88xTK688PmphM9Xqehe3DkoqYXlAU0JXNmXjxJicPwenhzg/640?wx_fmt=png)

3.获取样本资源加密数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmU7T5UuMFWZC9yaGjPMiapqIArBqTRhDKapuny2cedykiafBBMPV6ia22u8SJRemtIIBwSJicPgRc6uNA/640?wx_fmt=png)

4.将获取的资源加密数据加载到内存当中，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmU7T5UuMFWZC9yaGjPMiapqI6R2YR1Dxibibmo5VSQfEtJ03vziacLlFGiaNNJUqWWXXX3gglFIQdhicglA/640?wx_fmt=png)

5.将加密数据拷贝到另外一块分配的内存空间，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmU7T5UuMFWZC9yaGjPMiapqI8qrarCFHdIdpjGdsqeY3yhjCticNicG0EJ33kG9fgWhbrek8DsPzJpyg/640?wx_fmt=png)

6.然后解密加密数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmU7T5UuMFWZC9yaGjPMiapqIOV6ibTtHTw6fetLImG1SZgovSiaIh4f6dnzG6rxcLicN7tCpX5XvExqMg/640?wx_fmt=png)

7.解密之后获得PayLoad，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmU7T5UuMFWZC9yaGjPMiapqIbiabVLa8scCibjibCibyPyzLvuWJ8zoSArsiaibX59Mo6WfFWSqEP8GJibt6A/640?wx_fmt=png)

8.PayLoad主程序入口代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmU7T5UuMFWZC9yaGjPMiapqIeKb2pmNYP4PrBBeLoNv9hO5uRWpAu56JmYz2bFvZVOhGR0GMASnvBA/640?wx_fmt=png)

9.里面有一些反沙箱操作，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmU7T5UuMFWZC9yaGjPMiapqI3tUEFn4hlWHwKbdAmzzSCeXNJ510d7lNhm9MJXMhasXcyWaYlTKvlw/640?wx_fmt=png)

10.下载执行后面的PS恶意脚本，与此前笔者分析的基本一样了，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmU7T5UuMFWZC9yaGjPMiapqIOsjuqTWdZerOtUibcCibVTdlVFB1ichntkaEE9nW12r3RGicmNmQibEwkzw/640?wx_fmt=png)

其他分析过程省略，笔者只对其中的一个Bin文件进行了分析，里面就包含很多功能分析点，完整攻击链的样本比较复杂，可以自行下载研究，有不懂的参考笔者之前的文章。

总结结尾

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