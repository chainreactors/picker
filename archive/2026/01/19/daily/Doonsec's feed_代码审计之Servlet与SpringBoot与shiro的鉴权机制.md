---
title: 代码审计之Servlet与SpringBoot与shiro的鉴权机制
url: https://mp.weixin.qq.com/s/yz9QYEAQ4Uwlp1tnjyuPTA
source: Doonsec's feed
date: 2026-01-19
fetch_date: 2026-01-20T03:32:59.566426
---

# 代码审计之Servlet与SpringBoot与shiro的鉴权机制

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKJVWTZMqCoHCoU4ucFqFJV8D4QWbjdicBFmQibyplmuMAxg2Sd0Xr7ibGg/0?wx_fmt=jpeg)

# 代码审计之Servlet与SpringBoot与shiro的鉴权机制

原创

secureyang
secureyang

secureyang

![]()

在小说阅读器中沉浸阅读

Servlet与SpringBoot与shiro的鉴权机制Servlet下的Filter鉴权Filter的生命周期Filter权限校验web.xml中配置Filter实现权限校验Spring下的路由鉴权Spring的路由鉴权简单代码实现怎么知道拦截器对哪些路径进行过拦截呢？怎么知道拦截的具体实现是怎样的？真实案例寻找配置文件寻找拦截器配置Shiro鉴权

# Servlet与SpringBoot与shiro的鉴权机制

> 热部署
>
> ![image-20250601224804219](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKNTibpcbMkpCBFXdjMwjMw6ZLHIpah70h1ibVjicF1Ih0NZy0Lk2Mmibz0Q/640?wx_fmt=png&from=appmsg)
>
> 更新完代码之后，在 build 中选择重新编译即可实现代码加载
>
> ![image-20250601224911630](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKVrNdXNDrc2SFRYrhhqyy1Amg46rRuIKwI5bUJCxsJTvzeL7Q6AGHVA/640?wx_fmt=png&from=appmsg)

既第二节课的路由学习，第三节课开始学习鉴权机制

web.xml 文件一般存在于WEB\_INF 目录下，我们可以通过这里面的路由，跳转到相对应的代码实现的类

## Servlet下的Filter鉴权

首先第一种就是根据web.xml路由去查看各种操作（doGet与doPost）的鉴权，直接通过对参数是否存在或者参数值进行校验，从而实现鉴权，这种是最简单鉴权方式。比如下方给出一个案例：

![image-20250526145844248](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKhNiaictcKUFxPsOffS9OOD4uCDvtgx5xeWvWIN9yQOgDvtBZYEa2VfKQ/640?wx_fmt=png&from=appmsg)

这里就是，只要你通过web.xml文件的url-pattern成功访问到对应的类，就可以执行该类中的文件，然后只需要构造参数名token-key，就会默认你成功登录，然后再通过构造 fid 去下载文件。而至于 fid 在哪，格式是什么，我们可以再从源码其他地址去寻找。

我们打开源码之后，首先去找 web.xml 文件，然后对着 web.xml 文件去找 `<url-pattern>` 标签，该标签对应着我们要去访问的URL路径，然后再去找他所对应的 `<servlet-name>` 这里面就是所对应的类代码

### Filter的生命周期

init -> doFilter -> destroy

所以我们主要审计的方法就是 doFilter

我们新建一个`Filter_dome.java`代码，让他继承自 HttpFilter，然后重写方法

![image-20250601225250229](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKf4jXxyEAhdoy7IFmQkplCpEPXNyvIBzb20CzqXAbNm9EGLhjYRTsQQ/640?wx_fmt=png&from=appmsg)

此时，我们来访问一下 helloservlet，该类的路由如下图代码所示

![image-20250601225323062](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKuHwH0fCIckZ0iaicMribAL0ibicy80D2DcBRNIvGVssnUTNrQxtFES8XwRA/640?wx_fmt=png&from=appmsg)

我们看一下效果

![image-20250601225619337](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKljwGxmVoSiaEKw8T7yHP8UmmLY6oyTIBShYTNFnia1PhegUwsKThOxtA/640?wx_fmt=png&from=appmsg)

![image-20250601225841301](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKWicm6kWpZdSicR4evENhoM16ia7Mrnf9HskmCZbvCib987THZ5JRqSrtMQ/640?wx_fmt=png&from=appmsg)

