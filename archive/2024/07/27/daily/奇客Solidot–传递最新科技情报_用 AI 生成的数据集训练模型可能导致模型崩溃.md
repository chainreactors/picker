---
title: 用 AI 生成的数据集训练模型可能导致模型崩溃
url: https://www.solidot.org/story?sid=78804
source: 奇客Solidot–传递最新科技情报
date: 2024-07-27
fetch_date: 2025-10-06T17:43:02.088777
---

# 用 AI 生成的数据集训练模型可能导致模型崩溃

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

**本文已被查看 6788 次**

## 用 AI 生成的数据集训练模型可能导致模型崩溃

[![人工智能](https://icon.solidot.org/images/topics/topicAI.png?123)](/search?tid=151 "人工智能")

[Wilson](/~Wilson) (42865)发表于 2024年07月26日 12时54分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=78804&appkey=1370085986&title=%E7%94%A8%20AI%20%E7%94%9F%E6%88%90%E7%9A%84%E6%95%B0%E6%8D%AE%E9%9B%86%E8%AE%AD%E7%BB%83%E6%A8%A1%E5%9E%8B%E5%8F%AF%E8%83%BD%E5%AF%BC%E8%87%B4%E6%A8%A1%E5%9E%8B%E5%B4%A9%E6%BA%83 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自银色金属恋人**

根据发表在《自然》期刊上的一项研究，Google DeepMind 和牛津大学的研究人员发现，用 AI 生成的数据集训练 AI 模型可能导致模型崩溃，即在数代之后产生无意义的输出。举例来说，模型从中世纪建筑文本开始，到第九代输出了毫不相干的长耳大野兔。研究人员发现，AI 难以掌握训练数据集中不常见的文本行，后续在此输出上的训练无法延续这些微妙差异。以这种方式基于早期模型的输出训练新模型最终会陷入递归循环。以生成狗图像的模型为例，AI 模型倾向于重新创造训练数据中最常见的犬种，金毛猎犬相比贝吉格里芬凡丁犬（Petit Basset Griffon Vendeen）更常见，因此金毛猎犬会被过度代表。如果用过度代表金毛猎犬的数据集训练后续模型，问题将会愈发严重，后续模型将会忘记贝吉格里芬凡丁犬不知名犬种的存在，它将只会生成金毛猎犬的图像。最终模型将会崩溃，无法生成有意义的内容。
https://www.nature.com/articles/d41586-024-02420-7
https://tech.slashdot.org/story/24/07/26/0016252/ai-models-face-collapse-if-they-overdose-on-their-own-output

﻿

一个人知道自己为什么而活，就可以忍受任何一种生活。——尼采

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