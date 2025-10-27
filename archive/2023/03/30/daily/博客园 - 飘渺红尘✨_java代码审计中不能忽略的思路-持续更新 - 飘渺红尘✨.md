---
title: java代码审计中不能忽略的思路-持续更新 - 飘渺红尘✨
url: https://www.cnblogs.com/piaomiaohongchen/p/17244664.html
source: 博客园 - 飘渺红尘✨
date: 2023-03-30
fetch_date: 2025-10-04T11:07:20.430891
---

# java代码审计中不能忽略的思路-持续更新 - 飘渺红尘✨

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/piaomiaohongchen/)

# [飘渺红尘](https://www.cnblogs.com/piaomiaohongchen)

## 永远年轻永远热泪盈眶,永远在路上 星光不问赶路人,时光不负有心人

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/piaomiaohongchen/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E9%A3%98%E6%B8%BA%E7%BA%A2%E5%B0%98%E2%9C%A8)
* 订阅
* [管理](https://i.cnblogs.com/)

# [java代码审计中不能忽略的思路-持续更新](https://www.cnblogs.com/piaomiaohongchen/p/17244664.html "发布于 2023-03-29 14:51")

**1.反射和动态加载**

```
1.在java反序列化中，反射被频繁使用，使用反射修改，提取
2.动态代理的特性非常强大，java框架的过滤器就使用了动态加载这个特性
动态代理:https://juejin.cn/post/6844903591501627405

不仅在开发上，在安全领域，也广泛受用。

动态代理它的特点就是:被代理的类，调用任意方法，都会调用代理类的invoke方法。
利用这个tricks，我们可以寻找一些rce的利用链
```

   详细说下反射:

```
反射里面有两个函数，非常容易记混

1.newInstance 类似于new Class->实例化对象
2.invoke 从类中获取一个方法后,可以使用invoke() 来调用这个方法
参考:https://juejin.cn/post/6975888597865988127
```

一个个来，先看newInstance函数

newInstance和new创建实例化，虽然效果相同，但是原理差很多:

```
new是实例对象而newInstance是实用类的加载机制
new不用加载过就可用而newInstance需要加载并且有连接才可用
```

```
通过反射调用构造函数有两种方法：
调用无参构造函数：Class.newInstance()
调用带参数的构造函数：
通过 Class 类获取 Constructor
调用 Constructor 中的 newInstance(Object ... initarges) 方法
```

**2.作用域和try catch细节点**

理解java中的作用域非常重要，对代码审计，写代码都很有重要。
以一段代码为例子:

```
public static void main(String[] args) {
        try{
            float j=23/0;
            System.out.println(123);
            System.out.println(345);
//            System.out.println(s.length());
        } catch (ArithmeticException e) {
//            System.out.println(e);
            throw new ArithmeticException("123");
     }
//        System.out.println(s.length());
        System.out.println(123);
    }
```

这时候的报错是123，因为抛出了异常。因为 变量j在try这个异常处理作用域下。

![](https://img2023.cnblogs.com/blog/1090320/202303/1090320-20230322162445194-198795754.png)

拿出，把变量移出异常处理作用：

这时候报的就不是作用域中抛出的异常，而是自身的23/0的异常

![](https://img2023.cnblogs.com/blog/1090320/202303/1090320-20230322162511771-841456313.png)

再看个demo：

```
public static void main(String[] args) {
        try{
            float j=23/0;
//            System.out.println(s.length());
        } catch (ArithmeticException e) {
            System.out.println(e);
//            throw new ArithmeticException("123");
     }
        System.out.println(123);
    }
```

此时j变量在异常报错作用域内

此时会打印作用域外的内容，因为异常作用域处理了异常，会继续执行。

![](https://img2023.cnblogs.com/blog/1090320/202303/1090320-20230329142014897-1369831334.png)

移除j变量到异常处理作用域外:

```
public static void main(String[] args) {
        float j=23/0;
        try
//            System.out.println(s.length());
        } catch (ArithmeticException e) {
            System.out.println(e);
//            throw new ArithmeticException("123");
     }
        System.out.println(123);
    }
```

因为报异常，所以最后没有输出123

![](https://img2023.cnblogs.com/blog/1090320/202303/1090320-20230329142047636-2056617025.png)

只要throw抛出，就一定会走catch流:

某段cms测试代码:

```
package com.demo.testbug;

public class catch_test {
    public static void main(String[] args) {
        try {
            String cls ="xxxx";
            if(cls!=null) {
                try {
                    Class.forName(cls).newInstance();

                } catch (ClassNotFoundException classNotFoundException) {
                    throw new Exception("123");
                }
            }
        } catch (Throwable throwable2){
            System.out.println(444);
            System.out.println(throwable2);
    }
    }
}
```

这段代码，一定会走第二个catch流，因为第一个catch捕捉是抛出流，抛出必定要捕捉处理。

**3.编译类型和运行类型:**

定义变量左侧声明部分为编译类型,右侧运行类型是真实结果

运行属性，为编译类型。调用方法为运行类型

通常情况下，编译类型和运行类型一致。

使用多态的时候，编译类型和运行类型不一致

如:

```
Father f = new Son();
f.action()，调用函数是运行类型
f.属性 调用属性是看编译类型

牢记：调用方法走运行类型，调用属性走编译类型！！！
```

![](https://img2023.cnblogs.com/blog/1090320/202303/1090320-20230329142623997-689941201.png)

**5.instanceof**

```
tricks:
必须为引用类型，不能是基本类型
判断一个引用所指向的对象:instanceof
主要用来判断某个对象是不是某个类的实例。

son 和father有继承关系。此时s是子类，father是父类，是可以的。
```

![](https://img2023.cnblogs.com/blog/1090320/202303/1090320-20230329142306341-1484022804.png)

**6.request.getRequestDispatcher(**

请求转发可以用来绕过过滤器，还可以读取包含文件

![](https://img2023.cnblogs.com/blog/1090320/202303/1090320-20230329142339419-1699301192.png)

![](https://img2023.cnblogs.com/blog/1090320/202303/1090320-20230329142402301-1003854679.png)

更多参考:

<https://stackoverflow.com/questions/11187934/filter-mapped-on-forward-dispatcher-isnt-invoked-when-jsf-navigation-is-perform>

<https://www.yuque.com/pmiaowu/gpy1q8/pkzfug6spzrezz7k>

<https://blog.51cto.com/1031627059/1681958>

**7.再谈java项目各个配置文件**

![](https://img2023.cnblogs.com/blog/1090320/202303/1090320-20230329142525579-982333635.png)

**spring-mvc.xml:**
sping-mvc.xml文件中主要的工作是：启动注解、扫描controller包注解；静态资源映射；视图解析（defaultViewResolver）；文件上传（multipartResolver）;返回消息json配置。

**web.xml:**
(1)web项目启动时，读取web.xml配置文件，首先解析的是applicationContext.xml文件，其次才是sping-mvc.xml文件
(2)web.xml中配置的加载优先级context-param -> listener -> filter -> servlet

**spring.xml**

类似于web.xml

![](https://img2023.cnblogs.com/blog/1090320/202303/1090320-20230329142953938-652488949.png)

参考:<https://cloud.tencent.com/developer/article/1014354>

springmvc配置文件详解:

<https://www.cnblogs.com/alsf/p/9295987.html>

**2023.9.25更新 快过节了，更新下:**

**1.文件上传漏洞关键字搜索**:

```
1.upload Upload
2.<form action=
3.filename fileName
4.new File(
5.enctype="multipart/form-data"
6.MultipartHttpServletRequest multipartRequest
7.ServletFileUpload
....
```

**2.登录bypass关键字**:

```
1.setAttribute(
2.getRequestDispatcher(
3.new UserSession( new .*Session(
4.过滤器/拦截器bypass chain.doFilter(
5..setAuthent
6.authenticate(
7.setSessionId(
8.new User.*
9.session.setAttribute("

关注第三方组建druid等 Druid-Session监控-前端页面: /druid/websession.html
 Druid-Session监控-api接口: /druid/websession.json?orderBy=&orderType=asc&page=1&perPageCount=1000000
...
```

**3.关注jdbc:**

```
.getConnection(
DriverManager.getConnection(
```

**4.关注命令执行，命令拼接注入:**

```
/bin/sh
/bin/bash
cmd exec excute eval等
```

**5.反序列化漏洞关键字:**

```
Java有多种反序列化的方法，下面列举一些常用的方法：

1. 使用ObjectInputStream类：最常用的反序列化方法是使用Java的ObjectInputStream类。这个类可以将一个序列化的对象转换回原始的Java对象。

2. 使用XMLDecoder类：XMLDecoder类可以将XML格式的序列化对象转换回原始的Java对象。这个类通常用于在Java和其他语言之间进行数据交换。

3. 使用JSON工具库：如果序列化的数据是以JSON格式存储的，可以使用Java的JSON工具库（如Jackson、Gson等）将其转换回Java对象。

4. 使用自定义的反序列化方法：如果需要更精细的控制反序列化过程，可以使用Java的反射机制来自定义反序列化方法。

是的，除了Java自带的反序列化方法，还有许多第三方库和框架提供了自己的反序列化实现，下面列举一些常用的第三方反序列化方法：

1. Kryo：Kryo是一个快速、高效的Java序列化和反序列化库，它可以比Java自带的序列化和反序列化更快、更紧凑。Kryo支持许多数据类型，包括Java原始数据类型、集合、Map、甚至是自定义的POJO对象。

2. Protobuf：Protobuf是Google开发的一种高效的序列化和反序列化格式，它可以将数据转换为紧凑的二进制格式，并支持多种语言。在Java中，可以使用Google提供的protobuf-java库来实现序列化和反序列化功能。

3. FST：FST是一个快速的Java序列化和反序列化库，它可以比Java自带的序列化和反序列化更快、更紧凑。FST支持许多数据类型，包括Java原始数据类型、集合、Map、甚至是自定义的POJO对象。

4. ...