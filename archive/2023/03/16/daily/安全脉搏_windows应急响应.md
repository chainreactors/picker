---
title: windows应急响应
url: https://www.secpulse.com/archives/197547.html
source: 安全脉搏
date: 2023-03-16
fetch_date: 2025-10-04T09:44:41.362481
---

# windows应急响应

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

# windows应急响应

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-03-15

13,098

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197547-1678846112.png)

# windos分析排查-文件分析

## 分析排查介绍

分析排查是指对windows系统中的文件、进程、系统信息、日志记录等进行检查。查看windows系统中是否有运行异常的情况。主要目的在于保护windows系统的安全。

## 0x01 开机启动文件

一般情况下，被植入的木马病毒、恶意文件恶意程序等都会在计算机启动时自启动运行。

在windows中可通过以下三种方式查看开机启动项：

1.利用操作系统中的启动菜单

```
C:UsersAdministratorAppDataRoamingMicrosoftWindowsStartMenuProgramsStartup
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197547-1678846113.png "null")

2.利用系统配置msconfig

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197547-1678846114.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197547-1678846115.png "null")

3.利用注册表regedit

```
计算机HKEY_CURRENT_USERSOFTWAREMicrosoftWindowsCurrentVersionRun
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197547-1678846116.png "null")

```
计算机HKEY_LOCAL_MACHINESOFTWAREWOW6432NodeMicrosoftWindowsCurrentVersionRun
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197547-1678846117.png "null")

## 0x02 temp临时异常文件

temp临时文件夹，位于C:Document and SettingsAdministratorLocal Settings内。很多文件放在这里，用来收藏夹，浏览网页的临时文件，编辑文件等。

在运行输入%temp%可直接打开temp文件夹。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197547-1678846118.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197547-1678846119.png "null")

排查对象：查看temp文件夹PE文件（exe、dll、sys），或者是否具有特别大的tmp文件。

相关可疑文件可上传到云沙箱进行在线分析。

https://www.virustotal.com/gui/home/upload

https://x.threatbook.com/

https://ti.360.cn/#/homepage

为什么要排查Temp文件夹？

使用Temp文件夹有几个优点。在某些系统中，Temp文件夹位于RAM DISK上。与通常的磁盘文件系统相比，写入操作和文件操作要快的很多。

另一个优点是Temp文件夹对当前登录的用户具有读写访问权限，从而解决了恶意软件安装程序在没有适当权限的情况下尝试将恶意软件安装在目标位置时出现的任何文件系统权限错误。一旦恶意软件安装程序或恶意软件本身具有升级的特权，Temp文件夹通常用作暂存点。

操作系统还具有清理Temp文件夹中临时文件的不完整写入的优点，因此在恶意软件安装失败的情况下，操作系统负责删除文件的任何痕迹，从而防止恶意软件的任何部分或版本损坏它的主要可执行文件。所以恶意软件安装程序通常在恶意软件感染期间利用TMP文件和Windows Temp文件夹。

## 0x03 浏览器分析

服务器被攻击者拿下后，攻击者可能会使用服务器的浏览器进行访问网站，进行一系列下载操作。因此我们可以查看浏览器记录，排查浏览器是否被使用下载恶意代码。

1.浏览器浏览痕迹查看

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197547-1678846121.png "null")

2.浏览器文件下载记录查看

3.浏览器cookie信息查看

浏览器记录查看工具：https://launcher.nirsoft.net/downloads/index.html

## 0x04 文件时间属性分析

在windows系统下，文件属性的时间属性具有：创建时间、修改时间、访问时间。默认系统以修改时间作为展示。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197547-1678846124.png "null")

如果文件的修改时间早于创建时间这个文件存在可疑，异常的时间很有可能是攻击者进行恶意修改的不正常文件。

## 0x05 最近打开文件

Windows系统中默认记录系统中最近打开使用的文件信息。

可以在目录`C:Documents and SettingsAdministratorRecent`下查看

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197547-1678846125.png "null")

也可以使用Win+R打开运行后输入`%UserProfile%Recent`查看。然后利用Windows中的筛选条件查看具体时间范围的文件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197547-1678846127.png "null")

## 0x06 可疑进程发现与关闭

计算机与外部忘了通信是建立在TCP/UDP协议上的，并且每一次通信都是具有不同的端口（0-65535）。在计算机中木马病毒后，木马运行会与外部忘了进行通信，那么就可以通过查看忘了连接状态，找到对应的进程ID，然后关闭进程ID进行断开木马的通信连接。

使用如下相关命令进行排查：

```
netstat -ano | find "ESTABLISHED"  查看网络建立连接的状态
tasklist /svc | find "PID" 查看具体PID进程对应的程序
taskkill /PID xxx /T 关闭进程
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197547-1678846129.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197547-1678846130.png "null")

# Windows分析排查-系统信息排查

## 0x01 异常计划任务排查

在计算机中可以通过设定计划任务，在固定时间执行固定操作。一般情况下，攻击者设定计划任务在固定时间设置执行恶意代码，以达到隐蔽实现攻击的效果。

在使用schtasks命令可以对计划任务进行管理，直接输入schtasks可以查看当前计算机中保存的计划任务。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197547-16788461301.png "null")

使用任务管理器查看当前计算机中的计划任务，在开始菜单找到“计划任务程序”进行打开。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197547-1678846132.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197547-1678846133.png "null")

通过对相关的可疑计划任务进行排查，如发现相关运行程序可疑时，可根据文件路径找到程序使用云沙箱进行在线分析。

https://www.virustotal.com/gui/home/upload

https://x.threatbook.com/

https://ti.360.cn/#/homepage

## 0x02 隐藏账户发现与删除

隐藏账户是指攻击者入侵服务器后威朗能够持久保持对计算机的访问，在计算机系统中建立的不易被发现的计算机账户。

隐藏账户建立命令：

`net user test$ test /add && net localgroup administrator test$ /add`其中$符号可以导致系统管理员在使用net user时无法查看到test$用户。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197547-1678846135.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197547-1678846136.png "null")

检查注册表`计算机HKEY_LOCAL_MACHINESAMSAMDomainsAccountUsersNames`中是否有隐藏的账户，通过注册表进行建立的隐藏账户无法在计算机管理中进行查看，隐蔽性极高。在排查隐藏账户时可进行查看是否有相关可疑账户。发现确认可疑账户可右击进行删除。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197547-1678846138.png "null")

## 0x03 恶意进程发现与关闭

恶意代码在windows系统中运行过程中，将以进程的方式进行展示。其中恶意进程执行这各种恶意行为。对于可执行程序，可能直接使用杀毒软件进行查杀，但是并非所有的恶意程序都能被查杀。也可手动进行查杀，使用工具psexplore，然后利用在线云沙箱等进行检测分析。对恶意程序相关服务进行关闭。

## 0x04 补丁查看与更新

windows系统支持补丁以修复漏洞。可以使用systeminfo查看系统信息，并展示对应的系统补丁信息编号。也可以在卸载软件中查看系统补丁和第三方软件补丁。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197547-1678846139.png "null")

在win10中使用快捷键win+i，然后选择Windows更新。...