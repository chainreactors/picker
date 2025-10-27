---
title: 英特尔 4.75 亿美元错误：奔腾浮点除 Bug
url: https://www.solidot.org/story?sid=80180
source: 奇客Solidot–传递最新科技情报
date: 2024-12-30
fetch_date: 2025-10-06T19:36:31.710528
---

# 英特尔 4.75 亿美元错误：奔腾浮点除 Bug

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20251005)
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

**本文已被查看 5200 次**

## 英特尔 4.75 亿美元错误：奔腾浮点除 Bug

[![Bug](https://icon.solidot.org/images/topics/topicbug.png?123)](/search?tid=53 "Bug")
[![Intel](https://icon.solidot.org/images/topics/topicintel.png?123)](/search?tid=80 "Intel")

[Wilson](/~Wilson) (42865)发表于 2024年12月29日 23时27分 星期日 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=80180&appkey=1370085986&title=%E8%8B%B1%E7%89%B9%E5%B0%94%204.75%20%E4%BA%BF%E7%BE%8E%E5%85%83%E9%94%99%E8%AF%AF%EF%BC%9A%E5%A5%94%E8%85%BE%E6%B5%AE%E7%82%B9%E9%99%A4%20Bug "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自图书馆员与黄金锅**

1993 年英特尔发布了奔腾高性能处理器。一年之后 Nicely 教授在研究孪生素数时发现他的奔腾计算机在执行浮点除时会产生错误结果。1/824633702441 在三台奔腾计算机上的结果都是错误的，但旧计算机却能给出正确的答案。Nicely 教授其实不是第一个发现浮点除 bug 的人，几个月前英特尔内部测试就发现了该 bug，它估计出错的概率非常低，大约为 1/90 亿，认为问题微不足道，虽然如此它仍然悄悄修改了电路以修复问题。Nicely 教授在发现问题之后致电了英特尔技术支持，但对方不予理睬。于是他向计算机杂志和业内知名人士发送了该 bug 的电邮，其中一位收件人是《Undocumented DOS》作者 Andrew Schulman，他转发给了一家 DOS 软件公司的联合创始人 Richard Smith，Smith 随后将其发布在了 Compuserve 论坛上。Electronic Engineering Times 杂志的一位记者看到帖子后在杂志上撰写了有关奔腾 bug 的报道。英特尔解释说，bug 存在于被称为 PLA(Programmable Logic Array)的组件上，它充当了除法运算的查找表。它已经修复了 bug 将会为客户替换有问题的处理器。问题本应该就此了结了，然而英特尔对想要更换处理器的客户施加了限制，要求客户说服工程师他们需要如此高的精度才能替换，此举激怒了客户，再次引发了广泛的负面报道。当年 12 月 12 日 IBM 宣布停售奔腾计算机，英特尔随后屈服，宣布召回所有有缺陷的芯片，这次召回花费了英特尔 4.75 亿美元。
https://www.righto.com/2024/12/this-die-photo-of-pentium-shows.html
https://zh.wikipedia.org/wiki/%E5%A5%94%E8%85%BE%E6%B5%AE%E7%82%B9%E9%99%A4%E9%94%99%E8%AF%AF

﻿

柔和回答， 使怒消退。 言语暴戾， 触动怒气——箴言篇 15:1

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20251005)
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