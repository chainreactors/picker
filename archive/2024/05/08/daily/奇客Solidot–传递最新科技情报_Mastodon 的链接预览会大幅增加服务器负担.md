---
title: Mastodon 的链接预览会大幅增加服务器负担
url: https://www.solidot.org/story?sid=78090
source: 奇客Solidot–传递最新科技情报
date: 2024-05-08
fetch_date: 2025-10-06T17:16:44.287073
---

# Mastodon 的链接预览会大幅增加服务器负担

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

**本文已被查看 5064 次**

## Mastodon 的链接预览会大幅增加服务器负担

[![开源](https://icon.solidot.org/images/topics/topicopensource.png?123)](/search?tid=3 "开源")
[![Bug](https://icon.solidot.org/images/topics/topicbug.png?123)](/search?tid=53 "Bug")

[Wilson](/~Wilson) (42865)发表于 2024年05月07日 10时21分 星期二 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=78090&appkey=1370085986&title=Mastodon%20%E7%9A%84%E9%93%BE%E6%8E%A5%E9%A2%84%E8%A7%88%E4%BC%9A%E5%A4%A7%E5%B9%85%E5%A2%9E%E5%8A%A0%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%B4%9F%E6%8B%85 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自来自外星球的礼物**

和 X/Twitter 一样，去中心化微博服务 Mastodon 会对分享的链接生成预览。但与中心化的 X 不同的是，Mastodon 属于联邦宇宙平台，有数以百计的实例，生成的预览不限于一个实例，而是会有大量的实例几乎同时发出请求。这种联邦宇宙放大效应会大幅增加服务器负荷。对于大型网站而言，链接预览放大效应对其几乎不会构成影响。但小型网站就是另一回事了。Its FOSS 博客观察到，每次分享链接，网站会几乎停止响应或加载缓慢。安全工程师 Chris Partridge 在 2022 年报告，大约 3KB POST 导致其网站在不到 5 分钟内被请求了 114.7 MB 的数据，流量放大了 36704 倍。Mastodon 表示会在 4.4.0 版本中修复该问题，但 4.4.0 可能需要一年或更长时间才会发布。Mastodon 也许应该将其作为优先事项尽快修复。
https://tech.slashdot.org/story/24/05/05/0241211/is-mastodons-link-previewing-overloading-servers

﻿

活了一百年却只能记住30M字节是荒谬的。你知道，这比一张压缩盘还要少。人类境况正在变得日趋退。--Marvin Minsky

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