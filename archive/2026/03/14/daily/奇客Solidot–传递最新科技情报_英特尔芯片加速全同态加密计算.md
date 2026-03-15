---
title: 英特尔芯片加速全同态加密计算
url: https://www.solidot.org/story?sid=83765
source: 奇客Solidot–传递最新科技情报
date: 2026-03-14
fetch_date: 2026-03-15T04:34:27.405677
---

# 英特尔芯片加速全同态加密计算

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260314)
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

**本文已被查看 725 次**

## 英特尔芯片加速全同态加密计算

[![加密技术](https://icon.solidot.org/images/topics/topicencryption.png?123)](/search?tid=70 "加密技术")
[![Intel](https://icon.solidot.org/images/topics/topicintel.png?123)](/search?tid=80 "Intel")

[Edwards](/~Edwards) (42866)发表于 2026年03月14日 22时05分 星期六 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=83765&appkey=1370085986&title=%E8%8B%B1%E7%89%B9%E5%B0%94%E8%8A%AF%E7%89%87%E5%8A%A0%E9%80%9F%E5%85%A8%E5%90%8C%E6%80%81%E5%8A%A0%E5%AF%86%E8%AE%A1%E7%AE%97 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自三个太阳**

全同态加密（fully homomorphic encryption，FHE）允许对密文进行特定的代数运算得到仍然是加密的结果，与对明文进行同样的运算再将结果加密一样。这项技术可以在加密的数据中进行检索、比较等操作，整个处理过程中无需对数据进行解密。同态加密技术从根本上解决将数据及其操作委托给第三方时的保密问题。今天的文件通常是在传输和存储时加密，使用时解密，存在安全漏洞，FHE 可解决该问题。然而 FHE 在今天的普通 CPU 和 GPU 上执行运算的速度都非常慢，所需计算时间可能比直接处理解密后的数据要慢数千倍，甚至数万倍。创业公司和芯片巨头都在竞相推出 FHE 加速器。英特尔的方案就是 Heracles 芯片，使用 3 纳米 FinFET 工艺制造，相比其顶尖服务器 CPU 加速 5000 倍。在演示中，使用 Xeon 服务器 CPU 上执行一个 FHE 计算所需时间需要 15 毫秒，而 Heracles 仅只需要 14 微秒。Heracles 的核心是 64 个计算核心，排列成 8×8 的网格。计算核心旨在并行执行 FHE 计算中的多项式运算、数据处理等操作。
https://spectrum.ieee.org/fhe-intel

[回复](/comments?sid=83765&op=reply&type=story)

﻿

所谓现实只不过是一个错觉，虽然这个错觉非常持久。--爱因斯坦

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260314)
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