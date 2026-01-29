---
title: 微软错误配置将 example.com 流量重路由到日本公司域名
url: https://www.solidot.org/story?sid=83416
source: 奇客Solidot–传递最新科技情报
date: 2026-01-28
fetch_date: 2026-01-29T04:04:17.175184
---

# 微软错误配置将 example.com 流量重路由到日本公司域名

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260128)
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

**本文已被查看 1797 次**

## 微软错误配置将 example.com 流量重路由到日本公司域名

[![Bug](https://icon.solidot.org/images/topics/topicbug.png?123)](/search?tid=53 "Bug")

[Edwards](/~Edwards) (42866)发表于 2026年01月28日 17时11分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=83416&appkey=1370085986&title=%E5%BE%AE%E8%BD%AF%E9%94%99%E8%AF%AF%E9%85%8D%E7%BD%AE%E5%B0%86%20example.com%20%E6%B5%81%E9%87%8F%E9%87%8D%E8%B7%AF%E7%94%B1%E5%88%B0%E6%97%A5%E6%9C%AC%E5%85%AC%E5%8F%B8%E5%9F%9F%E5%90%8D "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自我是6号**

微软被发现将专门用于测试的 example.com 的流量重路由到日本住友电工的域名 sei.co.jp。该错误配置已经修正，微软表示正对此展开调查。example.com 以及 example.net 和 example.org 是保留用于测试的域名，被要求解析到 IANA 指定的 IP，不应该被任何一方访问。但 Azure 和其它微软网络中的设备此前被发现一直在将部分 example.com 流量路由到 sei.co.jp 的子域名。而在 Outlook 中设置测试账号 test@example.com 时邮件流量会自动配置路由到两个 sei.co.jp 子域名：imapgms.jnet.sei.co.jp 和 smtpgms.jnet.sei.co.jp。目前不清楚住友电工为什么会卷入此事。 Tinyapps.org 本月初报道称，该错误配置已存在五年之久。
https://arstechnica.com/information-technology/2026/01/odd-anomaly-caused-microsofts-network-to-mishandle-example-com-traffic/
https://tinyapps.org/blog/microsoft-mishandling-example-com.html

[回复](/comments?sid=83416&op=reply&type=story)

﻿

所有小说写的都是真事。怕吓着你们才叫小声说。 --王朔

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260128)
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