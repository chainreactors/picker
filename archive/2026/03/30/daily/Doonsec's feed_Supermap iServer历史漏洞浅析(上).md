---
title: Supermap iServer历史漏洞浅析(上)
url: https://mp.weixin.qq.com/s/00ZeX0Ks8aGMBwcjtvuItw
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:33:15.025676
---

# Supermap iServer历史漏洞浅析(上)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/iaG8gHwQY0XnW6UnBqrXqdDRPFLJUNib3uiaIxenjWXXxc6a4t4IGfayAAEh4hHqMZyH1bEnUEY3B5s6sKt3ogYDF3mNQibz0Mia8ScBLOFTfAzo/0?wx_fmt=jpeg)

# Supermap iServer历史漏洞浅析(上)

原创

路人甲
路人甲

红细胞安全实验室

![]()

在小说阅读器中沉浸阅读

## 漏洞复现

```
GET /iserver/output/../WEB-IN%2546/iserver-system.xml HTTP/1.1
Host: 127.0.0.1:8090
```

该请求主要获取`supermap`配置文件，还需搭配`iserver-security.db`来获取`supermap`数据库当中的管理员用户名（非固定，由用户自定义设置），组合起来即可获取目标系统`Token`

## 漏洞原理

首先是为什么这个路由可以未授权访问，`supermap`基于`Shiro`进行鉴权，当中`shirourls.ini`中并没有针对于`/**`的全局规则，故可以未授权访问

![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0Xlp9dyufc0LHobS6wUm13OHdEFoaJBic6mibeNAG1Mib1GCZON9JOYnLH8tupTDM7Ty8r42XzlTvmwxgqqXWsW8LHxFD2b4VvoblI/640?wx_fmt=png&from=appmsg)

导致本次漏洞的主要原因是`com.supermap.server.host.webapp.handlers.OutputPathHandler`这个处理器

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XmzfHZguQPakj5jjOl2N9p3LoticeJKv5LHicVQnBE77rzxoiaod8UOG2LnY5wn7HfZ85VAaHuK37rSfyklAibnX8KqIHwOEhIQRgI/640?wx_fmt=png&from=appmsg)

在这里判断以`/output`开头则会解码并使用`Forward`转发请求，转发的路由是解码后的路由，之所以可以转发读取文件有两个原因

* • Tomcat虽然存在`org.apache.catalina.core.StandardContextValve`这个`Valve`检测不能读取`WEB-INF`、`META-INF`等特殊目录下的文件，不过`Forward`转发请求的时候不过`Valve`，最多过`filter`

![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XkUdcIbRUfFQfiakKZMR4SfuicicX8icvMjB0DhnmXibnnhJmT6Kxia0l3DjboBflTsXgqNB7ThVzCyuqphoTCib9raVHnhqxsjGr24kQ/640?wx_fmt=png&from=appmsg)

* • 没有配置了`DispatcherType`带有`Forward`的`Filter`二次过滤，默认`Filter`的`DispatcherType`值为`REQUEST`

如下图所示可以看到这里`getDispatcher`底层会进行类似正常的路由匹配流程，解码并匹配`Wrapper`（`Servlet`在`Tomcat`容器内部的概念）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0Xlbbia0jibhFHNB2kXDnHvYHHm1y0YcRzicYibIDl5ZG8ytRxgSE0vHTUQibNy5aEHRq1uQct8KicDAzNCtsmVCUkouyqicJQzf8Wdcow/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0Xk0Tkw9hRsCnGwVWuwS99MQMB8IibVxkBjEwxRHxv8iawQHknmRoqPGAMBmHrZNEPKIIzEG8bkSap2Pdau39wzeAL1zScWKgIKHk/640?wx_fmt=png&from=appmsg)

