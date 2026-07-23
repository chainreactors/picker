---
title: 数学家仍然不知道乘法的最快方法
url: https://www.solidot.org/story?sid=84899
source: 奇客Solidot–传递最新科技情报
date: 2026-07-22
fetch_date: 2026-07-23T05:10:28.103829
---

# 数学家仍然不知道乘法的最快方法

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260722)
  [往日投票](/polllist)
* 皮肤

  [蓝色](/?theme=blue)
  [橙色](/?theme=yellow)
  [绿色](/?theme=green)
  [浅绿色](/?theme=clightgreen)

* 分类:
* [首页](//www.solidot.org/)
* [Linux](//linux.solidot.org/)
* [科学](//science.solidot.org/)
* [科技](//technology.solidot.org/)
* [移动](//mobile.solidot.org/)
* [苹果](//apple.solidot.org/)
* [硬件](//hardware.solidot.org/)
* [软件](//software.solidot.org/)
* [安全](//security.solidot.org/)
* [游戏](//games.solidot.org/)
* [书籍](//books.solidot.org/)
* [idle](//idle.solidot.org/)
* [云计算](//cloud.solidot.org/)
* [高飞的电子替身](//story.solidot.org/)

## 关注我们：

solidot新版网站常见问题，请点击[这里](/QA)查看。

## 消息

**本文已被查看 1757 次**

## 数学家仍然不知道乘法的最快方法

[![数学](https://icon.solidot.org/images/topics/topicmath.png?123)](/search?tid=41 "数学")

[Edwards](/~Edwards) (42866)发表于 2026年07月23日 00时52分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=84899&appkey=1370085986&title=%E6%95%B0%E5%AD%A6%E5%AE%B6%E4%BB%8D%E7%84%B6%E4%B8%8D%E7%9F%A5%E9%81%93%E4%B9%98%E6%B3%95%E7%9A%84%E6%9C%80%E5%BF%AB%E6%96%B9%E6%B3%95 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自超时空碎片**

我们在小学时学习的多位数乘法叫竖式乘法，其时间复杂度为 O(n²)，即位数越长，计算量随位数的平方增长。举例来说，两个两位数相乘，需要进行四次计算；两个三位数相乘，需要进行九次计算。位数越长，计算量会越来越惊人。那么 O(n²)是否是乘法的速度极限呢？苏联著名数学教授 Andrey Kolmogorov 在 1960 年的一次研讨会上讨论了这一猜想，仅仅一周之后，23 岁的学生 Anatoly Karatsuba 就给出了否定答案。他发现可以用简单快速的加法去替代费劲的乘法计算，而两个 n 位数相加的时间复杂度仅为 O(n)，加法只需要遍历数字一次，而乘法需要对 n 位数的每一位进行完整遍历。通过这一代数技巧，他将乘法的时间复杂度减少到 O(n^1.585)，比O(n²) 快得多。Karatsuba 算法的优势只有在数字较大时才会体现出来。Python 语言就使用了混合方法，当数字较小时使用小学乘法，当数字大于 630 位十进制数时改用 Karatsuba 的算法。2019 年数学家 David Harvey 和 Joris van der Hoeven 找到了一种比 Karatsuba 算法更快的方法，其时间复杂度为 O(n × log n)，但它相对于 Karatsuba 算法的优势只有在数非常非常大时才会体现。Harvey-van der Hoeven 算法被普遍认为是乘法的最快方法，但目前尚无正式证明。
https://www.scientificamerican.com/article/mathematicians-still-dont-know-the-fastest-way-to-multiply-numbers/
https://zh.wikipedia.org/wiki/%E4%B9%98%E6%B3%95%E7%AE%97%E6%B3%95

[回复](/comments?sid=84899&op=reply&type=story)

﻿

只有两种编程语言：一种是天天挨骂的，另一种是没人用--Bjarne Stroustrup

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260722)
* [过去的投票](/polllist)
* [编辑介绍](/authors)
* [隐私政策](/privacy)
* [使用条款](/terms)
* [网站介绍](/introd)
* [RSS](/index.rss)

本站提到的所有注册商标属于他们各自的所有人所有，评论属于其发表者所有，其余内容版权属于 solidot.org(2009-) 所有 。

[![php](https://icon.solidot.org/images/btn/php.gif)](//php.net/ "PHP 服务器")
[![apache](https://icon.solidot.org/images/btn/apache.gif)](//apache.org/ "Apache 服务器")
[![mysql](https://icon.solidot.org/images/btn/mysql.gif)](//www.mysql.com/ "MySQL")

[![](https://icon.solidot.org/images/btn/solidot-s.gif)](//www.solidot.org "solidot.org")

京ICP证161336号    [京ICP备15039648号-15](http://beian.miit.gov.cn) 北京市公安局海淀分局备案号：11010802021500 [![](//icon.zhiding.cn/beian/icon.png)](//icp.valu.cn/search/domain/solidot.org?verifyCode=pu7c4)

举报电话：010-62641205　涉未成年人举报专线：010-62641208 举报邮箱：jubao@zhiding.cn　网上有害信息举报专区：<https://www.12377.cn>