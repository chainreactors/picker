---
title: 勒索软件使用了微软签名的恶意 Windows 驱动
url: https://www.solidot.org/story?sid=73650
source: 奇客Solidot–传递最新科技情报
date: 2022-12-15
fetch_date: 2025-10-04T01:32:46.394019
---

# 勒索软件使用了微软签名的恶意 Windows 驱动

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

**本文已被查看 5911 次**

## 勒索软件使用了微软签名的恶意 Windows 驱动

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[wanwan](/~wanwan) (42055)发表于 2022年12月14日 19时41分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=73650&appkey=1370085986&title=%E5%8B%92%E7%B4%A2%E8%BD%AF%E4%BB%B6%E4%BD%BF%E7%94%A8%E4%BA%86%E5%BE%AE%E8%BD%AF%E7%AD%BE%E5%90%8D%E7%9A%84%E6%81%B6%E6%84%8F%20Windows%20%E9%A9%B1%E5%8A%A8 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自终极失控**

微软取消了多个 Microsoft 硬件开发者账号，原因是这些账号通过 Windows Hardware Developer Program 认证程序递交的驱动在获得签名之后被用于包括勒索软件在内的网络攻击。微软称，安全公司 SentinelOne、Mandiant 和 Sophos 在 10 月 19 日报告了这些活动，随后的调查发现 Microsoft Partner Center 的多个开发者账号参与了递交恶意驱动获得微软签名的活动。安全研究人员称，他们发现了一种新的工具包，包含了名为 STONESTOP (加载器) 和 POORTRY（内核模式驱动）的组件被用于网络攻击，其中 POORTRY 有微软签名。
https://msrc.microsoft.com/update-guide/vulnerability/ADV220005

﻿

死会引人哭泣。虽则如此，人生的三分之一却在睡眠中打发掉了。--拜伦

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