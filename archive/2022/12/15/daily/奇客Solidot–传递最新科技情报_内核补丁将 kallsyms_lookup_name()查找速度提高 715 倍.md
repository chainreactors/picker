---
title: 内核补丁将 kallsyms_lookup_name()查找速度提高 715 倍
url: https://www.solidot.org/story?sid=73648
source: 奇客Solidot–传递最新科技情报
date: 2022-12-15
fetch_date: 2025-10-04T01:32:46.936506
---

# 内核补丁将 kallsyms_lookup_name()查找速度提高 715 倍

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

**本文已被查看 10849 次**

## 内核补丁将 kallsyms\_lookup\_name()查找速度提高 715 倍

[![Linux](https://icon.solidot.org/images/topics/topiclinux.png?123)](/search?tid=7 "Linux")

[Wilson](/~Wilson) (42865)发表于 2022年12月14日 17时25分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=73648&appkey=1370085986&title=%E5%86%85%E6%A0%B8%E8%A1%A5%E4%B8%81%E5%B0%86%20kallsyms_lookup_name%28%29%E6%9F%A5%E6%89%BE%E9%80%9F%E5%BA%A6%E6%8F%90%E9%AB%98%20715%20%E5%80%8D "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自你的名字**

Linux 6.2 合并了华为开发者 Zhen Lei 递交的一个补丁，将 kallsyms\_lookup\_name()的查找速度提高了 715 倍。kallsyms\_lookup\_name() 用于根据名字查找一个符号的地址，能用于查找内核符号表中的任何符号。Zhen Lei 此前在补丁描述中解释说，目前内核使用的查找方法是将 kallsyms\_names 中的符号逐一展开，然后查找，这种算法的时间复杂度是 O(n)。如果像地址一样将名字按升序排序，可以使用二叉树搜索。这种算法的时间复杂度是 O(log(n))。从 O(n) 到 O(log(n)) 查找时间可以大幅减少。
https://www.phoronix.com/news/Linux-6.2-Modules

﻿

什么都比不上厄运更能磨练人的德性。——莎士比亚

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