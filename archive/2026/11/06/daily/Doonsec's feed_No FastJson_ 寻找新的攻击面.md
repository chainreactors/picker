---
title: No FastJson: 寻找新的攻击面
url: https://mp.weixin.qq.com/s/m8Hc0q8qDCBMsMdRVREh3g
source: Doonsec's feed
date: 2026-11-06
fetch_date: 2026-11-07T07:56:18.755984
---

# No FastJson: 寻找新的攻击面

# No FastJson: 寻找新的攻击面

原创

路人甲
路人甲

红细胞安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 前景回顾

在《FastJson 1.2.83 远程代码执行分析》一文中，我们简要分析了`fastjson 1.2.83`下无`gadget`的代码执行原理，其本质是由于双亲委派机制导致的。我们在前文分析的过程中，已经明白了为什么默认的`springboot fatjar`场景下无法打成单`http`实现代码执行的原因，是因为在走进`com.alibaba.fastjson.util.TypeUtils#loadClass(java.lang.String, java.lang.ClassLoader, boolean)`的时候，由于传入的`defaultClassLoader`为`null`，转而选用了`Thread.currentThread().getContextClassLoader()`来获取当前上下文类加载器，也就是内置的`TomcatEmbeddedWebappClassLoader`，其`loadClass`方法调用了`Class.forName`，然后在`forName0`校验的过程中对类名做了限制，导致无法实现单`http`的情况下`RCE`。只有当设置了`ParserConfig`的`defaultClassLoader`或者在其他中间件环境下其不为空的情况下，才能正常走进`URLClassLoader#loadClass`，这样才不会存在前置的`forName0`校验类名。

## No FastJson

眼尖的读者可能发现了其中的问题，在`TomcatEmbeddedWebappClassLoader`当中最终是通过`org.springframework.boot.web.embedded.tomcat.TomcatEmbeddedWebappClassLoader#loadFromParent`来加载我们的`payload`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0Xmic8iaCibOibcXhhXa3vgxKMRcWTeZOClYwH6qjv0lnhkzgkVAmfNrQyibXMVtQAicCyic0M0xdErmpBQFq0FIBNDlxkbrQQoxwpg6G4/640?wx_fmt=png&from=appmsg)

当中关键的是这个传入的`payload`并没有经过任何变化，最终保持了原始输入走到了这里，通过`Class.forName`触发了后续的类加载，而由于这里设置了第二个参数为`false`，导致在这里并不会执行类加载的初始化行为。

是不是可以有一个大胆的猜想，无需`fastjson`，仅通过`Class.forName`就能够触发呢？我们编写如下测试控制器来验证

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XkvFUHxvO4rWNW6FsUpkdtaRoPw1VjNPYdbjmoDPgXfXuj3juyMeiaA1ffJgfkyreibbb4bKdNyCl2328BAH26vdkicmBu9G1a0ZQ/640?wx_fmt=png&from=appmsg)

这在很多产品业务代码里是一个很常见的场景，甚至在不少组件状态传递的过程中也有这种场景。

前面我们说了，由于`Class.forName`的第二个参数为`false`，不会执行初始化行为，也就是在这里不会执行类当中的静态代码块，只有等到被主动触发的时候才会执行。所以这里我们的`payload`需要改动一下，不再使用`@JsonType`注解：

![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0Xm1ibt0g2ChcBibkLBaquoaOdgoicuYkgHwsavE9QfDyBFeo8TLYlH9gyjDsJOWoc22EQWt7VTRxS026aa8MkP52TkuccJjZscezc/640?wx_fmt=png&from=appmsg)

通过`javaassit`修改成特定类名后如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XmCuNJcnaPaDDmMM8YNmvUCFg1YUywsawLibVU2TG8yibkNjmriaIc7q75Ku24Hq7Pp7qnmJQrefqLpcZc8KxrwvzYqjt34c9ic0D8/640?wx_fmt=png&from=appmsg)

接着构造请求来验证猜想：

![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XmxiaC4pBianvE65bttALlgn9oU2micsKsIbAvnDmb1mbVxvHEQFbTpDYfricH3Q0bAiaAGKIJKofQCN7icXu9VMZtZ2GO3sKaUDJffs/640?wx_fmt=png&from=appmsg)

这里其实也不能使用`http`的方式来加载，因为走的还是`forName0`，会校验类名的合法性。

我们下断点来回顾一下这个过程

![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XmZPyh0YrRFxGw4mYQMh32N2XCUibDzLlp9F3QvlibThucicvtXo9XlznEic3o2s1dRJpficCFR5pAvibjaQORCcvNTtiaYwXVj79xPek/640?wx_fmt=png&from=appmsg)

