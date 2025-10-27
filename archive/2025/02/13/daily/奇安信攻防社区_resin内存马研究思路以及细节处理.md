---
title: resin内存马研究思路以及细节处理
url: https://forum.butian.net/share/4133
source: 奇安信攻防社区
date: 2025-02-13
fetch_date: 2025-10-06T20:32:28.741101
---

# resin内存马研究思路以及细节处理

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

### resin内存马研究思路以及细节处理

最近实习过程中在进行一些内存马的工作，其中有些中间件自己还不是很熟悉，于是一个一个想着把他们都过一遍。然后又正好在回顾和学习泛微的一些洞，对应着resin也过一遍。

idea2024没有之前的那个resin插件了，推荐这个大佬的插件https://github.com/chao2hang/resin\\_idea/releases/tag/1.0
idea导入即可
0x01 resin基本概念补充
================
filters
-------
官方文档提到resin的filter遵循Servlet的规范,那整体思路应该也是差不多的，只不过tomcat管理这些filters和resin的管理方式或者说具体的功能类不同。resin服务中也应该会存在一个上下文的web应用管理器，类似于context。
写一个filter其实也就是一样的，只不过这里写的servlet是3.0的，包名是从javax开始。然后注册也是写在web.xml中。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-79dd3f24c4b5acf01dc4a68116e6ceb3d739afd2.png)
写一个样例：
```java
package org.main;
import javax.servlet.\*;
import java.io.IOException;
public class TestFilter implements Filter {
@Override
public void init(FilterConfig filterConfig) throws ServletException {
}
@Override
public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws ServletException, IOException {
System.out.println("TestFiltering....");
filterChain.doFilter(servletRequest, servletResponse);
}
@Override
public void destroy() {
}
}
```
然后web.xml注册一下全路由，在dofilter这里打个断点就可以开始看resin的调用堆栈结构了。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-a6d3670a7a67b059f581ad296939eb19d4cd38cc.png)
这里比较奇怪的一点是在ServletInvocation的service方法之后有很多的filterchain，这些在官网的filters文档中提到了，是resin自带的，我们可以在com.cauho.filters包下找到这些自带的filter。
Invocation
----------
这个类我们之后会经常遇到。当一个web请求发过来的时候，resin一定会创建一个Invocation用来进行帮助请求处理和管理各种内存上下文对象。简单一点说就是起到一个桥梁的作用，用于存储上下文信息，包括request和response。
当然，它的生命周期始于一次路由的请求，终结于一次路由请求的结束。具体到堆栈和代码中，开始就是HttpRequest调用handleRequest中，resin首先需要获取到invocation，然后通过调用它的service方法来继续处理请求的逻辑。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-9d835482e620f47b62c1d51e036a87b2a996d519.png)
创建invocation要用到很多层buildInvocation，之后没必要一一跟进，我采取的分析方法是直接定位到调用测试用例的filter之前的那一层doFilter，然后观察测试用例Filter是如何装载进流程的。
0x02 resin流程简单分析
================
resin的很多功能都是通过filter实现的，所以我们一上来先默认分析resin-filter的注入流程。最后再补充listener的逻辑
整体功能实现
------
还是一样的调试方法，自建一个servlet，然后在他的service方法或者继承Httpservlet，在它的doGet或者doPost方法那里下个断点，开始调试。
这里HttpRequest的handleRequest走完之后是创建invocation，对于嵌套的流程idea会自动省略内部，只留外部，理论上还是创建完invocation才开始调其service方法。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-ac531ed87bbd921265a5871cd72b6bb9b49b22df.png)
这里看到每一个FilterChain的doFilter方法，比如WebAppFilterChain的doFilter。它最后是调用了this.\\_next的doFilter。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-de06b16a27063336ae9a3b50e83b434a2b6677c5.png)
然后是最后的filterfilterChain，他是调用到了this.\\_filter的doFilter。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-66cc1d2fb67cb6e88165d560c153d2331f56c0b3.png)
而当我们回到TestFilter的dofilter，实际上还是继续调用this.\\_next的dofilter方法。只不过下一个filterchain是servletfilterchain，就直接开始调servlet的逻辑了。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-0ab9b708f2b87bf9afac8f10578283facfa6ba50.png)
说这么多其实是就是为了说明一个点。resin中间件的功能有很多都是通过filterchain实现的，他有很多filterchain，不像Tomcat中的filter更像是一个扩展功能。
观察前面提到的Invocation调用栈和动调试一下，发现实际上所有的filterchain都是在WebApp的buildInvocation​方法中进行的。但是代码内容太多了，建议师傅们在看的话就自己调试到com.caucho.server.webapp.WebApp​的buildInvocation​方法即可，这里能关系到我们自建filter创建的只有一行代码，下文会提到
filterchain创建流程
---------------
invocation的生命周期在上文提到过，当我们第一次请求一段路由时，由于内存中并没有当前路由对应的缓存，所以在AbstractHttpRequest的getInvocation​方法中的if (invocation != null) {​判断无法通过，直接进else读取当前请求的host和port来创建invocation。后续就会经过多层的invocation的创建封装，所有的filterchain是在最后的WebApp的buildInvocation中加载的。
而buildInvocation的内容中关于filterfilterchain的创建是this.\\_filterMapper.buildDispatchChain((Invocation)invocation, chain);​这条代码实现的。说白了也就是filterMapper的功能。
​buildDispatchChain​的具体的内容如下，有两段差不多的synchronized逻辑，唯一的区别在if (map.isMatch(invocation))，第一个synchronized中是if (map.isMatch(invocation.getServletName()))​，整个流程中都没有往filterMapping中写servletName，所以只有在第二段synchronized代码段中才会匹配到对应的filter，我们也只看第二段synchronized:
```java
synchronized(this.\_filterMap) {
for(i = this.\_filterMap.size() - 1; i &gt;= 0; --i) {
map = (FilterMapping)this.\_filterMap.get(i);
if (map.isMatch(invocation)) {
filterName = map.getFilterName();
filter = this.\_filterManager.createFilter(filterName);
config = this.\_filterManager.getFilter(filterName);
if (!config.isAsyncSupported()) {
invocation.clearAsyncSupported();
}
chain = this.addFilter(chain, filter);
}
}
```
先看if (map.isMatch(invocation))，具体跟进到isMatch：
你会发现出了匹配servletName之外，还会循环匹配filterMapping中的matchList变量，要实现往这个matchList中写入对应的内容，需要调用到filterManager的addfilterMapping方法。根据传入的filterMapping中的urlPattern配置进行matchlist的写入
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-75698b4a9d7a2d48b211452812685b8038978f70.png)
回到synchronized的代码块内容，chain = this.addFilter(chain, filter);​这里的chain返回值是filterfilterchain，也就是会调用到真正的filter。那么要能够创建出我们自己的filterfilterchain，调用addfilter方法时需要传入两个参数，chain和filter。chain其实不用管，他是servletChain，是调用栈一路传过来的，而filter是调用filterManager的createFilter方法创建的：this.\\_filterManager.createFilter(filterName);​filterName又是从filterMapping中取出的。所以，只要我们能否够往filterMapping里面写入我们自己的filter和配置内容就能够在流程中创建出filterfilterchain。
跟进filterManager的createFilter方法，对应的分析写在注释中
```java
public Filter createFilter(String filterName) throws ServletException {
//从当前\_filters变量中根据filterName取出对应的config，然后判断config是否为空，如果为空的话就直接抛错了。
FilterConfigImpl config = (FilterConfigImpl)this.\_filters.get(filterName);
if (config == null) {
throw new ServletException(L.l("`{0}' is not a known filter. Filters must be defined by before being used.", filterName));
} else {
Class&lt;?&gt; filterClass = config.getFilterClass();
synchronized(config) {
Filter var10000;
try {
//第一处获取到filter的地方。我们其实可以直接往\_instances中put自建的filter和filtername
Filter filter = (Filter)this.\_instances.get(filterName);
if (filter != null) {
var10000 = filter;
return var10000;
}
InjectManager beanManager = InjectManager.create();
this.\_bean = beanManager.discoverInjectionTarget(filterClass);
//config由于我们一直要用到，包括写入对应的路由urlpattern，存储filter的class和name等
//所以这种将对应filter写入config的方式也是可以的，一劳永逸。
filter = config.getFilter();
CreationalContext env = beanManager.createCreationalContext((Contextual)null);
if (filter == null) {
//如果两者都没有选择，最后还是会通过InjectionTarget反射构造出filter。并且由于我们注入器构造filter的时候会默认使用当前resin容器的类加载器进行defineClass
//所以当前的InjectManager能够在内存中找到我们指定的恶意filter
filter = (Filter)this.\_bean.produce(env);
}
this.\_bean.inject(filter, env);
ContainerProgram init = config.getInit();
if (init != null) {
init.configure(filter);
}
this.\_bean.postConstruct(filter);
filter.init(config);
this.\_instances.put(filterName, filter);
var10000 = filter;
.....
}
```
后续我就默认filterMapping和config是同一个东西了。
总结一下要做的事情就开始具体的写入：
- FlterMapper中存入了当前resin容器的所有的自建filterconfig。具体在变量\\_filterMap​中。它buildDispatchChain​的时候会遍历\\_filterMap​，然后一个一个去匹配他们对应的路由，并调用filterManager来创建需要用到的filter。所以我们要往filterMap​添加新的filterMapping(为什么不是重写？这里为了最大化的不影响本来的业务，所以采用添加的方式)
- filterManager中需要往this.\\_filters​存入我们自己的filterConfig。
- filterMapping，实际就是filterConfig，需要存入filterName，filterClass，filter（可以不写，看是哪种获取filter的方式），以及对应的urlpattern路由
下面就是具体实现了
filter各项配置
----------
### filterManger
​FilterManager​中关注一个点，最终createFilter​方法中第一行FilterConfigImpl config = (FilterConfigImpl)this.\\_filters.get(filterName);​取config是从当前变量\\_filters​中取出的。这个filters在FilterManager​中有一个方法可以写入,addFilter：
```java
public void addFilter(FilterConfigImpl config) {
if (config.getSe...