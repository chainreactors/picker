---
title: 小朋友的新一期代码审计来了
url: https://mp.weixin.qq.com/s/b4O4Ngq9_8IVThBgHejLwA
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:41:19.477100
---

# 小朋友的新一期代码审计来了

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Dfrm5V3o6kT2AlibnodLaBNX7aY4l6skWTS068u2G5Xm0xM1QNmbwzXvODNmGav0xAMOV4rOvf7XjIY8k6Mv38zXXppLtOmkzAyMem1JlyqI/0?wx_fmt=jpeg)

# 小朋友的新一期代码审计来了

葡萄网络安全随记

![]()

在小说阅读器中沉浸阅读

以下文章来源于进击安全
，作者知名小朋友

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4Eu4ArzE5xKh7ouSAzvohwFkvzPibNQxs6X4k2SxgCvBA/0)

**进击安全**
.

主要分享一些个人实战经验，以及漏洞复现，代码审计，等等方面的文章，欢迎大家关注我的公众号呀，可以投稿哦，有稿费的哦，菜鸟路过～～～

历经四期培训，终于迎来了代码审计第五期培训，本次培训依旧一次报名一直可听，并且富含前面四期课程均可以听，先来看看之前的培训都有哪些内容，这里我给大家截屏看看。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/HBLcNkZ8PQddO5DZYzH4GcwlsOwEK5cR1A5XZuWXTP3ib3tWpcAtuLUaliasnZQvBmenGd0UNicFQOsJGyIzodicicg/640?from=appmsg)

一、往期-第四期课程

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dJGuszYr5iaRGiaZURAxJAROibCh1sjaZictcbC4iasuuOgCMQSDSwrG5Wfrx2QgfvKx8icDhm0gIia8fN6mThehEK8ww/640?from=appmsg)

###

### 我们先来看看上一期课程内容，内容如下，给各位师傅们讲解上一期课程讲解了哪些内容，包括相关的学员出货记录，以及部分课件内容。