这里通过`ClassLoader.getClassLoader(caller)`拿到了调用当前方法的类的类加载器（传入的`caller`就是调用`Class.forName`的类）

![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XlAuZKZs99N4sEeB9ibonycWqJQRUfibiaib66QoHYheyugREvYRE1GM6UTRadQzW5CibcEVNiaibIPktibhPrqLmAKDYibWZRHHsSaatgA/640?wx_fmt=png&from=appmsg)

接着往下走

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XnHyNCJiaicRR6c1vHFqom70j1LZonCq1koWUzF0wOA7JyrYx70ewxBFicY8y8vxHa9TrtPEVQibwSyHBSI9VEJMaVXaNm1vriaFuZ8/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0Xls1dkDKNYpr6UNQibt01OUFAja3SLj7D0ic8FS7YwwXLWcRBJLfuvEuoVgJaz91Cy7uYlTDB1xP2AibKEDb6D3icJkQDCCXr0QyzU/640?wx_fmt=png&from=appmsg)

到这里的后续逻辑和前文基本一致了

![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XnibsqupmoPv1OzMY0MsUkZNk0ickQP3741JvzV017USm4CtMJg14NzJ6fibLeTM4jp3w0hicvz3PvrL7lZke6UPTaiaIImBZ1Hy6fw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XmnyTXKHXGknqlE8kTEX4r1ziaadLMKfQytMFP0JQcicIL1uSsMF2U2RYdq4AoUe6kcPsF48cxr0YO2t2paytCogcJGWNLzKpCpE/640?wx_fmt=png&from=appmsg)

在`findClass`的过程中，`jdk`本身也会通过`getResource`来查找资源，而前文我们说过，`getResource`本质是通过`new URL`来实现的，自然支持`jar:`来加载资源。

所以到这里这个由于类加载导致的问题已经可以完全脱离`fastjson`本身，将漏洞利用的条件下降至只需要`fatjar + jdk`，且仅需要`Class.forName`可控即可，而实战场景中能够控制`Class.forName`的场景足够多，以历年最经典的`jdbc attack`来举例：

![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0Xl9y1ksWcgU7Yk0OHaxWJSLQTZpefdrbjj3icj8lZljib6liclibfnmQxLdqeicGMDfF5fI4FWbbGpQhLehEeVu6wibOIo0m48KWibQFw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XnlwPcvFG0IHRyfic2RzMvFlGGI2SrFU3QxTEvFDB1ibib2JUNg81SadRTUsZPOmQgbD6ConZiasgeIaVOJn8aYKGUo1HeenMW2yb4/640?wx_fmt=png&from=appmsg)

引入的均为最新版依赖，`mysql-connector-java 8.0.33`已经修复`getConnection`阶段触发的反序列化，而`postgresql 42.7.13`也早已修复`socketFactory`，将其限制在了期望类内。

而在目前仅需`Class.forName`可控就能`RCE`的加持下，这些限制都不再是问题，我们先以`mysql-connector-java 8.0.33`为例，其触发类加载的在`8.x`从`statementInterceptors`变为了`queryInterceptors`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0Xn61CDwbvdicsibrymR1wVwe2PiaVUJick9kibHgVgHZIQQaHxVf7Anlhmut5LW8ibgUo14YRibsxNG2ZeohCKOEhib4J1VtuvssJEyJibk/640?wx_fmt=png&from=appmsg)

指定该参数后，传入的类名会通过`com.mysql.cj.jdbc.ConnectionImpl#initializeSafeQueryInterceptors`当中的`Util.loadClasses`进行加载，但是这里限制了类型必须是`QueryInterceptor.class`

![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0Xnwby7CbicUiaaCtdPwragh4qmxCXAQDcBs1YfcN4M8pYcicIheiaUYKDmRJHpO2Xia3SX4KIZD0MDfeA9IDnREG5GrGCxeIBUmEKUE/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XmdR6x969eyJiaXW2TcWvCt24tSKrF3aY1lhLOXRNZgrAk6GQ2gZs6FRQJCKkKe9SOiabvN6FSTIrvq1pq3N10rKiaicCfHB8c8fKc/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XnswtplDicdXBecegeia46Z6icWQjyXwx5zj1mXfTUXMtgvy0tH91f1e9PcpUhE3voWje4SRBhjyKK0CBnByJR4h8ibMdsCOBibsHSo/640?wx_fmt=png&from=appmsg)

