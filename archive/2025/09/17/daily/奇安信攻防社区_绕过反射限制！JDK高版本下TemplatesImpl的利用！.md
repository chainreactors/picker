---
title: 绕过反射限制！JDK高版本下TemplatesImpl的利用！
url: https://forum.butian.net/share/4551
source: 奇安信攻防社区
date: 2025-09-17
fetch_date: 2025-10-02T20:13:46.313691
---

# 绕过反射限制！JDK高版本下TemplatesImpl的利用！

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

### 绕过反射限制！JDK高版本下TemplatesImpl的利用！

* [CTF](https://forum.butian.net/topic/52)
* [渗透测试](https://forum.butian.net/topic/47)

《java安全漫谈》中讲到过利用TemplatesImpl链加载字节码，当时要求恶意类需要继承AbstractTranslet，至于为什么当时并没有说清，现在再聊下这个，以及如何不需要AbstractTranslet也能成功打通这条链子，这也可以为JDK高版本下继续使用TemplatesImpl奠定基石。

p牛在《java安全漫谈》中讲到过利用`TemplatesImpl`链加载字节码，当时要求恶意类需要继承`AbstractTranslet`，至于为什么当时并没有说清，现在再聊下这个，以及如何不需要`AbstractTranslet`也能成功打通这条链子，这也可以为JDK高版本下继续使用`TemplatesImpl`奠定基石。
本文为学习之作，其中难免会有理解差错，还请见谅，发出来也是参考的作用。
- - - - - -
### 回顾TemplatesImpl利用链
这条利用链如下：
TemplatesImpl#getOutputProperties() -&gt; TemplatesImpl#newTransformer() -&gt; TemplatesImpl#getTransletInstance() -&gt; TemplatesImpl#defineTransletClasses() -&gt; TransletClassLoader#defineClass()
> 在《java安全漫谈》中p牛给出TemplatesImpl类里重写了defineClass方法，并且这里没有显式地声明其定义域。Java中默认情况下，如果一个 方法没有显式声明作用域，其作用域为default。所以也就是说这里的defineClass由其父类的 protected类型变成了一个default类型的方法，可以被类外部调用。
因此，因为无法在外部直接访问`ClassLoader#defineClass`，所以才利用了`TemplatesImpl`“借船出海”。
在利用时，我们需要在几个参数上进行操作，分别是：
- `\_bytecodes`
- `\_name`
- `\_tfactory`
下面再来探究下为什么。
- - - - - -
![](https://cdn.nlark.com/yuque/0/2025/png/50620181/1756174649270-b796e87f-a93c-46bd-a099-bab511f25af3.png)
在`com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl#getTransletInstance`有如下三个注意的点。
在456、457行存在实例化操作，如果数组和下标可控，则可以实现代码执行。
有个前提是`\_name`不能为空，此外对于`\_class`为空的情况，会走`defineTransletClasses()`方法。
跟进`defineTransletClasses()`方法。
![](https://cdn.nlark.com/yuque/0/2025/png/50620181/1756175132063-6ff5d976-d9fb-45c1-86c4-e4c43bdac0e6.png)
在该方法中，有几个限制条件。首先是`\_bytecodes`不能为空，因为在415行会采用`defineClass`进行加载字节码。
然后`\_tfactory`不能为空，这是为了生成`loader`，对于工厂类可以用`com.sun.org.apache.xalan.internal.xsltc.trax.TransformerFactoryImpl#TransformerFactoryImpl`。
这段代码的作用是给`\_class`数组赋值。
![](https://cdn.nlark.com/yuque/0/2025/png/50620181/1756175304596-2578fc21-f43f-439a-afdc-b35dfef31b6e.png)
![](https://cdn.nlark.com/yuque/0/2025/png/50620181/1756175327454-f76567f5-4eb7-4ae4-9e77-7d922f910512.png)
判断父类是否是`com.sun.org.apache.xalan.internal.xsltc.runtime.AbstractTranslet`，如果是赋值数组下标。
对于数组下标`\_transletIndex`要求也比较严格，如果该类不是`AbstractTranslet`子类，则会抛出异常。
于是基本的TemplatesImpl的利用链所使用的恶意类是`AbstractTranslet`的子类了。
![](https://cdn.nlark.com/yuque/0/2025/png/50620181/1756175738923-2e7883c2-c25d-4f17-b388-031ad12d6568.png)
![](https://cdn.nlark.com/yuque/0/2025/png/50620181/1756175753961-5b7309e8-be86-4064-aa58-3c4f87228089.png)
这一块就是`TemplatesImpl#getOutputProperties() -> TemplatesImpl#newTransformer()`,至于如何触发`getOutputProperties()`可以通过触发getter、toString或者是直接`newTransformer`。
![](https://cdn.nlark.com/yuque/0/2025/png/50620181/1756176082044-78a83a1e-72fc-4cea-99f5-9cee8a0fa309.png)
![](https://cdn.nlark.com/yuque/0/2025/png/50620181/1756176071889-b783e323-2bfa-48c3-b2ea-172e1d9fe845.png)
于是最基本的利用链如上所示。当前JDK版本为\*\*1.8.0\\_411\*\*。
- - - - - -
### JDK17以后利用的问题
那我们升到JDK18呢？利用链是否还可以使用。
![](https://cdn.nlark.com/yuque/0/2025/png/50620181/1756176313714-00a7e374-e950-43be-b462-bf7b409208b7.png)
给我们抛出了一个这样异常。
原因在于，从\*\*JDK9\*\*开始，Java引入了\*\*JPMS（Java Platform Module System，模块系统）\*\*。具体体现为：
- \*\*内部API封装\*\*：以前可以随意地去调用`com.sun.\*`等内部类，但在JDK17之后，这些类已经被模块系统强封装，默认不可以访问。
- \*\*强封装机制\*\*：模块之间的可见性由`module-info.java`描述，如果某个包没有`exports`，外部模块就无法直接访问。
- \*\*反射限制\*\*：在JDK8及之前，常常通过`setAccessible(true)`来绕过`private`限制，反射访问类的私有字段或构造函数。但是在JDK17以上，即使使用`setAccessible(true)`，也会被`InaccessibleObjectException`拦截，除非手动添加JVM参数`--add-opens`开放模块或者使用`Java Agent/Instrumentation`来打破封装。
> [从JDK8迁移到更高版本的JDK需要注意的点](https://docs.oracle.com/en/java/javase/17/migrate/migrating-jdk-8-later-jdk-releases.html#GUID-7BB28E4D-99B3-4078-BDC4-FC24180CE82B)
>
> &lt;font style="color:rgb(26, 24, 22);"&gt;一些工具和库使用反射来访问 JDK 的部分仅供内部使用。这种反射的使用会对安全性和JDK 的可维护性产生负面影响。为了帮助迁移，JDK 9 到 JDK 16 允许此反射继续，但会发出有关&lt;/font&gt;\*&lt;font style="color:rgb(26, 24, 22);"&gt;非法反射访问&lt;/font&gt;\*&lt;font style="color:rgb(26, 24, 22);"&gt;的警告。但是，JDK 17 是&lt;/font&gt;\*&lt;font style="color:rgb(26, 24, 22);"&gt;强封装的&lt;/font&gt;\*&lt;font style="color:rgb(26, 24, 22);"&gt;，因此默认情况下不再允许此反射。访问 API 的非公共字段和方法将抛出一个InaccessibleObjectException。
因此在高版本中，我们无法去直接利用`TemplatesImpl`了，并且`setAccessible`方法也被做了限制。
### 如何破局？
在Kcon2021Code大会上，哥斯拉作者`BeichenDream`提出了使用`Unsafe`类进行绕过`modle`的限制。“前人栽树，后人乘凉”，那下面来学习下`Unsafe`类的使用。
> &lt;font style="color:rgb(0, 0, 0);"&gt;Unsafe是位于sun.misc包下的一个类，主要提供一些用于执行低级别、不安全操作的方法，如直接访问系统内存资源、自主管理内存资源等，这些方法在提升Java运行效率、增强Java语言底层资源操作能力方面起到了很大的作用。但由于Unsafe类使Java语言拥有了&lt;/font&gt;\*\*&lt;font style="color:rgb(0, 0, 0);"&gt;类似C语言指针一样操作内存空间的能力&lt;/font&gt;\*\*&lt;font style="color:rgb(0, 0, 0);"&gt;，这无疑也增加了程序发生相关指针问题的风险。在程序中过度、不正确使用Unsafe类会使得程序出错的概率变大，使得Java这种安全的语言变得不再“安全”，因此对Unsafe的使用一定要慎重。&lt;/font&gt;
在`Unsafe`类的源码中，有这样一个关键的方法。
```java
public static Unsafe getUnsafe() {
Class var0 = Reflection.getCallerClass();
if (!VM.isSystemDomainLoader(var0.getClassLoader())) {
throw new SecurityException("Unsafe");
} else {
return theUnsafe;
}
}
```
获取`Unsafe`的反射调用者，判断其系统域加载器是否为JDK内部类。如果是返回`Unsafe`类，如果不是抛出异常，等待上层`catch`处理。
在`BeichenDream`的bypass代码中，利用了反射调用的方式：
```java
private static Unsafe getUnsafe() {
Unsafe unsafe = null;
try {
Field field = Unsafe.class.getDeclaredField("theUnsafe");
field.setAccessible(true);
unsafe = (Unsafe) field.get(null);
} catch (Exception e) {
throw new AssertionError(e);
}
return unsafe;
}
```
有个问题在于JDK17之后对`field.setAccessible`做了限制那是如何继续进行使用的呢？
> 但是需要注意，\*\*sun.misc和sun.reflect包可供所有JDK版本（包括JDK17）中的工具和库进行反射\*\*。
跟进分析`setAccessible`方法，首先调用`AccessibleObject`类的静态方法`checkPermission`，该方法检查当前的安全策略是否允许改变访问控制；如果不允许，会抛出`SecurityException`。&lt;/font&gt;
```java
public void setAccessible(boolean flag) {
AccessibleObject.checkPermission();
if (flag) checkCanSetAccessible(Reflection.getCallerClass());
setAccessible0(flag);
}
```
```java
static void checkPermission() {
@SuppressWarnings("removal")
SecurityManager sm = System.getSecurityManager();
if (sm != null) {
// SecurityConstants.ACCESS\_PERMISSION is used to check
// whether a client has sufficient privilege to defeat Java
// language access control checks.
sm.checkPermission(SecurityConstants.ACCESS\_PERMISSION);
}
}
```
接着，当设置非公共字段或方法的访问权限为true时，会调用`checkCanSetAccessible`方法，这个方法检查调用`setAccessible`方法的类是否有权限改变访问控制。`Reflection.getCallerClass`方法获取调用`setAccessible`方法的类，不包括匿名内部类。&lt;/font&gt;
跟进`java.lang.reflect.AccessibleObject#checkCanSetAccessible`方法，就可以看到，`callerModule`获取调用者的模块，`declaringModule`获取声明成员（方法或字段）的类的模块，如果调用者的模块与声明成员的类的模块相同，或者调用者是未知模块（`Object.class.getModule()`通常返回null），则允许访问。&lt;/font&gt;
原来模块相同或者是`Object.class.getModule`（未知模块）就可以绕过限制了啊！那就有操作空间了——我们知道`Unsafe`类相当于一个“指针”，而指针的作用在于指向变量的内存地址，那么我就可以通过Unsafe进行修改当前的`module`属性（实际上就是改内存地址吧），使其同`java.\*`下类的`module`属性一致来进行绕过。
如何实现？
在`Unsafe`类中，存在方法`getAndSetObject`，该方法是一个用于原子操作的方法，它主要用于在多线程环境下对对象的字段进行安全的更新操作，类似于反射赋值，可以利用其修改调用类的`module`。
```java
public final Object getAndSetObject(Object o, long offset, Object newValue) {
return theInternalUnsafe.getAndSetReference(o, offset, newValue);
}
```
这里直接给出代码，本质上是利用了`Unsafe`类修改当前类`module`位置改了到未知模块（`Object.class.getModule()`）类的`module`位置，这样就可以通过高版本JDK底层`java.lang.reflect.AccessibleObject#checkCanSetAccessible`方法中`module`校验机制。
```java
package com.test;
import com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl;
import com.sun.org.apache.xalan.internal.xsltc.trax.TransformerFactoryImpl;
import sun.misc.Unsafe;
import javax.xml.transform.TransformerConfigurationException;
import java.io.F...