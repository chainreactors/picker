---
title: 水木羽林与ClickHouse达成合作，WINGFUZZ模糊测试护航数据库安全
url: https://www.freebuf.com/news/375467.html
source: FreeBuf网络安全行业门户
date: 2023-08-20
fetch_date: 2025-10-04T11:59:52.989112
---

# 水木羽林与ClickHouse达成合作，WINGFUZZ模糊测试护航数据库安全

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

水木羽林与ClickHouse达成合作，WINGFUZZ模糊测试护航数据库安全

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

水木羽林与ClickHouse达成合作，WINGFUZZ模糊测试护航数据库安全

2023-08-19 08:17:52

所属地 上海

系统稳定性始终是数据库厂商的核心关注点，而安全是数据库稳定运行的基础。作为国际头部厂商，ClickHouse持续在全球范围寻找可满足稳定性要求的安全保障技术。

近期，水木羽林WINGFUZZ数据库模糊测试系统已经在ClickHouse完成落地，实现了模糊测试DevSecOps集成，协助ClickHouse团队在产品高速迭代过程中发现并修复了大量可导致系统崩溃的严重缺陷，得到了团队的高度认可。

此次合作与测试的更多内容已经发布在ClickHouse官网的技术Blog（如下图所示），点击<https://ClickHouse.com/blog/fuzzing-wingfuzz>即可查看。![](https://image.3001.net/images/20230819/1692404169_64e009c92f66e27041960.png!small)

## ****WINGFUZZ X ClickHouse****

ClickHouse公司一直关注数据库模糊测试技术的发展，其研发、测试和安全团队不仅熟悉相关开源模糊测试工具，也在以高标准、高要求的态度对于专业的数据库模糊测试技术供应商，在其Blog中也介绍了团队内部的模糊测试工作探索。

在与水木羽林建立合作之后，WINGFUZZ模糊测试产品顺利集成到了ClickHouse的日常测试中，成为其研发、测试和安全团队中必不可少的的重要工具。

Blog中写道：“随着 ClickHouse 的发展速度，随着我们的不断前进和新功能的构建，模糊测试在确保我们产品的稳定性和安全性方面发挥着至关重要的作用。”

相对于传统数据库，ClickHouse对于水木羽林团队而言是一个较新的对象。而WINGFUZZ 方案的快速适配能力，也给ClickHouse团队留下深刻印象：

“即使在我们大量的测试文件夹中有如此多的测试查询，WINGFUZZ 团队依然能够快速调整他们独一无二的方法并开始对 ClickHouse 进行模糊测试。”

在应用过程中，WINGFUZZ系统体现了强大的缺陷发现能力，部分缺陷直接被提交为Github issue。同时，ClickHouse团队也十分重视模糊测试所发现的缺陷，针对发现的问题会及时着手解决：

“WINGFUZZ 团队在过去几个月已经报告了大量数据库错误，并于近期报告了另一份包含 8 个独特发现的列表。一旦这些问题作为 GitHub 问题发布，我们的核心工程团队就会立即解决。”![](https://image.3001.net/images/20230819/1692404215_64e009f7d5e45d01e429f.png!small)

后续，水木羽林将继续加深与ClickHouse的合作，探索在集群中开展持续并行模糊测试的落地，这一部分的工作也将在Blog的Part 2中继续介绍。

## WINGFUZZ数据库模糊测试

WINGFUZZ数据库模糊测试系统可以对关系型数据库、分析型数据库、时序数据库进行模糊测试，挖掘系统稳定性、安全性相关问题。系统可支持黑盒与灰盒场景下的覆盖率引导模糊测试，并可自动适配目标数据库SQL语法，高效开展测试。当前，数据库测试系统已面向开源数据库挖掘近百个CVE漏洞，涵盖崩溃挂库、内存异常、逻辑错误等众多类型，并在众多国内、国际数据库厂商实现商业落地应用。![](https://image.3001.net/images/20230819/1692404239_64e00a0f63db77d48cf81.png!small)

WINGFUZZ数据库模糊测试系统利用了团队自研的多种核心优化技术，如在Blog中介绍的基于元数据的语法无关的变异生成，以及基于类型亲和性的查询序列生成技术等，可以协助生成语义正确且类型丰富的SQL序列。基于这些前沿技术，WINGFUZZ系统可以帮助数据库研发团队、安全研究团队有效提升工作效率，保障系统质量安全。

## ****关于 ClickHouse****

ClickHouse是领先的分析型数据库厂商，采用开源+SaaS服务的商业模式，2021年估值达到20亿美元。ClickHouse创新性地使用自定义的二进制列存储格式，用于以最高效率存储和索引大量数据，是一种高效、高性能和高可扩展性的数据分析工具。ClickHouse数据库的性能大幅超越了很多商业 MPP 数据库软件，相比传统的数据库软件要快 10-1000倍。![](https://image.3001.net/images/20230819/1692404260_64e00a240fd36262470fd.png!small)

ClickHouse适用于各种类型的数据分析，包括实时和流数据分析、数据仓库、商业智能和在线事务处理。当前，ClickHouse已经被广泛应用于中国电信、腾讯、Uber、ebay、CloudFlare、迪士尼等众多国内外技术企业，提供高速度高扩展的数据处理支持。

## 关于水木羽林

水木羽林是软件质量与安全测试领域创新企业，核心创始团队毕业于清华大学，在软件安全与分析领域积累深厚，在应用、协议、数据库、浏览器和操作系统上累计挖掘的数百个高危安全漏洞收录到国家信息安全漏洞库，相关工作也被谷歌、微软等测试平台集成应用。水木羽林已在航天五院嵌入式操作系统、统信桌面操作系统、腾讯云数据库、南大通用数据库、中船舰船控制系统等基础软件质量与安全保障上发挥了重要作用。

# 系统安全 # 网络安全技术

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

WINGFUZZ X ClickHouse

WINGFUZZ数据库模糊测试

关于 ClickHouse

关于水木羽林

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