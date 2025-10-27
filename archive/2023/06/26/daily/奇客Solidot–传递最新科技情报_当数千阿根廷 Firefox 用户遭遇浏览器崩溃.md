---
title: 当数千阿根廷 Firefox 用户遭遇浏览器崩溃
url: https://www.solidot.org/story?sid=75324
source: 奇客Solidot–传递最新科技情报
date: 2023-06-26
fetch_date: 2025-10-04T11:47:36.330688
---

# 当数千阿根廷 Firefox 用户遭遇浏览器崩溃

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

**本文已被查看 8521 次**

## 当数千阿根廷 Firefox 用户遭遇浏览器崩溃

[![Firefox](https://icon.solidot.org/images/topics/topicfirefox.png?123)](/search?tid=39 "Firefox")
[![Bug](https://icon.solidot.org/images/topics/topicbug.png?123)](/search?tid=53 "Bug")

[Wilson](/~Wilson) (42865)发表于 2023年06月25日 13时19分 星期日 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=75324&appkey=1370085986&title=%E5%BD%93%E6%95%B0%E5%8D%83%E9%98%BF%E6%A0%B9%E5%BB%B7%20Firefox%20%E7%94%A8%E6%88%B7%E9%81%AD%E9%81%87%E6%B5%8F%E8%A7%88%E5%99%A8%E5%B4%A9%E6%BA%83 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自大臣号遇难者**

本周一 Mozilla 开发者检测到大量 Linux 用户的浏览器崩溃事件。受影响的主要是阿根廷用户，他们运行的是一个基于 Debian 10 的发行版 Huayra v5，发生崩溃时用户都是在 Google 上搜索图像。所有 Firefox 版本都受到影响。这可能暗示了问题不在于 Firefox 而是 Google 这边。Mozilla 开发者在分析后发现，崩溃都是发生在堆栈探测（stack probing）期间。JIT 在接触保留下一个 JavaScript 调用变量的区域时发生了溢出。而 Google 的代码被发现在单一帧中分配了 2 万个变量。这可能是机器生成代码发生异常。所以在使用 ChatGPT 写代码时还是要三思而后行。但之所以发生崩溃是 Linux 内核的旧 bug 与 Google JavaScript 代码组合的结果。Linux kernel 4.20 修复了该 bug，而 Huayra v5 基于的 Debian 10 使用的是 4.19。
https://bugzilla.mozilla.org/show\_bug.cgi?id=1839139
https://fosstodon.org/@gabrielesvelto/110592904713090347

﻿

实力永远意味着责任和危险。 -- 罗斯福. T.

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