---
title: Goby 利用内存马中的一些技术细节【技术篇】
url: https://www.4hou.com/posts/XVmm
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-30
fetch_date: 2025-10-04T11:06:04.991146
---

# Goby 利用内存马中的一些技术细节【技术篇】

Goby 利用内存马中的一些技术细节【技术篇】 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Goby 利用内存马中的一些技术细节【技术篇】

Goby
[行业](https://www.4hou.com/category/industry)
2023-03-29 11:52:09

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)122144

收藏

导语：前置漏洞的利用、内存马的生成以及内存马的使用

**0×01 前言**

投稿在 Goby 社区的内存马文章已经写了两篇，在第一篇《 [Shell 中的幽灵王者-JAVAWEB 内存马【认知篇】](http://mp.weixin.qq.com/s?__biz=MzI4MzcwNTAzOQ==&mid=2247521497&idx=1&sn=50e062aa20930102e6b787711d0e214a&chksm=eb847f79dcf3f66f1ac0d14065fdef2576393e9142f36c5add4e738eebbf3b71410a79e759ef&scene=21#wechat_redirecthttps://www.4hou.com/posts/zlkq)》中介绍了 JavaWeb 内存马技术的历史演变、分类，从认知层面对常见的 JavaWeb 内存马技术进行了介绍；第二篇《 [用Goby通过反序列化漏洞一键打入内存马【利用篇】](http://mp.weixin.qq.com/s?__biz=MzI4MzcwNTAzOQ==&mid=2247521997&idx=1&sn=d3c444f95c97f06b1d24240a91bd898d&chksm=eb847d6ddcf3f47b0c50ab4a97b2adbee3241149d9a3ac5a56958e76ac33ede48e0bbd108952&scene=21#wechat_redirecthttps://www.4hou.com/posts/xjK3)》中主要介绍了如何将内存马与漏洞进行初步结合，使 Goby 可以通过反序列化漏洞一键打入内存马，并与 Goby 的 PoC、插件系统融合，使用者只需要点点点就可以完成一键化漏洞的打入。

 本篇作为 Goby 社区内存马文章的第三篇，主要从技术方面介绍一下，在前两篇文章的基础上，在使用 Goby 通过反序列化漏洞一键打入内存马的过程中，所使用的一些技术细节。

 当然，在使用 Goby PoC 进行打入的过程中，使用者无需知道这些细节，但是了解和学习技术有助于掌握一些通用的思路。

 本文主要分为三个部分：“前置漏洞的利用”、“内存马的生成”以及“内存马的使用”，给大家分享一些 Goby 中相关的技术点和其中的细节或坑，欢迎大家一起讨论。

这里简单演示一下相关的技术的一些使用效果，以下视频演示了使用 Goby 通过反序列化一键注入 Filter 型内存马，并通过自定义 URLClassLoader 携带虚假信息，来躲避安全人员的排查，并且通过清除日志来达到无痕的目的。

上传视频封面

[使用 Goby 通过反序列化一键注入 Filter 型内存马视频](https://www.bilibili.com/video/BV18g4y1s7Ai/?spm_id_from=333.999.0.0)

Goby一键打入内存马功能可在社区版免费使用，[Goby - Attack surface mapping](https://gobysec.net/updates)

##

**0×02 前置漏洞利用**

首先来说下前置漏洞利用部分，之前的文章提到，作为实战化漏洞利用、武器化开发的视角，我们更倾向于在漏洞利用过程中，一键化打入内存马，而不是先拿到 JSP webshell 再转为内存马，因此，这里需要考虑在漏洞利用过程中如何直接执行内存马的植入动作。

## 2.1 动态加载与类的初始化

在目前大多数的漏洞利用中，如果想要执行复杂的恶意攻击逻辑，一般都是使用新建 URLClassLoader、当前线程的类加载器、自定义类加载器等来进行恶意类字节码的装载及初始化。

在不同的利用场景下，可以看情况选取不同的类加载器来实现，但也有的时候没办法选择，需要看情况进行调整：

* 使用新建 URLClassLoader，如果没有指定，则默认使用系统类加载器作为 parent ClassLoader，也就是 AppClassLoader；
* 使用当前线程的上下文类加载器，一般使用Thread.currentThread().getContextClassLoader() 获取；
* 新建自定义类加载器，一般是定义一个通过字节码进行类加载的方法，就相当于封装一个 public 的 defineClass 方法；
* 在某些利用场景下，无法自定义 ClassLoader ，例如 BCEL ClassLoader 的利用途径等。

在不同情况下，使用不同的 ClassLoader 加载恶意类，将会面临不同的问题：

* 使用当前线程的上下文类加载器，或无法控制类加载器时，可能存在同一类名无法加载两次的情况，需要额外处理；
* 在使用例如 BCEL ClassLoader 等特殊的 ClassLoader 时，由于跨类加载加载的问题，需要通过纯反射对一些类和接口进行访问和调用，面临比较大的体力工作。

在漏洞利用的过程中进行动态类加载时，普遍的情况是需要人为的打破双亲委派机制，将恶意类注入到系统中。

与类加载息息相关的就是类的初始化，通常在恶意代码中，会写一些初始化的恶意逻辑，一般可以写在 static 语句块或 public 无参构造方法中：

* static 语句块在类加载的时候执行一次，在其生命周期只执行一次；
* public 无参构造方法在类初始化的时候进行调用，每次新建类实例会调用。

因此，可以根据具体的情况选择类加载器，与将恶意逻辑放置在什么位置。

## 2.2 回显与内存马

在 Goby 反序列化打入内存马的插件上线后，我对漏洞库中反序列化漏洞的利用均进行了增强与修正。

 熟悉 Goby 的朋友可能知道，Goby 对于漏洞利用的检测分为 PoC 与 EXP，在面对 Java 原生反序列化时，原本的检测和利用程序为：

* PoC 使用 URLDNS 配合 Goby 自带的 dnslog 平台 GodServer 进行漏洞检测；
* EXP 使用 YSOSERIAL 的字节码，动态替换命令执行部分的 hex 值，进行命令执行的写入。

使用上述逻辑漏洞的检出，是大部分人员面对反序列化漏洞的检测方式，技术上这种检测方式并没有问题，但是实际执行中会遇到如下问题：

1. 由于网络或 DNSLOG 平台不稳定，可能导致收不到 DNSLOG 的问题，或者 DNSLOG 有较长的延时；

2. 漏洞利用仅仅进行命令执行，时常无法得知漏洞利用是否成功，也无法知道漏洞执行的结果；

3. 在不出网的情况下，无法进行反弹 shell，也无法执行更高级的动作，对实战来说，实用性很差。

因此，为了解决实战化的可用性问题，在后续更新的漏洞利用 PoC 均采用了回显的技术，将命令执行的结果返回 response 中；而 EXP 中则是直接打入内存马，节省了中间的很多过程。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230328/1680001217140139.png "1680001217140139.png")

在构造回显时，则涉及到关键 request 的定位，搜索内存等技术点，而内存马的打入，则又需要针对漏洞环境准备高可用的内存马，有了这些技术加持，可以解决上面提到的问题，无需第三方 dnslog、OOB 等，直接进行漏洞的高精准检测与利用。

## 2.3 条条大路通内存马

漏洞种类有非常多，能提供任意代码执行的种类也非常多，例如 Java 原生反序列化漏洞、Fastjson/Jackson/XStream 反序列化漏洞、SpEL/Ognl 等表达式注入等。但有很多情况需要额外的利用方式，才能打通漏洞利用的流程，这里以原生反序列化利用为例，列举一些利用链的改造，使其直接可以进行内存马的打入。

* Transformer[] 利用链，最经典的利用链，一般是 chain 一个 Runtime.getRuntime().exec() 或者 new ProcessBuilder().start() 来进行命令执行。
  如果想执行一些额外的功能，还可以使用 new URLClassLoader().loadClass() 来进行远程类加载。
  在不出网的情况下，可以通过 com.sun.org.apache.bcel.internal.util.ClassLoader.loadClass()、org.mozilla.javascript.DefiningClassLoader().defineClass()、new ScriptEngineManager().getEngineByName("JavaScript").eval() 的方式写入 JS 进行恶意类的打入，一键利用内存马。

![](https://pica.zhimg.com/80/v2-a06c705b36cabd503aa4b128ad0cd6c2_720w.png?source=d16d100b)

* BeanShell 利用链，虽然 Bsh 支持全部 Java 语法及很多松散写法，但是说到底还是脚本语言的解析，如果使用了这些写法或脚本中使用了数组等，在反序列化过程中会调用相关实现类的相关方法，可能用到 Interpreter 对象，报空指针，因此还是可以使用 ScriptEngineManager 解析 JS 的方式执行内存马。

![](https://pic1.zhimg.com/80/v2-3ca024500da3dde8e6b260031945c589_720w.png?source=d16d100b)

* C3P0 在原版中，C3P0 链使用了 PoolBackedDataSource 进行远程类加载来进行漏洞利用。
  但实际上，C3P0 还可以通过Tomcat 的 getObjectInstance 方法调用 ELProcessor 的 eval 方法实现表达式注入，可以通过 EL 表达式来进行内存马的打入，除了 EL 表达式，还可以使用 Groovy、SnakeYaml 等。

![](https://pic1.zhimg.com/80/v2-a57b903706b43a21045f7f9759a34f2d_720w.png?source=d16d100b)

这里随便举了几个反序列化利用链串联到内存马的技术思路，除此之外还有更多的漏洞利用情况，可以酌情进行“曲线救国”，考虑到行文的篇幅，这里就不在赘述更多的思路。

**0×03 内存马的生成**

说过了前置的漏洞利用方向，接下来，讲下在内存马生成过程中涉及到的一些技术细节。

## 3.1 动态生成技术

考虑到不同漏洞利用点，不同的漏洞利用场景和需求，不同人员的习惯不同等，在实际环境中，内存马的内容不能是一成不变的，需要根据种种配置进行动态生成。

 因此，这里使用 javassist 进行内存马恶意类字节码的动态生成与写入。在内存马的准备过程中，将会面临一些的一些需求：

* 漏洞利用方式是固定的，例如命令执行、常用的冰蝎、哥斯拉或者自研的 webshell 交互工具，基本都是可复用的自定义漏洞利用方式；
* 内存马能够自定义 URL 、自定义密码，除了常见的 AES 密钥，还可以设置额外的鉴权机制；
* 可以随意选用任意一种内存马技术，使用任意一种利用方式，均可以快速动态生成。

因此，我这里将关键逻辑最终抽象成一个相同的方法，这个方法的前两个参数分别是 Request 和 Response 对象，无论是命令执行、冰蝎、哥斯拉等等，都可以在这个方法下注入自己的逻辑。对于不同的中间件，由于封装和实现和不同，在进入关键逻辑前进行额外的判定以及处理，使最终处理逻辑一致。

例如下面是冰蝎的核心逻辑：

![](https://pica.zhimg.com/80/v2-24645822e1c161e0bfd7fa3970cfba21_720w.png?source=d16d100b)

下面是哥斯拉的核心逻辑：

![](https://pica.zhimg.com/80/v2-69eb8fea69cddcdceddd8b3ac13f5afd_720w.png?source=d16d100b)

下面是命令执行的逻辑：

![](https://picx.zhimg.com/80/v2-4f5d89bfe05df3dfd73359f89395f33b_720w.png?source=d16d100b)

在确定了利用的参数后，则可以根据不同的内存马类型、不同的利用方式进行字节码的组装，将关键方法依次插入恶意类，最终形成一个完整的内存马。

## 3.2 ClassLoader 的问题

之前提到了在恶意类的动态加载和初始化时，要考虑 ClassLoader 的选取问题，这里在内存马加载后也一样，有关 ClassLoader 的问题需要额外注意。
第一种情况，作为内存马文件本身，一般需要将自身的实例放在处理路由的关键位置中，如全局上下文的某个 Map 成员变量中，这种情况就需要传递一个实例的引用，只要在内存马恶意类初始化时将自身对象的一个实例注册在系统内关键位置即可。
但是也有例外，例如在 Struts2 框架中，关键位置中储存的不是类实例，而是类名，在处理路由时，如果找到映射，则动态创建类实例并调用其 execute 方法进行处理，因此，在进行恶意内存马的注入时，不应单单进行类名和路由的映射，还应该将内存马自身类加载到关键上下文中，使其在实例化类时能够找到我们注入的恶意类。
在利用方式上，除了命令执行回显外，内存马的关键逻辑依旧还是通过传递类字节码来实现的。涉及到类加载的部分，除了之前提到的 URLClassLoader、自定义 ClassLoader、线程上下文类加载器之外，依旧可以玩出很多的花样：

* 使用 java.lang.reflect.Proxy#defineClass0() 注册类；
* 使用 sun.misc.Unsafe#defineAnonymousClass() 向 JVM 中直接注册类；

也可以使用一些封装类，这些封装类可能调用一些不常见的 ClassLoader 等：

* 使用 jdk.nashorn.internal.runtime.ScriptLoader#installClass() 注册对象
* 使用 com.sun.naming.internal.VersionHelper#loadClass()

除了上面这些，还有 JavaSec 群友分享了他找到一些方法：

* jxxload\_help.PathVFSJavaLoader#loadClassFromBytes
* org.python.core.BytecodeLoader1#loadClassFromBytes
* sun.org.mozilla.javascript.internal.DefiningClassLoader#defineClass
* java.security.SecureClassLoader#defineClass
* org.mozilla.classfile.DefiningClassLoader#defineClass

## 3.3 利用方式

对于内存马利用方式，最常见的三种利用即是，命令执行回...