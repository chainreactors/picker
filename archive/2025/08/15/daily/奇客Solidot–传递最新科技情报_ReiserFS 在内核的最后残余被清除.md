---
title: ReiserFS 在内核的最后残余被清除
url: https://www.solidot.org/story?sid=82053
source: 奇客Solidot–传递最新科技情报
date: 2025-08-15
fetch_date: 2025-10-07T00:48:14.005158
---

# ReiserFS 在内核的最后残余被清除

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

**本文已被查看 30559 次**

## ReiserFS 在内核的最后残余被清除

[![Linux](https://icon.solidot.org/images/topics/topiclinux.png?123)](/search?tid=7 "Linux")

[Edwards](/~Edwards) (42866)发表于 2025年08月15日 00时02分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=82053&appkey=1370085986&title=ReiserFS%20%E5%9C%A8%E5%86%85%E6%A0%B8%E7%9A%84%E6%9C%80%E5%90%8E%E6%AE%8B%E4%BD%99%E8%A2%AB%E6%B8%85%E9%99%A4 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自尘埃记**

去年发布的 Linux 6.13 正式移除了 ReiserFS 文件系统，但它的痕迹并没有完全清除掉。SUSE 开发者 David Sterba 在内核文档和部分工具中发现 ReiserFS 的残留后，发出补丁清除 ReiserFS 在内核的最后残余。ReiserFS 已经移除，因此内核文档中提到 ReiserFS 的部分也需要删除。唯一的例外是 ReiserFS R5 哈希函数，它仍然被部分内核代码使用。Reiser4 文件系统代码目前无人维护，Hans Reiser 在内核文件系统的时代彻底结束。
www.phoronix.com/news/ReiserFS-Documentation-Cleanse

[回复](/comments?sid=82053&op=reply&type=story)

﻿

所谓现实只不过是一个错觉，虽然这个错觉非常持久。--爱因斯坦

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