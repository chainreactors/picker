---
title: 【技术原创】FortiOS REST API 开发指南
url: https://www.secpulse.com/archives/194191.html
source: 安全脉搏
date: 2022-12-29
fetch_date: 2025-10-04T02:38:46.882748
---

# 【技术原创】FortiOS REST API 开发指南

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

# 【技术原创】FortiOS REST API 开发指南

[工具](https://www.secpulse.com/archives/category/tools)

[嘶吼RoarTalk](https://www.secpulse.com/newpage/author?author_id=3451)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2022-12-28

12,794

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194191-1672212485.gif)

# ![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194191-1672212486.png)0x00 前言

本文将要介绍FortiOS REST API的相关用法，分享开发的实现细节。

# ![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194191-16722124861.png)0x01简介

本文将要介绍以下内容：

强化环境听力

FortiOS REST API 方式登录

常用操作

常用功能

# ![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194191-1672212487.png)0x02 Fortigate环境

这里以Fortigate作为FortiOS REST API的测试环境，安装FortiGate for VMware

参考资料：https://getlabsdone.com/how-to-install-fortigate-on-vmware-workstation/

**1.下载FortiGate for VMware安装包**

下载地址：https://support.fortinet.com/

选择Support-> VMImages，选择产品：FortiGate，选择平台：VMWare ESXi

注：

7.2之前的版本可以使用15天，7.2之后的版本需要账号注册

**2.导入ova文件**

打开FortiGate-VM64.ova导入VMWare

**3.配置网卡**

3个网卡，我们只需要保留3个，删掉后面的107个，默认3个网卡的具体配置如下：

(1)管理网卡

点击VMware workstation-> Edit->Virtual Network Editor点击Change settings，点击Add Network...，选择VMnet2，选择，Type选择Host-only，DHCP选择Enabled

如下图

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194191-1672212488.png)

商业网卡设置成VMnet2

(2)WAN网卡

设置成bridged

(3)局域网网卡

选择network adapter 3，点击LAN Segments...，点击Add，命名为Fortigate LAN

网卡设置成LAN segment，选择Fortigate LAN

最终配置成图

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194191-16722124881.png)

**4.开启虚拟机**

用户名：admin职位，为默认空

查看激活状态的命令：get system status

查看ip的命令：diagnose ip address list

得到管理网卡的ip为192.168.23.128

**5.访问网页管理页面**

地址为：http://192.168.23.128

# ![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194191-1672212489.png)0x03 FortiOS REST API 登录方式

参考资料：https://www.used.net.ua/index.php/fajlovyj-arkhiv/category/35-fortinet.html?download=83:fortios-5-6-11-rest-api-reference

FortiOS REST API支持以下类型登录：

**1.使用admin用户登录**

需要管理员用户admin的明文，不需要额外的配置

通过访问访问https://

需要注意的是，使用管理员用户登录结束后需要进行访问https://

Python示例代码如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194191-16722124891.png)
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194191-1672212491.png)

代码实现以下三个功能：

管理员用户信息，查询成功

REST API用户信息，查询成功

查询配置文件信息，查询成功

**2.使用API密钥**

参考资料：https://docs.fortinet.com/document/forticonverter/6.0.2/online-help/866905/connect-fortigate-device-via-api-token

需要额外创建配置文件和用户，生成API密钥

(1)创建配置文件

登录网页管理页面，选择System-> Admin Profiles->Create New

Name设置为api\_admin

将所有权限均设置为Read/Write

(2)创建用户

选择System-> Administrators-> Create New->REST API Admin

Username设置为api\_user

Administrator profile设置为api\_admin

自动生成 API 密钥，测试环境得到的结果为r3h53QbtrmNtdk0HH5qwnw8mkcmnt7

API key有以下使用方式：

作为 URL 的参数使用，示例：?access\_token=r3h53QbtrmNtdk0HH5qwnw8mkcmnt7

标题中，示例："Authorization": "Bearer r3h53QbtrmNtdk0HH5qwnw8mkcmnt7"

Python示例代码如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194191-1672212492.png)

代码实现以下三个功能：

管理员用户信息，查询失败

REST API用户信息，查询成功

查询配置文件信息，查询成功

# ![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194191-1672212494.png)补充：通过漏洞(CVE-2022-40684)可屏蔽身份认证

Python示例代码如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194191-16722124941.png)
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194191-1672212496.png)

代码实现以下三个功能：

管理员用户信息，查询成功

REST API用户信息，查询成功

查询配置文件信息，查询成功

# ![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194191-1672212497.png)0x04 常用操作

**1. 调试输出**

为了方便调试，可以在cli执行以下命令：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194191-1672212498.png)

一分钟在cli输出调试信息3

如下图

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194191-16722124981.png)

**2.文件打包**

可提取使用挂载vmdk的方式加载文件，逆向分析REST API的实现

破解方法：https ://www.horizontal-fortiswitchmanager-460-dive-cve-2022-484 /

**3.增删改查操作**

读取内容使用GET方法

新建内容使用POST方法

修改内容使用PUT方法

删除内容使用DELETE方法

# ![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194191-16722124982.png)0x05 常用功能

**1.创建本地用户**

需要访问/api/v2/cmdb/user/local，发送json数据

Python示例代码如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194191-1672212499.png)

**2.添加防火墙**

需要访问/api/v2/cmdb/firewall/policy，发送json数据

Python示例代码如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194191-1672212500.png)
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194191-1672212501.png)

**3.导出所有配置**

通过访问/api/v2/cmdb/system/admin导出用户信息时，密码项被加密，格式为"password":"ENC XXXX"

这里可通过备份功能导出所有配置，获得加密的用户身份，访问位置为/api/v2/monitor/system/config/backup?destination=file&scope=global

Python示例代码如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194191-1672212503.png)

**4.抓包**

需要完成以下操作：

新建抓包过滤器

开启抓包过滤器

停止数据包捕获过滤器

下载数据包

删除数据包捕获过滤器

Python示例代码如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194191-16722125031.png)
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194191-1672212504.png)
![](https://secpulseoss.oss-cn-...