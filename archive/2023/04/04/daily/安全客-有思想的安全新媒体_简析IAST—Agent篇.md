---
title: 简析IAST—Agent篇
url: https://www.anquanke.com/post/id/288054
source: 安全客-有思想的安全新媒体
date: 2023-04-04
fetch_date: 2025-10-04T11:29:08.354093
---

# 简析IAST—Agent篇

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 简析IAST—Agent篇

阅读量**509100**

|评论**1**

发布时间 : 2023-04-03 16:30:46

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

## 一 IAST简单介绍

IAST(Interactive Application Security Testing)交互式应用程序安全测试，通过服务端部署Agent探针，流量代理/VPN或主机系统软件等方式，监控Web应用程序运行时函数执行并与扫描器实时交互，高效、精准的安全漏洞，是一种运行时灰盒安全测试技术。在分析并评估了业界主流的几家IAST产品后，发现IAST一般可以提供agent插桩检测、流量代理、流量信使等几种漏洞检测模式，其中除agent插桩模式外，其余几种检测模式与DAST被动漏洞扫描的原理一致，所以本篇文章我们主要分析agent插桩模式。

agent插桩的检测模式，一般分为主动和被动模式。那怎么理解agent插桩模式呢？我们结合JavaAgent技术来做解释。-javaagent是java命令的一个参数，该参数可以指定一个jar包，该jar包内实现了一个premain()方法，在执行正常程序的main()方法会先运行这个premain方法，是一个JVM层做功能增强的机制。说到java的功能增强，可以想到动态代理、Spring AOP、拦截器等技术，这些方式主要是在函数执行前后做一些增强逻辑，而JavaAgent可以直接获取到类加载前的字节码，再结合一些字节码修改技术，从而通过修改字节码来增强函数功能。通过这种方式，我们可以获取类、方法的一些信息，比如类名、方法名、参数、返回值等，同时也可以做一些拦截操作。所以，这项技术通常被用于实现调用链监控、日志采集等组件，而在安全方向的应用，IAST和RASP则是典型例子。

对于IAST来说，agent的检测模式通常被分为被动模式和主动检测模式。在被动模式下，agent可以动态获取一次请求的调用链、数据流等信息，基于获取的信息，IAST可以做一些基于污点追踪的白盒分析，从而检测该次请求的调用链中是否存在漏洞；在主动模式下，agent会hook一些危险函数，当一次请求触发到这些危险函数后，agent会将该次请求发送给IAST server端，并使用DAST能力发送攻击payload做主动验证。基于这些特性，IAST非常适合融入到DevOps的测试环节，在业务测试完成正常功能逻辑测试工作的同时，无感知的进行一些安全漏洞的检测。

* IAST被动检测模式
  ![]()
* IAST主动检测模式
  ![]()

这里我们主要研究一下IAST被动检测模式的细节，该检测模式也是IAST首推的检测模式。在上文提到，在被动检测模式下，agent主要用来做Web应用程序的数据采集并传至分析引擎，分析引擎做白盒分析。接下来，我们就实际的去实现一个agent，对一次请求做调用链数据采集。

还是以Java为例，实现一个agent需要掌握以下几种技术：

1. JavaAgent技术。
2. 字节码修改技术。主流的字节码修改工具有javassist、Byte Buddy和ASM等，其中javassit的使用比较简单，ASM则较为复杂且需要对.class文件结构、变量表等底层知识有一定的理解，但是其性能更优。我们这里只是写一个简单讲解一下agent的工作逻辑，所以我们选择使用javassist。
3. JVM类加载机制。
4. ThreadLocal

接下来，我们来简单写几个例子介绍一下这几项技术。

## 二 JavaAgent

前文已经基本介绍了JavaAgent这项技术，而实际实现一个JavaAgent需要以下几个步骤：

1. 定义一个MANIFEST.MF文件，必须包含Premain-Class选项，通常也会加入Can-Redfine-Classes和Can-Restransform-Classes选项。
2. 创建一个Premain-Class指定的类，类中包含premain方法，方法逻辑由用户自己去编写。
3. 将premain的类和MANIFEST.MF文件打成jar包。
4. 使用-javaagent参数，启动要代理的方法。

在执行以上步骤后，JVM会先执行premain()方法，大部分类加载前都通过该方法。

