---
title: Wechat2RSS:更新频率策略设计
url: https://buaq.net/go-153249.html
source: unSafe.sh - 不安全
date: 2023-03-14
fetch_date: 2025-10-04T09:28:03.214328
---

# Wechat2RSS:更新频率策略设计

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Wechat2RSS:更新频率策略设计

最近重写了这块逻辑，实现在较低的请求频率下，尽可能快速的获取
*2023-3-13 21:21:50
Author: [blog.xlab.app(查看原文)](/jump-153249.htm)
阅读量:24
收藏*

---

最近重写了这块逻辑，实现在较低的请求频率下，尽可能快速的获取到更新信息

常见的RSS更新情况是设定一个时间间隔，每过一个间隔就检查一次，最开始Wechat2RSS也是这样设计的

设计每3个小时检查一次

把这些公众号的请求时间平摊到3个小时里慢慢请求，每3个小时完成一次轮询

随着公众号数量的增加，3个小时逐渐增加到12个小时，300+个公众号平摊下来大概2分钟一个

仍然频繁的触发微信端的限频

再后来又增加了限频后自动休眠和限频提醒，然后手动解封，周末重新设计了这块的逻辑

## 预测

绝大多数微信公众号的最大更新频率是一天一更，所以请求的频率不用很高

同时又有历史文章数据，可以通过历史更新时间来预测这个作者的下次更新时间

只要在下次更新时间之后检查更新，就能以最小的请求数量，最快的速度获取到更新

简简单单的线性预测，就能得到下次更新时间

考虑到有些作者的更新频率不稳定，且时间间隔较长，订阅的很多可能一年也就更新几次，时间间隔可能在几天到几个月不等，这时线性预测就不太行了，作者突然明天更新，我可能要等几个星期才能收到

为了确保能尽快的获取到更新，每个账号每24个小时都要检查一次，这似乎又回到了原点

## 更新时间

公众号的更新时间要比更新日期更加稳定，毕竟打工人几乎不会在工作时间更新文章

所以可以把更新时间作为预测的依据，来规划什么时间去检查这个公众号

贫瘠的数学知识让我想起了平均数+标准差来描述这个期望

预计更新时间=平均更新时间

检查时间=预计更新时间+一个标准差

## 最后

差点忘记写了，那个限频提醒已经24小时没有出现了

文章来源: https://blog.xlab.app/p/d73537b/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)