---
title: sql注入学习分享
url: https://www.secpulse.com/archives/194877.html
source: 安全脉搏
date: 2023-01-13
fetch_date: 2025-10-04T03:43:12.373137
---

# sql注入学习分享

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# sql注入学习分享

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[hackctf](https://www.secpulse.com/newpage/author?author_id=34005)

2023-01-12

15,983

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194877-1673504790.jpeg)

本文为看雪论坛精华文章

看雪论坛作者ID：xi@0ji233

#

```
一

WEB框架
```

web应用一改我们平时常见的 p2p 和 C/S 模式，采用 B/S 模式。随着网络技术的发展，特别随着Web技术的不断成熟，B/S 这种软件体系结构出现了。浏览器-服务器（Browser/Server）结构，简称 B/S 结构，与 C/S不同，其客户端不需要安装专门的软件，只需要浏览器即可，浏览器与Web服务器交互，Web服务器与后端数据库进行交互，可以方便地在不同平台下工作。

比如我们玩的英雄联盟就是典型的 C/S 结构的服务，因为有大量图片资源和 3D 模型存储在本地，因此提前安装好客户端就可以方便地与服务器进行交互，如果采用 B/S 结构的话，在我们游戏开始的时候就要与服务器建立连接，下载好各种资源到本地，然后再与服务器进行交互，各种页游均是 B/S 结构。B/S 的优势就是对需要服务一方的电脑要求较低，很容易可以兼容系统上的差异，客户往往只需要安装浏览器便可以享受全部的 web 服务。web 应用会先向我们的浏览器发送前端语言 javascript 或者 html 给浏览器解析执行，我们经过一定的操作之后会向服务器发送请求，然后服务器根据我们的请求做出不同的答复，这个答复还是前端语言形成的网页。

服务器会根据什么规则去响应请求，这个就要用到后端语言了，如 php,aspx 等都是常见的后端语言，现在以 php 为主。比如我们实现一个登录页面，那么这个登录肯定是会用到数据库查询操作的，我们将请求提交给服务器之后，后端语言得到我们发送的数据，然后后端语言就会相应地构造 sql 语句去执行数据库查询，并根据查询结果来响应我们

那么我们很清晰了，我们负责发送数据，php 构造 sql 语句去查询。首先明白一点，sql 语句肯定我们能控制，因为我输入什么它就要去查什么。我们的输入一定会被嵌入 sql 语句。如果我们在 sql 中能输入任意内容，那我就相当于直接控制了整个数据库。sql 注入的就这么产生了，带来的本质危害也就是数据库信息泄露，如果数据库配置权限过高甚至能让攻击者拿到 shell。

##

```
二

sql语言
```

SQL(Structured Query Language，结构化查询语言)是一种特定目的程式语言，用于管理关系数据库管理系统（RDBMS），或在关系流数据管理系统（RDSMS）中进行流处理。

SQL基于关系代数和元组关系演算，包括一个数据定义语言和数据操纵语言。SQL的范围包括数据插入、查询、更新和删除，数据库模式创建和修改，以及数据访问控制。尽管SQL经常被描述为，而且很大程度上是一种声明式编程（4GL），但是其也含有过程式编程的元素。(from wiki)

我们最常用的数据库系统是mysql。

```
三

Mysql常用函数
```

###

### 数据库基本信息函数

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194877-1673504791.png)

###

###

### 注意，这些函数都无参数且在使用时必须使用 select 关键字输出。

### 字符串处理函数

在sql中，字符串通常使用一对单引号表示。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194877-16735047911.png)

sql注入常用函数

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194877-1673504792.png)

```
四

Mysql内置数据库
```

Mysql：保存账户信息，权限信息，存储过程，event，时区等信息。

sys：包含了一系列的存储过程、自定义函数以及视图来帮助我们快速的了解系统的元数据信息。（元数据是关于数据的数据，如数据库名或表名，列的数据类型，或访问权限等）

performance\_schema：用于收集数据库服务器性能参数。

information\_schema：它提供了访问数据库元数据的方式。其中保存着关于MySQL服务器所维护的所有其他数据库的信息。如数据库名，数据库的表，表的数据类型与访问权限等。

这里看似很复杂，实际上你只需要知道这个 performance\_schema 数据库就可以了。对于一个未知的数据库，我们首先需要知道它的数据库名，数据表名，知道表名之后还得知道字段名，这样我们才能使用类似这样的 sql 语句 select 字段名 from 数据库.表名; 去泄露数据库的具体信息。

我们 navicat 打开这个数据库观察一下有什么表。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194877-16735047921.png)

看着很多，其实我们只需要关心三个表：schemata，tables，columns，它们分别能爆出数据库名，表名和字段名。

我们先看看第一个表 schemata 的具体信息：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194877-1673504794.png)

