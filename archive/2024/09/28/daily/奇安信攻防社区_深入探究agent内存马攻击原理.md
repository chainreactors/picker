---
title: 深入探究agent内存马攻击原理
url: https://forum.butian.net/share/3775
source: 奇安信攻防社区
date: 2024-09-28
fetch_date: 2025-10-06T18:20:00.852398
---

# 深入探究agent内存马攻击原理

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

### 深入探究agent内存马攻击原理

* [漏洞分析](https://forum.butian.net/topic/48)

agent内存马的本质就是通过agentmain方法，修改正在运行的Java类，在其中插入恶意直接码，从而达到命令执行。

一、什么是agent内存马
=============
Java agent本质上可以理解为一个插件，该插件就是一个精心提供的jar包。只是启动方式和普通Jar包有所不同，对于普通的Jar包，通过指定类的main函数进行启动。但是Java Agent并不能单独启动，必须依附在一个Java应用程序运行，在面向切面编程方面应用比较广泛。 Java agent 的jar包通过JVMTI（JVM Tool Interface）完成加载，最终借助JPLISAgent（Java Programming Language Instrumentation Services Agent）完成对目标代码的修改。主要功能如下：
- 可以在加载java文件之前做拦截把字节码做修改
- 可以在运行期将已经加载的类的字节码做变更
- 比如我们用到过的Jcoco，Arthas, chaosblade等，都是使用Java agent技术来实现
agent内存马的本质就是通过agentmain方法，修改正在运行的Java类，在其中插入恶意直接码，从而达到命令执行
二、前置知识
======
Instrumentation类
----------------
`Instrumentation` 是 `JVMTIAgent`（JVM Tool Interface Agent）的一部分，Java agent通过这个类和目标 `JVM` 进行交互，从而达到修改数据的效果
### addTransformer方法
该方法定义如下
```java
void addTransformer(ClassFileTransformer transformer);
```
`addTransformer 方法`来用于注册`Transformer（转换器`），所以我们可以通过编写实现 ClassFileTransformer 接口的类，来注册我们自己的转换器，在`agent`\*\*拦截修改\*\*类时，便会调用我们所传入\*\*转换器对象\*\*的`transformer方法`
> Instrumentation 中含有名为 transformer 的 Class 文件转换器，在agent对类进行拦截修改时，便调用该方法，该方法可以改变二进制流的数据
### getAllLoadedClasses方法
该方法定义如下
```java
Class[] getAllLoadedClasses();
```
我们可以通过`getAllLoadedClasses 方法`获取所有已加载的 Class，我们可以通过遍历 Class 数组来寻找我们需要重定义的 class
一个简单的demo
`Agdemo.java`
```java
import java.lang.instrument.Instrumentation;
public class Agdemo {
public static void premain(String agentArgs,Instrumentation ins){
Class[] classes=ins.getAllLoadedClasses();
for(Class c:classes){
System.out.println(c.getName());
}
}
}
```
其他文件仍与上文相同
执行以下命令运行
```shell
java -javaagent:agent.jar=111 -jar hello.jar
```
成功输出所有已加载的类
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-4dd5c089d499f2ec198983bcea8c379bd5d43394.png)
### retransformClasses方法
该方法定义如下
```java
void retransformClasses(Class<?>... classes) throws UnmodifiableClassException;
```
`retransformClasses 方法`可以重新定义已加载的 `class` ，当我们想修改一个已经加载的类的时候可以调用该函数，来重新触发这个`Transformer`\*（也就是addTransformer注册的转换器的transform方法）\*的拦截，以此达到对已加载的类进行字节码修改的效果
VirtualMachine类
---------------
`VirtualMachine` 可以来实现获取系统信息，内存dump、现成dump、类信息统计（JVM加载的类），常用的方法有\*\*LoadAgent\*\*，\*\*Attach\*\* 和 \*\*Detach\*\* 。
\*\*Attach\*\* ：通过jvm的id连接jvm
```java
VirtualMachine vm = VirtualMachine.attach(v.id());
//v为VirtualMachineDescriptor对象，下文有讲
```
\*\*loadAgent\*\*：向Attach方法获取的jvm注册一个代理程序agent
```java
String path = "AgentMain.jar的路径";
vm.loadAgent(path)
```
\*\*Detach\*\*：从 JVM 上面解除一个代理(agent)
VirtualMachineDescriptor类
-------------------------
`VirtualMachineDescriptor` 是一个描述虚拟机的容器类，可以通过VirtualMachine.list()获取，
```java
List<VirtualMachineDescriptor> list = VirtualMachine.list();
```
常用的方法有
\*\*displayName()\*\*：获取当前jvm运行的主类名
\*\*id()\*\*：获取\*\*当前jvm的`id`\*\*，得到`id`后就可以用`VirtualMachine.attach()`方法通过`id`获得该虚拟机，然后再使用`VirtualMachine.loadAgent()`方法对该`id`注册agent
三、两种agent
=========
Java agent一共分为两种:
\*\*premain 方法\*\*：在jvm启动时执行（该特性在 jdk 1.5 之后才有）
\*\*agentmain方法\*\*：在jvm加载后执行（该特性在 jdk 1.6 之后才有）
> 普通的 Java 类是以 main 函数作为入口，Java Agent 的入口则是 premain 和 agentmain
premain 方法
----------
我们先创建一个类实现 `premain 方法`
`Agdemo.java`
```java
import java.lang.instrument.Instrumentation;
public class Agdemo {
public static void premain(String agentArgs,Instrumentation ins){
Class[] classes=ins.getAllLoadedClasses();
System.out.println(agentArgs);
for(Class c:classes){
System.out.println(c.getName()); //测试上文的getAllLoadedClasses方法
}
}
}
```
同时创建对应的清单（\*\*main fest\*\*）
`agent.mf` （注意最后一行要为空格）
```mf
Manifest-Version: 1.0
Premain-Class: Agdemo
```
这里补充下mf文件的知识，大致选项如下
```list
Main-Class：包含 main 方法的类（类的全路径名）
Premain-Class: 包含 premain 方法的类（类的全路径名）
Agent-Class: 包含 agentmain 方法的类（类的全路径名）
Boot-Class-Path: 设置引导类加载器搜索的路径列表。查找类的特定于平台的机制失败后，引导类加载器会搜索这些路径。按列出的顺序搜索路径。列表中的路径由一个或多个空格分开。路径使用分层 URI 的路径组件语法。如果该路径以斜杠字符（“/”）开头，则为绝对路径，否则为相对路径。相对路径根据代理 JAR 文件的绝对路径解析。忽略格式不正确的路径和不存在的路径。如果代理是在 VM 启动之后某一时刻启动的，则忽略不表示 JAR 文件的路径。（可选）
Can-Redefine-Classes: true表示能重定义此代理所需的类，默认值为 false（可选）
Can-Retransform-Classes: true 表示能重转换此代理所需的类，默认值为 false （可选）
Can-Set-Native-Method-Prefix: true表示能设置此代理所需的本机方法前缀，默认值为 false（可选）
```
然后使用javac将其编译为class文件
```shell
javac Agdemo.java
```
然后将class文件和mf一起打包为jar，获取代理程序 agent.jar，即为我们的代理程序
```shell
jar cvfm agent.jar agent.mf Agdemo.class
```
然后创建我们被代理的类
`Hello.java`
```java
public class Hello {
public static void main(String[] args) {
System.out.println("Hello,World");
}
}
```
然后创建清单 `Hello.mf`
```mf
Manifest-Version: 1.0
Main-Class: Hello
```
同样将其编译为class文件
```shell
javac Hello.java
```
然后和清单一起打包为jar文件，我们得到被代理的程序 `hello.jar`
```shell
jar cvfm hello.jar Hello.mf Hello.class
```
然后使用java命令，使用`agent代理`运行 `hell.jar`
```shell
java -javaagent:agent.jar=114514 -jar hello.jar
```
成功运行
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-aa5d0e6672194f37c6a057af97b00b9f3fe4deeb.png)
agent方法
-------
`agent代理`的设置与`premain`略有不同，需要用到`VirtualMachine 和 VirtualMachineDescriptor类，`获取其jvm的id，然后对其注册`agent代理`
具体流程如下
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-2942e5c1046c8b21174205b404c169585ba52eeb.png)
我们同样需要创建一个`实现agentmain方法`的类
`Agenttest.java`
```java
import java.lang.instrument.Instrumentation;
public class Agenttest {
public static void agentmain(String agentArgs, Instrumentation ins) {
ins.addTransformer(new MyTransformer(),true); //MyTransformer()类是需要自己编写的
}
}
```
编写一个实现了`ClassFileTransformer`的转换器类
`MyTransformer.java`
```java
import java.lang.instrument.ClassFileTransformer;
import java.lang.instrument.IllegalClassFormatException;
import java.security.ProtectionDomain;
public class MyTransformer implements ClassFileTransformer {
public byte[] transform(ClassLoader loader, String className, Class<?> classBeingRedefined, ProtectionDomain protectionDomain, byte[] classfileBuffer) throws IllegalClassFormatException {
System.out.println(className);
return classfileBuffer;
}
}
```
然后创建清单 `agentmain.mf`（注意要留一行空格）
```mf
Manifest-Version: 1.0
Can-Redefine-Classes: true
Can-Retransform-Classes: true
Agent-Class: Agenttest
```
然后编译并打包，获得代理程序 `AgentMain.jar`
```php
javac Agenttest.java
javac MyTransformer.java
jar cvfm AgentMain.jar agmain.mf Agenttest.class MyTransformer.class
```
下一步编写我们被代理的类
这个类中需要导入`VirtualMachine 类与VirtualMachineDescriptor类`
这里有些坑：
> mac环境下jdk是能直接找到 VirtualMachine 类
>
> 但是在windows中jdk中无法找到，可以手动将jdk目录下的lib目录中的tools.jar添加进当前工程的Libraries中
>
> 并且在Java9及以后的版本不允许SelfAttach(即无法attach自身的进程)，会报错`Can not attach to current VM`，我们在运行时添加参数 `-Djdk.attach.allowAttachSelf=true`即可
创建被代理的类 `Hello.java`
```java
import com.sun.tools.attach.VirtualMachine;
import com.sun.tools.attach.VirtualMachineDescriptor;
import java.util.List;
public class Hello {
public static void main(String[] args) throws Exception{
String path = "AgentMain.jar的路径";
List<VirtualMachineDescriptor> list = VirtualMachine.list();
for (VirtualMachineDescriptor v:list){
System.out.println(v.displayName());
if (v.displayName().contains("Hello")){
// 将 jvm 虚拟机的 pid 号传入 attach 来进行远程连接
VirtualMachine vm = VirtualMachine.attach(v.id());
// 将我们的 agent.jar 发送给虚拟机
vm.loadAgent(path);
vm.detach();
}
}
}
}
```
成功运行
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-cb7aff795b3b88d0164e6475c22055f67f2a71dc.png)
这里解释下为什么会输出上面四个类
> 当一个类被加载到 JVM 中时，类加载器会通知 Java 虚拟机，然后 Java 虚拟机会调用注册的 ClassFileTransformer 实现类的 transform 方法来处理这个类
1. Hello类就是我们定义的入口类
2. `java.lang.IndexOutOfBoundsExcept...