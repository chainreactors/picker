---
title: 回顾对 AUR 的攻击
url: https://www.solidot.org/story?sid=84647
source: 奇客Solidot–传递最新科技情报
date: 2026-06-22
fetch_date: 2026-06-23T06:06:54.172532
---

# 回顾对 AUR 的攻击

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

**本文已被查看 2371 次**

## 回顾对 AUR 的攻击

[![Linux](https://icon.solidot.org/images/topics/topiclinux.png?123)](/search?tid=7 "Linux")
[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2026年06月22日 22时47分 星期一 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=84647&appkey=1370085986&title=%E5%9B%9E%E9%A1%BE%E5%AF%B9%20AUR%20%E7%9A%84%E6%94%BB%E5%87%BB "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自红女王**

由用户递交的软件仓库 Arch User Repository(AUR)最近遭遇了大规模恶意攻击，攻击者创建了一系列新账号，然后通过这些账号接管无人维护的软件包（被称为 orphaned packages），植入恶意代码，推送恶意更新。Arch 项目的维护者现已关闭了新用户注册，正在讨论如何处理这些被恶意滥用的无人维护软件包。AUR 中的软件包由用户递交，其他用户可通过搜索下载 PKGBUILD 文件、解依、编译、安装和更新软件。它不提供软件的二进制版本。目前 AUR 中有逾 107,000 个软件包，其中近 14,000 个无人维护可供认领。任何注册用户都可以认领和修改无人维护的软件包。它提供的软件包未经审核，风险由用户自己承担。其它 Linux 发行版也都有类似的软件仓库，如 Fedora 的 Copr，openSUSE 的 Open Build Service (OBS)，Ubuntu 的 Personal Package Archives (PPA)。但这些服务与 AUR 有显著区别：它们提供了类似官方软件包的构建环境，而且不允许预编译二进制文件或私有软件。AUR 的规定过于宽松而在这次攻击中遭到了滥用。
https://lwn.net/SubscriberLink/1077619/f7b07c5489fdd43a/
https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/thread/4JRS73YVTE7JUYHHE3ZDUIHXYHXZ3YQQ/
https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/thread/YWSB5N3NQMDHQZDJN2FHX6J2HEA4BYYN/

[回复](/comments?sid=84647&op=reply&type=story)

﻿

我们所需要的，不是天才，不是玩世不恭者，不是愤世嫉俗者，不是机敏的策略家，而是真挚的，坦诚的人。要使我们能够找到重返纯朴与真诚的道路，我们的精神包容量足够地充分，我们自身的正直足够地问心无愧了吗？--朋霍费尔

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