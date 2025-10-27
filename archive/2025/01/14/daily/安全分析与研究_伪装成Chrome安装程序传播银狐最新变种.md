---
title: 伪装成Chrome安装程序传播银狐最新变种
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247489956&idx=1&sn=91861b57be376b8d6fa0d075edf1d6b6&chksm=902fb68ca7583f9a4714da177a1e775f3170d9875f63c7e39f99f27ff826fa2f22f3cec354c2&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-01-14
fetch_date: 2025-10-06T20:10:55.727553
---

# 伪装成Chrome安装程序传播银狐最新变种

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAterhJzLr5dpE09Q6bEIFYz2LmecUDl8ozZibuOnjE1O51nQehJOojEg/0?wx_fmt=jpeg)

# 伪装成Chrome安装程序传播银狐最新变种

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

原文首发出处：

https://xz.aliyun.com/t/16989

先知社区 作者：熊猫正正

近日，笔者捕获到一例伪装成Chrome安装程序传播恶意软件的最新攻击样本，对该样本进行了详细分析，里面的恶意模块都使用了增肥和无效数字签名等技术，以逃避安全厂商的检测，同时还有一些反虚拟机检测，样本中包含三个ShellCode恶意代码，还利用了一个开源的注入工具，会通过系统中的相关安全产品信息等，使用多种不同的方式注入加载执行ShellCode代码，分享出来供大家参考学习。

详细分析

1.初始样本伪装成Chrome的MSI安装程序，相关信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAZ9aPaKVQ0erbTmmUBwAg56UhbDdNySzghibptUKLXnwuaD6R1icbQJWw/640?wx_fmt=png)

2.解析MSI安装程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAxicS8OkrgkQEcFlibv6EibvPpeOZQDNmx0cBwkH86z0Ig37zumXDw7pPg/640?wx_fmt=png)

3.CustomAction安装脚本，调用恶意模块的导出函数exitzi，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAnuu0XjHZudyrN39PeHwVIpVSCTReH6Jcrs2Hcoe2B1whAC48ibz2IEw/640?wx_fmt=png)

4.MSI解压缩之后，包含恶意模块，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAic3STLPiaAl484EolvshJaIg1LjSBRHde6kdvR9stT8Ez9a5H6zTmhwg/640?wx_fmt=png)

5.恶意模块带有无效数字签名，数字签名信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAiasDMVceae1V6I68NKlicficCQuzsHwKHQDhlgLyibvkkUys6iaNKc8dL0g/640?wx_fmt=png)

6.恶意模块使用了“增肥”技术，大小为二百多M，在DATA段中加入了大量的垃圾数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQA2kaib9yLYr2wvvEmPKnyb0ooh7jWf7phuSicDCibrpGBJnGIgibBrpCI6Q/640?wx_fmt=png)

7.恶意模块的导出函数exitzi，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAZ4w4FH8Pag9Z1YcD2n1kNIhAoAlpVERVe5ZZ2B60XFNWf5pmK59mDw/640?wx_fmt=png)

8.在指定的目录生成压缩包文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAoPHnWD1XMjsXzib9QooLpiaTxia2hO0He6IDkRccAdjv8vxBicauPVWd2Q/640?wx_fmt=png)

9.生成的压缩包，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAKwQ5kOPoLT58s5S9ysZNshPc5G630jYkicz6wNvqakVbI51UzHrm74g/640?wx_fmt=png)

10.通过遍历进程等信息反虚拟机操作，然后通过密码解压缩文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAWRTshxTDWYq2aUIyicQAh5ImqfJyoXJTq1UZ25FxRVM1U6qKcN8G75Q/640?wx_fmt=png)

11.解压缩之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQASfQhhYhYsme11On2llzJIfz1V0yZvMeb2ZJpCic8730Sz5ZBrEiaibnzQ/640?wx_fmt=png)

12.里面包含的恶意模块同样使用了相关的无效数字签名和增肥技术，模块大小为四百多M，相关信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQA0uflZmOABPVybSZAWu1R7pNwT2PibXv6xN41xS6yzQdh4cgr3GgTGUQ/640?wx_fmt=png)

13.同样使用白+黑的技术，加载恶意模块，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQA1uXiaictasTPic3HictRbRIPMoERPmbzuGqrcsKQvsvkJH48KnuWP6nh2w/640?wx_fmt=png)

14.判断主程序调用参数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAxKFWnOU7IQuQqrNNLG7yibD98Z6fyPxolQXticL3amPEBLVF6utvME3w/640?wx_fmt=png)

15.如果参数不对，则启动主程序并调用参数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAWk8PZSakyJ5CJk2o0WpMSdCicn4Zuqbnzz0rTe4bDaa9CFN59kMJib1Q/640?wx_fmt=png)

16.判断是否存在hh.exe进程，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAn2ZMRqx4wae5IytibvWl3f5RI5gKN5m71SP7RrYrhBz7yWh6hYBatSg/640?wx_fmt=png)

17.如果不存在，则启动hh.exe进程，然后读取view.png图片的内容，然后将shellcode注入到hh.exe进程当中，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQA3lMVL66tmHK1md7rZRTiaDVgBVqY6etT6koevobTTLJHMQtFhJWR7ibA/640?wx_fmt=png)

18.注入ShellCode代码到进程当中，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAofdSoM6zC4WH3U5fiarkru6gTUC1pHyolI7iaKIMek25eftCqgAt9hvQ/640?wx_fmt=png)

19.ShellCode代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAHGEBHkq98BX7nyYM6gt3pWTRwoJosgBoPbuNiaTiaH7HWiaQl594GIEqg/640?wx_fmt=png)

