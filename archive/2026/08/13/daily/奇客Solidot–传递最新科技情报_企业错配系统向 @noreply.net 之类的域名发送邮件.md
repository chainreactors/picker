---
title: 企业错配系统向 @noreply.net 之类的域名发送邮件
url: https://www.solidot.org/story?sid=85079
source: 奇客Solidot–传递最新科技情报
date: 2026-08-13
fetch_date: 2026-08-14T03:59:44.399215
---

# 企业错配系统向 @noreply.net 之类的域名发送邮件

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260813)
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

**本文已被查看 2102 次**

## 企业错配系统向 @noreply.net 之类的域名发送邮件

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2026年08月13日 14时06分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=85079&appkey=1370085986&title=%E4%BC%81%E4%B8%9A%E9%94%99%E9%85%8D%E7%B3%BB%E7%BB%9F%E5%90%91%20%40noreply.net%20%E4%B9%8B%E7%B1%BB%E7%9A%84%E5%9F%9F%E5%90%8D%E5%8F%91%E9%80%81%E9%82%AE%E4%BB%B6 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自失眠**

安全研究员 Cory Solovewicz 分别在 2020 年和 2024 年购买了两个域名 noreply.us 和 noreply.net，他原本计划用于过滤该域名地址收到的邮件，结果发现有很多企业的邮件系统也会向该域名发送邮件，而且数量非常庞大。他无意中打造了一个蜜罐。他在本月举行的 Defcon 安全大会公布了结果：noreply.net 自 2024 年 12 月以来收到了 401,796 封邮件，平均每天 699.99 封；noreply.us 数量没有这么多，自 2020 年以来发送了 37255 封邮件。他指出，邮件是企业邮件系统自动发送的，并非人工撰写，这些都是内部系统配置错误导致的。另一名安全研究员 Mike Sheward 在购买了 deleteduser.com 域名之后也有类似的发现，企业没有真的彻底删除用户账号，而只是改了电邮地址。Sheward 透露，一家 AI 公司向该域名发送了大量邮件，该公司利用目标识别技术检测中东工业场所中可能违反安全规程的工人，他从这家公司收到了数千张 CCTV 监控录像截图。
https://arstechnica.com/security/2026/08/a-researcher-bought-noreply-net-companies-started-sending-him-secrets/

[回复](/comments?sid=85079&op=reply&type=story)

﻿

发现可能性的界限的唯一办法就是越过这个界限，到不可能中去。--阿瑟·克拉克

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260813)
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