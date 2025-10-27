---
title: 朝鲜黑客利用最近修复的 Windows 0day 安装 rootkit
url: https://www.solidot.org/story?sid=79020
source: 奇客Solidot–传递最新科技情报
date: 2024-08-21
fetch_date: 2025-10-06T18:03:57.299280
---

# 朝鲜黑客利用最近修复的 Windows 0day 安装 rootkit

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

**本文已被查看 5537 次**

## 朝鲜黑客利用最近修复的 Windows 0day 安装 rootkit

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2024年08月20日 13时56分 星期二 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=79020&appkey=1370085986&title=%E6%9C%9D%E9%B2%9C%E9%BB%91%E5%AE%A2%E5%88%A9%E7%94%A8%E6%9C%80%E8%BF%91%E4%BF%AE%E5%A4%8D%E7%9A%84%20Windows%200day%20%E5%AE%89%E8%A3%85%20rootkit "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自梦蛇**

微软在上周的例行安全更新中修复了一个 0day 漏洞 CVE-2024-38193，它位于 AFD.sys 中，属于释放后使用漏洞。微软警告攻击者利用该漏洞能获得系统权限，运行不受信任的代码。软件巨人当时没有披露谁在利用该漏洞。本周一，向微软报告该漏洞的组织 Gen 的研究人员披露，朝鲜黑客组织 Lazarus 在利用该漏洞安装 rootkit。研究人员称，攻击者针对的是从事加密货币工程或在航空航天领域工作的目标，旨在入侵其雇主的网络，以及窃取加密货币。Lazarus 利用该漏洞安装了 FudModule——它属于被称为 rootkit 的恶意程序。微软知道该漏洞之后花了半年时间才修复。黑客利用该漏洞的时间显然远长于半年。
https://arstechnica.com/security/2024/08/windows-0-day-was-exploited-by-north-korea-to-install-advanced-rootkit/
https://www.gendigital.com/blog/news/innovation/protecting-windows-users

﻿

在b进位制中，以数n起头的数出现的机率为logb(n + 1) − logb(n)--本福特定律

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