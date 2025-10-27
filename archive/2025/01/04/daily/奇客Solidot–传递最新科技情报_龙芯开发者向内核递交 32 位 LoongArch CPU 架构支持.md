---
title: 龙芯开发者向内核递交 32 位 LoongArch CPU 架构支持
url: https://www.solidot.org/story?sid=80224
source: 奇客Solidot–传递最新科技情报
date: 2025-01-04
fetch_date: 2025-10-06T20:10:37.840639
---

# 龙芯开发者向内核递交 32 位 LoongArch CPU 架构支持

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

**本文已被查看 26445 次**

## 龙芯开发者向内核递交 32 位 LoongArch CPU 架构支持

[![Linux](https://icon.solidot.org/images/topics/topiclinux.png?123)](/search?tid=7 "Linux")

[Wilson](/~Wilson) (42865)发表于 2025年01月03日 14时49分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=80224&appkey=1370085986&title=%E9%BE%99%E8%8A%AF%E5%BC%80%E5%8F%91%E8%80%85%E5%90%91%E5%86%85%E6%A0%B8%E9%80%92%E4%BA%A4%2032%20%E4%BD%8D%20LoongArch%20CPU%20%E6%9E%B6%E6%9E%84%E6%94%AF%E6%8C%81 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自奥泊城的珍宝**

龙芯过去几年一直在开发其自研架构 LoongArch，该架构源自 MIPS，部分受到了开源架构 RISC-V 的启发。Linux 内核早在 2022 年就合并了支持 LoongArch 的补丁，过去几年的支持主要围绕 64 位 LoongArch 架构。龙芯开发者刚刚向内核递交了一组补丁，为内核加入了 32 位 LoongArch 架构支持。在 32 位架构逐渐消失的时代，为什么龙芯要加入 32 位支持？开发者解释说，LoongArch32 在特定领域仍然高度相关，除了嵌入式应用，部分供应商在活跃开发应用级 LoongArch32 处理器，龙芯已发布了两个开源参考硬件实现 openLA500 和 openLA1000。LoongArch32 还被纳入中国国家计算机架构课程和嵌入式系统课程，如全国大学生计算机系统能力大赛就使用了 LoongArch32 CPU。LoongArch32 将尽可能重用 LoongArch64 代码。
https://www.phoronix.com/news/LoongArch-32-bit-Linux-uAPI
https://lore.kernel.org/lkml/20250102-la32-uapi-v1-0-db32aa769b88@flygoat.com/

﻿

法律必须被信仰，否则形同虚设。--伯尔曼

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