---
title: 微软工程师向 Linux 6.13 贡献的代码在发布前夕被禁用
url: https://www.solidot.org/story?sid=80328
source: 奇客Solidot–传递最新科技情报
date: 2025-01-15
fetch_date: 2025-10-06T20:10:39.268587
---

# 微软工程师向 Linux 6.13 贡献的代码在发布前夕被禁用

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

**本文已被查看 29602 次**

## 微软工程师向 Linux 6.13 贡献的代码在发布前夕被禁用

[![Linux](https://icon.solidot.org/images/topics/topiclinux.png?123)](/search?tid=7 "Linux")

[Wilson](/~Wilson) (42865)发表于 2025年01月14日 21时35分 星期二 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=80328&appkey=1370085986&title=%E5%BE%AE%E8%BD%AF%E5%B7%A5%E7%A8%8B%E5%B8%88%E5%90%91%20Linux%206.13%20%E8%B4%A1%E7%8C%AE%E7%9A%84%E4%BB%A3%E7%A0%81%E5%9C%A8%E5%8F%91%E5%B8%83%E5%89%8D%E5%A4%95%E8%A2%AB%E7%A6%81%E7%94%A8 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自理智与情感与海妖**

去年 11 月 Linux 6.13 合并窗口期间，微软工程师贡献的一组补丁允许 Linux x86\_64 将只读执行（ROX)大页用于分配可执行内核。然而距离 Linux 6.13 发布还剩下一周时间（预计本周日也就是 1 月 19 日释出），这组代码被发现会破坏部分启用 Control Flow Integrity (CFI)的设置，以及导致部分英特尔笔记本电脑在休眠后无法恢复。英特尔工程师 Peter Zijlstra 准备递交一个补丁暂时禁用 EXECMEM\_ROX 支持。而 EXECMEM\_ROX 支持补丁被发现在合并到内核主线前没有获得 Linux x86/x86\_64 维护者的签名。
https://www.phoronix.com/news/Linux-6.13-Dropping-EXECMEM\_ROX

﻿

大胆的假设，小心的求证；认真的做事，严肃的做人。 --胡适

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