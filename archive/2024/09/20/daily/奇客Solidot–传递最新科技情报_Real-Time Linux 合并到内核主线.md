---
title: Real-Time Linux 合并到内核主线
url: https://www.solidot.org/story?sid=79288
source: 奇客Solidot–传递最新科技情报
date: 2024-09-20
fetch_date: 2025-10-06T18:27:14.511194
---

# Real-Time Linux 合并到内核主线

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

**本文已被查看 23535 次**

## Real-Time Linux 合并到内核主线

[![Linux](https://icon.solidot.org/images/topics/topiclinux.png?123)](/search?tid=7 "Linux")

[Wilson](/~Wilson) (42865)发表于 2024年09月19日 14时56分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=79288&appkey=1370085986&title=Real-Time%20Linux%20%E5%90%88%E5%B9%B6%E5%88%B0%E5%86%85%E6%A0%B8%E4%B8%BB%E7%BA%BF "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自诺比、龙和意识星云**

在长达 20 年之后，Real-Time Linux(PREEMPT\_RT)合并到内核主线。从 Linux 6.12 开始，所有发行版都将包含实时 Linux 代码。这意味着 Linux 将开始运行在更多任务关键设备和工业硬件上。实时操作系统对时间限制非常严格，需要确保关键任务在指定时间期限内完成。实时内核代码合并到主线的最后一个障碍是重新设计 print\_k 函数。print\_k 函数最早是 Linus Torvalds 本人开发用于调试的工具，但程序在调用 print\_k 时会产生硬延迟，这对于实时系统是不可接受的。今年初内核社区终于在重设 print\_k 上达成了一致。
https://www.zdnet.com/article/20-years-later-real-time-linux-makes-it-to-the-kernel-really/

﻿

善待他人，即是最善待自己。

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