---
title: Golang 如何实现自定义 CDC 工具？
url: https://cloudsjhan.github.io/2024/05/04/Golang-%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E8%87%AA%E5%AE%9A%E4%B9%89-CDC-%E5%B7%A5%E5%85%B7%EF%BC%9F/
source: cloud world
date: 2024-05-05
fetch_date: 2025-10-06T17:15:42.306673
---

# Golang 如何实现自定义 CDC 工具？

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## Golang 如何实现自定义 CDC 工具？

posted

2024-05-04

|

in

[CDC](/categories/CDC/)

|

visitors:

|

|

wordcount:

917
|

min2read ≈

3

Golang 如何实现自定义 CDC 工具

![](https://)

### CDC

变更数据捕获（CDC）是一种跟踪数据库更改的技术，允许开发人员捕获应用于行的插入、更新和删除。它是数据集成和实时处理任务的重要组成部分。在本文中，我们将讨论如何在 Golang 中为 PostgreSQL、Oracle、MySQL、MongoDB 和 SQL Server 等多个数据库开发自定义 CDC 工具。

通常在 CDC 领域或者说大数据领域都是 java 的生态比较繁荣，比如 Flink, Spark, 最近大火的 [paimon](https://paimon.apache.org/ "paimon") 都是 java 写的。Java 在数据生态的繁荣为对应数据工具的开发提供了土壤。那么我们 Gopher 如果也想开发 CDC 工具怎么办？今天介绍的是一些 golang 的 Lib，基于这些 lib 我们也可以实现自定义的 CDC 工具。

### PostgreSQL

对于 PostgreSQL，我们可以使用 [pglogrepl](github.com/jackc/pglogrepl "pglogrepl") 库（github.com/jackc/pglogrepl）。该库提供了 PostgreSQL 中的逻辑解码和流复制协议的低级 API。它允许您读取 PostgreSQL 的预写式日志（WAL），这些日志是存储所有对数据库的更改的地方。通过读取和解码这些日志，我们可以跟踪数据库中的更改。解码可以在插件级别或消费者级别进行，这取决于 PostgreSQL 中使用的解码插件。

### Oracle

为 Oracle 创建 CDC 工具要复杂一些。Oracle 有一个名为 “LogMiner” 的内置工具，它允许您通过 SQL 接口查询在线和归档的重做日志文件。数据的主要来源将是 V$LOGMNR\_CONTENTS 视图，这是 LogMiner 在对其进行挖掘后的重做日志数据的视图。

我们的 CDC 工具需要定期查询此视图，并解析 SQL\_REDO 和 SQL\_UNDO 字段，以了解对数据库所做的更改。这需要理解 Oracle 的 SQL 语法，并可能处理不同版本的 Oracle，因为语法可能会发生变化。

### MySQL

可以使用 [go-mysql](https://github.com/go-mysql-org/go-mysql "go-mysql") 库（github.com/go-mysql-org/go-mysql/canal）处理 MySQL。该软件包提供了一个框架，用于将 MySQL 的 binlog 同步到其他系统。它支持将 MySQL 的 binlog 同步到用户定义的处理程序，例如 stdout 和 Kafka 消息队列。通过使用该库，我们可以相对简单地跟踪数据库中的更改。

### MongoDB

对于 MongoDB，我们可以使用 [mongo-driver/mongo](go.mongodb.org/mongo-driver/mongo "mongo-driver") 包（go.mongodb.org/mongo-driver/mongo）。该软件包为 Go 提供了 MongoDB 驱动程序 API。MongoDB 驱动程序支持 “Change Streams”，它允许应用程序访问实时数据更改，而无需尾随 oplog 的复杂性和风险。应用程序可以使用更改流订阅单个集合、数据库或整个部署上的所有数据更改，并立即对其进行响应。

### SQL Server

对于 SQL Server，我们可以利用 [go-mssqldb](github.com/denisenkom/go-mssqldb "go-mssqldb") 包（github.com/denisenkom/go-mssqldb）。SQL Server 支持变更跟踪，它跟踪表上的 DML 更改（插入、更新、删除）。通过查询这些变更表，我们可以获取有关更改的信息。请注意，这只会告诉我们更改行的键，而不是数据本身。要获取更改的数据，我们需要对实际数据表进行另一个查询。

### 结论

在 Golang 中创建自定义 CDC 工具涉及理解每个数据库用于记录更改的基础机制。通过利用现有软件包的功能，我们可以构建一个强大的工具，可以跟踪多种类型数据库的更改。然而，要实现高效和有效的 CDC 工具，需要对每个数据库的日志机制有透彻的了解，以及对 Golang 有扎实的掌握。

---

-------------The End-------------

Title:[Golang 如何实现自定义 CDC 工具？](/2024/05/04/Golang-%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E8%87%AA%E5%AE%9A%E4%B9%89-CDC-%E5%B7%A5%E5%85%B7%EF%BC%9F/)

Author:[cloud sjhan](/ "visit cloud sjhan blog")

Publish Time:2024年05月04日 - 21:05

Last Update:2024年05月04日 - 21:05

Original Link:[https://cloudsjhan.github.io/2024/05/04/Golang-如何实现自定义-CDC-工具？/](/2024/05/04/Golang-%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E8%87%AA%E5%AE%9A%E4%B9%89-CDC-%E5%B7%A5%E5%85%B7%EF%BC%9F/ "Golang 如何实现自定义 CDC 工具？")

License: [By-NC-ND 4.0 international](https://creativecommons.org/licenses/by-nc-nd/4.0/ "Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)")。

![cloud sjhan wechat](/images/wechat-qcode.jpg)

keep going, keep coding

donate

![cloud sjhan 微信支付](/images/wechatpay.jpg)

微信支付

![cloud sjhan 支付宝](/images/alipay.jpg)

支付宝

[Golang](/tags/Golang/)
 [CDC](/tags/CDC/)

(>给这篇博客打个分吧<)

[基于 langchaingo 对接大模型 ollama 实现本地知识库问答系统](/2024/05/03/%E5%9F%BA%E4%BA%8E-langchaingo-%E5%AF%B9%E6%8E%A5%E5%A4%A7%E6%A8%A1%E5%9E%8B-ollama-%E5%AE%9E%E7%8E%B0%E6%9C%AC%E5%9C%B0%E7%9F%A5%E8%AF%86%E5%BA%93%E9%97%AE%E7%AD%94%E7%B3%BB%E7%BB%9F/ "基于 langchaingo 对接大模型 ollama 实现本地知识库问答系统")

[一些在 Golang 中高效处理 Collection 类型的库](/2024/05/05/%E4%B8%80%E4%BA%9B%E5%9C%A8-Golang-%E4%B8%AD%E9%AB%98%E6%95%88%E5%A4%84%E7%90%86-Collection-%E7%B1%BB%E5%9E%8B%E7%9A%84%E5%BA%93/ "一些在 Golang 中高效处理 Collection 类型的库")

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

1. [1. CDC](#CDC)
2. [2. PostgreSQL](#PostgreSQL)
3. [3. Oracle](#Oracle)
4. [4. MySQL](#MySQL)
5. [5. MongoDB](#MongoDB)
6. [6. SQL Server](#SQL-Server)
7. [7. 结论](#结论)

© 2018 — 2025

cloud sjhan
|

Site words total count:
308.0k

stay hungry,stay foolish

Total Words:308.0k

0%

;