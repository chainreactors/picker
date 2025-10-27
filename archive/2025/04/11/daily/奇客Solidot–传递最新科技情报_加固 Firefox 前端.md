---
title: 加固 Firefox 前端
url: https://www.solidot.org/story?sid=81012
source: 奇客Solidot–传递最新科技情报
date: 2025-04-11
fetch_date: 2025-10-06T22:05:05.949269
---

# 加固 Firefox 前端

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

**本文已被查看 6843 次**

## 加固 Firefox 前端

[![Firefox](https://icon.solidot.org/images/topics/topicfirefox.png?123)](/search?tid=39 "Firefox")
[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2025年04月10日 14时23分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=81012&appkey=1370085986&title=%E5%8A%A0%E5%9B%BA%20Firefox%20%E5%89%8D%E7%AB%AF "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自蒲公英王朝2：风暴之墙**

Firefox Application Security Team 安全团队在其博客 Attack & Defense 上发表文章，介绍了在加固 Firefox 前端上所做的工作。Firefox 的大部分 UI 是使用标准 Web 技术如 HTML、CSS 和 JavaScript 实现的，这么做的好处是可以在所有桌面操作系统上使用浏览器引擎渲染前端，缺陷是容易受到注入攻击。最常见的注入攻击是跨站脚本（Cross-Site Scripting 简写 XSS）攻击。为缓解 Firefox UI 的 XSS 和其它注入攻击，安全团队重写了逾 600 个 JavaScript 事件处理程序。这些代码将应用于 Firefox 下一个版本 v138(目前的稳定版本是 Firefox 137)。安全团队表示通过消除一整类攻击类型，他们大幅提高了攻击者利用 Firefox 的门槛。
Attack & Defense：Hardening the Firefox Frontend with Content Security Policies

﻿

什么都比不上厄运更能磨练人的德性。——莎士比亚

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