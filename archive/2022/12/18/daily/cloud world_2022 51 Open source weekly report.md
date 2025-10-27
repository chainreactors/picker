---
title: 2022 51 Open source weekly report
url: https://cloudsjhan.github.io/2022/12/17/2022-51-Open-source-weekly-report/
source: cloud world
date: 2022-12-18
fetch_date: 2025-10-04T01:51:30.609705
---

# 2022 51 Open source weekly report

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## 2022 51 Open source weekly report

posted

2022-12-17

|

in

[weekly-report](/categories/weekly-report/)

|

visitors:

|

|

wordcount:

1,122
|

min2read ≈

4

2022 NO.51 周报

![](https://)

距离上一次 weekly report 已经过去整整一个月，在 [databend-py](https://github.com/databendcloud/databend-py)、[databend-sqlalchemy](https://github.com/databendcloud/databend-sqlalchemy) 基本可用的前提下我开始着手在 [dbt](https://docs.getdbt.com/) 的生态中支持 databend cloud。dbt 提供了一种插件生态，我们可以开发专有的 adapter plugin 从而将 DBT 扩展到任何数据平台。dbt 算是在数据领域的新物种，在国内感觉用的还不是很多，但是在国外已经俨然成为现代数据领域的后起之秀。所以下面先抛砖引玉，简单介绍一下 dbt。

## What is dbt?

dbt 是一个非常强大和灵活的数据工具，它可以快速构建数据 pipe、基于 jinjia 模板以自动测试、构建和填充分析模型，包括文档的自动生成和开箱即用的数据血缘，非常适合自动化数仓的工作。其核心代码是一个开源 Python 库 - [dbt-core](https://github.com/dbt-labs/dbt-core) 。可以参考[这个项目](https://discourse.getdbt.com/t/how-we-set-up-our-computers-for-working-on-dbt-projects/243)快速上手体验一下。

需要强调的一点是 dbt 并不是传统的 ETL 工具，

![ETL](https://tva1.sinaimg.cn/large/008vxvgGgy1h973opa25sj30pw0bamxw.jpg)

它并不在系统之间传输或者加载数据，而是通过使用 SQL 和 YAML 来转换已经被加载到数仓中的数据。这种先加载后转换的概念，称为 ELT。

![ELT](https://tva1.sinaimg.cn/large/008vxvgGgy1h96n06kdcwj30qk0cg3zb.jpg)

在 ELT 的过程中，数据无须等待即可进入数仓，转换出现错误也不需要重新加载，能够提高效率并降低成本。下面我也会介绍一个 EL 的工具 - airbyte，看 airbyte + dbt 如何实现完美的 ELT 流程。关于 dbt 的介绍就到这里，想要深入了解的同学可以参考 dbt 官网和 dbt-core 的 github 主页。

## How to use dbt with Databend Cloud

经过几周与 dbt 的搏斗，支持 databend 的 dbt adapter 插件 [dbt-databend-cloud](https://github.com/databendcloud/dbt-databend) 终于能够跑通官方的 case 了✿✿ヽ(°▽°)ノ✿。开发的过程中也帮 databend 本身发现并解决了一些问题:

#### Issue

[Feature: support `a.*` in SQL](https://github.com/datafuselabs/databend/issues/8906)

[Feature: support `||` concat function in SQL](https://github.com/datafuselabs/databend/issues/8876)

[Feature: support SQL-style double-quoted identifier in get\_path](https://github.com/datafuselabs/databend/issues/9131)

#### PR

[fix: double-quote in get\_path](https://github.com/datafuselabs/databend/pull/9206)

期间也有跟 dbt 社区的讨论，非常感谢 dbt 社区的热心帮助:

#### Disscussion

[Field “path” of type Path in DatabendRelation has invalid value](https://github.com/dbt-labs/dbt-core/discussions/6276)

我们可以跟着这个 [wiki - How to use dbt with Databend Cloud](https://github.com/databendcloud/dbt-databend/wiki/How-to-use-dbt-with-Databend-Cloud) 体验一下 dbt 的强大能力，希望后面能顺利将 dbt-databend 加入到官方 dbt-adapters 的维护阵营当中去。

## What is airbyte?

上面我们介绍 ELT 的时候提到过 `airbyte`，这里再展开介绍一下。[Airbyte](https://airbytehq.github.io/) 是一个开源的云原生数据集成平台，可以让用户从各种来源提取、转换和加载数据到各种目标。

![airbyte](https://tva1.sinaimg.cn/large/008vxvgGgy1h972vmd7aqj318v0s9n14.jpg)

airbyte 的架构设计易于扩展，非常灵活，允许用户开发自定义的 source/destination connector ，并且可以很方便地加入到 airbyte 的平台里。这里我主要是开发了一个 destination connector，将 databend cloud 作为数据的目的入口，这样用户就可以很容易地从各个数据源，比如 S3, Clickhouse, Filebot ，甚至本地文件同步数据到 databend cloud，并且 airbyte 的 Normalization 能力结合 dbt 后能够将原始数据转换成完整表结构的数据表。

等这个 [PR](https://github.com/airbytehq/airbyte/pull/19815) 合并后就可以在 airbyte cloud 上使用 databend cloud 作为 data source 了。

## ClickVisual 支持 databend source

ClickVisual 是一个轻量级的由[石墨文档](https://shimo.im/)开源的日志查询、分析、报警的可视化平台，提供一站式应用可靠性的可视化的解决方案。既可以独立部署使用，也可作为插件集成到第三方系统。目前是市面上唯一一款支持 ClickHouse 的类 Kibana 的业务日志查询平台。之前 ClickVisual 只支持 Clickhouse 作为数据源来存储、查询日志，我添加了一些代码经过调试后现在也能支持 databend cloud 作为数据源。

[Feat: support databend source](https://github.com/clickvisual/clickvisual/pull/823)

[feat: support exist log table for databend](https://github.com/clickvisual/clickvisual/pull/835)

![](https://tva1.sinaimg.cn/large/008vxvgGgy1h972v1gxwjj30zk0js76o.jpg)

但是由于目前 databend 不支持类似 Clickhouse `status='200'` ( `status` 是 `int32` 类型) 这样的语法，所以字段过滤查询的功能需要等这个 [issue-836](https://github.com/clickvisual/clickvisual/issues/836) 解决后才能正常使用。

## Openkruise 遗留 PR

说起来真是非常惭愧，不仅已经很久没有参加 OpenKruise 的双周会了而且还遗留了一个陈年老 PR 没有完成，其实两周前 [zmberg](https://github.com/zmberg) 就联系我尽快处理一下这个问题，所以这周无论如何也要把这个 [PR](https://github.com/openkruise/kruise/pull/1028) 关掉 😭。

---

综上，希望 2022 的最后两周工作顺利🎉。

---

-------------The End-------------

Title:[2022 51 Open source weekly report](/2022/12/17/2022-51-Open-source-weekly-report/)

Author:[cloud sjhan](/ "visit cloud sjhan blog")

Publish Time:2022年12月17日 - 10:12

Last Update:2022年12月17日 - 21:12

Original Link:[https://cloudsjhan.github.io/2022/12/17/2022-51-Open-source-weekly-report/](/2022/12/17/2022-51-Open-source-weekly-report/ "2022 51 Open source weekly report")

License: [By-NC-ND 4.0 international](https://creativecommons.org/licenses/by-nc-nd/4.0/ "Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)")。

![cloud sjhan wechat](/images/wechat-qcode.jpg)

keep going, keep coding

donate

![cloud sjhan 微信支付](/images/wechatpay.jpg)

![cloud sjhan 支付宝](/images/alipay.jpg)

[weekly-report](/tags/weekly-report/)

(>给这篇博客打个分吧<)

[2022 47 Open source weekly report](/2022/11/13/2022-47-Open-source-weekly-report/ "2022 47 Open source weekly report")

[2023 12 Open Source weekly report](/2023/03/17/2023-12-Open-Source-weekly-report/ "2023 12 Open Source weekly report")

* Content
* Overview

![cloud sjhan](/images/avatar.png)

[166
日志](/archives/)

[40
分类](/categories/index.html)

[73
标签](/tags/index.html)

[RSS](/atom.xml)

[GitHub](https://github.com/hantmac "GitHub")

E-Mail

Links

* [CSDN](https://blog.csdn.net/u012421976 "CSDN")
* [w3school](http://www.w3school.com.cn/ "w3school")
* [快搜](http://search.chongbuluo.com/ "快搜")

1. [1. What is dbt?](#What-is-dbt)
2. [2. How to use dbt with Databend Cloud](#How-to-use-dbt-with-Databend-Cloud)
   1. [2.0.1. Issue](#Issue)
   2. [2.0.2. PR](#PR)
   3. [2.0.3. Disscussion](#Disscussion)

- [3. What is airbyte?](#What-is-airbyte)
- [4. ClickVisual 支持 databend source](#ClickVisual-支持-databend-source)
- [5. Openkruise 遗留 PR](#Openkruise-遗留-PR)

© 2018 — 2025

cloud sjhan
|

Site words total count:
308.0k

stay hungry,stay foolish

Total Words:308.0k

0%

;