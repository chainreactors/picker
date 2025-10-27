---
title: GitHub又双叒宕机，背后原因揭秘！
url: https://www.freebuf.com/news/366724.html
source: FreeBuf网络安全行业门户
date: 2023-05-18
fetch_date: 2025-10-04T11:40:03.302047
---

# GitHub又双叒宕机，背后原因揭秘！

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

GitHub又双叒宕机，背后原因揭秘！

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

GitHub又双叒宕机，背后原因揭秘！

2023-05-17 11:12:22

所属地 上海

GitHub的首席安全官和工程部高级副总裁今天分享了关于上周代码托管平台发生的一系列故障的更多细节。

虽然这些事件的根源不尽相同，但从5月9日到5月11日，它们影响了GitHub的大部分主要服务，曾导致大范围的数据库连接和认证失败长达十小时。

![1684291301_64643ee5b6b66a020f3be.png!small](https://image.3001.net/images/20230517/1684291301_64643ee5b6b66a020f3be.png!small)

上周，GitHub经历了几次可用性事件，既有长时间运行的，也有持续时间较短的。目前这些情况均已经得到缓解，所有系统现在都已经在正常运行。

5月9日，GitHub提供Git数据的内部服务的配置发生了变化，导致8个主要服务中断。

第二次故障发生在5月10日，该故障影响了GitHub应用的认证令牌的发放，造成故障的原因是由于负责管理GitHub应用权限的API的高负荷和低效率实施造成的。

5月10日，为GitHub App认证令牌提供服务的数据库集群出现了GitHub App权限写入延迟7倍的情况（状态为黄色）。

在这次事件的大部分时间里，这些授权令牌请求的失败率为8-15%，在短时间内甚至达到76%的峰值。

5月11日，GitHub出现第三次故障，造成故障的原因是服务于Git数据的数据库集群崩溃并触发了自动故障转移机制，导致读取副本丢失。

![1684292564_646443d49798cf73887cb.png!small](https://image.3001.net/images/20230517/1684292564_646443d49798cf73887cb.png!small)

事件历史 (GitHub)

GitHub方面表示，目前正在解决Git数据库崩溃的问题，这个问题目前已经引起了不止一次的事件。这项工作已经在进行中，并将优先得到处理。同时，GitHub也在解决关于数据库故障转移的问题，以确保故障转移总是在没有干预的情况下完全恢复。

GitHub将在5月份可用性报告中分享有关这些中断情况的详细信息，以及目前正在采取哪些措施来解决导致这些中断的问题。同时还会公布事件进展细节，以及如何提高GitHub可用性进展的一般更新等问题。

2022年3月，GitHub也曾遭遇过多次中断，当时该公司表示事件原因是由平台主数据库集群的资源争用问题引起的。

GitHub还在2022年2月发生过一次重大故障。当时一度导致GitHub平台在全球范围内关闭，并且一切访问网站的请求均被阻止。

参考链接：https://www.bleepingcomputer.com/news/technology/github-reveals-reason-behind-last-weeks-string-of-outages/

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)