---
title: 研究人员提出一种超低成本的 AI 训练方法
url: https://www.solidot.org/story?sid=80489
source: 奇客Solidot–传递最新科技情报
date: 2025-02-07
fetch_date: 2025-10-06T20:37:03.793179
---

# 研究人员提出一种超低成本的 AI 训练方法

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

**本文已被查看 6228 次**

## 研究人员提出一种超低成本的 AI 训练方法

[![人工智能](https://icon.solidot.org/images/topics/topicAI.png?123)](/search?tid=151 "人工智能")

[Wilson](/~Wilson) (42865)发表于 2025年02月06日 23时53分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=80489&appkey=1370085986&title=%E7%A0%94%E7%A9%B6%E4%BA%BA%E5%91%98%E6%8F%90%E5%87%BA%E4%B8%80%E7%A7%8D%E8%B6%85%E4%BD%8E%E6%88%90%E6%9C%AC%E7%9A%84%20AI%20%E8%AE%AD%E7%BB%83%E6%96%B9%E6%B3%95 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自八十天环游地球**

AI 训练通常成本高昂，金额可能多达千万美元。上周五斯坦福大学、华盛顿大学、艾伦 AI 研究所以及 Contextual AI 的研究人员在预印本平台 arXiv 上发表了论文《s1: Simple test-time scaling》，提出了一种超低成本的 AI 训练方法，在 AI 社区引发了轰动。OpenAI 第一个提出了被称为 inference-time scaling laws（推理时间扩展定律）的方法，本质上指的是大模型在输出答案前如果“思考”更长时间那么就可能获得更高的性能。但无论是 OpenAI 还是 R1 都没有给出具体实现方法。在这篇论文中，研究人员给出了一种简单实现：在进行推理时用“等待”替换“停止思考”，迫使其继续思考进行第二次推理并核查第一次的答案。研究人员使用了一个小模型，将 56K 示例数据集筛选到 1K，这 1K 数据集足以在 32B 模型上实现 o1-preview 的性能，额外的数据不会提高性能。他们使用 16 个 NVIDIA H100 进行训练，每次运行 26 分钟，花了约 6 美元。
Tim Kellogg：S1: The $6 R1 Competitor?
arXiv:2501.19393

﻿

你不问我，我就不会说谎话。

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