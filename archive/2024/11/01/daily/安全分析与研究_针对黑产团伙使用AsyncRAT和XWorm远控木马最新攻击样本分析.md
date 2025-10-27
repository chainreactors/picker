---
title: 针对黑产团伙使用AsyncRAT和XWorm远控木马最新攻击样本分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247489381&idx=1&sn=c4d6ab859ac03c71c553e73c5e94ec7e&chksm=902fb84da758315b13169f1e6d3aaed12f4deeed8b9dc050e2bb4a155fc3c5960627dcb760e9&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2024-11-01
fetch_date: 2025-10-06T19:17:40.473174
---

# 针对黑产团伙使用AsyncRAT和XWorm远控木马最新攻击样本分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEzscC23ibB1FIx58rM27vLbia9P9qDt4Rv1Gr2JP9CqyeqVqZc3M2jPAA/0?wx_fmt=jpeg)

# 针对黑产团伙使用AsyncRAT和XWorm远控木马最新攻击样本分析

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

原文首发出处：

https://xz.aliyun.com/t/14473

先知社区 作者：熊猫正正

近日发现一批新的钓鱼攻击活动，黑产团伙直接使用AsyncRAT和XWorm等远控木马黑客工具，对受害者进行远程控制，进行网络诈骗等攻击活动，笔者对这批样本进行详细跟踪分析。

样本分析

1.样本一伪装成Microsoft Edge程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEV60ibvBa9CeCC7brAHoJ8CJZ5VlbduDvrHNfNIAPVnhdqjMwDVoIhFQ/640?wx_fmt=png)

2.编译时间为2024年5月12号，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEDic0PfxC8AjfzH8usX3J1PAon01RWkxXszL7c6DbEEXWRiakaluP2ESw/640?wx_fmt=png)

3.从网上下载ShellCode代码，并加载到内存中执行，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEJ0IqPB6W5fFBXpBZb50EWFjFVJ2W7e2ic2SUYMuR6oialMXtb8lY5QCw/640?wx_fmt=png)

4.远程服务器地址和端口为123.99.200.160:6428，下载的文件为160.bin，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEnMpSzqyESCtianS971N5JavhyQrNErW4dXT10RdV2Kob0BNoXcCSPbA/640?wx_fmt=png)

5.下载的shellcode代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofE1ckTzZmqUibnHNnEvBs5dRwxLGWX59WzuHPJwPMQ7ILMt9wfia0HsGiaQ/640?wx_fmt=png)

6.获取VirtualAlloc函数地址，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEcwfxLJrCPDlEGLE82lYGAicNdv3Kl1W0OTWbvJTMDKctbOQM2DZGUhw/640?wx_fmt=png)

7.分配内存空间，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEqv0Xv9woicZdzS7EsfhUnBgJgFy6zlBERLo3O9XgeXp31sRiczBzt1BQ/640?wx_fmt=png)

8.将shellcode中包含的加密数据拷贝到分配的内存空间，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofE53DAoDskuzZt9HrthYgxwlBl8V3lt2bpWfvfMVmgOkibe5NNyIC7bCg/640?wx_fmt=png)

9.解密加密的数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEbhVOVt1neG834TrOxhDlShUWNRLpQ22xicrp436CdMcbV1T3f2JzHTg/640?wx_fmt=png)

10.解密之后的数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEO2yG55h1Mibu44dKOxnVcrDrKztIfHm4KUYSmd7NrVzDaXtB21KhBxw/640?wx_fmt=png)

11.通过Patch AmsiScanBuffer函数来绕过AMSI内存劫持，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEPhqtNeCjfWakHxTz984k63ibtvV7bq0yBxzLINHiciavAEUqLSFF6fia5A/640?wx_fmt=png)

12.Patch AmsiScanBuffer函数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofE4NCPPYyIvibgUmWibYzFJ5zQUuRaCbKx1eUpt9icDdJczp0YX2ejpYeUQ/640?wx_fmt=png)

13.Patch之后AmsiScanBuffer函数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEwSmFcnuRZR4uTAoAHiciaAsmqgBR8aqw49PW8c5FvF9nT1cN1ia2q9icsw/640?wx_fmt=png)

14.通过Path WldpQueryDynamicCodeTrust等函数绕过WLDP机制，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofER5zOxicjHonyuxHfiaiaib9F3fpgfBZP9ClAMphRGhmVdPX0s1wug1WLBQ/640?wx_fmt=png)

15.Patch WldpQueryDynamicCodeTrust函数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofE5chsSE9xD3yy92ibvnwRAD4HHedo91fOeCkiauoANaKmcz4VFuVNKbDw/640?wx_fmt=png)

16.Patch之后WldpQueryDynamicCodeTrust函数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEZicgxV6PKELZKvMsR0xxUiaklSaJRiciaVWrpcr2EOibibKTdC50qwpRGmiag/640?wx_fmt=png)

17.Patch WldpIsClassInApprovedList函数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEzrJyuYMBTrL4z0yO4gLiaX1oLszraTNBtB1mXYvHBKWzeU6oT9icIFUw/640?wx_fmt=png)

18.Patch之后WldpIsClassInApprovedList函数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofETGrfDY5Ho5z8Ugy4ibMtIgXxLicnrlUkzjib7cxiaibp1Bd1vBPxKrhhiazQ/640?wx_fmt=png)

