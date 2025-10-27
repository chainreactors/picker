---
title: D-Link 漏洞挖掘
url: https://buaq.net/go-136394.html
source: unSafe.sh - 不安全
date: 2022-11-20
fetch_date: 2025-10-03T23:16:31.352011
---

# D-Link 漏洞挖掘

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/131dd17910cf8cea11df6187d9c004dc.jpg)

D-Link 漏洞挖掘

本文为看雪论坛优秀文章看雪论坛作者ID：混子1一前言学习二进制漏洞有一段时间了，一直学，一直复现，属实有点无聊，但实战挖系统漏洞或者虚拟化有点难度，于是就把目光放到了路由器，于是又学了一段时间的路由器
*2022-11-19 17:59:19
Author: [mp.weixin.qq.com(查看原文)](/jump-136394.htm)
阅读量:28
收藏*

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gox5h8Oo2e4iaYBHtzKaSXoMX8cTdUKib2Rbb3yAhY35ia1UADiak8gYFYwjKYahNK1DNnuT7icAkEBSw/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：混子1

```
一

前言
```

学习二进制漏洞有一段时间了，一直学，一直复现，属实有点无聊，但实战挖系统漏洞或者虚拟化有点难度，于是就把目光放到了路由器，于是又学了一段时间的路由器漏洞挖掘基础，最终开始分析了D-Link路由器。

```
二

了解
```

首先我们去cve-list可以看下历史漏洞，可以看到最近分析DIR-816型号的有点多，那我们也来分析它，但分析之前可以查一下该型号的版本，如果发现A2\_v1.10CNB04（简称“B04”）还有更高版本，那尽可能分析更高版本，说不定可以捡漏，在查找版本时，发现它有B05，我选择B05分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbtJdpe9HFLclWiaultphgqzSgKAAJ0k8PiaNmvUcA7DtD8Jfb82g8ZTUSQ/640?wx_fmt=png)

```
三

分析
```

固件下载和binwalk解压我就跳过了，解压后查看rcS文件，发现启动了telnetd和goahead服务，由于不太清楚goahead服务是什么，于是百度了下，发现是嵌入式web服务器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbtPIKGHuL3OjicfKe3QKoknVUQeKl7AC8pjTo8Cz3lfLzLvstHiaevdQBQ/640?wx_fmt=png)

于是从web服务入手，用IDA打开goahead。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbtvodPjUV2UI8EmKAphoV1dOF8nOpE3MLS2usAeG3I6DhRU0ojJZZCnA/640?wx_fmt=png)

## **命令注入**

根据cve-list发现在B04的web服务接口setSysAdm存在命令注入，于是我定位B05的setSysAdm接口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbt10hibxzWE55bPgI4JUWLSmCic0o46W1PRPuSF3ExicLFY3iaXkj4AhnG9A/640?wx_fmt=png)

doSystem函数是对system函数的二次封装，根据函数可以发现会执行var、v2和v4，这三个参数，但v2变量不可控，所以没办法利用，var和v4分别是admuser和admpass的值，可以利用。

## **栈溢出漏洞**

根据cve-list发现在B04的web服务接口form2IPQoSTcAdd存在栈溢出，于是我定位B05的form2IPQoSTcAdd接口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbtibZWPE4Kgluia4N4URxVuurMz5hyKG0kViapgSu2FC4xK3A5tfEB8JSfg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbtfl2aDBCNQDZLC4s8qcaYicYETyWC3uQ5TicLxYgwFzv9fOoicu0cvPyrQ/640?wx_fmt=png)

发现只要v10不为0，进去后都会执行sprintf函数，造成栈溢出，而v10值取决于ip\_ctl\_carrules初始化成功与否,一般情况下肯定成功，所以一定会造成栈溢出。

前面都属于捡漏，下面可以利用IDA查找strcpy，sprintf等危险函数的使用，这里就不过多叙述这种方法了，在浏览cve-list发现了B04的web服务接口form2Wan.cgi存在栈溢出，当wantype为3时，l2tp\_usrname会被base64解密，结果存入v94，不检查l2tp\_usrname的大小，导致栈溢出。由于该溢出和解密有关，所以我就比较好奇了，查看了B05对应接口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbtgfAia4HxNa10q5HUpooxt5Tv0iaHYpN9BUEeHZOHhiciakoOQT59UiacIZg/640?wx_fmt=png)

有点出入，但出入不大，websDecode64应该是解密函数，第二个参数是l2tp\_usrname值，第三个参数是l2tp\_usrname的长度，所以第一个参数应该是存储解密后的内容，进一步查看websDecode64函数，发现是base64解密，并且对长度没有限制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbtlp7cE68FREfulJvNHwc8ibagOI8rpqKJ2VYsFNUd4ElXUtsPU8c7wgA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbtyDzsJ9yNrRWsv9hA7aKe7qSI7F4icicV5kup07tp4tTJWekC8Nv88G5w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbtLpZo3JL8QQmkSXAL5fhcomkgMPPicNibKiaeMqKr9Vqx1unr9LibjIcs2A/640?wx_fmt=png)

这个函数也可以作为危险函数查找，最终提交了6个cve，捡漏两个，挖了四个。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbtSG1SlS3sjloyicSTjvaFdib4ZMVDhEuVic8SqUdRybt9dB9PuMen1Scbg/640?wx_fmt=png)

