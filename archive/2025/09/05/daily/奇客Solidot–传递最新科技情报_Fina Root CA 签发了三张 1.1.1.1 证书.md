---
title: Fina Root CA 签发了三张 1.1.1.1 证书
url: https://www.solidot.org/story?sid=82227
source: 奇客Solidot–传递最新科技情报
date: 2025-09-05
fetch_date: 2025-10-02T19:40:37.635788
---

# Fina Root CA 签发了三张 1.1.1.1 证书

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20251001)
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

**本文已被查看 6613 次**

## Fina Root CA 签发了三张 1.1.1.1 证书

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2025年09月04日 23时37分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=82227&appkey=1370085986&title=Fina%20Root%20CA%20%E7%AD%BE%E5%8F%91%E4%BA%86%E4%B8%89%E5%BC%A0%201.1.1.1%20%E8%AF%81%E4%B9%A6 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自探寻者**

Fina Root CA 于今年五月为 Cloudflare 的公共 DNS 服务 1.1.1.1 签发了三张证书，这一错误签发证书的安全事件直到本周三才曝光。Fina Root CA 受到了微软 Microsoft Root Certificate Program 的信任，但 Google、Mozilla 以及苹果 Safari 都未信任该 CA。安全专家称，攻击者能利用该证书发动中间人攻击，拦截最户与 Cloudflare DNS 服务之间的通信，攻击者可使用证书解密、查看和篡改来自 Cloudflare DNS 服务的流量。目前三张证书中的两张仍然有效，Cloudflare 声明它未授权 Fina 签发这些证书，它已展开调查，联络了微软、Fina 以及 Fina 的 TSP 监管机构，目前尚未收到 Fina 的回应。
arstechnica.com/security/2025/09/mis-issued-certificates-for-1-1-1-1-dns-service-pose-a-threat-to-the-internet/

[回复](/comments?sid=82227&op=reply&type=story)

﻿

尊严不值钱，却是我唯一真正拥有的！

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20251001)
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