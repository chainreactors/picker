---
title: 周下载量逾 20 亿次的 NPM 包被植入恶意代码
url: https://www.solidot.org/story?sid=82258
source: 奇客Solidot–传递最新科技情报
date: 2025-09-10
fetch_date: 2025-10-02T19:54:29.282297
---

# 周下载量逾 20 亿次的 NPM 包被植入恶意代码

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20251001)
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

**本文已被查看 4828 次**

## 周下载量逾 20 亿次的 NPM 包被植入恶意代码

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2025年09月09日 14时30分 星期二 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=82258&appkey=1370085986&title=%E5%91%A8%E4%B8%8B%E8%BD%BD%E9%87%8F%E9%80%BE%2020%20%E4%BA%BF%E6%AC%A1%E7%9A%84%20NPM%20%E5%8C%85%E8%A2%AB%E6%A4%8D%E5%85%A5%E6%81%B6%E6%84%8F%E4%BB%A3%E7%A0%81 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自奇岛**

这可能是历史上影响规模最大的一次供应链攻击：在一位维护者遭到钓鱼攻击导致其账户被攻击者窃取之后，其维护的 20 个 NPM 包被迅速植入了恶意代码，恶意代码旨在窃取加密货币。这些 NPM 包的周下载量超过 20 亿次。维护者 Josh Junon 收到了一封邮件，要求他登录网站更新 2FA 凭证，否则其账户将会被关闭。邮件使用的域名 support.npmjs.help 是在 3 天前创建的，模仿了 npm 官方域名 npmjs.com。在攻击者获得了他的 2FA 凭证之后，立即了更新了其维护的几十个 NPM 包，植入了窃取加密货币的代码，监控涉及以太坊、比特币、Solana、Tron 等加密货币的转账，一旦检测到此类交易，它会将目标钱包地址替换为攻击者控制的钱包地址。受影响的 NPM 包包括了 backslash@0.2.1、chalk@5.6.1、chalk-template@1.1.1、color-convert@3.1.1
、color-name@2.0.1 等等。
www.aikido.dev/blog/npm-debug-and-chalk-packages-compromised

[回复](/comments?sid=82258&op=reply&type=story)

﻿

尊严不值钱，却是我唯一真正拥有的！

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20251001)
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