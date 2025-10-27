---
title: Lumma Stealer最新攻击链样本详细分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490762&idx=1&sn=1d43d9ea8e2b2008924e6bf1e2b7d9e8&chksm=902fb3e2a7583af4e5c691a25bfb387429be5373530a381a2cf3adee094a284b13dc8826e4ec&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-02-27
fetch_date: 2025-10-06T20:36:06.550359
---

# Lumma Stealer最新攻击链样本详细分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8EksmBa77ceQkQKib4PfJKHzHOicoJJ8yvk4VicQhMoiaGtNueqfbWmlbibg/0?wx_fmt=jpeg)

# Lumma Stealer最新攻击链样本详细分析

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

原文首发出处：

https://xz.aliyun.com/news/16841

先知社区 作者：熊猫正正

Lumma Stealer(又名LummaC2 Stealer)是一种信息窃取程序，自2022年8月起就已通过俄语论坛上的恶意软件即服务(MaaS)模式运营，笔者近日捕获到该家族的最新的攻击链样本，使用Pyramid作为远程服务器下载恶意软件，对该攻击链样本进行了详细分析，发现有点意思，分享出来供大家参考学习。

详细分析

1.初始样本为一个短链接，打开之后，会跳转到另外一个网站，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8UtELhSxZmGAQ84U9cXsKatchjSgASjvufmFaIzDKP4oibd7Iaprj6qg/640?wx_fmt=png)

2.勾选对话框之后会弹出提示，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8bwHsVCSeWX8ngkCgdyZhGXZ1M8w67wYStHBQzic6mY96HcHDJfQC6HQ/640?wx_fmt=png)

3.按上面的指令，会将一段恶意Power Shell脚本复制到CMD命令执行框，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8OQs1mPD0L3xZViaHaicAYJBwQQplDNKPh2B9RibIMGhsCmo4ks987dQMA/640?wx_fmt=png)

4.恶意Power Shell脚本内容，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8iaN7rgicwqCBT0TOFTCcRGdpmlX2VFcLSB5SCUh2LMrdcvib6A3y5kThw/640?wx_fmt=png)

5.从GitHub远程服务器上下载执行另外一段恶意脚本，恶意脚本代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj871GGpocb2j8OQ3qp39IyTb22UceVA1kG7qQz6FEHj2dDRG5gQVvUeQ/640?wx_fmt=png)

6.通过Base64解密上面的恶意脚本之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8RJIVhGRYbRqu06uAupnRJWUAiahMibu6PQdf3zr9gMEM1h4pmDLFZDyA/640?wx_fmt=png)

7.解密出来的恶意脚本会从网上下载python程序压缩包并解压缩，然后会执行另外一段恶意脚本，解密该恶意脚本之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8TiaIzhZIN9cn7c8IJ3WKAiaTNA8AkicugZaodKftkg759wqSPORicQcsEA/640?wx_fmt=png)

8.恶意脚本会从Drop Box远程服务器上下载另外一段恶意Python代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8zLhXc1vFiaaSDzS28aYcY6xmmmKpVpre9OGzpOZ1VMhmBpvgwnicQiaQA/640?wx_fmt=png)

9.下载执行的恶意Python代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8aj0icRoVXBJicObWTMk7E2FseXw04moLfica9zvt9e71hDzbJ0Un19Yiag/640?wx_fmt=png)

10.解密上面的Python代码之后，会从Pyramid服务器上下载解密并执行相关的恶意代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj89lbK4icxticPiag4xxX3hGkfDjUKU2nvR1f44gAGQstEIG7Pqb0oESEag/640?wx_fmt=png)

11.Pyramid服务器的访问帐号和密码信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8xov67QcViao2KOUyDX1aeKG1Ru6FQyrQXhlX24X6icvHvLIGgEPDQqTg/640?wx_fmt=png)

12.通过解密出来的特定URL链接访问Pyramid服务器，由于分析的时候的该Pyramid服务器已经关闭，笔者在该恶意攻击者的GitHub上找到关联的最新的攻击样本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8PVt10aFIc8tUAfTibVlzUp4soDLfGToTy4AXh2KQhpH6XNaZzibo5rxQ/640?wx_fmt=png)

13.跟上面一样，逐层解密里面的恶意脚本之后，会从Drop Box远程服务器上下载一个恶意Python脚本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8YibCwKDChpr66CjibEH5audAO6icHJkbCJVnX7t5hVgBfQqsc06BaZichA/640?wx_fmt=png)

14.下载的恶意Python脚本，与上面类似，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8EggyvkgnwonZDbZOJdvzN1rRm1BwzfMyw7yNZNnZY5ZXP7yG7WcwvQ/640?wx_fmt=png)

15.解密上面的Python脚本之后，同样使用Pyramid服务器作为载体，下载执行后面的恶意代码，只是服务器IP变了，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8fujCxqDp4GiaibD86mJPia2vqvXn2rpDbZWJvNIAZsoHxm7k9YeV43ZeQ/640?wx_fmt=png)

16.解密出访问的URL链接，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8eQDD8sIry2NDpJ8KuFvx93dow5cNIgxpSDlruRt0e1mvzichhDaT8xw/640?wx_fmt=png)

