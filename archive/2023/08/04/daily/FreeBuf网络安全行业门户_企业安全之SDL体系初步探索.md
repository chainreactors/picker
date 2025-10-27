---
title: 企业安全之SDL体系初步探索
url: https://www.freebuf.com/articles/es/373784.html
source: FreeBuf网络安全行业门户
date: 2023-08-04
fetch_date: 2025-10-04T12:03:12.652537
---

# 企业安全之SDL体系初步探索

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

企业安全之SDL体系初步探索

* ![]()
* 关注

* [企业安全](https://www.freebuf.com/articles/es)

企业安全之SDL体系初步探索

2023-08-03 15:50:46

所属地 上海

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

## 前言

在甲方已经工作了一段时间，在做测试的过程中，也看了一些关于安全体系的文章，下面是我对SDL体系的一些初步了解，分享出来与大家共同探讨。

## SDL简介

SDL(security development lifecycle)是安全开发生命周期，侧重于软件开发的安全保证过程，构建更安全的软件同时降低开发成本。

SDL的核心理念就是将安全考虑集成在软件开发的每一个阶段：需求分析、设计、编码、测试和维护。从需求、设计到发布产品的每一个阶段每都增加了相应的安全活动，以减少软件中漏洞的数量并将安全缺陷降低到最小程度。

SDL体系一般使用于传统的瀑布式开发，其需求比较固定，流程较长。

## SDL目的

过去，企业应对安全问题往往是在上线前甚至上线后通过人工渗透测试、自动化安全扫描等方式发现漏洞，然后反馈至开发人员修改。这种方式存在下面的问题：

1）开发人员修复漏洞的周期长、成本高；

2）问题发现滞后，可能会限于当下技术而搁置安全问题；

3）同样的安全问题频繁出现，安全维护成本居高不下。

SDL就是为了解决这种问题，将安全集合在开发的每个阶段，尽早发现安全漏洞，尽早测试，降低修复安全漏洞的成本。

## 微软SDL流程

为了应对这些问题，不同企业或组织都提出了SDL模型，目前微软的SDL模型可以说是应用更广泛的一种，接下来一起来看看微软的SDL模型。

从下图可以看出，SDL分为了培训，需求，设计，实施，验证，发布，响应阶段。

![1691048679_64cb5ae79b778794c7c9c.png!small?1691048680494](https://image.3001.net/images/20230803/1691048679_64cb5ae79b778794c7c9c.png!small?1691048680494)

流程没有好坏之分，关键是要适合公司的状态，因此，在实际操作的过程中，不可能完全与上面的流程相同，要根据公司的实际情况进行改变。

### 安全培训

培训是最基础的一部分，旨在提高开发团队全体人员的安全意识，这有利于后续的操作。培训应该当做是一个常态化的工作来做，每周或每个月都应该组织安全培训。

开发和测试团队对安全管理工作的理解和支持是SDL体系顺利实施的基础，因此必须重视人员培训，精心开展相关人员培训工作。

目标：提高团队安全意识，减少安全风险发生

培训对象：开发人员，测试人员、项目经理、产品经理等

培训内容：常见的安全漏洞，不安全的组件列表，不安全函数等等

难点：开发人员时间不易协调

###

# 企业安全

![]()

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
已在FreeBuf发表 0 篇文章

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

前言

SDL简介

SDL目的

微软SDL流程

* 安全培训
* 需求&设计
* 实施
* 验证
* 发布
* 响应

SDL面临的挑战

总结

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