```
四

调试
```

用file命令查看goahead，可以看出是32位，小端存储，mips架构。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbtykKXh4z3y7s1GNic6PULdEzEETdI1ZgYibQHEvtmRAicUGSG8B5Skytqw/640?wx_fmt=png)

直接运行goahead程序会挂，因为没有相应的配置文件，我们可以尝试调试，先用IDA在主函数打断点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbtpEdRR96qpAQjc8lJLIia55jPycedhCb5Uar174PPq8Wv1XoPichDVS9g/640?wx_fmt=png)

根据汇编和反汇编代码，在各个if里面查看是否有return，在里面有return的if全部打断点，直到web服务启动前的所有if，然后f4，跳转下一断点，如果跳转下一断点，调试结束，说明上一个if，需要修改值，最终需要修改的就是91行的setdefault和126行v19。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbtPEE38Haf273aEH88Y278Yswt5PLJLxhwgQTeYVDfMpyibiaeZALG3fSQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbteKQxay6QpsDenxx21PeI9Rt7lLCrgDjNRj4oWHawIWQkQQibF9TtfQw/640?wx_fmt=png)

经过上面两个判断，最终就可以运行了。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbtXuA6j4b5n8J0s7SF9dOmBibN205KGl43gavkGHzZBywZ6lQkzn1VMlw/640?wx_fmt=png)
后面登录，也是需要修改值才能登录成功，如果想要验证的漏洞的话，可以自己尝试一下。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbtzhpFX5ibEK8XHhvf1WM1Nxg6Ph5j5Ticjv3Mx1Lbic8qTkCNatWZRDCYg/640?wx_fmt=jpeg)

**看雪ID：混子1**

https://bbs.pediy.com/user-home-964032.htm

\*本文由看雪论坛 混子1 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EUvNq2rQycZibURG09OtYP0XCHXZ3icZXcMlqrP9xKN6J9cwRouvpXMfRrRxdE0xCpPmeqybJGOPibw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458479751&idx=1&sn=ca684920ebd23cc09080ba6eefb94165&chksm=b18e5c0d86f9d51b3b31b8a99231416b78566b3365abfbe25625aeba78a44b769576548b316f&scene=21#wechat_redirect)

看雪2022KCTF秋季赛官网：https://ctf.pediy.com/game-team\_list-18-29.htm

**#****往期推荐**

1.[CVE-2022-21882提权漏洞学习笔记](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471430&idx=1&sn=6a47d0c5c8f3f6204548e80977ecd059&chksm=b18e7c8c86f9f59a88d9b8e83c8297e0ef65034a73436998ab835531baadaa51f3d630793b95&scene=21#wechat_redirect)

2.[wibu证书 - 初探](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471429&idx=1&sn=a85188de9b9697fd1b9e708bb8bb1fdb&chksm=b18e7c8f86f9f59933d6cbf0040ed796f06e37b23f17f1ae842eb22257de02338e1a8d751f6b&scene=21#wechat_redirect)

3.[win10 1909逆向之APIC中断和实验](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471421&idx=2&sn=e83cf7220dc1c4c06a2efc78593e30cc&chksm=b18e7b7786f9f2614ecce34e23be7f71a3d3516766aabda8f25ae41c81ef359a2c245503cf86&scene=21#wechat_redirect)

4.[EMET下EAF机制分析以及模拟实现](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468723&idx=2&sn=5a830d04185d80e1b6cfa639dc6c6c15&chksm=b18e71f986f9f8ef5b3c2fec51f69751e63a5d6bdbadf43b49728ba05606fc4ac63fda378c92&scene=21#wechat_redirect)

5.[sql注入学习分享](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468108&idx=1&sn=42c8ec155e13e3882cf4aeb60cdbb982&chksm=b18e0f8686f98690c9792298abb04dd243862ff8effd545dc668c7b1c682aaacf9797d899e97&scene=21#wechat_redirect)

6.[V8 Array.prototype.concat函数出现过的issues和他们的POC们](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468074&idx=2&sn=06eb27c1649bd4e3a3e43a46a9500add&chksm=b18e0e6086f9877644ba0de33658232f99213d1b1b074342260031cb529c1b7ad1b89b2e0204&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicdP7bNEwt8Ew5l2fRJxWETW07MNo7TW5xnw60R9WSwicicxtkCEFicpAlQg/640?wx_fmt=gif)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicdP7bNEwt8Ew5l2fRJxWETW07MNo7TW5xnw60R9WSwicicxtkCEFicpAlQg/640?wx_fmt=gif)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicdP7bNEwt8Ew5l2fRJxWETW07MNo7TW5xnw60R9WSwicicxtkCEFicpAlQg/640?wx_fmt=gif)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicd7icG69uHMQX9DaOnSPpTgamYf9cLw1XbJLEGr5Eic62BdV6TRKCjWVSQ/640?wx_fmt=gif)

点击“阅读原文”，了解更多！

文章来源: https://mp.weixin.qq.com/s?\_\_biz=MjM5NTc2MDYxMw==&mid=2458484349&idx=2&sn=c7f021fe2855aafda08aa8e84d521ac4&chksm=b18e4ef786f9c7e1cc0d8ddda584d964a1e445f35845a0b2e0d68290133fe47e7e6752eb31d1#rd
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)