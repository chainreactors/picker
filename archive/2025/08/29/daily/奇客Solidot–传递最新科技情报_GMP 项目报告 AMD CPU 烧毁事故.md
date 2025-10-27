---
title: GMP 项目报告 AMD CPU 烧毁事故
url: https://www.solidot.org/story?sid=82160
source: 奇客Solidot–传递最新科技情报
date: 2025-08-29
fetch_date: 2025-10-07T00:48:00.018622
---

# GMP 项目报告 AMD CPU 烧毁事故

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20251006)
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

**本文已被查看 5247 次**

## GMP 项目报告 AMD CPU 烧毁事故

[![AMD](https://icon.solidot.org/images/topics/topicamd.png?123)](/search?tid=22 "AMD")

[Edwards](/~Edwards) (42866)发表于 2025年08月28日 14时02分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=82160&appkey=1370085986&title=GMP%20%E9%A1%B9%E7%9B%AE%E6%8A%A5%E5%91%8A%20AMD%20CPU%20%E7%83%A7%E6%AF%81%E4%BA%8B%E6%95%85 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自泰山复仇**

GNU 多重精度运算库（GNU Multiple Precision Arithmetic Library，简称 GMP)项目披露该项目可能与 AMD Ryzen 9000 系列 CPU 不兼容。过去半年发生了两起测试时 Ryzen 9950X CPU 烧毁事故，他们的机器没有使用媒体广泛报道过的华擎主板。第一起发生在 2025 年 2 月，主板是华硕的 Prime B650M-K，散热器是 Noctua NH-U9S；第二起发生在 2025 年 8 月 24 日，主板是华硕 Prime B650M-A WIFI II，散热器型号相同。两起事故发生时 CPU 处于最大负载状态，运行手工编写的 asm 循环。两块 CPU 烧毁的情况都差不多，针脚侧发现了一块约 25 平方毫米的变色区域。开发者表示不清楚事故原因，他们没有超频或超压，上一代 Ryzen 7950X 在相同负载运行更长时间都没有出现问题。
gmplib.org/gmp-zen5

[回复](/comments?sid=82160&op=reply&type=story)

﻿

死会引人哭泣。虽则如此，人生的三分之一却在睡眠中打发掉了。--拜伦

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20251006)
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