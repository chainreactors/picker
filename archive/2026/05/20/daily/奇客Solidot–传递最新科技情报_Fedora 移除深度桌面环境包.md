---
title: Fedora 移除深度桌面环境包
url: https://www.solidot.org/story?sid=84353
source: 奇客Solidot–传递最新科技情报
date: 2026-05-20
fetch_date: 2026-05-21T06:03:12.914346
---

# Fedora 移除深度桌面环境包

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260520)
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

**本文已被查看 2441 次**

## Fedora 移除深度桌面环境包

[![Redhat](https://icon.solidot.org/images/topics/topicredhat.png?123)](/search?tid=99 "Redhat")
[![隐私](https://icon.solidot.org/images/topics/topic隐私.png?123)](/search?tid=133 "隐私")

[Wilson](/~Wilson) (42865)发表于 2026年05月20日 18时43分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=84353&appkey=1370085986&title=Fedora%20%E7%A7%BB%E9%99%A4%E6%B7%B1%E5%BA%A6%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83%E5%8C%85 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自基因先知者**

在 openSUSE 之后，Fedora 发行版移除了深度桌面环境包（Deepin Desktop）。2025 年初 SUSE 安全团队在一次例行审查中发现深度桌面环境有名叫 deepin-feature-enable 的软件包，该软件包是在 2021 年 4 月加入的，并没有咨询或通知 SUSE，它包含了一个“许可协议对话框（license agreement dialog）”，基本上说讲因为 openSUSE 的安全规定，它禁用了 deepin-api 和 deepin-daemon 需要的所有 dbus 和 polkit 功能，这可能导致 Deepin Desktop 不能正常工作，部分功能无效。如果用户不在意这些安全问题，可选择点击确认，之后会自动安装缺少的 dbus 和 polkit。安全团队的调查发现，deepin-daemon 中的核心组件从未递交进行安全审查，它们被悄悄的引入到了 openSUSE 中。鉴于 Deepin 社区过去几年多次违规，openSUSE 决定移除 Deepin Desktop。Fedora 项目随后也对深度桌面环境包展开安全审查，期间开发者发现难以联系部分深度软件包的维护者，因为安全担忧和软件包缺乏维护，它最终决定移除深度桌面环境。
https://pagure.io/fesco/issue/3409
https://www.phoronix.com/news/Fedora-Removing-Deepin

[回复](/comments?sid=84353&op=reply&type=story)

﻿

世间最庄严的问题是：我能做什么好事？

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260520)
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