---
title: 内核开发者讨论移除安腾架构
url: https://www.solidot.org/story?sid=74156
source: 奇客Solidot–传递最新科技情报
date: 2023-02-17
fetch_date: 2025-10-04T06:52:46.214595
---

# 内核开发者讨论移除安腾架构

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20251003)
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

**本文已被查看 9615 次**

## 内核开发者讨论移除安腾架构

[![Linux](https://icon.solidot.org/images/topics/topiclinux.png?123)](/search?tid=7 "Linux")
[![Intel](https://icon.solidot.org/images/topics/topicintel.png?123)](/search?tid=80 "Intel")

[Wilson](/~Wilson) (42865)发表于 2023年02月16日 22时32分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=74156&appkey=1370085986&title=%E5%86%85%E6%A0%B8%E5%BC%80%E5%8F%91%E8%80%85%E8%AE%A8%E8%AE%BA%E7%A7%BB%E9%99%A4%E5%AE%89%E8%85%BE%E6%9E%B6%E6%9E%84 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自千与千寻**

因基本上没人用且没人维护，内核开发者讨论是否移除英特尔的安腾/IA64 架构，讨论结果还是让它活着。问题最早是 Arm 开发者 Ard Biesheuvel 提出的，他指出内核的 IA64 版本无人维护，而根据一位可能是仅剩的用户报告它已经出问题一个月了，但没人关心，因此提议干脆移除它。Linux 作者 Linus Torvalds 说他不是 IA64 架构粉丝，但完全移除一个架构还是令人难过，而且它的维护负担看起来并不大。他同时表示，如果没人愿意花时间去处理故障，那么结束对 IA64 的支持只能是唯一选项。物理学家兼 Debian 维护者 John Paul Adrian Glaubitz 站出来拯救了 IA64，表示他有时间维护该架构，而且他还有一台安腾服务器可以测试。英特尔是在 2021 年退役了安腾处理器产品。
https://www.theregister.com/2023/02/16/itanium\_linux\_kernel/

﻿

以眼还眼，世界只会更盲目。--甘地

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20251003)
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