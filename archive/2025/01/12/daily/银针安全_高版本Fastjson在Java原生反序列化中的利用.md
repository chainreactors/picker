---
title: 高版本Fastjson在Java原生反序列化中的利用
url: https://mp.weixin.qq.com/s?__biz=Mzg2MDY2ODc5MA==&mid=2247484185&idx=1&sn=9068c43597d87c94568fe70974fd6365&chksm=ce239500f9541c160287b545120d6495c7a2aa9c5c75e0ad101c7a3d3600e86ea6b64ef75f63&scene=58&subscene=0#rd
source: 银针安全
date: 2025-01-12
fetch_date: 2025-10-06T20:16:48.051687
---

# 高版本Fastjson在Java原生反序列化中的利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/HwHmjibphiaE3mJ1NPaWuBoCCR5IsiaXqbTCBQh5xDrpU2JGw50SwUlZbVpe0f645GibPEYMXqj9YIAQUyZNP9YNeQ/0?wx_fmt=jpeg)

# 高版本Fastjson在Java原生反序列化中的利用

原创

Ape1ron

银针安全

#### 目录

* • 前言
* • 绕过思路一：从已知gadget中寻找TemplatesImpl替代品

+ • ReferenceSerialized
+ • LdapAttribute

* • 绕过思路二：利用JDBC-Attack替换TemplatesImpl

+ • mchange-commons-java
+ • c3p0
+ • postgresql
+ • mysql

* • Fastjson遍历getter方法的顺序
* • 绕过思路三：使用动态代理

+ • JdkDynamicAopProxy
+ • ObjectFactoryDelegatingInvocationHandler+JSONObject

* • 代码示例

## 前言

2023年3月，@y4tacker在博客公开了一条仅依赖fastjson的原生反序列化gadget chain，影响当时fastjson的所有版本（到2.0.26），博客原文：https://y4tacker.github.io/2023/03/20/year/2023/3/FastJson%E4%B8%8E%E5%8E%9F%E7%94%9F%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96/。

整条gadget chain如下，核心是Fastjson中的`JsonArray`类，该类被调用`toString`方法时，可遍历调用其元素的任意公开getter方法，从而触发`TemplatesImpl#getOutputProperties`方法，加载字节码完成代码执行。

