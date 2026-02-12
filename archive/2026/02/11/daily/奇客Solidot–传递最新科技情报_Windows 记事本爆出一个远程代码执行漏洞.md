---
title: Windows 记事本爆出一个远程代码执行漏洞
url: https://www.solidot.org/story?sid=83538
source: 奇客Solidot–传递最新科技情报
date: 2026-02-11
fetch_date: 2026-02-12T04:21:40.610020
---

# Windows 记事本爆出一个远程代码执行漏洞

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260211)
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

**本文已被查看 1499 次**

## Windows 记事本爆出一个远程代码执行漏洞

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2026年02月11日 20时29分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=83538&appkey=1370085986&title=Windows%20%E8%AE%B0%E4%BA%8B%E6%9C%AC%E7%88%86%E5%87%BA%E4%B8%80%E4%B8%AA%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自好兆头**

微软最近几年为其以精简著称的记事本应用引入了新功能，其中包括 AI 和 Markdown，新增功能也扩大了其攻击面，它刚刚爆出了一个远程代码执行漏洞 CVE-2026-20841，该漏洞与处理外链有关：当用户用记事本打开一个 Markdown 文件，攻击者可以引诱用户点击一个恶意链接，导致应用启动未经验证的协议去加载并执行远程文件。
https://www.cve.org/CVERecord?id=CVE-2026-20841
https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-20841

[回复](/comments?sid=83538&op=reply&type=story)

﻿

我讨厌星期一。--加菲猫

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260211)
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