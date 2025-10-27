---
title: Jeddak-DPSQL首次开源！基于差分隐私的SQL代理保护能力
url: https://www.anquanke.com/post/id/288888
source: 安全客-有思想的安全新媒体
date: 2023-05-27
fetch_date: 2025-10-04T11:38:08.288750
---

# Jeddak-DPSQL首次开源！基于差分隐私的SQL代理保护能力

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# Jeddak-DPSQL首次开源！基于差分隐私的SQL代理保护能力

阅读量**386946**

发布时间 : 2023-05-26 11:18:53

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

# 一、背景

火山引擎对于用户敏感数据尤为重视，在火山引擎提供的数据分析产品中，广泛采用差分隐私技术对用户敏感信息进行保护。此类数据产品通常构建于 ClickHouse 等数据引擎之上，以 SQL 查询方式来执行计算逻辑，且查询逻辑往往较为复杂，因此对差分隐私的应用提出了以下要求：

* **·**零改造、零感知：最大程度避免影响业务现有查询方式，最好做到业务零感知、零改造；
* **·**良好、灵活的适配性：能够适配不同数据引擎的查询语法，以及能够处理包含多层嵌套、多重计算、多表连接等情形的复杂 SQL 语句；
* **·**安全性与可用性平衡：能够根据业务数据质量要求，计算合理的隐私预算，在安全性和数据可用性之间保持平衡；

针对以上需求，火山引擎安全研究团队开发了Jeddak-DPSQL：一种基于差分隐私的SQL代理工具。Jeddak-DPSQL 能够兼容多种数据引擎和SQL方言，内嵌多种差分噪声扰动算法，具备隐私预算管理能力，并且能够与底层数据引擎结合，在数据分析师无感的情况下，对 SQL 语句进行自动化分析和结果加噪处理。作为数据安全和隐私合规治理的标准能力之一，Jeddak-DPSQL 已经在抖音集团相关业务中得到了普遍应用与验证。

在实际解决公司内部面临的问题风险后，我们决定对 Jeddak-DPSQL 进行开源，希望能够为同样面临该类问题的企业和个人提供一定参考和帮助，同时也希望能够有更多的外部开发者能够一起对该开源项目进行共建，完善 Jeddak-DPSQL 产品功能，共同构建更完备的应用生态。

# 二、全面了解 Jeddak-DPSQL

## 2.1 Jeddak-DPSQL介绍

Jeddak-DPSQL采用中心化差分隐私（Centralized Differential Privacy，简称CDP，适用于数据管理者可信的场景）模式，以中间件的形式接收SQL统计查询请求，返回满足差分隐私的查询结果。一个典型的查询请求处理流程如下：

* **·**首先，核心服务接受客户提交的SQL查询语句，对该语句进行解析和重写，以便于计算隐私噪声(如将AVG计算改为SUM/COUNT）；
* **·**然后，核心服务调用元数据管理服务，计算重写后的SQL查询所对应的数据表敏感度，同时在数据库上执行重写后的SQL查询，得到原始的查询结果；
* **·**最后，核心服务调用隐私预算管理服务得到为该查询分配的隐私预算，并结合敏感度在原始的查询结果中添加噪声并返回。

![]()

## 2.2 Jeddak-DPSQL解决的问题

### 案例背景

假设有一个数据库 business，存储用户消费数据，使用 clickhouse 引擎，其中一个表 user 存储用户信息，表中存在以下列：uid，name，age，sex，city，代表用户id、姓名、年龄、性别、城市。

### 查询需求

我们要查询用户数量和平均年龄的城市分布，使用 SQL 语句 1：

```
SELECT  COUNT(*) AS cnt，AVG(age) as agev, city
FROM business.user
group by city
```

### 风险

如果不应用隐私保护技术，可能面临差分攻击的风险，比如攻击者通过某渠道得知张三的 uid 为 803719，构造下面的 SQL 语句 2：

```
SELECT  COUNT(*) AS cnt，AVG(age) as agev, city
FROM business.user
WHERE uid != 803719
group by city
```

通过执行上面的 SQL语句1 和 SQL 语句2，可分别得到两个查询结果：

![]()

那么就可以通过比较两次查询结果得知张三所在的城市是北京，年龄大约 61 岁（120008*49.3276 = 5919706.62，120007*49.3275 = 5919645.29，5919706.62 – 5919645.29 约等于 61）

以上是一个简单的例子，现实场景中，攻击者可能通过背景知识构造更多样、更复杂的查询语句达到窃取隐私的目的。

因此，在上述SQL查询场景下，可以通过接入Jeddak-DPSQL对SQL进行分析和重写，最终执行重写后的SQL能够保证返回给使用者的数据满足差分隐私要求，进而达到对个人隐私保护的效果。

## 2.3 Jeddak-DPSQL在火山引擎的应用验证

1. 1、Jeddak-DPSQL已接入火山引擎的增长分析（finder)、A/B 测试等产品，间接服务300+外部客户，日均处理查询请求 200+。Jeddak-DPSQL服务不仅帮助业务满足了隐私保护和业务合规的需求，同时也成为创新型隐私计算技术应用的典范案例。
2. 2、开放隐私计算OpenMPC对外公布了“隐私计算2021年度优秀应用案例TOP10”。火山引擎云安全凭借“融合差分隐私的火山引擎DPSQL服务”案例，成功入选TOP10。