```
getRequestDispatcher:440, ApplicationContext (org.apache.catalina.core)
getRequestDispatcher:215, ApplicationContextFacade (org.apache.catalina.core)
getRequestDispatcher:1309, Request (org.apache.catalina.connector)
getRequestDispatcher:462, RequestFacade (org.apache.catalina.connector)
handle:36, OutputPathHandler (com.supermap.server.host.webapp.handlers)
process:204, AbstractHandler (com.supermap.server.host.webapp.handlers)
a:233, AbstractHandler (com.supermap.server.host.webapp.handlers)
invokeLowerPriorityHandlers:220, AbstractHandler (com.supermap.server.host.webapp.handlers)
process:206, AbstractHandler (com.supermap.server.host.webapp.handlers)
process:325, BasicHandler (com.supermap.server.host.webapp.handlers)
doFilter:254, ApplicationFilter (com.supermap.server.host.webapp)
internalDoFilter:168, ApplicationFilterChain (org.apache.catalina.core)
doFilter:144, ApplicationFilterChain (org.apache.catalina.core)
doFilter:40, TunnelFilter (com.supermap.services.filter)
internalDoFilter:168, ApplicationFilterChain (org.apache.catalina.core)
doFilter:144, ApplicationFilterChain (org.apache.catalina.core)
handleNonCORS:333, CorsFilter (org.apache.catalina.filters)
doFilter:160, CorsFilter (org.apache.catalina.filters)
internalDoFilter:168, ApplicationFilterChain (org.apache.catalina.core)
doFilter:144, ApplicationFilterChain (org.apache.catalina.core)
doFilter:129, HttpHeaderSecurityFilter (org.apache.catalina.filters)
internalDoFilter:168, ApplicationFilterChain (org.apache.catalina.core)
doFilter:144, ApplicationFilterChain (org.apache.catalina.core)
invoke:168, StandardWrapperValve (org.apache.catalina.core)
invoke:90, StandardContextValve (org.apache.catalina.core)
invoke:482, AuthenticatorBase (org.apache.catalina.authenticator)
invoke:130, StandardHostValve (org.apache.catalina.core)
invoke:93, ErrorReportValve (org.apache.catalina.valves)
invoke:74, StandardEngineValve (org.apache.catalina.core)
service:346, CoyoteAdapter (org.apache.catalina.connector)
service:396, Http11Processor (org.apache.coyote.http11)
process:63, AbstractProcessorLight (org.apache.coyote)
process:937, AbstractProtocol$ConnectionHandler (org.apache.coyote)
doRun:1793, NioEndpoint$SocketProcessor (org.apache.tomcat.util.net)
run:52, SocketProcessorBase (org.apache.tomcat.util.net)
runWorker:1190, ThreadPoolExecutor (org.apache.tomcat.util.threads)
run:659, ThreadPoolExecutor$Worker (org.apache.tomcat.util.threads)
run:63, TaskThread$WrappingRunnable (org.apache.tomcat.util.threads)
run:750, Thread (java.lang)
```

通过前面操作完成了路由匹配，也就是找`Servlet`这个步骤，这里由于没有处理它的`Servlet`所以会使用默认的`Servlet`，也就是`org.apache.catalina.servlets.DefaultServlet`(该servlet用于读取磁盘上的文件)，以上便是`getDispatcher`底层逻辑，接下来就是`forward`请求转发了

主要逻辑位于`org.apache.catalina.core.ApplicationDispatcher#doForward`方法里面

![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XkZD0fhagSw86cHpuA3wibDUr3uY0N1q1uUFOwanHKzvc6bsMbNzsJKgKia4UWZZ1riaj96Zf1yw0m4bdp5ictaf7YwwMAdPkjXH2I/640?wx_fmt=png&from=appmsg)

设置各种属性信息并继续调用`processRequest`处理请求

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0Xm248KIfUC0lMXoASFC3fdzMzYg0RUd3HvuSgxucRPL9TRAVWyg2shHKIia5UgqxqdVZLOWIq28LTtuq2tDKRG0VicfpiaFtlr0x0/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0Xk221GTt59C8HfgmXAKgSKhTwGhyzsdN6w9ibn0gJcOg3f4lzibibDr0pY2ic8B6DiaWXxdWPichkeauSPfRQqO0BxxAz90WibwNpkFMI/640?wx_fmt=png&from=appmsg)

匹配适用的`Filter`链组成过滤链并和`Wrapper`包装在一起，本质上就是`Tomcat`底层那套`Filter`责任链

前面之所以说想要文件读取还需要没有`DispatcherType`带有`Forward`的`Filter`二次过滤导致无法读取的原因也就是在这，在`org.apache.catalina.core.ApplicationFilterFactory#createFilterChain`方法构建`Filter`链的时候有个关键判断，也就是这里的`matchDispatcher`

