---
title: LastPass 用户密码库被盗
url: https://www.solidot.org/story?sid=73736
source: 奇客Solidot–传递最新科技情报
date: 2022-12-24
fetch_date: 2025-10-04T02:25:56.556250
---

# LastPass 用户密码库被盗

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

**本文已被查看 7162 次**

## LastPass 用户密码库被盗

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2022年12月23日 14时48分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=73736&appkey=1370085986&title=LastPass%20%E7%94%A8%E6%88%B7%E5%AF%86%E7%A0%81%E5%BA%93%E8%A2%AB%E7%9B%97 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自暗影徘徊**

提供密码管理服务的 LastPass 披露了最新安全事故的调查结果——用户信息和密码库被盗，但短时间内黑客要破解用户的主密码是非常困难的。LastPass 称它最近在第三方云储存服务监测到异常活动，它立即启动了调查。调查发现，黑客利用了今年 8 月入侵开发环境中窃取到的情报，黑客在 8 月的入侵中窃取了部分源代码和私有技术信息，其中包括了 LastPass 在云储存服务中用于访问和解密部分存储卷的凭证和密钥。黑客随后拷贝了用户信息的备份和用户密码库的备份。用户信息包括了公司名称、终端用户名称、账单地址、电子邮件地址、电话号码以及客户访问 LastPass 服务的 IP 地址。用户密码库使用了 256 位 AES 密钥加密，只能通过源自用户主密码使用 Zero Knowledge 零知识架构的唯一加密密钥解密。LastPass 没有储存用户的主密码。黑客可能会通过暴力破解尝试猜出用户的主密码，LastPass 认为这非常困难，它对客户可能遭遇钓鱼攻击发出了警告。
https://blog.lastpass.com/2022/12/notice-of-recent-security-incident/

﻿

发现可能性的界限的唯一办法就是越过这个界限，到不可能中去。--阿瑟·克拉克

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