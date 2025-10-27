---
title: 【技术原创】FortiOS REST API 开发指南
url: https://www.4hou.com/posts/wgNz
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-29
fetch_date: 2025-10-04T02:39:19.537661
---

# 【技术原创】FortiOS REST API 开发指南

【技术原创】FortiOS REST API 开发指南 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 【技术原创】FortiOS REST API 开发指南

3gstudent
[技术](https://www.4hou.com/category/technology)
2022-12-28 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)174831

收藏

导语：本文将要介绍FortiOS REST API的相关用法，分享开发的实现细节。

**0x00 前言**

本文将要介绍FortiOS REST API的相关用法，分享开发的实现细节。

**0x01简介**

本文将要介绍以下内容：

强化环境听力

FortiOS REST API 方式登录

常用操作

常用功能

**0x02 Fortigate环境**

这里以Fortigate作为FortiOS REST API的测试环境，安装FortiGate for VMware

参考资料：https://getlabsdone.com/how-to-install-fortigate-on-vmware-workstation/

**1.下载FortiGate for VMware安装包**

下载地址：https://support.fortinet.com/

选择Support-> VMImages，选择产品：FortiGate，选择平台：VMWare ESXi

注：

7.2之前的版本可以使用15天，7.2之后的版本需要账号注册

**2.导入ova文件**

打开FortiGate-VM64.ova导入VMWare

**3.配置网卡**

3个网卡，我们只需要保留3个，删掉后面的107个，默认3个网卡的具体配置如下：

(1)管理网卡

点击VMware workstation-> Edit->Virtual Network Editor点击Change settings，点击Add Network...，选择VMnet2，选择，Type选择Host-only，DHCP选择Enabled

如下图

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221104/1667541559122162.png "1667540402120846.png")

商业网卡设置成VMnet2

(2)WAN网卡

设置成bridged

(3)局域网网卡

选择network adapter 3，点击LAN Segments...，点击Add，命名为Fortigate LAN

网卡设置成LAN segment，选择Fortigate LAN

最终配置成图

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221104/1667541559212512.png "1667540465126451.png")**4.开启虚拟机**

用户名：admin职位，为默认空

查看激活状态的命令：get system status

查看ip的命令：diagnose ip address list

得到管理网卡的ip为192.168.23.128

**5.访问网页管理页面**

地址为：http://192.168.23.128

**0x03 FortiOS REST API 登录方式**

参考资料：https://www.used.net.ua/index.php/fajlovyj-arkhiv/category/35-fortinet.html?download=83:fortios-5-6-11-rest-api-reference

FortiOS REST API支持以下类型登录：

**1.使用admin用户登录**

需要管理员用户admin的明文，不需要额外的配置

通过访问访问https://

需要注意的是，使用管理员用户登录结束后需要进行访问https://

Python示例代码如下：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221104/1667541560547121.png "1667540569155990.png")![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221104/1667541560102585.png "1667540583150078.png")

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

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221104/1667541561201080.png "1667540791388371.png")

代码实现以下三个功能：

管理员用户信息，查询失败

REST API用户信息，查询成功

查询配置文件信息，查询成功

**补充：通过漏洞(CVE-2022-40684)可屏蔽身份认证**

Python示例代码如下：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221104/1667541562116648.png "1667540875152648.png")![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221104/1667541562430130.png "1667540888714085.png")

代码实现以下三个功能：

管理员用户信息，查询成功

REST API用户信息，查询成功

查询配置文件信息，查询成功

**0x04 常用操作**

**1. 调试输出**

为了方便调试，可以在cli执行以下命令：

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221104/1667541562143693.png "1667540973329640.png")

一分钟在cli输出调试信息3

如下图

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221104/1667541563498765.png "1667541021473029.png")

**2.文件打包**

可提取使用挂载vmdk的方式加载文件，逆向分析REST API的实现

破解方法： https ://www.horizontal-fortiswitchmanager-460-dive-cve-2022-484 /

**3.增删改查操作**

读取内容使用GET方法

新建内容使用POST方法

修改内容使用PUT方法

删除内容使用DELETE方法

**0x05 常用功能**

**1.创建本地用户**

需要访问/api/v2/cmdb/user/local，发送json数据

Python示例代码如下：

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221104/1667541563149129.png "1667541117351838.png")

**2.添加防火墙**

需要访问/api/v2/cmdb/firewall/policy，发送json数据

Python示例代码如下：

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221104/1667541564617685.png "1667541212148686.png")![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221104/1667541564141180.png "1667541223140425.png")

**3.导出所有配置**

通过访问/api/v2/cmdb/system/admin导出用户信息时，密码项被加密，格式为"password":"ENC XXXX"

这里可通过备份功能导出所有配置，获得加密的用户身份，访问位置为/api/v2/monitor/system/config/backup?destination=file&scope=global

Python示例代码如下：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221104/1667541565195348.png "1667541265138163.png")

**4.抓包**

需要完成以下操作：

新建抓包过滤器

开启抓包过滤器

停止数据包捕获过滤器

下载数据包

删除数据包捕获过滤器

Python示例代码如下：

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221104/1667541565195887.png "1667541429462501.png")![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221104/1667541566142938.png "1667541526128243.png")

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221104/1667541567105997.png "1667541542148705.png")

**0x06 小结**

本文以 Fortigate REST 的配置和介绍，介绍了 FortiOS 的相关用法，为创建本地用户、添加防火墙规则、导出所有的实现代码。

本文为 3gstudent 原创稿件，授权嘶吼独家发布，如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?IClYBTuD)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/wp-content/uploads/2017/06/83af13989dee96c0471f.jpg)

# [3gstudent](https://www.4hou.com/member/bmZO)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/bmZO)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖...