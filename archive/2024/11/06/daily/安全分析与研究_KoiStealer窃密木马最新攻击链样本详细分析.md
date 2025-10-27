---
title: KoiStealer窃密木马最新攻击链样本详细分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247489523&idx=1&sn=35d277979975927c4f0b7a0ecd8b7204&chksm=902fb8dba75831cdd9321ca0fcdf53c2935ef1fca74fea45d09ff8239cf959548f88476f44a0&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2024-11-06
fetch_date: 2025-10-06T19:19:47.719232
---

# KoiStealer窃密木马最新攻击链样本详细分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfm8n5hOxiauEoEvCTTvgMUvdAHcGgLDQEuPgAPWUxMbxYXjcDTeia18Qbw/0?wx_fmt=jpeg)

# KoiStealer窃密木马最新攻击链样本详细分析

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

原文首发出处：

https://xz.aliyun.com/t/14900

先知社区 作者：熊猫正正

KoiStealer是一种新型的窃密类木马，攻击者主要通过钓鱼邮件进行传播，该窃密木马能获取受害者屏幕截图、浏览器中储者的密码、Cookie等数据，然后利用盗取的这些数据，对受害者进行更进一步的诈骗攻击活动，笔者最近捕获到该木马最新的攻击活动，对该攻击活动攻击链样本进行了详细分析，供大家参考学习。

详细分析

1.钓鱼样本解压缩之后，伪装成PDF图标的快捷方式，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfm24vEcUAvXY1FDkcwgEmPN6O3ZtvRfB4hoKCJdqE6ZXvbcOMVjiarpHw/640?wx_fmt=png)

2.快捷方式执行的命令行参数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmRD1ZVJicXvUfupMrib6bTQ8XRpNialL4gdtpl87ygMHBwWLTcBojxZXeQ/640?wx_fmt=png)

3.创建计划任务启动项，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmpIu0MiaIA4bvStfBicKp4cLCKGSiaCwLSVqZkLTCDteCDPYSpFnCgaxCw/640?wx_fmt=png)

4.从远程服务器上下载计划任务启动项对应的恶意脚本文件并存放到%temp%目录下，下载的恶意脚本，从远程服务器上下载另外一个恶意脚本，并删除之前的计划任务启动项，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmv6owgfhfloLM9gpb3mcTKoibicicSrjV9fibUhA8eLJEC34wLgbxhZQrmg/640?wx_fmt=png)

5.下载的恶意脚本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmP01ZkdnRpEyGujibd36vtFnobNxxXJ13GXfnmbK1jhKFTFphibDh9OMA/640?wx_fmt=png)

6.恶意脚本将自身拷贝到%ProgramData%目录下并重命名，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmRXHJ0wlB21zHW6KSMnTH2CRNNx6SCdh5E4G2j5kRTQ0iaxvxTRNz7IQ/640?wx_fmt=png)

7.从远程服务器上下载恶意PowerShell脚本并执行，恶意PowerShell脚本内容，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmu9THEe7hQcdvQFMxs3yh6lncbQUl5Tia8iao42eZyJLK0H6T2nnE4QHg/640?wx_fmt=png)

8.恶意PowerShell脚本从远程服务器上请求PayLoad数据，PayLoad的编译时间为2024年2月21日，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfm8YyiciawQkV2nKsdelW52GpscfuVnErKxJGOjvhCYfLozffA0AHaWnkQ/640?wx_fmt=png)

9.然后通过ShellCode在内存中加载执行PayLoad数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmI06t8NTxNP6dsoXPmhcAeUBxCU3U4ckd6R1K7Scrkr64bt2UOJOkPg/640?wx_fmt=png)

10.ShellCode加载器代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmKm9vo0HhQZ7W4xYgqJ739pyg23s4goIcMF1LJDMazicZwVic1aT5uvicg/640?wx_fmt=png)

11.PayLoad代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmTPmwRoTRxBQVZsDWYIA7XYm44krUgU5t5ib7ru4wiaEibzNxo9XgHiarBA/640?wx_fmt=png)

12.获取程序资源数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmvwaqF9ibnQOtulKymjtFOR58QVwS1A7u0YLf935LxhKELqSnOPGQAibA/640?wx_fmt=png)

13.获取的资源数据ID为47574存储到分配的内存空间当中，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmqg5hG82BUJTnBYHGN1WPRgIoVp1qURpsZVUPcR76PXhE2RbsG18u9A/640?wx_fmt=png)

14.获取的资源数据ID为37252存储到分配的内存空间当中，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmrMfAFpZqOcMC0S5bEZyZBrQmXO72Rxcwb01uMGQAtGMy5eMWooEDeg/640?wx_fmt=png)

15.利用资源数据ID为37252的解密Key，解密资源数据ID为47574的加密数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmw55WgI4ZMlH7vdQtIicFIibyGKV1scTIYib1lxn9dKicfLHdp64v1Wcr1w/640?wx_fmt=png)

16.将加密的资源数据，拷贝到内存中，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmqFibp21PaU7WGEdoYrKDqJRLQZ1bPzQBlYX7etMuic9S23RBwc5icFeFg/640?wx_fmt=png)

17.解密加密的资源数据，解密算法，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmSKesTByeWPUwkVjd7Xg3aLoVSvucTwrzndeAlUGMBbjJnhPia0cfibyw/640?wx_fmt=png)

18.解密之后的资源数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmsCm7iac7IV9bjAzTLyebPzoWicZibhktotf6F7OAdbM7pOFuf8T2ocLRw/640?wx_fmt=png)

19.然后分配内存，将解密的PayLoad加载到该内存中，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmr0kNGWImfZDVGbYmwLicNalI7tqkG4PcTYl9fOgqYqWGa74k8icjuKbw/640?wx_fmt=png)

