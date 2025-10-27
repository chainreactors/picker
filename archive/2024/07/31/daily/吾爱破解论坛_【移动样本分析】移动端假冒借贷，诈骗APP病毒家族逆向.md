---
title: 【移动样本分析】移动端假冒借贷，诈骗APP病毒家族逆向
url: https://mp.weixin.qq.com/s?__biz=MjM5Mjc3MDM2Mw==&mid=2651141040&idx=1&sn=3bd58f858a3caf70ecb633f2b66d3c8a&chksm=bd50a3e48a272af2749eb324526f5a215b483f749211611dcd69f69e2b9163090fcea8852703&scene=58&subscene=0#rd
source: 吾爱破解论坛
date: 2024-07-31
fetch_date: 2025-10-06T17:44:06.466819
---

# 【移动样本分析】移动端假冒借贷，诈骗APP病毒家族逆向

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZLc302LNxrxpI6jHT5VXnKNbW8IotSUjo6ia2Q5d1YHA3MMicEtn6ZouneP6bX6SbFApyypSU40ybbw/0?wx_fmt=jpeg)

# 【移动样本分析】移动端假冒借贷，诈骗APP病毒家族逆向

原创

吾爱pojie

吾爱破解论坛

**作者论坛账号：fengyutongzhou**

最新又遇到一个移动端假冒借贷诈骗APP病毒家族，今天来搞一搞。还是老样子只分析网络行为，过程写的比较啰嗦，主要是分享思路和研究成果，讨论技术问题。此文章无向导，无结论。样本不传，只展示目录结构。环境及工具：夜神模拟器Android9、算法助手、JADX、小黄鸟。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLc302LNxrxpI6jHT5VXnKNJpotjhYxiaOF9RnbW4oEwic77t0BvV7SFOicl9BjTpmkPZes4Zficpc7Pw/640?wx_fmt=png&from=appmsg)

如图所示小黄鸟代理抓包会弹窗，不仅会弹窗，APP自身还不触发联网。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLc302LNxrxpI6jHT5VXnKNTgBPSrFL3FeEVx61hibHHDMEjFoibOscN9CyB3511d3VIPpJr60UnZPA/640?wx_fmt=png&from=appmsg)

MT管理器查看有壳是360加固。其实可以放弃了，不过换一种渗透思维，尝试找个同族无壳样本不就OK了。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLc302LNxrxpI6jHT5VXnKNicZ37knbVkO3hmFs2OibZTflpEzkH6L6zj1X28wjzlibHkZicZPJMmkDww/640?wx_fmt=png&from=appmsg)

这个同族没壳，开搞。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLc302LNxrxpI6jHT5VXnKNeXROv88CZYrwIeWQibBwaL7cRXjcXdvq6AOyWHs3MNqAsoz9uUZbIbw/640?wx_fmt=png&from=appmsg)

这是有壳那个样本，显示弹窗的栈是c.k.b.d.a.e.c
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLc302LNxrxpI6jHT5VXnKN6fj0yT8dicKEpeAa0YticdvogKOHw1ibbawjVPowHY4L2WFdnzvXqP2eg/640?wx_fmt=png&from=appmsg)

这是无壳样本，弹窗栈是c.j.b.d.a.e.c
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLc302LNxrxpI6jHT5VXnKNWY0icOtnOmdGaziaSNvWIVfK3QFouo72WWDQGaibTVaKDduY9nQ6bJJzQ/640?wx_fmt=png&from=appmsg)

JADX反编译看一下目录结构妥妥的混淆
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLc302LNxrxpI6jHT5VXnKNmFbxtTTguGJ88Z52kTDe3TgAk6Zmd1WamcplJOSufHKkrknBPIePUw/640?wx_fmt=png&from=appmsg)

定位无壳样本弹窗类，c.j.b.d.a.e类
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLc302LNxrxpI6jHT5VXnKNjoQd0LVoMwlHyTNubG6KgXOW59nswGU2INQHR19XkC84pQ92StjHPQ/640?wx_fmt=png&from=appmsg)

找到方法c，这个方法主要就是判断网络配置，C2398a.f7576a.m2732b先判断ture或flase，ture的话就执行弹窗，下面其他的网络判断操作都不执行，双击m2732b跟进代码。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLc302LNxrxpI6jHT5VXnKNy9yDzBL7dzEYZmHmsf6c2gREdZcEA2BiaDXHqQJr80wJiazqs95ibFr5Q/640?wx_fmt=png&from=appmsg)

主要是这里判断是否启用了VPN。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLc302LNxrxpI6jHT5VXnKN9BwquIFNt3CUUvpxCibVKoBheCib9DAm0IZbicA1I5iaibmT6OzctQAEaww/640?wx_fmt=png&from=appmsg)

来到最新版算法助手v2.1.2，创建一个HOOK脚本，让c.j.b.d.d.a.b函数无论如何都返回false。就可以了。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLc302LNxrxpI6jHT5VXnKN7GW7JwSxRmxHnKJJSekk7fkb4cZ5xYbMV26fHkDdQ0uFpTAmwQM71Q/640?wx_fmt=png&from=appmsg)

来到有壳的样本看效果，拦截c.k.b.d.d.a.b函数，成功。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLc302LNxrxpI6jHT5VXnKNibXFrjWiaOPR2bCldl7PkjLXp7k2H2mTuF6RnxIAyKStickFSsJCwAo1g/640?wx_fmt=png&from=appmsg)

这下有壳样本也搞定了，看到正常抓包，弹窗也没了。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLc302LNxrxpI6jHT5VXnKNfNiaCEJ2gwLKdtE1ljrcdT22aiaWbYSwJmRcssr91ibhLLia6mQOXExeUw/640?wx_fmt=png&from=appmsg)

分析一下网络行为，APP分别去myqcloud、阿里云OSS、亚马逊云，请求了资源文件。先说为什么，其实就是把URL加密后存在云上，主要是隐藏APP服务器地址。或者是进行线路冗余。这段操作有点像之前树蚺家族利用OSS存储服务来隐藏节点。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLc302LNxrxpI6jHT5VXnKNm7CYnblibBx8ezMkMBB2UlRJoEKX7vIAI8J0ic31LiaF8ZCCFoiafsvsjg/640?wx_fmt=png&from=appmsg)

算法助手HOOK，显示加密的内容为RSA加密。之后拿着密钥和密文来进行解密就可以把所有IP节点解密。

****-官方论坛****

www.52pojie.cn

**👆👆👆**

公众号**设置“星标”，**您**不会错过**新的消息通知

如**开放注册、精华文章和周边活动**等公告

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZK0l7v6mmrudZKXzpdM1WcomgJQnibvLzBUFRSurSkmIfl0ZrDNvSy3MszKNY3XOkcuUbWp31HMjLQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLyxib6edSK27iajkxL2xVZoS1Lbnzjavd2ZDp2KicftN0Tq7vEcJMlLG3chkhj7NcSTEMoLGTRjqDaA/0?wx_fmt=png)

吾爱破解论坛

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLyxib6edSK27iajkxL2xVZoS1Lbnzjavd2ZDp2KicftN0Tq7vEcJMlLG3chkhj7NcSTEMoLGTRjqDaA/0?wx_fmt=png)

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