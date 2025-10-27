---
title: 详解龙芯 3A6000
url: https://www.solidot.org/story?sid=77616
source: 奇客Solidot–传递最新科技情报
date: 2024-03-18
fetch_date: 2025-10-04T12:08:06.742242
---

# 详解龙芯 3A6000

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

**本文已被查看 7870 次**

## 详解龙芯 3A6000

[![硬件](https://icon.solidot.org/images/topics/topichardware.gif?123)](/search?tid=14 "硬件")

[Wilson](/~Wilson) (42865)发表于 2024年03月17日 21时45分 星期日 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=77616&appkey=1370085986&title=%E8%AF%A6%E8%A7%A3%E9%BE%99%E8%8A%AF%203A6000%20 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自夜屋**

Chips and Cheese 详细分析了龙芯公司最新的四核八线处理器 3A6000，测试显示它的性能与 AMD 的 Zen1 相当。3A6000 频率为 2.5 GHz，使用了新的 LA664 核心，相比上一代 3A5000 的 LA464 核心，LA664 是一大飞跃。LA664 拥有更大更深的管线和更多执行单元，加入了对同步多线程 (SMT)的支持。以 7-Zip 压缩为例，3A6000 相比 3A5000 性能提升约 38%，如果考虑 SMT 提升幅度还会更大。如果每个核心加载一个线程，在 7-Zip 压缩任务中四个 LA664 核心相当于四个 Zen1 核心。在 libx264 视频编码任务中，3A6000 与 Zen1 各有胜负。Zen1 至今仍然具有实用价值，因此 3A6000 可以轻松完成轻量级的日常工作任务。但软件生态系统则是另一回事，3A6000 是基于 MIPS 等指令集，意味着不可能运行 Windows，只能运行 Linux 发行版。3A6000 具有 Zen1 相当的单线程性能，但只有 4 个核心，对今天的 CPU 而言，四核已经越来越少见了。
https://chipsandcheese.com/2024/03/13/loongson-3a6000-a-star-among-chinese-cpus/

﻿

如果你想走到高处，就要使用自己的两条腿！不要让别人把你抬到高处；不要坐在别人的背上和头上。 --尼采·F.W.

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