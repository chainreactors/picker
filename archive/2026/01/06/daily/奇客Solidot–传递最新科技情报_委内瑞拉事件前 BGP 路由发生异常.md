---
title: 委内瑞拉事件前 BGP 路由发生异常
url: https://www.solidot.org/story?sid=83229
source: 奇客Solidot–传递最新科技情报
date: 2026-01-06
fetch_date: 2026-01-07T03:29:32.934248
---

# 委内瑞拉事件前 BGP 路由发生异常

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260106)
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

**本文已被查看 2350 次**

## 委内瑞拉事件前 BGP 路由发生异常

[![互联网](https://icon.solidot.org/images/topics/topicinternet.png?123)](/search?tid=17 "互联网")

[Edwards](/~Edwards) (42866)发表于 2026年01月06日 14时50分 星期二 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=83229&appkey=1370085986&title=%E5%A7%94%E5%86%85%E7%91%9E%E6%8B%89%E4%BA%8B%E4%BB%B6%E5%89%8D%20BGP%20%E8%B7%AF%E7%94%B1%E5%8F%91%E7%94%9F%E5%BC%82%E5%B8%B8 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自魔法生活**

根据 Cloudflare Radar 的监测，美国对委内瑞拉发动突然袭击前一天该国国有电信公司 CANTV 的自治系统 AS8048 发生了路由泄漏事件。当 BGP 流量从 A 点发送到 B 点，它可以被重路由经过 C 点。如果控制了 C 点，即使只有几个小时，理论上也可以收集到大量情报，这对政府机构非常有用。1 月 2 日 AS8048 的流量被路由经过了一条它原本不会经过的路线，该路线上的中转服务提供商 Sparkle 被公认不安全，也就是没有部署 BGP 安全功能如 RPKI 过滤。暂时还不清楚究竟发生了什么。
https://loworbitsecurity.com/radar/radar16/

[回复](/comments?sid=83229&op=reply&type=story)

﻿

实力永远意味着责任和危险。 -- 罗斯福. T.

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260106)
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