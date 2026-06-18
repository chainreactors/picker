---
title: Firefox 用 Zlib 的 Rust 语言版本替代了 C 语言版本
url: https://www.solidot.org/story?sid=84608
source: 奇客Solidot–传递最新科技情报
date: 2026-06-17
fetch_date: 2026-06-18T06:50:20.889621
---

# Firefox 用 Zlib 的 Rust 语言版本替代了 C 语言版本

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260617)
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

**本文已被查看 1971 次**

## Firefox 用 Zlib 的 Rust 语言版本替代了 C 语言版本

[![程序](https://icon.solidot.org/images/topics/topicprogramming.png?123)](/search?tid=5 "程序")
[![Firefox](https://icon.solidot.org/images/topics/topicfirefox.png?123)](/search?tid=39 "Firefox")

[Edwards](/~Edwards) (42866)发表于 2026年06月17日 18时31分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=84608&appkey=1370085986&title=Firefox%20%E7%94%A8%20Zlib%20%E7%9A%84%20Rust%20%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC%E6%9B%BF%E4%BB%A3%E4%BA%86%20C%20%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自环游黑海历险记**

Firefox 浏览器从 v151 开始，Gzip 压缩/解压缩就依赖于 zlib-rs 库，用 Rust 语言开发的版本替代了 C 语言版本改进了性能，提供了更好的内存安全性，以及带来了英特尔第 13 代/第 14 代酷睿 CPU 不稳定导致的崩溃问题。致力于用 Rust 语言重写关键库的非盈利组织 Trifecta Tech Foundation 在 2024 年夏天就与 Mozilla 讨论在浏览器中集成 zlib-rs，但从测试到落地花了两年时间，一个重要原因就是 zlib-rs 触发了臭名昭著的英特尔 CPU bug。测试中 zlib-rs 中的一些代码导致英特尔 Raptor Lake CPU 频繁崩溃，开发者最终发现问题与 Huffman 编码写入内存的一个特定指令相关，识别问题之后解决起来就容易了，开发者通过加入一段“不安全代码”修复了该问题。
https://trifectatech.org/blog/zlib-rs-in-firefox/

[回复](/comments?sid=84608&op=reply&type=story)

﻿

在b进位制中，以数n起头的数出现的机率为logb(n + 1) − logb(n)--本福特定律

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260617)
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