可以看到里面的schema\_name 字段的值就是我们当前这个数据库系统中所有的数据库的名字，从左边也可以一一对应看到对应的数据库。

然后看看第二个表 tables 的信息。因为有点多我们看主要的：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194877-1673504796.png)

可以看到里面有一个 table\_name 字段就是整个数据库系统的所有表名，然后前面的 table\_schema 就是这个表对应的数据库名。这里也可以看到我们这个数据库能从中找到 tables 和 schemata 这两个表名，以及其它乱七八糟的在上一张图也都有显示。

```
五

获得数据库信息的其它方式
```

在我们有一个 mysql 连接的情况下，我们想查看所有的数据库很简单，一句 show databases; 即可解决，但是通常情况下我们这样子输入并不能很好的回显，如果把数据库名作为一条记录输出出来那处理起来会好很多。

我们想查看数据库还可以用这种方式：

select schema\_name from information\_schema.schemata;

我们对比一下两个指令的结果。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194877-1673504799.png)

可以看到结果基本就是一样的。然后我们想查看比如说 world 数据库的表名，我们一般先 use world 再 show tables 或者一句话 show tables from world; 直接输出表名，但是有 information\_schema 这个数据库，我们就能通过这里把信息显示出来。

select table\_name from information\_schema.tables where table\_schema='world';

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194877-16735047991.png)

可以看到结果也是一模一样的。

剩下的爆字段就不演示了，同理的。

select column\_name from information\_schema.columns where table\_name='city';

以上的 payload 可以直接在注入的地方加进去，只需要改一下表名和数据库名即可。

```
六

sqli-labs环境搭建
```

主要学习的环境还是用的 sqli-labs ，我是直接在主机上搭建，因为修改代码起来十分方便，一改就能见到效果。但是这么做确保切断了对外界的网络连接，或者心大一点就算了，想着没人会对自己的主机发起进攻的。

然后自己再搭建一个 web 服务，能访问就算成功了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194877-1673504800.png)

在使用之前在 sqli-labssql-connections 目录下的 db-creds.inc 中配置一下自己的用户名和密码，再点击 setup 把数据库先配置好，如果一切OK，那么进入第一关的效果应该是这样的：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194877-1673504801.png)

##

```
七

sql注入详解
```

在对一个 ctf 打 sql 注入的时候，我们第一步就是要寻找注入点。怎么寻找注入点呢，因为后端源码我们都是不知道的，所以我们只能通过抓包的方式观察所有能提交的参数进行 sql 注入的测试。

找到注入点之后我们还需要判断注入的类型。大体的注入分两类，一类是有回显的注入，另一类是没有回显的注入。一般情况下我们优先考虑有回显的注入，因为时间成本比较低，那么我们先来看看有回显的注入吧。

### 有回显的注入

什么叫有回显？查询到的数据库信息会直接显示出来，你能看到的就叫有回显，反之则是没有回显。有回显的注入有以下类型：

1、联合查询的注入：通过union关键字泄露数据库信息。

2、堆叠注入：通过重新执行一个 sql 语句的方式泄露数据库信息，或者直接增删改查数据库。

3、报错注入：通过一些特殊的函数报错把信息显示出来。

4、二次注入：咕咕咕。

####

#### 联合查询的注入

利用要求：有回显

假如你是 admin 登录之后，它页面可能会显示 hello,admin。那么这个 hello 后面就是一个回显的点，这里就可以用来泄露其它信息。这里需要怎么理解呢，假如它在登录的逻辑是这样写的：

select username,passowrd from data.user where username='$input\_username' and password='$input\_password';

然后我们判断你的账号密码是否正确就主要看它是否能查找到记录，如果找到，那么我选取这条记录的第一个记录的 username 字段，然后输出这个，就达到了它成功登录了什么账号，我输出那个账号的目的了。

至于上面为什么说是第一条记录呢，这里你需要这么看：select 的返回结果可能有很多，而不管它返回了一条还是多条它都是一个数据集，是个二维的表。因此选择第一条记录是开发人员默认会加上的，此时我只需使得前面的语句查询失败（返回空数据集）并选取其它内容用 union 合并这个数据集，并把这里的其它内容替换成我想知道的内容，比如它的数据库名，表名，然后它这里就会原样输出这些信息了，我们就知道了。这里需要知道 union 是合并两个数据集的，因此两个数据集的宽度（字段数）必须一样，数据类型可以不一样，返回 php 处理之后都会变成字符串类型其实。

这里我们拿刚刚搭建的环境的第一关来做测试：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194877-1673504802.png)

这里我们不需要寻找测试点了，它这里已经贴心地提醒我们用 get 传一个 id 参数进去了，因此我们先试 1。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194877-1673504803.p...