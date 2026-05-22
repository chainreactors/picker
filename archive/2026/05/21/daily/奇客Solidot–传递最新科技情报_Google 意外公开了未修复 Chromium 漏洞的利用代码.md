---
title: Google 意外公开了未修复 Chromium 漏洞的利用代码
url: https://www.solidot.org/story?sid=84359
source: 奇客Solidot–传递最新科技情报
date: 2026-05-21
fetch_date: 2026-05-22T06:07:15.710933
---

# Google 意外公开了未修复 Chromium 漏洞的利用代码

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260521)
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

**本文已被查看 2142 次**

## Google 意外公开了未修复 Chromium 漏洞的利用代码

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")
[![Chromium](https://icon.solidot.org/images/topics/topicChromium.png?123)](/search?tid=155 "Chromium")

[Edwards](/~Edwards) (42866)发表于 2026年05月21日 14时02分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=84359&appkey=1370085986&title=Google%20%E6%84%8F%E5%A4%96%E5%85%AC%E5%BC%80%E4%BA%86%E6%9C%AA%E4%BF%AE%E5%A4%8D%20Chromium%20%E6%BC%8F%E6%B4%9E%E7%9A%84%E5%88%A9%E7%94%A8%E4%BB%A3%E7%A0%81 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自飞行村**

Google 周三公开了一个未修复 Chromium 漏洞的利用代码。该漏洞影响所有使用基于 Chromium 浏览器的用户。独立安全研究员 Lyra Rebane 在 2022 年底向 Google 报告了漏洞，但 29 个月后它仍然没有修复。本周三上午 Google 向 Chromium 的 bug 跟踪系统披露了漏洞，Rebane 一开始以为漏洞已经修复了，结果发现根本没有。Google 虽然之后删除了帖子，但其内容已被其它网站存档。该漏洞滥用了 Chromium 的 Browser Fetch API 打开一个持续活动的 Service Worker，恶意网站可通过 JavaScript 触发该 Service Worker 创建连接，监视用户的部分活动，它还可作为代理访问网站和发起 DDoS 攻击。安全研究人员认为这是一个严重的漏洞，它实际上相当于一个受限的后门，将浏览器变成僵尸网络的一部分。
https://arstechnica.com/security/2026/05/google-publishes-exploit-code-threatening-millions-of-chromium-users/

[回复](/comments?sid=84359&op=reply&type=story)

﻿

我并不同意你的观点，但是我誓死捍卫你说话的权利——伏尔泰

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260521)
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