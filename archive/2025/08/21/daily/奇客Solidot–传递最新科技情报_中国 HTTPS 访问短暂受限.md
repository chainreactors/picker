---
title: 中国 HTTPS 访问短暂受限
url: https://www.solidot.org/story?sid=82092
source: 奇客Solidot–传递最新科技情报
date: 2025-08-21
fetch_date: 2025-10-07T00:48:25.159235
---

# 中国 HTTPS 访问短暂受限

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20251006)
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

**本文已被查看 5535 次**

## 中国 HTTPS 访问短暂受限

[![互联网](https://icon.solidot.org/images/topics/topicinternet.png?123)](/search?tid=17 "互联网")

[Edwards](/~Edwards) (42866)发表于 2025年08月20日 11时19分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=82092&appkey=1370085986&title=%E4%B8%AD%E5%9B%BD%20HTTPS%20%E8%AE%BF%E9%97%AE%E7%9F%AD%E6%9A%82%E5%8F%97%E9%99%90 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自苹果树下的宇宙飞船**

8 月 20 日北京时间约 00:34 至 01:48 期间，中国 HTTPS 访问短暂受限。苹果报告 APP Store 在此期间遇到问题，但没有给出更多解释。分析显示，所有指向 TCP 443 端口的连接无条件注入伪造的 TCP RST+ACK 包，导致连接中断；无条件的 RST+ACK 注入仅发生在 TCP 443 端口（常用于 HTTPS），未见于其他常见端口（如 22、80、8443）；无条件注入同时扰乱了出入境双方向的连接，但触发机制不对称。
www.apple.com/cn/support/systemstatus/
gfw.report/blog/gfw\_unconditional\_rst\_20250820/zh/

[回复](/comments?sid=82092&op=reply&type=story)

﻿

每个人都受两种教育，一种来自别人，另一种更重要的是来自自己。--爱德华·吉本

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20251006)
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