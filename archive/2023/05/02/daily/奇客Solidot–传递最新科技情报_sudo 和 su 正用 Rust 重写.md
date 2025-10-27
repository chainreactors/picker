---
title: sudo 和 su 正用 Rust 重写
url: https://www.solidot.org/story?sid=74836
source: 奇客Solidot–传递最新科技情报
date: 2023-05-02
fetch_date: 2025-10-04T11:40:21.209075
---

# sudo 和 su 正用 Rust 重写

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

**本文已被查看 6664 次**

## sudo 和 su 正用 Rust 重写

[![开源](https://icon.solidot.org/images/topics/topicopensource.png?123)](/search?tid=3 "开源")

[Wilson](/~Wilson) (42865)发表于 2023年05月01日 21时55分 星期一 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=74836&appkey=1370085986&title=sudo%20%E5%92%8C%20su%20%E6%AD%A3%E7%94%A8%20Rust%20%E9%87%8D%E5%86%99 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自繁星若尘**

在亚马逊 AWS 的资助下，类 Unix 操作系统广泛使用的工具 sudo 和 su 正用 Rust 语言重写，以提高软件在内存方面的安全性，进一步增强 Linux 和开源生态系统的安全性。sudo 的开发始于 1980 年代，过去几十年里它已经成为一种必不可少的工具，但它是用 C 语言编写的，遭遇过许多与内存安全问题相关的漏洞。为了确保关键软件的安全性，防止内存安全漏洞，Ferrous Systems 和 Tweede Golf 正在联合将 sudo 从 C 移植到 Rust，他们的项目 sudo-rs 托管在 GitHub 上。
https://www.memorysafety.org/blog/sudo-and-su/

﻿

想想看吧，已经有一百万只猴子坐在一百万台打字机旁，可Usenet就是比不上莎士比。--Blair Houghton

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