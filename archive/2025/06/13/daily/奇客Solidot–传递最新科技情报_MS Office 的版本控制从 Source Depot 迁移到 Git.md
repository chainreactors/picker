---
title: MS Office 的版本控制从 Source Depot 迁移到 Git
url: https://www.solidot.org/story?sid=81538
source: 奇客Solidot–传递最新科技情报
date: 2025-06-13
fetch_date: 2025-10-06T22:53:35.982921
---

# MS Office 的版本控制从 Source Depot 迁移到 Git

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

**本文已被查看 5084 次**

## MS Office 的版本控制从 Source Depot 迁移到 Git

[![微软](https://icon.solidot.org/images/topics/topicMicrosoft.png?123)](/search?tid=150 "微软")

[Wilson](/~Wilson) (42865)发表于 2025年06月12日 21时56分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=81538&appkey=1370085986&title=MS%20Office%20%E7%9A%84%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6%E4%BB%8E%20Source%20Depot%20%E8%BF%81%E7%A7%BB%E5%88%B0%20Git "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自凡尔纳地球三部曲**

本世纪初，微软面临一大难题：Windows 操作系统日益复杂，代码行数数以百万计，迫切需要某种版本控制系统。Git 当时还不存在。Subversion（SVN)才走出 CVS 的影子，商业版本控制系统 Perforce 则过于昂贵。微软毕竟是微软，它决定基于 Perforce 构建自己的系统。于是 Source Depot 诞生了。相比今天流行的 Git，Source Depot 在很多方面都更为繁琐，它不是分布式架构，而是集中式的，断网就意味着可以休息了。如果是远程办公，你需要 VPN 以及祈祷。尽管如此，它为微软可靠服务了很多年。但今天它也是呈现老态了。修补和维护日益昂贵。数百名微软工程师耗时数年终于将版本控制从 Source Depot 迁移到了 Git。四千名工程师工作的 MS Office 办公软件项目切换到了 Git。
danielsada.tech/blog/carreer-part-7-how-office-moved-to-git-and-i-loved-devex/

﻿

自由的保证是什么?是对自己不再感到羞耻。--尼采

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