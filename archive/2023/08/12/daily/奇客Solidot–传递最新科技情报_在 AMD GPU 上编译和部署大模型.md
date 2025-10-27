---
title: 在 AMD GPU 上编译和部署大模型
url: https://www.solidot.org/story?sid=75768
source: 奇客Solidot–传递最新科技情报
date: 2023-08-12
fetch_date: 2025-10-04T12:02:29.029198
---

# 在 AMD GPU 上编译和部署大模型

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

**本文已被查看 10288 次**

## 在 AMD GPU 上编译和部署大模型

[![AMD](https://icon.solidot.org/images/topics/topicamd.png?123)](/search?tid=22 "AMD")
[![人工智能](https://icon.solidot.org/images/topics/topicAI.png?123)](/search?tid=151 "人工智能")

[Wilson](/~Wilson) (42865)发表于 2023年08月11日 14时08分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=75768&appkey=1370085986&title=%E5%9C%A8%20AMD%20GPU%20%E4%B8%8A%E7%BC%96%E8%AF%91%E5%92%8C%E9%83%A8%E7%BD%B2%E5%A4%A7%E6%A8%A1%E5%9E%8B "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自繁星若尘**

今天的大模型主要用英伟达的 GPU 训练，但让英伟达一家独大对整个生态系统并不是好事。MLC（Machine learning compilation） 项目正致力于在 AMD GPU 上编译和部署大模型，实现与英伟达 GPU 相当的性能。相对于英伟达深耕了近二十年的 CUDA 软件生态系统，AMD GPU 最大问题在于软件支持，它正通过投资 ROCm 缩小与英伟达的差距。MLC 是一项新兴技术，旨在编译和自动优化机器学习工作负载。它不会为每个后端如 ROCm 或 CUDA 构造特定的内核，而是自动为不同后端生成代码。开发者称，MLC-LLM 方案在 AMD RX 7900 XTX 上的性能达到了英伟达 GeForce RTX 4090 的八成，而 7900 XTX 的价格只有 RTX 4090 的六成。
https://blog.mlc.ai/2023/08/09/Making-AMD-GPUs-competitive-for-LLM-inference

﻿

千里之行始于足下，九层之台起于垒土。

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