---
title: Windows提权基础
url: https://www.secpulse.com/archives/189368.html
source: 安全脉搏
date: 2022-10-20
fetch_date: 2025-10-03T20:20:51.027577
---

# Windows提权基础

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

# Windows提权基础

[Windows](https://www.secpulse.com/archives/category/articles/system/windows)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-10-19

42,863

# 前置基础

提权条件提权不是在任何情况下都可以进行的，它有一定的前置条件，例如拥有内网普通用户权限、拥有WebShell、拥有FTP权限、拥有某些远程管理软件的账号和密码等，同时在本地或者远程服务器上存在相应的漏洞。当然，最重要的条件是拥有利用该漏洞的工具、代码或者程序！

## 基础信息查询

* • Administrators：管理员组，默认情况下，Administrators中的用户对计算机/域有不受限制的完全访问权
* • Power Users：高级用户组Power Users可以执行除了为Administrators组保留的任务外的其他任何操作系统任务
* • Users：普通用户组,这个组的用户无法进行有意或无意的改动
* • Guests：来宾组,来宾跟普通Users的成员有同等访问权，但来宾帐户的限制更多
* • Everyone：所有的用户，这个计算机上的所有用户都属于这个组

## 提权名称解释

**注册表**

注册表（Registry，繁体中文版Windows操作系统称之为登录档案）是Microsoft   Windows中的一个重要的数据库，用于存储系统和应用程序的设置信息。其中存放着各种参数，直接控制着Windows的启动、硬件驱动程序的装载以及一些Windows应用程序的运行，从而在整个系统中起着核心作用。这些作用包括了软、硬件的相关配置和状态信息，比如注册表中保存有应用程序和资源管理器外壳的初始条件、首选项和卸载数据等，联网计算机的整个系统的设置和各种许可，文件扩展名与应用程序的关联，硬件部件的描述、状态和属性，性能记录和其他底层的系统状态信息，以及其他数据等。

**计划任务**

计划任务是系统的常见功能，利用任务计划功能，可以将任何脚本、程序或文档安排在某个最方便的时间运行。任务计划在每次系统启动的时候启动并在后台运行；攻击者可以通过计划任务程序来运行准备好的恶意脚本、批处理文件夹、病毒程序、payload命令，使其在某个特定的时间运行，达到系统提权的目的。

**组策略**

Windows  2008  Server引入了一项新功能：策略首选项，组策略首选项使管理员可以部署影响域中计算机/用户的特定配置，通过在组策略管理控制台中配置的组策略首选项，管理员可以推出多种策略，例如，当用户登录其计算机时自动映射网络驱动器，更新内置管理员帐户的用户名或对注册表进行更改。

## 基础信息查询命令

```
#主机名
hostname
#查看系统名
wmic os get caption
#查看系统信息
systeminfo
#环境变量
set
#查看用户信息
net user
#查看当前安装程序
wmic product get name,version
#查看正在运行的进程列表
tasklist /svc | find "TermService"
#查看服务PID
netstat -and | find "1448"
#查看具体补丁信息
wmic qfe get Description,HotFixID,InstalledOn | findstr /C:"KBxxxxx" /C:"KBxxxxx"
```

## 查看目标重要配置命令

```
#查看系统版本
C:boot.ini
#IIS配置文件
C:WindowsSystem32inetsrvMetaBase.xml
#存储系统初次安装的密码
C:Windowsrepairsam
#Mysql配置
C:Program Filesmysqlmy.ini
#Mysql root
C:Program Filesmysqldatamysqluser.MYD
#php配置信息
C:Windowsphp.ini
#Mysql配置信息
C:Windowsmy.ini
#Windows系统的一个基本系统配置文件
C:Windowswin.ini
```

# Windows提权

## 内核提权

1.Win账号和密码的获取与破解

Windows账号和密码的获取主要针对获取了系统权限的情况，例如目标端口开放3389的情况；还有一种情况，就是通过提权0day执行其他可执行程序

2.通过执行`wce-w`命令（Windows Credientials Editor）直接获取系统登录过的账号明文。

Windows  Credentials Editor  （WCE）是一款功能强大的Windows平台内网渗透工具，它能列举登录会话，并且可以添加、改变和删除相关凭据（例如LM/NTHash）。这些功能在内网渗透中能够被利用，例如，在Windows平台上执行绕过Hash操作或者从内存中获取NT/LM  Hash  （也可以从交互式登录、服务、远程桌面连接中获取）以用于进一步的攻击，而且体积也非常小，是内网渗透时的必备工具。不过必须在管理员权限下使用，还要注意杀毒工具的免杀。

本地存储的凭证是否有可利用的`cmdkey /list`查询当前存储的凭证；以存储凭证的用户执行命令`runas /savecred /user:JIUSHI-PCjiushi ""`

查看目标补丁

```
//获取补丁信息
systeminfo或者systeminfo | findstr KB
Wmic qfe get Caption,Description,HotFixID,InstalledOn
//获取系统版本信息
systeminfo | findstr OS
```

* • windows exploit suggester（GitHub项目链接）
* • powershell中的sherlock脚本（GitHub项目链接）
* • 在线辅助查询补丁特征&&杀毒软件识别网站（网站链接）

## 数据库提权

攻击者可以通过SQL注入数据库获取数据库账号密码后，可以查看数据库配置文件（data、sql、inc、config、conn、database.....）和数据库安装文件（安装目录下**data/mysql/user.myd**）

frm：描述表结构文件，字段长度

myi：索引信息

myd：数据库信息文件，存储数据信息

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189368-1666158048.png "null")

