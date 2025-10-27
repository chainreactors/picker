---
title: android中注入型漏洞小结
url: https://buaq.net/go-137336.html
source: unSafe.sh - 不安全
date: 2022-11-27
fetch_date: 2025-10-03T23:52:28.384412
---

# android中注入型漏洞小结

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

![](https://8aqnet.cdn.bcebos.com/5b601f664295bd8a4aca69c6476677c0.jpg)

android中注入型漏洞小结

背景在android应用开发过程中，基于项目需求一般是团队开发，这就会出现使用多种编程语言(java、Kotlin、C++等)和一些通用框架。因此，当忽略和没有重视安全编程实践时，常见的注入型漏洞(如
*2022-11-26 08:48:50
Author: [mp.weixin.qq.com(查看原文)](/jump-137336.htm)
阅读量:42
收藏*

---

**背景**

在android应用开发过程中，基于项目需求一般是团队开发，这就会出现使用多种编程语言(java、Kotlin、C++等)和一些通用框架。因此，当忽略和没有重视安全编程实践时，常见的注入型漏洞(如SQL注入、XML注入和跨站点脚本(XSS)等)可能会在应用中表现出来，从而给项目带来一些安全风险和危害。

下面从基础理论方面做下这方面的小总结。

**注入漏洞原理**

注入漏洞它就是将用户输入或插入后端查询或命令时发生的一类安全漏洞。通过注入元字符，攻击者可以执行无意中被解释为命令或查询的一部分的恶意代码。

例如，通过操纵SQL查询，攻击者可以检索任意数据库记录或操纵后端数据库的内容。

这种注入类型漏洞在服务器端或web服务中最常见。android应用中也存在可利用的实例，但这种情况不太常见，而且攻击面更小。

**SQL注入攻击**

SQL注入攻击，它涉及将SQL命令集成到输入的数据中，模仿预定义SQL命令的语法。成功的SQL注入攻击允许攻击者读取或写入数据库，并可能执行管理命令，具体取决于服务器授予的权限。

Android应用程序中一般情况下，使用SQLite数据库来控制和管理本地数据存储。假设Android应用程序通过将用户凭据存储在本地数据库中来处理本地用户身份验证。当登录SQLite数据库后，应用程序查询数据库以搜索用户输入的用户名和密码的记录。

![](https://mmbiz.qpic.cn/mmbiz_png/haqlQiars3wpLibkr6ZBPjvpiaR3YtV3FMM2g6iaRSmZiccjKZHficTkk0JC5xSuPvNvDnMRaU2780OUI9c73PBXIRcA/640?wx_fmt=png&random=0.22299459031786917&random=0.1924282708241689&random=0.2127245260272348&random=0.49350724482976527&random=0.4674698664528585&random=0.6307199702736184&random=0.5029802866960769)

如果上图中用户名和密码都设置为'1' = '1'并且都为真的情况下，这个查询后的数据库就会返回所有记录，这样就能够正常登录，这样就出现非正常授权的用户也能够正常登录数据库。

因此针对这种类型的注入攻击，除了对输入数据进行校验外，也可结合对用户进行多重身份验证。确保登录的用户为指定授权的用户。

**XML注入攻击**

在XML注入攻击中，攻击者注入XML元字符以从结构上去改变XML内容。这可以用来破坏基于XML的应用程序或服务的逻辑，也可能允许攻击者利用XML解析器处理内容的操作。

这种XML攻击的一个流行变体是XML外部实体(XXE)。攻击者将包含统一资源标识符(URI)的外部实体定义注入到输入XML中。在解析过程中，XML解析器通过访问URI指定的资源来扩展攻击者定义的实体。解析应用程序的完整性最终决定了攻击者所具备的能力，恶意用户可以在其中执行以下任何操作：访问本地文件，触发对任意主机和端口的HTTP请求，发起跨站点请求伪造(CSRF)攻击，并导致拒绝服务条件。

XXE示例：打开本地文件/dev/random，返回无限字节流，可能导致拒绝服务。

![](https://mmbiz.qpic.cn/mmbiz_png/haqlQiars3wpLibkr6ZBPjvpiaR3YtV3FMMLLbgOrNBsk8wbbBtslsBL759doaiaP6uMEGsdtAE2Lc6hh2T0HPj81w/640?wx_fmt=png&random=0.6693735723835197&random=0.5019993140188339&random=0.2742289057544065&random=0.9943092548582873&random=0.3066429068488077&random=0.446473107961451&random=0.20736764376143557)

当前的android应用开发趋势主要集中于基于REST/JSON的服务，基于XML越来越不常见。但是在使用用户提供的或不受信任的内容来构造XML查询的罕见情况下，它可以由本地XML解析器进行解释。因此，在开发过程中应始终做好验证所述输入，并转义元字符。

**注入攻击向量**

android应用程序的攻击面与典型的web和网络应用程序截然不同。android应用程序通常不会在网络上公开服务，应用程序用户界面上的可行攻击向量也比较少。针对android应用程序的注入攻击最有可能通过进程间通信(IPC)接口发生，其中恶意应用程序攻击设备上运行的另一个应用程序。

**在手动安全审查过程中发现，潜在漏洞需要执行以下任一操作：**

1、识别不可信输入的可能入口点，然后从这些位置进行跟踪，以查看目标是否包含潜在的易受攻击的函数。

2、识别已知的、危险的库/API调用（例如SQL查询），然后检查未检查的输入是否成功地与相应的查询交互。

**对于不受信任的输入，一般是通过以下常见的几个方式进入应用程序：IPC调用；自定义URL方案；二维码；通过蓝牙、NFC或其它方式接收的输入文件；粘贴板；用户界面。**

降低注入攻击向量的实践方案：

1、使用可接受值列表对不受信任的输入进行类型检查和/或验证。

2、执行数据库查询时，使用带有变量绑定的准备语句（即参数化查询）。如果定义了准备好的语句，用户提供的数据和SQL代码将自动分离。

3、解析XML数据时，确保解析器应用程序配置为拒绝解析外部实体，以防止XXE攻击。

4、使用x509格式的证书数据时，请确保使用了安全的解析器。

**跨站点脚本**

**跨站点脚本(XSS),它允许攻击者将客户端脚本注入用户查看的网页。这种类型的漏洞在web应用中很常见。**

当用户在浏览器中查看注入的脚本时，攻击者能够绕过同源策略，从而实现各种攻击（例如窃取会话cookie、记录按键、执行任意操作等）。

在本地应用程序的环境中，XSS风险远没有那么普遍，原因很简单，这类应用程序不依赖web浏览器。然而，android中存在很多使用WebView组件，这样就可能容易受到此类攻击。

**可以在android应用程序中，分析所有存在的WebView，并分析应用程序呈现的不可信输入。**

如果WebView打开的URL部分由用户输入决定，则可能存在XSS问题。

![](https://mmbiz.qpic.cn/mmbiz_png/haqlQiars3wpLibkr6ZBPjvpiaR3YtV3FMMw6KJgjXOqekehoNSKfb5H90MIhiaxEzXv1AaVB8ozvANiadMKfoKXIicQ/640?wx_fmt=png&random=0.7971065483386102&random=0.3691102190635245&random=0.7362874505264287&random=0.9472863014605806&random=0.5375049937098115&random=0.3642217582220755&random=0.09012706707210705)![](https://mmbiz.qpic.cn/mmbiz_png/haqlQiars3wpLibkr6ZBPjvpiaR3YtV3FMMbOaZNrGibhlNd0qCxmytdVodA4HCvcCibPWLojISJbDD3InmFkpVbTtg/640?wx_fmt=png&random=0.6392962657771879&random=0.14827728040125732&random=0.7388698195143741&random=0.11169923123455194&random=0.025194138948272382&random=0.6327853866669273&random=0.6063644556529151)

如果使用WebView显示远程网站，则逃避HTML的负担将转移到服务器端。如果web服务器上存在XSS漏洞，则可用于在WebView上下文中执行脚本。

**降低跨站点脚本攻击实践：**

1、除非绝对必要，否则不会在HTML、JavaScript或其它解释上下文中呈现不受信任的数据。

2、适当的编码应用于转义字符，例如HTML实体编码。特别注意：当HTML嵌套在其他代码中时，转义规则会变得复杂，呈现位于JavaScript块中的URL。

考虑如何在响应中呈现数据。如果数据在HTML上下文中呈现，则必须转义六个控制字符：

![](https://mmbiz.qpic.cn/mmbiz_png/haqlQiars3wpLibkr6ZBPjvpiaR3YtV3FMMdfOZU8nsoRsiasWAC0zFnu4IgrxExHTziarPMDIoM3gJwShZfFoLf3Fg/640?wx_fmt=png&random=0.7808858939967223&random=0.7291893666395337&random=0.06643260286817343&random=0.11364268653926612&random=0.19392260830202024&random=0.335192401451075&random=0.1468751028623907)

针对跨站点脚本动态分析，可以使用手动或者自动输入模糊化来检测，即将HTML标记和特殊字符注入所有可用的输入字段，以验证web应用程序拒绝无效输入或转义其输出中的HTML元字符。

**反射XSS攻击是指通过恶意链接注入恶意代码的攻击。**为了测试这些攻击，自动输入模糊被认为是一种有效的方法。例如，BURP扫描程序在识别反映的XSS漏洞方面非常有效。**与自动化分析一样，确保所有输入向量都包含在测试参数的手动审查中。**

**结束**

**【推荐阅读】**

[**移动端安全几个可借鉴的开源代码**](https://mp.weixin.qq.com/s?__biz=Mzk0MjIxNzgwNg==&mid=2247486001&idx=1&sn=44b5d6421ea07e319ceb675db0ef916c&chksm=c2c7c510f5b04c061d633572ae30619d79b0449e70c9fe0e2b233fc8c772c10363016087f31d&scene=21#wechat_redirect)

[**android中webview的安全攻防**](https://mp.weixin.qq.com/s?__biz=Mzk0MjIxNzgwNg==&mid=2247485902&idx=1&sn=4fd423fe423d75175cf3d5bda483c0fa&chksm=c2c7c6eff5b04ff973ec5730e31dd29c676cb7570bd68c35d59511178b71e72dcc36ded995db&scene=21#wechat_redirect)

[**android逆向渗透测试必备清单**](https://mp.weixin.qq.com/s?__biz=Mzk0MjIxNzgwNg==&mid=2247485813&idx=1&sn=e61530dfd289ea5effed0c8f817a27c9&chksm=c2c7c654f5b04f42afc7740c5f3f7497b0536e7ac03926b18c0d3989eb715cf59dbd4089bc9c&scene=21#wechat_redirect)

文章来源: https://mp.weixin.qq.com/s?\_\_biz=MzAxMjE3ODU3MQ==&mid=2650557032&idx=3&sn=d20676093be1f83340c1be7b1e2bb092&chksm=83bd2f8cb4caa69aaa814c7ed3ffc641dbe6ea3666b74bc6ad530549488b06b1f635fdd06fee#rd
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)