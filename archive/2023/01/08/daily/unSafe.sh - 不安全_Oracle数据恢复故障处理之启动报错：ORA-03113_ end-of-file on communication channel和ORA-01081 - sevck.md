---
title: Oracle数据恢复故障处理之启动报错：ORA-03113: end-of-file on communication channel和ORA-01081 - sevck
url: https://buaq.net/go-144550.html
source: unSafe.sh - 不安全
date: 2023-01-08
fetch_date: 2025-10-04T03:18:52.660609
---

# Oracle数据恢复故障处理之启动报错：ORA-03113: end-of-file on communication channel和ORA-01081 - sevck

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Oracle数据恢复故障处理之启动报错：ORA-03113: end-of-file on communication channel和ORA-01081 - sevck

lsnrctl启动实例startup报错ORA-03113: end-of-file on communication channel$ su - oracleStep 1: You ne
*2023-1-7 11:47:0
Author: [www.cnblogs.com(查看原文)](/jump-144550.htm)
阅读量:15
收藏*

---

lsnrctl启动实例startup报错

ORA-03113: end-of-file on communication channel

```
$ su - oracle
```

Step 1: You need to look at the alert log. It isn't in /var/log as expected. You have to run an Oracle log reading program:

```
$ adrci
ADRCI: Release 11.2.0.1.0 - Production on Wed Sep 11 18:27:56 2013
Copyright (c) 1982, 2009, Oracle and/or its affiliates. All rights reserved.
ADR base = "/u01/app/oracle"
adrci>
```

Notice the ADR base. That is not the install. You need to see the homes so you can connect to the one that you use.

```
adrci> show homes
ADR Homes:
diag/rdbms/cci/CCI
diag/tnslsnr/cci/listener
diag/tnslsnr/cci/start
diag/tnslsnr/cci/reload
```

CCI is the home. Set that.

```
adrci> set home diag/rdbms/cci/CCI
adrci>
```

Now, you can look at the alert logs. It would be very nice if they were in /var/log so you could easily parse the logs. Just stop wanting and deal with this interface. At least you can tail (and I hope you have a scrollback buffer):

```
adrci> show alert -tail 100
```

Scroll back until you see errors. You want the FIRST error. Any errors after the first error are likely being caused by the first error. In my case, the first error was:

```
ORA-19815: WARNING: db_recovery_file_dest_size of 53687091200 bytes is 100.00% used, and has 0 remaining bytes available.
```

This is caused by transactions. Oracle is not designed to be used. If you do push a lot of data into it, it saves transaction logs. Those go into the recovery file area. Once that is full (50GB full in this case). Then, Oracle just dies. By design, if anything is messed up, Oracle will respond by shutting down.

There are two solutions, the proper one and the quick and dirty one. The quick and dirty one is to increase db\_recovery\_file\_dest\_size. First, exit adrci.

```
adrci> exit
```

Now, go into sqlplus without opening the database, just mounting it (you may be able to do this without mounting the database, but I mount it anyway).

```
$ sqlplus /nolog
SQL*Plus: Release 11.2.0.1.0 Production on Wed Sep 11 18:40:25 2013
Copyright (c) 1982, 2009, Oracle. All rights reserved.
SQL> connect / as sysdba
Connected.
SQL> startup mount
```

Now, you can increase your current db\_recovery\_file\_dest\_size, increased to 75G in my case:

```
SQL> alter system set db_recovery_file_dest_size = 75G scope=both
```

Now, you can shutdown and startup again and that previous error should be gone.

The proper fix is to get rid of the recovery files. You do that using RMAN, not SQLPLUS or ADRCI.

```
$ rman
Recovery Manager: Release 11.2.0.1.0 - Production on Wed Sep 11 18:45:11 2013
Copyright (c) 1982, 2009, Oracle and/or its affiliates.  All rights reserved.
RMAN> backup archivelog all delete input;
```

```
SQL> startup nomount
ORACLE 例程已经启动。

Total System Global Area 8317743104 bytes
Fixed Size                  2192296 bytes
Variable Size            4261416024 bytes
Database Buffers         4043309056 bytes
Redo Buffers               10825728 bytes
SQL> select group#,status from v$log;
select group#,status from v$log
                          *
第 1 行出现错误:
ORA-01507: ??????

SQL> select group#,status from v$log;
select group#,status from v$log
                          *
第 1 行出现错误:
ORA-01507: ??????
SQL> shutdown immediate
ORA-01507: ??????
ORACLE 例程已经关闭。
SQL> startup;
ORACLE 例程已经启动。

Total System Global Area 8317743104 bytes
Fixed Size                  2192296 bytes
Variable Size            4261416024 bytes
Database Buffers         4043309056 bytes
Redo Buffers               10825728 bytes
数据库装载完毕。
数据库已经打开。
SQL> select name from V$datafile;

NAME
--------------------------------------------------------------------------------
E:\APP\ORADATA\ORCL\SYSTEM01.DBF
E:\APP\ORADATA\ORCL\SYSAUX01.DBF
E:\APP\ORADATA\ORCL\UNDOTBS01.DBF
E:\APP\ORADATA\ORCL\USERS01.DBF
E:\APP\ORADATA\ORCL\EXAMPLE01.DBF

SQL> select group#,status from v$log;

    GROUP# STATUS
---------- ----------------
         1 INACTIVE
         2 CURRENT
         3 INACTIVE

SQL>
```

【版权所有@Sevck 博客地址http://www.cnblogs.com/sevck】 可以转载，注明出处.

文章来源: https://www.cnblogs.com/sevck/p/17032422.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)