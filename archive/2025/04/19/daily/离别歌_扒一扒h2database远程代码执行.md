---
title: 扒一扒h2database远程代码执行
url: https://www.leavesongs.com/PENETRATION/talk-about-h2database-rce.html
source: 离别歌
date: 2025-04-19
fetch_date: 2025-10-06T22:02:43.926315
---

# 扒一扒h2database远程代码执行

* [主页](/)
* 返回

Back to top
Share post

# 扒一扒h2database远程代码执行

phithon

Apr 19, 2025, 6:07 AM

阅读：17840

[网络安全](/sort/PENETRATION)

[java安全](/tag/java%E5%AE%89%E5%85%A8)

前两天在《[Java利用无外网（上）：从HertzBeat聊聊SnakeYAML反序列化](https://www.leavesongs.com/PENETRATION/jdbc-injection-with-hertzbeat-cve-2024-42323.html)》这篇文章里说JDBC注入的时候提到H2 Database Web Console的RCE，我曾在Vulhub中对这个漏洞有一段描述：

> 1.4.198版本及以后的H2控制台中，添加了新的[`-ifNotExists`选项](https://github.com/h2database/h2database/pull/1726)，默认禁用远程数据库创建，这将导致攻击者必须找到一个已存在的H2数据库才能执行上述JDBC攻击。

这个说法其实是不准确的，其实官方直到2.1.210才最终解决这个漏洞，过程中存在多次绕过的问题。作为一个喜欢考古的人，我找了一下h2 Database Web Console这个RCE漏洞的历史，在此分享一下。

## [H2 Databse SQL RCE (CVE-2018-10054)](#h2-databse-sql-rce-cve-2018-10054)

我追述到的最早提出使用H2 Database执行命令的是2018年的这篇文章：《[Abusing H2 Database ALIAS](https://mthbernardes.github.io/rce/2018/03/14/abusing-h2-database-alias.html)》。当然，我并不认为是这个作者首次发现了这个问题——因为原本使用`CREATE ALIAS`来执行代码就是H2设计时候的一个Feature，所以说不上是谁“发现”了这个功能。

需要注意的是，此时这个命令执行仅仅是SQL中的一个功能，文章作者找到了一个应用场景，就是登陆H2 Database自己提供的Web console，然后在其中执行恶意SQL命令来执行任意代码。

但是由于H2 Database提供了一个Web console的功能，而Web console不需要用户认证，只要创建一个数据库文件或内存数据库，即可登陆后台并执行任意SQL语句，进而执行任意代码：

[![image.png](/media/attachment/2025/04/19/bb7857f6-e89e-424c-9b5c-a3d0d3761889.101767c3d4c6.png)](/media/attachment/2025/04/19/bb7857f6-e89e-424c-9b5c-a3d0d3761889.png)

Web console这个问题被申请了一个CVE编号：[CVE-2018-10054](https://nvd.nist.gov/vuln/detail/cve-2018-10054)，官方在[这个issue](https://github.com/h2database/h2database/issues/1225)中回应道“h2 is not designed to be run outside of a secure environment”，意思是他们认为H2 Web console并不应该被运行在不安全的网络中，所以这不算一个漏洞。

不过，正如其他的很多漏洞一样，H2 Database的开发者最终还是妥协了，在2019年2月发布了1.4.198版本（涉及的PR是[#1580](https://github.com/h2database/h2database/pull/1580)和[#1726](https://github.com/h2database/h2database/pull/1726)）来缓解这个漏洞导致的安全问题，这个补丁将H2 Database设置为默认不允许创建新的数据库（`ifExists`选项从默认的false改成true）。

默认不允许创建数据库，这意味着下面两个结果：

* 由于不能创建数据库，需要找到目标服务器上一个已经存在的数据库文件才能登陆进Web console，这变相让CVE-2018-10054从Pre-Auth RCE变成了Post-Auth RCE
* 攻击者同样不能再使用In-Memory内存数据库，因为使用内存数据库也是在“创建”数据库

我们可以看看在代码org.h2.server.web.WebServer#getConnection中，这个选项是如何生效的：

[![image.png](/media/attachment/2025/04/19/45dabfb5-c276-43cb-8d65-06bbee50b0a5.a7cad488f5b1.png)](/media/attachment/2025/04/19/45dabfb5-c276-43cb-8d65-06bbee50b0a5.png)

当`ifExists`等于true时，则执行`databaseUrl += ";FORBID_CREATION=TRUE";`，意味着在连接字符串后面增加一个新的属性`FORBID_CREATION`，值为TRUE，即禁止创建数据库。

有了这个功能以后，官方开发者之一发表了这段感慨：“It is nice to have that warm, fuzzy feeling that we are “secure” now! 8-)”。这里的描述是“模糊的安全感”，而且安全感还是打引号的，这是否也预示着这个补丁被绕过的命运呢？

## [JDBC Attack](#jdbc-attack)

JDBC Attack最早应该是在Blackhat Europe 2019的议题《[New Exploit Technique In Java Deserialization Attack](https://i.blackhat.com/eu-19/Thursday/eu-19-Zhang-New-Exploit-Technique-In-Java-Deserialization-Attack.pdf)》中提出的，作者介绍了在MySQL中，如果攻击者控制了JDBC的URL，就可以使用`autoDeserialize`和`queryInterceptors`两个参数来构造反序列化漏洞。

在2021年，Chen Hongkun(@Litch1)和Xu Yuanzhen(@pyn3rd)在Hitb上发布了《[Make JDBC Attack Brilliant Again](https://conference.hitb.org/hitbsecconf2021sin/materials/D1T2%20-%20Make%20JDBC%20Attacks%20Brilliant%20Again%20-%20Xu%20Yuanzhen%20%26%20Chen%20Hongkun.pdf)》这个议题，正式在里面提到使用JDBC注入来利用前面的H2数据库任意代码执行漏洞。

由于H2 Database web console登陆时需要输入JDBC URL，JDBC Attack让CVE-2018-10054这个漏洞从原本后台执行代码，变成登陆阶段执行。

我们可以测试一下，如果H2版本低于1.4.198，直接使用议题中提到的方法URL即可执行任意代码：

```
jdbc:h2:mem:test;MODE=MSSQLServer;INIT=CREATE TRIGGER shell3 BEFORE SELECT ON INFORMATION_SCHEMA.TABLES AS $$//javascript
    java.lang.Runtime.getRuntime().exec("calc.exe")
$$;
```

[![image.png](/media/attachment/2025/04/19/014ec59d-6d8a-4805-9273-dd9c53708dcb.daa4d28ded52.png)](/media/attachment/2025/04/19/014ec59d-6d8a-4805-9273-dd9c53708dcb.png)

对于H2大于等于1.4.198的版本来说，如果使用上面的Payload，会出现如下问题，Database “mem:test” not found, either pre-create it or allow remote database creation (not recommended in secure environments)

[![image.png](/media/attachment/2025/04/19/626713fe-a65e-4269-ac38-32ec25263233.22bb245e97d2.png)](/media/attachment/2025/04/19/626713fe-a65e-4269-ac38-32ec25263233.png)

虽然没有登陆后台，但可见JDBC Attack的利用仍然受到`FORBID_CREATION=TRUE`补丁的影响。

## [JNDI Injection（CVE-2021-42392）](#jndi-injectioncve-2021-42392)

那么对于H2高于1.4.198的Web console，我们要怎么利用呢？

其实在登陆Web console的时候，我们就可以看到一个Driver Class的选项：

[![image.png](/media/attachment/2025/04/19/1cfd0c7f-84d4-48da-aeed-cab5dcae6c29.bc705a83850a.png)](/media/attachment/2025/04/19/1cfd0c7f-84d4-48da-aeed-cab5dcae6c29.png)

我们可以找一下这个Driver Class是在哪里使用的，org.h2.util.JdbcUtils#getConnection：

[![image.png](/media/attachment/2025/04/19/08b281fc-2757-410e-bab3-50b47b1083e3.d2973ecc76e1.png)](/media/attachment/2025/04/19/08b281fc-2757-410e-bab3-50b47b1083e3.png)

可以看到，Driver Class有两种可能的类别：`java.sql.Driver`和`javax.naming.Context`，默认的`org.h2.Driver`是实现的`java.sql.Driver`接口，但在第二个if语句的注释里已经告诉我们了，这里同样支持JNDI的方式来查找数据库连接。

那么这里我们也是可以构造一个JNDI注入漏洞的，只需要将driver class设置为`javax.naming.InitialContext`：

[![image.png](/media/attachment/2025/04/19/c2499dca-1f34-4d12-8293-42a1fa8b1d8e.15cbaac65491.png)](/media/attachment/2025/04/19/c2499dca-1f34-4d12-8293-42a1fa8b1d8e.png)

这个JNDI注入攻击方式最早是由jfrog在《[The JNDI Strikes Back – Unauthenticated RCE in H2 Database Console](https://jfrog.com/blog/the-jndi-strikes-back-unauthenticated-rce-in-h2-database-console/)》这篇文章里提出，时间是2022年1月。但实际上这篇文章的作者当时并没有意识到2021年发表的JDBC注入的利用，并且似乎认为“JNDI注入”是Log4Shell带来的一个新颖的攻击面，可以看出其对Java安全漏洞的了解还是有点偏少。

JNDI注入的问题在2.0.206中被修复，此后就安全了吗？

## [FORBID\_CREATION 绕过（CVE-2022-23221）](#forbid_creation-cve-2022-23221)

回看H2 database的JDBC Attack，前面说到在1.4.198后，漏洞的利用将会受到`FORBID_CREATION=TRUE`补丁的影响，攻击者需要找到目标服务器上一个已经存在的数据库后才能利用。

但真的是这样吗？

前面我们看过官方是如何禁止创建新的数据库的：

> 当`ifExists`等于true时，则执行`databaseUrl += ";FORBID_CREATION=TRUE";`，意味着在连接字符串后面增加一个新的属性`FORBID_CREATION`，值为TRUE，即禁止创建数据库。

在JDBC连接字符串后面增加一个属性：`;FORBID_CREATION=TRUE`。

但有趣的是，我曾在《[Java利用无外网（上）：从HertzBeat聊聊SnakeYAML反序列化](https://www.leavesongs.com/PENETRATION/jdbc-injection-with-hertzbeat-cve-2024-42323.html)》这篇文章中提到，“网上有一些文章说JDBC的INIT中不支持执行多个SQL语句，其实原因就是没有转义分号导致的，实际上这里并没有限制”。

也就是说，只要将分号使用反斜线转义，分号就会变成一个普通字符串。

所以，我们可以在JDBC URL字符串最末尾增加一个反斜线，转义`;FORBID_CREATION=TRUE`最前面的分号，就可以让这个属性失效：

```
jdbc:h2:mem:test;MODE=MSSQLServer;IGNORE_UNKNOWN_SETTINGS=TRUE;FORBID_CREATION=FALSE;INIT=CREATE TRIGGER shell3 BEFORE SELECT ON INFORMATION_SCHEMA.TABLES AS $$//javascript
    java.lang.Runtime.getRuntime().exec("calc.exe")
$$;XXX=\
```

当这个JDBC URL拼接上`;FORBID_CREATION=TRUE`后，就会变成：

```
jdbc:h2:mem:test;MODE=MSSQLServer;IGNORE_UNKNOWN_SETTINGS=TRUE;FORBID_CREATION=FALSE;INIT=CREATE TRIGGER shell3 BEFORE SELECT ON INFORMATION_SCHEMA.TABLES AS $$//javascript
    java.lang.Runtime.getRuntime().exec("calc.exe")
$$;XXX=\;FORBID_CREATION=TRUE
```

此时`XXX=\;FORBID_CREATION=TRUE`变成了一个整体，就不再有`FORBID_CREATION`这个选项了。

我这里使用`IGNORE_UNKNOWN_SETTINGS=TRUE`来忽略未知名字的属性，也就是`XXX`。但`IGNORE_UNKNOWN_SETTINGS`这个选项是在2.0.202版本以后才引入的（[#2271](https://github.com/h2database/h2database/pull/2271)），那么1.4.198到2.0.202之间又该如何利用漏洞呢？

其实将`XXX`修改成一个已知的属性名就可以了，比如`AUTHZPWD`：

[![image.png](/media/attachment/2025/04/19/d7a21111-6a98-4cee-adf7-29094a68b5e7.66f92155e68a.png)](/media/attachment/2025/04/19/d7a21111-6a98-4cee-adf7-29094a68b5e7.png)

利用这个方法，我们可以让1.4.198，2.0.202，甚至2.0.206以后的H2 database web console继续执行任意命令。

最终官方在2.1.210中修复了CVE-2022-23221这个漏洞，才彻底解决Web console登陆页面的RCE问题。

## [参考链接](#_1)

* <https://i.blackhat.com/eu-19/Thursday/eu-19-Zhang-New-Exploit-Technique-In-Java-Deserialization-Attack.pdf>
* [https://conference.hitb.org/hitbsecconf2021sin/materials/D1T2%20-%20Make%20JDBC%20Attacks%20Brilliant%20Again%20-%20Xu%20Yuanzhen%20&%20Chen%20Hongkun.pdf](https://conference.hitb.org/hitbsecconf2021sin/materials/D1T2%20-%20Make%20JDBC%20Attacks%20Brilliant%20Again%20-%20Xu%20Yuanzhen%20%26%20Chen%20Hongkun.pdf)
* <https://su18.org/post/jdbc-connection-url-attack/>
* <https://www.cnblogs.com/Welk1n/p/12056097.html>
* <https://jfrog.com/blog/the-jndi-strikes-back-unauthenticated-rce-in-h2-database-console/>
* <https://github.com/h2database/h2database/security/advisories/GHSA-h376-j262-vhq6>
* <https://github.com/h2database/h2database/pull/2271>
* <http...