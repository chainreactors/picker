---
title: G.O.S.S.I.P 2025 新春总动员（3）：世界上第一个计算机程序
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499675&idx=1&sn=fb738542c9b22d64ab6c87cf802aa5d7&chksm=c063d142f7145854186c858e444bdb69ebaf141e6c2bf869f8814054f43b64dcf8a63d09419c&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2025-02-07
fetch_date: 2025-10-06T20:37:39.093207
---

# G.O.S.S.I.P 2025 新春总动员（3）：世界上第一个计算机程序

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21FibK1j7BNb3SRtsmN8OXtBJvM9VJiaJEPB5e5Lh2kF1ibg2BsibYiahnhibxAKdPkjolyFBmYBPzHK0RWQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 2025 新春总动员（3）：世界上第一个计算机程序

原创

G.O.S.S.I.P

安全研究GoSSIP

我们经常把computer称为“电脑”，特别是在PC时代，“个人电脑”这个比较口语化的名称听上去就比“个人电子计算机”要上口一些，也许也间接帮助了比尔·盖茨和IBM的销售。不过早在ENIAC这个世界上第一台电子计算机问世以前，已经有了很多辅助计算的机械装置，实际上阿兰·图灵在二战中破解德军密码并不是完全靠了他的聪明才智想出来的算法，IBM当时也帮忙造了一堆计算设备用来加速搜索。不过话说回来，我们天天挂在嘴上的“计算机程序”（computer program，以及每天吵来吵去到底是C还是Rust更好）又是什么时候出现的呢？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FibK1j7BNb3SRtsmN8OXtBJXxSic1wEzvehUsrFJH43D5qxDhHU3qAf5lH9eeEgMUiaZD57SKvSsg3w/640?wx_fmt=png&from=appmsg)

春节假期过完，我们也该收心准备去干活了，所以新春总动员最后一期我们就和ACM官方杂志CACM一起，回顾下在差不多200年前问世的“计算机程序之南方古猿Lucy”：

在很多的书籍记载中，查尔斯·巴贝奇（Charles Babbage）都被认为是计算机之父。巴贝奇的差分机（difference engine）和分析机（Analytical Engine）设计思想，开启了人类征服计算的万里长征第一步。

这个程序具体是干嘛的呢？实际上就是一个初中数学水平（2000后，失敬了，也许你们幼儿园就学多元方程组了？）的题目：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FibK1j7BNb3SRtsmN8OXtBJNR8FTtO9WiaGO5ibicmOdZFjBupZlRc6DDbfJvvj8nicFviaCN3vrsaAiblg/640?wx_fmt=png&from=appmsg)

只要两个方程的参数a、b、a’、b’不是太奇怪，我们就可以运用高超的数学技巧，得到x和y的一般表达式：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FibK1j7BNb3SRtsmN8OXtBJp0vPibDUouVD0OR7UsSKNhm8S3W4Cg47TOj0LcxJfu0SshcOj4dbLug/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FibK1j7BNb3SRtsmN8OXtBJNBooxiauRHIwTXiaGicEkyMEJPbOwdAHNeOBLyCjv92hRhZEV4BHvUGQw/640?wx_fmt=png&from=appmsg)

现在的小学生应该可以轻而易举地写出代码来解决此类问题，然而在19世纪，要解决这个问题，缺少的不是思维，而是对机械的理解。在那个没有电子学知识的世纪，巴贝奇只能想象依靠机械装置来设计一种运算机器，把能量转换成运算：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FibK1j7BNb3SRtsmN8OXtBJgMecJibMz7yMc10iaxdOnCDibZxFubzIsVaNo4P7YRibPhxH7OZicIVCibLg/640?wx_fmt=png&from=appmsg)

在这种今天看起来有点滑稽的设计思想（不过据说有很多反对电动汽车的人信奉这种机械原教旨主义，甚至希望来一套内燃机计算机，可以去学习下当年的设计）的驱动下，巴贝奇提出了类似冯诺依曼结构（计算设备和存储设备）来运行的程序。计算x的基本思路用下面的表格来表示，这里面第一次出现了变量（v1到v7，有点像CPU的寄存器）的思想：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FibK1j7BNb3SRtsmN8OXtBJg1GjW1ayKiaoia1rODK6lThkgOKSzHp8ic5dyviaqQZ2ILn0yYDiaPIycDQ/640?wx_fmt=png&from=appmsg)

抽象下来的算法就是：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FibK1j7BNb3SRtsmN8OXtBJ77swjVDXSX2gp5gSnTC2r6P5eItBCDibHxaHJPgQ4icGb3DuWRW6L67w/640?wx_fmt=png&from=appmsg)

同样，运算y也是用这套程序：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FibK1j7BNb3SRtsmN8OXtBJzEmnfia5876HqaDEF9SwT4ShTnVMlNnDQsm1SPIt5tibTKnmrw7zea8A/640?wx_fmt=png&from=appmsg)

算法也类似：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FibK1j7BNb3SRtsmN8OXtBJibSIVV0jt5W2lhAptrobRyibYLBIGQmzORymqHsW5QUNsrz9xw6KPQ7w/640?wx_fmt=png&from=appmsg)

如果巴贝奇爵士穿越到今天，是会感叹人类的智力成就，还是为自己当年的卓越思想得以发扬光大而会心一笑呢？

具体的细节，可以参考CACM的文章：

> https://cacm.acm.org/research/the-first-computer-program/

关于巴贝奇和早期计算机的发展，有一本1982年出版的书籍《The Origins of Digital Computers: Selected Papers》可以参考阅读：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FibK1j7BNb3SRtsmN8OXtBJcKkgwghT1IxvuyEd5QqSrsAJiaGdsFTf8JKI4IFic95iaXsHCuzCKdibCQ/640?wx_fmt=png&from=appmsg)

---

记得刘慈欣在《朝闻道》里面有这么一段描写：

> “这个原始人仰望星空的时间超过了预警阀值，已对宇宙表现出了充分的好奇，到此为止，已在不同的地点观察到了十例这样的超限事件，符合报警条件。”
>
> “如果我没记错的话，你前面说过，只有当有能力产生创世能级能量过程的文明出现时，预警系统才会报警。”
>
> “你们看到的不正是这样一个文明吗？”
>
> 人们面面相窥，一片茫然。
>
> 排险者露出那毫无特点的微笑说：“这很难理解吗？当生命意识到宇宙奥秘的存在时，距它最终解开这个奥秘只有一步之遥了。”看到人们仍不明白，他接着说：“比如地球生命，用了四十多亿年时间才第一次意识到宇宙奥秘的存在，但那一时刻距你们建成爱因斯坦赤道只有不到四十万年时间，而这一进程最关键的加速期只有不到五百年时间。如果说那个原始人对宇宙的几分钟凝视是看到了一颗宝石，其后你们所谓的整个人类文明，不过是弯腰去拾它罢了。”

或许多年以后，面对超级人工智能，人类将会回想起查尔斯·巴贝奇写下第一个计算机程序的那个遥远的1837年的8月。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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