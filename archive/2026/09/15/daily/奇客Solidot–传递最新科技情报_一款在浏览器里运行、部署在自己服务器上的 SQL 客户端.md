---
title: 一款在浏览器里运行、部署在自己服务器上的 SQL 客户端
url: https://www.solidot.org/story?sid=85383
source: 奇客Solidot–传递最新科技情报
date: 2026-09-15
fetch_date: 2026-09-16T07:05:09.526034
---

# 一款在浏览器里运行、部署在自己服务器上的 SQL 客户端

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260915)
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

**本文已被查看 2746 次**

## 一款在浏览器里运行、部署在自己服务器上的 SQL 客户端

[![开源](https://icon.solidot.org/images/topics/topicopensource.png?123)](/search?tid=3 "开源")
[![数据库](https://icon.solidot.org/images/topics/topicdatabases.png?123)](/search?tid=63 "数据库")

[Edwards](/~Edwards) (42866)发表于 2026年09月15日 16时43分 星期二 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=85383&appkey=1370085986&title=%E4%B8%80%E6%AC%BE%E5%9C%A8%E6%B5%8F%E8%A7%88%E5%99%A8%E9%87%8C%E8%BF%90%E8%A1%8C%E3%80%81%E9%83%A8%E7%BD%B2%E5%9C%A8%E8%87%AA%E5%B7%B1%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8A%E7%9A%84%20SQL%20%E5%AE%A2%E6%88%B7%E7%AB%AF "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自外交豁免权**

Yusuf Gundogdu 写道：LibreDB Studio 是一个 MIT 协议的 SQL 客户端，不装在本地而是跑在服务器上，浏览器打开就能用，一条 docker run 就起来。16 个驱动覆盖 42 种数据库，PostgreSQL、MySQL、MongoDB、Redis、ClickHouse 这些都在内。9 月 8 日发布了 0.15.0 版本。我觉得值得一提的是他们把 AI 那部分做了实测：28 个模型跑同一套六项数据库任务，27 个通过 Ollama 完全在本地运行，最快的 qwen2.5:7b 只有 4.7 GB，一次完整运行中位数 6 秒，最小的 2.5 GB。数据逐个模型公开，包括没通过的和卡在哪一步。另外只读不是靠解析 SQL 挡的，是数据库自己挡的：PostgreSQL 上开只读事务，SQLite 上每条语句前重设 query\_only。
https://github.com/libredb/libredb-studio/blob/main/README\_zh.md
https://www.youtube.com/watch?v=QI\_6jxu2J7s

[回复](/comments?sid=85383&op=reply&type=story)

﻿

肚子大不可怕，可怕的是肚子里没有好东西。--加菲猫

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260915)
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