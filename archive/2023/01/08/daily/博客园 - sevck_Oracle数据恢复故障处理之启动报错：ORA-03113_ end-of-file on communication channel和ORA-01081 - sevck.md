---
title: Oracle数据恢复故障处理之启动报错：ORA-03113: end-of-file on communication channel和ORA-01081 - sevck
url: https://www.cnblogs.com/sevck/p/17032422.html
source: 博客园 - sevck
date: 2023-01-08
fetch_date: 2025-10-04T03:18:01.815800
---

# Oracle数据恢复故障处理之启动报错：ORA-03113: end-of-file on communication channel和ORA-01081 - sevck

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/sevck/)

# [Sevck's Blog](https://www.cnblogs.com/sevck)

## 关注互联网安全，软件开发，这里记录着我的渗透心得、开发文摘、随笔心情(Linux,Windows,Python,Java.Lua,JS,C++在学习)。JAVA安全网:https://www.javasec.cn

* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* 订阅
* [管理](https://i.cnblogs.com/)

# [Oracle数据恢复故障处理之启动报错：ORA-03113: end-of-file on communication channel和ORA-01081](https://www.cnblogs.com/sevck/p/17032422.html "发布于 2023-01-07 11:46")

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

posted @
2023-01-07 11:46
[sevck](https://www.cnblogs.com/sevck)
阅读(559)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202508/35695-20250830121216742-1062949948.jpg)](https://developer.huawei.com/consumer/cn/activity/digixActivity/digixcmsdetail/101750143863263087?ha_source=BKYQ3&ha_sourceId=89000408)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025

[![](//assets.cnblogs.com/images/ghs.png)浙公网安备 33010602011771号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)