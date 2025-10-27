---
title: XZ 5.6.2 释出，移除后门代码
url: https://www.solidot.org/story?sid=78307
source: 奇客Solidot–传递最新科技情报
date: 2024-05-31
fetch_date: 2025-10-06T16:51:00.353169
---

# XZ 5.6.2 释出，移除后门代码

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

**本文已被查看 7188 次**

## XZ 5.6.2 释出，移除后门代码

[![开源](https://icon.solidot.org/images/topics/topicopensource.png?123)](/search?tid=3 "开源")
[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2024年05月30日 14时38分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=78307&appkey=1370085986&title=XZ%205.6.2%20%E9%87%8A%E5%87%BA%EF%BC%8C%E7%A7%BB%E9%99%A4%E5%90%8E%E9%97%A8%E4%BB%A3%E7%A0%81 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自抓落叶**

引发广泛关注的 XZ 后门事件两个月之后，项目维护者 Lasse Collin 释出了新版本 XZ 5.6.2，移除了 v5.6 和 v5.6.1 中的后门代码 CVE-2024-3094。他同时宣布了一位支持维护者 Sam James。对 XZ 后门事件的调查仍然在进行之中。XZ 5.6.2 还修复了一系列 bug，包括修复了用最新 NVIDIA HPC SDK 构建的问题，移除 GNU Indirect Function(IFUNC)支持，XZ 后门代码使用了 IFUNC 支持，但移除主要是因为性能优势太小但复杂性大幅增加。
https://github.com/tukaani-project/xz/
https://www.phoronix.com/news/XZ-5.6.2-Released

﻿

会玩的人才会学

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