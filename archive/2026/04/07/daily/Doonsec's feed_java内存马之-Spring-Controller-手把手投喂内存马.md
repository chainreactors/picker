---
title: java内存马之-Spring-Controller-手把手投喂内存马
url: https://mp.weixin.qq.com/s/0YTVSCs0eVMEQpkCU7rQhQ
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:33:50.811632
---

# java内存马之-Spring-Controller-手把手投喂内存马

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ic8BH9EFusn7ZU5Tiae7UnO7YbBaaDKOEcwMCXFAmT62rR2cgRUibicibSkD86frxYydQuzlAQyematIDibDl2ycYWzOeRZegpUn4ZvzkCQh98BSQ/0?wx_fmt=jpeg)

# java内存马之-Spring-Controller-手把手投喂内存马

原创

三呼呼
三呼呼

古月安全

![]()

在小说阅读器中沉浸阅读

**基础知识介绍**

Spring:是 Java 生态中最流行的应用程序框架，它是使用 Java 语言编写的一个开源企业应用开发框架，提供全面的编程和配置模型。

Spring Boot：是Spring框架的一个模块，旨在简化Spring应用程序的初始搭建和开发过程。它提供了默认配置，可以快速创建独立的、生产级的基于Spring的应用程序，其内置了Tomcat，使用Spring Boot时，我们通常不需要关心Servlet容器的配置，因为它提供了自动配置。而直接使用Tomcat时，我们需要手动配置和部署文件。

Spring内存马是一种无文件、驻留在内存中的恶意后门程序，它利用Spring框架的机制动态注册恶意组件，从而实现对入侵服务器的持久化控制。由于其完全存在于内存中，不写入磁盘，Spring内存马的隐蔽性很高，因为它利用的是Spring正常的机制，而且没有文件落地。检测Spring内存马需要监控Spring容器的动态变化，例如检查新注册的Controller、Interceptor或Bean，以及监控不正常的URL映射。

**Spring内存马工作原理：**Spring内存马通常通过利用应用程序的漏洞（如反序列化漏洞、SQL注入、文件上传漏洞等）注入，然后动态注册恶意的Spring组件（如Controller、Interceptor等）。这些组件与正常业务组件一样运行在Spring容器中，但包含恶意功能。

**常见的Spring内存马类型包括**

Controller内存马：攻击者动态注册一个恶意的Controller，该Controller可以映射特定的URL路径，当访问该路径时，执行攻击者指定的命令（如系统命令、文件操作等）并返回结果。

Interceptor内存马：攻击者注册一个自定义的拦截器（Interceptor），该拦截器会在每个请求处理之前或之后执行恶意代码。由于拦截器可以拦截多个请求，因此这种内存马具有较高的触发频率。

Bean内存马：通过修改Spring容器中的已有Bean或动态注册新的Bean，在Bean的初始化方法或业务方法中植入恶意代码。这种内存马可能利用Spring的依赖注入机制，在Bean被其他组件使用时触发。

RequestMapping内存马：通过动态修改RequestMapping映射，将恶意方法绑定到特定的URL上，当访问该URL时触发恶意代码。

**什么是Controller-概念**

Spring的Controller作为Web请求的入口点，我们通常会在Controller中定义处理HTTP请求的方法，这些方法可以返回数据（如JSON）或视图（如HTML页面）。 在Spring中Controller是Spring MVC框架中的核心组件，**负责接收用户请求（接收HTTP请求（GET、POST、PUT、DELETE等））、处理业务逻辑（调用Service层处理业务逻辑）、返回响应结果（返回客户端内容）**。它是Web应用的"调度中心"，协调用户界面与后端服务之间的交互。Spring MVC中的Controller核心组件，包括Handler、Mapping、Method、HandlerMapping等。

Handler（处理器）：

Handler是处理请求的组件。它可以是任何类型的对象，但通常是我们编写的Controller类中的方法（即被@RequestMapping或其变体注解的方法）。Handler负责处理具体的请求，并返回模型和视图或直接返回数据。

Mapping（映射）：

映射指的是将HTTP请求（URL、方法、参数等条件）与特定的Handler关联起来的过程。可以通过注解（如@RequestMapping）或配置来定义映射。

Method（方法）：

这里特指Controller类中处理请求的具体方法。一个Controller类中可以有多个方法，每个方法都可以是一个独立的Handler，处理不同的请求。

HandlerMapping（处理器-映射关系）：

它的职责是根据请求（HttpServletRequest）找到对应的Handler（即处理请求的控制器方法）。可registerMapping() 方法动态注册映射关系

**核心特性**

1. 注解驱动：使用注解声明Controller和请求映射，减少XML配置，提高开发效率

2. 参数绑定：自动将请求参数绑定到方法参数，支持路径变量、查询参数、请求体等

