---
title: getRequestURl导致的安全鉴权问题
url: https://forum.butian.net/share/3730
source: 奇安信攻防社区
date: 2024-09-19
fetch_date: 2025-10-06T18:25:01.485048
---

# getRequestURl导致的安全鉴权问题

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

### getRequestURl导致的安全鉴权问题

* [漏洞分析](https://forum.butian.net/topic/48)

getRequestURl导致的安全鉴权问题

经常我们在看到相关的一些JAVA程序站点的时候会遇到一些问题即为，为什么他们的POC在最后总有一
些让人不理解的字符例如：;.js ;server ;.css等。
我们进行盲猜的时候大概可以知道这大概率是为了绕过鉴权的，但是因为什么可以导致被绕过呢，今天
我们来展开分析。
### 获取URL的几个方法：
```String
System.out.println("1:我是getRequestURI"+requestURI);
StringBuffer requestURL \= request.getRequestURL(); //获取url
System.out.println("2:我是getRequestURl"+requestURI);
String servletPath \= request.getServletPath(); //获取Servlet的路径
System.out.println("3:我是getServletPath"+requestURI);
```
在JAVA当中获取到当前的URL一般可以分为上述几个方法，我们来进行运行查看。
![Snipaste\_2024-08-22\_21-32-56.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-9c00fcbfa186c917c46a90c8f5fa4f56e053a6bb.png)
可以看到最后一个是I的获取到的只是访问的目录
URL的获取到的是全部的一个地址
ServletPath获取到的也是一个访问目录
在经过测试之后可以发现一个问题：
#### 测试相关的Payload绕过
![Snipaste\_2024-08-22\_21-33-51.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-0373e4ddf61e06d8c6e9133788cfe4293a2fa092.png)
那么即为上述问题，可以看到不同的获取URL的方法，对于结果并不一样。
可以看出来，其中两个方法：
getRequestURL
getRequestURI
获取到的参数都不尽相同，但是我们是否能够成功的进行访问呢。
![Snipaste\_2024-08-22\_21-35-07.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-c9d700cc8dd95c4c44d75525d087a2a6a79b3a88.png)
可以看到我们即使输入别的参数也是可以正常访问到的。
这里我们模拟一个环境。
getRequestURL方法
![Snipaste\_2024-08-22\_21-35-26.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-048fe2f5b01cc0c8087ab9c1fba3f597f645df3d.png)
这里我设置了一个过滤器，要求是过滤全部的请求，通读一次代码为，若是在URL当中判断出来存在相关的.css的时候放行，若是不存在.css那么不允许进行放行。
![Snipaste\_2024-08-22\_21-35-52.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-6286563fb054d83037c1c519a5f6fda2f1f0e8c7.png)
那么我们使用上述的payload即可进行相关的绕过，导致我们可以成功的被放行。
#### getRequestURI方法
![Snipaste\_2024-08-22\_21-36-32.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-77faf4cf48c9500b981d7402de53736048b32c80.png)
同样我们换成getRequestURI方法的时候也是可以进行绕过的。
![Snipaste\_2024-08-22\_21-36-51.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-0835c6d9a648235f3d96cb1281bb215cb3fce53f.png)
那么我们换成下一个方法
#### getServletPath方法
![Snipaste\_2024-08-22\_21-37-25.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-0d84b50cd092d521e75927802698fbf231f0e003.png)
我们在进行测试绕过的时候可以发现。
![Snipaste\_2024-08-22\_21-37-45.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-5c3e37554df47297c4c9bb7d87a43ede090703cf.png)
使用这个方法是不能够成功绕过的。
#### equals与endsWith
并且自己在测试的时候发现，若是变为equals方法是无法进行绕过的。
再通过查询相关资料之后发现
![Snipaste\_2024-08-22\_21-38-26.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-38eb7bbb682a4682e6ad83d8f6c9b7e7e098e651.png)
equals是进行判断两个值是否等价，也就是是否是完全相等的，然而endsWith是来判断一个字符串的结尾是否为指定结尾的
![Snipaste\_2024-08-22\_21-38-59.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-87db0e36b4225a3c2df63081dc0e67703cacee28.png)
可以看到其中的indexOf方法也是比较好理解的，也是进行一个指定内容在字符串当中出现的位置。
然而startsWith方法则是进行判断是否以某个字符串开头的
![Snipaste\_2024-08-22\_21-39-45.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-163b9e0bba75f3befb6a5d880bef87789517c311.png)
在其他方法当中都是可以绕过的除了(equles)那么方法startsWith该如何进行绕过呢。
下面代码实例
![Snipaste\_2024-08-22\_21-40-11.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-48988148b35860cdcd152565d5efed9c11ccc8f0.png)
可以看到这段过滤器当中进行了判断是否.css开头，那么这种办法是无法进行绕过的，但是如果他指定某一个路径开头呢
![Snipaste\_2024-08-22\_21-40-31.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-2002503ae05422cee4ce0d8da2ca3ed0bd7b1f90.png)
回到刚才我们可以看到我们输入/a/../index也是可以的，那么当过滤器代码变为了下面这种
![Snipaste\_2024-08-22\_21-40-51.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-8944b05559e643eeef35d558145adac6f53e6058.png)
指定我们以css目录开头
![Snipaste\_2024-08-22\_21-41-09.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-14765ba670c4ae367fb7779eefe7b542133607f0.png)
同样我们也是可以进行绕过的。
全程代码只有一个路由/Servlet\\_dome以及一个过滤器
#### 相关代码
```jspackage
import jdk.nashorn.internal.ir.RuntimeNode;
import javax.servlet.\\*;
import javax.servlet.http.HttpServletRequest;
import java.io.IOException;
import java.io.PrintWriter;
public class Filter\\_dome implements Filter {public void init(FilterConfig config) throws ServletException {
}
public void destroy() {
}
@Override
public void doFilter(ServletRequest request, ServletResponse response,
FilterChain chain) throws ServletException, IOException {
HttpServletRequest req \= (HttpServletRequest) request;
String requestURL \= req.getRequestURI();
if (requestURL.startsWith("/css")){
chain.doFilter(request,response);
}
else {
PrintWriter writer \= response.getWriter();
writer.println("false");
}
}
}
```
#### 相关Servlet代码
```package
import javax.servlet.\\*;
import javax.servlet.http.\\*;
import javax.servlet.annotation.\\*;
import java.io.IOException;
import java.io.PrintWriter;
@WebServlet(name \= "Servlet\\_dome", value \= "/Servlet\\_dome")
public class Servlet\\_dome extends HttpServlet {
@Override
protected void doGet(HttpServletRequest request, HttpServletResponse
response) throws ServletException, IOException {
String requestURI \= request.getRequestURI(); // 获取整个URL
System.out.println("1:我是getRequestURI"+requestURI);
StringBuffer requestURL \= request.getRequestURL(); //获取url
System.out.println("2:我是getRequestURl"+requestURL);
String servletPath \= request.getServletPath(); //获取Servlet的路径
System.out.println("3:我是getServletPath"+servletPath);
PrintWriter writer \= response.getWriter();
writer.println("success");
}
@Override
protected void doPost(HttpServletRequest request, HttpServletResponse
response) throws ServletException, IOException {
}
}
```
#### 相关web.xml代码
```<?xml
<web-app xmlns\="http://xmlns.jcp.org/xml/ns/javaee"
xmlns:xsi\="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation\="http://xmlns.jcp.org/xml/ns/javaee
http://xmlns.jcp.org/xml/ns/javaee/web-app\\_4\\_0.xsd"
version\="4.0"\>
<filter>
<filter-name>Filter\\_dome</filter-name>
<filter-class>controller.Filter\\_dome</filter-class>
</filter>
<filter-mapping>
<filter-name>Filter\\_dome</filter-name>
<url-pattern>/\\*</url-pattern>
</filter-mapping>
</web-app>
```
### 相关案例：
#### 某大型源码导致权限的绕过
![Snipaste\_2024-08-22\_21-43-02.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-1ad613e27c809d9efe404013f0aa916aef3dc1b6.png)
这一段是进行过滤SQL注入攻击的，但是发现使用的getRequestURl来获取到相关的路径，并且通过
indexOf来判断出现的位置，出现相关参数之后就不会在进行绕过而是进行了放行，导致被sql注入攻击
#### 某大型厂商导致权限绕过
![Snipaste\_2024-08-22\_21-43-30.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-53d6be33ef2cbe12a89f4cd3e4ee8d50c90d6002.png)
这个运用了Spring框架，其中明确规定了若是访问路径为.js或.css等不进行过滤，然而看下面的过滤器类
名称可以看到为Login等方法，也能想到可以进行绕过认证导致前台漏洞的产生
### \*\*总结\*\*
getRequestURL() 和 getRequestURI() 这两个API解析的URL是包含特殊字符的，当使用不当时会存在
安全问题，我们应该进行使用 \*\*getServletPath()\*\* 来获取URI。

* 发表于 2024-09-18 10:14:37
* 阅读 ( 19080 )
* 分类：[漏洞分析](https://forum.butian.net/community/Vul_analysis)

1 推荐
 收藏

## 1 条评论

[![](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/10992)

**[Ambition](https://forum.butian.net/people/10992)**
2024-09-23 18:07

好好好

* [0 条评论](#comment-2152)
* 0

请先 [登录](https://forum.butian.net/login) 后评论

请先 [登录](https://forum.butian.net/login) 后评论

[![echoa](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/7780)

[echoa](https://for...