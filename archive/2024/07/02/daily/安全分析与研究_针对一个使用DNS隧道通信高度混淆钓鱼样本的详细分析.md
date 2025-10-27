---
title: 针对一个使用DNS隧道通信高度混淆钓鱼样本的详细分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247488439&idx=1&sn=2d98183fd07377dcfef2011034f7782e&chksm=902fbc9fa7583589d2005a5c58704d609d777086b008a1ece3947cf73373e06a504c49bfcaf0&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2024-07-02
fetch_date: 2025-10-06T17:45:32.546776
---

# 针对一个使用DNS隧道通信高度混淆钓鱼样本的详细分析

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmW5GgUud9AGrujrAltULWBF5MAtZyEqWbHiazvFR31PUBBKSacZwCz8Uoe7RtuylsicGD9CZ0ka3aibg/0?wx_fmt=jpeg)

# 针对一个使用DNS隧道通信高度混淆钓鱼样本的详细分析

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

原文首发出处：

https://xz.aliyun.com/t/14825

先知社区 作者：熊猫正正

近日在某个交社论坛上有人公布了一个有趣的钓鱼样本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFA0Zs64xEicokVjvsyBaq0DTHia6Qmbx89YibkKsTPNn1Uicb9FJl3K51yQ/640?wx_fmt=png)

从公布的渠道下载到相关的样本，对该样本进行了详细分析，通过分析发现该样本感染了正常程序，这也是之前常用的一种恶意软件攻击方式之一，分享该样本的详细分析供大家参考学习。

详细分析

1.样本伪装成简历以及专利相关信息，对公司的HR进行钓鱼攻击，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFvzK7icQFxNIvoVycJRyMEuulNZmlF36fZpPTAVJStpkxM3eIfyt4AyQ/640?wx_fmt=png)

2.样本的编译时间为2024年1月9日，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFUg0dJT9Tjh0Aj9HAKh0kTvl5iawvj87WOBRib3mX5FEWWS0NPqbKJAuw/640?wx_fmt=png)

3.样本信息显示为腾讯应用宝程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBF1hXNJ1Elfpht2U0nSdIAiaz0eaQ17cwp2pF5v6uUWFxwg66skxTlVzg/640?wx_fmt=png)

4.样本的PDB信息为腾讯应用宝程序PDB信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFOZt9Lb2nZnEchcKhSUCMfGU3EqPpA6niaydgOVqM1zmTyRL6q79TzPg/640?wx_fmt=png)

5.猜测样本应该是修改了腾讯应用宝程序，查看样本的入口点WinMain代码，与腾讯应用宝相关程序对比，未发现明显异常，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFJClPxE3yO9LdHqRHyXKRY6h2RYWriaaCVBq8kkt7pkJI33Aq7fNCCqg/640?wx_fmt=png)

6.通过分析发现问题出在\_\_scrt\_common\_main\_seh函数代码中，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFccSSF2kTy7U0mT0ZWSWT5dmtT04h3icjpl7WuVXffDny4w0sW9ewgiaw/640?wx_fmt=png)

7.\_\_scrt\_initialize\_crt函数代码被替换了，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFprCrzewTia6lF0fy3nIlBeib1KRibibNKia6st3chic7nNOE9fVaibib5ugR8w/640?wx_fmt=png)

8.动态调试执行到ShellCode代码处，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBF67pDaYNibJiaaibVO3RbghRiceYs0pia9HRICCWCFlU6iaSdGIbhSrobGfxw/640?wx_fmt=png)

9.设置程序资源数据的属性，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFgBEMEx5UaTQibmxuGf0bM1GcnFMENoCnvHVV3dffu8LQHVxVmWjabUQ/640?wx_fmt=png)

10.样本修改了腾讯应用宝程序中的资源数据，增加了加密的数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFCTnkatNnSnVsIb0MGSU7guicP2tQia0bm1nrYwNPACC7waDfh53Obabw/640?wx_fmt=png)

11.ShellCode代码解密资源中的恶意代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFu10Xvj1bugqmuasRp6R7aOpLiblAef8wqrynDxjQNyMc4tljiaAhWBEw/640?wx_fmt=png)

12.资源中加密的数据解密之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFOq9vokmJctvILDWB1Mu0He3I51HIQ5XicdaTicNptR36T7iaLJa5kdybw/640?wx_fmt=png)

13.设置解密后的资源数据属性，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFjxestles1MqpAhR4A9mwlcUNhbPxbOG1juJy9zwIdhJ28ryKSfcOzw/640?wx_fmt=png)

14.执行到解密后的资源数据代码处，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFYX6R2tiauhSVxtw8N2CRr3bcb6GfVxIsxjmnhTlDTlytlkrKjDoD1PA/640?wx_fmt=png)

