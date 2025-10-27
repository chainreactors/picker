---
title: 中国公司收购 Polyfill 之后植入恶意程序
url: https://www.solidot.org/story?sid=78560
source: 奇客Solidot–传递最新科技情报
date: 2024-06-30
fetch_date: 2025-10-06T16:55:42.189480
---

# 中国公司收购 Polyfill 之后植入恶意程序

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

**本文已被查看 8052 次**

## 中国公司收购 Polyfill 之后植入恶意程序

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2024年06月29日 21时47分 星期六 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=78560&appkey=1370085986&title=%E4%B8%AD%E5%9B%BD%E5%85%AC%E5%8F%B8%E6%94%B6%E8%B4%AD%20Polyfill%20%E4%B9%8B%E5%90%8E%E6%A4%8D%E5%85%A5%E6%81%B6%E6%84%8F%E7%A8%8B%E5%BA%8F "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自量子之夜**

polyfill.js 是广泛使用的用于支持旧浏览器的开源库，有逾 10 万网站通过 cdn.polyfill.io 域名嵌入了该脚本。今年二月，一家中国公司收购了该域名和相关 Github 账号，然后通过 cdn.polyfill.io 向移动设备植入恶意程序。新拥有者还迅速删除了 Github 上的相关讨论。Polyfill 原作者建议移除该脚本，因为现代浏览器不再需要它，但如果必须使用，可以用 CDN 服务商 Fastly 和 Cloudflare 的替代。安全研究人员发现，植入的恶意程序使用假的 Google 分析域名 www.googie-anaiytics.com 将移动设备用户重定向到博彩网站。代码针对逆向工程有特定保护代码，而且只在特定时间对特定移动设备激活。它在检测到管理员后不会激活。当检测到网络分析服务时它会延迟执行。研究人员给恶意程序起名为“跳转（tiaozhuan）”——恶意代码使用的一个函数名叫 check\_tiaozhuan。
https://sansec.io/research/polyfill-supply-chain-attack

﻿

如果你怀疑自己，那么你的立足点确实不稳固了。

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