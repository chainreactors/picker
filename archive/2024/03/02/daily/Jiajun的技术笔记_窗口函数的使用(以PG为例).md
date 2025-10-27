---
title: 窗口函数的使用(以PG为例)
url: https://jiajunhuang.com/articles/2024_03_01-pg_window_function.md.html
source: Jiajun的技术笔记
date: 2024-03-02
fetch_date: 2025-10-04T12:09:58.770863
---

# 窗口函数的使用(以PG为例)

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

* [窗口函数的使用(以PG为例)](#%25E7%25AA%2597%25E5%258F%25A3%25E5%2587%25BD%25E6%2595%25B0%25E7%259A%2584%25E4%25BD%25BF%25E7%2594%25A8%2528%25E4%25BB%25A5PG%25E4%25B8%25BA%25E4%25BE%258B%2529)

# 窗口函数的使用(以PG为例)

很少做数据统计，之前一直没有接触和使用窗口函数。今天看了一下文档，发现在统计领域，窗口函数非常强大，当然，缺点就是把计算量
移到了数据库这一层，但是没关系，对于少量数据，直接一条SQL解决，cool！

在 SQL 中，窗口函数是一种特殊类型的函数，可以在一组相关的行（称为”窗口”）上执行计算。窗口函数可以解决很多数据统计的功能，
例如包括计算移动平均、总计、累计和排名等。

首先我们看下语法：

```
SELECT depname, empno, salary, avg(salary) OVER (PARTITION BY depname) FROM empsalary;
```

它的主要特点，就是有一个 `OVER` 子句，子句里一般会包含 `PARTITION BY` 语句，当然也可以不包含。我们来建一个表，并且插入一些
数据：

```
postgres=# create table empsalary(depname text, empno int, salary float);
CREATE TABLE
postgres=# insert into empsalary(depname, empno, salary) values ('develop', 11, '5200');
INSERT 0 1
postgres=# insert into empsalary(depname, empno, salary) values ('develop', 7, '4200');
INSERT 0 1
postgres=# insert into empsalary(depname, empno, salary) values ('develop', 9, '4500');
INSERT 0 1
postgres=# insert into empsalary(depname, empno, salary) values ('develop', 8, '6000');
INSERT 0 1
postgres=# insert into empsalary(depname, empno, salary) values ('develop', 10, '5200');
INSERT 0 1
postgres=# insert into empsalary(depname, empno, salary) values ('personnel', 5, '3500');
INSERT 0 1
postgres=# insert into empsalary(depname, empno, salary) values ('personnel', 2, '3900');
INSERT 0 1
postgres=# insert into empsalary(depname, empno, salary) values ('personnel', 3, '4800');
INSERT 0 1
postgres=# insert into empsalary(depname, empno, salary) values ('sales', 1, '5000');
INSERT 0 1
postgres=# insert into empsalary(depname, empno, salary) values ('sales', 4, '4800');
INSERT 0 1
```

然后执行上述SQL：

```
postgres=# SELECT depname, empno, salary, avg(salary) OVER (PARTITION BY depname) FROM empsalary;
  depname  | empno | salary |        avg
-----------+-------+--------+--------------------
 develop   |    11 |   5200 |               5020
 develop   |     7 |   4200 |               5020
 develop   |     9 |   4500 |               5020
 develop   |     8 |   6000 |               5020
 develop   |    10 |   5200 |               5020
 personnel |     5 |   3500 | 4066.6666666666665
 personnel |     2 |   3900 | 4066.6666666666665
 personnel |     3 |   4800 | 4066.6666666666665
 sales     |     1 |   5000 |               4900
 sales     |     4 |   4800 |               4900
(10 rows)
```

可以看到，输出中，前三列是数据库里原来的数据，第四列是 avg(salary)，整个数据已经按 `depname` 分区，然后区域内再计算avg。

再看一个例子：

```
postgres=# SELECT depname, empno, salary,
       rank() OVER (PARTITION BY depname ORDER BY salary DESC)
FROM empsalary;
  depname  | empno | salary | rank
-----------+-------+--------+------
 develop   |     8 |   6000 |    1
 develop   |    10 |   5200 |    2
 develop   |    11 |   5200 |    2
 develop   |     9 |   4500 |    4
 develop   |     7 |   4200 |    5
 personnel |     3 |   4800 |    1
 personnel |     2 |   3900 |    2
 personnel |     5 |   3500 |    3
 sales     |     1 |   5000 |    1
 sales     |     4 |   4800 |    2
(10 rows)
```

可以看到，输出仍然是按 `depname` 分区，然后区域内进行排名。

再来看一个例子：

```
postgres=# SELECT salary, sum(salary) OVER () FROM empsalary;
 salary |  sum
--------+-------
   5200 | 47100
   4200 | 47100
   4500 | 47100
   6000 | 47100
   5200 | 47100
   3500 | 47100
   3900 | 47100
   4800 | 47100
   5000 | 47100
   4800 | 47100
(10 rows)
```

这个例子里，`OVER()` 里没有子句，因此是对全局产生作用，整个作为一个窗口，然后计算 `sum(salary)`。

通过这三个简单的例子，可以一窥窗口函数的强大，一些常规的计算和统计任务，可以一条SQL直接解决，例如年级成绩排名，按科目排名等等。

---

Refs:

* <https://www.postgresql.org/docs/current/tutorial-window.html>

---

##### 相关文章

* [容器时代的日志处理](/articles/2018_04_12-docker_logging.md.html)
* [Golang和Thrift](/articles/2018_04_10-golang_thrift.md.html)
* [折腾Kubernetes](/articles/2018_04_05-kubernetes.md.html)
* [协程(coroutine)简介 - 什么是协程？](/articles/2018_04_03-coroutine.md.html)
* [goroutine 切换的时候发生了什么？](/articles/2018_03_29-goroutine_schedule.md.html)
* [Prometheus 数据类型](/articles/2018_03_19-prometheus.md.html)
* [Gin源码阅读与分析](/articles/2018_03_16-gin_source_code.md.html)
* [如何面试-作为面试官得到的经验](/articles/2018_03_10-interview.md.html)
* [自己写一个容器](/articles/2018_03_09-write_you_a_container.md.html)
* [Golang(Go语言)中实现典型的fork调用](/articles/2018_03_08-golang_fork.md.html)
* [软件开发之禅---大事化小，各个击破](/articles/2018_02_26-zen_of_dev.md.html)
* [程序员的自我修养：链接，装载与库 阅读笔记](/articles/2018_02_25-linker_loader.md.html)
* [Redis源码阅读与分析三：哈希表](/articles/2018_02_24-redis_source_code_hash_table.md.html)
* [Redis源码阅读与分析二：双链表](/articles/2018_02_24-redis_source_code_doubly_linked_list.md.html)
* [Redis源码阅读与分析一：sds](/articles/2018_02_24-redis_source_code_sds.md.html)

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