3. 内容协商：根据Accept头返回不同格式数据，支持JSON、XML、HTML等多种媒体类型

4. 异常处理：统一的异常处理机制，可自定义错误响应格式

**创建Controller**

现在开始创建一个spring boot的项目，认识Controller：

首先到下图的站点直接下载demo，自动创建的项目，下载之后在idea中打开即可：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ic8BH9EFusn7ChuTKLqRTsriaK6dt5asKQ4bpEFyPWhDndiaLDdFefzibYm4y511fHibf6PeI1K4Nd3v6V8aEQJibgE8XaiagPxVg1qKtRt9LGN1ibg/640?wx_fmt=webp&from=appmsg)

打开之后项目结构是这样的：

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn7OEm7O47E0ckHanN9x83JaqQSwqfeaibcAGF7toBsLWyV0fS4cQQCUwNOKTe4libp3LQiar0Rg7htsHpibeKZJjLia17bhRfLM188M/640?wx_fmt=webp&from=appmsg)

在项目下新建一个自己的controller：FirstController.java，代码如下：

```
package com.example.demo.demos.web;import org.springframework.web.bind.annotation.GetMapping;import org.springframework.web.bind.annotation.RequestMapping;import org.springframework.web.bind.annotation.RestController;@RestController@RequestMapping("/api")  // 添加基础路径public class FirstController {    @GetMapping("/index")  // 通过@GetMapping注解，添加url访问路径public String index() {        return "index page";    }    // 可通过注解可以添加更多端点---url访问路径@GetMapping("/hello")    public String hello() {        return "Hello Spring Boot!";    }}
```

直接主函数启动项目：

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn7VtRxfJSd0rjvjsqwFl8QZt6p5byCGTtXtKTP50gLOjedrqFcB8BRJIIggrmWxIPOBUwKzbtWYgEt3b4084qlrDHKzicMRfHMg/640?wx_fmt=webp&from=appmsg)

访问http://127.0.0.1:8080/api/index 页面正常访问：

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn4cZTHgwfy8ib5kkhicAm8WQJRjmyHur8rmMQbIgbEAB9UpbnKwK2A3jlMXQsz9KTSs70CBDFJLjSJEIPL04ErAEtRs3gnUUZ2M8/640?wx_fmt=webp&from=appmsg)

**小结：**通过这里其实可以看出来，这跟java的servlet的配置很像（[java内存马之-servlet-手把手教你写内存马](https://mp.weixin.qq.com/s?__biz=Mzk5MDI5NDAyMw==&mid=2247484588&idx=1&sn=02abb069c2829b27e5888b688139066e&scene=21#wechat_redirect)），只是这里通过spring注解（@RequestMapping主路径配置，@GetMapping()主路径下的路径与方法绑定）的方式自动实现了，url访问路径与类的绑定关系。而且spring内置了tomcat启动web项目。

那么有没有可能思路是差不多的，只需要弄清楚这个绑定关系是如何实现的就可以了！现在来验证一下这个推断：

**controller加载过程分析**

**在启动应用的时候，spring就会将所有的已有的controller分别存放到mappingRegistry中，逐一注册！**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ic8BH9EFusn6zMbDAKxYMxXwtbtqxtZxLQqsULjWs9uWt5KxuGyNETbvrWk3ribPmXRibnJ8nRPKDibYhUNLh84TEfZdulwcjIvmMJLYvHPXHaw/640?wx_fmt=webp&from=appmsg)

现在通过调试的方式尝试找controller的请求过程中加载过程：

在firstController的index处test()方法打上断点：如下图所示，在执行我们的test的方法之前，通过反射执行了很多方法。通过反射执行可能与我们关注的没有太大关系。毕竟上面我们得到的结论可能跟servlet类似。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn704cVQtVBib3F8CfvwATaPjMRUuSYTkyzgibNs0joR9SjwsexrM7Y4iaR30gtzWPEvia6djvC2cziaYJnibQnkulLO4rrh1ia3fiboB60/640?wx_fmt=webp&from=appmsg)

直接来到下面的划线部分，果然看到了HttpServlet，且执行了对应的doGet方法，与servlet内存马分析的时候几乎一样！可能重点就在这附近。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ic8BH9EFusn5Ha9bbIdY2J9rRqvgiaPJPcTuIGwoDnm95vXpXicLX6LZ98cdljdSzEwMdvP7icmk30bp3b8dYt5vhCTXMBRXEFVymOHGxBtXPoE/640?wx_fmt=webp&from=appmsg)

并且该方法的参数中的request的attributes属性值中确实包含了我们的请求api/index。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn4mIaBz0Eputrpy0AqRWBWfBD2n06T9D8bBUlYZLvKDpCoxyuOwnk0Im1VAXv3U3ww34k4lV9xtbcMf5mKXZgsycYcpgvu3KmQ/640?wx_fmt=other&from=appmsg)

