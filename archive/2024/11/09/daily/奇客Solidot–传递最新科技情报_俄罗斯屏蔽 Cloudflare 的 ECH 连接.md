---
title: 俄罗斯屏蔽 Cloudflare 的 ECH 连接
url: https://www.solidot.org/story?sid=79714
source: 奇客Solidot–传递最新科技情报
date: 2024-11-09
fetch_date: 2025-10-06T19:16:59.405370
---

# 俄罗斯屏蔽 Cloudflare 的 ECH 连接

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

**本文已被查看 6423 次**

## 俄罗斯屏蔽 Cloudflare 的 ECH 连接

[![审查](https://icon.solidot.org/images/topics/topicCensorship.png?123)](/search?tid=120 "审查")

[Wilson](/~Wilson) (42865)发表于 2024年11月08日 11时44分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=79714&appkey=1370085986&title=%E4%BF%84%E7%BD%97%E6%96%AF%E5%B1%8F%E8%94%BD%20Cloudflare%20%E7%9A%84%20ECH%20%E8%BF%9E%E6%8E%A5 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自哈特拉斯船长历险记**

Gundaz Aghayev 写道：Cloudflare 最近部署的隐私保护协议 Encrypted Client Hello(ECH)不小心规避了各国的审查系统，俄罗斯已将其封锁。封锁只针对 Cloudflare，其他 ECH 不受影响，俄国 DPI 系统 TSPU (техническиесредства противодействия угрозам) 目前的检测条件是包含 `cloudflare-ech.com`的 TLS SNI 扩展和 TLS ECH 扩展，缺一不可。俄罗斯政府机构“互联网监控和控制中心” (ЦМУ ССОП) 发表文章建议禁用非法的 TLS ECH 技术，甚至停止使用 Cloudflare CDN，转而使用俄国国内的替代如“国家 DDoS 攻击应对系统” (НСПА)。它还指控 Cloudflare 公司由美国国务院授意、侵害各国信息主权。
https://community.cloudflare.com/t/access-issues-in-russia-unable-to-disable-ech-in-free-plan/733401
https://github.com/net4people/bbs/issues/393#issuecomment-2462130383
https://cmu.gov.ru/ru/news/2024/11/07/рекомендуем-отказаться-от-cdn-сервиса-cloudflare/

﻿

任何有可能出错的事将会出错--墨菲定理

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