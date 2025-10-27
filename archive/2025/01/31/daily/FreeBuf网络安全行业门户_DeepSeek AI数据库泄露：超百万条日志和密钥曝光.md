---
title: DeepSeek AI数据库泄露：超百万条日志和密钥曝光
url: https://www.freebuf.com/articles/420968.html
source: FreeBuf网络安全行业门户
date: 2025-01-31
fetch_date: 2025-10-06T20:10:15.646386
---

# DeepSeek AI数据库泄露：超百万条日志和密钥曝光

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

DeepSeek AI数据库泄露：超百万条日志和密钥曝光

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

DeepSeek AI数据库泄露：超百万条日志和密钥曝光

2025-01-30 15:39:00

所属地 上海

![image](https://image.3001.net/images/20250130/1738238577405411_498d31c15b804fec87a80e5dce97a1d2.png!small)

近日，备受瞩目的中国人工智能初创公司深度搜索（DeepSeek）因数据库暴露在互联网上而引发关注，此举可能导致恶意攻击者获取敏感数据。据Wiz安全研究员Gal Nagli透露，暴露的ClickHouse数据库“允许对数据库操作进行全面控制，包括访问内部数据的能力”。

此次泄露事件涉及超过一百万条日志流，包含聊天记录、密钥、后端细节以及其他高度敏感信息，如API密钥和操作元数据。在云安全公司尝试联系后，深度搜索已修复了该安全漏洞。

## 数据库暴露的严重性

该数据库托管在`oauth2callback.deepseek[.]com:9000`和`dev.deepseek[.]com:9000`，据称允许未经授权的访问者获取大量信息。Wiz指出，此次暴露使得攻击者可以在无需任何身份验证的情况下，完全控制数据库并可能在深度搜索环境中进行权限提升。

攻击者利用ClickHouse的HTTP接口，通过浏览器直接执行任意SQL查询。目前尚不清楚是否有其他恶意行为者趁机访问或下载了数据。

## AI服务快速发展的安全隐忧

Nagli在一份声明中表示：“AI服务的快速普及，若缺乏相应的安全措施，本质上存在风险。尽管AI安全的关注点大多集中在未来威胁上，但真正的危险往往来自基本风险——比如数据库的意外外部暴露。”

他进一步强调：“保护客户数据必须成为安全团队的首要任务，安全团队与AI工程师密切合作以保护数据并防止泄露至关重要。”

![image](https://image.3001.net/images/20250130/1738238578856361_12700c6ce999443bb140d4a703b1ea63.png!small)

![image](https://image.3001.net/images/20250130/1738238579689870_2dc98f69ec2b4d789545184112d46bea.png!small)

## 深度搜索的崛起与挑战

深度搜索因其突破性的开源模型而成为AI领域的热门话题，这些模型声称可以与OpenAI等领先的AI系统相媲美，同时具有高效和成本效益。其推理模型R1被誉为“AI的斯普特尼克时刻”。

尽管深度搜索的AI聊天机器人在多个市场的Android和iOS应用商店中迅速登顶，但它也成为“大规模恶意攻击”的目标，导致公司暂时暂停了注册。

在2025年1月29日发布的更新中，公司表示已发现问题并正在努力修复。与此同时，深度搜索的隐私政策也受到审查，其与中国的关系更成为美国国家安全关注的焦点。

## 国际监管与争议

此外，深度搜索的应用程序在意大利数据保护监管机构要求提供其数据处理实践和训练数据来源的信息后不久便无法使用。目前尚不清楚应用程序的下架是否是对监管机构问题的回应。

彭博社、金融时报和华尔街日报还报道称，OpenAI和微软正在调查深度搜索是否未经许可使用OpenAI的应用程序编程接口（API）来训练其模型，这种方法被称为“蒸馏”。OpenAI的一位发言人告诉《卫报》：“我们知道[中国]的一些团体正在积极使用包括蒸馏在内的方法，试图复制美国先进的AI模型。”

**参考来源：**

> [DeepSeek AI Database Exposed: Over 1 Million Log Lines, Secret Keys Leaked](https://thehackernews.com/2025/01/deepseek-ai-database-exposed-over-1.html)

# 数据安全

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

数据库暴露的严重性

AI服务快速发展的安全隐忧

深度搜索的崛起与挑战

国际监管与争议

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