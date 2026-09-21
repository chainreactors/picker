---
title: 每个 英伟达 GPU 包含了 10-40 个 RISC-V 核心
url: https://www.solidot.org/story?sid=85436
source: 奇客Solidot–传递最新科技情报
date: 2026-09-20
fetch_date: 2026-09-21T07:26:35.350368
---

# 每个 英伟达 GPU 包含了 10-40 个 RISC-V 核心

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260920)
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

**本文已被查看 2342 次**

## 每个 英伟达 GPU 包含了 10-40 个 RISC-V 核心

[![硬件](https://icon.solidot.org/images/topics/topichardware.gif?123)](/search?tid=14 "硬件")

[Edwards](/~Edwards) (42866)发表于 2026年09月21日 00时41分 星期一 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=85436&appkey=1370085986&title=%E6%AF%8F%E4%B8%AA%20%E8%8B%B1%E4%BC%9F%E8%BE%BE%20GPU%20%E5%8C%85%E5%90%AB%E4%BA%86%2010-40%20%E4%B8%AA%20RISC-V%20%E6%A0%B8%E5%BF%83 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自凡尔纳地球三部曲**

英伟达在 2024 年称当年它的 GPU 产品共使用了逾 10 亿 RISC-V 核心。这些 RISC-V 核心没有被用于图形渲染，而是充当了微控制器，执行各类辅助任务，根据型号不同，每个 GPU 包含了 10-40 个 RISC-V 核心。英伟达在 RISC-V 之前使用的是私有微控制器 FAst Logic CONtroller（Falcon）。Falcon 最早于 2005 年随 G98 引入，到了 2016 年单个 GPU 芯片集成了超过 15 个不同的 Falcon 引擎，十年间使用的 Falcon 核心总数约 30 亿个，这些核心被用于视频编解码、电源管理、安全引擎等不同任务。Falcon 为 32 位核心，没有数据缓存，不再满足英伟达的需求，它开始寻找替代，在评估了 Arm、MIPS 等架构之后，它最终选择了开源指令集架构的 RISC-V。
https://www.xda-developers.com/your-nvidia-gpu-dozens-risc-v-cores-one-took-over-graphics-driver/

[回复](/comments?sid=85436&op=reply&type=story)

﻿

计算机没什么用。他们只会告诉你答案。--毕加索

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260920)
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