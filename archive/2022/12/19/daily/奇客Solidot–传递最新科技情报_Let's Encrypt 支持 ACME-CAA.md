---
title: Let's Encrypt 支持 ACME-CAA
url: https://www.solidot.org/story?sid=73685
source: 奇客Solidot–传递最新科技情报
date: 2022-12-19
fetch_date: 2025-10-04T01:53:59.545674
---

# Let's Encrypt 支持 ACME-CAA

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

**本文已被查看 3905 次**

## Let's Encrypt 支持 ACME-CAA

[![加密技术](https://icon.solidot.org/images/topics/topicencryption.png?123)](/search?tid=70 "加密技术")

[Wilson](/~Wilson) (42865)发表于 2022年12月18日 22时58分 星期日 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=73685&appkey=1370085986&title=Let%27s%20Encrypt%20%E6%94%AF%E6%8C%81%20ACME-CAA "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自追光的孩子**

Let's Encrypt 宣布支持 ACME-CAA(Certification Authority Authorization)——它是 DNS CAA 记录的一个扩展，旨在堵上 Domain Validation（域名验证）的漏洞。SSL 证书的一个主要目的是限制中间人攻击。而当你从 CA 如 Let's Encrypt 为一个域名申请证书，Let's Encrypt 必须采取措施确认你是域名的合法所有者。域名验证的方法通常是 CA 生成随机的质询字符串，要求你将其托管在自己的域名上。如果你成功的完成了这一要求，那么意味着你控制着该域名，因此是域名的合法运营者。问题是在执行域名验证时你还没有 SSL 证书，也就是说 CA 验证你的域名是通过 HTTP 而不是 HTTPS，这意味着整个域名验证过程容易遭到中间人攻击。ACME-CAA 就是设计堵上漏洞，要求 CAA 记录指向 Let’s Encrypt 的一个特定帐户名。
https://www.devever.net/~hl/acme-caa-live

﻿

把理想运用到真实的事物上，便有了文明。

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