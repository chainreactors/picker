---
title: MySQL 死锁日志分析方法
url: https://www.freebuf.com/news/414280.html
source: FreeBuf网络安全行业门户
date: 2024-11-02
fetch_date: 2025-10-06T19:16:58.922608
---

# MySQL 死锁日志分析方法

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

MySQL 死锁日志分析方法

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

MySQL 死锁日志分析方法

2024-11-01 15:36:05

所属地 北京

作者：京东物流 张凯

# 引言

MySQL 死锁是线上经常遇到的现象，但是死锁分析却并不总是件容易的事情，本文介绍 MySQL 死锁日志的分析方法，帮助研发从日志中快速提取有效信息，从而提高死锁原因分析的效率。

# 死锁介绍

## 触发条件

死锁的触发条件包括四个：

•互斥

•占有且等待

•不可抢占用

•循环等待

如下图所示，**两个事务加锁顺序不同导致死锁**。

![](https://image.3001.net/images/20200701/1593550745.png!small)

发生死锁后只需要破坏发生死锁四个条件中的任意一个条件就可以解除死锁状态。数据库层面有两种策略用于打破死锁状态：

•被动，设置事务等待锁的超时时间，事务锁等待超时后自动回滚。默认 50 秒；

•主动，开启主动死锁检测，检测到死锁后回滚其中一个事务。默认开启。

其中默认使用第二种策略，也就是检测到死锁后立即回滚，从而解除死锁状态。因此发生死锁时业务可能报错死锁，但不会报错锁等待超时。

## 死锁检测

innodb\_deadlock\_detect 参数用于控制是否开启死锁检测，该参数是 5.7.15 中引入。

```
mysql>select@@innodb_deadlock_detect;+--------------------------+|@@innodb_deadlock_detect|+--------------------------+|                        1|+--------------------------+1rowinset(0.00 sec)
```

死锁检测本质上是一个搜索问题，5.7 中使用深度优先算法实现，具体是判断锁等待关系图中是否有环。

高并发场景下可以考虑关闭死锁检测，原因是如果锁等待队列很长，死锁检测成本高，会导致实例性能下降。但是前提是应用层面可以避免死锁，因此通常不建议关闭。

下面通过介绍一个死锁案例对死锁日志的格式与分析方法有一个感性认识。

# 死锁案例

## 日志

```
------------------------LATEST DETECTED DEADLOCK------------------------2024-04-14 08:07:05 0x7fb6d39a6700*** (1) TRANSACTION:TRANSACTION 13020605130, ACTIVE 25 sec starting index readmysql tables in use 1, locked 1LOCK WAIT 33 lock struct(s), heap size 3520, 33 row lock(s), undo log entries 34MySQL thread id 2343498932, OS thread handle 140424015394560, query id 28769967039 x.x.x.x xwms_rw updatingUPDATE stock_occupySET update_time = NOW(),update_user = 'WAPS',qty_out_occupy=qty_out_occupy + 12.0000WHERE map_area_id = 608AND goods_no='EMG4418433215231'AND owner_no='0'AND lot_no='-1'AND product_level='100'         AND org_no = '10'AND distribute_no = '10'AND warehouse_no = '126'AND map_area_id = 608*** (1) WAITING FOR THIS LOCK TO BE GRANTED:RECORD LOCKS space id 127 page no 5255 n bits 272 index idx_map_goods_product_lot_owner of table `xwms`.`stock_occupy` trx id 13020605130 lock_mode X locks rec but not gap waitingRecord lock, heap no 53 PHYSICAL RECORD: n_fields 6; compact format; info bits 00: len 8; hex 8000000000000260; asc        `;;1: len 16; hex 454d4734343138343333323135323331; asc EMG4418433215231;;2: len 3; hex 313030; asc 100;;3: len 2; hex 2d31; asc -1;;4: len 1; hex 30; asc 0;;5: len 8; hex 8000000000042de4; asc       - ;;*** (2) TRANSACTION:TRANSACTION 13020606128, ACTIVE 10 sec starting index readmysql tables in use 1, locked 110 lock struct(s), heap size 1136, 7 row lock(s), undo log entries 8MySQL thread id 2343006037, OS thread handle 140423210886912, query id 28769967052 x.x.x.x xwms_rw updatingUPDATE stock_occupySET update_time = NOW(),update_user = 'WAPS',qty_out_occupy=qty_out_occupy + 11.0000WHERE map_area_id = 608AND goods_no='EMG4418442253742'AND owner_no='0'AND lot_no='-1'AND product_level='100'AND org_no = '10'AND distribute_no = '10'AND warehouse_no = '126'AND map_area_id = 608*** (2) HOLDS THE LOCK(S):RECORD LOCKS space id 127 page no 5255 n bits 272 index idx_map_goods_product_lot_owner of table `xwms`.`stock_occupy` trx id 13020606128 lock_mode X locks rec but not gapRecord lock, heap no 53 PHYSICAL RECORD: n_fields 6; compact format; info bits 00: len 8; hex 8000000000000260; asc        `;;1: len 16; hex 454d4734343138343333323135323331; asc EMG4418433215231;;2: len 3; hex 313030; asc 100;;3: len 2; hex 2d31; asc -1;;4: len 1; hex 30; asc 0;;5: len 8; hex 8000000000042de4; asc       - ;;*** (2) WAITING FOR THIS LOCK TO BE GRANTED:RECORD LOCKS space id 127 page no 5276 n bits 240 index idx_map_goods_product_lot_owner of table `xwms`.`stock_occupy` trx id 13020606128 lock_mode X locks rec but not gap waitingRecord lock, heap no 38 PHYSICAL RECORD: n_fields 6; compact format; info bits 00: len 8; hex 8000000000000260; asc        `;;1: len 16; hex 454d4734343138343432323533373432; asc EMG4418442253742;;2: len 3; hex 313030; asc 100;;3: len 2; hex 2d31; asc -1;;4: len 1; hex 30; asc 0;;5: len 8; hex 8000000000044335; asc       C5;;*** WE ROLL BACK TRANSACTION (2)
```

其中：

•加锁索引相同，都是二级索引；

•两个事务中三个锁对应两个主键，包括 8000000000044335（279349）/ 8000000000042de4（273892）；

•binlog 中显示提交事务也就是事务 1 中先后 update 279349 与 273892，因此判断死锁原因是交叉更新。

## 表结构

```
`id`bigint(20)NOTNULLAUTO_INCREMENTCOMMENT'自增id',`map_area_id`bigint(20)NOTNULLCOMMENT'地图区域ID',`goods_no`varchar(50)NOTNULLCOMMENT'商品编号',`product_level`varchar(50)NOTNULLCOMMENT'商品等级',`lot_no`varchar(50)NOTNULLCOMMENT'批次号',`owner_no`varchar(50)NOTNULLCOMMENT'货主编号',PRIMARYKEY(`id`),UNIQUEKEY`idx_map_goods_product_lot_owner`(`map_area_id`,`goods_no`,`product_level`,`lot_no`,`owner_no`)
```

其中：

•加锁索引是二级联合唯一索引；

•update 根据二级唯一索引更新非索引字段，因此执行时具体原地更新主键索引，二级索引不变，且加锁类型是 X 型 record lock；

•综合以上信息，判断死锁原因是两个事务交叉更新同一张表的两行数据导致死锁。

下面介绍如何从死锁日志中获取有效信息，并分析其中最重要的信息-锁，包括锁的类型、不同类型锁的兼容性、常见加锁规则。

# 死锁分析方法

## 日志格式

简化后的死锁日志格式如下所示。

```
InnoDB:***(1)TRANSACTION:InnoDB:***(1) WAITING FOR THIS LOCKTO BE GRANTED:InnoDB:***(2)TRANSACTION:InnoDB:***(2) HOLDS THE LOCK(S):InnoDB:***(2) WAITING FOR THIS LOCKTO BE GRANTED:InnoDB:*** WE ROLL BACK TRANSACTION(1)
```

其中主要信息包括：

•两个事务

•两条 SQL

•三部分锁信息

其中存在的问题包括：

•两个事务有等锁 SQL，没有可能存在的持锁 SQL；

•事务 1 缺少持锁类型，8.0 中已提供；

•SQL 超长时自动截断；

•加锁行数据是十六进制，因此需要根据字段的数据类型转换成对应格式，比如十进制或字符串。

其中前两种信息的缺失直接导致死锁分析的难度增大，因此死锁原因分析通常需要反推来处理，也就是从等锁类型判断持锁类型。

缺少部分可以参考以下分析方法：

•binlog，可以获取提交事务中已执行的 SQL 以及可能存在的更新前的记录；

•general log，可以获取提交事务与回滚事务中已执行的 SQL，包括已执行无更新的操作，比如删除不存在的记录。

## 锁信息

MySQL 中锁的粒度包括实例、表、行，其中后两种都可能导致死锁，本文假设都是行粒度，也就是行锁。

注意**行锁是给表的索引的记录加锁**，且是给访问过的对象加锁。

死锁日志中与锁相关的信息包括：

•锁所属表，比如分区表与非分区表的加锁规则不同；

•锁所属索引，比如唯一键与非唯一键的加锁规则不同；

•锁类型，其中不同类型锁的兼容性不同；

•锁定数据行，其中：

◦不同行的加锁类型可能不同，比如右边界记录（supremum pseudo-record）的 next-key lock 无法退化；

◦数据行是否标记删除可能影响到后续加锁，一个字节中的第六位表示是否标记删除（info bits），因此十进制 32 表示标记删除。比如二级唯一索引的唯一性检查时如果发现冲突行已标记删除，将循环给下一行加锁直到数据不冲突。

当然也有其他因素影响加锁的类型，主要包括：

•数据库版本，比如 5.7.26 中针对 replace / insert duplicate 语句的加锁进行优化，唯一键不冲突时不加间隙锁；

•事务隔离级别，比如 RC 中没有间隙锁；

这些信息都可以认为是死锁案例的特征，其中**锁类型是最重要的特征**。

## 锁类型

锁类型（type\_mode）主要包括以下三部分信息：

•lock\_mode，表示锁的模式，包括 IS、IX、S、X、AUTO\_INC；

•lock\_type，表示锁的粒度，包括 RECORD 与 TABLE，对应行锁与表锁；

•rec\_lock\_type，表示行锁的类型，包括 record lock、gap lock、next-key lock、insert intention lock。其中：

◦gap lock 是事务隔离级别 RR 中为解决幻读引入的锁类型；

◦insert intention lock 是一种特殊的 gap lock，表示插入的意向，用于在插入操作存在 gap lock 时表示等待状态。

比如死锁日志中锁类型显示 lock\_mode X locks rec but not gap waiting，其中：

•lock\_mode = X

•lock\_type = RECORD

•rec\_lock\_type = record lock

•lock\_status = WAITING

注意锁的状态分两种，包括已获取到（GRANTED）与等待中（WAITING）。

**死锁由两组锁等待组成，锁等待发生在锁冲突时，锁冲突根据锁兼容矩阵判断**，下面介绍锁兼容矩阵。

## 锁兼容矩阵

不同类型行锁的兼容性见下表，其中第一行表示已有的锁，第一列表示要加的锁，❌ 表示锁冲突。

| 锁类型 | record | gap | next-key | insert intention |
| --- | --- | --- | --- | --- |
| record | ❌ |  | ❌ |  |
| gap |  |  |  |  |
| next-key | ❌ |  | ❌ |  |
| insert intention |  | ❌ | ❌ |  |

其中：

•insert intention 不影响其他事务加任何类型的锁；

•gap lock 只和 insert intention 冲突，用于防止其他事务在间隙中插入记录导致幻读，与其他锁不冲突；

•**如果已有的锁是等待状态，要加的锁与该锁冲突，要加的锁同样会发生锁等待。**

## 常见加锁规则

加锁场景：

•查询（数据定位），不是 MVCC，加锁读，包括回表加锁；

•更新，下面是部分场景与对应加锁类型：

◦为防止脏写，record lock；

◦为防止幻读，gap lock；

◦为防止唯一键冲突，next-key lock。

加锁类型：

•显式锁；

•隐式锁，比如 insert、update、delete 语句在没有锁冲突时不加显式锁，必要时转换成显式锁。

**加锁的单位是 next-key lock，部分场景下会发生退化**，其中：

•退化为 record lock：

◦唯一索引上的等值查询；

•退化为 gap lock：

◦非唯一索引的等值查询向右遍历到第一个不满足等值条件的记录；

不退化的场景：

•supremum pseudo-record；

•inse...