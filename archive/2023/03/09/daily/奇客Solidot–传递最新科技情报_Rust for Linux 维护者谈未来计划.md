---
title: Rust for Linux 维护者谈未来计划
url: https://www.solidot.org/story?sid=74329
source: 奇客Solidot–传递最新科技情报
date: 2023-03-09
fetch_date: 2025-10-04T09:01:56.677122
---

# Rust for Linux 维护者谈未来计划

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

**本文已被查看 8388 次**

## Rust for Linux 维护者谈未来计划

[![Linux](https://icon.solidot.org/images/topics/topiclinux.png?123)](/search?tid=7 "Linux")

[Wilson](/~Wilson) (42865)发表于 2023年03月08日 14时48分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=74329&appkey=1370085986&title=Rust%20for%20Linux%20%E7%BB%B4%E6%8A%A4%E8%80%85%E8%B0%88%E6%9C%AA%E6%9D%A5%E8%AE%A1%E5%88%92 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自蒸汽歌剧**

Linux 内核从 6.1 开始加入了对 Rust 语言的初步支持，Rust for Linux 维护者 Miguel Ojeda 接受采访，谈论项目的现状和未来。他表示目前的工作主要是为上游加入足够的抽象，为首批 Rust 驱动做好准备。而首批进入上游的驱动可能包括 Asahi Linux 的 GPU 驱动、Android 的 Binder 和 NVMe 驱动。它们将为未来的 Rust 内核抽象和驱动树立标杆。在此过程中还需要相关的内核维护者参与进来评估和评论代码。一旦 Rust for Linux 准备就绪，内核使用 Rust 的一个明显优点是减少内存相关漏洞。此前的报告显示，七成的漏洞是由于C/C++ 代码库中的内存安全问题导致的。如果使用 Rust 能消除其中大部分或者减轻漏洞的严重程度，那么对终端用户而言意味着安全性改进，需要紧急给内核打补丁的次数减少，企业也可能更少遭到入侵。
Asahi Linux 项目已经发布了支持苹果 AGX GPU 处理器的驱动早期版本。
https://www.heise.de/hintergrund/Three-Questions-and-Answers-Rust-for-Linux-7532262.html
https://lwn.net/ml/linux-kernel/20230307-rust-drm-v1-0-917ff5bc80a8@asahilina.net/

﻿

要节约用水，尽量和女友一起洗澡--加菲猫

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