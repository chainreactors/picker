---
title: Softaculous 遭遇长达 33 小时的 BGP 路由劫持
url: https://www.solidot.org/story?sid=85256
source: 奇客Solidot–传递最新科技情报
date: 2026-09-01
fetch_date: 2026-09-02T06:40:18.632452
---

# Softaculous 遭遇长达 33 小时的 BGP 路由劫持

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260901)
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

**本文已被查看 2011 次**

## Softaculous 遭遇长达 33 小时的 BGP 路由劫持

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2026年09月01日 22时35分 星期二 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=85256&appkey=1370085986&title=Softaculous%20%E9%81%AD%E9%81%87%E9%95%BF%E8%BE%BE%2033%20%E5%B0%8F%E6%97%B6%E7%9A%84%20BGP%20%E8%B7%AF%E7%94%B1%E5%8A%AB%E6%8C%81 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自火星大师**

8 月 28 日 20:57 UTC 左右，一个不相关网络 BGP 路由通告了 Softaculous 使用的 Hetzner IP 段，将部分原本发送到 Softaculous 系统的流量劫持到攻击者控制的服务器。Hetzner 是 Softaculous 的上游基础设施供应商，而 Softaculous 则是一家为 Web 托管服务商提供软件的公司，它的 Virtualizor 控制面板被管理员用于部署和管理 VPS。这次 BGP 路由劫持影响了 Virtualizo 更新服务器以及客户和计费网站。攻击者还从 Let's Encrypt CA 获取了有效的 TLS 证书，Let's Encrypt 的自动域名所有权验证也被劫持到了攻击者控制的 IP。Softaculous 于 8 月 29 日 08:50 UTC 向 Hetzner 报告了事件，Hetzner 随后通过发布相同的路由通告遏制了问题。但攻击者于 20:00 UTC 再次了长达 10 小时的路由劫持。8 月 30 日 05:50-06:10 UTC 路由通告被撤回，劫持停止。Softaculous 建议在攻击期间登陆过的用户立即重置密码，以及重置所有重用该密码的账户。同一时间段内输入过银行卡信息的客户也应检查其账单。攻击者在此期间推送了一个恶意的 Virtualizor 更新包，它建议所有 Virtualizor 用户检查其服务器并轮换凭证。
https://www.theregister.com/security/2026/09/01/33-hour-bgp-hijack-of-softaculous-traffic-prompts-security-scramble/5293608

[PEC 2026 AI创新者大会暨第三届提示工程峰会邀您参会](https://jinshuju.com/f/QMxIGi?x_field_1=solidot)
[回复](/comments?sid=85256&op=reply&type=story)

﻿

肚子大不可怕，可怕的是肚子里没有好东西。--加菲猫

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260901)
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