![](https://mmbiz.qpic.cn/mmbiz_png/HD0HxvpnwC5ZeImfWYKsmFnrQxS8uec0lgeqCdbhfrzK5af1GicN0VznKVcCJFJwfqDVFIopkWP0OQxia5Y2Fj7g/640?&wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/vjKYWs9y65W5n4PxYWtJKL6NFQ5b33EDmVhhibZ7XqTbzFP6AKT75NO9ruuOia5WEJlbCukAFpHGbhicHv0elprLg/640?&wx_fmt=png)

往期-第四期基础课程

![](https://mmbiz.qpic.cn/sz_mmbiz_png/byR65XibZJfW0aVCxh4yatvn7mHPias6u1M2xpeaYD31jyyrHgz550eWgUu6O2KFmah7jZVsyceicfXzRh2nR2pyA/640?&wx_fmt=png)

###

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kQSvybwBicDpIW8MT6xrDThDicGiaR0VArHdxIjc6MWpTmwKP26E7tgvqLeAP3z8Aqbu34ckhRhExIPbNFgPxibBLFGzRIibs8y2Gms/640?wx_fmt=png&from=appmsg)

此为第四期基础课程，共计授课四十次，此外第四期相较于第三期新增了APP、小程序、WEB逆向，同时主线仍然在代码审计上面，其中基础课程主要目的为：

掌握代码审计思路、完成0-1、能够独立开始审计项目。

讲解方向如下：

✅ NET代码审计

✅ APP、小程序、WEB逆向

✅ JAVA代码审计

（当然个人认为讲的最好的是JAVA代码审计，而且此次代码审计偏向0-1的实现，更多的是讲解完漏洞原理之后小朋友带着进行实战代码审计，分析各个项目，从理论→实践的演变，当然小朋友们每个课程都是这种方式。）

![](https://mmbiz.qpic.cn/mmbiz_png/HD0HxvpnwC5ZeImfWYKsmFnrQxS8uec0lgeqCdbhfrzK5af1GicN0VznKVcCJFJwfqDVFIopkWP0OQxia5Y2Fj7g/640?&wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/vjKYWs9y65W5n4PxYWtJKL6NFQ5b33EDmVhhibZ7XqTbzFP6AKT75NO9ruuOia5WEJlbCukAFpHGbhicHv0elprLg/640?&wx_fmt=png)

往期-第四期进阶课程

![](https://mmbiz.qpic.cn/sz_mmbiz_png/byR65XibZJfW0aVCxh4yatvn7mHPias6u1M2xpeaYD31jyyrHgz550eWgUu6O2KFmah7jZVsyceicfXzRh2nR2pyA/640?&wx_fmt=png)

###

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kTvh6IEiaUOx9zmdDewibx5vAw5RAa841qEM2fv4RqyjnTXpBkUnLRE64jDuNRCnwEagIYghnFVkbmy02icfNehYumXg2xibRDAtibQ/640?wx_fmt=png&from=appmsg)

    为什么在第四期课程分为了基础课程以及进阶课程，就是因为发现学员大部分都是为了审计而去审计，单一的去使用某一个方法审计漏洞，而不会进行漏洞的组合拳，扩大危害，**虽然自己都是实战案例，但是发现学员都是跟着案例当中的漏洞去套用在了自己的源码\项目当中**。

所以开启了第四期进阶代码审计课程，课程目的主要为：

✅ 深入理解鉴权

✅ 漏洞组合拳扩大危害

✅ 尝试0-1贴合多数学员完成前台RCE出货

（本次授课累计20余次，专项针对以上目的，大量分析鉴权&绕过、组合拳利用、前台RCE）

![](https://mmbiz.qpic.cn/mmbiz_png/HD0HxvpnwC5ZeImfWYKsmFnrQxS8uec0lgeqCdbhfrzK5af1GicN0VznKVcCJFJwfqDVFIopkWP0OQxia5Y2Fj7g/640?&wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/vjKYWs9y65W5n4PxYWtJKL6NFQ5b33EDmVhhibZ7XqTbzFP6AKT75NO9ruuOia5WEJlbCukAFpHGbhicHv0elprLg/640?&wx_fmt=png)

往期-第四期-部分学员报喜&课件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/byR65XibZJfW0aVCxh4yatvn7mHPias6u1M2xpeaYD31jyyrHgz550eWgUu6O2KFmah7jZVsyceicfXzRh2nR2pyA/640?&wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kTic5f3Mrt7JXiaHWJ9Nl1VSSWLpOnVQFUT7vhTTXdMYZS0nZc6I2nYIWdibY2EsmoiatfasFqpRVv1INibjxCuSNAAMd8wBzz9Iks8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kTkjqJ6kNtzFzc3k1VDcYCV2dSaXmoBBDblMzibyVoiaDQrmZIRqIbR4jtOFErGibIJBNB4q2pb6oUfibrbwicuXWqwMngZcnMj1lhE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kQZ0NOdTcycWq8h9wpct48nicHIxZ4wxiaRroW8NqHbBgNXyONWhrO7gGYia4UUENTNyH7TrIriaSibibShnqLtQdDYhRt7enIeCrZw4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kSTA1uRxJUNRoHhzKYQWQsiaaMicIicIYq07UVqw7LqgpE6BHmHZZX1JKLGQJ7DT137icxMIlvqx2S7Ma0ZqIRia1ibRAFcnhPRsGz5o/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kSztHdBNyfWI3TiaK1hrBgPozjibViaHiaWVoGxl4kPiaVriaP9QnaeY5kq1WoCtBCaSeP17G3pRNY4T56sIdDC01KlhUAlD5p4JoXuk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kSqHH6XNC8YDVXibOVdtvSxY7eicndI2165ZDjOLPicKuE5LhERxmnS4M6cSE4Bhdics6n1D9UiaWxNde5Da2LEo708iaygibkqX7wsib0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kTmOBHbaRfgGCypCVFp4KBic1wBfAaojBC3dO5iaUo9fVhDvAYudntjR2LSTNSDf72vho6dNh4x2Nic0fAicBwgnbjOsh88ibZVyO7U/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kRtQlWksfBNUgoGfXG3LNwOoibfx5MIoxwpaibCD5iaOeOqLY0RZA9Mh6luVFtbpw7CQjMhqibRw6zRdeAfGngXTGpcGohibqggMHiaw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kS7nhclW0wguh1cLz2wia6LibkmdYXUlCXicXh4NfwLadnVdibzqO0icwCMvT2H9iayFjMSeTtdibxySticP6A3bq7J8icty9h2LXoBXgAQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kQfPVhrqr5BNqzwKicWjvafgoFuo7bCHt9qboBYZGwVfo14lQKmLJGgRTr0l6kr0mZwLKCdH89oaqz577yRqSKqwNhONnqibBGtA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kSI5nOYelnDU8BiaLvUaqBElaiaBRibicDmojmbAltCEwXbaBVNFxc8SxiahlZndG823etuPI1t9wrlX2ZNutwWuJ7icXZD2rRUFpwoY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kQRJEN3P8LI8fO9r9YHtmJ1d4OKqnNhvForuCqKv7pnxhthkIjrjXxlqicZv99NEddT37z1bcc4NW7NuSllPjP2wJnsdbzMl5Fg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/G4zicxKmtXXhicvpUX9R0fxBOic1XNQdlPRrh27zNXQlQ9UYKWLzvZvPYqu3licIgC4v7j1ArN4vfJjoxp4MgTvFmA/640?from=appmsg)

上下滑动查看更多

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pu52Sn0jPu0EbVUSia7W7sUxTVicmhGmYTkl23iaZv7FdOTQE7bh7lb3gMR7hqLULFpHDq5UyDClYpOMAgnLljB2w/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kSTA1uRxJUNRoHhzKYQWQsiaaMicIicIYq07UVqw7LqgpE6BHmHZZX1JKLGQJ7DT137icxMIlvqx2S7Ma0ZqIRia1ibRAFcnhPRsGz5o/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kQZ0NOdTcycWq8h9wpct48nicHIxZ4wxiaRroW8NqHbBgNXyONWhrO7gGYia4UUENTNyH7TrIriaSibibShnqLtQdDYhRt7enIeCrZw4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kTkjqJ6kNtzFzc3k1VDcYCV2dSaXmoBBDblMzibyVoiaDQrmZIRqIbR4jtOFErGibIJBNB4q2pb6oUfibrbwicuXWqwMngZcnMj1lhE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kTic5f3Mrt7JXiaHWJ9Nl1VSSWLpOnVQFUT7vhTTXdMYZS0nZc6I2nYIWdibY2EsmoiatfasFqpRVv1INibjxCuSNAAMd8wBzz9Iks8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kQ3CrxibSp0ccicnwpoAIxCD41vlbrLv2uowHYvZY3E4TNd5iabTdTOFwiaSLVhMaDXQOicM19xyb8w5IViax7HaiaorpJXicyB4ByQXvA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kTa2PibaiaOk8IjiciamYEF2AgYicZxvsK6iarrPlwZlL0sr3iaNVX9SbGtAicMZl4icLeKCo6GDoP3NjicleBY22gh0QGUjpolnSzu6OWVA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kQRJEN3P8LI8fO9r9YHtmJ1d4OKqnNhvForuCqKv7pnxhthkIjrjXxlqicZv99NEddT37z1bcc4NW7NuSllPjP2wJnsdbzMl5Fg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kSI5nOYelnDU8BiaLvUaqBElaiaBRibicDmojmbAltCEwXbaBVNFxc8SxiahlZndG823etuPI1t9wrlX2ZNutwWuJ7icXZD2rRUFpwoY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dfrm5V3o6kQfPVhrqr5BNqzwKicWjvafgoFuo7bCHt9qboBYZGwVfo14lQKmLJGgRTr0l6kr0mZwLKCdH89oaqz577yRqSKqwNhONnqibBGtA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kS7nhclW0wguh1cLz2wia6LibkmdYXUlCXicXh4NfwLadnVdibzqO0icwCMvT2H9iayFjMSeTtdibxySticP6A3bq7J8icty9h2LXoBXgAQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kRtQlWksfBNUgoGfXG3LNwOoibfx5MIoxwpaibCD5iaOeOqLY0RZA9Mh6luVFtbpw7CQjMhqibRw6zRdeAfGngXTGpcGohibqggMHiaw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kTmOBHbaRfgGCypCVFp4KBic1wBfAaojBC3dO5iaUo9fVhDvAYudntjR2LSTNSDf72vho6dNh4x2Nic0fAicBwgnbjOsh88ibZVyO7U/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kSqHH6XNC8YDVXibOVdtvSxY7eicndI2165ZDjOLPicKuE5LhERxmnS4M6cSE4Bhdics6n1D9UiaWxNde5Da2LEo708iaygibkqX7wsib0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Dfrm5V3o6kREA7K2B8fn46xvuv7KYLUQeG8zx8D8jqw7Zv5ECfV...