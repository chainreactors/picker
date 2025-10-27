---
title: 因违反打包政策 openSUSE 移除 Deepin Desktop
url: https://www.solidot.org/story?sid=81232
source: 奇客Solidot–传递最新科技情报
date: 2025-05-08
fetch_date: 2025-10-06T22:28:32.415921
---

# 因违反打包政策 openSUSE 移除 Deepin Desktop

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

**本文已被查看 27276 次**

## 因违反打包政策 openSUSE 移除 Deepin Desktop

[![SuSE](https://icon.solidot.org/images/topics/topicsuse.png?123)](/search?tid=103 "SuSE")

[Wilson](/~Wilson) (42865)发表于 2025年05月07日 23时27分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=81232&appkey=1370085986&title=%E5%9B%A0%E8%BF%9D%E5%8F%8D%E6%89%93%E5%8C%85%E6%94%BF%E7%AD%96%20openSUSE%20%E7%A7%BB%E9%99%A4%20Deepin%20Desktop "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自开普罗纳的魔法师**

SUSE 安全团队在年初的一次例行审查中发现深度桌面环境（Deepin Desktop）有一个叫 deepin-feature-enable 的软件包，该软件包是在 2021 年 4 月加入的，并没有咨询或通知 SUSE，它包含了一个“许可协议对话框（license agreement dialog）”，基本上说讲因为 openSUSE 的安全规定，它禁用了 deepin-api 和 deepin-daemon 需要的所有 dbus 和 polkit 功能，这可能导致 Deepin Desktop 不能正常工作，部分功能无效。如果用户不在意这些安全问题，可选择点击确认，之后会自动安装缺少的 dbus 和 polkit。安全团队的调查发现，deepin-daemon 中的核心组件从未递交进行安全审查，它们被悄悄的引入到了 openSUSE 中。鉴于 Deepin 社区过去几年多次违规，openSUSE 决定移除 Deepin Desktop。
security.opensuse.org/2025/05/07/deepin-desktop-removal.html

﻿

工作撵跑三个魔鬼：无聊、堕落和贫穷。

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