19.在内存中加载解密出来的NET程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofE1xgvictOcAGGUXenOq5dZ7enAH3coNwfYk6ym5txLWictGxDdCSIdWjQ/640?wx_fmt=png)

20.解密出来的NET程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEyapeXMkhicFoNzC1uI9RyCu7AntR4IibaLuNvox9eKkP1NmuNG3tDKrw/640?wx_fmt=png)

21.此前分析过该家族样本的，基本上一眼就能认出这是AsyncRAT远控，远程IP地址为123.99.200.160，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEib8WtKsgxSZUKmDxgOsfMIZiaS4AntWRhEKGcUqSfYkQNp1r58icWRaFQ/640?wx_fmt=png)

22.AsyncRAT远控是一款开源的远控工具，笔者从网上下载到该远控工具，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofE1ZDWfOuaZvka4qhpiaicvBUdYib5yS3m35900F8Nxs1so8ut6KREkm3tw/640?wx_fmt=png)

23.工具运行之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofE7SqYLiaE3KzRLbg0uuPRtKqZswK4jHuibDQRkhL3WOXkHe8UtGkNgEqg/640?wx_fmt=png)

24.笔者利用该工具生成一个服务端程序，然后反编译服务器程序，可以发现代码结构与上面解密出来的NET程序，基本一致，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEOAoVRPHf6XbmRdiajlicRxTFUQsvdRFOTDbban3oIrgagScyAgExL29Q/640?wx_fmt=png)

25.样本二的编译时间为2024年5月8号，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEwEXJ1O0BH5YRmVz4YgwkX7K9nTVUqtSGwomy1EicuMsHq5yIhINCMoQ/640?wx_fmt=png)

26.样本二主体代码结构与样本一基本一致，从远程服务器上下载ShellCode代码，然后在内存中加载执行，远程服务器地址和端口为154.38.121.174:80，下载的文件为qwe1.bin，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEYD7UJt1O8BDQC4CuaUdJVDMwAH5Hick5KN9wDlNHroDsvxMGDo4recQ/640?wx_fmt=png)

27.下载的shellcode代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEbfzCYZRTUOwQibiafHOArBXzLibIFwl8Lbgac2P0lqhyP9l8wqyTc5LCg/640?wx_fmt=png)

28.获取函数地址，分配相应的内存空间，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEDQT9dI6Fog1M5msBic01MgWHyhx0ble51cDK00O3H0SMQ7XibEV65VOw/640?wx_fmt=png)

29.与样本一类似，将ShellCode中包含的加密数据拷贝到内存空间，然后解密，解密算法也与样本一类似，应该是同一套框架生成的ShellCode，解密之后的ShellCode，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofE8EDAlhpLuGTf20QLwOX9dmkWQrEpQ8YQwdXHNlBP47t3jyRG7icmlTQ/640?wx_fmt=png)

30.解密出来的ShellCode执行过程，与样本一中解密出来的ShellCode过程一致，在内存中解密出来的NET程序，编译时间为2024年5月9号，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEzPT3AEe6iaBkxsELo99ARDMcsbRCRnv839fYRsXyoECAZwSia2BTyPgA/640?wx_fmt=png)

31.解密出来的NET程序经过简单的混淆处理，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEvcBwP3AtFiafibvv4ibK2NbpEz3R8AHSNmppgXPTfDfr9fysr705R4Ajw/640?wx_fmt=png)

32.此前分析过该家族样本的，也可以一眼看出这是XWorm远控木马，动态调试该远控木马版本为XWorm V5.6,如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEZI2OeMWEsBiaT3UpaMnxAJwyKZ4fBlKR1ZpagL3icqexXHNs9vMlceLA/640?wx_fmt=png)

33.远控服务器IP地址为154.38.121.174，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEDd4QAe1kiceTfdljN25tOqRPaFObcQrWW0TIVYsCP69VVkMRP94g0QQ/640?wx_fmt=png)

34.笔者拿到XWorm 6.5版本的远控工具，运行之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEEibKkuXqLSx0ySM4tqUA0zzfOHfALSJA8b66hEejtsaic2fGKwLGn6Nw/640?wx_fmt=png)

35.生成一个混淆后的服务端程序，与上面解密出来的NET程序，程序的代码结构完全一致，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEzvicf4s8icicen6VDibm6rrvZ0icNM2og7sUXUbzNH2eemHLNuCnuwnZic8A/640?wx_fmt=png)

可以得出黑客团伙就是使用XWorm 5.6远控工具生成的混淆的木马服务端程序。

威胁情报

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUapCiaUxG5vHOd3RzTyUofEwH2bep7QUHboap0MoGgWficbQXtianoq5OFNV8ye3gDpN9oUbMic5Bj2g/640?wx_fmt=png)

总结结尾

今年各黑产团伙仍然非常活跃，去年大量使用Gh0st各种变种版本远控受害者主机，被统称为使用“银狐”工具的黑产团伙，之后也曾发现使用AsyncRAT远控，现在开始使用XWorm远控，通过跟踪可以发现黑产团伙仍然在不断更新自己的攻击样本，直接使用一些现有的RAT远控木马，以及免杀加载器等，不断降低自己的攻击成本，以寻求利益的最大化。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3R...