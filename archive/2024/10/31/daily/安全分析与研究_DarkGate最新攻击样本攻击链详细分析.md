---
title: DarkGate最新攻击样本攻击链详细分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247489341&idx=1&sn=9fd04e3b13e688b5062bbe735e62ad4c&chksm=902fb815a7583103a83542f243429fcf18e0a08576f8623fe753e6ff4b09f98ce24ce5a8c532&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2024-10-31
fetch_date: 2025-10-06T18:54:18.444263
---

# DarkGate最新攻击样本攻击链详细分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDpibP198wvxiagDC73Ap9iaQ4c7avCHJpibe1Nq24tp4d7w3CvNbZc0p3nA/0?wx_fmt=jpeg)

# DarkGate最新攻击样本攻击链详细分析

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

原文首发出处：

https://xz.aliyun.com/t/14537

先知社区 作者：熊猫正正

DarkGate恶意软件于2018年首次被曝光，它是一款商业加载器，其功能包括下载文件并执行到内存、隐藏虚拟网络计算模块、键盘记录、信息窃取和权限升级等，一般使用合法的AutoIt程序加载运行AutoIt加密脚本。

DarkGate由作者RastaFarEye开发，在俄语地下网络犯罪论坛推广出售，通过订阅模式提供，每个月价格高达1.5万美元，尽管DarkGate在2018年才开始流行，2023年RastaFarEye发布了DarkGate V4版本，同年十月发布DarkGate V5版本，最新的DarkGate版本为V6版本，该恶意软件因其功能完善，具有一定的免杀检测逃避机制，以及不断融入新的技术，开发新的功能，最近几年DarkGate恶意软件受欢迎程度与日俱增，保持业界领先地位。

最近一段时间，DarkGate攻击活动非常频繁，笔者针对DarkGate最新的一批攻击样本整个攻击链进行了详细分析，供大家参考，有兴趣的朋友可以去网上下载对应的样本，自己动手调试，深入学习一下，应该可以学到不少东西。

详细分析

1.初始样本为一个HTML文件，打开之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsD9ytCKGrEicb13gGnZbVjfdQcCmf1rBkKFkLzOVE3hzTPRpUnjmsNMqQ/640?wx_fmt=png)

2.点击How to fix之后，界面变成如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsD3q5M6NaYEg5GnWAJaOF7tBROPrichr6v6hGxdOT1BFrCMib1QfFTZmRg/640?wx_fmt=png)

3.按照上面的提示进行操作，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDQ7ib92rueSkrvr8cntvbuJMhaZzibcB9d0sAqPkWBfILicUpGrl2C9oiaA/640?wx_fmt=png)

4.执行的CMD命令内容，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDanSuOz38cpR5GggY1JmHC83JL4Sjibg3wicDdZphpMKZicmZa1nw35NRQ/640?wx_fmt=png)

5.下载后的HTA样本，内容如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDWv2FlaEqDLdoolebjlVzc7IZUejRwgA46jXFbdj55v10gyICHba9sQ/640?wx_fmt=png)

6.调用PowerShell执行脚本，从远程服务器上下载恶意脚本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDLHqx6tv92u7wk2q2pBlSicYkqQhDxOjDM0licfw6lgSPg7AObyM5RTLw/640?wx_fmt=png)

7.下载的恶意脚本，内容如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDwTv8AHmptwfujzjGaGkPIa5mIH1N2NXUYU71O472opAeicpaNUcH6Uw/640?wx_fmt=png)

8.创建目录，然后从远程服务器上下载恶意压缩包文件，解压缩文件到创建的目录，并启动程序，设置目录为隐藏属性，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDouTwXkdpECoGvBKMvicslh79q5rpk4bMM9Iftgu0Xq6gNbUviac6tnHQ/640?wx_fmt=png)

9.通过Autoit3.exe调用script.a3x文件，script.a3x文件内容包含AutoIt脚本的特征字符串AU3!EA06，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDz0RFbaFmOiaKG0SB0BuTeiaEmGHrmJhaTHZB2l8D7X3PibsBq5tCE9oPw/640?wx_fmt=png)

