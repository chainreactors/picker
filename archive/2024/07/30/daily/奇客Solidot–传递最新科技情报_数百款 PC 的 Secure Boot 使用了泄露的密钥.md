---
title: 数百款 PC 的 Secure Boot 使用了泄露的密钥
url: https://www.solidot.org/story?sid=78823
source: 奇客Solidot–传递最新科技情报
date: 2024-07-30
fetch_date: 2025-10-06T17:45:01.656355
---

# 数百款 PC 的 Secure Boot 使用了泄露的密钥

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

**本文已被查看 5242 次**

## 数百款 PC 的 Secure Boot 使用了泄露的密钥

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2024年07月29日 16时05分 星期一 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=78823&appkey=1370085986&title=%E6%95%B0%E7%99%BE%E6%AC%BE%20PC%20%E7%9A%84%20Secure%20Boot%20%E4%BD%BF%E7%94%A8%E4%BA%86%E6%B3%84%E9%9C%B2%E7%9A%84%E5%AF%86%E9%92%A5 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自失落之心**

2007 年，中国研究员 icelord 在 CSDN 发表了一篇博文，介绍了 BIOS Rootkit 的一种简单实现。2011 年，被称为 Mebromi 的 BIOS Rootkit 实现走到了现实生活里。2012 年行业联盟宣布采用 Secure Boot 去抵御 BIOS 恶意程序。Secure Boot 基于 BIOS 继任者 UEFI，它使用公钥加密阻止加载任何未使用预批准数字签名签名的代码。固件安全供应商 Binarily 上周发布的报告显示，戴尔、宏碁、富士通、技嘉、惠普、英特尔、联想和超微销售的数百款 PC 使用了 2022 年泄露的测试平台密钥(PK)保护其 UEFI Secure Boot 实现。加密密钥的泄露意味着 Secure Boot 所提供的安全保护被破坏了。泄露密钥由 AMI 创建，主要提供给客户测试用，但测试密钥却不知何故进入了产品中，而且在这些公司的 PC 产品中共享。Binarly 创始人兼 CEO Alex Matrosov 指出，想象一下，一栋公寓楼所有住客都有相同的前门锁和钥匙。如果有人丢失钥匙，整栋楼都会出问题。更糟的情况是，其它建筑物也使用了相同的锁和钥匙。总共有 215 款 PC 受到影响，你可以检查下自己使用的 PC 型号是否名单中。
https://www.binarly.io/blog/pkfail-untrusted-platform-keys-undermine-secure-boot-on-uefi-ecosystem
https://arstechnica.com/security/2024/07/secure-boot-is-completely-compromised-on-200-models-from-5-big-device-makers/
https://blog.csdn.net/icelord/article/details/1604884

﻿

天地不仁，以万物为刍狗；圣人不仁，以百姓为刍狗。 --老子

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