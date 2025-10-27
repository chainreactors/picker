---
title: Tor 项目宣布抵御 DoS 攻击的 Proof-of-Work Defense
url: https://www.solidot.org/story?sid=75895
source: 奇客Solidot–传递最新科技情报
date: 2023-08-26
fetch_date: 2025-10-04T12:00:40.003656
---

# Tor 项目宣布抵御 DoS 攻击的 Proof-of-Work Defense

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

**本文已被查看 6555 次**

## Tor 项目宣布抵御 DoS 攻击的 Proof-of-Work Defense

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2023年08月25日 19时10分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=75895&appkey=1370085986&title=Tor%20%E9%A1%B9%E7%9B%AE%E5%AE%A3%E5%B8%83%E6%8A%B5%E5%BE%A1%20DoS%20%E6%94%BB%E5%87%BB%E7%9A%84%20Proof-of-Work%20Defense "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自飞行村**

Tor 项目宣布了设计抵御 DoS 攻击的工作量防御机制（Proof-of-Work Defense）。工作量证明 PoW 是一种动态的反应机制，在正常工作条件下保持休眠。当 onion 服务面临压力时，PoW 将提示传入的客户端连接连续执行复杂操作，onion 服务将根据客户端的工作量水平进行连接优先排序。此举旨在将 DoS 攻击的成本增加到难以维持的水平，优先考虑合法流量，抑制攻击流量。onion 服务因为优先考虑客户的隐私混淆 IP 地址而容易遭到 DoS 攻击，传统的基于 IP 的速率限制无效，因此 Tor 项目设计了一种工作量证明机制，在不影响客户隐私的同时遏制 DoS 攻击。如果攻击者向 onion 服务发送大量连接请求，PoW 防御会启动增加访问 .onion 网站所需的计算量。增加的计算量对绝大部分设备是可控的，所耗费时间从 5 毫秒到 30 毫秒。攻击流量增加，工作量就会增加，最多需要 1 分钟的工作量。整个过程对用户是不可见的。
https://blog.torproject.org/introducing-proof-of-work-defense-for-onion-services/

﻿

不要向邪恶低头，而是要更勇敢地继续与之对抗。——维吉尔

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