我们发现，具体的请求流程是：请求先到Servlet的init进行servlet的初始化，再直接到Filter进行请求鉴权验证

### Filter权限校验

那么，Filter 到底是如何对请求进行放行的呢，我们看下图

![image-20250601230406280](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKs3YK3z2y1qqniab6jeoxIP3Cgnmfcic5nficGEKZBSYPvMORbgZibrJIIQ/640?wx_fmt=png&from=appmsg)

![image-20250601230509929](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKlGIRtW8KGYoyxsvTwm82cyia6jibtlh5tYTDmrQiaacdMpnzjMicnPpSicg/640?wx_fmt=png&from=appmsg)

以上就是Filter的一个大致的基础用法，那么他一般到底是怎么对URL进行权限校验的呢？我们向下看

其实最简单的判断方法就是看你的请求URL当中是否含有无危害或者有危害的字段，比如：.css .js 等

![image-20250601231810455](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKTHcCOvtUdRgUaiaaWGUicwvGWxHDNtIb5xhnfDQZibdHSCOGYDOUvqy6w/640?wx_fmt=png&from=appmsg)

所以一般简单的情况就会采取这样的方式来对请求路径做校验，我们从结果中可以看到，URL中没有 .css ，因此被禁止访问。

**但是，针对 servlet 的tomcat的原理，使用 ; 会导致代码中所取到的URL字符串中可以包含.css，而在tomcat容器中，会将 ; 之后的内容过滤掉，因此，针对我们上述的场景，可以使用 ;.css 来绕过这个简单的权限校验**

![image-20250601232909143](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAK5HicySwUyXRc3ddeV3CmYMaMAPZ649YlRe7ZAibl8G5r3GfZPYRWjxNQ/640?wx_fmt=png&from=appmsg)

而且我们发现，参数竟然还成功传递和接收了，有点东西

但是，这种绕过方法也是有限制的，只针对 tomcat 容器情况下，使用 `getRequestURL()` 与 `getRequestURI()` 两种方法可以进行绕过，如果采用 `getServletPath()` 来获取请求路径的话，使用 ; 来绕过就是失败的。

### web.xml中配置Filter实现权限校验

当然，Filter也同样可以在web.xml中去配置

## Spring下的路由鉴权

![image-20250602151244808](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKZxlQz7j6MNPmXbXsvyedcoPKWamRFwAdacALxqicIzwE6M1epLrhu9Q/640?wx_fmt=png&from=appmsg)

这种情况会有一个单独写出来的可以不用 if 来判断的 路由鉴权

Spring boot 中有内置的tomcat容器，因此上述我们提到的 ; 绕过方法也是可以的

### Spring的路由鉴权简单代码实现

**第一步：**注册一个拦截器到MVC框架中（为神马Filter不需要注册请看上面的图片对比）

![image-20250602152331995](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAK8Fwv3oWpkMibO4EIJOM47zyu6q4PbLIUpqpTlOzvqopJ77uvHt7V2Xg/640?wx_fmt=png&from=appmsg)

当然啊，其实这里的 excludePathPatterns经过测试好像没起作用。

其中，新建的拦截器对象名称就是要实现的拦截器所对应的真实类名

![image-20250602151412960](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKhDClelISpNFVAib7sW66cbxXaz8bViaibYSy3mJQkKhyAwvSuRJqvmiamw/640?wx_fmt=png&from=appmsg)

我们来访问一下看看效果：

![image-20250602151503903](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKCZj5OlX1yuobRIJ7cBfOkRTMtTOpyib6IU7eTfA5uQpOEljLiaTDZR0w/640?wx_fmt=png&from=appmsg)

我们可以发现，请求到该URL的时候，第一时间会直接通过，但由于实际上并没有这个文件，所以会跳转到 /error 这个URL中去，但 拦截器 并没有允许这样的URL，因此又会出现 forbidden。而我们直接访问之前的路由，则是会被直接禁止。

![image-20250602151709306](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKGMBDAeLpUJ5ibiaqDDJI3jLGUsd7QyWialDrZEWHviaA3RP6FA0FgMPiaYw/640?wx_fmt=png&from=appmsg)

因此，有了上述的基础之后我们再来看，如何去审计对应的问题：

### 怎么知道拦截器对那些路径进行过拦截呢？

进去之后直接搜 `implements WebMvcConfigurer` ，在这份文件里，会列出所有的拦截器，以及该拦截器要对应的拦截那些路径，放过那些路径。

