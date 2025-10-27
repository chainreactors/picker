---
title: Java 反序列化之 XStream 反序列化
url: https://www.secpulse.com/archives/202377.html
source: 安全脉搏
date: 2023-06-28
fetch_date: 2025-10-04T11:46:45.565032
---

# Java 反序列化之 XStream 反序列化

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

# Java 反序列化之 XStream 反序列化

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-06-27

19,716

## 0x01 XStream 基础

### XStream 简介

XStream 是一个简单的基于 Java 库，Java 对象序列化到 XML，反之亦然(即：可以轻易的将 Java 对象和 XML 文档相互转换)。

### 使用 XStream 实现序列化与反序列化

下面看下如何使用 XStream 进行序列化和反序列化操作的。

先定义接口类

**IPerson.java**

```
public interface IPerson {
    void output();
}
```

接着定义 Person 类实现前面的接口：

```
public class Person implements IPerson {
    String name;
    int age;

    public void output() {
        System.out.print("Hello, this is " + this.name + ", age " + this.age);
    }
}
```

XStream 序列化是调用 `XStream.toXML()` 来实现的：

```
public class Serialize {
    public static void main(String[] args) {
        Person p = new Person();
        p.age = 6;
        p.name = "Drunkbaby";
        XStream xstream = new XStream(new DomDriver());
        String xml = xstream.toXML(p);
        System.out.println(xml);
    }
}
```

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202306251455181.png)

XStream 反序列化是用过调用 `XStream.fromXML()` 来实现的，其中获取 XML 文件内容的方式可以通过 `Scanner()` 或 `FileInputStream` 都可以：

**Deserialize.java**

```
import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.DomDriver;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Deserialize {
    public static void main(String[] args) throws FileNotFoundException {
//        String xml = new Scanner(new File("person.xml")).useDelimiter("\\Z").next();
        FileInputStream xml = new FileInputStream("G:\\OneDrive - yapuu\\Java安全学习\\JavaSecurityLearning\\JavaSecurity\\XStream\\XStream\\XStream-Basic\\src\\main\\java\\person.xml");
        XStream xstream = new XStream(new DomDriver());
        Person p = (Person) xstream.fromXML(xml);
        p.output();
    }
}
```

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202306251455183.png)

### XStream 几个部分

XStream 类图，参考[XStream 源码解析](https://www.hetianlab.com/https%3A//www.jianshu.com/p/387c568faf62)：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202306251455185.png)

主要分为四个部分：

【---- 帮助网安学习，以下所有学习资料免费领！领取资料加 we~@x：yj009991，备注 “安全脉搏” 获取！】
① 网安学习成长路径思维导图
② 60 + 网安经典常用工具包
③ 100+SRC 漏洞分析报告
④ 150 + 网安攻防实战技术电子书
⑤ 最权威 CISSP 认证考试指南 + 题库
⑥ 超 1800 页 CTF 实战技巧手册
⑦ 最新网安大厂面试题合集（含答案）
⑧ APP 客户端安全检测指南（安卓 + IOS）

#### MarshallingStrategy 编码策略

* marshall : object->xml 编码
* unmarshall : xml-> object 解码

两个重要的实现类：

* `com.thoughtworks.xstream.core.TreeMarshaller` : 树编组程序
* 调用 Mapper 和 Converter 把 XML 转化成 Java 对象

> 其中的 start 方法开始编组

其中调用了 `this.convertAnother(item)` 方法

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202306251455186.png)

> convertAnother 方法的作用是把 XML 转化成 Java 对象。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202306251455187.png)

#### Mapper 映射器

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202306251455188.png)

简单来说就是通过 mapper 获取对象对应的类、成员、Field 属性的 Class 对象，赋值给 XML 的标签字段。

#### Converter 转换器

XStream 为 Java 常见的类型提供了 Converter 转换器。转换器注册中心是 XStream 组成的核心部分。

转换器的职责是提供一种策略，用于将对象图中找到的特定类型的对象转换为 XML 或将 XML 转换为对象。

简单地说，就是输入 XML 后它能识别其中的标签字段并转换为相应的对象，反之亦然。

转换器需要实现 3 个方法，这三个方法分别是来自于 `Converter` 类以及它的父类 `ConverterMatcher`

* canConvert 方法：告诉 XStream 对象，它能够转换的对象；
* marshal 方法：能够将对象转换为 XML 时候的具体操作；
* unmarshal 方法：能够将 XML 转换为对象时的具体操作；

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202306251455189.png)

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202306251455190.png)

具体参考：<http://x-stream.github.io/converters.html>

这里告诉了我们针对各种对象，XStream 都做了哪些支持。

#### EventHandler 类

EventHandler 类为动态生成事件侦听器提供支持，这些侦听器的方法执行一条涉及传入事件对象和目标对象的简单语句。

EventHandler 类是实现了 InvocationHandler 的一个类，设计本意是为交互工具提供 beans，建立从用户界面到应用程序逻辑的连接。

EventHandler 类定义的代码如下，其含有 target 和 action 属性，在 `EventHandler.invoke()->EventHandler.invokeInternal()->MethodUtil.invoke()` 的函数调用链中，会将前面两个属性作为类方法和参数继续反射调用：

```
public class EventHandler implements InvocationHandler {
    private Object target;
    private String action;
    ...

    public Object invoke(final Object proxy, final Method method, final Object[] arguments) {
        ...
                return invokeInternal(proxy, method, arguments);
        ...
    }

    private Object invokeInternal(Object proxy, Method method, Object[] arguments) {
        ...

                Method targetMethod = Statement.getMethod(
                             target.getClass(), action, argTypes);
                ...
                return MethodUtil.invoke(targetMethod, target, newArgs);
            }
            ...
    }

    ...
}
```

这里重点看下 `EventHandler.invokeInternal()` 函数的代码逻辑，如注释：

```
private Object invokeInternal(Object var1, Method var2, Object[] var3) {
//-------------------------------------part1----------------------------------
//作用:获取interface的name,即获得Comparable,检查name是否等于以下3个名称
        String var4 = var2.getName();
        if (var2.getDeclaringClass() == Object.class) {
            if (var4.equals("hashCode")) {
                return new Integer(System.identityHashCode(var1));
            }

            if (var4.equals("equals")) {
                return var1 == var3[0] ? Boolean.TRUE : Boolean.FALSE;
            }

            if (var4.equals("toString")) {
                return var1.getClass().getName() + '@' + Integer.toHexString(var1.hashCode());
            }
        }
//-------------------------------------part2----------------------------------
//貌似获取了一个class和object
        if (this.listenerMethodName != null && !this.listenerMethodName.equals(var4)) {
            return null;
        } else {
            Class[] var5 = null;
            Object[] var6 = null;
            if (this.eventPropertyName == null) {...