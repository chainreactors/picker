---
title: 英伟达 CUDA 对机器学习的垄断正逐步瓦解
url: https://www.solidot.org/story?sid=73904
source: 奇客Solidot–传递最新科技情报
date: 2023-01-17
fetch_date: 2025-10-04T04:03:29.990761
---

# 英伟达 CUDA 对机器学习的垄断正逐步瓦解

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

**本文已被查看 5894 次**

## 英伟达 CUDA 对机器学习的垄断正逐步瓦解

[![人工智能](https://icon.solidot.org/images/topics/topicAI.png?123)](/search?tid=151 "人工智能")

[Wilson](/~Wilson) (42865)发表于 2023年01月16日 22时16分 星期一 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=73904&appkey=1370085986&title=%E8%8B%B1%E4%BC%9F%E8%BE%BE%20CUDA%20%E5%AF%B9%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E7%9A%84%E5%9E%84%E6%96%AD%E6%AD%A3%E9%80%90%E6%AD%A5%E7%93%A6%E8%A7%A3 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自美丽新世界**

过去十年，机器学习软件开发框架经历了巨大变化。虽然大部分框架严重依赖于英伟达 CUDA，在 英伟达 CUDA 上有最佳性能。但随着 PyTorch 2.0 和 OpenAI Triton 的到来，英伟达 CUDA 对机器学习的垄断地位正逐渐瓦解。几年前，Google 的 TensorFlow 框架及专用加速器 TPU 具有先发优势，Google 被认为有望在机器学习行业占据主导地位。然而 Google 未能将先发优势转变为行业主导地位。PyTorch 赢了。没有使用 PyTorch 和 GPU 的 Google 孤立于机器学习社区。Google 偏爱自己软件栈和硬件，甚至于以典型的 Google 风格，它还开发了第二个框架 Jax 与自家的 TensorFlow 展开直接竞争。PyTorch 的一大优势是其灵活性，而即将到来的 2.0 将能更容易的利用不同硬件资源。PyTorch 2.0 改进英伟达 A100 GPU 训练性能达 86%，CPU 推理性能提升 26%，显著减少了训练模型所需的计算时间和成本。它还可以扩展到 AMD、英特尔、Tenstorrent、Luminous Computing、特斯拉、Google、亚马逊、微软、Marvell、Meta、Graphcore、Cerebras、SambaNova 等公司生产的 GPU 和加速器上。OpenAI 的 Triton 同样对英伟达的机器学习闭源软件护城河产生冲击，它可以跳过闭源 CUDA 库如 cuBLAS，使用开源库如 cutlass。优化 CUDA 需要对底层硬件有深入了解，而 Triton 能让高级语言达到与使用低级语言相当的性能，提高了可用性。OpenAI Triton 目前只支持英伟达 GPU，但未来将会支持其它硬件制造商。
https://www.semianalysis.com/p/nvidiaopenaitritonpytorch

﻿

计算机就跟比基尼一样，省去了人们许多的胡思乱想。--萨姆·尤因

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