20.最后跳转执行到PayLoad代码入口点，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmo80wEyLvnas0DHXnBCFUOZMbC5Xc3NKqTy8ZGl86GUhTibCRtBLLsnA/640?wx_fmt=png)

21.解密之后的PayLoad编译时间为2024年6月4日，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfm9Zpu9zw8neMsK5Fu89lz0MNe2omPjc7T4awN8SLMichCm8QicichiclugA/640?wx_fmt=png)

22.PayLoad代码，会判断机器操作系统语言版本，如果为以下语言ID版本，则直接退出程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmI0DUOZDV1TZD22EHiaPmurA1ShNSnEXKAMhNAsibwlshGjPQd7tvetCA/640?wx_fmt=png)

23.获取主机相关信息，如果不满足，则退出程序，主要是为了反沙箱操作，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmCVsBnEKZRSibUh42iacSgdibiajxXdibgTexZajDGmkses3lu1EVpeJVFFg/640?wx_fmt=png)

24.通过获取主机的文件信息，用户名等信息反沙箱，例如获取主机用户名，判断是否为列表中的用户名，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmjDicJYlAB8iaJbaFr1l4Nv8jUNfD5P6ONq1vUWzzWI6fQOu88QqcEyzg/640?wx_fmt=png)

25.获取远程服务器URL连接地址hxxp://176.10.111.71/guapen.php，并创建临时文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmlwyWEJVeJibT3b9vBia42ZOCPpTvibdVuBmEUZjEibDlibgFfEoEDsEYVKQ/640?wx_fmt=png)

26.获取%ProgramData%目录下的恶意脚本文件，并设置计划任务，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmotu9iaJkPYmkKj3vn0pJNlJd5nDickgBibGrrlmdACtwV36jefaH0TSDg/640?wx_fmt=png)

27.设置的计划任务，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmWiaqicdTvzvmGdeI9e6uqOf3OU8PRsn1oibOciaQsTdStUYwZq3hqHsBgA/640?wx_fmt=png)

28.从远程服务器上获取相应的配置文件数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmL3RPnfZKTt21dX0JgmutKl90HlxDPojha9BQF8pvQxNcGfL6hd3uAA/640?wx_fmt=png)

29.通过固定的请求数据格式，向远程服务器发起请求，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmrGG4GSVIMRX08iaUw2HgZ5wlYiaYphjvRjBRItx2s57zM0aVwkAZHYnA/640?wx_fmt=png)

30.请求数据格式内容，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmJ0UVJUkKP0oKvv58jU6nB8tbaSxrqZVGdsAkqAdGB9XBfNfGeuBsLg/640?wx_fmt=png)

31.获取主机名等信息，然后以固定格式向远程服务器发送POST请求，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmNyzTMRtE7pogickzoc5uticGezwIsKibheBsnW561pic4VrDd8PETRCFrg/640?wx_fmt=png)

32.从远程服务器下载恶意PowerShell脚本并执行，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmaTyLT2SnemHh9lCAn7rYaGBJ0E2EK5GCj8qaeibBaXDS4zOjCT57ong/640?wx_fmt=png)

33.下载的恶意脚本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmbLVjvjNlDhBoR3x4EeQZicnPgYs8YfDBY27CclMBLWvpcGOrKnCnicrA/640?wx_fmt=png)

34.从远程服务器上下载配置数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmYc5A5qIIF3QP3y7whPsCJOzkG4LshrPzQ3kCopVfNkVibZpT3ZyQNTQ/640?wx_fmt=png)

35.恶意文件配置数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmXPXoJTOrZ4lhyiaTmbvQCvIMNpsMrA3X5klvmpehjUIZ0Iiay0KTXwNw/640?wx_fmt=png)

36.异或解密上面的加密数据，并加载执行，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmIC4zniaUfk2icWlTjX8V2Sp6VaOic1mVeqFYdIIhaSvWDib5SUR0MO4UUg/640?wx_fmt=png)

37.解密出来的最后PayLoad是一个NET编写的程序，使用Obfuscar(1.0)[-]混淆，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmtZO812Tryq8COOBnCVmrVpdcu2pIoSLZohd1V8ziaq6cMqbkh6Se2gg/640?wx_fmt=png)

38.解混淆之后，与此前分析的KoiStealer代码结构一致，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmprSQctiaNGibnjSqf11yV0AvwHD1W6DqeAqgJ6RU4c4OVnj217EoQgOQ/640?wx_fmt=png)

39.获取到相关的配置信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmsDiajnv9J1cUAvsbrhVibA3sJibKibNgIwibdlmYwT23gTQELvfh49Svg2g/640?wx_fmt=png)

40.获取浏览器相关信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfm6ymO9RUavE52z5edVGKvCrLJ7FU6ozoP28wYCajBuzLkV7kWvfPhdA/640?wx_fmt=png)

威胁情报

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWJexz5uKOUP4r2glbYOQfmNe5KktRpgQ6icichxaEMo2VXNItL3THITvH5uNiaOmveicrMRkicv8Was6Q/640?wx_fmt=png)

总结结尾

黑客组织利用各种恶意软件进行的各种攻击活动已经无处不在，防不胜防，很多系统可能已经被感染了各种恶意软件，全球各地每天都在发生各种恶意软件攻击活动，黑客组织一直在持续更新自己的攻击样本以及攻击技术，不断有企业被攻击，这些黑客组织从来没有停止过攻击活动，非常活跃，新的恶意软件层出不穷，旧的恶意软件又不断更新，需要时刻警惕，可能一不小心就被安装了某个恶意软件。

安全分析与研究，专注于全球恶意软件的分析与研究，深度追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbiz.qpi...