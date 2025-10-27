---
title: Linus Torvalds 回应内核合并 Rust 代码争议
url: https://www.solidot.org/story?sid=80618
source: 奇客Solidot–传递最新科技情报
date: 2025-02-22
fetch_date: 2025-10-06T20:36:49.051030
---

# Linus Torvalds 回应内核合并 Rust 代码争议

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

**本文已被查看 34947 次**

## Linus Torvalds 回应内核合并 Rust 代码争议

[![Linux](https://icon.solidot.org/images/topics/topiclinux.png?123)](/search?tid=7 "Linux")

[Wilson](/~Wilson) (42865)发表于 2025年02月21日 23时46分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=80618&appkey=1370085986&title=Linus%20Torvalds%20%E5%9B%9E%E5%BA%94%E5%86%85%E6%A0%B8%E5%90%88%E5%B9%B6%20Rust%20%E4%BB%A3%E7%A0%81%E4%BA%89%E8%AE%AE "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自人猿泰山之世外帝国**

Linus Torvalds 在内核邮件列表上正式回应了 DMA 维护者 Christoph Hellwig 反对合并 Rust 代码的观点。Torvalds 指出，Hellwig 反对的合并请求根本不涉及 DMA 层，而他的做法和反应实际上代表着“作为 DMA
维护者，我控制 DMA 代码怎么用”，Torvalds 认为这不是任何工作的运作模式。他的立场实际上意味着 Rust 代码甚至不能使用，或者与他维护的 DMA 代码有任何交互。作为维护者，Hellwig 负责 DMA 代码，但不负责谁或如何使用。不喜欢 Rust 或者不关心 DMA 中任何 Rust 代码都没问题，但无视 Rust 不想处理 Rust 代码也意味着对 Rust 没有任何发言权。
kernel.org : lore.kernel.org/rust-for-linux/CAHk-=wgLbz1Bm8QhmJ4dJGSmTuV5w\_R0Gwvg5kHrYr4Ko9dUHQ@mail.gmail.com/

﻿

任何有可能出错的事将会出错--墨菲定理

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