---
title: Java agent注入技术初探 - 郑瀚Andrew
url: https://buaq.net/go-168167.html
source: unSafe.sh - 不安全
date: 2023-06-11
fetch_date: 2025-10-04T11:44:37.587824
---

# Java agent注入技术初探 - 郑瀚Andrew

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/733bfe485b1bb89ce1571f0b297241ae.jpg)

Java agent注入技术初探 - 郑瀚Andrew

拿常规的hook和event callback技术进行类比可以按照如下通俗理解：JVMTI相当于操作系统原生提供的hook和event callback回调框架，它是一个事件驱动的工具实现接
*2023-6-10 21:16:0
Author: [www.cnblogs.com(查看原文)](/jump-168167.htm)
阅读量:48
收藏*

---

![](https://img2023.cnblogs.com/blog/532548/202306/532548-20230607110642164-830747121.png)

拿常规的hook和event callback技术进行类比可以按照如下通俗理解：

* JVMTI相当于操作系统原生提供的hook和event callback回调框架，它是一个事件驱动的工具实现接口，通过JVMTI才能对JVM内部状态进行感知和交互
* instrumentation API相当于hook和event callback回调API接口，是具体实现和JVM交互的API实现接口，它原生支持了JVM内部类的Hook劫持机制
* Agent相当于一个独立于操作系统内核的第三方程序，JVM内部状态感知和交互的事情不太适合在JVM内部集成，而是通过一个外部的第三方Agent来完成
* 字节码生成库相当于Shellcode/so/exe/elf生成器，用于生成具体的符合JVM规范的hook函数代码逻辑
* 启动时静态挂载（premain）相当于LD\_PRELOAD机制或者Boot启动机制注入，可以实现在JVM应用启动前执行agent的代码逻辑，premain是注入shellcode/so的入口函数
* 运行时动态挂载（agentmain）相当于ptrace动态so/dll/shellcode注入技术，区别在于JVM原生支持的Attach API内部就集成了进程间通信功能，相比于ptrace shellcode注入技术，VirtualMachine要更加稳定。agentmain是注入shellcode/so的入口函数

## 0x1：JVMTI介绍

关于JVM TI技术，官方文档的解释如下：

The JVM tool interface (JVM TI) is a native programming interface for use by tools. It provides both a way to inspect the state and to control the execution of applications running in the Java virtual machine (JVM). JVM TI supports the full breadth of tools that need access to JVM state, including but not limited to:

* profiling
* debugging
* monitoring
* thread analysis
* coverage analysis tools

**Note:** JVM TI was introduced at JDK 5.0. JVM TI replaced the Java Virtual Machine Profiler Interface (JVMPI) and the Java Virtual Machine Debug Interface (JVMDI) which, as of JDK 6, are no longer provided.

JVMTI（Java Virtual Machine Tool Interface）是一套由 Java 虚拟机提供的，为 JVM 相关的工具提供的 Native 接口集合。JVMTI 是从 Java SE 5 开始引入，整合和取代了以前使用的 Java Virtual Machine Profiler Interface (JVMPI) 和 the Java Virtual Machine Debug Interface (JVMDI)，而在 Java SE 6 中，JVMPI 和 JVMDI 已经消失了。

JVMTI 提供了一套”代理”程序机制，可以支持第三方工具程序以代理的方式连接和访问 JVM，并利用 JVMTI 提供的丰富的编程接口，完成很多跟 JVM 相关的功能。从 Java SE 5 开始，可以使用 Java 的Instrumentation 接口（java.lang.instrument）来编写 Agent。无论是通过 Native 的方式还是通过 Java Instrumentation 接口的方式来编写 Agent，它们的工作都是借助 JVMTI 来进行完成。

JVMTI和Instumentation API的作用很相似，都是一套 JVM 操作和监控的接口，且都需要通过 agent 来启动：

* Instumentation API​需要打包成 jar，并通过 Java agent 加载（对应启动参数: -javaagent，或者通过attach api动态注入）
* JVMTI 需要打包成动态链接库（随操作系统，如.dll/.so 文件），并通过 JVMTI agent 加载（对应启动参数:-agentlib/-agentpath，或者通过attach api动态注入）

## 0x2：加载时机

* 启动时（Agent\_OnLoad）
* 运行时 Attach（Agent\_OnAttach）

## 0x3：功能

Instumentation API 可以支持 Java 语言实现 agent 功能，但 Instumentation API 本身是基于 JVMTI 实现的，JVMTI 功能比 Instumentation API 更强大，它支持：

* 获取所有线程、查看线程状态、线程调用栈、查看线程组、中断线程、查看线程持有和等待的锁、获取线程的 CPU 时间、甚至将一个运行中的方法强制返回值……
* 获取 Class、Method、Field 的各种信息，类的详细信息、方法体的字节码和行号、向 Bootstrap/System Class Loader 添加 jar、修改 System Property……
* 堆内存的遍历和对象获取、获取局部变量的值、监测成员变量的值……
* 各种事件的 callback 函数，事件包括：类文件加载、异常产生与捕获、线程启动和结束、进入和退出临界区、成员变量修改、gc 开始和结束、方法调用进入和退出、临界区竞争与等待、VM 启动与退出……
* 设置与取消断点、监听断点进入事件、单步执行事件……

## 0x4：JVMTI 与 Java agent

Java agent 是基于 JVMTI 实现，核心部分是 ClassFileLoadHook和TransFormClassFile。

* ClassFileLoadHook​是一个 JVMTI 事件，该事件是 Instrumentation agent 的一个核心事件，主要是在读取字节码文件回调时调用，内部调用了TransFormClassFile的函数。
* TransFormClassFile​的主要作用是调用java.lang.instrument.ClassFileTransformer的tranform​方法，该方法由开发者实现，通过Instrumentation的addTransformer方法进行注册。

在字节码文件加载的时候，会触发ClassFileLoadHook​事件，该事件调用TransFormClassFile​，通过经由Instrumentation​ 的 addTransformer 注册的方法完成整体的字节码修改。

对于已加载的类，需要调用retransformClass​函数，然后经由redefineClasses​函数，在读取已加载的字节码文件后，若该字节码文件对应的类关注了ClassFileLoadHook​事件，则调用ClassFileLoadHook事件。后续流程与类加载时字节码替换一致。

参考链接：

```
https://docs.oracle.com/javase/8/docs/technotes/guides/jvmti/
```

关于Java Interface Instrumentation技术，官方文档的解释如下：

```
public interface Instrumentation
```

This class provides services needed to instrument Java programming language code.

Instrumentation is the addition of byte-codes to methods for the purpose of gathering data to be utilized by tools. Since the changes are purely additive, these tools do not modify application state or behavior.

Examples of such benign tools include

* monitoring agents
* profilers
* coverage analyzers
* event loggers

There are two ways to obtain an instance of the `Instrumentation` interface:

1. When a JVM is launched in a way that indicates an agent class. In that case an `Instrumentation` instance is passed to the `premain` method of the agent class.
2. When a JVM provides a mechanism to start agents sometime after the JVM is launched. In that case an `Instrumentation` instance is passed to the `agentmain` method of the agent code.

Once an agent acquires an `Instrumentation` instance, the agent may call methods on the instance at any time.

JDK™5.0中引入包java.lang.instrument。 该包提供了一个Java编程API，可以用来开发增强Java应用程序的工具，例如监视它们或收集性能信息。 使用 Instrumentation，开发者可以构建一个独立于应用程序的代理程序（Agent），用来监测和协助运行在 JVM 上的程序，甚至能够替换和修改某些类的定义。有了这样的功能，开发者就可以实现更为灵活的运行时虚拟机监控和 Java 类操作了，这样的特性实际上提供了一种虚拟机级别支持的 AOP 实现方式，使得开发者无需对 JDK 做任何升级和改动，就可以实现某些 AOP（AOP核心理念是定义切入点（pointcut）以及通知（advice）。程序控制流中所有匹配该切入点的连接点（joinpoint）都将执行这段通知代码）的功能了。

在 Java SE 6 里面，instrumentation 包被赋予了更强大的功能，所有这些新的功能，都使得 instrument 包的功能更加丰富，从而使 Java 语言本身更加强大，包括：

* **启动后的 instrument**。在 Java SE6 里面，最大的改变是运行时的 Instrumentation 成为可能。在 Java SE 5 中，Instrument 要求在运行前利用命令行参数或者系统参数来设置代理类，在实际的运行之中，虚拟机在初始化之时（在绝大多数的 Java 类库被载入之前），instrumentation 的设置已经启动，并在虚拟机中设置了回调函数，检测特定类的加载情况，并完成实际工作。但是在实践中，有很多的情况，我们没有办法在虚拟机启动之时就为其设定代理，这样实际上限制了 instrument 的应用。而 Java SE 6 的新特性改变了这种情况，通过 Java Tool API 中的 attach 方式，我们可以很方便地在运行过程中动态地设置加载代理类，以达到 instrumentation 的目的。
* **本地代码（native code）instrument**。对 native 的 Instrumentation 也是 Java SE 6 的一个崭新的功能，这使以前无法完成的功能 —— 对 native 接口的 instrumentation 可以在 Java SE 6 中，通过一个或者一系列的 prefix 添加而得以完成。
* **动态改变 classpath**。Java SE 6 里的 Instrumentation 也增加了动态添加 class path 的功能。
* 等等

这些改变，意味着 Java 具有了更强的动态控制、解释能力，它使得 Java 语言变得更加灵活多变。

java.lang.instrument包的具体实现，依赖于 JVMTI。在 Instrumentation 的实现当中，存在一个 JVMTI 的代理程序，通过调用 JVMTI 当中 Java 类相关的函数来完成 Java 类的动态操作。

Instrumentation 的最大作用，就是类定义动态改变和操作。在 Java SE 5 及其后续版本当中，开发者可以在一个普通 Java 程序（带有 main 函数的 Java 类）运行时，通过 –javaagent参数指定一个特定的 jar 文件（包含 Instrumentation 代理）来启动 Instrumentation 的代理程序。

Instrumentation 的一些主要方法如下：

```
public interface Instrumentation {
    /**
     * 注册一个Transformer，从此之后的类加载都会被Transformer拦截。
     * Transformer可以直接对类的字节码byte[]进行修改
     */
    void addTransformer(ClassFileTransformer transformer);

    /**
     * 对JVM已经加载的类重新触发类加载。使用的就是上面注册的Transformer。
     * retransformClasses可以修改方法体，但是不能变更方法签名、增加和删除方法/类的成员属性
     */
    void retransformClasses(Class<?>... classes) throws UnmodifiableClassException;

    /**
     * 获取一个对象的大小
     */
    long getObjectSize(Object objectToSize);

    /**
     * 将一个jar加入到bootstrap classloader的 classpath里
     */
    void appendToBootstrapClassLoaderSearch(JarFile jarfile);

    /**
     * 获取当前被JVM加载的所有类对象
     */
    Class[] getAllLoadedClasses();
}
```

其中最常用的方法是addTransformer(ClassFileTransformer transformer)​，这个方法可以在类加载时做拦截，对输入的类的字节码进行修改，其参数是一个ClassFileTransformer接口，定义如下：

```
public interface ClassFileTransformer {

    /**
     * 传入参数表示一个即将被加载的类，包括了classloader，classname和字节码byte[]
     * 返回值为需要被修改后的字节码byte[]
     */
    byte[]
    transform(  ClassLoader         loader,
                String              className,
                Class<?>            classBeingRedefined,
                ProtectionDomain    protectionDomain,
                byte[]              classfileBuffer)
        throws IllegalClassFormatException;
}
```

addTransformer​方法配置之后，后续的类加载都会被Transformer拦截。对于已经加载过的类，可以执行retransformClasses​来重新触发这个Transformer​的拦截。类加载的字节码被修改后，除非再次被retransform，否则不会恢复。

在运行时，我们可以通过Instrumentation的redefineClasses​方法进行类重定义，在redefineClasses方法上有一段注释需要特别注意...