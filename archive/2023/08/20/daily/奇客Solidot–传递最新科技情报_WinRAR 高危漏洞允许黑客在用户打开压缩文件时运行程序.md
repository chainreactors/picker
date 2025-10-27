---
title: WinRAR 高危漏洞允许黑客在用户打开压缩文件时运行程序
url: https://www.solidot.org/story?sid=75841
source: 奇客Solidot–传递最新科技情报
date: 2023-08-20
fetch_date: 2025-10-04T11:59:53.791290
---

# WinRAR 高危漏洞允许黑客在用户打开压缩文件时运行程序

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

**本文已被查看 7729 次**

## WinRAR 高危漏洞允许黑客在用户打开压缩文件时运行程序

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2023年08月19日 19时24分 星期六 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=75841&appkey=1370085986&title=WinRAR%20%E9%AB%98%E5%8D%B1%E6%BC%8F%E6%B4%9E%E5%85%81%E8%AE%B8%E9%BB%91%E5%AE%A2%E5%9C%A8%E7%94%A8%E6%88%B7%E6%89%93%E5%BC%80%E5%8E%8B%E7%BC%A9%E6%96%87%E4%BB%B6%E6%97%B6%E8%BF%90%E8%A1%8C%E7%A8%8B%E5%BA%8F "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自喀迈拉空间**

WinRAR 修复了一个高危漏洞 CVE-2023-40477，该漏洞允许远程攻击者通过引诱受害者打开一个特制的 RAR 压缩文件去执行任意代码。该漏洞需要欺骗用户因此危险等级评分略低为 7.8/10。该漏洞是 Zero Day Initiative 的 研究员 goodbyeselene 发现的，2023 年 6 月 8 日报告给开发商 RARLAB，漏洞存在于恢复卷处理过程中，是未能正确验证用户提供的数据导致的。RARLAB 在 8 月 2 日释出 WinRAR v6.23 修复了该漏洞。WinRAR 用户需要尽可能快的升级。WinRAR v6.23 还修复了另一个会导致错误文件初始化的漏洞。
https://www.zerodayinitiative.com/advisories/ZDI-23-1152/
https://www.win-rar.com/singlenewsview.html?&L=0&tx\_ttnews%5Btt\_news%5D=232&cHash=c5bf79590657e32554c6683296a8e8aa

﻿

渴求美德而非奖赏。

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