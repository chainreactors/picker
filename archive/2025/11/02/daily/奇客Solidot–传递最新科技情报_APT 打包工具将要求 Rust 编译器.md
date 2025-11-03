---
title: APT 打包工具将要求 Rust 编译器
url: https://www.solidot.org/story?sid=82698
source: 奇客Solidot–传递最新科技情报
date: 2025-11-02
fetch_date: 2025-11-03T03:15:20.965573
---

# APT 打包工具将要求 Rust 编译器

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20251102)
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

**本文已被查看 828 次**

## APT 打包工具将要求 Rust 编译器

[![Debian](https://icon.solidot.org/images/topics/topicdebian.png?123)](/search?tid=30 "Debian")

[Edwards](/~Edwards) (42866)发表于 2025年11月03日 00时17分 星期一 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=82698&appkey=1370085986&title=APT%20%E6%89%93%E5%8C%85%E5%B7%A5%E5%85%B7%E5%B0%86%E8%A6%81%E6%B1%82%20Rust%20%E7%BC%96%E8%AF%91%E5%99%A8 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自永恒先生**

Debian 开发者 Julian Andres Klode 在万圣节宣布，他计划最早从 2026 年 5 月起 APT 打包工具要求使用 Rust 编译器。理由是 APT 代码库的部分会受益于内存安全编程语言 Rust，有必要在 Debian 中强制要求使用 Rust，因此最早从明年 5 月起将在 APT 中引入 Rust 硬依赖和 Rust 代码。首批是 Rust 编译器和标准库，以及 Sequoia 生态系统。缺乏 Rust 支持的 m68k、Hewlett Packard Precision Architecture (HPPA)、SuperH/SH4 和 Alpha 的 Debian 版本面临被弃用。
https://lists.debian.org/deity/2025/10/msg00071.html
https://www.phoronix.com/news/Debian-APT-Will-Require-Rust

[回复](/comments?sid=82698&op=reply&type=story)

﻿

所有小说写的都是真事。怕吓着你们才叫小声说。 --王朔

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20251102)
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