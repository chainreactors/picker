---
title: 十分之一 Tor 出口节点被用于发动中间人攻击
url: https://www.solidot.org/story?sid=85666
source: 奇客Solidot–传递最新科技情报
date: 2026-10-20
fetch_date: 2026-10-21T06:49:38.507577
---

# 十分之一 Tor 出口节点被用于发动中间人攻击

* 至顶科技：
* [至顶网](https://www.zhiding.cn/ "至顶网")
* [科技行者](https://www.techwalker.com/ "科技行者")
* [Solidot](https://www.solidot.org/ "Solidot")

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20261020)
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

**本文已被查看 2387 次**

## 十分之一 Tor 出口节点被用于发动中间人攻击

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2026年10月20日 23时22分 星期二 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=85666&appkey=1370085986&title=%E5%8D%81%E5%88%86%E4%B9%8B%E4%B8%80%20Tor%20%E5%87%BA%E5%8F%A3%E8%8A%82%E7%82%B9%E8%A2%AB%E7%94%A8%E4%BA%8E%E5%8F%91%E5%8A%A8%E4%B8%AD%E9%97%B4%E4%BA%BA%E6%94%BB%E5%87%BB "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自破译滑铁卢**

10 月 2 日攻击者利用其控制的 333 个出口节点协同拦截 SSH 连接发动中间人攻击。Tor 出口节点是构成 Tor 回路的三个中继的最后一跳，连接了 Tor 匿名网络与开放互联网。根据目标网站使用的是 HTTPS 还是 HTTP 协议，决定了出口节点是否能看到和操纵用户访问的内容。目前整个 Tor 网络共有大约 3000 个出口节点，这意味着攻击者控制了十分之一的出口中继。攻击者实际上早在 8 月就控制了运行 Tor 节点的服务器，部署了恶意程序 Ebury 1.8.3，它是一种 Linux 下的 OpenSSH 后门和凭据窃取程序。此次协同攻击有两个目的：尽可能多收集未加密邮件流量；拦截 SSH 连接——即 SSH 中间人攻击。如果攻击期间你的 Tor 回路经过了 333 个恶意出口节点之一，那么当你尝试通过 22 端口建立 SSH 连接，你的请求会被重定向到 12 台 SSH 拦截服务器中的一台。如果用户无视中间人攻击警告，那么攻击者将会窃取密码，建立服务器连接，监视用户输入的每一条命令，以及植入 Ebury。Tor 项目团队于 10 月 4 日将这些恶意节点标记为 BadExit，即 Tor 回路不再利用这些节点出口流量。10 月 5 日所有恶意节点全部关闭，部分是 Tor 节点运营者接到通知后关闭的，部分是攻击者自己关闭的。鉴于幕后攻击者收集未加密邮件数据，此次行动可能是出于经济动机。
https://kaba.cx/posts/20261020\_Tor/

[回复](/comments?sid=85666&op=reply&type=story)

﻿

人们还往往把真理和错误混在一起去教人，而坚持的却是错误。--歌德

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20261020)
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