10.提取script.a3x中的AutoIt脚本之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDK4IkrcK9liaGFU7cJGic5UTotl2swtBfhKB4ibZjIyhabMZ3EiaN5raibqQ/640?wx_fmt=png)

11.AutoIt脚本通过执行解密出来的恶意代码，在内存中加载执行解密出来的ShellCode代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDicIWMYyic8Bcc0aoDKZ2jpAs22XCsG9C3AwuhujpdyFDzA8g4pDGIHTQ/640?wx_fmt=png)

12.解密出来的ShellCode代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDqcZ8q3vEzlN52aQEcKIVWxn3cvnzCwvc7SmzJI7Itozyrkvd4BKopA/640?wx_fmt=png)

13.动态调试ShellCode代码，获取相关函数地址，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDA3uUKrTLxX2lb0R4Cu48lf0SzP0fJ7zVyI9dxHJehF6XPUHbHzvicCQ/640?wx_fmt=png)

14.跳转执行到解密出来的PayLoad代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDWdjRQy7enqU2JeiaBopbu7vvxcI1xwtLiblu1Rcu1Qo55dJTDianoiaOQg/640?wx_fmt=png)

15.PayLoad的入口点代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsD4t5bP9wlrqk4Lqw2nfnOUcGChWKv7QdRnxq8ZnnGksl7DQzdLW05pA/640?wx_fmt=png)

16.解密出来的PayLoad是一个Delphi编写的程序，编译时间被修改了，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDibB8BoibMc6QFYmqcOgfLItvVl2OsriaXd5Y0TrCEHYp8ZaDmK9JkWSwQ/640?wx_fmt=png)

17.通过分析发现解密出来的Payload就是DarkGate恶意软件加载器程序，该加载器代码与此前发现的DarkGate加载器代码结构基本一致，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDb3hfiaOjAn1WZ5GIjdAPGcPWA7Dfu2dBMRjiagBfVVF9VyCzaJaZpEaA/640?wx_fmt=png)

18.通过获取程序命令行参数，来判断程序是否为人为执行的，可能是反沙箱操作，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsD7HO0xqJqFUdwCoATKT8FL5nLTicZqp2QFXcHOBWZ2FjLw4rJbdyXy8Q/640?wx_fmt=png)

19.如果发现是人为执行的，则弹出提示对话框，然后退出程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsD0rJV2rdcx5D5frCkbzOaO7fhKutLdgGuMhc34aBayLeFgAibpfsU3wQ/640?wx_fmt=png)

20.获取操作系统键盘信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsD5gHlnBypZHqiczf0zs2ahTd6Oqs63J4zzm9sfneicfbJh0TrIf0wqo5A/640?wx_fmt=png)

21.检测操作系统版本及启动信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsD4AtmVs2f5BaLNDeymvMavF3xHGAbhDMX8iaJE9T7V8pWdlFzbojtEicg/640?wx_fmt=png)

22.获取磁盘剩余空间，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDw0wZFU10JurdkB7boDpf3LbaMs3ZfmVyUic9lVgLiasYFx0PtAgDjPNw/640?wx_fmt=png)

23.查询HKEY\_LOCAL\_MACHINE\SOFTWARE\Borland\Delphi\RTL注册表 FPUMaskValue的值，来确定此环境下是否能支持 Delphi 程序的运行，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDeXZsad1tcSRTYetZ51qp8PqJDVszAvDqDRiazViaiasCN35sHibsvVB9bg/640?wx_fmt=png)

24.读取autoit脚本内容，然后在内存中解密出DarkGate主体程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDYxEREY6ZEtkM43V0iabfpxGyNwuoEg7ia27P6nOIeZHqg7ESVggicnnrw/640?wx_fmt=png)

25.解密出来的DarkGate主体程序，也是Delphi编写，编译时间也被修改了，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDwzB2nWavMviaq9XUMN3PXMSpQ2DlyhJ4v6f5k99LicU5vwvwcs5Iiawzw/640?wx_fmt=png)

