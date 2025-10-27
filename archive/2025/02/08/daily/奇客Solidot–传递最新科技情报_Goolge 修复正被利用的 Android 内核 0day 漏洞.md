---
title: Goolge 修复正被利用的 Android 内核 0day 漏洞
url: https://www.solidot.org/story?sid=80496
source: 奇客Solidot–传递最新科技情报
date: 2025-02-08
fetch_date: 2025-10-06T20:37:46.735687
---

# Goolge 修复正被利用的 Android 内核 0day 漏洞

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

**本文已被查看 8403 次**

## Goolge 修复正被利用的 Android 内核 0day 漏洞

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")
[![Android ](https://icon.solidot.org/images/topics/topicAndroid.png?123)](/search?tid=171 "Android ")

[Wilson](/~Wilson) (42865)发表于 2025年02月07日 21时26分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=80496&appkey=1370085986&title=Goolge%20%E4%BF%AE%E5%A4%8D%E6%AD%A3%E8%A2%AB%E5%88%A9%E7%94%A8%E7%9A%84%20Android%20%E5%86%85%E6%A0%B8%200day%20%E6%BC%8F%E6%B4%9E "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自惨败**

Goolge 本月初释出了两组安全补丁 2025-02-01 和 2025-02-05，修复了 48 个漏洞，其中包括一个 Android 内核 0day 高危漏洞。该漏洞编号 CVE-2024-53104，影响 Linux 内核的 USB Video Class(UVC)驱动，属于越界写入 bug，存在于 uvc\_driver.c 的 uvc\_parse\_format()函数中。该漏洞会导致内存损坏、程序崩溃甚至任意代码执行。攻击者可利用该 bug 提权，可用于安装恶意程序、更改或删除数据，或创建拥有完整管理权限的新帐户。该漏洞已被用于针对性的有限攻击。Android 用户最好立即更新到最新的安全补丁。
The DefendOps Diaries：Google Fixes Android Kernel Zero-Day Exploited in Attacks

﻿

渴求美德而非奖赏。

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