如下图结构：req 是一个RequestFacade对象，持有一个request对象，request对象中的属性attributes是一个hashMap，里面保存了我们自定义的controller相关信息，是分别存放的。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ic8BH9EFusn7FWIKg5rEDyBatE5R5Umt6T2NS9TshBE0sroLqGJuEUlDuVib53gzuNWo2As5mf5y8cLojrKnYKVgKChrtUlR4nyJiaxXPMscBw/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn4kmG6IqkFiaZMCkxkwOBjb5CtWShPNKUEKw7SSPHvLQ1FGdfU2dtC3Qg778Co7T6ffgdjEfrSvT6w6eMO6Hzicx49WylEscjxaU/640?wx_fmt=webp&from=appmsg)

然后再往下就是将这个request作为参数，调用其他方法，最终执行到了我们的自定义方法test()。

但是其中有一个问题需要知道：api/index如何与test()方法对应上的，这样我们访问index的时候，服务器才知道该执行对应的test()方法，而不是其他方法，类似servlet的映射关系。

跟进processRequest(request, response);这个方法，看下一步对request对象进行了哪些操作！

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ic8BH9EFusn5r3yYNian7W9QjOH45D1UcjdpQsODte2jNXJf2hicCt9AvZsHWiboS63riaDXGVg3qu7da0BPe6GLEx0TwNBWD8ZOlCXXI6W6878Q/640?wx_fmt=webp&from=appmsg)

又将其作为参数，执行了doService(request, response);方法。

**再这个方法里面对request请求进行了一系列赋值操作，将其中一个key值，设置了一个webApplicationContext对象：**

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn5yiaQAMxzVpib7V6GZ7m7G3M7PTQK4JV1p6VZVspNVadjzlBjKDXb0wf1EXU2HYHia2Xe7tmeZFZNolqB7BkYDqUlWfum9TnASLA/640?wx_fmt=webp&from=appmsg)

然后再次传递给doDispatch(request, response);方法

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn5PDXULwxXeclwG9ISyibmoIm9nCMruTiceZTwFhR2Aibr4gesibXAuPRrzWyaSpvOpl4KB8iaFNQpIc6NhOQxqalic19RL8Vk6qGgwo/640?wx_fmt=webp&from=appmsg)

该方法就对request做了很多操作了：先把他赋值给一个HttpServletRequest processedRequest = request; 变量。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn55R2vT1TxqmqAuibLC6tY8cdbPMPW3icdZ9SiaoKU3MgicYt6qvmj47P8Lj7ojopIHomsTRV3YQnCOMiaPia9XMI19UkicX8ohRlAzVE/640?wx_fmt=webp&from=appmsg)

然后从里面拿到了我们的请求信息api/index：

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn5o3AM02wXRIWuhrjBMibNicI1iaGu7rFJiaESXkHP3IhKjv0L8QHKFiafh1srHRxNEKj9Qjaklmz4q0n2XTnzRicDnslkT2mzM1ibjick/640?wx_fmt=webp&from=appmsg)

然后下一行得到一个mappedHandler，这个对象竟然是我们的FirstController的test()方法：

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn4FhL5tRB3Zkv45oCSrCp07s0e3H6NzTDalJMrpUJ64TiclOehbGTfA7EdUCxL2QKjMgZzTAxH0RFLVv6cmwiajWKHj7K8KgBYGU/640?wx_fmt=webp&from=appmsg)

并且该方法后面调用了doDispatch，将processedRequest，response，mappedHandler的handler属性一起作为参数执行。

```
// Actually invoke the handler.// 实际调用处理器。mv = ha.handle(processedRequest, response, mappedHandler.getHandler());
```

再往后就是一些反射调用，执行到我们的test()方法了。该方法前面还有注释，实际调用处理器（即我们写的Controller方法）处理请求。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn4iadaatLC2AkgeGO1liacc7OiaBPrDzZP5cQdXgQx9mBl1OtfICia7EiauMN7kdvXW4ib0zR3loHX0zZh7zc4Kic8x0913X2BlCwQ9Ak/640?wx_fmt=other&from=appmsg)

那么大概率doDispatch()方法里面，就对request请求进行了一些列操作，然后得到了对应得需要执行得方法。

回到下图中代码处mappedHandler得取值方法：

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn5AMwzMbRrLia1Ykibz7G4dXlb8yCQcTlwCb0wFSWd5mQX0dJWcUEgknyNpzRXWhUjBSvBrblxNLcOkhwv3L1uEfDYGBZ4EU7VAA/640?wx_fmt=other&from=appmsg)

这个方法前面也有个注（释// Determ...