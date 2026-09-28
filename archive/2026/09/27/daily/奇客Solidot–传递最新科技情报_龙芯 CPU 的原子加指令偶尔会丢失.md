---
title: 龙芯 CPU 的原子加指令偶尔会丢失
url: https://www.solidot.org/story?sid=85484
source: 奇客Solidot–传递最新科技情报
date: 2026-09-27
fetch_date: 2026-09-28T07:56:37.781844
---

# 龙芯 CPU 的原子加指令偶尔会丢失

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260927)
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

**本文已被查看 2941 次**

## 龙芯 CPU 的原子加指令偶尔会丢失

[![Bug](https://icon.solidot.org/images/topics/topicbug.png?123)](/search?tid=53 "Bug")

[Edwards](/~Edwards) (42866)发表于 2026年09月27日 17时57分 星期日 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=85484&appkey=1370085986&title=%E9%BE%99%E8%8A%AF%20CPU%20%E7%9A%84%E5%8E%9F%E5%AD%90%E5%8A%A0%E6%8C%87%E4%BB%A4%E5%81%B6%E5%B0%94%E4%BC%9A%E4%B8%A2%E5%A4%B1 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自泰坦棋手**

今年 2 月 Debian 13 的龙芯架构移植版 loong13 的维护者在编译打包过程中发现，normaliz 的自带测试会死循环导致打包超时。第一次排查发现原子加指令会在特定情况下丢失更新，但原因未知。今年 8 月，开发者在 AI 的帮助下重新寻找 normaliz 中原子加丢失的问题。他们让 AI 去找最小复现，在这个过程中负责指挥 AI 调查的方向。大概两天后找到了一个稳定的复现程序，才发现事情的根源是：CPU 的原子加法指令，偶尔会不原子。开发者向龙芯报告了问题，两周后龙芯给出了修复的测试固件，确认问题解决。龙芯表示会在国庆节（10 月 1 日）之前发布固件。该问题主要影响使用 LA664 核心的 3C6000/S 和 3A6000。
https://jia.je/hardware/2026/09/24/loongson-cpu-erratum/#%E7%AC%AC%E4%B8%80%E8%BD%AE%E6%8E%92%E6%9F%A5

[回复](/comments?sid=85484&op=reply&type=story)

﻿

你不问我，我就不会说谎话。

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260927)
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