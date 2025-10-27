---
title: Snap 前开发者开发脚本用 Flatpaks 取代 Snap
url: https://www.solidot.org/story?sid=75398
source: 奇客Solidot–传递最新科技情报
date: 2023-07-03
fetch_date: 2025-10-04T11:53:08.480894
---

# Snap 前开发者开发脚本用 Flatpaks 取代 Snap

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

**本文已被查看 7900 次**

## Snap 前开发者开发脚本用 Flatpaks 取代 Snap

[![Ubuntu](https://icon.solidot.org/images/topics/topicubuntu.png?123)](/search?tid=111 "Ubuntu")

[Wilson](/~Wilson) (42865)发表于 2023年07月02日 23时14分 星期日 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=75398&appkey=1370085986&title=Snap%20%E5%89%8D%E5%BC%80%E5%8F%91%E8%80%85%E5%BC%80%E5%8F%91%E8%84%9A%E6%9C%AC%E7%94%A8%20Flatpaks%20%E5%8F%96%E4%BB%A3%20Snap "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自神秘博士：噬悲者**

Alan Pope 在 2021 年离开了工作了 10 年的 Canonical 公司，是 Canonical 主导的包格式 Snap 的共同开发者。该公司今年早些时候发布的 Ubuntu 23.04 默认移除了对竞争对手 Flatpak 格式的支持。Flatpak 和 Snap 都类似 docker，旨在提供一种独立于发行版的打包格式，解决包依赖问题，能在不导致依赖地狱的情况下在同一个系统上安装同一个程序的多个版本。Flatpak 由 Red Hat 主导开发，完全开源，能存在多个 Flatpak 软件库。相比下，Snap 的后端是 Canonical 私有的，只存在一个 Canonical 控制的 Snap 应用商店。Alan Pope 开发了一个脚本 unsnap，如果一个 Snap 软件包存在对应的 Flatpak 包，那么它将会自动用 Flatpak 包替换 Snap 包。该脚本托管在 GitHub 上。
https://github.com/popey/unsnap

https://linux.slashdot.org/story/23/07/01/0046224/former-canonical-developer-is-working-on-a-script-that-replaces-snaps-with-flatpaks

﻿

人们还往往把真理和错误混在一起去教人，而坚持的却是错误。--歌德

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