# 三、如何使用Jeddak-DPSQL

git 开源项目地址：<https://github.com/bytedance/Jeddak-DPSQL>

## 1. 下载

git clone <https://github.com/bytedance/Jeddak-DPSQL>

## 2. 快速部署

完成Jeddak-DPSQL下载后，按照README中的部署引导部分完成服务部署，整个部署过程包括以下步骤：

* **·**服务依赖包安装：进入项目根目录，使用pip install -r requirements.txt安装服务所需完整pip包
* **·**MetaData存储准备：在使用DPSQL时，需要维护源数据表的MetaData信息，为后续加噪计算敏感度作准备。Jeddak-DPSQL使用Mysql对相应元数据信息进行存储，因此需要用户提前在自己的Mysql数据库中创建相应的表
* **·**隐私预算消耗存储准备：使用Jeddak-DPSQL系统过程，可以记录对表级别的数据查询时的隐私预算消耗。主要通过Mysql进行记录，因此需要用户提前在自己的Mysql数据库中创建相应的表
* **·**数据库连接配置：Jeddak-DPSQL中使用数据库主要有Mysql和Redis，因此需要对这两个数据库连接地址进行配置
* **·**服务启动：完成上述配置后可以在项目根目录运行bootstrap.sh脚本启动服务

## 3. 正式使用

完成Jeddak-DPSQL部署后，按照README中的快速开始部分可以进行功能体验，整个过程如下：

* **·**选择要测试的数据源(Hive或ClickHouse)，导入要进行查询测试的原始数据集
* **·**初始化metadata和隐私预算
  + **·**生成 metadata
    启动dpsql服务后， 调用接口 /api/v1/metadata/generate，生成metadata，可参考：

```
def meta_generate():
  args = {
      "db_config": {
          "host": <hive_host>,
          "database": <hive_dbname>,
          "username": <hive_username>,
          "password": <hive_password>
      },
      "table_name": "us_accidents_dec21_updated",
      "db_type": db_type
  }
  route_path = "/api/v1/metadata/generate"# local service,  host:127.0.0.1, port:5000url = "http://%s:%s/%s" % (host, port, route_path)
  headers = {"content-type": "application/json"}
  r = requests.post(url, json=args, headers=headers)

if __name__ == '__main__':
   meta_generate()
```

* 确认metadata 生成完成
  调用 /api/v1/metadata/get 接口，确认 metadata 生成完成

```
def meta_get():
    args = {
        "prefix": <hive_host>,
        "db_name": <hive_dbname>,
        "table_name": "us_accidents_dec21_updated"
    }
    route_path = "/api/v1/metadata/get"# local service,  host:127.0.0.1, port:5000url = "http://%s:%s/%s" % (host, port, route_path)
    headers = {"content-type": "application/json"}
    r =  requests.get(url, json=args, headers=headers)
    print(r.text)
```

