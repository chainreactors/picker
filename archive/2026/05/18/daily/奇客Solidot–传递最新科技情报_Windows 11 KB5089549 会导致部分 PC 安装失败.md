---
title: Windows 11 KB5089549 会导致部分 PC 安装失败
url: https://www.solidot.org/story?sid=84324
source: 奇客Solidot–传递最新科技情报
date: 2026-05-18
fetch_date: 2026-05-19T06:04:00.458111
---

# Windows 11 KB5089549 会导致部分 PC 安装失败

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260518)
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

**本文已被查看 2010 次**

## Windows 11 KB5089549 会导致部分 PC 安装失败

[![Bug](https://icon.solidot.org/images/topics/topicbug.png?123)](/search?tid=53 "Bug")

[Edwards](/~Edwards) (42866)发表于 2026年05月18日 16时34分 星期一 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=84324&appkey=1370085986&title=Windows%2011%20KB5089549%20%E4%BC%9A%E5%AF%BC%E8%87%B4%E9%83%A8%E5%88%86%20PC%20%E5%AE%89%E8%A3%85%E5%A4%B1%E8%B4%A5 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自空中城堡**

微软证实本月释出的例行安全更新 Windows 11 KB5089549 会导致部分 PC 安装失败，原因是对系统启动至关重要的 EFI 系统分区（ESP）空间不足。如果 ESP 可用空间不足 10 MB，KB5089549 安装会失败，返回 0x800f0922 错误，用户会看到安装卡在了 35-36%，然后回滚，提示空间不足。微软提供了一个临时的修复方法：以管理员身份打开命令提示符。运行以下命令：reg add “HKLM\SYSTEM\CurrentControlSet\Control\Bfsvc /v EspPaddingPercent /t REG\_DWORD /d 0 /f”。然后重启受影响的设备。
https://www.neowin.net/news/microsoft-confirms-windows-11-kb5089549-fails-install-shares-workarounds/

[回复](/comments?sid=84324&op=reply&type=story)

﻿

世间最庄严的问题是：我能做什么好事？

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260518)
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