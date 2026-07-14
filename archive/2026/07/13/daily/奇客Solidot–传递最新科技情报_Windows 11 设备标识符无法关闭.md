---
title: Windows 11 设备标识符无法关闭
url: https://www.solidot.org/story?sid=84810
source: 奇客Solidot–传递最新科技情报
date: 2026-07-13
fetch_date: 2026-07-14T04:47:28.630682
---

# Windows 11 设备标识符无法关闭

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260713)
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

**本文已被查看 2286 次**

## Windows 11 设备标识符无法关闭

[![隐私](https://icon.solidot.org/images/topics/topic隐私.png?123)](/search?tid=133 "隐私")

[Edwards](/~Edwards) (42866)发表于 2026年07月13日 13时38分 星期一 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=84810&appkey=1370085986&title=Windows%2011%20%E8%AE%BE%E5%A4%87%E6%A0%87%E8%AF%86%E7%AC%A6%E6%97%A0%E6%B3%95%E5%85%B3%E9%97%AD "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自神童的陷阱**

最近的一起案件显示微软能利用唯一设备标识符跟踪用户。该标识符被称为 Global Device Identifier（GDID），它关联用户使用的微软账号（Microsoft Account）。当用户使用微软账号登陆 Windows 时，微软会读取 Device PUID（Passport Unique ID，位于注册表 HKCU\SOFTWARE\Microsoft\IdentityCRL\ExtendedProperties 下），然后分配一个唯一永久 ID，该 ID 号储存在本地，多个后台服务会读取该 ID 号，并添加到操作系统向微软报告的所有活动中。重新安装 Windows 后，用户会分配到一个新的 ID 号，新旧 ID 号很容易与同一个账号关联起来。
https://www.windowslatest.com/2026/07/10/you-cant-fully-disable-microsofts-gdid-windows-11-tracker-but-these-settings-limit-what-it-captures/

[回复](/comments?sid=84810&op=reply&type=story)

﻿

自由的保证是什么?是对自己不再感到羞耻。--尼采

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260713)
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