---
title: MS Edge 被发现会在内存中明文加载所有密码
url: https://www.solidot.org/story?sid=84213
source: 奇客Solidot–传递最新科技情报
date: 2026-05-05
fetch_date: 2026-05-06T05:09:16.245108
---

# MS Edge 被发现会在内存中明文加载所有密码

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260505)
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

**本文已被查看 2245 次**

## MS Edge 被发现会在内存中明文加载所有密码

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2026年05月05日 22时12分 星期二 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=84213&appkey=1370085986&title=MS%20Edge%20%E8%A2%AB%E5%8F%91%E7%8E%B0%E4%BC%9A%E5%9C%A8%E5%86%85%E5%AD%98%E4%B8%AD%E6%98%8E%E6%96%87%E5%8A%A0%E8%BD%BD%E6%89%80%E6%9C%89%E5%AF%86%E7%A0%81 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自一九八四·上来透口气**

MS Edge 浏览器被发现启动时会在内存中明文加载其保存的所有密码。相比下 Chrome 只在需要时解密凭证，没有将所有密码保存在内存中。Edge 和 Chrome 都是基于开源的 Chromium。微软的做法让从内存中抓取重要数据变得更容易，也增加了共享环境下密码泄露的风险。安全研究人员将这一问题报告给了微软，收到的回应是该行为就是这么设计的。研究人员在 GitHub 上发布了概念演示工具 EdgeSavedPasswordsDumper。
https://lemmy.zip/post/63729962?scrollToComments=true
https://github.com/L1v1ng0ffTh3L4N/EdgeSavedPasswordsDumper/tree/main/EdgeSavedPasswordsDumper

[回复](/comments?sid=84213&op=reply&type=story)

﻿

大胆的假设，小心的求证；认真的做事，严肃的做人。 --胡适

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260505)
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