![image-20250602152507361](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAK8Fwv3oWpkMibO4EIJOM47zyu6q4PbLIUpqpTlOzvqopJ77uvHt7V2Xg/640?wx_fmt=png&from=appmsg)

### 怎么知道拦截的具体实现是怎样的？

Spring中我们进去可以去搜索 preHandler 这个方法，这个方法中则实现了对目标请求的校验，来判断到底是放行还是阻断，而且这个类方法的返回值是 bool 类型，因此它是通过返回结果为 true 或者 false 来判断的。

当然，我们一般更推荐先去搜 `implements WebMvcConfigurer` ，这个文件里会列出所有的拦截器，不然直接去搜索 preHandler 可能会有很多文件，看起来很乱。

然后找到对应的 拦截器 名称之后，再进入 拦截器去看就知道了。

如果不在 Spring 中的Filter类中做路由鉴权，而是在HandlerInterceptor接口中操作，通过preHandle类的实现实现到Filter，并且使用的是 request.getServletPath()。就无法绕过，但使用 request.getRequestURI() 还是依旧可以用 ;.css 这样的方式来绕过

### 真实案例

**海康威视智能综合安防系统**

#### 寻找配置文件

* 进入源码之后，我们首先去找配置文件，怎么找呢，找到 WEB-INF 目录，再找到里面的 classes 目录，打开该目录，我们可以看到一个叫做 springMVC.xml，当然，也有可能重命名，比如这里就是 springMVC-servlet.xml

![image-20250602165151031](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKIpIYRVFQa0ibluO5g7DmgxEWFULgD4pHumVdBK9rZV5aNFEsZ2Egy5g/640?wx_fmt=png&from=appmsg)

* 进入源码，双击 shift ，在弹出框中直接搜索 springMVC 即可

![image-20250602165749994](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKVfWSYUUZQedbTUia0VnWFOHUl1R03uf3j6Bp6OWiarobziblac31Nr1xQ/640?wx_fmt=png&from=appmsg)

#### 寻找拦截器配置

进入配置文件之后，直接搜索 interceptor

![image-20250602170155840](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKZ60Y1DBMvJUl5RJ9eeEHxP1A8lBy75qpIobA6DFA9dpAl4zr9NZdCQ/640?wx_fmt=png&from=appmsg)

而下面的 <bean> 标签中其实就是反转注册一个类，这个类就是拦截器的类，其中具体实现的代码就在其中。

> 这里其实就和SpringBoot框架中拦截器实现很相似，先是注册一个拦截器类到MVC框架中，然后再实现注册的这个类。

然后去找这个拦截器类具体位置在哪，复制类名，双击 shift，粘贴搜索

![image-20250602170619220](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKGnCsyXrKhh4QRnCnpeeSTWPicG5FVDTIuUeicZaoviceuCRLkGZRZIbLA/640?wx_fmt=png&from=appmsg)

进入之后，去找上面提到的 preHandler 类

![image-20250602170655784](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKVmk8UDI0HNnRib8icruJxb7R2QNaZTFlqcnlicPGuzXeUEWaZSKJib6yhA/640?wx_fmt=png&from=appmsg)

![image-20250602171425298](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKPVUJ3bVibhm6VwXTav1hrkp2lj6EvKue1HRrPWbCKJV6F0iaJlu8fKPQ/640?wx_fmt=png&from=appmsg)

## Shiro鉴权

Shiro鉴权绕过 | yemoli's blog

进到源码之后，搜索 `ShiroFilterFactoryBean shiroFilter`

在这个类中，进行路由鉴权的时候，我们去找 `filterChainDefinitionMap.put("/getName","anon");` 这样的代码，只要后面是有 anon 这个参数的，就表示该路径不需要鉴权

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKhrWXUOnW99NBFq0QG13UYQviawrn5icFob5WcRaH44Me9jjMRYibaN6Og/640?wx_fmt=png&from=appmsg)

当然，这里面也可以用 ; 来 绕过路径的鉴权，从而导致绕过。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoQW0gRe2T7PcibUQdxRXlZ9gUmhnDnCnZH1QV9ickJOicpYfupCNqRefT4xquSPPTcAIhDibeicp4aL8ZQ/0?wx_fmt=png)

secureyang

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

![作者头像](http://mmbiz.qpic.cn/sz_...