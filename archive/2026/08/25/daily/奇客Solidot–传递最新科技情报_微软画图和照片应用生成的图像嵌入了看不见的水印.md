---
title: 微软画图和照片应用生成的图像嵌入了看不见的水印
url: https://www.solidot.org/story?sid=85192
source: 奇客Solidot–传递最新科技情报
date: 2026-08-25
fetch_date: 2026-08-26T03:05:29.414421
---

# 微软画图和照片应用生成的图像嵌入了看不见的水印

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260825)
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

**本文已被查看 2164 次**

## 微软画图和照片应用生成的图像嵌入了看不见的水印

[![人工智能](https://icon.solidot.org/images/topics/topicAI.png?123)](/search?tid=151 "人工智能")

[Edwards](/~Edwards) (42866)发表于 2026年08月25日 19时12分 星期二 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=85192&appkey=1370085986&title=%E5%BE%AE%E8%BD%AF%E7%94%BB%E5%9B%BE%E5%92%8C%E7%85%A7%E7%89%87%E5%BA%94%E7%94%A8%E7%94%9F%E6%88%90%E7%9A%84%E5%9B%BE%E5%83%8F%E5%B5%8C%E5%85%A5%E4%BA%86%E7%9C%8B%E4%B8%8D%E8%A7%81%E7%9A%84%E6%B0%B4%E5%8D%B0 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自摩若博士岛**

Windows 画图（Paint）和照片（Photos）应用都集成了微软的 AI 工具 Copilot，支持通过本地模型和云端生成图像。AI 生成的图像会嵌入两个水印，其一是可见的 Copilot logo，其二是不可见的能跟踪到用户身份的唯一识别码 GUID。画图和照片使用的本地模型（仅限于 Copilot+ PC）共四个文件，容量不到 400MB，无论本地还是云端用户输入的提示词都会发送到微软服务器进行内容审核，服务器会返回 GUID 以及审核后的提示词，GUID 随后就嵌入在 AI 生成的图像之中。
https://xusheng.dev/posts/reversing/mspaint\_invisible\_watermark/main/
https://learn.microsoft.com/zh-cn/dotnet/api/system.guid?view=net-10.0

[PEC 2026 AI创新者大会暨第三届提示工程峰会邀您参会](https://jinshuju.com/f/QMxIGi?x_field_1=solidot)
[回复](/comments?sid=85192&op=reply&type=story)

﻿

冬天已经到来，春天还会远吗？--雪莱

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260825)
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