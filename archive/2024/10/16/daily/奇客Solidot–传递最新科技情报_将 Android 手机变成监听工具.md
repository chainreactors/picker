---
title: 将 Android 手机变成监听工具
url: https://www.solidot.org/story?sid=79499
source: 奇客Solidot–传递最新科技情报
date: 2024-10-16
fetch_date: 2025-10-06T18:53:33.535789
---

# 将 Android 手机变成监听工具

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

**本文已被查看 7597 次**

## 将 Android 手机变成监听工具

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")
[![Android ](https://icon.solidot.org/images/topics/topicAndroid.png?123)](/search?tid=171 "Android ")

[Wilson](/~Wilson) (42865)发表于 2024年10月15日 23时48分 星期二 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=79499&appkey=1370085986&title=%E5%B0%86%20Android%20%E6%89%8B%E6%9C%BA%E5%8F%98%E6%88%90%E7%9B%91%E5%90%AC%E5%B7%A5%E5%85%B7 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自夏日永别**

之前的实验表明，智能手机中的陀螺仪和加速计等惯性测量单元（IMU），可以通过检测声波振动监听对话。这意味着，即使是一个没有开启麦克风权限的应用程序也可以通过 IMU 获得对话内容。为了不让攻击者获得准确信息，Google 将 Android 应用从 IMU 采样数据的频率限制在每秒 200 次，使攻击者无法准确获得对话内容。根据发表在预印本平台 arXiv 上的预印本，研究人员发现了一个漏洞——通过欺骗陀螺仪和运动传感器在时间上稍微偏移地进行测量，将应用实际采样率从每秒 200 次提高到 400 次，可以突破上述保护措施。利用这种方法，攻击者能修复获得的音频量大大提升。与每秒仅采集 200 个样本相比，他们的方法在 AI 转录时单词错误率降低了 83%。这表明，目前的安全保护措施“不足以防止复杂的窃听攻击发生”，应该对其重新评估。
https://arxiv.org/abs/2409.16438
https://news.sciencenet.cn/htmlnews/2024/10/531588.shtm

﻿

太阳绝不为它所做的善事后悔，也从不指望任何报酬。

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