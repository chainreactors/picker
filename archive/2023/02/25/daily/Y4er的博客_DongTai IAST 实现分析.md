---
title: DongTai IAST 实现分析
url: https://y4er.com/posts/dongtai-iast/
source: Y4er的博客
date: 2023-02-25
fetch_date: 2025-10-04T08:01:34.352370
---

# DongTai IAST 实现分析

[Y4er的博客](/ "Y4er的博客")

[归档](/posts/) [专栏](/series/) [分类](/categories/) [标签](/tags/) [笔记](/note/) [朋友](/friends/) [作品](/showcase/)

浅色深色跟随系统

[Y4er的博客](/ "Y4er的博客")

取消

[归档](/posts/)[专栏](/series/)[分类](/categories/)[标签](/tags/)[笔记](/note/)[朋友](/friends/)[作品](/showcase/)

浅色深色跟随系统

## 目录

* [模块](#模块)
* [dongtai-agent模块](#dongtai-agent模块)
* [dongtai-core模块](#dongtai-core模块)
* [如何实现污点传播](#如何实现污点传播)
* [总结](#总结)

## 目录

* [模块](#模块)
* [dongtai-agent模块](#dongtai-agent模块)
* [dongtai-core模块](#dongtai-core模块)
* [如何实现污点传播](#如何实现污点传播)
* [总结](#总结)

# DongTai IAST 实现分析

![Y4er avatar](/img/avatar.jpg)[Y4er](https://github.com/Y4er "Author")
 收录于  类别 [代码审计](/categories/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/)

2023-02-24  2023-02-24  约 4833 字
 预计阅读 22 分钟

目录

* [模块](#模块)
* [dongtai-agent模块](#dongtai-agent模块)
* [dongtai-core模块](#dongtai-core模块)
* [如何实现污点传播](#如何实现污点传播)
* [总结](#总结)

警告

本文最后更新于 2023-02-24，文中内容可能已过时。

# # 模块

DongTai-agent-java 由agent.jar、dongtai-core.jar 、dongtai-inject.jar、dongtai-servlet.jar四部分构成，其中：

1. agent.jar用来管理 agent 的生命周期和配置。agent 的生命周期包括下载、安装、启动、停止、重启、卸载。agent 的配置包括配置应用启动模式、漏洞检验模式、是否开启代理等。
2. dongtai-core.jar是核心 jar 包，其主要功能是：字节码插桩、数据采集、数据预处理、数据上报、第三方组件管理等。
3. dongtai-inject.jar是间谍 jar 包，用于注入至BootStrap ClassLoader，后续在目标应用中调用dongtai-core.jar中的数据采集方法。
4. dongtai-servlet.jar用于获取应用发送的请求以及收到的响应，用于数据展示以及请求重放功能。

# # dongtai-agent模块

`dongtai-agent/pom.xml:109`

指定了agent的入口点

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/c31ba46a-62f8-784e-6380-1cb7fbe43fed.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/c31ba46a-62f8-784e-6380-1cb7fbe43fed.png "image.png")

image.png

Premain-Class是通过`java -javaagent:agent.jar -jar app.jar`这种指定agent方式中首先进入的agent程序入口点 premain
Agent-Class 是通过attach的入口点 agentmain

`io.dongtai.iast.agent.AgentLauncher`和`io.dongtai.iast.agent.Agent`

Agent类通过`io.dongtai.iast.agent.Agent#doAttach` jattach.exe 将jar包注入到jvm进程中

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/bc2d3aab-b93d-93ad-d507-66bf830de6ee.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/bc2d3aab-b93d-93ad-d507-66bf830de6ee.png "image.png")

image.png

其实就是调用了 io.dongtai.iast.agent.AgentLauncher#agentmain

不管是premain还是agentmain最终都会进行安装判断，进入`io.dongtai.iast.agent.AgentLauncher#install`

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/52de4daa-c5b0-e9bc-a544-a889b2d2f596.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/52de4daa-c5b0-e9bc-a544-a889b2d2f596.png "image.png")

image.png

上报注册事件，然后进入`io.dongtai.iast.agent.AgentLauncher#loadEngine`

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/2c81a538-91ed-5532-739f-9c9fdc9d7611.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/2c81a538-91ed-5532-739f-9c9fdc9d7611.png "image.png")

image.png

将inst对象传给io.dongtai.iast.agent.manager.EngineManager创建一个引擎管理器的单例对象，然后用这个对象创建一个监控线程，调用io.dongtai.iast.agent.monitor.MonitorDaemonThread#startEngine 启动引擎

并且启动了agentMonitorDaemonThread后台监控线程

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/6b886db3-d47b-47e4-6963-9f4b48673e35.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/6b886db3-d47b-47e4-6963-9f4b48673e35.png "image.png")

image.png

监控线程会启动更多的子线程来监控心跳、性能、配置等等

关键在 io.dongtai.iast.agent.monitor.MonitorDaemonThread#startEngine

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/a3465831-8bb8-a45b-cae6-9c7216688a03.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/a3465831-8bb8-a45b-cae6-9c7216688a03.png "image.png")

image.png

extractPackage判断自身依赖包`agent.jar`、`dongtai-core.jar` 、`dongtai-inject.jar`、`dongtai-servlet.jar`是否存在

install将dongtai-inject.jar加入到BootstrapClassLoader，新建了一个IastClassLoader对象加载dongtai-core.jar中的`com.secnium.iast.core.AgentEngine`类，调用其install函数

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/1dc71852-98ab-b04f-0750-9e68b945e316.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/1dc71852-98ab-b04f-0750-9e68b945e316.png "image.png")

image.png

由此，该模块就是注入了一个dongtai-inject.jar到bootstrapclassloader，然后反射调用`com.secnium.iast.core.AgentEngine#install`

# # dongtai-core模块

com.secnium.iast.core.AgentEngine#install 根据上面的反射传递过来的参数来初始化AgentEngine引擎，然后run

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/ffc7e50c-a5ab-6ccd-c859-90f5aee86778.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/ffc7e50c-a5ab-6ccd-c859-90f5aee86778.png "image.png")

image.png

构造函数中有两个IEngine对象 ConfigEngine TransformEngine

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/6c0f088c-11fa-8296-af96-f3c5e627ec52.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/6c0f088c-11fa-8296-af96-f3c5e627ec52.png "image.png")

image.png

在初始化引擎init时会调用这两个对象的init，并且传递属性配置和策略管理对象

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/af14fee4-500b-9979-81ec-eabb9e89ef01.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/af14fee4-500b-9979-81ec-eabb9e89ef01.png "image.png")

image.png

io.dongtai.iast.core.init.impl.ConfigEngine#init 中加载策略

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/12b71cce-5461-7ae3-7184-1b7b515f6fb4.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/12b71cce-5461-7ae3-7184-1b7b515f6fb4.png "image.png")

image.png

io.dongtai.iast.core.init.impl.TransformEngine#init 中初始化Transformer转换对象

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/1cd51cb6-86d1-04ea-6bf3-ca89e66600d7.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/1cd51cb6-86d1-04ea-6bf3-ca89e66600d7.png "image.png")

image.png

在引擎run时会调用IEngine的start

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/8f37ee60-246a-1466-4b1b-29e446cd0771.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/8f37ee60-246a-1466-4b1b-29e446cd0771.png "image.png")

image.png

io.dongtai.iast.core.init.impl.TransformEngine#start 中调用`java.lang.instrument.Instrumentation#addTransformer(java.lang.instrument.ClassFileTransformer, boolean)`进行类文件转换（重写class）

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/154013d4-4d56-fcbf-ab37-a7e453c266fe.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/154013d4-4d56-fcbf-ab37-a7e453c266fe.png "image.png")

image.png

io.dongtai.iast.core.bytecode.IastClassFileTransformer 这部分应该是dongtai的核心

IastClassFileTransformer实现了java.lang.instrument.ClassFileTransformer接口的transform函数

java

```
byte[]
transform(  ClassLoader         loader,
            String              className,
            Class<?>            classBeingRedefined,
            ProtectionDomain    protectionDomain,
            byte[]              classfileBuffer)
    throws IllegalClassFormatException;
```

> Once a transformer has been registered with addTransformer, the transformer will be called for every new class definition and every class redefinition. Retransformation capable transformers will also be called on every class retransformation. The request for a new class definition is made with ClassLoader.defineClass or its native equivalents. The request for a class redefinition is made with Instrumentation. redefineClasses or its native equivalents.

这个接口的作用在于：一旦使用java.lang.instrument.Instrumentation#addTransformer(java.lang.instrument.ClassFileTransformer, boolean)注册了转换函数之后，在jvm中每一次获取类定义或者类重定义时都会调用这个transform函数

也就是说，dongtai重写了所有jvm中存在的class字节码，看一下dongtai是怎么转换的

`io.dongtai.iast.core.init.impl.TransformEngine#start` 中调用addTransformer之后继续调用 `io.dongtai.iast.core.bytecode.IastClassFileTransformer#reTransform`

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/aaf4c684-5455-4a...