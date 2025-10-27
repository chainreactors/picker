---
title: 基于 Flink CDC 构建 MySQL 到 Databend 的 实时数据同步
url: https://cloudsjhan.github.io/2025/08/22/%E5%9F%BA%E4%BA%8E-Flink-CDC-%E6%9E%84%E5%BB%BA-MySQL-%E5%88%B0-Databend-%E7%9A%84-%E5%AE%9E%E6%97%B6%E6%95%B0%E6%8D%AE%E5%90%8C%E6%AD%A5/
source: cloud world
date: 2025-08-23
fetch_date: 2025-10-07T00:48:07.765332
---

# 基于 Flink CDC 构建 MySQL 到 Databend 的 实时数据同步

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## 基于 Flink CDC 构建 MySQL 到 Databend 的 实时数据同步

posted

2025-08-22

|

in

[Databend](/categories/Databend/)

|

visitors:

|

|

wordcount:

1,343
|

min2read ≈

7

![](https://)

# 基于 Flink CDC 构建 MySQL 到 Databend 的 实时数据同步

这篇教程将展示如何基于 Flink CDC 快速构建 MySQL 到 Databend 的实时数据同步。本教程的演示都将在 Flink SQL CLI 中进行，只涉及 SQL，无需一行 Java/Scala 代码，也无需安装 IDE。

假设我们有电子商务业务，商品的数据存储在 MySQL ，我们需要实时把它同步到 Databend 中。

接下来的内容将介绍如何使用 Flink Mysql/Databend CDC 来实现这个需求，系统的整体架构如下图所示：

## **准备阶段**

准备一台已经安装了 Docker 的 Linux 或者 MacOS 电脑。

### **准备教程所需要的组件**

接下来的教程将以 `docker-compose` 的方式准备所需要的组件。

### debezium-MySQL

docker-compose.yaml

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` version: '2.1' services:   postgres:     image: debezium/example-postgres:1.1     ports:       - "5432:5432"     environment:       - POSTGRES_DB=postgres       - POSTGRES_USER=postgres       - POSTGRES_PASSWORD=postgres   mysql:     image: debezium/example-mysql:1.1     ports:       - "3306:3306"     environment:       - MYSQL_ROOT_PASSWORD=123456       - MYSQL_USER=mysqluser       - MYSQL_PASSWORD=mysqlpw ``` |

### Databend

docker-compose.yaml

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` | ``` version: '3' services:   databend:     image: datafuselabs/databend     volumes:       - /Users/hanshanjie/databend/local-test/databend/databend-query.toml:/etc/databend/query.toml     environment:       QUERY_DEFAULT_USER: databend       QUERY_DEFAULT_PASSWORD: databend       MINIO_ENABLED: 'true'     ports:       - '8000:8000'       - '9000:9000'       - '3307:3307'       - '8124:8124' ``` |

在 `docker-compose.yml` 所在目录下执行下面的命令来启动本教程需要的组件：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` ocker-compose up -d ``` |

该命令将以 detached 模式自动启动 Docker Compose 配置中定义的所有容器。你可以通过 docker ps 来观察上述的容器是否正常启动。

### **下载 Flink 和所需要的依赖包**

1. 下载 [Flink 1.16.0](https://archive.apache.org/dist/flink/flink-1.16.0/flink-1.16.0-bin-scala_2.12.tgz) 并将其解压至目录 `flink-1.16.0`
2. 下载下面列出的依赖包，并将它们放到目录 `flink-1.16.0/lib/` 下：
3. **下载链接只对已发布的版本有效, SNAPSHOT 版本需要本地编译**

* [flink-sql-connector-mysql-cdc-2.3.0.jar](https://repo1.maven.org/maven2/com/ververica/flink-sql-connector-mysql-cdc/2.3.0/flink-sql-connector-mysql-cdc-2.3.0.jar)
* 最好将 conf/flink-conf.yaml 中的 taskmanager.memory.process.size 改为 4096m

  以及将 [taskmanager.sh](http://taskmanager.sh) 中的 UseGCG1 去掉

## 编译 flink-connector-databend

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` git clone https://github.com/databendcloud/flink-connector-databend cd flink-connector-databend mvn clean install -DskipTests ``` |

将 target/flink-connector-databend-1.16.0-SNAPSHOT.jar 拷贝到目录 `flink-1.16.0/lib/` 下。

### **准备数据**

### **在 MySQL 数据库中准备数据**

进入 MySQL 容器

|  |  |
| --- | --- |
| ``` 1 ``` | ``` docker-compose exec mysql mysql -uroot -p123456 ``` |

创建数据库 mydb 和表 `products`，并插入数据:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` | ``` CREATE DATABASE mydb; USE mydb;  CREATE TABLE products (id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255) NOT NULL,description VARCHAR(512)); ALTER TABLE products AUTO_INCREMENT = 10;  INSERT INTO products VALUES (default,"scooter","Small 2-wheel scooter"), (default,"car battery","12V car battery"), (default,"12-pack drill bits","12-pack of drill bits with sizes ranging from #40 to #3"), (default,"hammer","12oz carpenter's hammer"), (default,"hammer","14oz carpenter's hammer"), (default,"hammer","16oz carpenter's hammer"), (default,"rocks","box of assorted rocks"), (default,"jacket","water resistent black wind breaker"), (default,"cloud","test for databend"), (default,"spare tire","24 inch spare tire"); ``` |

### Databend 中建表

|  |  |
| --- | --- |
| ``` 1 ``` | ``` CREATE TABLE bend_products (id INT NOT NULL, name VARCHAR(255) NOT NULL, description VARCHAR(512) ); ``` |

## **启动 Flink 集群和 Flink SQL CLI**

使用下面的命令跳转至 Flink 目录下

|  |  |
| --- | --- |
| ``` 1 ``` | ``` cd flink-16.0 ``` |

使用下面的命令启动 Flink 集群

|  |  |
| --- | --- |
| ``` 1 ``` | ``` ./bin/start-cluster.sh ``` |

启动成功的话，可以在 <http://localhost:8081/> 访问到 Flink Web UI，如下所示：

使用下面的命令启动 Flink SQL CLI

|  |  |
| --- | --- |
| ``` 1 ``` | ``` ./bin/sql-client.sh ``` |

## **在 Flink SQL CLI 中使用 Flink DDL 创建表**

首先，开启 checkpoint，每隔3秒做一次 checkpoint

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` -- Flink SQL Flink SQL> SET execution.checkpointing.interval = 3s; ``` |

然后, 对于数据库中的表 `products` 使用 Flink SQL CLI 创建对应的表，用于同步底层数据库表的数据

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` -- Flink SQL Flink SQL> CREATE TABLE products (id INT,name STRING,description STRING,PRIMARY KEY (id) NOT ENFORCED) WITH ('connector' = 'mysql-cdc', 'hostname' = '127.0.0.1', 'port' = '3306', 'username' = 'root', 'password' = '123456', 'database-name' = 'mydb', 'table-name' = 'products', 'server-time-zone' = 'UTC' ); ``` |

最后，创建 d\_products 表， 用来订单数据写入 Databend 中

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` -- Flink SQL create table d_products (id INT,name String,description String) with ('connector' = 'databend', 'url'='databend://cloudapp:ssggkxgub3k0@tn3ftqihs.gw.aws-us-east-2.default.databend.com:443/testdb?warehouse=medium-p8at&ssl=true', 'database-name'='testdb', 'table-name'='bend_products', 'sink.batch-size' = '1', 'sink.ignore-delete' = 'false', 'sink.flush-interval' = '1000', 'sink.max-retries' = '3'); ``` |

使用 Flink SQL 将 products 表中的数据同步到 Databend 的 d\_products 表中：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` insert into d_products select * from products; ``` |

此时 flink job 就会提交成功，打开 flink UI 可以看到:

同时在 databend 中可以看到 MySQL 中的数据已经同步过来了：

## 同步 Insert/Update 数据

此时我们在 MySQL 中再插入 10 条数据：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` INSERT INTO products VALUES (default,"scooter","Small 2-wheel scooter"), (default,"car battery","12V car battery"), (default,"12-pack drill bits","12-pack of drill bits with sizes ranging from #40 to #3"), (default,"hammer","12oz carpenter's hammer"), (default,"hammer","14oz carpenter's hammer"), (default,"hammer","16oz carpenter's hammer"), (default,"rocks","box of assorted rocks"), (default,"jacket","water resistent black wind breaker"), (default,"cloud","test for databend"), (default,"spare tire","24 inch spare tire"); ``` |

这些数据会立即同步到 Databend 当中。

假如此时 MySQL 中更新了一条数据:

那么 id=10 的数据在 databend 中也会被立即更新：

## **环境清理**

操作结束后，在 `docker-compose.yml` 文件所在的目录下执行如下命令停止所有容器：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` docker-compose down ``` |

在 Flink 所在目录 `flink-1.16.0` 下执行如下命令停止 Flink 集群：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` ./bin/stop-cluster.sh ``` |

## 结论

以上就是基于 Flink CDC 构建 MySQL 到 Databend 的 实时数据同步的全部过程。

mysql flink connector is over 2.4.1

flin version is 1.17.1

---

-------------The End-------------

Title:[基于 Flink CDC 构建 MySQL 到 Databend 的 实时数据同步](/2025/08/22/%E5%9F%BA%E4%BA%8E-Flink-CDC-%E6%9E%84%E5%BB%BA-MySQL-%E5%88%B0-Databend-%E7%9A%84-%E5%AE%9E%E6%97%B6%E6%95%B0%E6%8D%AE%E5%90%8C%E6%AD%A5/)

Author:[cloud sjhan](/ "visit cloud sjhan blog")

Publish Time:2025年08月22日 - 17:08

Last Update:2025年08月22日 - 17:08

Original Link:[https://cloudsjhan.github.io/2025/08/22/基于-Flink-CDC-构建-MySQL-到-Databend-的-实时数据同步/](/2025/08/22/%E5%9F%BA%E4%BA%8E-Flink-CDC-%E6%9E%84%E5%BB%BA-MySQL-%E5%88%B0-Databend-%E7%9A%84-%E5%AE%9E%E6%97%B6%E6%95%B0%E6%8D%AE%E5%90%8C%E6%AD%A5/ "基于 Flink CDC 构建 MySQL 到 Databend 的 实时数据同步")

License: [By-NC-ND 4.0 international](https://creativecommons.org/licenses/by-nc-nd/4.0/ "Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)")。

![cloud sjhan wechat](/images/wechat-qcode.jpg)

keep going, keep coding

donate

![cloud sjhan 微信支付](/images/wechatpay.jpg)

微信支付

![cloud sjhan 支付宝](/images/alipay.jpg)

支付宝

[Databend](/tags/Databend/)
 [Flink](/tags/Flink/)

(>给这篇博客打个分吧<)

[Deep Dive into SeaTunnel Databend Sink Connector CDC Implementation](/2025/08/18/Deep-Dive-into-Sea...