26.DarkGate主程序版本号为6.5.9，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDevNkCdebrpv6tmUicQZXzjFrK7bdF4ibwzKCoUla4uvvE2eicU8eo84UQ/640?wx_fmt=png)

27.生成LNK快捷方式文件，并设置自启动项，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDq9JVGyqYs78dutOcJOYWg1237GCn6I2gVTrkyOqHB4st5mPu2gicVLg/640?wx_fmt=png)

28.LNK快捷方式命令行，通过DarkGate恶意软件加载器加载AutoIt恶意脚本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDMB9IfUbSkcd3lT4ERwOR1y8u4Ja6nGtrpH1EyMY5D1XIuJicSHwuibmQ/640?wx_fmt=png)

29.在指定目录下生成DarkGate恶意软件加载器和AutoIt恶意脚本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDia9iajhx2KjXTzibCcalkHUdib1Gkzv6ViaN4eiac4eK5qpmm6doibdNx3icLw/640?wx_fmt=png)

30.生成的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDn07tmS8YSlvVib3URBjIdricbYnrpxmqCd4I2gl57tArl9C1qYbDcZvQ/640?wx_fmt=png)

31.检测系统上的安全软件信息，相关安全软件目录列表，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDTGkPAb5uJmpdgWlGe3voYyctzFUX8iaibmASqkyqvoMBjtS79ZNaiatcQ/640?wx_fmt=png)

32.收集主机系统相关目录的数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDs10YYzDhVZGyz5k5JsUjw1k5fiaZicKJX0v7buT2MnLtQlzmdF1Xe0Xg/640?wx_fmt=png)

33.键盘记录功能，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsD7St6y0l49n2gTGvWh7RYqzHyhwpgWDkbwiaAJXuaQGm6DiasehDLadXw/640?wx_fmt=png)

34.获取系统剪切板信息，后面来判断是否为bitcoin地址，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDuvuIPEViaAIdhd9dNuZPTkABEqKSw9FnWT02evVxWK5hsjtKVZNma8A/640?wx_fmt=png)

35.解密出DarkGate配置相关信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDgeHazZmm11SCNoiaMQrQxK6qyuJhaYtHR2JYISF7qnJ9FleIwgoPS3g/640?wx_fmt=png)

36.与远程服务器域名flexiblemaria.com进行通信，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDYjibyqVwpiccibuxHCK5NdQVzibg4PCkMbljEfrT7lNScibIGfXLSOibCLGQ/640?wx_fmt=png)

37.DarkGate整体的功能还是比较完善的，就不一一列举了，而且该恶意软件一直在更新维护，功能会越来越完善，相关的c2通信指令，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDvw8rVz3cx0qN0oAOPYAJEZCZEGib5IPzHORAaccfbTmpKS09hDVcjEQ/640?wx_fmt=png)

上面的c2命令，具体的可以去参考DarkGate恶意软件介绍，到这里DarkGate最新攻击样本的整个攻击链样本就分析完了，最近活跃的一批DarkGate最新攻击活动基本与上面的攻击链一样。

威胁情报

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUUWBdzBTV0TuvtjPmK8OsDyr8Z1zAtjAdwU06j5gOPcdibUxwIBtykiapcPIOGhJAxK36Garw1cZLA/640?wx_fmt=png)

总结结尾

黑客组织利用各种恶意软件进行的各种攻击活动已经无处不在，防不胜防，很多系统可能已经被感染了各种恶意软件，全球各地每天都在发生各种恶意软件攻击活动，黑客组织一直在持续更新自己的攻击样本以及攻击技术，不断有企业被攻击，这些黑客组织从来没有停止过攻击活动，非常活跃，新的恶意软件层出不穷，旧的恶意软件又不断更新，需要时刻警惕，可能一不小心就被安装了某个恶意软件。

安全分析与研究，专注于全球恶意软件的分析与研究，追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbi...