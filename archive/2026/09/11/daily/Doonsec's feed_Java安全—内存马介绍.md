---
title: Java安全—内存马介绍
url: https://mp.weixin.qq.com/s/5qnUImJF0iiJyyVTVAVVlQ
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:47:35.368345
---

# Java安全—内存马介绍

# Java安全—内存马介绍

原创

Drunkbaby
Drunkbaby

绿洲安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

免责声明

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/yucJ5603pv6y9MicQevnPpS4CsCLTb4vl1TvOp58mSichNPWK2ibaZVbjg7xCnL6M4RDBu4PpbibwK9NszHvNfvHJA/640?from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=6)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/mhIicicHPJQWHJs7GmXyfEYSLiadDbOoO8fdkFSzWf6j1blmwDCmIWqgnzJwkryWsJ6CtOskUMHnnEIuicHtyCq4jQ/640?from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=7)

**由于传播、利用本公众号绿洲安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号绿洲安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢**

## 0x01 前言

Java 内存马这一块要学的基础知识还是蛮多的，所以还是先把基础打牢了，再去看攻击方法比较好。

## 0x02 内存马简史

由于现在各种防护措施越来越多，文件shell就如c0ny1师傅所说的大部分已经气数已尽，内存马因其隐蔽性等优点从而越来越盛行。

其实内存马由来已久，早在17年n1nty师傅的[《Tomcat源码调试笔记-看不见的shell》](https://mp.weixin.qq.com/s?__biz=MzI5Nzc0OTkxOQ==&mid=2247483666&idx=1&sn=6421b39037735953fa3148bdbf5bf912&scene=21#wechat_redirect)中已初见端倪，但一直不温不火。后经过rebeyong师傅使用agent技术加持后，拓展了内存马的使用场景，然终停留在奇技淫巧上。在各类hw洗礼之后，文件shell明显气数已尽。内存马以救命稻草的身份重回大众视野。特别是今年在shiro的回显研究之后，引发了无数安全研究员对内存webshell的研究，其中涌现出了LandGrey师傅构造的Spring controller内存马。至此内存马开枝散叶发展出了三大类型：

1. servlet-api类

* filter型
* servlet型

2. spring类

* 拦截器
* controller型

3. Java Instrumentation类

* agent型

> 在讲内存马之前，我们还是看一看 jsp 基础。

## 0x03 JSP 基础

* 首先是 JSP 环境的搭建，我们要起一个 JSP 的环境，有的教程说起 SpringMVC 的，其实完全没必要，简单的 JSP 即可。

### 1. 什么是JSP

JSP（Java Server Pages），是Java的一种动态网页技术。在早期Java的开发技术中，Java程序员如果想要向浏览器输出一些数据，就必须得手动`println`一行行的HTML代码。为了解决这一繁琐的问题，Java开发了JSP技术。

JSP可以看作一个Java Servlet，主要用于实现Java web应用程序的用户界面部分。网页开发者们通过结合HTML代码、XHTML代码、XML元素以及嵌入JSP操作和命令来编写JSP。

当第一次访问JSP页面时，Tomcat服务器会将JSP页面翻译成一个java文件，并将其编译为.class文件。JSP通过网页表单获取用户输入数据、访问数据库及其他数据源，然后动态地创建网页。

### 2. JSP 环境的搭建

可以直接看我这篇文章，其他文章感觉说的有点玄乎了，其实 IDEA 里面内置了 JSP 的项目框架，可以直接搭建的。

Servlet 项目搭建

### 3. JSP的语法

#### 脚本程序

脚本程序可以包含任意量的Java语句、变量、方法或表达式，只要它们在脚本语言中是有效的。脚本程序的格式如下

```
<% 代码片段 %>
```

下面是使用示例

```
<html>  <body>  <h2>Hello World!!!</h2>  <% out.println("GoodBye!"); %>  </body>  </html>
```

#### JSP声明

一个声明语句可以声明一个或多个变量、方法，供后面的 Java 代码使用。JSP 声明语句格式如下

```
<%! 声明  %>
```

同样等价于下面的XML语句

```
<jsp:declaration>   代码片段</jsp:declaration>
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/goxicFBGKAF5K1Nja4gLKCbciaZFGoC3yOpibEZ5dicdc1j4GmT1W3E5FZjxUEwiaibpuWZJyQCrFqYX2beZwuWSyibFzPCXq0VicSnSibFR3ibB35yRY/640?wx_fmt=png&from=appmsg)

下面是使用示例

```
<html><body><h2>Hello World!!!</h2><%! String s= "GoodBye!"; %><% out.println(s); %></body></html>
```

![](https://mmbiz.qpic.cn/mmbiz_png/goxicFBGKAF5wuvnicSicFbK9FSNK2GIliaVoqgpM6WgIgLLWVEEWDEy3MDiaXg3iaPWVKIyEMZKGiavsiaEQ42SicTfXiaoNUCX03Wr7AOibUB0DHnUpU/640?wx_fmt=png&from=appmsg)

其实在脚本里面也是可以直接进行声明的

```
<%      int i = 3;  %>
```

#### JSP 表达式

```
<%= 表达式 %>
```

等价于下面的XML表达式

```
<jsp:expression>   表达式</jsp:expression>
```

下面是使用示例

```
<html><body><h2>Hello World!!!</h2><p><% String name = "Drunkbaby"; %>username:<%=name%></p></body></html>
```

输出如图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/goxicFBGKAF5Kmib3xG8K0Edm4FY3rHHmreGEEbEJ0dXqSWV3xrCILnxc9f4DOXBt894vdM2ibsQMOgoU0iaLXiaUmeZQZ3W29qeT2rHKaIlLRSw/640?wx_fmt=png&from=appmsg)

#### JSP 指令

JSP指令用来设置与整个JSP页面相关的属性。下面有三种JSP指令

![](https://mmbiz.qpic.cn/mmbiz_png/goxicFBGKAF6abmBePxqbGOp4vTRvAAriaDZfMjNYIpdNf113WmUqJetlNEV6ZvBOmgeEeYicZkzethVPQx523zEpzmMMUiauw878Jk6xnic8xqM/640?wx_fmt=png&from=appmsg)

比如我们能通过page指令来设置jsp页面的编码格式

```
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
```

回显是一样的，因为 JSP 属于模板引擎

#### JSP 注释

格式如下

```
<%-- 注释内容 --%>
```

### 4. JSP内置对象

JSP有九大内置对象，他们能够在客户端和服务器端交互的过程中分别完成不同的功能。其特点如下

* 由 JSP 规范提供，不用编写者实例化
* 通过 Web 容器实现和管理
* 所有 JSP 页面均可使用
* 只有在脚本元素的表达式或代码段中才能使用

| 对  象 | 类型 | 说  明 |
| --- | --- | --- |
| request | javax.servlet.http.HttpServletRequest | 获取用户请求信息 |
| response | javax.servlet.http.HttpServletResponse | 响应客户端请求，并将处理信息返回到客户端 |
| out | javax.servlet.jsp.JspWriter | 输出内容到 HTML 中 |
| session | javax.servlet.http.HttpSession | 用来保存用户信息 |
| application | javax.servlet.ServletContext | 所有用户共享信息 |
| config | javax.servlet.ServletConfig | 这是一个 Servlet 配置对象，用于 Servlet 和页面的初始化参数 |
| pageContext | javax.servlet.jsp.PageContext | JSP 的页面容器，用于访问 page、request、application 和 session 的属性 |
| page | javax.servlet.jsp.HttpJspPage | 类似于 Java 类的 this 关键字，表示当前 JSP 页面 |
| exception | java.lang.Throwable | 该对象用于处理 JSP 文件执行时发生的错误和异常；只有在 JSP 页面的 page 指令中指定 isErrorPage 的取值 true 时，才可以在本页面使用 exception 对象。 |

## 0x04 传统内存马

* 讲完了 Tomcat 架构的理解和 JSP 的一些基础，我们可以正式开始学习内存马了

我们先来看一看传统的 JSP 内存马是什么样子的。

```
<%
	Runtime.getRuntime().exec(request.getParameter("cmd"));
%>
```

上面是最简单的一句话木马，没有回显，适合用来反弹shell。我们这里弹个计算器看一看。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/goxicFBGKAF5CJxFONABJEk9whZLfJNr4P5EBIdrRfJNnXqbqGN5jfkOWzla2uPJ3nINXlX1yrOuXdtiasMknnvaUW74PpR36rd6ohHYymwQ0/640?wx_fmt=png&from=appmsg)

下面是一个带回显的JSP木马

```
<%
	Runtime.getRuntime().exec(request.getParameter("cmd"));
%>
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/goxicFBGKAF57Gxb2tSNORqRBPOtH0s99FWRXRNtaeZS6oc7Yw8PW9iakatcmEbce8Csck1cQDeLLEaLtpbbVpldVicIQRMhHEQGGDpNO80nns/640?wx_fmt=png&from=appmsg)

传统的JSP木马特征性强，且需要文件落地，容易被查杀。因此现在出现了内存马技术。Java内存马又称”无文件马”，相较于传统的JSP木马，其最大的特点就是无文件落地，存在于内存之中，隐蔽性强。

* 利用Java Web组件：动态添加恶意组件，如Servlet、Filter、Listener等。在Spring框架下就是Controller、Intercepter。
* 修改字节码：利用Java的Instrument机制，动态注入Agent，在Java内存中动态修改字节码，在HTTP请求执行路径中的类中添加恶意代码，可以实现根据请求的参数执行任意代码。

## 0x05 Tomcat 中的三个 Context 的理解

### Context

context是上下文的意思，在java中经常能看到这个东西。那么到底是什么意思呢？

根据yzddmr6师傅的理解，如果把某次请求比作电影中的事件，那么context就相当于事件发生的背景。例如一部电影中的某个镜头中，张三大喊“奥利给”，但是只看这一个镜头我们不知道到底发生了什么，张三是谁，为什么要喊“奥利给”。所以就需要交代当时事情发生的背景。张三是吃饭前喊的奥利给？还是吃饭后喊的奥利给？因为对于同一件事情：张三喊奥利给这件事，发生的背景不同意义可能是不同的。吃饭前喊奥利给可能是饿了的意思，吃饭后喊奥利给可能是说吃饱了的意思。

在WEB请求中也如此，在一次request请求发生时，背景，也就是context会记录当时的情形：当前WEB容器中有几个filter，有什么servlet，有什么listener，请求的参数，请求的路径，有没有什么全局的参数等等。

### ServletContext

ServletContext是Servlet规范中规定的ServletContext接口，一般servlet都要实现这个接口。

大概就是规定了如果要实现一个WEB容器，他的Context里面要有这些东西：获取路径，获取参数，获取当前的filter，获取当前的servlet等

```
package javax.servlet;

import java.io.InputStream;import java.net.MalformedURLException;import java.net.URL;import java.util.Enumeration;import java.util.EventListener;import java.util.Map;import java.util.Set;import javax.servlet.ServletRegistration.Dynamic;import javax.servlet.descriptor.JspConfigDescriptor;

public interface ServletContext {    String TEMPDIR = "javax.servlet.context.tempdir";
    String getContextPath();    ServletContext getContext(String var1);    int getMajorVersion();    int getMinorVersion();    int getEffectiveMajorVersion();    int getEffectiveMinorVersion();    String getMimeType(String var1);    Set getResourcePaths(String var1);    URL getResource(String var1) throws MalformedURLException;    InputStream getResourceAsStream(String var1);    RequestDispatcher getRequestDispatcher(String var1);    RequestDispatcher getNamedDispatcher(String var1);    /** @deprecated */    Servlet getServlet(String var1) throws ServletException;    /** @deprecated */    Enumeration getServlets();    /** @deprecated */    Enumeration getServletNames();    void log(String var1);    /** @deprecated */    void log(Exception var1, String var2);    void log(String var1, Throwable var2);    String getRealPath(String var1);    String getServerInfo();    String getInitParameter(String var1);    Enumeration getInitParameterNames();    boolean setInitParameter(String var1, String var2);    Object getAttribute(String var1);    Enumeration getAttributeNames();
    void setAttribute(String var1, Object var2);
    void removeAttribute(String var1);
    String getServletContextName();
    Dynamic addServlet(String var1, String var2);
    Dynamic addServlet(String var1, Servlet var2);

    Dynamic addServlet(String var1, Class var2);
     extends Servlet> T createServlet(Classvar1) throws ServletException;
    ServletRegistration getServletRegistration(String var1);
    Map ? extends ServletRegistration> getServletRegistrations();
    javax.servlet.FilterRegistration.Dynamic addFilter(String var1, String var2);
    javax.servlet.FilterRegistration.Dynamic addFilter(Str...