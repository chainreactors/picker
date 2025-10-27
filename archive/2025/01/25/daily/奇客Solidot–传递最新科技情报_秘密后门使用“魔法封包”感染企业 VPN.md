---
title: 秘密后门使用“魔法封包”感染企业 VPN
url: https://www.solidot.org/story?sid=80419
source: 奇客Solidot–传递最新科技情报
date: 2025-01-25
fetch_date: 2025-10-06T20:10:23.685157
---

# 秘密后门使用“魔法封包”感染企业 VPN

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

**本文已被查看 7671 次**

## 秘密后门使用“魔法封包”感染企业 VPN

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2025年01月25日 00时49分 星期六 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=80419&appkey=1370085986&title=%E7%A7%98%E5%AF%86%E5%90%8E%E9%97%A8%E4%BD%BF%E7%94%A8%E2%80%9C%E9%AD%94%E6%B3%95%E5%B0%81%E5%8C%85%E2%80%9D%E6%84%9F%E6%9F%93%E4%BC%81%E4%B8%9A%20VPN "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自海底两万里**

当攻击者利用后门在目标网络获得访问权限之后，他们希望其努力成果不会被竞争对手利用或被安全软件监测出。他们可使用的一种应对之策是为后门配备一个被动代理，该代理将保持休眠状态，直到接收到“魔法封包”。安全公司 Lumin Technology 的研究人员报告了 J-Magic 后门使用“魔法封包”悄悄控制了数十个运行 Juniper Network Junos OS 的企业 VPN。J-Magic 是轻量级后门程序，只运行在内存之中，这增加了其被安全软件检测出的难度。研究人员是在 VirusTotal 上发现了 J-Magic，发现它在 36 个组织的网络内运行，他们不清楚后门是如何安装的。J-Magic 从 2023 年中期至少活跃到 2024 年中期，其目标覆盖半导体、能源、制造业和 IT 垂直企业。
https://blog.lumen.com/the-j-magic-show-magic-packets-and-where-to-find-them/
https://arstechnica.com/security/2025/01/backdoor-infecting-vpns-used-magic-packets-for-stealth-and-security/

﻿

花代价所换来的一点才智，抵过别人传授的数倍不止。

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