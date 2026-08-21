---
title: AliExpress 被发现静默运行 WebAudio 指纹
url: https://www.solidot.org/story?sid=85150
source: 奇客Solidot–传递最新科技情报
date: 2026-08-20
fetch_date: 2026-08-21T03:04:02.918643
---

# AliExpress 被发现静默运行 WebAudio 指纹

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260820)
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

**本文已被查看 1895 次**

## AliExpress 被发现静默运行 WebAudio 指纹

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2026年08月20日 23时26分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=85150&appkey=1370085986&title=AliExpress%20%E8%A2%AB%E5%8F%91%E7%8E%B0%E9%9D%99%E9%BB%98%E8%BF%90%E8%A1%8C%20WebAudio%20%E6%8C%87%E7%BA%B9 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自地球的呼唤**

有开发者注意到一个奇怪的现象：蓝牙耳机支持多点蓝牙音频，能同时连接 PC 和手机，PC 通常优先播放音频，只有在 PC 没有播放内容时手机才会播放音频。这位开发者注意到，在 Firefox 或 Chrome 浏览器中打开 AliExpress 网页后，手机会停止播放音频，关闭网页则会恢复。这位开发者随后展开了调查，发现高度混淆的阿里巴巴安全脚本会创建两个 WebAudio 图形，成为浏览器指纹的一部分，该静默运行的 WebAudio 指纹会干扰多点蓝牙音频。用户可利用 uBlock Origin 扩展屏蔽阿里巴巴的脚本 collina.js 和 fireyejs.js 关闭这一指纹。
https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html

[回复](/comments?sid=85150&op=reply&type=story)

﻿

我并不同意你的观点，但是我誓死捍卫你说话的权利——伏尔泰

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260820)
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