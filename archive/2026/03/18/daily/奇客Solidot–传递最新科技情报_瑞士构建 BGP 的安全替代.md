---
title: 瑞士构建 BGP 的安全替代
url: https://www.solidot.org/story?sid=83798
source: 奇客Solidot–传递最新科技情报
date: 2026-03-18
fetch_date: 2026-03-19T04:19:27.200178
---

# 瑞士构建 BGP 的安全替代

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260318)
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

**本文已被查看 1902 次**

## 瑞士构建 BGP 的安全替代

[![互联网](https://icon.solidot.org/images/topics/topicinternet.png?123)](/search?tid=17 "互联网")

[Edwards](/~Edwards) (42866)发表于 2026年03月18日 18时00分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=83798&appkey=1370085986&title=%E7%91%9E%E5%A3%AB%E6%9E%84%E5%BB%BA%20BGP%20%E7%9A%84%E5%AE%89%E5%85%A8%E6%9B%BF%E4%BB%A3 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自圣天秤星**

边界网关路由（BGP）不是为安全设计的，而是为构成互联网的数以千计的自治系统之间大规模快速路由数据包设计的。过去四十年，BGP 运作良好，但其安全缺陷也日益显现。为堵上漏洞，BGP 引入了一系列补丁和扩展如 Resource Public Key Infrastructure (RPKI)、BGPsec 和 RPKI-based Route Origin Authorization (ROA)，但无法从根本上解决问题。瑞士苏黎世联邦理工学院开发的 SCION——代表 Scalability, Control, and Isolation On Next-Generation Networks——尝试从根本上改变互联网的路由架构，提供一种更安全的替代。SCION 的首席架构师 Adrian Perrig 是苏黎世联邦理工的计算机科学教授，一直致力于提升互联网的安全。他发现安全无法拼拼凑凑，必须彻底改变设计。SCION 尝试通过三个关联机制解决 BGP 的安全缺陷：其一是多路径路由，两点之间能同时建立数十条甚至数百条并行路径，一条路径发生故障，系统会在几毫秒内完成重路由；其二是不依赖证书颁发机构的隔离域名 ISD 机制；其三是加密路径验证，路径上的每个路由器都提供一个加密签名。瑞士银行已成功测试了 SCION。
https://www.theregister.com/2026/03/17/switzerland\_bgp\_alternative/

[回复](/comments?sid=83798&op=reply&type=story)

﻿

你自己的代码如果超过6个月不看，再看的时候也一样像是别人写--伊格尔森定律

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260318)
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