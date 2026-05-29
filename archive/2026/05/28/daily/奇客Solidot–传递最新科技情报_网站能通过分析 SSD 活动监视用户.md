---
title: 网站能通过分析 SSD 活动监视用户
url: https://www.solidot.org/story?sid=84427
source: 奇客Solidot–传递最新科技情报
date: 2026-05-28
fetch_date: 2026-05-29T06:04:58.705426
---

# 网站能通过分析 SSD 活动监视用户

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260528)
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

**本文已被查看 1842 次**

## 网站能通过分析 SSD 活动监视用户

[![隐私](https://icon.solidot.org/images/topics/topic隐私.png?123)](/search?tid=133 "隐私")

[Edwards](/~Edwards) (42866)发表于 2026年05月28日 20时43分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=84427&appkey=1370085986&title=%E7%BD%91%E7%AB%99%E8%83%BD%E9%80%9A%E8%BF%87%E5%88%86%E6%9E%90%20SSD%20%E6%B4%BB%E5%8A%A8%E7%9B%91%E8%A7%86%E7%94%A8%E6%88%B7 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自第一日**

浏览器已经演变成类似操作系统的复杂平台，但不断加入的新特性也增加了浏览器的攻击面，引入新的漏洞。最新的攻击被称为 FROST(fingerprinting remotely using OPFS-based SSD timing)，通过测量用户使用的 SSD 的部分 I/O（输入/输出）操作时序，攻击者能识别用户在浏览器标签页打开的网站以及正在运行的应用程序。FROST 攻击无需任何交互，只需打开执行攻击的网站。FROST 攻击完全在浏览器中运行。它使用 JavaScript 与 OPFS（origin private file system）交互。OPFS 是 Web API 的一部分，是一个为特定网站预留的专属存储空间，用于运行完成特定任务所需的目标代码。网站无需任何交互就可以直接创建该空间。该攻击的一大缺陷是需要的 OPFS 文件比较大，可能需要 1GB 左右，因此会容易检测出来。
https://arstechnica.com/security/2026/05/websites-have-a-new-way-to-spy-on-visitors-analyzing-their-ssd-activity/

[回复](/comments?sid=84427&op=reply&type=story)

﻿

把理想运用到真实的事物上，便有了文明。

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260528)
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