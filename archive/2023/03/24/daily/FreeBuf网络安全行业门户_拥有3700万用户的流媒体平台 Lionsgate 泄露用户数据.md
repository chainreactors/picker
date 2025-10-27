---
title: 拥有3700万用户的流媒体平台 Lionsgate 泄露用户数据
url: https://www.freebuf.com/news/361352.html
source: FreeBuf网络安全行业门户
date: 2023-03-24
fetch_date: 2025-10-04T10:29:46.062737
---

# 拥有3700万用户的流媒体平台 Lionsgate 泄露用户数据

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

拥有3700万用户的流媒体平台 Lionsgate 泄露用户数据

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

拥有3700万用户的流媒体平台 Lionsgate 泄露用户数据

2023-03-23 11:35:07

所属地 上海

![](https://image.3001.net/images/20230323/1679541140_641bc394b081cccb0e938.png!small)

根据Cybernews的研究，娱乐业巨头Lionsgate公司泄露了用户的IP地址和他们在其电影流媒体平台上观看的内容的信息。

在调查过程中，我们的研究人员发现，视频流平台Lionsgate Play通过一个开放的ElasticSearch实例泄露了用户数据。
Cybernews研究团队发现了一个未受保护的20GB的服务器日志，其中包含近3000万个条目，其中最早的是2022年5月。这些日志暴露了用户的IP地址、操作系统和网络浏览记录等用户数据。

研究人员还发现了记录在案的HTTP GET请求的不明哈希值，这是客户提出的请求的记录，通常用于从网络服务器获取数据：当这些请求被提出时，它们被存储在服务器的日志文件中。

## 机遇与危险并增

Lionsgate娱乐公司，拥有几部获得全球认可的知名电影和电视特许经营权，包括《暮光之城》、《电锯惊魂》、《终结者》、《饥饿游戏》和《分歧者》系列。

虽然Netflix以超过2.3亿的用户数保持在所有流媒体平台的首位，但Lionsgate公司拥有超过3700万的全球用户，去年的收入为36亿美元。

在新冠疫情的影响下，在线流媒体平台的人气一直在增长。2022年，在美国，视频点播平台的订阅率达到83%，在8年间增长了30%以上。

但是，随着平台上用户数量的增加，它们正成为网络犯罪分子的目标。即使是轻微的安全漏洞也可能造成严重的损害，然而安全问题往往被忽视。

## 数据可能有助于网络攻击

随着新的流媒体服务越来越多，我们可以看到，错误配置和数据泄露的风险也在增长。

在此次特定的案例中，泄露的信息通常不会在黑客社区中分享。尽管如此，它仍然是敏感的。这些被泄露的数据在有针对性的攻击中可能是有用的，特别是当与其他泄露的或公开的信息相结合时。

例如，用户的IP地址和设备数据的组合可以被恶意行为者利用，对他们进行有针对性的攻击，这样就可以向他们的设备提供恶意的有效载荷。

同时研究人员还表示：攻击者可以将用户的搜索查询和浏览的内容与他们的IP地址进行交叉对比，以建立一个更全面的个人档案。

最后，研究人员提醒道：随着使用数据的增加，攻击者可以确定行为模式，并可能利用这些信息来制作更准确、更有针对性的网络钓鱼攻击。

> 参考链接：securityaffairs.com/143886/security/lionsgate-data-leak.html

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

文章目录

机遇与危险并增

数据可能有助于网络攻击

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