17.访问该URL链接，需要脚本中的帐号和密码，然后下载恶意代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8KsCIQESCNNbdKAMvaPGfh17kvOWbLTwDuw1nWRvicL3SkTiaicRXql7Cw/640?wx_fmt=png)

18.下载的恶意代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8UtWUZ1JXfpEhrHdiab7rcJoe2senklsO8PJg6m2nsJmaC2v5v0J5aJw/640?wx_fmt=png)

19.再解密从Pyramid服务器下载回来的恶意代码，根据条件选择使用ChaCha20或XOR算法解密，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8Kz997cnibZ7axjZCEHNgrIMFocvgMJOoE0XwiaHtyE7cn9P7BlbftTog/640?wx_fmt=png)

20.通过分析发现使用ChaCha20算法解密，解密Key和IV包含在脚本中，恶意代码解密之后，是另外一个恶意Python脚本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8JXW9Ztiab0s37hg5sVjJh0VTKvPDaPhaib7icFSCBcg7EXHUiay841mwNg/640?wx_fmt=png)

21.该恶意脚本同样使用Pyramid服务器作为载体，下载执行后面的恶意代码，先从服务器上下载解密需要的模块，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8g7Eib0Jz1TOgDR5eVcpG4ibNbRFVJk714ibryl3PWO8bqXWJ10KUibiaNicA/640?wx_fmt=png)

22.然后下载解密解压缩需要的windows模块，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8xl2b7g1abok4U3DnMFu26KSS0oI1sVVSAiciciacYicZuNcADbzFPC9R4w/640?wx_fmt=png)

23.下载解密解压缩之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8jZlKicKy7uGWA2iaQXdIicAyYSM7zo7bEbWibQG7PSdHB5gvF2tetqjicicg/640?wx_fmt=png)

24.最后下载解密恶意模块，并通过上面的模块，在内存中加载执行，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8fF49BCQtUTkMyQxx0ibLCbhJcDCtOa1etvTQzDU3tkLO7Iocgj3EXicQ/640?wx_fmt=png)

25.下载解密的恶意模块，编译时间为2025年1月12日，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8hgxCxgPqpl79cYGoick5FdtcFSn8okwIWYDg7tztG11ic8Uf2aISZvSg/640?wx_fmt=png)

26.恶意模块，启动rundll32.exe进程，然后将恶意PayLoad注入到进程当中，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj83ejkAKz7hO0N1rPDqlZUyTeMlNiceCAiafoLE6vxfvUGNwBZnGLAC4cg/640?wx_fmt=png)

27.注入的PayLoad代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8JFJllksXQX9YhWyzVjoDfvFu2UFptzQtibg3Iwj2RNeVmM2kQh6yFwg/640?wx_fmt=png)

28.PayLoad入口点代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj89GpF66DEYAZcH1LZMjlqkbibtZUVPkaJXzxdmDnxgbicgoibBOf2iaC9IQ/640?wx_fmt=png)

29.里面使用了大量的XOR解密操作，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8MMNvbibOa5bzicXUiaSHlBOCvAtgQE1CIVuxb6IKEGAGqLd8M3kictT5tA/640?wx_fmt=png)

30.与此前分析的Lumma Stealer窃密木马相似，解密出来的C2域名为apporholis.shop，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8a6icYSHjcDicDaeT6RTB7KhyrkA2HA3XXWWZPZBribUJtRNeMb49QPTVA/640?wx_fmt=png)

到此整个Lumma Stealer攻击链的样本就全部分析完毕了，通过使用Pyramid服务器作为服务器载体，然后解密特定的URL和请求头信息获取加密的数据，再解密执行，有点意思，恶意脚本和二进制样本都使用了多种加密方式来逃避杀毒软件的查杀，目前为止大部分链接已经失效，服务器关闭了，很多样本已经拿不到了，笔者在最短的时间内，通过快速分析拿到了该窃密木马最新的完整的攻击链样本，通过恶意软件威胁情报数据平台显示Lumma Stealer应该是全球最近一两年最流行的窃密木马了，还针对数字货币人员进行过定向的钓鱼攻击，盗取数字货币。

威胁情报

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV1XGeEmjTCkrfMxV2Xdoj8ibx3QrYiajm7YISJpcnN0VQ32zSDYuIeoZa5OqicgvtNs5JKLSDwrkeWQ/640?wx_fmt=png)

总结结尾

黑客组织利用各种恶意软件进行的各种攻击活动已经无处不在，防不胜防，很多系统可能已经被感染了各种恶意软件，全球各地每天都在发生各种恶意软件攻击活动，黑客组织一直在持续更新自己的攻击样本以及攻击技术，不断有企业被攻击，这些黑客组织从来没有停止过攻击活动，非常活跃，新的恶意软件层出不穷，旧的恶意软件又不断更新，需要时刻警惕，可能一不小心就被安装了某个恶意软件。

安全分析与研究，专注于全球恶意软件的分析与研究，深度追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXJVicq5cxzeou29uVBHz19Hgvt8lszj2WwSRkN0wEAFmVBBiakBUrXTVA7XSBYbIibfb02LXba8uYicw/640?wx_fmt=png&from=appmsg)

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