15.解密后的资源代码，包括大量的混淆和字符串加密，加大分析的难度，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFOAedWMI22tnxZNvg7I1fjBHAgh5rarFibnic67WwDTeNLEP7VH91Nv7A/640?wx_fmt=png)

16.设置程序相关字节区段的属性，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFg8qUYJicdWuAWNib7xqkHHB15EYTVic5Rl7B3OtiaPjTSTPF9iaTceyooqg/640?wx_fmt=png)

17.解密出相关字符串信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFUzibQPRWNWpHQWsQiaiaKZmQXwR7OEbKd8hGia1oZRb8SjYojK07RChdVA/640?wx_fmt=png)

18.解密函数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFAmibuQqPVCAcaaQ5rXgO8OkTydMtickrJ2aj4PpxEjbtzhuZTc6iajO0Q/640?wx_fmt=png)

19.获取相关函数地址，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFUTyXHD0cY0sBPnNuFUBovVEsibqzEktt9uYTMoViatdVGibmnOdttAC0A/640?wx_fmt=png)

20.加载相关的DLL，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBF3wCARo2DPyFs4lTVmuWviavicV9r537xicOszfJzgY2yiaiarAKSN1Gt7KQ/640?wx_fmt=png)

21.获取相关函数地址，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFkdjVrduPEp2PKqNRIIEic2WbQRD9gmVGp3ApF7jicMfLc0x8kibu19A1g/640?wx_fmt=png)

22.获取主机%ProgramFiles%以USERNAME变量的值，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFd3sib4HlicurJibI1Tzp2zicpibCcZmic4X94x8TN2PiaBvKvkERPQ683akKA/640?wx_fmt=png)

23.遍历进程，查看是否存在相关的安全分析工具进程，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFMDDT0pia9PWkQicjG8GUF15E1IDosZicVr5HhxzichpSaGzFIVxSWIgjHw/640?wx_fmt=png)

24.相关的安全分析工具进程列表，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFxVa6Ria4vtzKONIz0W9LhKrFeRlE1SCHWttEaeH9g0xiac6WiaOTwP9Qg/640?wx_fmt=png)

25.如果发现上面这些安全分析工具进程，则直接结束进程，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFGqwkeDBkLH1BB33hdDocLwXPFsaPCKA84mh1ykK5OTeUibzsHX2w5hA/640?wx_fmt=png)

26.解密加密字符串，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFzC2T4Nm6EEkg3toQEcoiba8YoNNQU6jg8gtKFfdbiaU376xh93icicD9dA/640?wx_fmt=png)

27.解密之后的字符串，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFklv0PyZxfI2a8fzzNsIBS3jib3FTlJ9bdPHrqM74yRX6dB36WyQtrsQ/640?wx_fmt=png)

28.解密相关字符串，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFOcPBpbeEWt7zePibIKHkmej9hVYAIGZUX7jplziahyCWUiaxTDtWdZ2ng/640?wx_fmt=png)

29.解密出来的字符串，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFeibicbvCTA8BCwKlP9We3Rxq2gtec6AyLTvCXcmxCiaNWsvrZ8DQZSC5g/640?wx_fmt=png)

30.样本使用DNS隧道通信技术，最终解密出来的DNS域名类似，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFbEBnWpaQxrAqGAm5FMicP0rrMyl4iapiaD9WDHtFOd2LGfwQzzH3x2IZg/640?wx_fmt=png)

31.将该域名在威胁情报平台上查询，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFSefSyPKFMXKgVO9YHLdKY3UvzlRBc6457TOluKsmszPKdtvQqtqJow/640?wx_fmt=png)

32.在C:\Users\Public目录下生成一个相同名字的docx文档，然后打开该文档，迷惑受害者，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFGKQmqySvtjz9TH5o0O5iaHxFE2WCLEbIuKZ6VmMatcB0qQ9B1IiaXiccw/640?wx_fmt=png)

33.发送HTTP请求，与服务器进行通信连接，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFO6omY9SwuQ2ugCyoIFibhlIeyp9Dsgqyv74w2SEWejibZOXxm18XQJkg/640?wx_fmt=png)

通过分析该钓鱼样本可能是某红队攻击样本，样本中使用了大量混淆代码，防止分析人员对样本进行详细分析，同时样本通信采用了DNS隧道通信技术。

威胁情报

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmW5GgUud9AGrujrAltULWBFdgSSUkpGiaAorc5K5qMia4mOdMib5ld5qicThpIzF5jz77QaK1Hu9Z5YDg/640?wx_fmt=png)

总结结尾

安全对抗会一直持续存在，有攻必有防，攻与防就是矛与盾的关系，安全研究人员需要持续不断的提升自己的安全能力。

笔者一直从事与恶意软件威胁情报相关的安全分析与研究工作，包含各种各样的不同类型的恶意软件，通过深度分析和研究这些恶意软件，了解全球黑客组织最新的攻击技术以及攻击趋势。

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