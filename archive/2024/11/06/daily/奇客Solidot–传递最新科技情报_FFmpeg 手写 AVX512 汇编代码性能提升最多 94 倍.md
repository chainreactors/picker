---
title: FFmpeg 手写 AVX512 汇编代码性能提升最多 94 倍
url: https://www.solidot.org/story?sid=79684
source: 奇客Solidot–传递最新科技情报
date: 2024-11-06
fetch_date: 2025-10-06T19:18:27.623897
---

# FFmpeg 手写 AVX512 汇编代码性能提升最多 94 倍

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

**本文已被查看 5391 次**

## FFmpeg 手写 AVX512 汇编代码性能提升最多 94 倍

[![开源](https://icon.solidot.org/images/topics/topicopensource.png?123)](/search?tid=3 "开源")

[Wilson](/~Wilson) (42865)发表于 2024年11月05日 17时02分 星期二 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=79684&appkey=1370085986&title=FFmpeg%20%E6%89%8B%E5%86%99%20AVX512%20%E6%B1%87%E7%BC%96%E4%BB%A3%E7%A0%81%E6%80%A7%E8%83%BD%E6%8F%90%E5%8D%87%E6%9C%80%E5%A4%9A%2094%20%E5%80%8D "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自黑暗之潮**

开源多媒体编解码器项目 FFmpeg 的开发者通过手写实现优化了 AVX-512 指令集的汇编代码路径，加速 FFmpeg 多媒体处理库中的特定功能，相比标准实现，性能提升了 3-94 倍。手写汇编代码路径在视频行业是相当少见的。AVX-512 支持使用 512 位寄存器并行处理大量数据，一次操作能处理最多 16 个单精度 FLOPS 或 8 个双精度 FLOPS，它对视频和图像处理等计算密集型任务很有用。英特尔 12 到 14 代酷睿处理器禁用了 AVX-512 指令集，目前完整支持 AVX-512 的消费者 CPU 是 AMD 最近上市的 Ryzen 9000 系列处理器。
https://news.slashdot.org/story/24/11/04/2140206/ffmpeg-devs-boast-of-up-to-94x-performance-boost-after-implementing-handwritten-avx-512-assembly-code

﻿

不管我们已经观察到多少只白天鹅，都不能确立“所有天鹅皆为白色”的理论。只要看见一只黑天鹅就可以驳倒它。——卡尔·波普尔

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