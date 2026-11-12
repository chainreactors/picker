---
title: AMD 公布 Zen 6 CPU 细节
url: https://www.solidot.org/story?sid=85852
source: 奇客Solidot–传递最新科技情报
date: 2026-11-11
fetch_date: 2026-11-12T09:01:31.827549
---

# AMD 公布 Zen 6 CPU 细节

* 至顶科技：
* [至顶网](https://www.zhiding.cn/ "至顶网")
* [科技行者](https://www.techwalker.com/ "科技行者")
* [Solidot](https://www.solidot.org/ "Solidot")

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20261111)
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

**本文已被查看 3487 次**

## AMD 公布 Zen 6 CPU 细节

[![AMD](https://icon.solidot.org/images/topics/topicamd.png?123)](/search?tid=22 "AMD")

[Edwards](/~Edwards) (42866)发表于 2026年11月11日 14时25分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=85852&appkey=1370085986&title=AMD%20%E5%85%AC%E5%B8%83%20Zen%206%20CPU%20%E7%BB%86%E8%8A%82 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自团圆奇遇**

AMD 披露了 Zen 6 CPU 家族的细节。从表面看，Zen 6 是 Zen 5 的自然演进，核心扩展了乱序执行结构以及其它方面的迭代改进。但深入内部会发现 AMD 对核心的多个方面进行了重构，其改进类似从 Zen 1 到 Zen 2。 Zen 6 分支预测错误开销从 Zen 5 的 3.5-4 纳秒缩短到了 3-3.5 纳秒，降低了分支预测错误延迟。Zen 6 能在 L1 指令缓存内实现每周期处理 2 个分支，指令足迹超出 L1 缓存容量后会降至每周期处理 1 个分支，Zen 6 主要提升了分支目标缓冲器（BTB）的速度而非容量。Zen 6 的分支预测单元精确度接近 Zen 5，执行速度则更快。Zen 5 单线程只能使用一个解码集群，而 Zen 6 提升到了单线程能使用两个解码集群。Zen 6 在整数运算上恢复了 Zen 4 的 NOP（空操作）配对机制，每时钟周期最多可处理 16 个 NOP，配备相同的 6 个算术逻辑单元 Zen 6 每时钟周期可完成 5.96 次 64 位加法运算而 Zen 5 为 5.25 次。AMD 将整数乘法单元的数量从 3 个减少到了 2 个，理由是 3 个整数乘法单元带来的性能提升不足以抵消占用的芯片面积成本。Zen 5 的经典核心（Classic cores）与高密度核心（Dense cores）在架构上几乎完全相同，区别在于单个 CCD 内的核心数量以及每个核心所分配的 L3 缓存大小。但 Zen 6 家族发生了变化。AMD 对 Zen 6 与 Zen 6c 进行了架构的差异性设计，Zen 6c 部分乱序执行结构的容量更大，能同时处理更多的指令，更好应对较高的延迟。Zen 6 优化了高频，而 Zen 6c 能更好容忍较高的内存延迟。Zen 6 和 Zen 6c 分别采用 12 核和 32 核的 CCD 设计，每个核心均配备 4 MB 的 L3 缓存。12 核 CCD 拥有 48 MB 的 L3 缓存，32 核 CCD 拥有 128 MB。L3 缓存延迟从 Zen 5 的约 47 个周期增加到 Zen 6 的 55 个周期和 Zen 6c 的 66 个周期，原因可能是缓存容量的增大以及网格互连节点数量的增加。Zen 6 通过更高的时钟频率抵消了延迟增幅，Zen 6c 则因为低时钟频率以及更大的 CCX 显著增加了延迟。AMD 的测试显示 zen 6 整数运算提升 14% 浮点提升 11%，Zen 6c ipc 提升 20%。
https://chipsandcheese.com/p/amds-zen-6-family-feeding-the-beast

[回复](/comments?sid=85852&op=reply&type=story)

﻿

你在活着的同时，也在学习着，无论如何，你活着。--道格拉斯·亚当斯

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20261111)
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