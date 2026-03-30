---
title: Google TurboQuant AI 压缩算法大幅减少大模型内存使用
url: https://www.solidot.org/story?sid=83907
source: 奇客Solidot–传递最新科技情报
date: 2026-03-29
fetch_date: 2026-03-30T04:46:32.574427
---

# Google TurboQuant AI 压缩算法大幅减少大模型内存使用

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260329)
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

**本文已被查看 1997 次**

## Google TurboQuant AI 压缩算法大幅减少大模型内存使用

[![Google](https://icon.solidot.org/images/topics/topicgoogle.png?123)](/search?tid=26 "Google")
[![人工智能](https://icon.solidot.org/images/topics/topicAI.png?123)](/search?tid=151 "人工智能")

[Edwards](/~Edwards) (42866)发表于 2026年03月29日 19时05分 星期日 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=83907&appkey=1370085986&title=Google%20TurboQuant%20AI%20%E5%8E%8B%E7%BC%A9%E7%AE%97%E6%B3%95%E5%A4%A7%E5%B9%85%E5%87%8F%E5%B0%91%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%86%85%E5%AD%98%E4%BD%BF%E7%94%A8 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自人猿泰山之英雄归来**

Google 研究院发布了压缩算法 TurboQuant，能在大幅减少大模型内存占用的同时提高速度和维持精度。TurboQuant 旨在减小键值缓存的大小，被称为是储存重要信息减少再计算的“数字查找表（digital cheat sheet）”。大模型并不理解任何东西，它通过映射词元文本语义的向量去模拟对事物的理解。大模型的向量通常使用 XYZ 坐标进行编码，而实现 TurboQuant 压缩的系统将向量转换为笛卡尔坐标系的极坐标，向量被简化为两类信息：半径（核心数据强度）和方向（数据含义）。如果使用 XYZ 坐标编码向量，那么特定位置可以编码为“向东走 3 个街区，向北走 4 个街区”，采用笛卡尔坐标编码向量，那么同样的信息编码为“沿 37 度方向走 5 个街区” ，简化了空间节省了计算。Google 的早期测试显示，TurboQuant 在部分测试中实现了 8 倍的性能提升，内存占用减少到原来的六分之一，同时质量没有损失。实现 TurboQuant 算法将有助于降低 AI 模型的运行成本和内存占用，但也可能推动更复杂模型的出现，因此对降低内存价格可能没有什么效果。
https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/
https://arxiv.org/abs/2504.19874

[回复](/comments?sid=83907&op=reply&type=story)

﻿

花代价所换来的一点才智，抵过别人传授的数倍不止。

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260329)
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