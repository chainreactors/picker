---
title: 2022 43 Open source weekly report
url: https://cloudsjhan.github.io/2022/10/21/2022-43-Open-source-weekly-report/
source: cloud world
date: 2022-10-22
fetch_date: 2025-10-03T20:36:04.080154
---

# 2022 43 Open source weekly report

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## 2022 43 Open source weekly report

posted

2022-10-21

|

in

[weekly-report](/categories/weekly-report/)

|

visitors:

|

|

wordcount:

704
|

min2read ≈

3

2022 NO.40 weekly report

![](https://)

## Go driver SDK for databend cloud released!

由于在 databend cloud 各个项目的代码中已经充斥着大量重复的请求 databend-query 的代码，所以亟需一个 driver SDK 来实现大一统，于是在几周前就开始着手实现 databend cloud 的 go driver，当时用比较短的时间大概实现了一个架子，详情可以见 [这篇文章](https://cloudsjhan.github.io/2022/09/02/2022-36-Open-source-weekly-report/)。碍于中间有几个优先级比较高的工作就暂时搁置了，本周 all in 这个项目一周，终于 release 了 [v0.0.1 版本](https://github.com/databendcloud/databend-go)，虽然代码的结构、功能的丰富程度、代码的优雅程度都跟标杆 SDK - [clickhouse-go](https://github.com/ClickHouse/clickhouse-go) 的水平有较大差距，但基本的方法比如 `sql.Open`, `Exec`, `Query`, `Next`, `Rows` 等都已经可用。先来看几个🌰吧!

### Execution

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` | ```   dsn, cfg, err := getDSN()   if err != nil {   log.Fatalf("failed to create DSN from Config: %v, err: %v", cfg, err)       } conn, err := sql.Open("databend", dsn)   if err != nil {       return err    }   conn.Exec(`DROP TABLE IF EXISTS data`)   _, err = conn.Exec(`   CREATE TABLE IF NOT EXISTS  data(       Col1 UInt8,       Col2 String   )    `)   if err != nil {       return err   }   _, err = conn.Exec("INSERT INTO data VALUES (1, 'test-1')") ``` |

### Query Row

可以用 `Scan` 方法来解析出单条数据

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` row := conn.QueryRow("SELECT * FROM data") var (     col1             uint8     col2, col3, col4 string     col5            []string     col6             time.Time ) if err := row.Scan(&col1, &col2, &col3, &col4, &col5, &col6); err != nil {     return err } ``` |

### Query Rows

当然可以用 `Next` 来不断迭代获取所有数据

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` row := conn.QueryRow("SELECT * FROM data") var (     col1             uint8     col2, col3, col4 string     col5            []string     col6             time.Time ) for rows.Next() {     if err := row.Scan(&col1, &col2, &col3, &col4, &col5, &col6); err != nil {     return err     }     fmt.Printf("row: col1=%d, col2=%s, col3=%s, col4=%s, col5=%v, col6=%v\n", col1, col2, col3, col4, col5, col6) } ``` |

这样在请求 databend-query 的时候，就不用再每次都写一遍 http 请求/解析的代码啦。

## bendsql 尝鲜 go driver

Go driver release 后马上就迎来了第一个用户(小白鼠) - [bendsql](https://github.com/databendcloud/bendsql)。bendsql 中有个命令用来执行 SQL 语句， `bendsql query "select * from table"`，所以我先将这里面请求 databend-query 的代码都换成了 go driver - `https://github.com/databendcloud/bendsql/pull/22`，可以看到删掉了不少代码，清晰了不少。接下来要在其他项目中去检验了。

来看看效果：
![](https://tva1.sinaimg.cn/large/005UfcOkly8h7d6u4upl3j31gq0fuwfq.jpg)

## kruise-tools

本周 `kubectl-kruise` 插件迎来了一次[更新](https://github.com/openkruise/kruise-tools/releases/tag/v1.0.5)，包含了两个 bug-fix 和新的 feature:

🐛 Bug fix:

* Fix rollout status of partitioned update <https://github.com/openkruise/kruise-tools/pull/68>
* Fix ads patch for rollout undo <https://github.com/openkruise/kruise-tools/pull/71>

🚀 Feat:

* Support kubectl-kruise create ContainerRecreateRequest <https://github.com/openkruise/kruise-tools/pull/66>
* Add resourcedistribution generator <https://github.com/openkruise/kruise-tools/pull/69>. Thanks @dong4325

  其中 resourcedistribution generator 是开源之夏的一个项目，主要是用来方便用户生成 resourceDistrubution 资源的，关于 [resouceDistribution](https://openkruise.io/docs/user-manuals/resourcedistribution) 和这个 generator 后面等功能稳定后再多做介绍。

好了，以上。

---

-------------The End-------------

Title:[2022 43 Open source weekly report](/2022/10/21/2022-43-Open-source-weekly-report/)

Author:[cloud sjhan](/ "visit cloud sjhan blog")

Publish Time:2022年10月21日 - 18:10

Last Update:2022年10月21日 - 20:10

Original Link:[https://cloudsjhan.github.io/2022/10/21/2022-43-Open-source-weekly-report/](/2022/10/21/2022-43-Open-source-weekly-report/ "2022 43 Open source weekly report")

License: [By-NC-ND 4.0 international](https://creativecommons.org/licenses/by-nc-nd/4.0/ "Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)")。

![cloud sjhan wechat](/images/wechat-qcode.jpg)

keep going, keep coding

donate

![cloud sjhan 微信支付](/images/wechatpay.jpg)

![cloud sjhan 支付宝](/images/alipay.jpg)

支付宝

[weekly-report](/tags/weekly-report/)

(>给这篇博客打个分吧<)

[2022-41 homebrew formula example for go](/2022/10/06/homebrew-formula-example-for-go/ "2022-41 homebrew formula example for go")

[2022 47 Open source weekly report](/2022/11/13/2022-47-Open-source-weekly-report/ "2022 47 Open source weekly report")

* Content
* Overview

![cloud sjhan](/images/avatar.png)

cloud sjhan

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

1. [1. Go driver SDK for databend cloud released!](#Go-driver-SDK-for-databend-cloud-released)
   1. [1.1. Execution](#Execution)
   2. [1.2. Query Row](#Query-Row)
   3. [1.3. Query Rows](#Query-Rows)
2. [2. bendsql 尝鲜 go driver](#bendsql-尝鲜-go-driver)
3. [3. kruise-tools](#kruise-tools)

© 2018 — 2025

cloud sjhan
|

Site words total count:
308.0k

stay hungry,stay foolish

Total Words:308.0k

0%

;