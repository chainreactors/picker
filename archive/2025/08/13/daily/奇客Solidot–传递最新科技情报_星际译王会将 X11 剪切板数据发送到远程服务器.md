---
title: 星际译王会将 X11 剪切板数据发送到远程服务器
url: https://www.solidot.org/story?sid=82025
source: 奇客Solidot–传递最新科技情报
date: 2025-08-13
fetch_date: 2025-10-07T00:47:47.149446
---

# 星际译王会将 X11 剪切板数据发送到远程服务器

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20251006)
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

**本文已被查看 3211 次**

## 星际译王会将 X11 剪切板数据发送到远程服务器

[![隐私](https://icon.solidot.org/images/topics/topic隐私.png?123)](/search?tid=133 "隐私")

[Edwards](/~Edwards) (42866)发表于 2025年08月12日 21时53分 星期二 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=82025&appkey=1370085986&title=%E6%98%9F%E9%99%85%E8%AF%91%E7%8E%8B%E4%BC%9A%E5%B0%86%20X11%20%E5%89%AA%E5%88%87%E6%9D%BF%E6%95%B0%E6%8D%AE%E5%8F%91%E9%80%81%E5%88%B0%E8%BF%9C%E7%A8%8B%E6%9C%8D%E5%8A%A1%E5%99%A8 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自向世界倾诉爱**

LWN 发表的一篇文章谈论了星际译王词典软件的潜在隐私问题。用户在 Debian 上安装星际译王时会默认安装插件包 stardict-plugin，其中之一是网易的有道在线词典插件，该插件还会链接另一个在线词典 dict.cn。在 X11 下星际译王默认会启用扫描功能，监视用户的文本选择通过弹出窗口提供自动翻译。在 Wayland 下该功能被破坏了，因为 Wayland 默认禁止应用程序捕获其它应用的文本。星际译王的 Debian 包维护者 Xiao Sheng Wen 认为这种做法没有问题，指出如果用户不想使用扫描功能或有道插件，可以禁用它们。但 Vincent Lefevre 认为，涉及隐私的功能永远不应该默认启用。用户可能会在文本选择时泄漏敏感信息，比如从密码管理器中复制粘贴密码。
lwn.net/SubscriberLink/1032732/3334850da49689e1/

[回复](/comments?sid=82025&op=reply&type=story)

﻿

任何人均有其价值

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20251006)
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