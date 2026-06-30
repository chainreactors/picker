---
title: 灵晟超算使用的 LX2 处理器
url: https://www.solidot.org/story?sid=84707
source: 奇客Solidot–传递最新科技情报
date: 2026-06-29
fetch_date: 2026-06-30T06:08:57.228265
---

# 灵晟超算使用的 LX2 处理器

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260629)
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

**本文已被查看 2057 次**

## 灵晟超算使用的 LX2 处理器

[![超级电脑](https://icon.solidot.org/images/topics/topicsuperpc.png?123)](/search?tid=124 "超级电脑")

[Edwards](/~Edwards) (42866)发表于 2026年06月29日 17时41分 星期一 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=84707&appkey=1370085986&title=%E7%81%B5%E6%99%9F%E8%B6%85%E7%AE%97%E4%BD%BF%E7%94%A8%E7%9A%84%20LX2%20%E5%A4%84%E7%90%86%E5%99%A8 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自黄泉归来**

Top500 上周公布了最新的超算榜单，深圳国家超算中心的灵晟首次亮相即登顶榜单。灵晟超算在 Linpack 测试中比排名第二的美国劳伦斯利弗莫尔国家实验室 El Capitan 超算快 22%，在 HPCG 测试中快 26%。它是首个仅靠 CPU 实现持续双精度浮点性能逾 2 Exaflops 的超算系统，美国的超算使用了 GPU 加速器。据 Chips and Cheese 根据相关幻灯片和相关 arXiv 论文报道，灵晟使用的 LX2 CPU 是基于 ARMv9.2 架构，支持 Scalable Matrix Extension(SME)指令集。相比下日本 ARM 超算富岳(Fugaku)是基于 ARMv8 架构，在今天已经相当老了。LX2 的每个核心都有 32 KB 的 L1 指令缓存和 32 KB 的 L1 数据缓存。芯片由两个计算模块（die）组成，每个模块包含四个 40 核心簇。每个簇有 2 个核心被禁用，因此每个簇有 38 个活跃核心，每个模块有 152 个活跃核心。每个簇配备 28.5 MB 的 L2 缓存，每个模块有 114 MB 的 L2 缓存，整个 LX2 封装有 304 个活跃核心和 228 MB 的总 L2 缓存。304 个核心以 1.55 GHz 运行，每个 LX2 CPU 提供 60.3 TFLOP/s 的 FP64 计算性能，功耗为 690 瓦。LX2 配备了八个“高带宽内存”，带宽为 4 TB/s（另一篇报道称 4 TB/s per chiplet，8 TB/s per socket）。所谓的高带宽内存可能不是 HBM。灵晟超算系统包含了逾 22,000 个节点和 1379 万个 CPU 核心。
https://arxiv.org/abs/2605.08633v1
https://chipsandcheese.com/p/top500-at-isc26-we-have-a-new-number
https://www.solidot.org/story?sid=84657

[回复](/comments?sid=84707&op=reply&type=story)

﻿

冬天已经到来，春天还会远吗？--雪莱

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260629)
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