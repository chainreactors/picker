---
title: 微软称一个隐藏的 Windows Bug 触发了持续逾一天的宕机事故
url: https://www.solidot.org/story?sid=85903
source: 奇客Solidot–传递最新科技情报
date: 2026-11-16
fetch_date: 2026-11-17T09:56:22.277536
---

# 微软称一个隐藏的 Windows Bug 触发了持续逾一天的宕机事故

* 至顶科技：
* [至顶网](https://www.zhiding.cn/ "至顶网")
* [科技行者](https://www.techwalker.com/ "科技行者")
* [Solidot](https://www.solidot.org/ "Solidot")

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20261116)
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

**本文已被查看 3168 次**

## 微软称一个隐藏的 Windows Bug 触发了持续逾一天的宕机事故

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2026年11月16日 23时00分 星期一 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=85903&appkey=1370085986&title=%E5%BE%AE%E8%BD%AF%E7%A7%B0%E4%B8%80%E4%B8%AA%E9%9A%90%E8%97%8F%E7%9A%84%20Windows%20Bug%20%E8%A7%A6%E5%8F%91%E4%BA%86%E6%8C%81%E7%BB%AD%E9%80%BE%E4%B8%80%E5%A4%A9%E7%9A%84%E5%AE%95%E6%9C%BA%E4%BA%8B%E6%95%85 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自羊皮纸迷踪**

微软公布了初步事件报告，称一个隐藏的 Windows Bug 触发了持续逾一天的宕机事故。它将于 11 月 20 日公布更详细的信息。微软称，它于今年 7 月部署了针对 Microsoft 365 网络网关服务器的一项修正，运行三个多月未出现问题。但这次修正引入了一个锁争用的 bug：一个 Windows 内部进程中多个任务争夺对共享资源的访问权，特定流量条件下会耗尽处理器和内存资源。微软此前的测试未能发现这一问题，原因是测试是在硬件性能较弱的机器上进行的，在拥有更多核心的新硬件上，该问题会非常显著。两个条件触发了该 bug：Teams 流量从一个备用网关迁移到了与 Exchange Online 共用的主网关；一个不相关问题导致 14% 的网关服务器容量处于不可用状态。剩余服务器容量本来足够应付需求，但两个条件组合触发了 bug。当服务器发生故障自动系统会将连接转移到正常端点。然而这种额外的负载在其它地方引发了相同的故障，导致服务中断在不到两小时内蔓延至多个区域。最严重的时候逾八成服务器处于无响应状态。
https://www.theregister.com/saas/2026/11/16/microsoft-blames-monster-email-outage-on-software-defect-introduced-in-july-fix/5310026

[回复](/comments?sid=85903&op=reply&type=story)

﻿

天地不仁，以万物为刍狗；圣人不仁，以百姓为刍狗。 --老子

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20261116)
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