---
title: 用开源方法复现 DeepSeek-R1
url: https://www.solidot.org/story?sid=80441
source: 奇客Solidot–传递最新科技情报
date: 2025-01-29
fetch_date: 2025-10-06T20:08:51.551580
---

# 用开源方法复现 DeepSeek-R1

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

**本文已被查看 9095 次**

## 用开源方法复现 DeepSeek-R1

[![开源](https://icon.solidot.org/images/topics/topicopensource.png?123)](/search?tid=3 "开源")
[![人工智能](https://icon.solidot.org/images/topics/topicAI.png?123)](/search?tid=151 "人工智能")

[Wilson](/~Wilson) (42865)发表于 2025年01月28日 20时57分 星期二 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=80441&appkey=1370085986&title=%E7%94%A8%E5%BC%80%E6%BA%90%E6%96%B9%E6%B3%95%E5%A4%8D%E7%8E%B0%20DeepSeek-R1 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自夜袭动物园**

DeepSeek 的最新模型 R1 过去几天引发了轰动，出色的性能和低廉的成本冲击了硅谷的 AI 叙事，以至于最大的 AI 芯片供应商英伟达的股价暴跌，市值蒸发了六千亿美元，迫使英伟达公开声明 DeepSeek 的业务仍然需要大量它的 GPU。DeepSeek R1 虽然声称是开源模型，但它只开源了模型权重，代码和数据集都没有公开。现在开发者宣布了一个真正的开源项目 Open-R1，试图复现 DeepSeek-R1。该项目旨在系统地重建 DeepSeek-R1 的数据和训练流程，验证其声明，突破开放推理模型的界限，为未来模型利用这些技术奠定基础。
Huggingface——Open-R1: a fully open reproduction of DeepSeek-R1

﻿

发现可能性的界限的唯一办法就是越过这个界限，到不可能中去。--阿瑟·克拉克

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