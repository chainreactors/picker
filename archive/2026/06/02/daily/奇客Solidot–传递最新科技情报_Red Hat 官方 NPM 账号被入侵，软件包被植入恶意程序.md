---
title: Red Hat 官方 NPM 账号被入侵，软件包被植入恶意程序
url: https://www.solidot.org/story?sid=84459
source: 奇客Solidot–传递最新科技情报
date: 2026-06-02
fetch_date: 2026-06-03T06:45:45.421947
---

# Red Hat 官方 NPM 账号被入侵，软件包被植入恶意程序

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260602)
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

**本文已被查看 2123 次**

## Red Hat 官方 NPM 账号被入侵，软件包被植入恶意程序

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2026年06月02日 15时09分 星期二 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=84459&appkey=1370085986&title=Red%20Hat%20%E5%AE%98%E6%96%B9%20NPM%20%E8%B4%A6%E5%8F%B7%E8%A2%AB%E5%85%A5%E4%BE%B5%EF%BC%8C%E8%BD%AF%E4%BB%B6%E5%8C%85%E8%A2%AB%E6%A4%8D%E5%85%A5%E6%81%B6%E6%84%8F%E7%A8%8B%E5%BA%8F "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自即临之族**

Red Hat 官方 NPM 账号 @redhat-c​​loud-services 被入侵，该账号相关联的多个软件包植入了窃取凭证的恶意程序。恶意程序旨在窃取 GitHub Action Secret、以及 AWS、GCP、Azure、Kubernetes、HashiCorp Vault、npm 和 CircleCI 等的凭证，它还是一种能自我传播的蠕虫，会利用窃取的 npm 令牌和 npm 的 bypass\_2fa 参数，自动重新发布其它软件包的后门版本。Red Hat 在一份声明中表示，恶意软件包已经移除，它仍然在进行调查，初步分析未发现对客户或合作伙伴环境或 Red Hat 生产系统造成任何影响。
https://www.stepsecurity.io/blog/multiple-redhat-cloud-services-npm-packages-compromised
https://arstechnica.com/security/2026/06/dozens-of-red-hat-packages-backdoored-through-its-offical-npm-channel/

[回复](/comments?sid=84459&op=reply&type=story)

﻿

自由的保证是什么?是对自己不再感到羞耻。--尼采

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260602)
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