![](https://mmbiz.qpic.cn/mmbiz_jpg/HwHmjibphiaE3mJ1NPaWuBoCCR5IsiaXqbTVzFpZzBvKvmTwADtJxpADEFM7y2xbPE39sUDlErO6yT3S4DroBfMHA/640?wx_fmt=jpeg&from=appmsg "null")

注： `HashMap`的作用是为了保持一个`TemplatesImpl`的反序列化引用，绕过`SecureObjectInputStream`重写`resolveClass`的限制。

2023年4月，Fastjson更新了2.0.27版本，在`com.alibaba.fastjson2.util.BeanUtils`中增加了黑名单限制，在黑名单中的类不会被调用getter方法，`TemplatesImpl`也被加入了黑名单，导致该gadget chain无法直接利用。

![](https://mmbiz.qpic.cn/mmbiz_png/HwHmjibphiaE3mJ1NPaWuBoCCR5IsiaXqbTfOVibFp8bFfH3qHPFliaPYMYiaS3QRkgI0MSs7vRsa7WM2WibeXkhJmFcQ/640?wx_fmt=png&from=appmsg "null")

`JsonArray`在调用其元素getter方法时，有一个通过ASM生成字节码的过程，对比2.0.26与2.0.27版本生成的最终代码，可以看到`TemplatesImpl#getOutputProperties`方法不再被调用。

![](https://mmbiz.qpic.cn/mmbiz_png/HwHmjibphiaE3mJ1NPaWuBoCCR5IsiaXqbTlOO3LQcmpZrrVxPicJXlIQXBhkShlYy5vhaU2eXt8vYB3q2Lib9sznZQ/640?wx_fmt=png&from=appmsg "null")

到目前最新的2.0.53版本，一共有24个黑名单，在前期黑名单是明文的类名，后面变成了根据类名计算出一个hashCode64，代码在`com.alibaba.fastjson2.util.Fnv#hashCode64`方法，魔改一下fastjson-blacklist项目（替换hashCode计算函数）找出所有黑名单类列表如下：

```
-9214723784238596577L,    // javassist.CtMethod
-9030616758866828325L,    // org.apache.xalan.xsltc.trax.TemplatesImpl
-8335274122997354104L,    // org.apache.ibatis.javassist.CtNewClass
-6963030519018899258L,    // org.apache.ibatis.javassist.CtClass
-4863137578837233966L,  // javassist.CtClass
-3653547262287832698L,     // org.apache.ibatis.javassist.CtConstructor
-2819277587813726773L,    // org.apache.ibatis.javassist.CtMethod
-2669552864532011468L,    // java.lang.ref.ReferenceQueue
-2458634727370886912L,    // java.security.ProtectionDomain
-2291619803571459675L,    // com.sun.org.apache.xalan.internal.xsltc.trax.TransformerFactoryImpl
-1811306045128064037L,    // org.apache.xalan.xsltc.trax.TransformerFactoryImpl
-864440709753525476L,    // org.apache.xalan.xsltc.runtime.AbstractTranslet
-779604756358333743L,   // org.mockito.internal.creation.bytebuddy.MockMethodInterceptor
8731803887940231L,        // org.apache.commons.collections.functors.ChainedTransformer
1616814008855344660L,   // javassist.CtNewClass
2164749833121980361L,    // com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl
2688642392827789427L,    // java.util.concurrent.locks.Lock
3724195282986200606L,    // org.apache.wicket.util.io.DeferredFileOutputStream
3742915795806478647L,    // java.io.InputStream
3977020351318456359L,    // sun.nio.ch.FileChannelImpl
4882459834864833642L,    // javassist.CtConstructor
6033839080488254886L,    // java.util.concurrent.locks.ReentrantLock
7981148566008458638L,    // com.sun.org.apache.xalan.internal.xsltc.runtime.AbstractTranslet
8344106065386396833L    // javassist.CtNewNestedClass
```

## 绕过思路一：从已知gadget中寻找TemplatesImpl替代品

第一种绕过的思路是寻找`TemplatesImpl`的替代品，既然`JsonArray`可以调用任意公开getter方法，那么只要**寻找到一个在黑名单外且通过getter方法触发利用的类即可，先从已有gadget chain中物色一下替代者**。

### ReferenceSerialized

首先想到的是`com.mchange.v2.naming.ReferenceIndirector$ReferenceSerialized`，该类在C3P0 gadget chain中首次出现，所需依赖：`com.mchange:mchange-commons-java`。

`ReferenceSerialized#getObject`方法可以通过`URLClassLoader`进行一次远程类加载，调用栈如下：

```
referenceToObject:91, ReferenceableUtils (com.mchange.v2.naming)
getObject:118, ReferenceIndirector$ReferenceSerialized (com.mchange.v2.naming)
apply:-1, 603650290 (com.mchange.v2.naming.ReferenceIndirector$ReferenceSerialized$$Lambda$23)
getFieldValue:40, FieldWriterObjectFunc (com.alibaba.fastjson2.writer)
write:256, FieldWriterObject (com.alibaba.fastjson2.writer)
write:68, ObjectWriter1 (com.alibaba.fastjson2.writer)
write:364, ObjectWriterImplList (com.alibaba.fastjson2.writer)
toJSONString:1647, JSON (com.alibaba.fastjson)
toString:904, JSONArray (com.alibaba.fastjson)
readObject:86, BadAttributeValueExpException (javax.management)
...
```

![](https://mmbiz.qpic.cn/mmbiz_png/HwHmjibphiaE3mJ1NPaWuBoCCR5IsiaXqbTXbuonDtSqgGT8AWfoSZS0bpaowicODO3ClyZ11UYRYicZP447gR8exgQ/640?wx_fmt=png&from=appmsg "null")

修改后的gadget chain如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/HwHmjibphiaE3mJ1NPaWuBoCCR5IsiaXqbTeOPYoZ2VPaGribG0IDaic95Z8yaA2DcQGzNX9oPricBlicYv9CPCZRaOwA/640?wx_fmt=jpeg&from=appmsg "null")

注：实现代码见最后一节代码示例

### LdapAttribute

`com.sun.jndi.ldap.LdapAttribute`也是一个可以替代`TemplatesImpl`的类，jdk自带，`LdapAttribute`在2021 年realworldctf 中由voidfyoo 发现。`LdapAttribute#getAttributeDefinition`方法可以触发一次JNDI注入。

![](https://mmbiz.qpic.cn/mmbiz_png/HwHmjibphiaE3mJ1NPaWuBoCCR5IsiaXqbTASUZZibndKiboYQicj1GxWgCp0xaaibR2KPUnZocEapvD5GhFicJPHzfOMg/640?wx_fmt=png&from=appmsg "null")

gadget chain如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/HwHmjibphiaE3mJ1NPaWuBoCCR5IsiaXqbTbTqWXt9mPs5hcyoHybArJs7c2BD7rQoh6BgicfpsquoibX2NmX1IaBfQ/640?wx_fmt=jpeg&from=appmsg "null")

## 绕过思路二：利用JDBC-Attack替换TemplatesImpl

`ReferenceSerialized`和`LdapAttribute`都是已知的gadget，但个人感觉这两个类在实际利用中都有一些缺陷，`ReferenceSerialized`的依赖并非大热门，`LdapAttribute`转JNDI注入的利用方式也不太友好，高版本jdk的JNDI利用一般是通过反序列化或者找本地的ObjectFactory，搞不好兜兜转转又回到了反序列化。

于是就想着寻找一个新的通过getter方法利用的gadget，正好这几年JDBC-Attack比较热门，部分数据库JDBC-Attack利用方式不依赖反序列化或JNDI，可以直接执行代码或读取文件（例如H2、Pgsql、Mysql），因此就往这个方向靠了一下。

1. 1. JDBC-Attack的常见入口方法为`java.sql.DriverManager#getConnection`，可以用这个静态方法作为污点往前找。
2. 2. JDBC-Attack的实际触发点是在各个数据库`java.sql.Driver`实现类的`connect`方法，该方法也是污点之一（实际上包含前者）。不过Driver接口本身并没有继承`Serializable`接口，因此还依赖方法自行动态创建/获取`Driver`实现类。

### mchange-commons-java

涉及类：`com.mchange.v1.db.sql.DriverManagerDataSource`

调用链：

```
com.mchange.v1.db.sql.DriverManagerDataSource#getConnection()->
java.sql.DriverManager#getConnection(java.lang.String, java.util.Properties)
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/HwHmjibphiaE3mJ1NPaWuBoCCR5IsiaXqbTW88ia5gIAKfvGj5iaspUmKPuzEDr5YJnRfnzLSwoxIVd6gjxPdjGEaiaQ/640?wx_fmt=jpeg&from=appmsg "null")依赖：

```
<dependency>
    <groupId>com.mchange</groupId>
    <artifactId>mchange-commons-java</artifactId>
    <version>0.2.19</version>
</dependency>
```

`DriverManagerDataSource`只能作为JDBC-Attack的入口，因为依赖本身不包含JDBC-Attack利用的，还需要结合数据库的JDBC依赖来利用。

### c3p0

涉及类：`com.mchange.v2.c3p0.DriverManagerDataSource`、`com.mchange.v2.c3p0.test.FreezableDriverManagerDataSource`，这两个类都是`com.mchange.v2.c3p0.impl.DriverManagerDataSourceBase`的子类。

调用链：

```
# 1
com.mchange.v2.c3p0.DriverManagerDataSource#getConnection()->
java.sql.Driver#connect()

# 2
com.mchange.v2.c3p0.test.FreezableDriverManagerDataSource#getConnection()->
java.sql.Driver#connect
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/HwHmjibphiaE3mJ1NPaWuBoCCR5IsiaXqbTxQXiasbuuDzvV7YFNVrWn168GbEyp4out14cbPHbWW6HPr2ibwqly9sQ/640?wx_fmt=jpeg&from=appmsg "null")依赖：

```
<dependency>
    <groupId>com.mchange</groupId>
    <artifactId>c3p0</artifactId>
    <version>0.9.5.5</version>
</dependency>
```

### postgresql

以上的两个依赖中的gadget都来自数据库连接池，本身只有触发JDBC连接的能力，实际利用还需要结合对应的数据库JDBC依赖。下面直接从数据库JDBC依赖本身寻找完整的调用链。

涉及类：`org.postgresql.ds.PGSimpleDataSource`、`org.postgresql.ds.PGConnectionPoolDataSource`。

两个类都是`org.postgresql.ds.common.BaseDataSource`的子类，真正起作用的也是`BaseDataSource#getConnection`方法，但`BaseDataSource`本身是抽象类，也没有实现`Serializable`接口，这两个子类恰好补足了利用条件。

调用链：

```
org.postgresql.ds.common.BaseDataSource#getConnection()->
org.postgresql.ds.common.BaseDataSource#getConnection(java.lang.String, java.lang.String)->
java.sql.DriverManager#getConnecti...