调用隐私保护查询接口，获得经过差分隐私保护的查询结果

```
def query_sql_noise(sql, data_source):
      key = {
          "sql": sql,
          "dbconfig": {
              "reader": data_source,
              "host": <hive_host>,
              "database": <hive_dbname>,
              "port": <hive_port>
          },
          "queryconfig": {
             "traceid": "traceid",
          }
      }
      route_path = "/api/v1/query"url = "http://%s:%s/%s" % (host, port, route_path)
      headers = {"content-type": "application/json"}
      r = requests.post(url, json=key, headers=headers)
      return resif __name__ == "__main__":
      sql = "select count(severityc) from menu_page group by severity"
      section = "hivereader"
      res = query_sql_noise(sql, section)
      print(res)
```

更多接口使用方式可以参考项目README中的API Documentation部分

# 四、后续计划

由于当前是Jeddak-DPSQL的首个开源版本，因此还存在很多不完善的地方，希望大家能够多多谅解。Jeddak-DPSQL计划进行长期维护，欢迎大家使用，也希望有更多的外部开发者能够一起对该开源项目进行共建，完善产品功能，构建更完备的应用生态。

# 五、关于安全研究

火山引擎安全研究部门的愿景是创新突破前沿安全理论技术，赋能数字经济。部门当前以可信隐私计算产品Jeddak为载体，从可信计算、联邦学习、多方安全计算、差分隐私、密文计算、共识计算等方向着手，开展隐私计算技术的前沿研究和应用探索。基于这些领域最新前沿理论技术，创新研发、突破瓶颈，实现数据全生命周期安全与隐私保护，以及可信隐私计算等应用服务落地：赋能业务、保驾护航；更进一步打破数据孤岛，推动数据多源融合与流通交易，发挥数据价值。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**火山引擎云安全**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/288888](/post/id/288888)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [数据保护](/tag/%E6%95%B0%E6%8D%AE%E4%BF%9D%E6%8A%A4)
* [差分隐私](/tag/%E5%B7%AE%E5%88%86%E9%9A%90%E7%A7%81)
* [隐私计算](/tag/%E9%9A%90%E7%A7%81%E8%AE%A1%E7%AE%97)

**+1**11赞

收藏

![](https://p3.ssl.qhimg.com/t01d7c5cb6fdb04a6cc.png)火山引擎云安全

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t01d7c5cb6fdb04a6cc.png)](/member.html?memberId=165382)

[火山引擎云安全](/member.html?memberId=165382)

火山引擎云安全产品是字节跳动旗下的企业级安全技术服务产品

* 文章
* **40**

* 粉丝
* **4**

### TA的文章

* ##### [为AI Agent行为立“规矩”——字节跳动提出Jeddak AgentArmor智能体安全框架](/post/id/312426)

  2025-09-28 13:43:32
* ##### [教你打造一款AI安全助手 | 安全MCP的实践指南](/post/id/311884)

  2025-09-05 10:40:51
* ##### [当数字世界的“万能钥匙”被滥用，谁来守护核心资产？火山的 MCP 安全授权新范式](/post/id/311597)

  2025-08-28 09:50:41
* ##### [广汽集团×火山引擎：出海合规助力企业新增长](/post/id/311498)

  2025-08-26 10:17:09
* ##### [智能体防御 | 一文了解3种系统提示词加固方法](/post/id/311279)

  2025-08-18 16:34:50

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

### 热门推荐

文章目录

* [2.1 Jeddak-DPSQL介绍](#h2-0)
* [2.2 Jeddak-DPSQL解决的问题](#h2-1)
  + [案例背景](#h3-2)
  + [查询需求](#h3-3)
  + [风险](#h3-4)
* [2.3 Jeddak-DPSQL在火山引擎的应用验证](#h2-5)
* [1. 下载](#h2-6)
* [2. 快速部署](#h2-7)
* [3. 正式使用](#h2-8)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5....