20.判断C:\users\public\downloads\目录下是否存在aut.txt文件，读取aut.png图片文件中的ShellCode代码，并执行，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAKk4lWTAjhvHw8aWTGMEVs4fpL4eQdqg6f2fgqLwf3CPEicRvd31UL4A/640?wx_fmt=png)

21.读取PNG图像ShellCode代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAaqjicUhYwhjZ4y5kIRYW7F4h9HoupeykWNyicRN1fOGzhga3BGdXqicuw/640?wx_fmt=png)

22.ShellCode代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAUyic0jsH3CZszDeApoV69yq7icIhgibUK1EwFgkicPJY2wc6NKUefibcqTA/640?wx_fmt=png)

23.下面来重点分析两个PNG图像中包含的ShellCode代码，先看view.png中的ShellCode代码，分配相应的内存空间，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAqWr9sR8V8mc4NKyEzryMaVHQl4MY4nM8tk4lQticHJ3csCCw4TmNVPA/640?wx_fmt=png)

24.拷贝ShellCode中的加密数据到内存当中，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAIsgAvCR5BX6HUbUNEkju8OUmicI0H8ckHmsEjjBLLRJ18lmEsgYTz3A/640?wx_fmt=png)

25.解密加密的数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQA0kYM5reMFg5eskvvicpdx6jFjVlAKgsppKDibjtMRVNAfx5DKqywibCzA/640?wx_fmt=png)

26.解密数据之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAUPTOQnkkZCDoD84X67ogiafgafpcnCvvXPfzSxjAG2A1RRyIcItIFCA/640?wx_fmt=png)

27.PayLoad的编译时间为2024年12月13号，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAb4ttNeZkTMcgZAunTPnrZIPeeibO0IYrB8apicuCL6yJ3tjH1SaEmibtA/640?wx_fmt=png)

28.解密出来PayLoad的应该也是银狐黑产的一个变种样本，相关的C2域名信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAUsbocYuGK8VJwRV1zg8Ho1RbH4jkjZZBl6VlNn8L0iaiagbn8NNk6NNA/640?wx_fmt=png)

29.解析C2配置信息，与此前银狐样本类似，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQA0YuYjcVGtQgSEyKqG6u9ohDfjzUicoTEnTickcWWOAaHrhfxr3JvQHJg/640?wx_fmt=png)

30.通过分析aut.png图像中ShellCode代码功能与上面view.png图像中ShellCode代码功能一致，但解密出来的PayLoad不一样，通过分析该PayLoad引用了一个注入工具的代码，并会将ShellCode代码注入到explore.exe进程当中，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAQ6WCh9Kjyz0Y0ea3B5DgUjYiamDtV4YkhocL8avffvvchnlPAbCtAbg/640?wx_fmt=png)

31.代码中包含的PDB信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAQWsP6XSb4yhficHZLAKufdtPC0TicyXSDylTEkVm9YlNINxD4ib33L4ow/640?wx_fmt=png)

32.注入进程过程，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQA8sbco71Ioibz83pvJFF8PL4ib5XOr9DYS2prGelQsiacG3rPCpttpYnkg/640?wx_fmt=png)

33.注入到explorer.exe进程之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQANP98TiaLibOwH9qHYhNzfjGHOh9uSSBq6QQ8X2l0qpmBgPcB3ImqEAUA/640?wx_fmt=png)

34.注入的ShellCode代码与上面的两个ShellCode代码的逻辑一致，分配相应的内存空间，然后将加密的数据拷贝到内存空间当中，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAc7uQKdevcXFDE1KlFcAbkdu9s46TpTDlcZxpPGNjUU0rlcwmicAobPw/640?wx_fmt=png)

35.解密ShellCode代码后面的数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAQtBJiaKjED7d1LkVReBoib4aNAFS52Uw1nagX4QiafYiajNic1BYHgZZHJg/640?wx_fmt=png)

36.最后解密出PayLoad，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAOMWaMsibHFwphCL0l8xiaAxNRz9ic6163jOxT5o81umsgMZAJ9X2MCjBg/640?wx_fmt=png)

37.最终解密出来的PayLoad，查询相关注册表项，设置快捷方式等，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAtLNANZLyiac8gia317N5VADsBppZxJ9GxIAfrO3hh4R3fFz4JYvGrBJw/640?wx_fmt=png)

38.设置自启动注册表项，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAZx6Vfokrg9m8H0gHYSMIdrne7w7Hvm0zWP3j9BoKFQtibtPoNBVbYnw/640?wx_fmt=png)

到这里三段ShellCode基本上分析完了，三段ShellCode的代码结构基本一致，应该是同一个框架生成的，两个图片中分别包含一段ShellCode恶意代码，其中一个图片中会解密出另外一个ShellCode代码，并使用开源工具注入到进程当中执行，一个图片中ShellCode代码最终解密出来的PayLoad核心应该为银狐的最新变种。

威胁情报

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAvHGOwpiagqL6QeW0ScSyGIo9vFngs8dvryfFZFjUBa6xLBa7t9ibJibibw/640?wx_fmt=png)

总结结尾

黑客组织利用各种恶意软件进行的各种攻击活动已经无处不在，防不胜防，很多系统可能已经被感染了各种恶意软件，全球各地每天都在发生各种恶意软件攻击活动，黑客组织一直在持续更新自己的攻击样本以及攻击技术，不断有企业被攻击，这些黑客组织从来没有停止过攻击活动，非常活跃，新的恶意软件层出不穷，旧的恶意软件又不断更新，需要时刻警惕，可能一不小心就被安装了某个恶意软件。

安全分析与研究，专注于全球恶意软件的分析与研究，深度追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmUFuaUxnXJueQzIgFvKDDQAMNWnNxuKxOiazwV340ZWLNabkxDjrO...