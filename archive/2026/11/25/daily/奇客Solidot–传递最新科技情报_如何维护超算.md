---
title: 如何维护超算
url: https://www.solidot.org/story?sid=85989
source: 奇客Solidot–传递最新科技情报
date: 2026-11-25
fetch_date: 2026-11-26T10:13:33.431601
---

# 如何维护超算

* 至顶科技：
* [至顶网](https://www.zhiding.cn/ "至顶网")
* [科技行者](https://www.techwalker.com/ "科技行者")
* [Solidot](https://www.solidot.org/ "Solidot")

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20261125)
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

**本文已被查看 3123 次**

## 如何维护超算

[![超级电脑](https://icon.solidot.org/images/topics/topicsuperpc.png?123)](/search?tid=124 "超级电脑")

[Edwards](/~Edwards) (42866)发表于 2026年11月25日 22时18分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=85989&appkey=1370085986&title=%E5%A6%82%E4%BD%95%E7%BB%B4%E6%8A%A4%E8%B6%85%E7%AE%97 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自火星众神**

美国橡树岭国家实验室的超算 Frontier 有数以千计的计算节点，维护其正常工作是一大挑战。无法纠正的内存错误，维护失误都会引发问题。技术人员在狭窄紧密的机架之间工作时可能会重启错误的节点，或意外触碰相邻节点的电源。硬件故障可能会影响单个节点，但对于运行在数千个处理器上的模拟任务而言，这可能导致整个进程逐渐停止工作。随之而来的问题是：计算进度最近储存的时间？多少计算工作需要重做？调度程序多久才能让该任务重新运行？Frontie 超算上 HBM 内存发生无法纠正双位错误的概率是每天 1.5 次，相比下该实验室的上一代超算 Summit 每两周才会出现一次此类错误，原因是 Frontie 的内存总容量是 Summit 的 16 倍以上。除了内存，有问题的 GPU 固件、互连故障都会导致严重问题。一个 GPU 故障，使用 1,024 个 GPU 的计算任务就可能被迫停止。有性能问题的 GPU 同样会带来问题：如果某个参与计算的 GPU 单元运行速度只有正常的 80%，其它单元需要停下来等待它。超算使用检查点（checkpointing）机制定时保存计算结果，一旦出错模拟任务无需从头开始。
https://www.theregister.com/systems/2026/11/25/the-worlds-fastest-computers-have-a-problem-keeping-the-work-running/5311710

[回复](/comments?sid=85989&op=reply&type=story)

﻿

人们还往往把真理和错误混在一起去教人，而坚持的却是错误。--歌德

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20261125)
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