通过上面的步骤，我们来接下来实现一个简单的JavaAgent

### 2.1 包含premain方法的agent类

先给出一个例子

```
 public class AgentDemo {

     public static void premain(String args, Instrumentation inst){
         inst.addTransformer(new DefinTransformer(), true);
     }

     static class DefinTransformer implements ClassFileTransformer{

         public byte[] transform(ClassLoader loader, String className, Class<?> classBeingRedefined, ProtectionDomain protectionDomain, byte[] classfileBuffer) throws IllegalClassFormatException {
             System.out.println("premain load class:" + className);
             return new byte[0];
         }
     }

 }
```

解释一下以上代码，在类加载时，JVM会先执行premain()方法，方法中的`inst.addTransformer(new DefinTransformer(), true)`是添加一个ClassFileTransformer接口的实现类， 该类实现一个transform()方法，该方法中我们可以写一些自己的逻辑。可以看到transform的入参有被加载类的类加载器、类名、字节码等信息，返回类型则是byte[]，这样我们可以返回修改后的字节码，之后JVM加载的就是我们修改过后的字节码了，这里我们简单打印一下加载中的类名。

现在我们还缺少一个MANIFEST.MF文件，使用maven插件可以在打包时自动生成。

```
 <plugin>
        <groupId>org.apache.maven.plugins</groupId>
         <artifactId>maven-jar-plugin</artifactId>
         <version>3.1.0</version>
         <configuration>
           <archive>
             <!--自动添加META-INF/MANIFEST.MF -->
             <manifest>
               <addClasspath>true</addClasspath>
             </manifest>
             <manifestEntries>
               <Premain-Class>org.example.agent.AgentDemo</Premain-Class>
               <Agent-Class>org.example.agent.AgentDemo</Agent-Class>
               <Built-By>dgcat</Built-By>
               <Can-Redefine-Classes>true</Can-Redefine-Classes>
               <Can-Retransform-Classes>true</Can-Retransform-Classes>
             </manifestEntries>
           </archive>
         </configuration>
 </plugin>
```

Premain-Class和Agent-Class写agent类型的全类名即可，如果需要添加其他配置，可在`<manifestEntries>`中添加对应标签和值，这里不再多做介绍。

### 2.2 运行agent

写一个用于测试的类并编译成.class。

```
 package org.example.test;
 public class MainTest {

     public static void main(String[] args) throws InterruptedException {
         System.out.println("start");
         Thread.sleep(3000);
         System.out.println("end");
     }
 }
```

使用-javaagent参数执行agent包并运行：

```
java -javaagent:./agentdemo-1.0.jar org.example.test.MainTest
```

输出结果如下：
![]()

可以看到不止我们自己编写的测试类，有很多jdk中的类也被打印出来了，可见JavaAgent功能还是比较强大的。

## 三 Javassist

Javassist可以实现动态创建类、添加类的属性和方法，修改类的方法等操作。这里我们不需要做添加方法、属性等操作，只需要获取类名、方法名、入参、出餐等信息，所以这里仅仅叙述如何获取这些信息，至于其他多的功能，可参考：<https://bugstack.cn/md/bytecode/javassist/2020-04-19-%E5%AD%97%E8%8A%82%E7%A0%81%E7%BC%96%E7%A8%8B%EF%BC%8CJavassist%E7%AF%87%E4%B8%80%E3%80%8A%E5%9F%BA%E4%BA%8Ejavassist%E7%9A%84%E7%AC%AC%E4%B8%80%E4%B8%AA%E6%A1%88%E4%BE%8Bhelloworld%E3%80%8B.html>

### 3.1 信息获取

**获取类**

```
ClassPool pool = ClassPool.getDefault();
// 获取类
CtClass ctClass = pool.get("org.dgcat.demo.javassist.HelloDemo");
String clazzName = ctClass.getName();
```

通过类名获取类的信息，也包括类里面一些其他获取属性的操作，比如：ctClass.getSimpleName()、ctClass.getAnnotations() 等。

**获取方法**

```
CtMethod ctMethod = ctClass.getDeclaredMethod("test");
String methodName = ctMethod.getName();
```

通过 getDeclaredMethod 获取方法的 CtMethod 的内容。之后就可以获取方法的名称等信息。

**方法信息**

```
MethodInfo methodInfo = ctMethod.getMethodInfo();
```

