---
title: AMD 从 Chiplet 中得到的教训
url: https://www.solidot.org/story?sid=75365
source: 奇客Solidot–传递最新科技情报
date: 2023-06-29
fetch_date: 2025-10-04T11:48:54.640286
---

# AMD 从 Chiplet 中得到的教训

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20251003)
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

**本文已被查看 8450 次**

## AMD 从 Chiplet 中得到的教训

[![AMD](https://icon.solidot.org/images/topics/topicamd.png?123)](/search?tid=22 "AMD")

[Wilson](/~Wilson) (42865)发表于 2023年06月28日 18时42分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=75365&appkey=1370085986&title=AMD%20%E4%BB%8E%20Chiplet%20%E4%B8%AD%E5%BE%97%E5%88%B0%E7%9A%84%E6%95%99%E8%AE%AD "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自阿尔法计划**

过去五年处理器从单个硅片转变成小芯片（Chiplet）集，小芯片们像大芯片一样集体行动。这种方法意味着芯片的不同功能块能用最适合的技术构建，有利于降低成本。AMD 产品技术架构师 Sam Naffziger 是小芯片方法的早期推动者，他接受采访谈论 AMD 从中得到的教训。他说小芯片架构的目的之一是对软件完全透明，因为软件很难改变。AMD 第二代 EPYC CPU 由一个位于中心位置的 I/O 小芯片和周围环绕的计算芯片构成。这种布局减少了内存延迟，消除了第一代芯片遭遇的软件挑战。AMD 最新的 MI300 加速器集成了 CPU 芯片和 GPU 芯片，对软件而言意味着可以共享内存地址空间，软件不再需要管理内存，降低了编程难度。
https://spectrum.ieee.org/chiplet

﻿

活了一百年却只能记住30M字节是荒谬的。你知道，这比一张压缩盘还要少。人类境况正在变得日趋退。--Marvin Minsky

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20251003)
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