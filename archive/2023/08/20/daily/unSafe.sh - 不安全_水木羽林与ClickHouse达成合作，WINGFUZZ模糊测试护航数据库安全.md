---
title: 水木羽林与ClickHouse达成合作，WINGFUZZ模糊测试护航数据库安全
url: https://buaq.net/go-174836.html
source: unSafe.sh - 不安全
date: 2023-08-20
fetch_date: 2025-10-04T11:58:53.625641
---

# 水木羽林与ClickHouse达成合作，WINGFUZZ模糊测试护航数据库安全

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

![](https://8aqnet.cdn.bcebos.com/58489bc90c4e5bff5ef6e4f8a8bafaae.jpg)

水木羽林与ClickHouse达成合作，WINGFUZZ模糊测试护航数据库安全

主站 分类 漏洞 工具 极客
*2023-8-19 08:17:52
Author: [www.freebuf.com(查看原文)](/jump-174836.htm)
阅读量:20
收藏*

---

[![freeBuf](https://www.freebuf.com/images/logoMax.png)](https://www.freebuf.com/)

主站

分类

漏洞

工具

极客

Web安全

系统安全

网络安全

无线安全

设备/客户端安全

数据安全

安全管理

企业安全

工控安全

特色

头条

人物志

活动

视频

观点

招聘

报告

资讯

区块链安全

标准与合规

容器安全

公开课

![](https://www.freebuf.com/freebuf/img/7aa3bf7.svg) ![](https://www.freebuf.com/freebuf/img/181d733.svg)

官方公众号企业安全新浪微博

![](https://www.freebuf.com/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](https://www.freebuf.com/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

* [资讯](https://www.freebuf.com/news)

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

文章来源: https://www.freebuf.com/news/375467.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)