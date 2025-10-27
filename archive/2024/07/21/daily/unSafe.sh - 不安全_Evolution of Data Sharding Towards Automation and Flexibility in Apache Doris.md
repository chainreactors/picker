---
title: Evolution of Data Sharding Towards Automation and Flexibility in Apache Doris
url: https://buaq.net/go-251617.html
source: unSafe.sh - 不安全
date: 2024-07-21
fetch_date: 2025-10-06T17:39:16.469289
---

# Evolution of Data Sharding Towards Automation and Flexibility in Apache Doris

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

![](https://8aqnet.cdn.bcebos.com/0b52e5d07214c260dffbb2fe041f8576.jpg)

Evolution of Data Sharding Towards Automation and Flexibility in Apache Doris

To handle large datasets, distributed databases introduce strategies like partitioning and bucketing
*2024-7-20 22:0:22
Author: [hackernoon.com(查看原文)](/jump-251617.htm)
阅读量:11
收藏*

---

To handle large datasets, distributed databases introduce strategies like partitioning and bucketing. Data is divided into smaller units based on specific rules and distributed across different nodes so databases can perform parallel processing for higher performance and data management flexibility.

Like in many databases, [Apache Doris](https://doris.apache.org/?ref=hackernoon.com) shards data into partitions, and then a partition is further divided into buckets. **Partitions** are typically defined by time or other continuous values. This allows query engines to quickly locate the target data during queries by pruning irrelevant data ranges.

**Bucketing**, on the other hand, distributes data based on the hash values of one or more columns, which prevents data skew.

Prior to version [2.1.0](https://doris.apache.org/blog/release-note-2.1.0?ref=hackernoon.com), there were two ways you could create data partitions in Apache Doris:

* **[Manual Partition](https://doris.apache.org/docs/table-design/data-partition/?ref=hackernoon.com#manual-partitioning)**: Users specify the partitions in the table creation statement or modify them through DDL statements afterwards.
* **[Dynamic Partition](https://doris.apache.org/docs/table-design/data-partition/?ref=hackernoon.com#dynamic-partition)**: The system automatically maintains partitions within a pre-defined range based on the data ingestion time.

In Apache Doris 2.1.0, we have introduced **[Auto Partition](https://doris.apache.org/docs/table-design/data-partition/?ref=hackernoon.com#auto-partition)**. It supports partitioning data by RANGE or by LIST and further enhances flexibility on top of automatic partitioning.

## Evolution of partitioning strategies in Doris

In the design of data distribution, we focus more on partition planning because the choice of partition columns and partition intervals heavily depends on the actual data distribution patterns, and a good partition design can largely improve the query and storage efficiency of the table.

In Doris, the data table is divided into partitions and then buckets in a hierarchical manner. The data within the same bucket then forms a data **tablet**, which is the minimum physical storage unit in Doris for data replication, inter-cluster data scheduling, and load balancing.

![](https://hackernoon.imgix.net/images/oNIroQpI1FZj2l5g1MSUvunDFzu2-ap83edp.jpeg?auto=format&fit=max&w=3840)

### Manual Partition

Doris allows users to manually create data partitions by RANGE and by LIST.

For time-stamped data like logs and transaction records, users typically create partitions based on the time dimension. Here's an example of the CREATE TABLE statement:

```
CREATE TABLE IF NOT EXISTS example_range_tbl
(
    `user_id` LARGEINT NOT NULL COMMENT "User ID",
    `date` DATE NOT NULL COMMENT "Data import date",
    `timestamp` DATETIME NOT NULL COMMENT "Data import timestamp",
    `city` VARCHAR(20) COMMENT "Location of user",
    `age` SMALLINT COMMENT "Age of user",
    `sex` TINYINT COMMENT "Sex of user",
    `last_visit_date` DATETIME REPLACE DEFAULT "1970-01-01 00:00:00" COMMENT "Last visit date of user",
    `cost` BIGINT SUM DEFAULT "0" COMMENT "User consumption",
    `max_dwell_time` INT MAX DEFAULT "0" COMMENT "Maximum dwell time of user",
    `min_dwell_time` INT MIN DEFAULT "99999" COMMENT "Minimum dwell time of user"
)
ENGINE=OLAP
AGGREGATE KEY(`user_id`, `date`, `timestamp`, `city`, `age`, `sex`)
PARTITION BY RANGE(`date`)
(
    PARTITION `p201701` VALUES LESS THAN ("2017-02-01"),
    PARTITION `p201702` VALUES LESS THAN ("2017-03-01"),
    PARTITION `p201703` VALUES LESS THAN ("2017-04-01"),
    PARTITION `p2018` VALUES [("2018-01-01"), ("2019-01-01"))
)
DISTRIBUTED BY HASH(`user_id`) BUCKETS 16
PROPERTIES
(
    "replication_num" = "1"
);
```

The table is partitioned by the data import date `date`, and 4 partitions have been pre-created. Within each partition, the data is further divided into 16 buckets based on the hash value of the `user_id`.

With this partitioning and bucketing design, when querying data from 2018 onwards, the system only needs to scan the `p2018` partition. This is what the query SQL looks like:

```
mysql> desc select count() from example_range_tbl where date >= '20180101';
+--------------------------------------------------------------------------------------+
| Explain String(Nereids Planner)                                                      |
+--------------------------------------------------------------------------------------+
| PLAN FRAGMENT 0                                                                      |
|   OUTPUT EXPRS:                                                                      |
|     count(*)[#11]                                                                    |
|   PARTITION: UNPARTITIONED                                                           |
|                                                                                      |
|    ......                                                                            |
|                                                                                      |
|   0:VOlapScanNode(193)                                                               |
|      TABLE: test.example_range_tbl(example_range_tbl), PREAGGREGATION: OFF.          |
|      PREDICATES: (date[#1] >= '2018-01-01')                                          |
|      partitions=1/4 (p2018), tablets=16/16, tabletList=561490,561492,561494 ...      |
|      cardinality=0, avgRowSize=0.0, numNodes=1                                       |
|      pushAggOp=NONE                                                                  |
|                                                                                      |
+--------------------------------------------------------------------------------------+
```

If the data is distributed unevenly across partitions, the hash-based bucketing mechanism can further divide the data based on the `user_id`. This helps to avoid load imbalance on some machines during querying and storage.

However, in real-world business scenarios, one cluster may have tens of thousands of tables, which means it is impossible to manage them manually.

```
CREATE TABLE `DAILY_TRADE_VALUE`
(
    `TRADE_DATE`              datev2 NOT NULL COMMENT 'Trade date',
    `TRADE_ID`                varchar(40) NOT NULL COMMENT 'Trade ID',
    ......
)
UNIQUE KEY(`TRADE_DATE`, `TRADE_ID`)
PARTITION BY RANGE(`TRADE_DATE`)
(
    PARTITION p_200001 VALUES [('2000-01-01'), ('2000-02-01')),
    PARTITION p_200002 VALUES [('2000-02-01'), ('2000-03-01')),
    PARTITION p_200003 VALUES [('2000-03-01'), ('2000-04-01')),
    PARTITION p_200004 VALUES [('2000-04-01'), ('2000-05-01')),
    PARTITION p_200005 VALUES [('2000-05-01'), ('2000-06-01')),
    PARTITION p_200006 VALUES [('2000-06-01'), ('2000-07-01')),
    PARTITION p_200007 VALUES [('2000-07-01'), ('2000-08-01')),
    PARTITION p_200008 VALUES [('2000-08-01'), ('2000-09-01')),
    PARTITION p_200009 VALUES [('2000-09-01'), ('2000-10-01')),
    PARTITION p_200010 VALUES [('2000-10-01'), ('2000-11-01')),
    PARTITION p_200011 VALUES [('2000-11-01'), ('2000-12-01')),
    PARTITION p_200012 VALUES [('2000-12-01'), ('2001-01-01')),
    PARTITION p_200101 ...