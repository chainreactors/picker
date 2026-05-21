---
title: Google 云服务 GCP 不小心将其大客户 Railway 的账号封禁
url: https://www.solidot.org/story?sid=84355
source: 奇客Solidot–传递最新科技情报
date: 2026-05-20
fetch_date: 2026-05-21T06:03:07.681462
---

# Google 云服务 GCP 不小心将其大客户 Railway 的账号封禁

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260520)
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

**本文已被查看 2018 次**

## Google 云服务 GCP 不小心将其大客户 Railway 的账号封禁

[![Google](https://icon.solidot.org/images/topics/topicgoogle.png?123)](/search?tid=26 "Google")
[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2026年05月20日 21时51分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=84355&appkey=1370085986&title=Google%20%E4%BA%91%E6%9C%8D%E5%8A%A1%20GCP%20%E4%B8%8D%E5%B0%8F%E5%BF%83%E5%B0%86%E5%85%B6%E5%A4%A7%E5%AE%A2%E6%88%B7%20Railway%20%E7%9A%84%E8%B4%A6%E5%8F%B7%E5%B0%81%E7%A6%81 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自凡尔纳地球三部曲**

2024 年 Google 云服务 GCP 的错误配置导致澳大利亚退休基金管理公司 UniSuper 的数据被完全删除，幸运的是 UniSuper 在另一家公司有备份。这起事故导致 UniSuper 下线了一周多时间。2026 年 5 月 19 日 GCP 发生了一起类似的严重事故，它的自动系统将其大客户、PaaS 平台 Railway.com 的生产账号给封了，导致 Railway 的服务下线，根据 Railway 官方博客的事故报告，宕机持续了大约 8 个小时。账号封禁发生在 19 日 22:10 UTC，导致 Railway 失去了 GCP 相关的基础设施，这些基础设施支持了控制面板、API 以及部分网络基础设施。Railway 立即联系了 GCP 的客户经理，22:29 UTC 账号恢复，但计算实例、磁盘以及网络都需要逐个慢慢恢复，直到第二天 07:58 UTC 事故才完全解决。Railway 宣布将降低对 GCP 的依赖，计划将 GCP 从热路径中移除，保留作为备份/故障转移服务。
https://blog.railway.com/p/incident-report-may-19-2026-gcp-account-outage

[回复](/comments?sid=84355&op=reply&type=story)

﻿

也许我是错而你是对，但只有我们一起努力，才能更接近真理。——卡尔·波普尔

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260520)
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