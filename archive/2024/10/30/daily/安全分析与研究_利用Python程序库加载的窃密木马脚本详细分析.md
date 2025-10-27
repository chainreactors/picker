---
title: 利用Python程序库加载的窃密木马脚本详细分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247489299&idx=1&sn=490ef891c029eb532897fdea93a7c902&chksm=902fb83ba758312d97abc5327ae5d9ad3cc4c88765eb5b28feec6861ebedd47fe787b7f0003f&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2024-10-30
fetch_date: 2025-10-06T18:52:44.152672
---

# 利用Python程序库加载的窃密木马脚本详细分析

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDpibP198wvxiagDC73Ap9iaQ4c7avCHJpibe1Nq24tp4d7w3CvNbZc0p3nA/0?wx_fmt=jpeg)

# 利用Python程序库加载的窃密木马脚本详细分析

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

原文首发出处：

https://xz.aliyun.com/t/15963

先知社区 作者：熊猫正正

近日，笔者在逛某论坛的时候发现一例Python Stealer窃木马，下载回来研究之后发现有点意思，分享出来供大家参考学习，切记不管是使用什么程序或工具，一定要从官方下载，千万不要随意打开和使用非官方的程序或工具。

详细分析

1.从gitlab上下载相关的样本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDc37dRBqRgxQqK24Q7OAGpCDruw2TyAibBvsNoleKjEOgY1D5TNicz1mA/640?wx_fmt=png)

2.下载压缩包样本文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDDuOUKIsnJribrKfUUL1iazXzZxnpT5mbCRgfxIxR79lv1gJNLgicwpNUQ/640?wx_fmt=png)

3.解压缩文件之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDibgQguGia4895DfUqgNLLuqRT0HS6cBRialKNA1AicOkroSwGicFE0icg0Sg/640?wx_fmt=png)

4.通过分析发现压缩包中的二进制文件都是正常的，难倒是样本下载出错了，传统的套路不都是白+黑的方式吗？进一步分析发现恶意代码隐藏在Lib库文件下面，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDoLYCYrfib9vaSxVXS7IAHuR9rZ6s5pEyqkQ3NyR23WsWzNYJd3AWnnw/640?wx_fmt=png)

5.通过ipinfo.io网站获取主机用户名、所在国家地区、时间戳、IP地址等信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDaX7SNZbv8aj3eEhJUKKdL4mYVHqzMJeFS1OgzMDmSgOfIrWDoCUicIA/640?wx_fmt=png)

6.收集FireFox、Chrome、Edge等浏览器相关数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDc5wHoBb2WIfPKSaXgxKncP2GBWSiaS8EIT0O9TgYv7diayJibL4MRZiaBA/640?wx_fmt=png)

7.获取FireFox浏览器登录信息、Cookie数据、密钥数据等，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDdibulgvpgIcbibE1qvGNlWHNkFjZiaUbnmXkymibY6DXLUicqtKg2ick9lgg/640?wx_fmt=png)

8.获取Chrome浏览器登录数据、本地数据、Cookie数据等，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDcCEoOPlfWMfprTt6OSEnIBGLJaVB8jvcLNon7fib3JvmCHiblACbYXYw/640?wx_fmt=png)

9.获取Edge浏览器登录数据、本地数据、Cookie数据等，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsD1yBic26Ec03l5ztP2bIW4VZfst2iarzicPFy3dJeebXLOLMSzWR86Xtkg/640?wx_fmt=png)

10.获取FireFox登录数据，解密出登录的用户名和密码等，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDrhIGxyIj4ibSAIiaIBfN1Egfn05tiasgdQeNuWI99fBJwCIZ3eSoUdrVw/640?wx_fmt=png)

11.解密的过程，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsD5s22a0MOC2Pje4ltJw7BNNwoIJGaTe1BS3Pg5zKCGs87OWfLnK1LIg/640?wx_fmt=png)

