---
title: 因配置错误，微软可能已泄露大量客户敏感数据
url: https://www.freebuf.com/news/347368.html
source: FreeBuf网络安全行业门户
date: 2022-10-21
fetch_date: 2025-10-03T20:30:36.422231
---

# 因配置错误，微软可能已泄露大量客户敏感数据

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

因配置错误，微软可能已泄露大量客户敏感数据

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

因配置错误，微软可能已泄露大量客户敏感数据

2022-10-20 11:12:08

所属地 上海

据Bleeping Computer 10月19日消息，微软在当天表示，部分客户的敏感信息可能因配置错误的微软服务器而存泄露风险。

![](https://image.3001.net/images/20221020/1666235600_6350bcd0c4ef43dc15027.png!small)

微软透露，这种配置错误可能导致未经身份验证的访问行为，从而泄露微软和客户之间某些业务文件、交易数据以及客户的个人信息，包括姓名、电子邮件地址、电子邮件内容、公司名称和电话号码。但截至目前的调查，微软称没有任何迹象表明客户帐户或系统已经被入侵，并已将情况通知给受影响的客户。

## 泄露的数据可能与全球 65000 个实体有关

虽然微软没有提供有关此数据泄漏的任何其他详细信息，但威胁情报公司 SOCRadar 在当天发布的博客文章中透露，数据保存在配置错误的 Azure Blob 存储桶中。SOCRadar 声称，它能将这些敏感信息与来自 111 个国家和地区的 65000 多个实体相关联，其中存储的文件时间跨度从2017年开始至2022年8月。

SOCRadar 分析认为，暴露的数据具体包括了执行证明 (PoE) 和工作说明书 (SoW) 文件、用户信息、产品订单/报价、项目详细信息、PII（个人身份信息）以及可能泄露知识产权的数据和文件。

微软对SOCRadar关于这一事件的告知和分析表示感谢，但同时指出SOCRadar的博文严重夸大了问题的范围和具体数字，并指出SOCRadar在此事件中发布的数据泄露搜索工具不符合确保客户隐私或安全的最佳利益，并可能使客户面临不必要的安全风险。

## 搜索泄露数据的在线工具

SOCRadar发布的数据泄露搜索工具名为 BlueBleed，它允许公司查找其敏感信息是否与泄露的数据一致。除了在微软配置错误的服务器中发现的内容外，BlueBleed 还允许搜索从其他五个公共存储桶收集的数据。

仅在微软的服务器中，SOCRadar 就声称已经发现了包含敏感信息的 2.4 TB 数据，到目前为止，在分析暴露的文件时发现了超过 335000 封电子邮件、133000 个项目和 548000 个用户名。SOCRadar警告，攻击者可能已经访问了数据，并利用数据进行勒索、钓鱼，或将其放到暗网上拍卖。

> 参考来源：[Microsoft data breach exposes customers’ contact info, emails](https://www.bleepingcomputer.com/news/security/microsoft-data-breach-exposes-customers-contact-info-emails/)

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

泄露的数据可能与全球 65000 个实体有关

搜索泄露数据的在线工具

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