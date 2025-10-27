---
title: Linus Torvalds 痛恨大小写不敏感的文件系统
url: https://www.solidot.org/story?sid=81171
source: 奇客Solidot–传递最新科技情报
date: 2025-04-29
fetch_date: 2025-10-06T22:07:26.296468
---

# Linus Torvalds 痛恨大小写不敏感的文件系统

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

**本文已被查看 28936 次**

## Linus Torvalds 痛恨大小写不敏感的文件系统

[![Linux](https://icon.solidot.org/images/topics/topiclinux.png?123)](/search?tid=7 "Linux")

[Wilson](/~Wilson) (42865)发表于 2025年04月28日 18时31分 星期一 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=81171&appkey=1370085986&title=Linus%20Torvalds%20%E7%97%9B%E6%81%A8%E5%A4%A7%E5%B0%8F%E5%86%99%E4%B8%8D%E6%95%8F%E6%84%9F%E7%9A%84%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自致命的发动机**

文件系统 Bcachefs 开发者 Kent Overstreet 关于大小写折叠问题的讨论引发了 Linux 作者对文件系统大小写不敏感的批评。Linus Torvalds 认为文件系统应该区分大小写，不区分是绝对错误的，一开始就不应该实现。他说文件系统的开发者永远不会吸取教训。区分大小写是个 bug，文件系统开发者可能太推崇旧的 FAT 文件系统，以至于试图以拙劣的方式重新创造它。
/.:Linus Torvalds Expresses His Hatred For Case-Insensitive File-Systems
lore.kernel.org/lkml/CAHk-=wjajMJyoTv2KZdpVRoPn0LFZ94Loci37WLVXmMxDbLOjg@mail.gmail.com/#t

﻿

发现可能性的界限的唯一办法就是越过这个界限，到不可能中去。--阿瑟·克拉克

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