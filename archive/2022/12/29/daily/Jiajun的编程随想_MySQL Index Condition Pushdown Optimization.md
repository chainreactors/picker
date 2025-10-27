---
title: MySQL Index Condition Pushdown Optimization
url: https://jiajunhuang.com/articles/2022_12_28-index_condition_pushdown_optimization.md.html
source: Jiajun的编程随想
date: 2022-12-29
fetch_date: 2025-10-04T02:38:39.895676
---

# MySQL Index Condition Pushdown Optimization

[Jiajun的技术笔记](/)

搜索

* [EN](https://blog.jiajunhuang.com)
* [归档](/archive)
* [分享](/sharing)
* [随想](/notes)
* [友链](/friends)
* 工具

  [面试题库](https://tiku.jiajunhuang.com)
  [幻灯片](https://jiajunhuang.com/page/index.md)
* [关于](/aboutme)

目录

* [MySQL Index Condition Pushdown Optimization](#MySQL%2bIndex%2bCondition%2bPushdown%2bOptimization)

# MySQL Index Condition Pushdown Optimization

比如数据库中有如下表:

```
show create table people\G
*************************** 1. row ***************************
       Table: people
Create Table: CREATE TABLE `people` (
  `zipcode` varchar(16) NOT NULL,
  `lastname` varchar(32) NOT NULL,
  `address` varchar(32) NOT NULL,
  KEY `idx_people_zipcode_lastname_address` (`zipcode`,`lastname`,`address`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
1 row in set (0.001 sec)
```

我们执行如下查询：

```
SELECT * FROM people
  WHERE zipcode='95054'
  AND lastname LIKE '%etrunia%'
  AND address LIKE '%Main Street%';
```

如果没有 index condition pushdown optimization 的话，那么执行步骤如下：

1. 对比 `idx_people_zipcode_lastname_address` 索引中 `zipcode` 是否能匹配，如果可以匹配，获取整个数据行；
2. 对比 `WHERE` 中的条件，看是否可以全部匹配；

而有了 index condition pushdown optimization 之后，步骤则变成了：

1. 对比 `idx_people_zipcode_lastname_address` 索引中的 `zipcode` 是否能匹配，同时对比 `WHERE` 语句中，index中包含的部分，看是否可以通过；
2. 如果可以通过，获取整个数据行；
3. 对比 `WHERE` 中的条件，看是否可以全部匹配；

这两者的区别就在于，是否充分利用了索引中的值，提前进行了数据的过滤。我们在 `EXPLAIN` 的时候，如果当前数据库查询使用了这项优化，则会在 `Extra`
那一列显示 `Using index condition`。

---

ref:

* <https://dev.mysql.com/doc/refman/5.7/en/index-condition-pushdown-optimization.html>

---

##### 相关文章

* [Python字符串格式化](/articles/2017_04_16-python_string_format.md.html)
* [Gunicorn 简明教程](/articles/2017_04_08-gunicorn.md.html)
* [Raft 论文阅读笔记](/articles/2017_03_29-raft.md.html)
* [什么是 Golang Comparable Types](/articles/2017_03_06-golang_comparable_types.md.html)
* [GFS 论文阅读](/articles/2017_03_02-gfs.md.html)
* [MapReduce 论文阅读](/articles/2017_03_02-map_reduce.md.html)
* [一起来做贼：Goroutine原理和Work stealing](/articles/2017_02_24-goroutine_and_work_stealing.md.html)
* [Go语言的defer, panic和recover](/articles/2017_02_15-go_defer_panic_and_recover.md.html)
* [再读vim help：vim小技巧](/articles/2017_01_24-vim_manual.md.html)
* [再读 Python Language Reference](/articles/2017_01_24-python_language_reference.md.html)
* [设计模式（2）- 深入浅出设计模式 阅读笔记](/articles/2017_01_22-head_first_design_patterns_2.md.html)
* [设计模式（1）- 深入浅出设计模式 阅读笔记](/articles/2017_01_21-head_first_design_patterns.md.html)
* [Cython! Python和C两个世界的交叉点](/articles/2017_01_15-cython_rocks.md.html)
* [socketserver 源码阅读与分析](/articles/2017_01_09-socketserver_source_code.md.html)
* [functools 源码阅读与分析](/articles/2017_01_08-functools_source_code.md.html)

---

加载评论

* [![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%202.svg)](https://www.digitalocean.com/?refcode=dedfc09c3066&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)
* [![](/static/email.png)
  邮件 订阅](https://eepurl.com/guVPMj)
* [![](/static/rss.png)
  RSS 订阅](/rss)
* [![](/static/web.png)
  Web开发简介系列](/articles/2017_10_19-web_dev_series.md.html)
* [![](/static/computer.png)
  数据结构的实际使用](/tutorial/data_structure/index.md)
* [![](/static/golang.png)
  Golang 简明教程](/tutorial/golang/index.md)
* [![](/static/python.png)
  Python 教程](/tutorial/python/index.md)

本站热门

* [socks5 协议详解](/articles/2019_06_06-socks5.md.html)
* [zerotier简明教程](/articles/2019_09_11-zerotier.md.html)
* [搞定面试中的系统设计题](/articles/2019_04_29-system_design.md.html)
* [frp 源码阅读与分析(一)：流程和概念](/articles/2019_06_11-frpc_source_code_part1.md.html)
* [用peewee代替SQLAlchemy](/articles/2020_05_29-use_peewee.md.html)
* [Golang(Go语言)中实现典型的fork调用](/articles/2018_03_08-golang_fork.md.html)
* [DNSCrypt简明教程](/articles/2019_10_31-dnscrypt.md.html)
* [一个Gunicorn worker数量引发的血案](/articles/2020_03_11-gunicorn_worker.md.html)
* [Golang validator使用教程](/articles/2020_04_10-golang_validator.md.html)
* [Docker组件介绍（二）：shim, docker-init和docker-proxy](/articles/2018_12_24-docker_components_part2.md.html)
* [Docker组件介绍（一）：runc和containerd](/articles/2018_12_22-docker_components.md.html)
* [使用Go语言实现一个异步任务框架](/articles/2020_04_24-gotasks.md.html)
* [协程(coroutine)简介 - 什么是协程？](/articles/2018_04_03-coroutine.md.html)
* [SQLAlchemy简明教程](/articles/2019_10_30-sqlalchemy.md.html)
* [Golang的template(模板引擎)简明教程](/articles/2019_08_23-golang_html_template.md.html)

[@jiajunhuang](https://github.com/jiajunhuang) 2015-2024, All Rights Reserved。本站禁止转载，引用请注明作者与原链。