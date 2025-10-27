---
title: 从JS到内网横向
url: https://www.secpulse.com/archives/199384.html
source: 安全脉搏
date: 2023-04-22
fetch_date: 2025-10-04T11:32:11.834497
---

# 从JS到内网横向

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

# 从JS到内网横向

[内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-04-21

18,384

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-1682062886.png)

## 前言

前段时间参加了一场攻防演练，使用常规漏洞尝试未果后，想到不少师傅分享过从JS中寻找突破的文章，于是硬着头皮刚起了JS，最终打开了内网入口获取了靶标权限和个人信息。在此分享一下过程。

**声明**：本次演练中，所有测试设备均由主办方提供，所有流量均有留档可审计，所有操作均在授权下完成，所有数据在结束后均已安全销毁。

## 通过JS打点

开局只有一个登录页面，无法枚举用户名并且尝试爆破未果。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-1682062892.jpeg "null")

利用bp抓包查看JS相关文件发现存在sql语句

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-1682062893.jpeg)

跟踪`comboxsql`变量，发现定义了一个`action`类

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-1682062894.jpeg "null")

搜索这个action类路径，发现访问方式是通过url拼接

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-1682062896.jpeg "null")

将该路径进行拼接，并将参数输入sql语句，测试发现该数据库为mssql数据库，可通过xp\_cmdshell来执行系统命令。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-1682062897.jpeg "null")

## shellcodeloader上线CS

执行system权限后，打算直接使用远程下载上线免杀cs，但是未上线成功，查看进程发现有360企业云，触发拦截了执行exe行为。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-1682062899.jpeg "null")

换种思路，通过下载哥斯拉webshell后，利用哥斯拉的shellcodeloader功能，加载自己CS木马的shellcode可上线成功。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-1682062900.jpeg "null")

## 解密数据库配置信息

因执行任何exe文件时，均提示拒绝访问，无法进行文件的运行，通过搜索本机配置文件发现了数据库的账号密码，但是数据库密码加密了

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-1682062901.jpeg "null")

通过查找历史网站备份文件，发现的该系统早期配置文件并未做数据库密码加密配置，测试发现可以连接数据库。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-16820629011.jpeg "null")

另外查找本系统数据库备份文件时，意外发现了该服务器部署的另一套业务系统，并且数据库配置文件中的账号、密码和数据库ip同样也为加密存储。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-1682062902.jpeg "null")

通过查找该系统特征发现为SiteServer CMS系统。从网上搜索发现了该cms的专用加解密工具 `SiteServer CLI`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-1682062905.jpeg "null")

运行后也可获取数据库明文配置信息

```
Server=x.x.x.x;Uid=sa;Pwd=xxCSthink!@#123;Database=NEWdfgxx
```

cs开启代理进行连接，测试连接成功

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-1682062907.jpeg "null")

不过同样发现该数据库服务器也无法执行exe程序，无法运行mimikatz读取管理员哈希，无法建立用户，无法上传tscan进行内网扫描，在这尬住了。最后使用cs插件的信息探测，可探测内网网段资产。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-1682062909.jpeg "null")

使用17010插件攻击失败

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-1682062910.jpeg "null")

使用proxychains配合msf获取了PC权限

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-1682062912.jpeg "null")

-w752

使用mimikaz读取管理员密码开启远程桌面发现无法登录限制

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-1682062914.jpeg "null")

msf加载mimikaz模块

```
privilege::debug
ts::multirdp
```

## 获取内网权限

建立新用户，进入个人pc电脑

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-1682062915.jpeg "null")

通过该PC机为据点，上传TideFinger和Tscan搭配进行内网扫描，在这有必要介绍下该两款工具。

**Go语言版的TideFinger指纹识别功能：** 1、加入Dismap、Vscan、Kscan、fofa、ServerScan等多个指纹 2、并加入了ServerScan的非web服务指纹，优化了资产发现的协程并发效率。3、显示效果借鉴了Dismap，在效率和指纹覆盖面方面应该是目前较高的了

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-1682062916.png)

**Go语言版的Tscan功能：** 1、Tscan为Tide安全团队共同维护的内外网资产扫描工具 2、基础代码随Fscan更新进行迭代 3、与潮声POC漏洞检测平台联动，团队成员每月会编写近期爆出的poc和定期收集整理网上已发布的poc检测模块最后进行更新发布。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-1682062923.jpeg)

扫描内网网段后，接下来是漏洞验证的过程，瞄了一眼结果没有发现能直接getshell的洞，不过指纹探测出了内网其中一ip开放了2222端口为rmi。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-1682062925.jpeg "null")

虽然拿到了该服务器权限，但是通过对本服务器进行信息搜集时，并未发现其它相关的账号密码信息。

## SAM文件获取用户hash

使用mimikaz中`sekurlsa::logonpasswords`命令尝试读取进程lsass的信息来获取当前登录用户的密码信息，输出结果发现没有administrator等用户信息（主要是因为拿权限上cs时，估计触发了杀软策略导致服务器重启了），然后使用`query user`发现管理员用户不在线，故无法直接通过内存读取管理员hash。使用mimikaz读取SAM文件中的hash。

```
#提升权限
privilege::debug
#提升至system
token::elevate
#抓取sam
lsadump::sam
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-1682062926.jpeg "null")

## hash传递

拿到NTLM Hash后发现无法从在线网站直接解密出明文密码 通过获取的NTLM进行hash传递获取四台服务器权限。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-1682062927.jpeg "null")

接下来利用hash登录该服务器，继续进行信息搜集。在其中一台服务器内发现了套娃远程桌面，并且为03系统

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199384-16820629271.jpeg "null")

## 获取服务器密码规律

通过mimikaz读取该密码（在KB2871997之前，Mimikatz可以直接抓取明文密码）

```
* Username : Administrator
* Domain : WIN-LAOLOVGMF
* Password : xxxxxy401*1009

* Username : Administrator
* Domain : SD-68QDNY80KE
* Password : xxxxxy101*2006

* Username : SDAdministrator
* Domain : SD-93O4N5O2UD
* Password : xxxxxy501*2003
```

以及获取数据库配置密码

```
 <add key="dbHostName" value="."/>
            <add key="dbDBName" value="REPSDU"/>
            <add key="dbUserName" value="sa"/>
            <add key="dbUserPwd" value...