---
title: BGP 系统的 Bug 处理方式导致部分网络故障
url: https://www.solidot.org/story?sid=81406
source: 奇客Solidot–传递最新科技情报
date: 2025-05-28
fetch_date: 2025-10-06T22:28:33.184514
---

# BGP 系统的 Bug 处理方式导致部分网络故障

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

**本文已被查看 4670 次**

## BGP 系统的 Bug 处理方式导致部分网络故障

[![互联网](https://icon.solidot.org/images/topics/topicinternet.png?123)](/search?tid=17 "互联网")
[![Bug](https://icon.solidot.org/images/topics/topicbug.png?123)](/search?tid=53 "Bug")

[Wilson](/~Wilson) (42865)发表于 2025年05月27日 22时40分 星期二 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=81406&appkey=1370085986&title=BGP%20%E7%B3%BB%E7%BB%9F%E7%9A%84%20Bug%20%E5%A4%84%E7%90%86%E6%96%B9%E5%BC%8F%E5%AF%BC%E8%87%B4%E9%83%A8%E5%88%86%E7%BD%91%E7%BB%9C%E6%95%85%E9%9A%9C "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自失忆的星球**

2025 年 5 月 20 日 7AM (UTC) ，可能是和记黄埔(AS9304)或 Starcloud(AS135338)广播了一则有问题的 BGP 消息，该消息包含了损坏的 BGP Prefix-SID Attribute。BGP Prefix-SID Attribute 主要用于内部 BGP 会话，在单一网络内部路由流量，它泄漏到全局路由表可能是因为将外部 BGP 会话错误配置为内部会话。对于错误的 BGP 消息，配置了 RFC7606 (“BGP 容错”)的系统会将其过滤或丢弃掉。然而 JunOS 系统没有丢弃错误消息，而是转发给了对等网络，直到该消息被没有配置 BGP 容错的 Arista EOS 系统接收到，最终导致部分网络发生故障，可能导致客户网络连接短暂中断。运行 JunOS 系统的 Juniper 硬件被互联网中转运营商广泛使用，受到此次事故影响的网络包括了 SpaceX Starlink AS14593、字节跳动 AS396986、Disney Worldwide Services AS23344 等。
blog.benjojo.co.uk/post/bgp-attr-40-junos-arista-session-reset-incident

﻿

柔和回答， 使怒消退。 言语暴戾， 触动怒气——箴言篇 15:1

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