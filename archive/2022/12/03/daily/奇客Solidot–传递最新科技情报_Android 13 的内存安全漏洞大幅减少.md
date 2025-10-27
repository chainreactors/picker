---
title: Android 13 的内存安全漏洞大幅减少
url: https://www.solidot.org/story?sid=73540
source: 奇客Solidot–传递最新科技情报
date: 2022-12-03
fetch_date: 2025-10-04T00:24:26.984623
---

# Android 13 的内存安全漏洞大幅减少

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

**本文已被查看 8533 次**

## Android 13 的内存安全漏洞大幅减少

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2022年12月02日 16时43分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=73540&appkey=1370085986&title=Android%2013%20%E7%9A%84%E5%86%85%E5%AD%98%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E%E5%A4%A7%E5%B9%85%E5%87%8F%E5%B0%91 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自电波骑士**

过去十多年内存安全漏洞占到了所有产品漏洞的 65% 以上，但从 2019 到 2022 年 Android 中内存安全漏洞的比例从 76% 降至了 35%，2022 年是第一年内存安全漏洞不再占到 Android 漏洞的半数以上。Google 的 Jeffrey Vander Stoep 表示，虽然相关性不能代表因果性，但内存安全漏洞的减少与采用 Rust 语言有关。 Android 12 开始支持 Rust 作为 C/C++ 的内存安全替代语言。在 Android 13 中，所有新增原生代码(C/C++/Rust) 中有 21% 是 Rust 编写的，Android 开源项目 AOSP 中有大约 150 万行 Rust 代码，到目前为止 Rust 代码中没有发现任何内存安全漏洞。Google 并不预计这个数字会永远保存为零，但相对于 Rust 的代码行数，Rust 实现了其预期的目的，即防止最常见的内存安全漏洞。
https://security.googleblog.com/2022/12/memory-safe-languages-in-android-13.html

﻿

具有新想法的人在其想法实现之前是个怪人。

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