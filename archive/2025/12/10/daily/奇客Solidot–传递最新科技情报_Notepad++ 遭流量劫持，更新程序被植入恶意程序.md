---
title: Notepad++ 遭流量劫持，更新程序被植入恶意程序
url: https://www.solidot.org/story?sid=83021
source: 奇客Solidot–传递最新科技情报
date: 2025-12-10
fetch_date: 2025-12-11T03:23:25.805383
---

# Notepad++ 遭流量劫持，更新程序被植入恶意程序

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20251210)
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

![](https://icon.solidot.org/images/default_ads_gaofei84e_0704.jpg)

## 消息

**本文已被查看 412 次**

## Notepad++ 遭流量劫持，更新程序被植入恶意程序

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2025年12月11日 00时50分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=83021&appkey=1370085986&title=Notepad%2B%2B%20%E9%81%AD%E6%B5%81%E9%87%8F%E5%8A%AB%E6%8C%81%EF%BC%8C%E6%9B%B4%E6%96%B0%E7%A8%8B%E5%BA%8F%E8%A2%AB%E6%A4%8D%E5%85%A5%E6%81%B6%E6%84%8F%E7%A8%8B%E5%BA%8F "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自哈尔的移动城堡**

Notepad++ 发布安全警告，它遭遇了流量劫持，部分地区的更新程序被植入恶意程序。调查发现，Notepad++ 更新程序 WinGUp 的流量被劫持到恶意服务器，下载恶意可执行文件。更新程序使用版本检查功能查询 URL“https://notepad-plus-plus.org/update/getDownloadUrl.php”并评估返回的 XML 文件。更新程序使用 XML 文件中列出的 Download-URL，将文件保存到 %TEMP% 文件夹并执行。任何能拦截和篡改此流量的攻击者都可以更改 Download-URL。Notepad++ v8.8.7 前它使用了自签名证书，允许攻击者创建篡改后的更新并将其推送给受害者。从 v8.8.7 开始 Notepad++ 使用了来自 GlobalSign 签发的合法证书进行签名。
https://notepad-plus-plus.org/news/v889-released/
https://www.heise.de/news/Notepad-Updater-installierte-Malware-11109571.html

[回复](/comments?sid=83021&op=reply&type=story)

﻿

就算它工作不正常也别担心。如果一切正常，你早该失业了--Mosher的软件工程定律

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20251210)
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