![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XkampoZruhraKnyNtt2vYAFcj2TXTeHLp4ibCwPGcVe9PrnTqyqYyFtibBWDY8U7EvggmqicM0ZeMDom6OKF2icKRNWxDSuntTtqkI/640?wx_fmt=png&from=appmsg)

这个属性在前面的`forward`方法调用里设置的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XkHktFDXyGibq5HClR2gWobKyEfyJrwicl8MRbZ4FDZva7P5AL6eWib9r9X6EJahXcr3a1sU7cPTicsOvugvut6u78VKO27cftGmbI/640?wx_fmt=png&from=appmsg)

认`DispatchType`为`REQUEST`，也就是无法过滤`Forward`请求，进而导致文件读取

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XlvbNiarKGtxrPdAB8YN0WYysN02dTpFoQnVHKzwXS3SoRMycM9b5gbXibwhxsfLgZo1J5ibtnDYFwRs9tzHIv03kcKR6SYlauMia8/640?wx_fmt=png&from=appmsg)

## Forward利用面

在真实场景下`Forward`可能存在如下利用面：

* • 文件读取（需要类似本次漏洞一样二次解码转发的场景，之所以需要二次解码是因为直接访问的话默认`Tomcat`会解码一次，解码一次后处理流程走到`StandardContextValve`的时候判断不通过）
* • 鉴权绕过：利用请求转发去请求被`Filter`过滤的一些敏感接口

影响`Forward`利用的主要因素有如下：

* • 多套过滤机制：在实战场景可能碰到既有`Filter`过滤又有`SpringAOP`或者`SpringInterceptor`过滤的场景，这时候能否利用成功还得看后面的`SpringAOP`或者`SpringInterceptor`过滤代码，因为这两个过滤在请求转发处理之后处理的
* • 配置`Forward DispatcherType`的`Filter`：配置该`DispatcherType`的`Filter`在请求转发的场景仍然生效，例如如下`Filter`

```
    <filter>
        <filter-name>UrlRewriteFilter</filter-name>
        <filter-class>org.tuckey.web.filters.urlrewrite.UrlRewriteFilter</filter-class>
    </filter>
    <filter-mapping>
        <filter-name>UrlRewriteFilter</filter-name>
        <url-pattern>/*</url-pattern>
        <dispatcher>REQUEST</dispatcher>
        <dispatcher>FORWARD</dispatcher>
    </filter-mapping>
```

## 思考

该漏洞在实战中有较为明显的`/../`跨目录特征，基本会被`WAF`拦截，有没有什么好办法绕过呢？

## 最后

本文当中所提及内容均来自实战代码审计班课程内容，关于该产品更加深入利用手法可以咨询课程

顺便再推荐一下我师傅的代码审计课程。近期某统一认证产品的课程章节已结束，马上开启某报表的章节，感兴趣的朋友可以尽快加入。课程中包含各类产品最新补丁对应的 0day 漏洞（非水洞） 的挖掘与分析；过往课程也涵盖多款市面产品的 0day / 1day / nday 漏洞案例讲解。课程后续会持续更新推进，支持一次报名长期学习与答疑。适合真正对代码审计感兴趣、或想系统学习但缺少思路与方法体系的同学（如有其他目的请勿打扰）。对基础要求不高，能读懂代码即可，真正帮助你从只能读懂代码到找到问题。个人学习过程中受益良多，特此分享推荐给希望提升自己的朋友（非广告）。若有打扰，敬请见谅。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XmJB2pJ9rW9WecBpAjwUySgDibz2dDH5WPHmNKRoQZDzibor0kITxPdKaPHwu46VDxgIiaTxp8RbRS8ajHjUzSypXiavsFvJXer5Oc/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzYC69W0IO3S4qrZ0yybLeL6M05Mo57Rqiaic5uxAS9x9Ehjt2WiarmiaHs16BZjUyccpYgHtxkXjGib2Lw/0?wx_fmt=png)

红细胞安全实验室

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/DibMxurmMHzYC69W0IO3S4qrZ0yybLeL6M05Mo57Rqiaic5uxAS9x9Ehjt2WiarmiaHs16BZjUyccpYgHtxkXj...