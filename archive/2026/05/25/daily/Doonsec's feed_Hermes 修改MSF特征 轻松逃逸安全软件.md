---
title: Hermes 修改MSF特征 轻松逃逸安全软件
url: https://mp.weixin.qq.com/s/YY9lnq-_go9ToDKB-lfN8g
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:08:16.728267
---

# Hermes 修改MSF特征 轻松逃逸安全软件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1N1JeeKBordpia6FdLLFBZ1lQnmyib5O4ibRlqc0sbIdyibWZMUXy0ALUk8BZrzoFTO991XbDeDz7yMeTYbcjnwtJo639pxCRSCEggDjJruPVt8/0?wx_fmt=jpeg)

# Hermes 修改MSF特征 轻松逃逸安全软件

原创

大表哥吆
大表哥吆

kali笔记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 在前期文章中，我们讲到过通过手动修复特征的方式实现逃逸杀毒软件。但是这对开发者和编译环境有很大的要求，接下来，让我们来看看，如何简化整个过程。

**免责申明:** 本文旨在学习和研究，所有资源尽在内网环境中测试。坚决反对一切危害网络安全的行为，造成后果自行负责！
`Hermes`的接入，可以让我们的整个流程更加简单，从反编译到汇编，只需简单几步。

### 01反编译

我们先让Hermes对生成的java包进行反编译。

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorcBfrEicic2GDyF822ichVygTe9W8UVzeNKMMrj3CKQYibjWtZNAJayEIeMhV5LDQH6g0mQrvx6H7gSLdmnsQYeovg889Y4wbaFvsE/640?wx_fmt=png&from=appmsg)![编译后，对源码进行了解读](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorc0ZjQLrUnlqNUmQrIic0LqLwlYerBnOfjyHHs1GgzpbiaAzN2ZCfD6LiaibgsFJNK9j6xqDmTEZTiaEm9cU3lJYvU8J2GzTG2AAP60/640?wx_fmt=png&from=appmsg)

编译后，对源码进行了解读

### 02 特征替换

接下来，我们让其将特征替换掉。

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorfjm3OWMCYX6xGEN6rGH62ahSmc9LekSz47tMmVzhQX8tr6EhgK6BNibunu2TZ0y9DUYe7tViboHsa2O68uY9ibVIugvsY2QQz6Zg/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorcdx8jnlywvkCTIx9EQC1JoP838n1dCTicDT87nmffanooYusInG34Noc90r1Uynvm6w7hicia9ic0iccntbxCnGRrN34xernDmErxM/640?wx_fmt=png&from=appmsg)

### 03 删除多余IF语句

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorecHNHzOKeSYdVDfpQHPdibm3ibmZrchuRdcoBlD1yTLXSCbiaVJaWeXEostgqQagDathW5eOJFNQT3TntU8xlMdrMddmu9EhWZqQ/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorfBuoCs1TG6mOlViaSnfTqibY248W5Mt6mLFQUicVAWaAfKyhZiavsoAQaeSS2tJsQeeNjH07DKsJDutMB4yJJHwsTuJLzGqnNKpiaE/640?wx_fmt=png&from=appmsg)

### 04 打包

接下来，我们打包为可执行文件。

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBordMOhe5v6kZH6ON33kBezicSibaqInOVKxftCB9qK2CKLU3teTfhGgf6DLlo003QiawyHRjkHehdmJoDGetfCoUYVfVxGPiaNrcUHI/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorfGMQB0ibwFo1SCzeDkQIkxnTsTJ2s0viczibOdicQerc1443y0ABeia9uS8yrHnZibCCqJUdvddzKQ1d6dcBzCattd1n4m1JMFrF05U/640?wx_fmt=png&from=appmsg)

### 05 创建Skill

创建技能，下次更快更简单。
![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBoreC9cjlQ0LjObjGic0S4AXry3OsV9FPd9n3fibq2wwF4ZvZ723gv0TMLAATDlke0a0WEmDic2LL3dxxOqIw61ibfM1cmKUZMqOgdLM/640?wx_fmt=png&from=appmsg)

### 06 测试

接下来，我们进行逃逸测试。

![火绒](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorefv7NrIF3Elzw4mIDHS21peZ9K6amvKm2L9pQGZD10l9nshfN8Fer1j0mrOKRvS4ney32ffvPZyKjtXErBVgHTLuThURNhO7c/640?wx_fmt=png&from=appmsg)

火绒

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBordKODiamCaYRnmzRx4Xezx8tGVc19j0voSFZIZqYNZs8WLXEY4o8hPM4nalFI4RxcfSB8l3PDmJZKSQkZiaytZ8j8Uhaa8jftMJA/640?wx_fmt=png&from=appmsg)

在线0/48

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorep2BTicvSUKGTRAibuId5AVgYdmDmdUt2Y2Zia8gJrDY66mibEk0ib5KbNRwE8DUTU6NRzcKtLuicotaXYfypM5Rx9r2X4OJVsicOTww/640?wx_fmt=png&from=appmsg)![会话上线](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorcryEjShUULFtOnZKOA1TPht7OVV1ceZ2jDRwCLVb8ymfxXPyWA0NoxKNeKwnCr0GyOlWj7o9wlZIXtia4xjbXfqYVL0tpJ582Q/640?wx_fmt=png&from=appmsg)

会话上线

### 07 总结

OpenClaw Hermes等智能体的接入，为我们的工作带来的极大的便利，同样也带来了前所未有的新的挑战。借助AI资源，不断去学习，提高自身安全能力素养，更好地服务社会。

更多精彩文章 欢迎关注我们

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatia2JZVpfzEcXsOV52zrUXfJ951pRnM6UK5ghiaE4iaicHYADqWZFQmlZicF01GdKdwg9hRKlhiceeibQuRQ/0?wx_fmt=png)

kali笔记

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatia2JZVpfzEcXsOV52zrUXfJ951pRnM6UK5ghiaE4iaicHYADqWZFQmlZicF01GdKdwg9hRKlhiceeibQuRQ/0?wx_fmt=png)

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