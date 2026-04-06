---
title: AWS 工程师报告 Linux 7.0 下 PostgreSQL 性能暴降一半
url: https://www.solidot.org/story?sid=83966
source: 奇客Solidot–传递最新科技情报
date: 2026-04-05
fetch_date: 2026-04-06T04:44:16.988241
---

# AWS 工程师报告 Linux 7.0 下 PostgreSQL 性能暴降一半

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260405)
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

**本文已被查看 2103 次**

## AWS 工程师报告 Linux 7.0 下 PostgreSQL 性能暴降一半

[![Linux](https://icon.solidot.org/images/topics/topiclinux.png?123)](/search?tid=7 "Linux")
[![数据库](https://icon.solidot.org/images/topics/topicdatabases.png?123)](/search?tid=63 "数据库")

[Edwards](/~Edwards) (42866)发表于 2026年04月06日 00时33分 星期一 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=83966&appkey=1370085986&title=AWS%20%E5%B7%A5%E7%A8%8B%E5%B8%88%E6%8A%A5%E5%91%8A%20Linux%207.0%20%E4%B8%8B%20PostgreSQL%20%E6%80%A7%E8%83%BD%E6%9A%B4%E9%99%8D%E4%B8%80%E5%8D%8A "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自火星之剑**

亚马逊 AWS 工程师 Salvatore Dipietro 报告 Linux 7.0 下 PostgreSQL 的吞吐量和延迟性能出现了显著的下降。Linux 7.0 目前还在开发中，预计会在一两周内发布。测试显示，在基于 arm64 架构的 Graviton4 服务器上 PostgreSQL 的吞吐量仅为上个内核版本的 0.51 倍，原因是用户空间自旋锁导致花费的时间大幅增加。根本原因被认为是 Linux 7.0 新引入的对内核可用抢占模式的限制上。PostgreSQL 开发者要求在不同条件下重复进行更多测试。
https://www.phoronix.com/news/Linux-7.0-AWS-PostgreSQL-Drop
https://lore.kernel.org/lkml/yr3inlzesdb45n6i6lpbimwr7b25kqkn37qzlvvzgad5hfd7ut@xv4cihno76wu/

[回复](/comments?sid=83966&op=reply&type=story)

﻿

世界上只有两个东西是无限的，一为宇宙，一为人类的愚蠢，我所不能肯定的乃是前者。 --爱因斯坦

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260405)
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