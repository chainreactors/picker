---
title: Linux 7.2 内核完全移除 strncpy 函数
url: https://www.solidot.org/story?sid=84644
source: 奇客Solidot–传递最新科技情报
date: 2026-06-22
fetch_date: 2026-06-23T06:06:58.572574
---

# Linux 7.2 内核完全移除 strncpy 函数

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260622)
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

**本文已被查看 2650 次**

## Linux 7.2 内核完全移除 strncpy 函数

[![Linux](https://icon.solidot.org/images/topics/topiclinux.png?123)](/search?tid=7 "Linux")

[Edwards](/~Edwards) (42866)发表于 2026年06月22日 18时55分 星期一 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=84644&appkey=1370085986&title=Linux%207.2%20%E5%86%85%E6%A0%B8%E5%AE%8C%E5%85%A8%E7%A7%BB%E9%99%A4%20strncpy%20%E5%87%BD%E6%95%B0%20 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自你在天堂里遇见的下一个人**

在 6 年 362 个补丁之后，Linux 7.2 内核终于完全移除了 strncpy() 函数。strncpy() 是一个 C 语言字符串复制函数，内核文档将其标记为“极度危险（actively dangerous）”。strncpy()是一类内存错误的主要来源：包含敏感数据的内核缓冲区可能会在未终止字符串边界外泄漏字节，导致内存信息泄露。strncpy()被 5 个不同函数取代：strscpy() 用于 NUL 结尾的目的地址，strscpy\_pad() 用于 NUL 结尾零填充的目标地址， strtomem\_pad() 用于非 NUL 结尾固定宽度字段，memcpy\_and\_pad() 用于显式填充的有边界复制，memcpy()用于已知长度的内存复制。
https://linux.slashdot.org/story/26/06/21/1810200/after-six-years-of-work-and-over-360-patches-linux-72-finally-removes-bug-prone-strncpy

[回复](/comments?sid=84644&op=reply&type=story)

﻿

计算机没什么用。他们只会告诉你答案。--毕加索

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260622)
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