也就是如果类型不匹配，其不会继续构造实例。解决办法也很简单，给我们的恶意类加上实现`QueryInterceptor`接口即可，这里可以选择在其初始化的时候植入恶意代码或是无参构造等都可以

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0Xl7jMFslcZLic10NEMNTp5yxPPgKibRCQvBA0CcoZGkHlp0oFibAz1SyAuKANYHGWTzlynfeLmJrMETfkicSFmUrBOdafYzBWRmDicY/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0Xl52IR4pZnsFxpNMKGbhhAC9o7KMhCTGsmkGSvkm8zunBCYdpib2FdvWHVr2jSt1V30P88MLYoepicmZOuVXOUjA1YZN1D6KpgeY/640?wx_fmt=png&from=appmsg)

接着同样修改为特殊类名

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XnfIGb4ZibqLkMLHdmJBiaLuLLzZL7nQQxHBKzSbTHvTaWnyrZ1OibSUJUDVlzHUIElTqNiapJyHxQ29K9ddQB8TJVLn1iaibiaXfP4xA/640?wx_fmt=png&from=appmsg)

然后构造请求验证：

![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0Xn5h80IRxWVBSib1fLa9Tq0Zud69HSTA106fshAppY9BCnIEmBvRYm2HRSvrdZmqwxgcc5xrJWCJulcN550EI1LYhvPR78vXphY/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XmZoXOILdbxgXTqgAxGfH21QFkHicXuExzhH7s0xNe8tpSUBibrTGxzd53tC0Y3ax6Y1GwWC0hASu2phXicHBKicG0akPeNKQhDzQ0/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0Xkd7ZneuBMWHV7WWnQTocuCL83Wk95icQceIUHGicrSmaNl7rXWZ9iaiaEPqcIwrlazaW69iasU0SYK1ydV4tHDAcn9UQJlgSauZ4To/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XnvTHibkwTTtHVQrNbXVrpHAaNicKz1E9aOFILFnQ9xK5RCg7ULDa8dyiaHvRgCfdAKWcKaicFjwzYNZUWnNhQia4ndaKbOLtlSEAa0/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XkhbWebkHiauTmWt8L7SRuldhkd8zDVdbJT9PiaFNpknUwHFQlwgpY6LbmUaxia0yxja52mtBeZmELqxTaFlj0w2WhaTa3jvYocAg/640?wx_fmt=png&from=appmsg)

接下来换`PostgreSQL`，同样的也在之前的修复里判断了期望类

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaG8gHwQY0XlIHjoo3d6CmGibUOKYXr33ibia0HL0CmOFQnooKCcxZFCH9dWxbS7M9V2hvzj89wkWaTmBmhaofQlLfxhVica8oicwHA6Ux42ibHbos/640?wx_fmt=png&from=appmsg)

我们只需要给我们的恶意类继承至`SocketFactory`即可

![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XkEwxzJkjlCfxMU6xhUpVG3JgNqbIovasM8JPXaKIqr2do50SHaxic3MUPNiauM06w2RKNBwic3VxJgcYMptmQmb8cl9Q6nXERPwQ/640?wx_fmt=png&from=appmsg)

修改为特殊类名后：

![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XkRMPdia2CwATHrEBQUQJRIUl28q3GjJtUmyShtaa7icaTibibxsc8Tnd8xEKicMla5M33fiby9lgzH3UCFWrGOTQITib9mUFXHD2Aibno/640?wx_fmt=png&from=appmsg)

接着构造请求继续验证：

![](https://mmbiz.qpic.cn/mmbiz_png/iaG8gHwQY0XnQbicCoow1a8JyTkOf9OWT3JFkz7ibxDJWiaHiavg3dh3gHXGxfOraPvZGbzVicAibSwqun7v3LJciaGLEh29PFPXkmXzTHNXe9N0lPk/640?wx_fmt=png&from=appmsg)

## 最后

`jdbc`场景只是抛砖引玉，相信未来会有更多姿势来利用这个点。目前实测很多产品在此基础上可以老洞开新花，剩下的玩法留给读者自行探索了。

本文当中所提及知识来自实战代码审计班课程内容，关于该产品更加深入利用手法可以咨询课程。

顺便再推荐一下我师傅的代码审计课程。近期某报表的课程章节已结束，马上开启新的章节，感兴趣的朋友可以尽快加入。课程中包含各类产品最新补丁对应的 0day 漏洞（非水洞） 的挖掘与分析；过往课程也涵盖多款市面产品的 0day / 1day / nday 漏洞案例讲解。课程后续会持续更新推进，支持一次报名长期学习与答疑。适合真正对代码审计感兴趣、或想系统学习但缺少思路与方法体系的同学（如有其他目的请勿打扰）。对基础要求不高，能读懂代码即可，真正帮助你从只能读懂代码到找到问题。个人学习过程中受益良多，特此分享推荐给希望提升自己的朋友（非广告）。若有打扰，敬请见谅。

下方是进阶班课表

![图片](https://mmbiz.qpic.c...