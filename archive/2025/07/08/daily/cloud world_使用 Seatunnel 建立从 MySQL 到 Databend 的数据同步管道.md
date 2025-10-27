---
title: 使用 Seatunnel 建立从 MySQL 到 Databend 的数据同步管道
url: https://cloudsjhan.github.io/2025/07/07/%E4%BD%BF%E7%94%A8-Seatunnel-%E5%BB%BA%E7%AB%8B%E4%BB%8E-MySQL-%E5%88%B0-Databend-%E7%9A%84%E6%95%B0%E6%8D%AE%E5%90%8C%E6%AD%A5%E7%AE%A1%E9%81%93/
source: cloud world
date: 2025-07-08
fetch_date: 2025-10-06T23:24:57.547050
---

# 使用 Seatunnel 建立从 MySQL 到 Databend 的数据同步管道

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## 使用 Seatunnel 建立从 MySQL 到 Databend 的数据同步管道

posted

2025-07-07

|

in

[Databend](/categories/Databend/)

|

visitors:

|

|

wordcount:

1,208
|

min2read ≈

5

使用 Seatunnel 建立从 MySQL 到 Databend 的数据同步管道

![](https://)

使用 Seatunnel 建立从 MySQL 到 Databend 的数据同步管道

## 前言

[SeaTunnel](https://github.com/apache/seatunnel "seatunnel") 是一个非常易用、超高性能的分布式数据集成平台，支持实时海量数据同步。 每天可稳定高效地同步数百亿数据，已被近百家企业应用于生产，在国内较为普及。

[Databend](https://github.com/databendlabs/databend "databend") 是一款开源、弹性、低成本，基于对象存储也可以做实时分析的云原生湖仓。

## seatunnel 架构

SeaTunnel 整体架构：

![img](https://wubx.net/assets/images/seatunnel_arch-c02a9d297450d0f9522324b2f196fa06.png)

本文将使用 Seatunnel 建立从 MySQL 到 Databend 的数据同步管道，实现从 MySQL 数据源同步数据到 Databend 目标表的目的。

## SeaTunnel MySQL-CDC 和 Databend Sink Connector

SeaTunnel 的 MySQL CDC 连接器允许从 MySQL 数据库中读取快照数据和增量数据，其实现的原理是基于 debezium-mysql-connector 。

而 Databend 在 PR [[Feature][Connector-V2] Support databend source/sink connector](https://github.com/apache/seatunnel/pull/9331) 之后也同时在 seatunnel 中支持了 Databend 作为 Source 和 Sink Connector。这里我们使用 Seatunnel 的 MySQL-CDC Source Connector 和 Databend Sink Connector 来搭建数据同步管道。

### 编译 Seatunnel

由于上述 Databend Connector 的 PR 刚合并入 seatunnel 的 dev 分支，还没有正式 release，所以目前要使用 Databend Connector 的话，需要基于源码对 seatunnel 进行构建。

#### Clone 源码

首先我们需要从 [GitHub](https://github.com/apache/seatunnel) 克隆 SeaTunnel 源代码。

|  |  |
| --- | --- |
| ``` 1 ``` | ``` git clone git@github.com:apache/seatunnel.git ``` |

#### 本地安装子项目

在克隆源代码之后，需要运行 `./mvnw` 命令将子项目安装到 maven 本地存储库。否则代码无法在 JetBrains IntelliJ IDEA 中正确启动。

|  |  |
| --- | --- |
| ``` 1 ``` | ``` ./mvnw install -Dmaven.test.skip ``` |

#### 构建 Seatunnel

安装 maven 后，可以使用以下命令进行编译和打包。

|  |  |
| --- | --- |
| ``` 1 ``` | ``` mvn clean package -pl seatunnel-dist -am -Dmaven.test.skip=true ``` |

构建后的内容在 `seatunnel/seatunnel-dist/target` 中，我们需要解压 `apache-seatunnel-2.3.12-SNAPSHOT-src.tar.gz`，得到如下目录：

![image-20250707225303179](https://p.ipic.vip/jkucr9.png)

`bin` 下面是可以直接运行的 shell 脚本，能够一键启动 seatunnel；

config 中是 jvm options 相关的配置文件；

lib 中是运行 seatunnel 或者 connector 相关的 jar 包。

### 创建 connector 配置文件

我们的任务设定是通过 SeaTunnel 从 MySQL 中同步 mydb.t1 表。 配置文件 为 mysql-to-databend.conf：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``` | ``` env{   parallelism = 1   job.mode = "STREAMING"   checkpoint.interval = 2000 }  source {   MySQL-CDC {    base-url="jdbc:mysql://127.0.0.1:3306/mydb"    username="root"    password="123456"    table-names=["mydb.t1"]    startup.mode="initial"   } } sink {   Databend {     url = "jdbc:databend://127.0.0.1:8000?presigned_url_disabled=true"     database = "default"     table = "t1"     username = "databend"     password = "databend"     # 批量操作设置     batch_size = 2     # 如果目标表不存在，是否自动创建     auto_create = true   } } ``` |

相关的参数设定可以参考 [seatunnel MySQL文档](https://github.com/apache/seatunnel/blob/dev/docs/en/connector-v2/source/Mysql.md) 和 [seatunnel Databend Connector](https://github.com/apache/seatunnel/blob/dev/docs/en/connector-v2/source/Databend.md)。

### 本地启动 MySQL 与 Databend

#### 启动并初始化 MySQL 表数据

本地启动 MySQL 后，创建一个数据库 `mydb`，在 mydb 中新建一张表并插入 10 条数据：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` create database mydb; use mydb; create table t1 (a int, b varchar(100)); insert into t1 values(1,'aa') ... insert into t1 values(10,'bb') ``` |

### 本地启动 Databend

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` | ``` version: '3' services:   databend:     image: datafuselabs/databend:v1.2.754-nightly     platform: linux/arm64     ports:       - "8000:8000"     environment:       - QUERY_DEFAULT_USER=databend       - QUERY_DEFAULT_PASSWORD=databend       - MINIO_ENABLED=true     volumes:       - ./data:/var/lib/minio     healthcheck:       test: "curl -f localhost:8080/v1/health || exit 1"       interval: 2s       retries: 10       start_period: 2s       timeout: 1s ``` |

直接 `docker-compose up` 即可启动 databend 服务。

### 启动 seatunnel

|  |  |
| --- | --- |
| ``` 1 ``` | ``` ./bin/seatunnel.sh --config ./bin/mysql-to-databend.conf -m local ``` |

![image-20250707230833879](https://p.ipic.vip/fzjccp.png)

启动后 Databend Sink Connector 会首先将 MySQL 表中的全量数据同步过来:

![image-20250707231035562](https://p.ipic.vip/c89rt7.png)

接下来我们往 MySQL 中插入几条数据，就会同步 MySQL 中增量的数据：

![image-20250707231208003](https://p.ipic.vip/1pjyrc.png)

可以看到 seatunnel 在终端输出的日志：

![image-20250707231319145](https://p.ipic.vip/5zsk70.png)

以及 Databend 中查询到数据：

![image-20250707231352622](https://p.ipic.vip/fu4asb.png)

说明数据已经及时同步过来了。

> 目前 Databend Sink Connector 还只支持 Append Only 模式，对于 update、delete 的数据没做处理，会在下一个 seatunnel 的 PR 中实现完整的 CDC 功能。

## 结论

通过本文我们成功实现了从 MySQL 到 Databend 的实时数据同步管道。这个解决方案具有以下优势：

1. **简单易用**：SeaTunnel 提供了简洁的配置方式，只需少量配置即可建立高效的数据同步管道。
2. **实时性强**：基于 CDC 技术，能够实时捕获 MySQL 的数据变更并同步到 Databend。
3. **可扩展性好**：SeaTunnel 的分布式架构使其能够处理海量数据同步需求。
4. **低开发成本**：无需编写复杂的 ETL 代码，通过配置文件即可完成数据集成任务。

需要注意的是，目前 Databend Sink Connector 还只支持 Append Only 模式，对于 update、delete 的数据没做处理，完整的 CDC 功能将在后续的 PR 中实现。这个方案特别适合需要将 MySQL 数据实时同步到 Databend 进行分析的场景，帮助企业构建实时数据湖仓架构。

---

-------------The End-------------

Title:[使用 Seatunnel 建立从 MySQL 到 Databend 的数据同步管道](/2025/07/07/%E4%BD%BF%E7%94%A8-Seatunnel-%E5%BB%BA%E7%AB%8B%E4%BB%8E-MySQL-%E5%88%B0-Databend-%E7%9A%84%E6%95%B0%E6%8D%AE%E5%90%8C%E6%AD%A5%E7%AE%A1%E9%81%93/)

Author:[cloud sjhan](/ "visit cloud sjhan blog")

Publish Time:2025年07月07日 - 23:07

Last Update:2025年07月07日 - 23:07

Original Link:[https://cloudsjhan.github.io/2025/07/07/使用-Seatunnel-建立从-MySQL-到-Databend-的数据同步管道/](/2025/07/07/%E4%BD%BF%E7%94%A8-Seatunnel-%E5%BB%BA%E7%AB%8B%E4%BB%8E-MySQL-%E5%88%B0-Databend-%E7%9A%84%E6%95%B0%E6%8D%AE%E5%90%8C%E6%AD%A5%E7%AE%A1%E9%81%93/ "使用 Seatunnel 建立从 MySQL 到 Databend 的数据同步管道")

License: [By-NC-ND 4.0 international](https://creativecommons.org/licenses/by-nc-nd/4.0/ "Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)")。

![cloud sjhan wechat](/images/wechat-qcode.jpg)

keep going, keep coding

donate

![cloud sjhan 微信支付](/images/wechatpay.jpg)

![cloud sjhan 支付宝](/images/alipay.jpg)

[Databend](/tags/Databend/)
 [Seatunnel](/tags/Seatunnel/)

(>给这篇博客打个分吧<)

[打破信息差，手把手教你本地部署 DeepSeek](/2025/02/07/%E6%89%93%E7%A0%B4%E4%BF%A1%E6%81%AF%E5%B7%AE%EF%BC%8C%E6%89%8B%E6%8A%8A%E6%89%8B%E6%95%99%E4%BD%A0%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2-DeepSeek/ "打破信息差，手把手教你本地部署 DeepSeek")

[SeaTunnel Databend Sink Connector CDC 功能实现详解](/2025/08/18/SeaTunnel-Databend-Sink-Connector-CDC-%E5%8A%9F%E8%83%BD%E5%AE%9E%E7%8E%B0%E8%AF%A6%E8%A7%A3/ "SeaTunnel Databend Sink Connector CDC 功能实现详解")

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

1. [1. 前言](#前言)
2. [2. seatunnel 架构](#seatunnel-架构)
3. [3. SeaTunnel MySQL-CDC 和 Databend Sink Connector](#SeaTunnel-MySQL-CDC-和-Databend-Sink-Connector)
   1. [3.1. 编译 Seatunnel](#编译-Seatunnel)
      1. [3.1.1. Clone 源码](#Clone-源码)
      2. [3.1.2. 本地安装子项目](#本地安装子项目)
      3. [3.1.3. 构建 Seatunnel](#构建-Seatunnel)
   2. [3.2. 创建 connector 配置文件](#创建-connector-配置文件)
   3. [3.3. 本地启动 MySQL 与 Databend](#本地启动-MySQL-与-Databend)
      1. [3.3.1. 启动并初始化 MySQL 表数据](#启动并初始化-MySQL-表数据)
   4. [3.4. 本地启动 Databend](#本地启动-Databend)
   5. [3.5. 启动 seatunnel](#启动-seatunnel)
4. [4. 结论](#结论)

© 2018 — 2025

cloud sjhan
|

Site words total count:
308.0k

stay hungry,stay foolish

Total Words:308.0k

0%

;