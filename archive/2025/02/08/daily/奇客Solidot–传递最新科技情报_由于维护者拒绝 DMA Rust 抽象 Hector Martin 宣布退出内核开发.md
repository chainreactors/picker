---
title: 由于维护者拒绝 DMA Rust 抽象 Hector Martin 宣布退出内核开发
url: https://www.solidot.org/story?sid=80499
source: 奇客Solidot–传递最新科技情报
date: 2025-02-08
fetch_date: 2025-10-06T20:37:45.299448
---

# 由于维护者拒绝 DMA Rust 抽象 Hector Martin 宣布退出内核开发

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

**本文已被查看 34847 次**

## 由于维护者拒绝 DMA Rust 抽象 Hector Martin 宣布退出内核开发

[![Linux](https://icon.solidot.org/images/topics/topiclinux.png?123)](/search?tid=7 "Linux")

[Wilson](/~Wilson) (42865)发表于 2025年02月07日 23时28分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=80499&appkey=1370085986&title=%E7%94%B1%E4%BA%8E%E7%BB%B4%E6%8A%A4%E8%80%85%E6%8B%92%E7%BB%9D%20DMA%20Rust%20%E6%8A%BD%E8%B1%A1%20Hector%20Martin%20%E5%AE%A3%E5%B8%83%E9%80%80%E5%87%BA%E5%86%85%E6%A0%B8%E5%BC%80%E5%8F%91 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自发条女孩**

Rust-for-Linux 进入内核的努力遭到了内核维护者 Christoph Hellwig 的强烈反对。他拒绝了 DMA Rust 抽象补丁，不希望 Rust 代码靠近 DMA 层。他说支持另一种语言（他明确表示指的是任何语言，而不是特指 Rust）将使整个 Linux 项目无法维护。鉴于这一状况，负责将 Linux 移植到苹果 Arm 平台的 Asahi Linux 项目开发者 Hector Martin 在内核邮件列表上宣布退出内核开发，表示对内核开发过程以及社区管理方法失去信心，Asahi Linux 项目开发工作将主要集中在下游。
lkml.org From Hector Martin [PATCH] MAINTAINERS: Remove myself
LWN Resistance to Rust abstractions for DMA mapping

﻿

不管我们已经观察到多少只白天鹅，都不能确立“所有天鹅皆为白色”的理论。只要看见一只黑天鹅就可以驳倒它。——卡尔·波普尔

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