### Mysql数据库udf提权

提权原理：

已知root账号和密码，利用root权限创建可以调用cmd函数的udf.dll，当我们把udf.dll文件导出指定文件夹引入数据库的时候，其中的调用函数可以拿出来当作mysql函数来使用

udf文件：udf(即user-defined-function)是数据库的一个拓展接口，也称为用户自定义函数，用户通过自定义函数来实现在mysql中无法方便实现得功能（udf文件后缀名: .dll（windows）linux后缀名：.so）

提权条件：

Mysql版本<5.1版本的情况：udf.dll文件在Windows2003中放在：c:windowssystem32，在Windows2000中放在：c:winntsystem32。Mysql版本>5.1版本的情况：udf.dll文件必须放置在数据库安装目录下的libplugin（但是大于5.1版本的时候没有plugin这个文件夹，需要攻击者自己创建）

### Mysql数据库反射端口提权

* • 获取数据库的账号和密码，同时能够执行查询命令
* • secure\_file\_priv=,可导出udf.dll到系统目录或者mysql数据库安装目录下的lib下plugin
* • 授权Mysql数据库远程用户的登录

### Mysql数据库启动项提权

提权原理：使用mysql写文件，写一段vbs代码到开启自启动中；服务器重启的时候达到创建用户并提取（为了达到效果，可以尝试使用DDOS攻击迫使服务器重启）！

提权条件

* • secure\_file\_priv不为null
* • 已知账号和密码

### Mysql数据库mof提权

提权原理：mof文件是Mysql数据库的扩展文件，其存放路径c:/windows/system32/wbem/mof/nullevt.mof（它的作用是每隔5秒就会去监控进程创建和死亡），它就是利用了c:/windows/system32/wbem/mof目录中的nullevt.mof文件，每分钟都会在一个特定的时间去执行一次的特性，来写入我们的cmd命令使其被带入执行（有点像条件竞争）。

提权条件:

* • Windows2003及以下版本
* • secure-file-priv=不为null
* • mysql启动身份具有权限去读写C:/windows/system32/wbem/mof/目录

### SQLServer数据库xp\_cmdshell提权

提权原理：

xp\_cmdshell是sqlserver中的组件，可以以操作系统命令解释器的方式执行给定的命令字符串，并以文本行方式返回任何输出。可以用来执行系统命令

提权条件:

默认在sql server2000中是开启的，可以直接利用！默认在sqlserver2005之后的版本默认禁止，但是如果我们有sa权限，可以用命令开启！

## 权限问题导致提权

### 计划任务提权

如果我们对以高权限运行的任务所在目录具有写入权限，就可以使用恶意程序覆盖掉原来的程序。当计划任务下次执行时，就会以高权限运行恶意程序，进而完成提权攻击。

**at命令**

计划任务提权

```
at 17:51 cmd.exe
```

使用at的已经计划的命令作为后台程序运行。但是只适用于win7和winsrver2008，而且需要管理员权限才可以，成功执行。）所以个人感觉没有太大用处，你都可以使用Admin权限了，再用at去提权没有意义了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189368-1666158049.png "null")

**schtasks 命令**

查看服务状态

```
schtasks /Query /TN MyService2
```

有时候会报错无法加载列资源, 这是由于cmd编码是gbk导致的, 调整为美国编码 (此时无法打印非Ascii字符) 即可。

创建服务, 以 system 权限启动

```
schtasks /Create /TN MyService2 /SC DAILY /ST 10:00:00 /TR cmd.exe /RU SYSTEM
```

删除服务

```
schtasks /Delete /TN MyService2 /F
```

注意：该命令支持win7到win10, 借助工具才能看到 ！

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189368-1666158051.png "null")

**SC提权**

SC命令是Windows系统中功能强大的DOS命令，它能与"服务控制器"和已安装设备进行通讯；主要用于与服务控制管理器和服务进行通信的命令行程序。

```
sc Create MyService binPath= "cmd /c start" type= own type= interact
sc start MyService
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189368-1666158052.png "null")

注：该提权方法可以在XP系统环境下直接提权，Win7环境中需要将EnableLUA的值改为0，最后重启电脑，再次执行.bat文件（文件下载地址），后点击查看消息即可。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189368-1666158055.png "null")

### 注册表提权

**注册表键AlwaysInstallElevated提权**

AlwaysInstallElevated是一项功能，可为Windows计算机上的所有用户（尤其是低特权用户）提供运行任何具有高权限的MSI文件的功能。MSI是基于Microsoft的安装程序软件包文件格式，用于安装、存储、删除程序。通过组策略中的windows  installer来进行配置，默认情况下该配置是关闭的。

使用Perfusion注册表提权工具进行windows提权：版本范围是在Wi...