12.解密的时候需要用到加密的Key信息，获取Key的数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDHjicF7G72LqZ7UWOmlJB9Lrl3vQXSQb0TnFEslKDGaAOkxkFyTIHN2g/640?wx_fmt=png)

13.获取FireFox浏览器Cookie数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDfKR8q5ZW3zMynfxYpwRrwiccW51I4wfCSsA0GYkfJqcYAlF6NQyibySA/640?wx_fmt=png)

14.获取Chrome、Edge浏览器的登录数据，解密出用户名、密码以及访问的URL，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDtuQQd81ic3iaYgbVVkHn9I5HHbLicqnMkbDReJmrPttVzHqaNHhviavmGA/640?wx_fmt=png)

15.获取Chrome、Edge浏览器访问facebook、google mail、microsoft等网站的Cookie数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsD0siaWEEHNlWibJJfBrooDzwDPAE8waPibeasPo8YL9lcul3eqL2vPibXSQ/640?wx_fmt=png)

16.通过获取的Cookie信息，获取Facebook网站商业数据信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDCMYu2EeRh5Cy6DTibeX7csqicbF5udWmwlsiaKhGqZ5PgggXjRibWoP9bA/640?wx_fmt=png)

访问的网站为adsmanager.facebook.com、graph.facebook.com、m.facebook.com、business.facebook.com等。

17.然后在%temp%目录下创建相应的文件夹，文件夹名按国家地区+IP+时间戳等信息组合而成，获取的数据存放在对应的文件夹内，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDhaNZbDcOiaCmkJlHB8VvbNCQSdMVXeab0tykzC3uA4VBAuX0tyAZrnA/640?wx_fmt=png)

18.例如获取的Chrome数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDG5WYeWt5HfHUpekjZ7vpibGg3LYAu7wsJTVC8VnqxGDicPqaQugB93kg/640?wx_fmt=png)

19.将文件夹打包成ZIP压缩包之后，通过Telegram API上传到指定的Telegram Bot上面，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDNQpbZOC8xLnXoSuy9VrsVFrhFsaajV8S5PJhQcUU8TDhrw9mRQBrXA/640?wx_fmt=png)

20.Telegram Bot信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDAaAgG1MQojcsCsl2hs6nVrCqt8crG4WI92LUiaR9VMXPSVDkycA66Cg/640?wx_fmt=png)

到此该窃密木马就分析完毕了，都是源代码，不像二进制文件需要反汇编啥的，分析起来基本没啥难度，流程也非常清晰，没有混淆加密处理，但是这种加载方式有点意思，不是使用白+黑的方式，也不直接调用恶意Python脚本，而是通过python程序库来加载执行窃密脚本，由于涉及到的文件比较多，如果不仔细审计源代码很难发现。

威胁情报

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDxvTngdmo696AbPTr9Xe01VQDdHKLialrkyQsbibHFAQoxl4xZk6xsYicw/640?wx_fmt=png)

总结结尾

黑客组织利用各种恶意软件进行的攻击活动已经无处不在，防不胜防，很多系统可能已经被感染了各种恶意软件，全球各地每天都在发生各种恶意软件攻击活动，黑客组织一直在持续更新自己的攻击样本以及攻击技术，不断有企业被攻击，这些黑客组织从来没有停止过攻击活动，而且非常活跃，新的恶意软件层出不穷，旧的恶意软件又不断更新，需要时刻警惕，可能一不小心就被安装了某个恶意软件。

安全分析与研究，专注于全球恶意软件的分析与研究，追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLreq5DibibsFm4BFFlh7Rjd8xq8mVSQcnmbYljOxPdRu6cGViap4YugvcDgQ/640?wx_fmt=jpeg)

王正

笔名：熊猫正正

恶意软件研究员

长期专注于全球恶意软件的分析与研究，深度追踪全球黑客组织的攻击活动，擅长各种恶意软件逆向分析技术，具有丰富的样本分析实战经验，对勒索病毒、挖矿病毒、窃密、远控木马、银行木马、僵尸网络、高端APT样本都有深入的分析与研究

预览时标签不可点

阅读原文

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