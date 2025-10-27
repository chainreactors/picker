---
title: 英特尔 Linux 补丁将旧版本的微码视为漏洞
url: https://www.solidot.org/story?sid=79716
source: 奇客Solidot–传递最新科技情报
date: 2024-11-09
fetch_date: 2025-10-06T19:16:58.803461
---

# 英特尔 Linux 补丁将旧版本的微码视为漏洞

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

**本文已被查看 32184 次**

## 英特尔 Linux 补丁将旧版本的微码视为漏洞

[![Linux](https://icon.solidot.org/images/topics/topiclinux.png?123)](/search?tid=7 "Linux")
[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2024年11月08日 14时12分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=79716&appkey=1370085986&title=%E8%8B%B1%E7%89%B9%E5%B0%94%20Linux%20%E8%A1%A5%E4%B8%81%E5%B0%86%E6%97%A7%E7%89%88%E6%9C%AC%E7%9A%84%E5%BE%AE%E7%A0%81%E8%A7%86%E4%B8%BA%E6%BC%8F%E6%B4%9E "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自先知**

英特尔工程师 Dave Hansen 递交了一则 RFC 补丁，建议内核维护一个针对每个英特尔 CPU 系列的最新微码列表，如果 CPU 运行旧版本的微码，那么将会被视为存在漏洞而对用户发出警告，但这并不会阻止旧版本微码的 CPU 继续工作。微码通常被用于缓解 CPU 问题，其中很大一部分问题与安全相关。Hansen 认为如果系统运行旧版本的微码，那么你就无法相信系统是安全的，所以运行旧版本微码的系统就被视为存在漏洞。
https://www.phoronix.com/news/Linux-Intel-Old-Microcode-Vuln

﻿

读古人的书，一方面要知道古人聪明到怎样，一方面也要知道古人傻到怎样。--胡适

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