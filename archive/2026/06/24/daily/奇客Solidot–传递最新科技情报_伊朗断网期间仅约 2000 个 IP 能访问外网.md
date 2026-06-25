---
title: 伊朗断网期间仅约 2000 个 IP 能访问外网
url: https://www.solidot.org/story?sid=84665
source: 奇客Solidot–传递最新科技情报
date: 2026-06-24
fetch_date: 2026-06-25T06:08:55.915864
---

# 伊朗断网期间仅约 2000 个 IP 能访问外网

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260624)
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

**本文已被查看 1919 次**

## 伊朗断网期间仅约 2000 个 IP 能访问外网

[![审查](https://icon.solidot.org/images/topics/topicCensorship.png?123)](/search?tid=120 "审查")

[Edwards](/~Edwards) (42866)发表于 2026年06月24日 16时46分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=84665&appkey=1370085986&title=%E4%BC%8A%E6%9C%97%E6%96%AD%E7%BD%91%E6%9C%9F%E9%97%B4%E4%BB%85%E7%BA%A6%202000%20%E4%B8%AA%20IP%20%E8%83%BD%E8%AE%BF%E9%97%AE%E5%A4%96%E7%BD%91 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自帽子里的天空**

伊朗今年早些时候全国范围断网，持续数月之久。在断网期间，伊朗实施了白名单制度，也就是只有处于白名单内的极少数 IP 地址才能访问外网。研究人员利用位于伊朗境内的一台 VPS 以及位于匈牙利、美国以及日本的 VPS，根据伊朗自治系统通过 BGP 宣布的 IP 段总数约 11,766,454 个 IP 地址，伪造这些 IP 地址进行穷举，观察哪些 IP 能访问外网。结果显示，能访问外网的 IP 大约有 2000 个。研究人员还发现，即使这些 IP 能访问外网，它们也不能随意访问任何网站，而是受到了基于 SNI 的过滤机制的约束。但白名单 IP 地址也不是所有都受到 SNI 过滤，测试的 IP 至少有半数不受任何 SNI 过滤。这意味着白名单 IP 也存在不同的访问策略。
https://randlab.engineering.ucsc.edu/blogs/iran-allowlist/

[回复](/comments?sid=84665&op=reply&type=story)

﻿

真正的无知不是知识的缺乏，而是拒绝获取知识。——卡尔·波普尔

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260624)
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