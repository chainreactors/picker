---
title: Web中间件漏洞之Tomcat篇
url: https://www.secpulse.com/archives/201060.html
source: 安全脉搏
date: 2023-05-30
fetch_date: 2025-10-04T11:38:25.412737
---

# Web中间件漏洞之Tomcat篇

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

# Web中间件漏洞之Tomcat篇

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[第59号实验室](https://www.secpulse.com/newpage/author?author_id=49738)

2023-05-29

26,663

1

Tomcat简介

Tomcat 服务器是一个免费的开放源代码的 Web 应用服务器，属于轻量级应用服务器，在中小型系统和并发访问用户不是很多的场合下被普遍使用，是开发和调试 JSP 程序的首选。

对于一个初学者来说，可以这样认为，当在一台机器上配置好 Apache 服务器，可利用它响应 HTML（标准通用标记语言下的一个应用）页面的访问请求。实际上 Tomcat 是 Apache 服务器的扩展，但运行时它是独立运行的，所以当运行 tomcat 时，它实际上作为一个与 Apache 独立的进程单独运行的。

2

远程代码执行

漏洞简介及成因

Tomcat 运行在 Windows 主机上，且启用了 HTTP PUT 请求方法，可通过构造的攻击请求向服务器上传包含任意代码的 JSP 文件，造成任意代码执行。

影响版本：Apache Tomcat 7.0.0 – 7.0.81

漏洞复现

配置漏洞，开启put方法可上传文件功能

tomcat文件夹下的/conf/web.xml文件插入

 <init-param>

            <param-name>readonly</param-name>

            <param-value>false</param-value>

      </init-param>

重启tomcat服务

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201060-1685344954.jpg)

访问127.0.0.1：8080，burp抓包，send to Repeater，将请求方式改为PUT，创建一个122.jsp，并用%20转义空格字符。123.jsp内容为：

<%Runtime.getRuntime().exec(request.getParameter("cmd"));%>

返回201，说明创建成功

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201060-16853449541.jpg)

访问127.0.0.1：8080/122.jsp?cmd=calc

弹出计算器

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201060-1685344955.png)

漏洞修复

1）检测当前版本是否在影响范围内，并禁用PUT方法。

2）更新并升级至最新版。

3

后台弱口令war包部署

漏洞简介及成因

Tomcat支持在后台部署war文件，可以直接将webshell部署到web目录下。

若后台管理页面存在弱口令，则可以通过爆破获取密码。

漏洞复现

Tomcat安装目录下conf里的tomcat-users.xml配置如下

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201060-1685344955.jpg)

访问后台，登陆

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201060-1685344956.png)

上传一个war包，里面是jsp后门

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201060-1685344957.png)

成功上传并解析，打开

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201060-1685344957.jpg)

可执行系统命令

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201060-1685344958.jpg)

也可进行文件管理，任意查看、删除、上传文件

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201060-1685344959.png)

漏洞修复

1）在系统上以低权限运行Tomcat应用程序。创建一个专门的 Tomcat服务用户，该用户只能拥有一组最小权限（例如不允许远程登录）。

2）增加对于本地和基于证书的身份验证，部署账户锁定机制（对于集中式认证，目录服务也要做相应配置）。在CATALINA\_HOME/conf/web.xml文件设置锁定机制和时间超时限制。

3）以及针对manager-gui/manager-status/manager-script等目录页面设置最小权限访问限制。

4）后台管理避免弱口令。

4

反序列化漏洞

漏洞简介及成因

该漏洞与之前Oracle发布的mxRemoteLifecycleListener反序列化漏洞（CVE-2016-3427）相关，是由于使用了JmxRemoteLifecycleListener的监听功能所导致。而在Oracle官方发布修复后，Tomcat未能及时修复更新而导致 的远程代码执行。

该漏洞所造成的最根本原因是Tomcat在配置JMX做监控时使用了JmxRemoteLifecycleListener的方法。

漏洞影响版本：

ApacheTomcat 9.0.0.M1 到9.0.0.M11

ApacheTomcat 8.5.0 到8.5.6

ApacheTomcat 8.0.0.RC1 到8.0.38

ApacheTomcat 7.0.0 到7.0.72

ApacheTomcat 6.0.0 到6.0.47

漏洞复现

利用条件：外部需要开启JmxRemoteLifecycleListener监听的10001和10002端口，来实现远程代码执行。

conf/server.xml中第30行中配置启用JmxRemoteLifecycleListener功能监听的端口：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201060-16853449591.png)

配置好jmx的端口后，在tomcat版本所对应的extras/目录下来下载catalina-jmx-remote.jar以及下载groovy-2.3.9.jar两个jar包。下载完成后放至在lib目录下。

接着再去bin目录下修改catalina.bat脚本。在ExecuteThe Requested Command注释前面添加这么一行。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201060-1685344960.jpg)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201060-1685344961.png)

重启tomcat，监听本地的10001和10002的RMI服务端口是否成功运行。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201060-1685344961.jpg)

构造payload，弹出计算器

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201060-1685344962.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201060-1685344962.jpg)

成功弹出计算器。

漏洞修复

1、关闭JmxRemoteLifecycleListener功能，或者是对jmx JmxRemoteLifecycleListener远程端口进行网络访问控制。同时，增加严格的认证方式。

2、根据官方去升级更新相对应的版本。

**本文作者：[第59号实验室](newpage/author?author_id=49738)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/201060.html**](https://www.secpulse.com/archives/201060.html)

Tags: [tomcat](https://www.secpulse.com/archives/tag/tomcat)、[Web中间件](https://www.secpulse.com/archives/tag/web%E4%B8%AD%E9%97%B4%E4%BB%B6)、[漏洞](https://www.secpulse.com/archives/tag/%E6%BC%8F%E6%B4%9E)、[远程代码执行](https://www.secpulse.com/archives/tag/%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C)

点赞：
1
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![代码审计 | 同源策略的绕过](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/09/a799223d33bd92e8b0620d8ad38ecd2.jpg)

  代码审计 | 同源策略的绕过](https://www.secpulse.com/archives/203439.html "详细阅读 代码审计 | 同源策略的绕过")
* [![云原生安全联防联抗策略玩转微隔离](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/09/1694157547520-300x155.png)

  云原生安全联防联抗策略玩转微隔离](https://www.secpulse.com/archives/203414.html "详细阅读 云原生安全联防联抗策略玩转微隔离")
* [![从2023蓝帽杯0解题heapSpary入门堆喷](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/08/1693450185258-300x157.png)

  从2023蓝帽杯0解题heapSpary…](https://www.secpulse.com/archives/203218.html "详细阅读 从2023蓝帽杯0解题heapSpary入门堆喷")

评论  (0)

昵称

必填
您当前尚未登录。
[登录？](https://www.secpulse.com/user_login "登录")
[注册](https://www.secpulse.com/user-register)

邮箱

必填（保密）

快来写下你的想法吧！

upload

|  |  |  |
| --- | --- | --- |
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/1a3b6dd6d88ce8675bf30bc03975bab1_ce6692cb75dd2998ff4d70b9690c28a5.jpeg)](https://www.secpulse.com/newpage/author?author_id=49738aaa) | [第59号实验室](https://www.secpulse....