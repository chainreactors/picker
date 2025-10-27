---
title: 在 Confluent Cloud 上使用 Databend Kafka Connect 构建实时数据流同步
url: https://cloudsjhan.github.io/2024/07/25/%E5%9C%A8-Confluent-Cloud-%E4%B8%8A%E4%BD%BF%E7%94%A8-Databend-Kafka-Connect-%E6%9E%84%E5%BB%BA%E5%AE%9E%E6%97%B6%E6%95%B0%E6%8D%AE%E6%B5%81%E5%90%8C%E6%AD%A5/
source: cloud world
date: 2024-07-26
fetch_date: 2025-10-06T17:42:07.331738
---

# 在 Confluent Cloud 上使用 Databend Kafka Connect 构建实时数据流同步

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## 在 Confluent Cloud 上使用 Databend Kafka Connect 构建实时数据流同步

posted

2024-07-25

|

in

[databend](/categories/databend/)

|

visitors:

|

|

wordcount:

1,245
|

min2read ≈

5

![](https://)

### Confluent Cloud

[Confluent Cloud](https://confluent.cloud/ "Confluent Cloud") 是由 Confluent 公司提供的云服务，它是基于 Apache Kafka 的企业级事件流平台，允许用户轻松构建和管理分布式流处理应用。Confluent 由 Apache Kafka 的原始创建者创立，专注于提供围绕 Kafka 技术的产品和服务 。

Confluent Cloud 提供的主要优势包括简化的部署和管理，高可用性，以及自动扩展能力。它是一个云端托管服务，是 Confluent Enterprise 的云端版本，增加了云端管理控制台的组件，使得用户无需担心底层基础设施的维护和扩展问题，可以更专注于业务逻辑的实现 。

Confluent Cloud 与其他 Confluent 产品一样，提供了一系列的工具和服务，例如 Kafka Connect 用于连接外部系统，Schema Registry 用于管理数据格式的变更，以及 KSQL 用于流处理查询等。这些工具和服务帮助用户构建统一而灵活的数据流平台，实现数据的实时处理和分析 。

此外，Confluent Cloud 还提供了不同层级的服务，根据可用性、安全等企业特性分为 Basic、Standard 和 Dedicated 三个版本，支持按需创建资源，并且按量收费，为用户提供了灵活的付费选项。

### Databend Kafka Connect

Databend 提供了 [Databend-Kafka-Connect](https://github.com/databendcloud/databend-kafka-connect "Databend-Kafka-connect") 作为 Apache Kafka 的 Sink connector，直接接入到 Confluent Cloud 平台，就可以实时消费 kafka topic 中的数据并写入 Databend table。

Databend kafka connect 提供了诸多特性，例如自动建表，Append Only 和 Upsert 写入模式，自动的 schema evolution。

这篇文章我们将会介绍如何在 Confluent Cloud 上使用 Databend Kafka Connector 构建实时的数据同步管道。

### 实现

#### 创建自定义 connector

Confluent 提供了一个 connector hub，在这里可以找到所有已经内置到 Confluent Cloud 中的 Connector。对于没有内置的，Confluent 支持创建自定义 connector。

##### Add plugin

![](https://files.mdnice.com/user/4760/f3a43cc7-a2f0-4c1f-9382-082a695fab4d.png)

##### 配置 plugin

![](https://files.mdnice.com/user/4760/98a64e63-32a8-475f-8d14-e3ecf78611e6.png)

填写 connector 的名称、描述以及入口 class，在这里 databend connect 的入口类是：`com.databend.kafka.connect.DatabendSinkConnector`。

`git clone https://github.com/databendcloud/databend-kafka-connect.git` 下载源码编译或者直接到 [release](https://github.com/databendcloud/databend-kafka-connect/releases "databend connect release") 页面下载打包好的 jar 文件。将其上传至 Confluent Cloud。

![](https://files.mdnice.com/user/4760/a48ad287-d83a-4eb3-a634-beef35502ab0.png)

#### 创建 Topic

创建一个新的 kafka topic

![](https://files.mdnice.com/user/4760/d09db662-e41f-438c-b900-ad5f083efc25.png)

为新创建的 topic 定义一个 schema 以确定其数据结构。这里我们确定 kafka topic 中的数据格式为 AVRO，其 schema 为：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` | ``` {   "doc": "Sample schema to help you get started.",   "fields": [     {       "doc": "The int type is a 32-bit signed integer.",       "name": "id",       "type": "int"     },     {       "doc": "The string is a unicode character sequence.",       "name": "name",       "type": "string"     },     {       "doc": "The string is a unicode character sequence.",       "name": "age",       "type": "int"     }   ],   "name": "sampleRecord",   "type": "record" } ``` |

![](https://files.mdnice.com/user/4760/6835ebf0-17da-463c-9fe9-0d5db8d47720.png)

#### Add connector for topic

为刚创建的 topic 添加一个 sink connector

![](https://files.mdnice.com/user/4760/b7dcbb0b-bca7-4c59-9cf2-d81cd03a6ed2.png)

选择上面我们自定义的 databend connector 并配置 API key 和 secret。

#### 添加 databend connector 的配置文件

![](https://files.mdnice.com/user/4760/56ed12dc-4700-46d2-b19c-fcf217032576.png)

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` | ``` {   "auto.create": "true",   "auto.evolve": "true",   "batch.size": "1",   "confluent.custom.schema.registry.auto": "true",   "connection.attempts": "5",   "connection.backoff.ms": "10000",   "connection.database": "testsync",   "connection.password": "password",   "connection.url": "jdbc:databend://tn3ftqihs--medium-p8at.gw.aws-us-east-2.default.databend.com:443?ssl=true",   "connection.user": "cloudapp",   "errors.tolerance": "all",   "insert.mode": "upsert",   "key.converter": "org.apache.kafka.connect.storage.StringConverter",   "max.retries": "10",   "pk.fields": "id",   "pk.mode": "record_value",   "table.name.format": "testsync.${topic}",   "topics": "topic_avrob",   "value.converter": "io.confluent.connect.avro.AvroConverter" } ``` |

配置文件中指定了目标端的连接参数，数据库名，表名，kafka 相关信息以及 connector converter 。
key.converter 和 value.converter 就是指定的转换器，分别指定了消息键和消息值所使用的的转换器，用于在 Kafka Connect 格式和写入 Kafka 的序列化格式之间进行转换。这控制了写入 Kafka 或从 Kafka 读取的消息中键和值的格式。由于这与 Connector 没有任何关系，因此任何 Connector 可以与任何序列化格式一起使用。默认使用 Kafka 提供的 JSONConverter。有些转换器还包含了特定的配置参数。例如，通过将 key.converter.schemas.enable 设置成 true 或者 false 来指定 JSON 消息是否包含 schema。

#### 配置网络白名单

将数据写入的目标端的 host 填入 confluent cloud 的 connection endpoint 配置，confluent 会在 kafka 和目标端之间建立 private link 以确保网络通畅。

![](https://files.mdnice.com/user/4760/57e22044-1d49-4211-ae92-12539a15c680.png)

#### 确认配置并启动 kafka connector

![](https://files.mdnice.com/user/4760/256681ea-0f35-464d-9f14-1d5802ea2db2.png)

#### 向 topic 中发送样例数据

![](https://files.mdnice.com/user/4760/fb3b0903-f227-44bb-bbaf-ac2fc4bb224e.png)

确认 kafka connect 处于 running 状态后，

我们使用 confluent CLI 工具往 topic 中发送数据：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` confluent kafka topic produce topic_avrob  --value-format avro --schema schema.json ``` |

其中 `schema.json` 就是我们为 topic 定义的 schema。

![](https://files.mdnice.com/user/4760/7e5f2c3b-36bb-428d-af9b-7afa423e7261.png)

通过 confluent cloud 的日志我们可以看到 kafka connect 已经接收到来自 topic 的消息并开始写入 databend table：

![](https://files.mdnice.com/user/4760/77548f76-747d-44c8-9a39-72a860510212.png)

同时我们在 databend cloud 中可以看到 `testsync.topic_avrob` 表已经被自动创建且数据已写入：

![](https://files.mdnice.com/user/4760/f3a3c32b-7954-4db7-8b91-df153e11de70.png)

### 总结

通过以上步骤，我们就可以在 Confluent Cloud 与 Databend Cloud 之间，使用 Databend Kafka Connector 构建起二者之间的实时数据同步管道。

---

-------------The End-------------

Title:[在 Confluent Cloud 上使用 Databend Kafka Connect 构建实时数据流同步](/2024/07/25/%E5%9C%A8-Confluent-Cloud-%E4%B8%8A%E4%BD%BF%E7%94%A8-Databend-Kafka-Connect-%E6%9E%84%E5%BB%BA%E5%AE%9E%E6%97%B6%E6%95%B0%E6%8D%AE%E6%B5%81%E5%90%8C%E6%AD%A5/)

Author:[cloud sjhan](/ "visit cloud sjhan blog")

Publish Time:2024年07月25日 - 15:07

Last Update:2024年07月25日 - 15:07

Original Link:[https://cloudsjhan.github.io/2024/07/25/在-Confluent-Cloud-上使用-Databend-Kafka-Connect-构建实时数据流同步/](/2024/07/25/%E5%9C%A8-Confluent-Cloud-%E4%B8%8A%E4%BD%BF%E7%94%A8-Databend-Kafka-Connect-%E6%9E%84%E5%BB%BA%E5%AE%9E%E6%97%B6%E6%95%B0%E6%8D%AE%E6%B5%81%E5%90%8C%E6%AD%A5/ "在 Confluent Cloud 上使用 Databend Kafka Connect 构建实时数据流同步")

License: [By-NC-ND 4.0 international](https://creativecommons.org/licenses/by-nc-nd/4.0/ "Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)")。

![cloud sjhan wechat](/images/wechat-qcode.jpg)

keep going, keep coding

donate

![cloud sjhan 微信支付](/images/wechatpay.jpg)

![cloud sjhan 支付宝](/images/alipay.jpg)

[databend](/tags/databend/)
 [kafka connect](/tags/kafka-connect/)
 [confluent](/tags/confluent/)

(>给这篇博客打个分吧<)

[Lambda-Go：将函数式编程引入 Go](/2024/07/23/Lambda-Go%EF%BC%9A%E5%B0%86%E5%87%BD%E6%95%B0%E5%BC%8F%E7%BC%96%E7%A8%8B%E5%BC%95%E5%85%A5-Go/ "Lambda-Go：将函数式编程引入 Go")

[从 Golang 到 TinyGo：如何为 IOT 构建高效应用程序？](/2024/08/01/%E4%BB%8E-Golang-%E5%88%B0-TinyGo%EF%BC%9A%E5%A6%82%E4%BD%95%E4%B8%BA-IOT-%E6%9E%84%E5%BB%BA%E9%AB%98%E6%95%88%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%EF%BC%9F/ "从 Golang 到 TinyGo：如何为 IOT 构建高效应用程序？")

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

1. [1. Confluent Cloud](#Confluent-Cloud)
2. [2. Databend Kafka Connect](#Databend-Kafka-Connect)
3. [3. 实现](#实现)
   1. [3.1. 创建自定义 connector](#创建自定义-connector)
      1. [3.1.1. Add plugin](#Add-plugin)
      2. [3.1.2. 配置 plugin](#配置-plugin)
   2. [3.2. 创建 Topic](#创建-Topic)
   3. [3.3. Add connector for topic](#Add-connector-for-topic)
   4. [3.4....