MethodInfo 中包括了方法的信息；名称、类型等内容。

**方法类型**

```
boolean isStatic = (methodInfo.getAccessFlags() & AccessFlag.STATIC) != 0;
```

通过 methodInfo.getAccessFlags() 获取方法的标识，判断方法是否为静态方法。因为静态方法会影响后续的参数名称获取，静态方法第一个参数是 this ，需要排除。

**入参信息**

```
// 入参信息
CodeAttribute codeAttribute = methodInfo.getCodeAttribute();
LocalVariableAttribute attr = (LocalVariableAttribute) codeAttribute.getAttribute(LocalVariableAttribute.tag);
// 获取入参名
String name = attribute.variableNameByIndex(i);
//入参类型
CtClass[] parameterTypes = ctMethod.getParameterTypes();
```

**返回信息**

```
CtClass returnType = ctMethod.getReturnType();
```

**修改方法**

```
ctClass.insertBefore("{System.out.println(1);}");
ctClass.insertAfter("{System.out.println(1);}");
```

## 四 agent实现

### 4.1 写在最前

在实现一个agent前还有几个问题需要注意：

**agent隔离加载**

因为我们现在需要实现具有一定复杂逻辑的agent，所以我们不可避免的需要引入一些其他jar包做功能实现，而如果我们的agent与正常应用引入了同一个jar包的不同版本，这将发生jar包冲突，对正常应用产生未知影响。

要解决这个问题，我们需要自定义类加载器来加载agent中的类，因为在java中通过不同的类加载器加载同一个类是不一样的，一个类只能引用同一类加载器加载的类及其父加载器加载的类，更多的细节大家也可以去详细了解一下Java的类加载机制，java的很多框架如spring都有实现自己的类加载器实现隔离加载来解决冲突的问题。

所以我们现在需要将这个agent分为两个jar包，一个是agent包，另一个core包。agent包实现一个premain()方法、Tranformer类等，并且使用自定义类加载器加载core包，而core包是我们编写的修改字节码的逻辑。但这样还会有一个问题，我们修改后的正常代码，需要调用core包中的方法，而core包是自定义类加载器加载的，正好代码的类一般是应用类加载器加载的，所以正常代码这时候无法调用core中的方法。所以，还需要将正常代码调用的方法单独拆分出一个jar包，该包使用BootstrapClassLoader加载，该类加载器是类加载器的顶层，其加载的类可以被所有的类加载器加载的类引用，我们将这个jar命名为spy。

**标识一次请求的调用链**

在解决了一些类加载上的问题后，我们还有一个问题需要解决。因为我们需要对不同请求采集不同的调用链，那么如何当一次请求触发到一个方法后，我们如何标识这次方法调用是属于那次请求呢？这也是我们方法调用能否形成链路的关键。

这里我们借用ThreadLocal。ThreadLocal叫做线程变量，即ThreadLocal中填入的变量只属于当前线程，我们知道不同的请求实际对应不同的线程，那用独属于当前线程的变量标识一次请求是最合适不过了。

ThreadLocal的使用也比较简单，如下：

```
public class ThreadLocaDemo {

    private static ThreadLocal<String> localVar = new ThreadLocal<String>();

    public static void main(String[] args) {
        // 设置变量
         localVar.set("local_A");
         // 获取变量
         localVar.get();

    }
}
```

### 4.2 Agent包实现

首先，我们的项目分为三部分，agent、core和spy。
![]()

接下来，我们来实现一下agent包里的逻辑，agent主要实现两个类，一个是自定义的ClassLoader，一个是agent入口类。ClassLoader主要重写loadclass方法主要是注意一些jdk本身的类还是需要正常加载，第二就是spy包的类需要使用BootstrapClassLoader加载，其他的就不再多说。agent类实现permain()方法，主要是分别用不同的类加载器加载core和spy两个jar包，以及为instrumentation添加Transformer类。具体如下：

```
public static void premain(String agentOps, Instrumentation instrumentation) {
        try {
            // 启动类加载器加载spy
            File agentSpyFile = new File(SPY_JAR);
            if (!agentSpyFile.exists()) {
                System.out.println("Spy jar file does not exist: " + agentSpyFile);
                return;
            }
            instrumentation.appendToBootstrapClassLoaderSearch(new JarFile(agentSpyFile));

            //...